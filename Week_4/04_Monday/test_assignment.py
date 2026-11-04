"""Unfinished test prompts; replace the final stop with your own focused checks."""

from copy import deepcopy
from main import linear_search, binary_search
from ticket_data import TICKETS
from search_support import id_key, category_key


def assignment_checks():
    """Check independent expected answers, boundaries, traces, and input preservation."""

    # TUESDAY: use category order and accept any matching duplicate category.
    # Check unchanged input order/fields, including after unsuccessful searches.
    # Separately demonstrate T401's deliberate invalid-order miss on TICKETS.
    # Agreement between two implementations alone is not an independent oracle.

    # Create Test Data

    #1 Test Setup: Make a copy of the original tickets for testing.
    fixture = deepcopy(TICKETS)
    #2 Test Setup: Keep a separate copy to check later that the search functions did not change the data.
    original_fixture = deepcopy(fixture)

    #3 Test Linear Search: Find T403
    position, trace = linear_search(fixture, "T403")
    assert position == 0
    assert position is not None
    assert fixture[position]["id"] == "T403"
    assert trace == [(0, "T403"),]

    #4 Test Linear Search: Find T401
    position, trace = linear_search(fixture, "T401")
    assert position == 1
    assert trace == [
        (0, "T403"),
        (1, "T401"),
    ]

    #5 Test Linear Search: Missing T499
    position, trace = linear_search(fixture, "T499")
    assert position is None
    assert len(trace) == len(fixture)
    assert trace == [
        (0, "T403"),
        (1, "T401"),
        (2, "T405"),
        (3, "T402"),
        (4, "T404"),
        (5, "T406"),
    ]

    #6 Test Linear Search: Empty List
    position, trace = linear_search([], "T403")
    assert position is None
    assert trace == []

    #7 Test Linear Search: One Item
    singleton = [{"id": "T900"}]
    position, trace = linear_search(singleton, "T900")
    assert position == 0
    assert trace == [
        (0, "T900")
    ]

    #8 Test Linear Search: One Item Missing
    position, trace = linear_search(singleton, "T999")
    assert position is None
    assert trace == [
        (0, "T900")
    ]

    # Prepare Data for Binary Search

    # Binary Search requires the records to already be ordered using teh same key beign searched.
    id_ordered = sorted(fixture, key=id_key)

    # Check that our sorted order is what we expect.
    assert [ticket["id"] for ticket in id_ordered] == ["T401", "T402", "T403", "T404", "T405", "T406"]

    # Save a copy so we can make sure binary search does not change the ordered list.
    original_id_ordered = deepcopy(id_ordered)

    #9 Test Binary Search: Find T403
    position, trace = binary_search(id_ordered, "T403")
    assert position == 2
    assert id_ordered[position]["id"] == "T403"
    assert trace == [
        (0, 5, 2, "T403"),
    ]

    #10 Test Binary Search: Find First Item T401
    position, trace = binary_search(id_ordered, "T401")
    assert position == 0
    assert id_ordered[position]["id"] == "T401"
    assert trace[-1] == (
        0,
        1,
        0,
        "T401"
    )

    #11 Test Binary Search: Find Last Item T406
    position, trace = binary_search(id_ordered, "T406")
    assert position == 5
    assert id_ordered[position]["id"] == "T406"
    assert trace[-1] == (
        5,
        5,
        5,
        "T406"
    )

    #12 Test Binary Search: Missing T499
    position, trace = binary_search(id_ordered, "T499")
    assert position is None
    assert trace == [
        (0, 5, 2, "T403"),
        (3, 5, 4, "T405"),
        (5, 5, 5, "T406"),
    ]

    #13 Test Binary Search: Missing Below The Range
    position, trace = binary_search(id_ordered, "T400")
    assert position is None
    assert all(len(step) == 4 for step in trace)

    #14 Test Binary Search: Missing Between IDs
    position, trace = binary_search(id_ordered, "T403A")
    assert position is None
    assert all(len(step) -- 4 for step in trace)

    #15 Test Binary Search: Empty List
    position, trace = binary_search([], "T403")
    assert position is None
    assert trace == []

    #16 Test Binary Search: Item Found
    position, trace = binary_search(singleton, "T900")
    assert position == 0
    assert trace == [
        (0, 0, 0, "T900")
    ]

    #17 Test Binary Search: One Item Missing
    position, trace = binary_search(singleton, "T999")
    assert position is None
    assert trace == [
        (0, 0, 0, "T900")
    ]   

    #18 Test Category Search with Duplicates
    # Sort the tickets by category before using binary search
    category_ordered = sorted(fixture, key=category_key,)

    # Save the category order so we can check later that the searches do not change it
    original_category_ordered = deepcopy(category_ordered)

    # Search for account using linear search.
    linear_position, linear_trace = linear_search(category_ordered, "account", key=category_key,)

    #19 Test Search for account using binary search
    binary_position, binary_trace = binary_search(category_ordered, "account", key=category_key,)
    assert linear_position is not None
    assert binary_position is not None
    assert (category_ordered[linear_position]["category"] == "account")
    assert (category_ordered[binary_position]["category"] == "account")
    assert linear_trace[-1][1] == "account"
    assert binary_trace[-1][3] == "account"

    #20 Test Deliberate Invalid-Order Test
    linear_position, linear_trace = linear_search(fixture, "T401",)
    binary_position, binary_trace = binary_search(fixture, "T401",)
    assert linear_position == 1
    assert fixture[linear_position]["id"] == "T401"
    assert binary_position is None
    assert len(binary_trace) > 0

    #21 Test Check That The Data Was Not Changed
    assert fixture == original_fixture
    assert id_ordered == original_id_ordered
    assert category_ordered == original_category_ordered


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run tests without -O so assertions are enabled.")
    assignment_checks()
    print("AL04 checks passed.")
