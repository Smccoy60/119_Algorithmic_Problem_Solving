"""Optional English-first starter for individual search contracts and correctness."""

from ticket_data import TICKETS
from search_support import id_key, category_key, matches, compare_values
from ticket_display import show_ticket, show_tickets, show_trace


# MONDAY - Separate the requested value from the traversal.

def linear_search(records, target, key=id_key):
    """Return the first matching position and visits, or None and visits."""
    # Create an empty list to record every position and value visited.
    trace = []
    #Visit every record in its current order.
    for position, record in enumerate(records):
        # Use the supplied key function to select the searchable value.
        value = key(record)
        # Record the position and selected value before checking for a match.
        trace.append((position, value))
        # Check whether the selected value matches the target.
        if matches(value, target):
            # Return the matchinig position and completed trace.
            return position, trace
    # The target was not found; return None with the completed trace.
    return None, trace


def binary_search(records, target, key=id_key):
    """Return any matching position and interval visits on a key-ordered input."""
    # Create an empty list to record every interval visit.
    trace = []
    # The lowest valid position starts at the beginning of the list. 
    low = 0
    # The highest valid position starts at the end of the list.
    high = len(records) - 1
    # Continue while the search interval still contains candidates.
    while low <= high:
        # Find the integer midpoint of the current interval.
        middle = (low + high) // 2
        # Select the searchable value from the middle record.
        value = key(records[middle])
        # Record the bounds, midpoint, and selected value.
        trace.append((low, high, middle, value))
        # Compare the selected value with the requested target.
        comparision = compare_values(value, target)
        # A comparision of zero means the values are equal.
        if comparision == 0:
            # Return the matching position and completed trace.
            return middle, trace
        # A negative comparison means the selected value is too small.
        if comparision < 0:
            # Discard the midpoint and everything below it.
            low = middle + 1
        # Otherwise, the selected value is too large.
        else:
            # Discard the midpoint and everything above it.
            high = middle - 1
    # The interval became empty, so the target was not found.
    return None, trace


# TUESDAY CHECKPOINT - Verify the contract and preserve an independent submission.

def main():
    """Show completed searches with readable results and two small teaching traces."""

    # TUESDAY: finish the boundary/duplicate/nonmutation tests and short README.
    # Run the final personal week_04/AL04 copy before submitting its repo URL.
    # Copy completed functions into AL05 later; preserve this submitted snapshot.
    print("AL04 starter: begin with Monday's linear search.")
    # Display the original tickets in their supplied order.
    show_tickets("Original ticket order", TICKETS)

    # Linear Search: Found T403
    linear_position, linear_trace = linear_search(TICKETS, "T403")
    print("\nLinear search for T403:")

    # Position zero is valid, so test against None.
    if linear_position is not None: 
        show_ticket(TICKETS[linear_position])
    else:
        show_ticket(None)
    # Display the positions and values visited.
    show_trace("Linear search for T403", linear_trace)

    # Linear Search: Missing T499
    missing_position, missing_trace = linear_search(TICKETS, "T499")
    print("\nLinear search for T499:")
    if missing_position is not None:
        show_ticket(TICKETS[missing_position])
    else:
        show_ticket(None)
    # The main report does not need every trace, but this is useful for demonstating that the scan visited all six tickets.
    show_trace("Linear search for T499", missing_trace)

    # Prepare an Id-Ordered View
    # Binary search requires records already ordered by the same key.
    # Sorting happens outside binary_search.
    id_ordered_tickets = sorted(TICKETS, key=id_key)
    show_tickets("Tickets ordered by ID", id_ordered_tickets)
    print("I made it to Binary Search")

    # Binary Search: Found T403
    binary_position, binary_trace = binary_search(id_ordered_tickets, "T403")
    print("\nBinary search for T403:")
    if binary_position is not None:
        show_ticket(id_ordered_tickets[binary_position])
    else:
        show_ticket(None)
    show_trace("Binary search for T403", binary_trace)

    # Binary Search: Missing T499
    binary_missing_position, binary_missing_trace = binary_search(id_ordered_tickets, "T499")
    print("\nBinary search for T499:")
    if binary_missing_position is not None:
        show_ticket(id_ordered_tickets[binary_missing_position])
    else:
        show_ticket(None)

    # Deliberate Invalid_Order Example
    print("\nDeliberate invalid order search for T401:")
    # Linear search works because it does not require sorted input.
    invalid_linear_position, invalid_linear_trace = linear_search(TICKETS, "T401")
    # This deliberately violates the binary-search precondition.
    invalid_binary_position,invalid_binary_trace = binary_search(TICKETS, "T401",)
    print("Linear search position:", invalid_linear_position)
    print("Binary search position:", invalid_binary_position)
    show_trace("Linear trace for T401 in original order", invalid_linear_trace)
    show_trace("Invalid binary trace for T401 in original order", invalid_binary_trace)
    print("The binary search result is not reliable because the original " "tickets are not ordered by ID.")

    # Repeated Category Search
    # Prepare a category-ordered view outside the search algorithm.
    category_ordered_tickets = sorted(TICKETS, key=category_key)
    show_tickets("Tickets ordered by category", category_ordered_tickets)
    category_linear_position, category_linear_trace = linear_search(category_ordered_tickets, "account", key=category_key,)
    print("\nLinear category search for account:")
    if category_linear_position is not None:
        show_ticket(category_ordered_tickets[category_linear_position])
    else:
        show_ticket(None)
    category_binary_position, category_binary_trace = binary_search(category_ordered_tickets, "account", key=category_key,)
    print("\nBinary category search for account:")
    if category_binary_position is not None:
        show_ticket(category_ordered_tickets[category_binary_position])
    else:
        show_ticket(None)
    show_trace("Binary category search for account", category_binary_trace,)
    print("Categories can repeat, so either search may return any record " "whose category is account.")


if __name__ == "__main__":
    main()
