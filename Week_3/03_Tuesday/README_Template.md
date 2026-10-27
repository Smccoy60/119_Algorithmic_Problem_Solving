# AL03: Ticket Registry, Queue, and Undo

Name: Sarah Imhoff
Partners: None
Shared repository: (https://github.com/Smccoy60/119_Algorithmic_Problem_Solving/tree/main/Week_3/03_Tuesday)
My contribution: Completed the Monday registry, lookup, priority update, category filter work. Completed the Tuesday queue, processing, undo functions, tests and main program demonstration.

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
| Update one ticket's priority | Dictionary works better because I can access one ticket by its ID and update only that ticket's priority. |
| Select tickets in a category | A  scan is needed because multiple tickets can have the same category, so the tickets need to be checked for matches. |

## Work Notes and Reflections

* Tuesday
- I learned that a deque works well for pending tickets because tickets are processed in the order they were added.  T301 was added first and processed first, followed by T302
- I learned that the undo list works in the opposite order.  After processing T301 and then T302, the first undo restored T302 and the second undo restored T301.
- Preserving changes: I learned that undo should restore only the information that needs to be reversed.  Restoring a ticket's previous status should not undo an unrelated priority change.
- I had to make sure the state used the key undo consistently because the supplied display code expected state["undo].  I also corrected a test so that after processing two tickets, the undo list contained a record for both T301 and T302.

* Monday
- I learned that using a dictionary makes it easier to find and update one ticket when the ticket ID is used as the key.
- I learned that making an independent copy is important when I need to compare the state before and after an operation.  If I only create an alias, it change along with the live state and does not preserve the original values. 


## Assistance

I used AI to help understand FIFO queue processing with a deque, LIFO undo behavior, and preserving unrelated ticket changes during an undo.  

I used AI to help explain the Monday assignment requirements, understand the starter code, and work through the tests.  I reviewed the suggested changes, ran the tests, and checked the program output.  I also used AI to help understand the difference between list scanning and disctionary lookup.  The supplied ticket data and display modules were left as provided. 

## Instructor Comments

[Reserved for instructor feedback.]
