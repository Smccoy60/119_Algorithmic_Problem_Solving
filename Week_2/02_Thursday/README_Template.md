# AL02: Library Catalog Lookup and Big-O Recognition

Name: Sarah Imhoff
Partners: None
Shared repository: (https://github.com/Smccoy60/119_Algorithmic_Problem_Solving/tree/main/Week_2)
My contribution: Implemented scan lookup, index construction, indexed lookup, Big-O analysis, growth pattern recognition, testing, README documentation, and qualitative algorithm recommendations

## Run

Keep main.py, test_assignment.py, catalog_data.py, growth_examples.py,
and any other imported modules together.

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```
## Thursday Qualitative Decisions

- Patron's sinle B1 lookup: 
    I would recommend scan_lookup() when the catalog list is already available and no index has been built.  Since only one lookup is neede dand B1 is the first record in the catalog, the scan stops immediately and avoids teh extra work of building an index.

- Circulation desk repeated requests:
    I would recommend building an index with build_index() and using indexed_lookup() for repeated catalog searches.  Although creating the index requires an initial pass through all records, the index can be reused for many requests and each lookup is approximately O(1) on average.

- Index Construction: 
    Building the index requires O(n) work because every catalog record must be visited once and added to the dictionary.

- Additional storage: 
    The indexed approach requires O(n) additional space because the dictionary stores references to all catalog IDs and records.

- Reusing versus rebuilding: 
    Reusing an existing index is more efficient than rebuilding it for every request because the O(n) construction cost is only paid once.  Rebuilding the index for every lookup would repeatedly perform teh same work. 

- Verification: 
    The final application and tests were run successfully.  Both scan_lookup() and indexed_lookup() return the same book details for existing records and the same None result for missing records.

-Learning: The best algorithm can depend on the workload.  A simple scan may be appropriate for a single lookup, while building an index is beneficial when many repeated lookups will occur. 


## Tuesday Growth Pattern Notes

- first_id(): O(1) because it directly accesses the first record without looping through the catalog.
- all_ids(): O(n) because it visits every record one time to collect each ID.
- ordered_pairs(): O(n2) because each record is paried with every other record using nested loops. 
- halving_sizes(): O(log n) because the remaining size is reduced by approximately half during each loop iteration.

- B1 is a best-case scan because the match is found immediately at the beginning of the catalog
- B4 requires checking every record before finding a match because it is the last record in the catalog.
- B99 is a worst-case scan because the ID is not present, requiring every record to be checked before returning None.

- Repeated request testing confirmed that the same lookup returns consistent results.
- Retained request order testing confirmed that results are returned in the same order as the requested IDs.
- Unchanged record testing confirmed that scan_lookup() and build_index() do not modify the catalog data.
- Duplicate ID testing confirmed that validate_book_ids() rejects catalogs containing duplicate IDs.

- Learning: Different code patterns can have very different growth rates.  Direct access is O(1), a single loop is O(n), nested loops are O(n2), and repearted halving produces O(log n). 

## Work Notes and Reflections

- scan_lookup(): O(n) because it may need to check every book record before finding a match or determining the ID is not present.
- build_index(): O(n) because it loops through all book records once to crate the dictionary.
- indexed_lookup(): O(1) average case because dictionary key lookups are performed directly without scanning the records.
- Index storage: O(n) because an addtional dictionary is created to store all book IDs and records.

- Scan-case observation: Looking up B1 stops immediately (best case), while looking up B4 or the missing ID B99 requires checking every record 

- Workload choice 1: Looking up a single book in a small catalog.  A simple scan is acceptable because the number of records is small.
- Workload choice 2: Looking up many books repeatedly in a large catalog.  Building an index first is more efficient because each lookup is approximately O(1).

- Challenge: Understanding when to use a linear scan versus a dictionary lookup.

- Learning: Building an index requires additional memory, but it significantly improves lookup performance when many searches are needed. 


## Assistance

- Used for assistance understanding Big-O notation, validating algorithm choices and explaining growth behavior.  All code was reviewed, tested, and modified as needed before submission.  
 

## Instructor Comments

[Reserved for instructor feedback.]


