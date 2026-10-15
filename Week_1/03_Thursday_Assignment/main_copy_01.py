"""Optional English-first starter; develop one application across three days."""

from ticket_data import TICKETS

def validate_ticket(ticket):
    """Return readable issues, or an empty list when the ticket is valid."""
    issues = []
    ticket_id = ticket.get("id", "Unknown ID")
    if "age_days" not in ticket:
        issues.append(f"{ticket_id}: missing age_days")
    elif isinstance(ticket["age_days"], bool):
        issues.append(f"{ticket_id}: age_days cannot be True or False")
    elif not isinstance(ticket["age_days"], int):
        issues.append(f"{ticket_id}: age_days must be a number")
    if ticket.get("status") not in ["open", "closed"]:
        issues.append(f"{ticket_id}: invalid status")
    return issues

def select_open_tickets(records):
    """Return (selected, issues) for the valid open-ticket view."""
    selected = []
    issues = []
    for ticket in records:
        validation_issues = validate_ticket(ticket)
        if validation_issues:
            issues.extend(validation_issues)
        else: 
            if ticket["status"] == "open":
                selected.append(ticket)
    return selected, issues


def show_report(title, policy, selected, issues):
    """Present useful ticket details, a count, and records needing checking."""
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    print(f"Policy: {policy}")
    print(f"Selected Tickets: {len(selected)}\n")

    if selected:
        for ticket in selected:
            print(
    f"{ticket['id']} | "
    f"{ticket['category']} | "
    f"{ticket['priority']} | "
    f"{ticket['age_days']} days"
            )

    else:
        print("No tickets matched.")
    print("\nChecking Messages")
    if issues:
        for issue in issues:
            print("-", issue)
    else:
        print("No validation issues found.")


def main():
    """Run the stages you have implemented so far."""
    selected, issues = select_open_tickets(TICKETS)
    follow_up_selected, follow_up_issues = select_follow_up(TICKETS)

    show_report(
        "Open Ticket View",
        "Valid open tickets only",
        selected,
        issues
    )

    show_report(
        "Follow-Up List",
        "Valid open tickets at least 2 days old that are high priority or in the access category",
        follow_up_selected,
        follow_up_issues
    )

def needs_follow_up(ticket):
    """Apply the current follow-up policy to a previously validated ticket."""
    is_open = ticket["status"] == "open"
    old_enough = ticket["age_days"] >= 2
    is_high_priority = ticket["priority"] == "high"
    is_access_category = ticket["category"] == "access"

    meets_required_rules = is_open and old_enough
    meets_priority_or_category = is_high_priority or is_access_category

    return meets_required_rules and meets_priority_or_category

def select_follow_up(records):
    """Return (selected, issues) for the current follow-up policy."""
    selected = []
    issues = []

    for ticket in records: 
        validation_issues = validate_ticket(ticket)
        if validation_issues: 
            issues.extend(validation_issues)
        else:
            if needs_follow_up(ticket):
                selected.append(ticket)
    return selected, issues

if __name__ == "__main__":
    main()
