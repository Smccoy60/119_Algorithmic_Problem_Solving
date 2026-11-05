
from ticket_data import TICKETS
from search_support import id_key, days_key
from pipeline_support import select_open_tickets
from ticket_display import show_ticket, show_tickets, show_trace
from search_algorithms import linear_search, binary_search

# After preparing your local search_algorithms.py, add its search imports here.
# Copy your AL04 functions/imports, or use the instructor-released recovery module.


# TUESDAY - Stable ordering, with counts for one tiny example.

def insertion_sort(records, key):
    """Return a stable shallow ordered list, comparison/shift counts, and ID trace."""
    # Make a new outer list.  The ticket dictionaries inside the list are still shared.
    ordered = list(records)
    # Count every key comparison executed in the shifting loop.
    comparisons = 0
    # Count right-shifts only.
    moves = 0
    # Save the completed ID order after each insertion.
    trace = []
    # Position 0 is already a sorted one-record prefix. Begin with the record at position 1.
    for current_position in range(1, len(ordered)):
        # Save teh record that will be inserted.
        saved_record = ordered[current_position]
        # Save its key value so it can be compared with records in the sorted prefix. 
        saved_value = key(saved_record)
        # Start inspecting the record immediately to the left. 
        check_position = current_position - 1
        # Inspect earlier records from right to left.
        while check_position >= 0:
            # Count this executed key comparison.
            comparisons += 1
            # Stop when the earlier value is not larger. Stopping on equality preserves stable tie order.
            if key(ordered[check_position]) <= saved_value:
                break
            # Shift the larger earlier record one position right.
            ordered[check_position + 1] = ordered[check_position]
            # Count the right-shift.
            moves += 1
            # Continue checking toward the left.
            check_position -= 1
        # Place the saved record into the remaining gap. 
        ordered[check_position + 1] = saved_record
        # Record the full ID order after this insertion.
        trace.append([record["id"] for record in ordered])
    return ordered, comparisons, moves, trace

def build_views(records, minimum_days=4):
    """Return selected, age-display, and ID-search lists."""
    # Filter the authoritative source records.
    selected = select_open_tickets(records, minimum_days=minimum_days,)
    # Build the stable age-ordered dislay view.
    display_view, _, _, _ = insertion_sort(selected, key=days_key,)
    # Build a separate ID-ordered binary-search view.
    search_view = sorted(selected, key=id_key,)
    # Return all three purposeful views.
    return selected, display_view, search_view

def show_search_result(title, records, position, trace):
    """Display a view-relative search result and its trace."""
    print(f"\n{title}")
    if position is not None: show_ticket(records[position])
    else: 
        show_ticket(None)
    show_trace(
        title,
        trace,
    )


def main():
    """Present the completed AL05 filter, sort, and search pipeline"""
    print("AL05: Fileter, Sort, and Search Pipeline")

    print("\nTuesday: Stable Ordering Baseline")

    # Use supplied eligibility function.  This selects open tickets with days_open >= 4.
    selected = select_open_tickets(TICKETS, minimum_days=4,)
    # Show the eligible records in thier original source order.
    show_tickets("Selected open tickets aged at least 4 days", selected,)
    # Sort the selected records from fewer to more days open.
    ordered, comparisons, moves, trace = insertion_sort(selected, key=days_key,)
    # Show the stable age-ordered display.
    show_tickets("Stable age-ordered display", ordered,)
    print("\nTeaching evidence")
    print("Selected IDs:", [record["id"] for record in selected],)
    print("Age-ordered IDs:", [record["id"] for record in ordered],)
    print("Key comparisons:", comparisons,)
    print("Right-shifts:", moves,)
    print("\nID order after each insertion:")
    for insertion_number, id_order in enumerate(trace, start=1,):
        print(f"Insertion {insertion_number}: {id_order}")
    # Compare our ordered IDs with Python's stable sorted().
    expected = sorted(selected, key=days_key,)
    print("\nMatches sorted(..., key=days_key):",
          ordered == expected,)
    print("Source TICKETS order remains:", [record["id"] for record in TICKETS],)

    print("\nThursday: Compose, Change, and Verify")
    (
        selected,
        display_view,
        search_view,
    ) = build_views(
        TICKETS,
        minimum_days=4
    )

    show_tickets("Selected records at minimum_days=4", selected)
    show_tickets("Age-ordered display view", display_view,)
    show_tickets("ID-ordered search view", search_view,)

    # Linear seearch for T403 in selected
    linear_position, linear_trace = linear_search(
        selected,
        "T403",
        key=id_key,
    )

    show_search_result("Linear search for T403 in selected", selected, linear_position, linear_trace,)

    # Binary search for T403 in ID search view
    binary_position, binary_trace = binary_search(
        search_view,
        "T403",
        key=id_key,
    )
    show_search_result("Binary search for T403 in ID search view", search_view, binary_position, binary_trace,)
    if (linear_position is not None and binary_position is not None):
        print("\nBoth searches found the same record:", selected[linear_position] is search_view[binary_position])

    # Missing T499
    missing_linear_position, missing_linear_trace = linear_search(
        selected,
        "T499",
        key=id_key,
    )
    show_search_result("Linear search for absent T499", selected, missing_linear_position, missing_linear_trace,)
    missing_binary_position, missing_binary_trace = binary_search(
        search_view,
        "T499",
        key=id_key,
    )
    show_search_result("Binary search for absent T499", search_view, missing_binary_position, missing_binary_trace,)

    #Deliberate wrong-view example
    print("\nDeliberate invalid use: binary search for T406 in the age-ordered display view")
    wrong_position, wrong_trace = binary_search(
        display_view,
        "T406",
        key=id_key,
    )
    if wrong_position is not None:
        show_ticket(display_view[wrong_position])
    else: 
        show_ticket(None)
    show_trace("Invalid binary search for T406 in age order", wrong_trace)
    print("This result is not reliable because the age-ordered display is not ordered by ID.")

    # Issued change: Minimum Days = 7
    print("\nIssued Change: raise minimum days from 4 to 7")
    (
        selected_at_7,
        display_at_7,
        search_at_7,
    ) = build_views(
        TICKETS,
        minimum_days=7,
    )
    show_tickets("Selected records at minimum_days=7", selected_at_7,)
    show_tickets("Age-ordered display at minimum_days=7", display_at_7,)
    show_tickets("ID-ordered search view at minimum_days=7", search_at_7,)
    print("T406 no longer qualifies because it has only 4 days open.")

    # Confirm that T403 reamins searchable after rebuilding
    changed_position, changed_trace = binary_search(
        search_at_7,
        "T403",
        key=id_key,
    )
    show_search_result("Binary search for T403 after rule change", search_at_7, changed_position, changed_trace)

    # Empty selection minmum days = 8
    print("\nEmpty selection check: minimum_days=8")
    (
        selected_at_8,
        display_at_8,
        search_at_8,
    ) = build_views(
        TICKETS,
        minimum_days=8,
    )
    show_tickets("Selected records at minimum_days=8", selected_at_8,)
    empty_position, empty_trace = binary_search(
        search_at_8,
        "T403",
        key=id_key,
    )
    show_search_result("Binary search in the empty ID-search view", search_at_8, empty_position, empty_trace)

    # Final Source Check
    print("\nSource Tickets order reamins:",
        [record["id"] for record in TICKETS],)

if __name__ == "__main__":
    main()
