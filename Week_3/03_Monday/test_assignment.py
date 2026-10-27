"""Optional unfinished test scaffold; students choose expected ticket behavior."""

from collections import deque

from main import (
    build_registry,
    scan_lookup,
    indexed_lookup,
    update_priority,
    filter_by_category,
    enqueue_ticket,
    process_next,
    undo_process,
    repair_queue,
    cancel_ticket,
)
from ticket_data import TICKETS, SUPPORTED_CATEGORIES


def assignment_checks():
    """Check the implemented daily contracts against independent expectations."""
    # Test 1 - Does build_registry() build the registry?
    records = [record.copy() for record in TICKETS]
    registry = build_registry(records)
    assert len(registry) == len(records)

    # Test 2 - Did build_registry() make copies?
    assert registry["T301"] == records[0]
    assert registry["T301"] is not records[0]

    # Test 3 - Can scan_lookup() find a ticket?
    records = [record.copy() for record in TICKETS]
    found = scan_lookup(records, "T302")
    assert found is not None
    assert found["id"] == "T302"

    # Test 4 - What if scan_lookup() can't find the ID?
    assert scan_lookup(records, "T999") is None

    # Test 5 - What if scan_lookup() gets an empty list?
    assert scan_lookup([], "T301") is None

    # Test 6 - Test indexed_lookup() 
    records = [record.copy() for record in TICKETS]
    registry = build_registry(records)
    found = indexed_lookup(registry, "T302")
    assert found is registry["T302"]
    assert indexed_lookup(registry, "T999") is None
    assert indexed_lookup({}, "T301") is None

    # Test 7 - Duplicate Ticket Ids
    duplicate_records = [{"id": "T900", "title": "First", "category": "account", "priority": "normal", "status": "open",},
                         {"id": "T900", "title": "Second", "category": "network", "priority": "high", "status": "open"},]
    duplicate_snapshot = [record.copy() for record in duplicate_records]
    try: 
        build_registry(duplicate_records)
        assert False
    except ValueError:
        pass
    assert duplicate_records == duplicate_snapshot

    # Test 8 - Does update_priority() work?
    records = [record.copy() for record in TICKETS]
    registry = build_registry(records)
    old_title = registry["T301"]["title"]
    old_category = registry["T301"]["category"]
    old_status = registry["T301"]["status"]
    result = update_priority(registry, "T301", "high")
    assert result is True
    assert registry["T301"]["priority"] == "high"
    assert registry["T301"]["title"] == old_title
    assert registry["T301"]["category"] == old_category
    assert registry["T301"]["status"] == old_status

    # Test 9 - Missing ticket should NOT change anything
    before = {ticket_id: record.copy() for ticket_id, record in registry.items()}
    result = update_priority(registry, "T999", "high")
    assert result is False
    assert registry == before

    # Test 10 - filter_by_category()
    records = [record.copy() for record in TICKETS]
    registry = build_registry(records)
    account_tickets = filter_by_category(registry, "account")
    assert all(record["category"] == "account" for record in account_tickets)
    assert filter_by_category(registry, "not-a-category") == []

    # Test 11 - Are filtered tickets actually copies?
    if account_tickets:
        selected_id = account_tickets[0]["id"]
        original_priority = registry[selected_id]["priority"]
        account_tickets[0]["priority"] = "changed"
        assert registry[selected_id]["priority"] == original_priority

                                 



    # TUESDAY - Begin after Tuesday's instruction.
    # Build fresh state with an empty pending deque and undo list.
    # Check acceptance of open tickets and rejection of unknown/completed/queued IDs.
    # For rejected actions, compare registry, pending, and history before/after.
    # Process two IDs and predict which one a single undo restores first.
    # Check successive undo, empty queue/history, and preserved priority edits.
    # Save before-state values independently; an alias changes with live state.

    # THURSDAY - Begin after Thursday's instruction.
    # Check cancellation of open tickets both pending and not pending.
    # Check missing/completed cancellation leaves every state component unchanged.
    # Repair mixed, empty, all-valid, and all-missing queues; check retained order.
    # Check the original queue is unchanged and the returned queue is installed.
    # Save a copied selection, then update/cancel live tickets and check old values.
    # Rerun the earlier checks after adding these operations.

    # Add actual assertions for each stage as you complete it.
    # Remove this exception only after adding real executable checks.
    #raise NotImplementedError("Add focused checks before reporting success.")


def main():
    """Reject unfinished or disabled tests before reporting success."""
    if not __debug__:
        raise RuntimeError("Run tests without Python optimization (-O).")
    assignment_checks()
    print("Assignment checks passed.")


if __name__ == "__main__":
    main()
