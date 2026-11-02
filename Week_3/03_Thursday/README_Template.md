# AL03: Ticket Registry, Queue, and Undo

Name: Sarah Imhoff
Partners: None
Shared repository: (https://github.com/Smccoy60/119_Algorithmic_Problem_Solving/tree/main/Week_3/03_Tuesday)
My contribution: Completed the Monday registry, lookup, priority update, category filtering work. Completed the Tuesday queue, processing, and undo work. Completed the Thursday queue repair, ticket cancellation, snapshot tests, final testing, and program demonstration.

## Run

Keep main.py, test_assignment.py, ticket_data.py, ticket_display.py,
console_style.py, and any other imported modules together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

## Operation Comparison

| Operation | Representation fit / reason |
| --- | --- |
| Find one ticket by ID | A dictionary is efficient because the ticket ID is the key, so I can access one ticket directly instead of scanning teh entire list. |
| Update one ticket's priority | A dictionary works well because I can locate one ticket by ID and change only its priority field. |
| Select tickets in a category | A  scan is needed because multiple tickets can have the same category, so the tickets need to be checked for matches. |

## Work Notes and Reflections

* Thursday
- Queue Repair: I learned that repair_queue can create a new queue containing only IDs that still exist in the registry. It preserves the order of valid IDs and separately reports missing IDs.
- Installing repaired state: I learned that returning a repaired queue does not automatically change the live application state. The returned queue has to be assigned back to state["pending"].
- Cancellation: I learned that an open ticket can be removed from the registry and pending queue while keeping the other waiting tickets in their original order.  Missing and completed tickets are rejected without changing the state.
- Snapshot learning: I learned that copied ticket records can be used as a historical snapshot. Changing or canceling a live ticket later does not change the values that were already saved in the copied selection.
- Testing: I used independent before-state copies when verifying rejected actions so I could accurately confirm that the registry, pending queue, and undo list remained unchanged. 

* Tuesday
- Queue Processing: I learned that a deque works well for pending tickets because tickets are processed in the order they were added.  T301 was added first and processed first, followed by T302
- Undo: I learned that the undo list works in the opposite order.  After processing T301 and then T302, the first undo restored T302 and the second undo restored T301.
- Preserving changes: I learned that undo should restore only the information that needs to be reversed.  Restoring a ticket's previous status should not undo an unrelated priority change.
- I had to make sure the state used the key undo consistently because the supplied display code expected state["undo].  I also corrected a test so that after processing two tickets, the undo list contained a record for both T301 and T302.

* Monday
- I learned that using a dictionary makes it easier to find and update one ticket when the ticket ID is used as the key.
- I learned that making an independent copy is important when I need to compare the state before and after an operation.  If I only create an alias, it change along with the live state and does not preserve the original values. 


## Assistance

I used AI to help explain the assignment requirements and work through the Monday, Tuesday and Thursday stages.  I used AI to help understand dictionary lookups, FIFO queue processing, LIFO undo behavior, repairing stale queue references, and copied historical snapshots.

I also used AI to help troubleshoot coding and assertion errors.  I reviewed the suggested changes, entered the changes into my own file, ran the programs and compared the results with the expected behaviors from the class slides.  

The supplied ticket data and display modules were left as provided. 

## Instructor Comments

[Reserved for instructor feedback.]
