# AL05: Filter, Sort, and Search Pipeline

Name: Sarah Imhoff
My contribution: On Tuesday, I implemented and tested a stable insertion sort, used the supplied filtering function, verified ordering and coutns, and tested stability, copying behavior, and unchanged source data.  On Thursday, I completed the filter, sort, and search pipeline by creating separate age-display and ID-search views, using linear and binary search, rebuilding the views after a rule change, and expanding the assignment tests.

## Run

Keep main.py, test_assignment.py, search_algorithms.py, ticket_data.py,
search_support.py, pipeline_support.py, ticket_display.py, and console_style.py together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

## Pipeline and Work Notes

- Pipeline: Source tickets -> filter eligible open tickets -> stable age sort -> age-display view -> ID-ordered search view -> search. I learned that the display view and search view can contain the same records but need different ordering because they serve different purposes.
- One request: For one request, I can start with the source tickets, filter the records that meet the requirement, build the display and search views, and then perform the requested lookup.  The age-display view is ordered by days open, while binary search requires a separate view ordered by ID.
- Repeated requests: If multiple searches are needed using teh same eligibility rule, it makes sense to build the ID-ordered search view once and reuse it. This avoids rebuilding and resorting the same records before every search.  Linear search can search the selected records directly, while binary search uses the prepared ID-ordered view.
- Issued change: I changed minimum_days from 4 to 7 and rebuilt the views instead of tryign to reuse views created under the old rule. At 4 days, the selected IDs were T403, T405, T402 and T406. At 7 days, only T403 and T405 remained eligible. T406 was removed because it only had 4 days ope. I also tested minimum_days=8, which produced empty selected, display, and search.
- Search contract: Binary search must be performed on a view ordered by the same key being searched.  For an ID search, this means using the ID-ordered search view. I also deliberately called binary search on the age-ordered display view. That violates the binary-search contract. An invalid binary search might accidntally find a target or might miss it, so the result cannot be considered reliable.
- View-relative positions: The same ticket can have different positions in different views. At minimum_days=4, linear search found T403 at postion 0 in the selected source-order view, while binary search found T403 at position 1 in the ID-ordered search view. Both positions referred to the same underlying ticket record.
- Copying/stability: My insertion sort creates a new outer list, but intentionally share the original ticket dictionaries.  Stability means records with equal keys remain in their original relative order. T403 and T405 both have 7 days open, and T403 remains before T405 because T403 appeared first in the selected input.
- Tuesday results: As minimum_days=4, the selected IDs are T403, T405, T402, and T406. After stable insertion sorting by days_open, the order is T406, T402, T403, and T405.
- Thursday views at minimum_days=4:
    - Selected/source order: T403,T405, T402, T406
    - Age-display order: T406, T402, T403, T405
    - ID-search order: T402, T403, T405, T406
- Teaching evidence: The Tuesday insertion-sort example used 6 key comparisons and 5 right-shifts. These counts describe this particular small input and are not intended to represent timing or universal algorithm costs.
- Testing: I tested empty and singleton inputs, already ordered input, reverse input, shuffled input with tied values, stable tie behavior, comparison with Python's sorted(), unchanged source data, a new outer list, and shared record identities. On Thursday, I also tested the three pipeline views, found and missing searches, the binary-search ordering contract, the rule change to 7 days, an empty selection at 8 days, view ownership, and source nonmutation.
- Debugging: 
    - During Tuesday's work, I corrected a variable-name typo and an expected trace for teh already ordered input. A three-record ordered list has two insertion steps, so the trace contains the unchanged A, B, C order twice.
    - Thursday debugging: While building the complete pipeline, I corrected several small coding issues including a parameter-name typo, missing search and display imports, a missing colon, and a misspelled append. I also corrected a test that assumed binary search had to miss T406 when used on the incorrectly ordered age view. I learned that violating the binary-search precondition does not guarantee a failed search. It means the result is nto reliable. After correcting the tests, the complete assignment checks passed.


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

I used AI to help explain the stable insertion-sort and pipeline requirements, worked through the code based on the supplied starter instructions, troubleshoot Python syntax and assertion errors, and review my test expectations.  I entered and ran the code myself, reviewed teh console output, corrected errors as they appeared, and compared my program behavior with the assignment requirements. I verified that main.py completed successfully and that test_assignment.py finished with all AL05 assignment checks passing.

## Instructor Comments

[Reserved for instructor feedback.]
