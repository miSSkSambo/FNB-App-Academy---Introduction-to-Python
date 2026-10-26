
import requests

API_URL = "https://6ade7c294e88f1bba4a52733.mockapi.io/books"


def get_books():
    """GET: Retrieve all books."""
    try:
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
        books = response.json()

        print("\n========== GET ALL BOOKS ==========")
        print("Status code:", response.status_code)
        print("Total books:", len(books))

        for book in books:
            print(
                f"ID: {book.get('id')} | "
                f"Title: {book.get('title')} | "
                f"Author: {book.get('author')} | "
                f"Rating: {book.get('rating')}"
            )

        return books

    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)
    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    return None


def add_book(book):
    """POST: Add a new book."""
    try:
        response = requests.post(
            API_URL,
            json=book,
            timeout=15
        )
        response.raise_for_status()

        created_book = response.json()

        print("\n========== POST BOOK ==========")
        print("Status code:", response.status_code)
        print("Created book:", created_book)

        return created_book

    except requests.exceptions.HTTPError as error:
        print("HTTP error while adding book:", error)
    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    return None


def update_book(book_id, book):
    """PUT: Replace an existing book's details."""
    try:
        response = requests.put(
            f"{API_URL}/{book_id}",
            json=book,
            timeout=15
        )
        response.raise_for_status()

        print("\n========== PUT BOOK ==========")
        print("Status code:", response.status_code)
        print("Updated book:", response.json())

        return response.json()

    except requests.exceptions.HTTPError as error:
        print("HTTP error while updating book:", error)
    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    return None


def delete_book(book_id):
    """DELETE: Remove a book."""
    try:
        response = requests.delete(
            f"{API_URL}/{book_id}",
            timeout=15
        )
        response.raise_for_status()

        print("\n========== DELETE BOOK ==========")
        print("Status code:", response.status_code)
        print("Deleted book ID:", book_id)

        return True

    except requests.exceptions.HTTPError as error:
        print("HTTP error while deleting:", error)
    except requests.exceptions.RequestException as error:
        print("Request error:", error)

    return False


def confirm_deleted(book_id):
    """GET: Confirm a deleted book returns an HTTP error."""
    try:
        response = requests.get(
            f"{API_URL}/{book_id}",
            timeout=15
        )
        response.raise_for_status()

        print("WARNING: The book still exists.")
        print("Status code:", response.status_code)

    except requests.exceptions.HTTPError as error:
        print("\n========== DELETE CONFIRMATION ==========")
        print("The deleted book returned an HTTP error.")
        print("Status code:", error.response.status_code)

    except requests.exceptions.RequestException as error:
        print("Request error:", error)


def repair_books_without_ids(books):
    """Recreate records that do not have IDs, using POST."""
    repaired = []

    for book in books:
        if book.get("id"):
            continue

        new_book = {
            "title": book.get("title", "Untitled"),
            "author": book.get("author", "Unknown"),
            "rating": str(book.get("rating", "0"))
        }

        created = add_book(new_book)

        if not created or not created.get("id"):
            print("\nCould not recreate a book with a valid ID.")
            print("Stopping to avoid continuing with invalid records.")
            return None

        repaired.append(created)

    return repaired


def main():
    # 1. GET the existing inventory.
    books = get_books()

    if not isinstance(books, list):
        print("Could not retrieve inventory. Stopping.")
        return

    # 2. Repair old records that do not have IDs.
    if any(not book.get("id") for book in books):
        print("\n========== REPAIR MISSING IDs ==========")
        repaired = repair_books_without_ids(books)

        if repaired is None:
            return

        print("\nRecreated books:", len(repaired))

        # Reload inventory to get the generated IDs.
        books = get_books()

        if not isinstance(books, list):
            return

    # Select two distinct existing records with valid IDs.
    valid_books = [
        book for book in books
        if book.get("id")
    ]

    if len(valid_books) < 2:
        print("At least two books with valid IDs are required.")
        return

    update_id = valid_books[0]["id"]
    delete_id = valid_books[1]["id"]

    # 3. POST: Add a new book.
    new_book = {
        "title": "The Bookstore API Guide",
        "author": "Python Learning Team",
        "rating": "9"
    }

    add_book(new_book)

    # 4. PUT: Update an existing book.
    updated_book = {
        "title": "Updated Book - Revised Edition",
        "author": "Python Learning Team",
        "rating": "10"
    }

    update_book(update_id, updated_book)

    # 5. DELETE: Remove another existing book.
    deleted = delete_book(delete_id)

    # Immediately GET the deleted ID to confirm an HTTP error.
    if deleted:
        confirm_deleted(delete_id)

    # 6. GET the final inventory.
    print("\n========== FINAL INVENTORY ==========")
    get_books()


if __name__ == "__main__":
    main()
