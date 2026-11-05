"""Tuesday checks for AL05 stable insertion sorting."""

from copy import deepcopy
from main import insertion_sort, build_views
from ticket_data import TICKETS
from search_support import id_key, days_key
from pipeline_support import select_open_tickets
from search_algorithms import linear_search, binary_search


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

    """Thursday: Build views at minimum days = 4"""
    (selected_at_4, display_at_4, search_at_4) = build_views(source, minimum_days=4,)

    # Test 1 - Check the selected source-order IDs.
    assert [record["id"] for record in selected_at_4] == [
        "T403",
        "T405",
        "T402",
        "T406",
    ]

    # Test 2 - Check the stable age-display order.
    assert [record["id"] for record in display_at_4] == [
        "T406",
        "T402",
        "T403",
        "T405",
    ]

    # Test 3 - Check the separate ID-search order.
    assert [record["id"] for record in search_at_4] == [
        "T402",
        "T403",
        "T405",
        "T406",
    ]

    # Test 4 - Check exact age ordering.
    assert [record["days_open"] for record in display_at_4] == [
        4,
        5,
        7,
        7,
    ]

    # Test 5 - Stable tie order must be preserved.
    assert [record["id"] for record in display_at_4 if record["days_open"] == 7] == [
        "T403",
        "T405",
    ]

    # Test 6 - The completed ticket must remain excluded.
    assert all(record["id"] != "T404" for record in selected_at_4)

    # Test 7 - The two-day open ticket does not meet the threshold
    assert all(record["id"] != "T401" for record in selected_at_4)

    # Test 8 - Found T403
    linear_position, linear_trace = linear_search( selected_at_4, "T403", key=id_key)
    assert linear_position == 0
    assert (selected_at_4[linear_position]["id"] == "T403")
    assert linear_trace == [(0, "T403")]
    binary_position, binary_trace = binary_search(search_at_4, "T403", key=id_key)
    assert binary_position == 1
    assert (search_at_4[binary_position]["id"] == "T403")
    assert binary_trace == [(0, 3, 1,  "T403")]

    # Positions are relative to each particular view.
    assert linear_position != binary_position
    # Both positions identify the same shared dictionary.
    assert (selected_at_4[linear_position] is search_at_4[binary_position])

    # Test 9 - Missing T499
    missing_linear_position, missing_linear_trace = linear_search(selected_at_4, "T499", key=id_key)
    assert missing_linear_position is None
    assert missing_linear_trace == [
        (0, "T403"),
        (1, "T405"),
        (2, "T402"),
        (3, "T406"),
    ]
    missing_binary_position, missing_binary_trace = binary_search(search_at_4, "T499", key=id_key)
    assert missing_binary_position is None
    assert missing_binary_trace == [(0, 3, 1, "T403"), (2, 3, 2, "T405"), (3, 3, 3, "T406"),]

    # Test 10 - Deliberate wrong-view example
    wrong_position, wrong_trace = binary_search(selected_at_4, "T406", key=id_key)

    # Test 11 - T406 is present, but the age display is not ID ordered.
    assert any(record["id"] == "T406" for record in display_at_4)

    # Test 12 - For this supplied fixture, invalid binary search misses it.
    assert [record["id"] for record in display_at_4] == ["T406", "T402", "T403", "T405"]
    assert len(wrong_trace) > 0

    # Issued change to minimu days = 7
    (
        selected_at_7,
        display_at_7,
        search_at_7,
    ) = build_views(source, minimum_days=7,)
    assert [record["id"] for record in selected_at_7] == [
        "T403",
        "T405",
    ]
    assert [record["id"] for record in display_at_7] == [
        "T403",
        "T405",
    ]

    # Test 13 - Boundary age 7 is included
    assert all(record["days_open"] >= 7 for record in selected_at_7)

    # Test 14 - T406 no longer qualifies at the new threshold.
    assert all(record["id"] != "T406" for record in selected_at_7)

    # Test 15 - The equal seven day records remain stable.
    assert [record["id"] for record in display_at_7] == [
        "T403",
        "T405",
    ]

    # Test 16 - Search remains valid after rebuidling the views.
    rebuilt_position, rebuilt_trace = binary_search(search_at_7, "T403", key=id_key)
    assert rebuilt_position == 0
    assert (search_at_7[rebuilt_position]["id"] == "T403")
    assert rebuilt_trace == [(0, 1, 0, "T403")]

    # Empty selection at minimum days = 8
    (
        selected_at_8,
        display_at_8,
        search_at_8,
    ) = build_views(source, minimum_days=8,)
    assert selected_at_8 == []
    assert display_at_8 == []
    assert search_at_8 == []
    empty_position, empty_trace = binary_search(search_at_8, "T403", key=id_key)
    assert empty_position is None
    assert empty_trace == []

    # Each pipeline stage returns its own outer list.
    assert selected_at_4 is not source
    assert display_at_4 is not selected_at_4
    assert search_at_4 is not selected_at_4
    assert display_at_4 is not search_at_4

    # The views intentionally share eligible record dictionaries.
    for record in selected_at_4:
        display_record = next(candidate for candidate in display_at_4 if candidate["id"] == record["id"])
        search_record = next(candidate for candidate in search_at_4 if candidate["id"] == record["id"])
        assert record is display_record
        assert record is search_record

    # Rebuilding at different thresholds must not alter the source.
    assert source == original_source

if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run tests without -O so assertions are enabled.")
    assignment_checks()
    print("AL05 Tuesday checks passed.")
