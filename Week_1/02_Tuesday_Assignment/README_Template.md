# AL01: Ticket Rules and Follow-Up

Name: Sarah Imhoff
Partners: None
Shared repository: [https://github.com/Smccoy60/119_Algorithmic_Problem_Solving/tree/main/Week_1/02_Tuesday_Assignment]
My contribution: Built the program

## Run

Keep the following files in the same folder:

-01_main_copy.py
-ticket_data.py
-test_assignment.py
-console_style.py

Run the application:
```powershell
python main_copy_01.py
```

Run the assignment checks:
```powershell
python test_assignment.py
```

Expected test output: 
```text
Assignment checks passed
```

## Tuesday Progress Notes
* I added test cases for tickts that were 1 day old, 2 days old, and 3 days old.  These tests helped verify that the follow-up policy was workign correctly. During testing, I discovered that exactly 2 days old should qualify, so teh age comparison needed to use '>=2'.

* I also discovered that my closed-ticket test had an incorrect expected rsults.  After correcting the test, all assignment checks passed. 

* This assignment helped me understand how important boundary testing is.

## Work Notes and Reflections

- Used >= 2 because the assignment says the ticket is open AND at least two days old. When asked if "does exactly two days satisfy "at least two"?  The answer is yes. 
- T10 is invalid becuase a Boolean is not a recorded number of days
- T11 is missing age_days so this ticket is invalid
- T12 has a status of "waiting" and only open and closed appear to be valid statuses, so this ticket is invlaid. 
- Created a validate_ticket() function to check ticket data before it is used. 
- Learned that Boolean values such as True and False should not be accepted as valid age_days values.
- Created a select_open_tickets() function to separate valid open tickets from invalid records.
- Built a show_report() function to display selected tickets and validation message in a readable format.
- Encountered an issue where only one ticket was displayed.  I discovered that the return statement was accidentally indented inside the loop, causing the function to stop after the first record.
- Encountered an issue with an incorrect if/else indentation in show_report(). Fixing the indentation allowed the output to display correctly.
- Verified that valid open tickets were selected while closed tickets were excluded from the report.
- Confirmed that invalid records T10, T11, and T12 produced validation messages as expected.
- Created custom assignment checks to verify empty data, valid open tickts, and valid closed tickets.
- Learned how assert statements are used to compare expected results with actual program output. 
- Confirmed that open tickets are selected correctly and closed tickets are excluded from the report. 
- While creating assignment checks, I initially received a NotImplemented-Error because the test file was referencing unfiished starter code.  After updating the import and creating focused test cases, the checks ran successfully and displayed "Assignmetn checks passed."


## Code Explanation

Main_Copy_01 -
    needs_follow_up - 
        Creates a function named needs_follow_up. The function accepts one ticket at a time.  The ticket is stroed in the variable ticket. Example: id: T100, status: open, age_days: 3.  When the function runs, ticket contains all of that information. The next line checks whether both requirements are true, first if the ticket is open and then is the ticket at least 2 days old? The 'and' means both conditions must be true.  If both conditions are true, the function returns true, meaning that this ticket needs follow up. If the statement is not true, the fucntions reaches this line and means that the ticket is closed or the ticket is younger than 2 days, the function would return false.  This means that the ticket does not need follow-up.  

    select_follow_up(records) - 
        Create empty lists one that stores tickets that qualify and one that stores validation problems.  Look through every ticket one at a time.  Runs the validation code. If the teicket is bad, save thos emessages.  Otherwise check the follow up rules, only the vlaid tickets continue. At this point we will call the function that is built.  It will add matching tickets to the results list and return both lists.   

    validate_ticket(ticket) - 
        Checks one ticket to make sure the data is valid.  This creates an empty list called issues.  Gets the ticket ID. Check whether the age_days exists. Check whether age_days is a Boolean value. Check whether age_days in an integer. Check whether staus is eitehr "open" or "closed". Add messages to the issues list if problems are found. Returns the list of issues

    select_open_tickets(records) - 
        Looks through every ticket and decides whether it belongs in the open-ticket report. This creates an empty selected list. Creates an empty issues list.  Loops through every ticket in teh records list. Calls validate_ticket() for each ticket. If validation problems exist, add them to the issues list.  If no problems exist and teh ticket is open, add it to selected. Return both lists.

    show_report(totle, policy, selected, issues) - 
        Displays the results ina readable format. Prints a report heading. Prints the report title. Prints the policy being used. Shows the number of selected tickets. Displays information for each selected ticket. Prints the Checkign Messages section. Shows validation problems if any exist. Displays a success message if no issues were found. 

    main() - 
        This runs the program. calls select_open_tickets(TICKETS). Stores results in selected and isssues. Passes those values to show_report(). Displays the completed report. 

test_assignment.py
    from main_copy_01 import
        This imports the function that was created in main_copy_01. Allows the test file to run the function automatically.  Without this line, the test file wouldn't know where the select_open_tickets() is located.
    
    def check_selection -
        This creates a reusable testing function instead of writing the same test code over and over, values are passed into this function.

        Test # 1 - 
            this tests the Tuesday function. Starts the list of tickets and then one ticket dictionary. looks for Ticket ID T300, gets the status of open. The important test value is 1 as this ticket is only 1 day old. Close ticket and list.  No ticket should be selected. Expected issue count = 0, so no validation problems.
    
        Test #2 - 
            The assignment states that exactly two days qualifies. This status is open AND the age_days is 2 so T301 should be returned.  

        Test #3 - 
            This is an open ticket that has an age of greater than 2, so it should be selected. 

        Test #4 - 
            In this test the age passes, but the status of closed fails, so no ticket selected. 

     def check_selection -
        This creates a reusable testing function instead of writing the same test code over and over, values are passed into this function.

        selected, issues = selector(records) -
            this runs the function. For example: select_open_tickets(records) runs and saves the results into two variables (selected, issues).
    
        assert [record["id"] for record in selected] == expected_ids - 
            This checks whether the selected ticket IDs match what we expected. Example "T100" must equal "T100". If they don't match, Python stops and reports an error. 
    
        assert len(issues) == expected_issue_count - 
            this counts how many validation issues were produced. For example len(issues) might be 0 or 3 and it compares that number to what we expected. 
    
        assert all(isinstance(issue, str) and issue.strip() for issue in issues) - 
            This makes sure every issue: is a string and is not blank.   Examples: T10: invalid status
    
    def assignment_checks - 
        This is where the custom tests are created.  Each test checks a specific situation. 

        Test #1 - Input: [] = No tickets.  Expected selected tickets: [] = No tickets selected. Expected issues: 0 = No issues found

        Test #2 - Input: one valid open ticket. Expected result: T100 becuase open tickets should be selected.  Expected Issues 0 becuase the    ticket is valid

        Test #3 - Input: one valid closed ticket. Expected result: [] becuase closed tickets shoudl not appear in the open-ticket report. Expected issues 0 becuase the ticket itself is valid. 
    

## Assistance

Used AI to troubleshooot indentation issues, and verify expected output.  All code was reviewed, tested, adn adjusted before submission. Supplied files included ticket_data.py, main.py, test_assignment.py, adn console_style.py

## Instructor Comments

[Reserved for instructor feedback.]
