"""Optional English-first starter; one recognition-level app across three days."""

from catalog_data import BOOKS, validate_book_ids

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

if __name__ == "__main__":
    main()
