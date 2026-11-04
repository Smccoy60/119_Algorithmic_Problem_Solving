"""Optional English-first starter for stable sorting and a key-correct pipeline."""

from ticket_data import TICKETS
from search_support import id_key, days_key
from pipeline_support import select_open_tickets
from ticket_display import show_ticket, show_tickets

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


# THURSDAY - Compose existing interfaces; rebuild after the eligibility change.

def build_views(records, minimum_days=4):
    """Return selected, age-display, and ID-search lists sharing eligible records."""
    # Use the supplied open/age filter on the authoritative source.
    # Use your insertion sort with days_key to build the display view.
    # Use sorted with id_key to build the separate binary-search view.
    # Return the three lists; do not copy records or edit their fields.
    raise NotImplementedError("Connect selection to two purposeful orderings.")


def main():
    """Present Tuesday's stable insertion-sort baseline."""
    print("AL05: Tuesday Stable Ordering Baseline")

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

    # THURSDAY: build both views and use the local search_algorithms functions.
    # Find T403 and absent T499; resolve positions in the particular list searched.
    # Deliberately use the age display for ID binary search of T406; explain failure.
    # Rebuild from TICKETS at minimum_days=7, then 8, to show revised/empty results.
    # Keep app output readable; put short workload/copy/change notes in README.md.
    # Test and submit the complete personal week_04/AL05 folder independently.
    print("AL05 starter: begin with Tuesday's stable insertion sort.")


if __name__ == "__main__":
    main()
