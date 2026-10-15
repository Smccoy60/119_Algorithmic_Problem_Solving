"""Optional test support; students supply their focused cases and expectations."""

from main_copy_01 import select_open_tickets, select_follow_up


def check_selection(selector, records, expected_ids, expected_issue_count):
    """Compare selected IDs and issue count with independently chosen expectations."""
    selected, issues = selector(records)
    assert [record["id"] for record in selected] == expected_ids
    assert len(issues) == expected_issue_count
    assert all(isinstance(issue, str) and issue.strip() for issue in issues)


def assignment_checks():
    """Run the focused checks you create from the assignment's coverage checklist."""
    ## Open ticket selection tests
    check_selection(
select_open_tickets, 
        [],
        [],
        0
    )

    check_selection(
select_open_tickets,
        [
            {
                "id": "T100",
                "status": "open",
                "category": "software",
                "age_days": 2,
                "priority": "high"
            }
        ],
        ["T100"],
        0
    )

    check_selection(
select_open_tickets,
        [
            {
                "id": "T200",
                "status": "closed",
                "category": "software",
                "age_days": 2,
                "priority": "high"
            }
        ],
        [],
        0
    )

    ## Follow-up selection tests
    check_selection(
        select_follow_up,
        [
            {
                "id": "T300",
                "status": "open",
                "category": "software",
                "age_days": 1,
                "priority": "high"
            }
        ],
        [],
        0   
    )

    check_selection(
        select_follow_up,
        [
            {
                "id": "T301",
                "status": "open",
                "category": "software",
                "age_days": 2,
                "priority": "high"
            }
        ],
        ["T301"],
        0
    )

    check_selection(
        select_follow_up,
        [
            {
                "id": "T302",
                "status": "open",
                "category": "software",
                "age_days": 3,
                "priority": "high"
            }
        ],
        ["T302"],
        0
    )

    check_selection(
        select_follow_up,
        [
            {
                "id": "T303",
                "status": "closed",
                "category": "software",
                "age_days": 5,
                "priority": "high"
            }
        ],
        [],
        0
    )

    ## Revised follow-up selection tests

    ## Test 1: High-priority alternative qualifies
    check_selection(
        select_follow_up,
        [
            {
                "id": "T400",
                "status": "open",
                "category": "software",
                "age_days": 2,
                "priority": "high"
            }
        ],
        ["T400"],
        0
    )

    ## Test 2: Access-category alternative qualifies
    check_selection(
        select_follow_up,
        [
            {
                "id": "T401",
                "status": "open",
                "category": "access",
                "age_days": 2,
                "priority": "normal"
            }
        ],
        ["T401"],
        0
    )

    ## Test 3: Closed ticket cannot qualify
    check_selection(
        select_follow_up,
        [
            {
                "id": "T402",
                "status": "closed",
                "category": "access",
                "age_days": 5,
                "priority": "high"
            }
        ],
        [],
        0
    )

    ## Test 4: A one-day-old ticket cannot qualify
    check_selection(
        select_follow_up,
        [
            {
                "id": "T403",
                "status": "open",
                "category": "access",
                "age_days": 1,
                "priority": "high"
            }
        ],
        [],
        0
    )

    ## Test 5: Changed result under the Thursday policy
    check_selection(
        select_follow_up,
        [
            {
                "id": "T404",
                "status": "open",
                "category": "software",
                "age_days": 3,
                "priority": "normal"
            }
        ],
        [],
        0
    )

    ## Test 6: Preserved result under the Thursday policy
    check_selection(
        select_follow_up,
        [
            {
                "id": "T405",
                "status": "open",
                "category": "access",
                "age_days": 3,
                "priority": "normal"
            }
        ],
        ["T405"],
        0
    )




def main():
    """Run real checks without allowing unfinished or disabled tests to pass."""
    if not __debug__:
        raise RuntimeError("Run tests without Python optimization (-O).")
    assignment_checks()
    print("Assignment checks passed.")


if __name__ == "__main__":
    main()
