# AL02: Library Catalog Lookup and Big-O Recognition

Name: Sarah Imhoff
Partners: None
Shared repository: [URL]
My contribution: Implemented scan lookup, index construction, indexed lookup, Big-O analysis, testing and documentation

## Run

Keep main.py, test_assignment.py, catalog_data.py, growth_examples.py,
and any other imported modules together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

## Work Notes and Reflections

- scan_lookup(): O(n) because it may need to check every book record before finding a match or determining the ID is not present.
- build_index(): O(n) because it loops through all book records once to crate the dictionary.
- indexed_lookup(): O(1) average case because dictionary key lookups are performed directly without scanning the records.
- Index storage: O(n) because an addtional dictionary is created to store all book IDs and records.

- Scan-case observation: Looking up the last book or a missing book required checking more records than looking up the first book.

- Workload choice 1: Looking up a single book in a small catalog.  A simple scan is acceptable because the number of records is small.
- Workload choice 2: Looking up many books repeatedly in a large catalog.  Building an index first is more efficient because each lookup is approximately O(1).

- Challenge: Understanding when to use a linear scan versus a dictionary lookup.

- Learning: Building an index requires additional memory, but it significantly improves lookup performance when many searches are needed. 


## Assistance

- Used for assistance understanding Big-O notation, validating algorithm choices and explaining growth behavior.  All code was reviewed, tested, and modified as needed before submission.  

## Instructor Comments

[Reserved for instructor feedback.]
