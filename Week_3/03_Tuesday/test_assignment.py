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

    # Test 1 - Build fresh State
    records = [record.copy() for record in TICKETS]
    registry = build_registry(records)
    state = {"registry": registry, "pending": deque(), "undo": []}

    # Test 2 - Accept an Open Ticket
    result = enqueue_ticket(state, "T301")
    assert result is True
    assert list(state["pending"]) == ["T301"]
    assert state["registry"]["T301"]["status"] == "open"
    assert state["undo"] == []

    # Test 3 - Reject an Unknown Ticket
    registry_before = {
        ticket_id: record.copy() for ticket_id, record in state["registry"].items()
    }
    pending_before = deque(state["pending"])
    undo_before = [record.copy() for record in state["undo"]]
    result = enqueue_ticket(state, "T999")
    assert result is False
    assert state["registry"] == registry_before
    assert state["pending"] == pending_before
    assert state["undo"] == undo_before

# Test 4 - Reject a Ticket already waiting
    registry_before = {
        ticket_id: record.copy() for ticket_id, record in state["registry"].items()
    }
    pending_before = deque(state["pending"])
    undo_before = [record.copy() for record in state["undo"]]
    result = enqueue_ticket(state, "T301")
    assert result is False
    assert state["registry"] == registry_before
    assert state["pending"] == pending_before
    assert state["undo"] == undo_before

    # Test 5 - Reject a completed Ticket
    completed_records = [record.copy() for record in TICKETS]
    completed_state = {"registry": build_registry(completed_records), "pending": deque(), "undo": []}
    completed_state["registry"]["T304"]["status"] = "completed"
    registry_before = {ticket_id: record.copy() for ticket_id, record in completed_state["registry"].items()}
    pending_before = deque(completed_state["pending"])
    undo_before = [record.copy() for record in completed_state["undo"]]
    result = enqueue_ticket(completed_state, "T304")
    assert result is False
    assert completed_state["registry"] == registry_before
    assert completed_state["pending"] == pending_before
    assert completed_state["undo"] == undo_before

    # Test 6 - Add T302 behind T301
    result = enqueue_ticket(state, "T302")
    assert result is True
    assert list(state["pending"]) == ["T301", "T302"]
    assert state["undo"] == []

    # Test 7 - Process T301 first
    first_processed = process_next(state)
    assert first_processed == "T301"
    assert list(state["pending"]) == ["T302"]
    assert state["registry"]["T301"]["status"] == "completed"
    assert state["registry"]["T302"]["status"] == "open"
    assert state["undo"] == [
        {"ticket_id": "T301", "previous_status": "open",}
    ]

    # Test 8 - Process T302 second
    second_processed = process_next(state)
    assert second_processed == "T302"
    assert list(state["pending"]) == []
    assert state["registry"]["T301"]["status"] == "completed"
    assert state["registry"]["T302"]["status"] == "completed"
    assert state["undo"] == [
        {"ticket_id": "T301", "previous_status": "open",},
        {"ticket_id": "T302", "previous_status": "open",}
    ]

    # Test 9 - First undo restores T302
    first_restored = undo_process(state)
    assert first_restored == "T302"
    assert state["registry"]["T301"]["status"] == "completed"
    assert state["registry"]["T302"]["status"] == "open"
    assert list(state["pending"]) == ["T302"]
    assert state["undo"] == [
        {"ticket_id": "T301", "previous_status": "open",}
    ]

    # Test 10 - Second undo restores T301
    second_restored = undo_process(state)
    assert second_restored == "T301"
    assert state["registry"]["T301"]["status"] == "open"
    assert state["registry"]["T302"]["status"] == "open"
    assert list(state["pending"]) == ["T301", "T302"]
    assert state["undo"] == []

    # Test 11 - Empty undo history changes nothing
    registry_before = {ticket_id: record.copy() for ticket_id, record in state["registry"].items()}
    pending_before = deque(state["pending"])
    undo_before = [record.copy() for record in state["undo"]]
    result = undo_process(state)
    assert result is None
    assert state["registry"] == registry_before
    assert state["pending"] == pending_before
    assert state["undo"] == undo_before

    # Test 12 - Empty pending queue changes nothing
    empty_records = [record.copy() for record in TICKETS]
    empty_state = {"registry": build_registry(empty_records), "pending": deque(), "undo": []}
    registry_before = {ticket_id: record.copy() for ticket_id, record in empty_state["registry"].items()}
    pending_before = deque(empty_state["pending"])
    undo_before = [record.copy() for record in empty_state["undo"]]
    result = process_next(empty_state)
    assert result is None
    assert empty_state["registry"] == registry_before
    assert empty_state["pending"] == pending_before
    assert empty_state["undo"] == undo_before

    # Test 13 - Undo preserves a priority edit
    priority_records = [record.copy() for record in TICKETS]
    priority_state = {"registry": build_registry(priority_records), "pending": deque(), "undo": []}
    enqueue_ticket(priority_state, "T301")
    process_next(priority_state)
    update_priority(priority_state["registry"], "T301", "low")
    restored_id = undo_process(priority_state)
    assert restored_id == "T301"
    assert priority_state["registry"]["T301"]["status"] == "open"
    assert priority_state["registry"]["T301"]["priority"] == "low"
    assert list(priority_state["pending"]) == ["T301"]
    assert priority_state["undo"] == []

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
