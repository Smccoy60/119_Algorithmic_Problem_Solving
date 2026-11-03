# AL04: Search Contracts and Correctness

Name: [your name]
My contribution: [brief note; individual assignment]

## Run

Keep main.py, test_assignment.py, ticket_data.py, search_support.py,
ticket_display.py, and console_style.py together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

## Contract and Work Notes

- Ordering precondition: [why the original-list T401 binary search failed]
- Result agreement: [why positions can differ; how duplicate categories are handled]
- Reflection/debugging/learning: [brief observation; append as useful]

The two small traces can stay in console output. No separate report or essay.

## Assistance

[Supplied modules/starter and other help used, or none beyond supplied files.
For AI: tool/task and what you checked, changed, or rejected.]

## Instructor Comments

[Reserved for instructor feedback.]

## Coding Explanation - mainly for myself to keep track of what everything is doing

Creates an empty list where we'll remember everything the search checked -- trace = []
Walk through every ticket in its existing order, enumerate give mes position 0,1,2 and record give the actual ticket dictionary -- for position, record in enumerate(records):
Extracts whatever value we're searchign by -- value = key(record)
Records what was visited -- trace.append((position, value))
Checks whether the current ticket's value equals the target -- if matches(value, target):
If we find it, stop immediately and return: where it was found and everything we visited -- return position, trace
If we reach the end without finding anything -- return None, trace
