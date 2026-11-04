"""Tuesday checks for AL05 stable insertion sorting."""

from copy import deepcopy
from main import insertion_sort, build_views
from ticket_data import TICKETS
from search_support import id_key, days_key
from pipeline_support import select_open_tickets


def assignment_checks():
    """Check stable sorting, counts, traces, and ownership contracts."""
    # Prepare the supplied Tuesday selection.
    source = deepcopy(TICKETS)
    original_source = deepcopy(source)
    selected = select_open_tickets(source, minimum_days=4,)

    # The supplied filter should preserve source order.
    assert [record["id"] for record in selected] == [
        "T403",
        "T405",
        "T402",
        "T406",
    ]
    assert all(record["id"] != "T404" for record in selected)
    assert all(record["id"] != "T401" for record in selected)

    #1 Test - Test the main Tuesday insertion-sort example.
    ordered, comparisons, moves, trace = insertion_sort(selected, key=days_key,)
    assert [record["id"] for record in ordered] == [
        "T406",
        "T402",
        "T403",
        "T405",
    ]
    assert [record["days_open"] for record in ordered] == [
        4,
        5,
        7,
        7,
    ]

    #2 Test - Expected Tuesday Teaching Counts
    assert comparisons == 6
    assert moves == 5

    #3 Test - Expected full ID order after each insertion.
    assert trace == [
        ["T403", "T405", "T402", "T406",],
        ["T402", "T403", "T405", "T406",],
        ["T406", "T402", "T403", "T405",],
    ]

    #4 Test - Check stable ties
    seven_day_ids = [record["id"] for record in ordered if record["days_open"] == 7]

    #5 Test - T403 appeared before T405 in the input. Stable sorting must preserve that relationship.
    assert seven_day_ids == ["T403", "T405",]

    #6 Test - Compare with Python's stable sorted()
    expected = sorted(selected, key=days_key,)
    assert ordered == expected
    assert [record["id"] for record in ordered] == [record["id"] for record in expected]

    #7 Test - Check empty input
    empty_ordered, empty_comparisons, empty_moves, empty_trace = (insertion_sort([], key=days_key,))
    assert empty_ordered == []
    assert empty_comparisons == 0
    assert empty_moves == 0
    assert empty_trace == []

    #8 Test - Check singleton input
    singleton = [{"id": "T900", "days_open": 3,}]
    (
    singleton_ordered, singleton_comparisons, singleton_moves, singleton_trace,) = insertion_sort(singleton, key=days_key,)
    assert singleton_ordered == singleton
    assert singleton_ordered is not singleton
    assert singleton_ordered [0] is singleton [0]
    assert singleton_comparisons == 0
    assert singleton_moves == 0
    assert singleton_trace == []

    #9 Test - Check already ordered input
    already_ordered = [
        {"id": "A", "days_open": 1},
        {"id": "B", "days_open": 2},
        {"id": "C", "days_open": 3},
    ]
    (
        ordered_result,
        ordered_comparisons,
        ordered_moves,
        ordered_trace,
    ) = insertion_sort(
        already_ordered, 
        key=days_key,
    )
    assert [
        record["id"] for record in ordered_result
    ] == ["A", "B", "C"]
    assert ordered_comparisons == 2
    assert ordered_moves == 0
    assert ordered_trace == [
        ["A", "B", "C"],
        ["A", "B", "C"],
    ]

    #10 Test - Check reverse input
    reverse_input = [
        {"id": "C", "days_open": 3},
        {"id": "B", "days_open": 2},
        {"id": "A", "days_open": 1},
    ]
    (
        reverse_result,
        reverse_comparisons,
        reverse_moves,
        reverse_trace,
    ) = insertion_sort(
        reverse_input,
        key=days_key,
    )
    assert [record["id"] for record in reverse_result] == ["A", "B", "C"]
    assert reverse_comparisons == 3
    assert reverse_moves == 3
    assert reverse_trace == [
        ["B", "C", "A"],
        ["A", "B", "C"],
    ]

    #11 Test - Check shuffled input with stable ties
    shuffled = [
        {"id": "A", "days_open": 7},
        {"id": "B", "days_open": 5},
        {"id": "C", "days_open": 7},
        {"id": "D", "days_open": 3},
    ]
    shuffled_original = deepcopy(shuffled)
    (
        shuffled_result,
        shuffled_comparisons,
        shuffled_moves,
        shuffled_trace,
    ) = insertion_sort(
        shuffled,
        key=days_key,
    )
    assert [record["id"] for record in shuffled_result] == ["D", "B", "A", "C"]
    assert [record["id"] for record in shuffled_result if record["days_open"] == 7] == ["A", "C",]
    assert shuffled_result == sorted(shuffled, key=days_key)
    assert shuffled_comparisons > 0
    assert len(shuffled_trace) == 3
    assert shuffled == shuffled_original

    #12 Test - Check sorting under a different named key
    id_result, _, _, _ = insertion_sort(selected, key=id_key)
    assert [record["id"] for record in id_result] == ["T402", "T403", "T405", "T406",]
    assert id_result == sorted(selected, key=id_key,)

    #13 Test - Check new-list and shared-record ownership
    assert ordered is not selected
    for record in ordered:
        matching_source_record = next(
            source_record for source_record in selected if source_record["id"] == record["id"])
        assert record is matching_source_record

    #14 Test = Check that source order and fields were not changed
    assert source == original_source
    assert [record["id"] for record in selected] == ["T403", "T405", "T402", "T406",]


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run tests without -O so assertions are enabled.")
    assignment_checks()
    print("AL05 Tuesday checks passed.")
