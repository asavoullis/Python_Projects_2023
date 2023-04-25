class Book:
    def __init__(self, id, title, content) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.last_page = 0
        self.bookmarks = []
    
    def display_page(self, page_number):
        # Check if the page number is valid
        if 1 <= page_number <= len(self.content):
            self.last_page = page_number - 1
            return self.content[self.last_page]
        else:
            return "Page not found."

    def add_bookmark(self, page_number):
        if 1 <= page_number <= len(self.content) and page_number not in self.bookmarks:
            self.bookmarks.append(page_number)

    def remove_bookmark(self, page_number):
        if page_number in self.bookmarks:
            self.bookmarks.remove(page_number)

class Library:
    def __init__(self):
        self.collection = {}
        self.active_book = None
        self.id_counter = 0
    
    def add_to_collection(self, title, content):
        new_book = Book(self.id_counter, title, content)
        self.collection[new_book.id] = new_book
        self.id_counter += 1

    def remove_from_collection(self, id):
        if id in self.collection:
            del self.collection[id]
            if self.active_book == id:
                self.active_book = None

    def set_active_book(self, id):
        if id in self.collection:
            self.active_book = id
            # Reset last_page when switching books
            self.collection[self.active_book].last_page = 0

    def display_page(self, page_number=None):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            if page_number is None:
                page_number = active_book.last_page + 1
            return active_book.display_page(page_number)
        else:
            return "No active book selected."

    def turn_page(self, page_number=None):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            if page_number is None:
                page_number = active_book.last_page + 2  # Turn to the next page
            return active_book.display_page(page_number)
        else:
            return "No active book selected."

    def add_bookmark(self, page_number):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            active_book.add_bookmark(page_number)
            return f"Bookmark added to page {page_number} of {active_book.title}"
        else:
            return "No active book selected."

    def remove_bookmark(self, page_number):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            active_book.remove_bookmark(page_number)
            return f"Bookmark removed from page {page_number} of {active_book.title}"
        else:
            return "No active book selected."

# Example usage:

# Initialize a Library instance
library = Library()

# Add books to the library
library.add_to_collection("Book 1", ["Page 1 content.", "Page 2 content.", "Page 3 content."])
library.add_to_collection("Book 2", ["Page 1 content.", "Page 2 content."])

# Set an active book
library.set_active_book(1)  # Assuming Book 1 has an ID of 1

# Display the current page of the active book
current_page = library.display_page()
print(current_page)  # Output: "Page 1 content."

# Turn the page
next_page = library.turn_page()
print(next_page)  # Output: "Page 2 content."

# Add a bookmark
bookmark_message = library.add_bookmark(2)
print(bookmark_message)  # Output: "Bookmark added to page 2 of Book 1"

# Display the current page with a specified page number
specified_page = library.display_page(1)
print(specified_page)  # Output: "Page 1 content."

# Remove a bookmark
bookmark_message = library.remove_bookmark(2)
print(bookmark_message)  # Output: "Bookmark removed from page 2 of Book 1"
