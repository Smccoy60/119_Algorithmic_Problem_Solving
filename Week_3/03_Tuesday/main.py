"""Optional English-first starter; develop one ticket application across three days."""

from collections import deque  # Used beginning Tuesday.

from ticket_data import TICKETS, SUPPORTED_CATEGORIES
from ticket_display import display_tickets, display_state


def build_registry(records):
    """Return independent ticket records indexed by unique ID."""
    registry = {}
    for record in records:
        ticket_id = record["id"]
        if ticket_id in registry:
            raise ValueError("Duplicate ticket ID")
        registry[ticket_id] = record.copy()
    return registry


def scan_lookup(records, ticket_id):
    """Return the first matching ticket, or None when absent."""
    for record in records:
        if record["id"] == ticket_id:
            return record
    return None


def indexed_lookup(registry, ticket_id):
    """Return the matching live ticket, or None when absent."""
    return registry.get(ticket_id)


def update_priority(registry, ticket_id, priority):
    """Update one existing ticket's priority and report whether it was found."""
    if ticket_id not in registry:
        return False
    registry[ticket_id]["priority"] = priority
    return True


def filter_by_category(registry, category):
    """Return independent copies of tickets matching the selected category."""
    results = []
    for record in registry.values():
        if record["category"] == category:
            results.append(record.copy())
    return results


# ======================================================================
# TUESDAY - Process in order and undo one action
# Wait until Tuesday's instruction before beginning this stage.
# ======================================================================

def enqueue_ticket(state, ticket_id):
    """Queue a known open ticket once, returning whether it was accepted."""
    # Check that the ID exists, its ticket is open, and it is not already waiting.
    # If any check fails, return False without changing any part of state.
    # Otherwise, add the ID at the back of pending and return True.
    registry = state["registry"]
    pending = state["pending"]
    if ticket_id not in registry:
        return False
    if registry[ticket_id]["status"] != "open":
        return False
    if ticket_id in pending:
        return False
    pending.append(ticket_id)
    return True


def process_next(state):
    """Complete the oldest waiting ticket and remember its previous status."""
    # If pending is empty, return None without changing state.
    # Take the oldest ID from the front of pending and find its live ticket.
    # Append a history record with named ticket_id and previous_status fields.
    # Mark the ticket completed and return its ID.
    pending = state["pending"]
    if not pending:
        return None
    ticket_id = pending.popleft()
    ticket = state["registry"][ticket_id]
    history_record = {"ticket_id": ticket_id, "previous_status": ticket["status"],}
    state["undo"].append(history_record)
    ticket["status"] = "completed"
    return ticket_id
    


def undo_process(state):
    """Restore the latest processed ticket and return it to the queue front."""
    # If history is empty, return None without changing state.
    # Remove the newest history record and use its named fields to find the ticket.
    # Restore only its prior status; keep unrelated priority changes.
    # Return the ID to the front of pending, then return that ID to the caller.
    undo = state["undo"]
    if not undo:
        return None
    history_record = undo.pop()
    ticket_id = history_record["ticket_id"]
    previous_status = history_record["previous_status"]
    state["registry"][ticket_id]["status"] = previous_status
    state["pending"].appendleft(ticket_id)
    return ticket_id


# ======================================================================
# THURSDAY - Cancel consistently and preserve snapshots
# Wait until Thursday's instruction before beginning this stage.
# ======================================================================

def repair_queue(registry, pending):
    """Return a new queue of known IDs and a list of removed missing IDs."""
    # Prepare a new empty deque and a list for removed IDs.
    # Visit pending in order: keep known IDs in the new queue, collect missing IDs.
    # Return both collections without changing registry or the original pending.
    # The owning application must install the returned queue into its state.
    raise NotImplementedError("Repair missing-ticket references without reordering.")


def cancel_ticket(state, ticket_id):
    """Remove an open ticket and any waiting request, leaving history unchanged."""
    # Check existence and open status before making any changes.
    # Return False unchanged for a missing or completed ticket.
    # Remove the eligible ticket from the registry and remove its pending reference.
    # You may reuse repair_queue, installing its returned queue into state.
    # Leave other requests in order and history unchanged; return True.
    raise NotImplementedError("Cancel an open ticket consistently.")


def main():
    """Show only the daily stages whose operations you have completed."""
    # MONDAY: build a fresh registry from TICKETS.
    # Compare scan/index answers before edits; display a found or missing result.
    # Update one priority. Check a category using SUPPORTED_CATEGORIES membership.
    # Select copied category records and show them using display_tickets.
    # Keep a selection to revisit later; do not call unfinished later-day functions.

    # TUESDAY: add a state dictionary with registry, pending deque, and undo list.
    # Queue two open IDs; process both in arrival order; undo the last processing.
    # Use display_state to make waiting work and restoration clear.
    # Reject unknown, completed, and duplicate pending requests without changes.

    # THURSDAY: use a separate stale-queue example and install its repaired queue.
    # Demonstrate open-ticket cancellation and unchanged state for rejected actions.
    # Compare an earlier saved selection with the registry after update/cancellation.
    # Run all tests, add brief personal README notes, and commit progress.
    # Each partner tests a full personal copy and submits their own repository URL.

    # Replace this message as your Monday baseline becomes ready.
    registry = build_registry(TICKETS)
    scan_result = scan_lookup(TICKETS, "T302")
    index_result = indexed_lookup(registry, "T302")

    if scan_result is not None:
        display_tickets("Scan lookup result", [scan_result])
    else:
        print("Ticket not found.")

    if index_result is not None:
        display_tickets("Indexed lookup result", [index_result])
    else:
        print("Ticket not found.")

    update_priority(registry, "T301", "high")
    category = "account"
    if category in SUPPORTED_CATEGORIES:
        selected = filter_by_category(registry, category)
        display_tickets("Selected category tickets", selected)
    else:
        print("Unsupported category.")

    state = {
        "registry": registry,
        "pending": deque(),
        "undo": [],
    }

    enqueue_ticket(state, "T301")
    enqueue_ticket(state, "T302")
    display_state("Two tickets waiting", state)
    first_processed = process_next(state)
    second_processed = process_next(state)
    print(f"Processed first: {first_processed}")
    print(f"Processed second: {second_processed}")
    display_state("After processing two tickets", state)
    restored_id = undo_process(state)
    print(f"Undid processing for: {restored_id}")
    display_state("After one undo", state)
    restored_id = undo_process(state)
    print(f"Undid processing for: {restored_id}")
    display_state("After second undo", state)
    
if __name__ == "__main__":
    main()
