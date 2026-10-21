"""Optional English-first starter; one recognition-level app across three days."""

from catalog_data import BOOKS, validate_book_ids

# MONDAY - Implement equivalent lookups after Monday's instruction.


def scan_lookup(records, book_id):
    """Return the first matching book, or None when absent."""
    for book in records:
        if book["id"] == book_id:
            return book
    return None


def build_index(records):
    """Map each previously validated catalog ID to its book record."""
    validate_book_ids(records)
    index = {}
    for book in records:
        index[book["id"]] = book
    return index


def indexed_lookup(index, book_id):
    """Return the indexed book or None when the catalog ID is absent."""
    return index.get(book_id)


def main():
    """Show the examples for the lookup functions you have completed."""
    validate_book_ids(BOOKS)
    catalog_index = build_index(BOOKS)
    ids_to_check = ["B1","B4","B99"]
    for book_id in ids_to_check:
        scan_result = scan_lookup(BOOKS, book_id)
        index_result = indexed_lookup(catalog_index, book_id)
        print(f"\nLooking for {book_id}")
        if scan_result:
            print(f"Scan Found: " f"{scan_result['id']} - " f"{scan_result['author']}")
        else:
            print("Scan Found: None")
        if index_result:
                print(f"Index Found: " f"{index_result['id']} - " f"{index_result['title']} by " f"{index_result['author']}")
        else:
                print("Index Found: None")



# TUESDAY - Recognize growth; wait for Tuesday's instruction.
# Inspect first_id, all_ids, ordered_pairs, and halving_sizes in growth_examples.py.
# Ask whether each examines one item, visits every item, visits every pair,
# or repeatedly reduces the remaining size.
# Give each a Big-O label and one brief reason in your README.
# Explain how a first-match scan differs from a last-match or absent-ID scan.
# Finish focused tests for empty input, repeated queries, order, and unchanged data.
# No counter function, timer, benchmark runner, or experiment report is needed.

# THURSDAY - Choose qualitatively and submit after Thursday's instruction.
# Consider a patron's one first-book request when the catalog list is available.
# Contrast it with a circulation desk's repeated IDs when an index can be reused.
# Explain construction and extra storage, not a measured speed winner.
# Add brief choices, learning, contribution, and assistance notes to the README.
# Copy the full app, data, growth examples, tests, and imported support modules
# into your own class repository; test the copy and submit your own URL.
# Keep this same main.py all week; no artificial extra feature or report.


if __name__ == "__main__":
    main()
