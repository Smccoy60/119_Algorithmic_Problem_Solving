"""Optional unfinished test scaffold; students choose expected lookup answers."""

from main import scan_lookup, build_index, indexed_lookup
from catalog_data import BOOKS, validate_book_ids


def assignment_checks():
    """Run focused checks based on AL02's lookup contracts."""
    validate_book_ids(BOOKS)

    index = build_index(BOOKS)
    expected_first = BOOKS[0]
    expected_last = BOOKS[-1]

    #First Record
    assert scan_lookup(BOOKS, "B1") == expected_first
    assert indexed_lookup(index, "B1") == expected_first

    #Last Record
    assert scan_lookup(BOOKS, "B4") == expected_last
    assert indexed_lookup(index, "B4") == expected_last

    #Missing Record
    assert scan_lookup(BOOKS, "B99") is None
    assert indexed_lookup(index, "B99") is None

    #Empty Input
    assert scan_lookup([], "B1") is None
    empty_index = build_index([])
    assert indexed_lookup(empty_index, "B1") is None


def main():
    """Reject unfinished or disabled tests before reporting success."""
    if not __debug__:
        raise RuntimeError("Run tests without Python optimization (-O).")
    assignment_checks()
    print("Assignment checks passed.")


if __name__ == "__main__":
    main()
