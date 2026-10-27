# AL03: Ticket Registry, Queue, and Undo

Name: Sarah Imhoff
Partners: None
Shared repository: (https://github.com/Smccoy60/119_Algorithmic_Problem_Solving/tree/main/Week_3/03_Monday)
My contribution: Completed the Monday registry, lookup, priority update, category filter, tests, and main program demonstration

## Run

Keep main.py, test_assignment.py, ticket_data.py, ticket_display.py,
console_style.py, and any other imported modules together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

## Operation Comparison

do not implement every operation twice or maintain two live stores.

| Operation | Representation fit / reason |
| --- | --- |
| Find one ticket by ID | Dictionary is more efficient because I can look up the ticket directly by its ID instead of scanning through the entire list. |
| Update one ticket's priority | Dictionary works better because I can access the ticket by ID and update only that ticket's priority. |
| Select tickets in a category | A list/dictionary scan is needed because multiple tickets can have the same category, so each ticket needs to be checked. |

## Work Notes and Reflections

* Monday
- I learned that using a dictionary makes it easier to find and update one ticket when the ticket ID is used as the key.
- Contract or snapshot learning: I learned that making a copy is important when I want to save the original values.  If I change a copied ticket, it does not change the live ticket in the registry. 

- Processing and undo: [one observation from two processed tickets and one undo]
- Contract or snapshot learning: [one brief observation in your own words]

## Assistance

I used AI to help explain the Monday assignment requirements, understand the starter code, and work through the tests.  I reviewed the suggested changes, ran the tests, and checked the program output.  I also used AI to help understand the difference between list scanning and disctionary lookup.  The supplied ticket data and display modules were left as provided. 

## Instructor Comments

[Reserved for instructor feedback.]
