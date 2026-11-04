# AL05: Filter, Sort, and Search Pipeline

Name: Sarah Imhoff
My contribution: For Tuesday, I implemented and tested a stable insertion sort, used the supplied open-ticket filter, verified the expected age ordering and counts, and tested stability, copying behavior, and unchanged source data.

## Run

Keep main.py, test_assignment.py, search_algorithms.py, ticket_data.py,
search_support.py, pipeline_support.py, ticket_display.py, and console_style.py together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

## Pipeline and Work Notes

- Pipeline: Source tickets -> filter eligible open tickets -> stable age sort -> display view.  The search-view and lookup steps will be added during the Thursday portion of the assignment.
- One request: For one request, I can start with the source tickets, filter the records that meet the requirement, and create the ordered view needed for that request.  This does require the filtering and sorting setup before displaying the results.
- Repeated requests: To be completed Thursday.
- Issued change: To be completed Thursday.
- Copying/stability or debugging learning: My insertion sort creates a new outer list, but the ticket dictionaries inside the new list are the same record objects as the source.  I also learned that stability means records with equal keys stay in their original relative order. T403 and T405 both have 7 days open, so T403 remains before T405 after sorting because it appeared first in the selected input.
- Tuesday results: As minimum_days=4, the selected IDs are T403, T405, T402, and T406. After stable insertion sorting by days_open, the order is T406, T402, T403, and T405.
- Teaching evidence: The Tuesday example used 6 key comparisons and 5 right-shifts. These counts describe this particular small input and are not intended to represent timing or universal algorithm costs.
- Testing: I tested empty and singleton inputs, already ordered input, reverse input, shuffled input with tied values, stable tie behavior, comparison with Python's sorted(), unchanged source data, a new outer list, and shared record identities.
- Debugging: While testing, I corrected a variable-name typo and an expected trace for the already ordered input. The three-record ordered input has two insertion steps, so the trace contains the unchanged A,B,C order twice. Working through the trace helped me understand that the trace records the list after every insertion even when no right-shift happens.


## Assistance

The following files were supplied with the AL05 assignment:
* ticket_data.py
* serach_suppory.py
* pipeline_support.py
* ticket_display.py
* console_style.py
* the main.py starter
* the test_assignment.py starter
* the README template

I created my local search_algorithms.py using the linear_search and binary_search functions from my completed AL04 work.

I used AI to help explain the stable insertion-sort requirements, trouble Python syntax and assertion errors, and review my test expectations.  I entered and ran the code myself, compared the console output withthe assignment requirements, corrected errors as they appeared, and checked that the final Tuesday results matched the required IDs, counts, stability behavior, and unchanged-source contract.

## Instructor Comments

[Reserved for instructor feedback.]
