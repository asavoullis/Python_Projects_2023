# Define the Book class to represent books with their attributes
class Book:
    def __init__(self, id, title, content) -> None:
        # Initialize book attributes
        self.id = id
        self.title = title
        self.content = content
        self.last_page = 0
        self.bookmarks = []
        self.ratings = []  # List of user ratings (e.g., 1 to 5 stars)
        self.reviews = []  # List of user reviews

    # Method to display a specific page of the book
    def display_page(self, page_number):
        # Check if the page number is valid
        if 1 <= page_number <= len(self.content):
            self.last_page = page_number - 1
            return self.content[self.last_page]
        else:
            return "Page not found."

    # Method to add a bookmark to a specific page
    def add_bookmark(self, page_number):
        if 1 <= page_number <= len(self.content) and page_number not in self.bookmarks:
            self.bookmarks.append(page_number)

    # Method to remove a bookmark from a specific page
    def remove_bookmark(self, page_number):
        if page_number in self.bookmarks:
            self.bookmarks.remove(page_number)

    # Method to add a user rating to the book
    def add_rating(self, rating):
        if 1 <= rating <= 5:  # Assuming a 5-star rating system
            self.ratings.append(rating)
        else:
            print("Insert number from 1 to 5")

    # Method to add a user review to the book
    def add_review(self, review):
        self.reviews.append(review)

# Define the Library class to manage a collection of books
class Library:
    def __init__(self):
        # Initialize the library's attributes
        self.collection = {}  # Dictionary to store books (ID to Book object)
        self.active_book = None  # ID of the currently active book
        self.id_counter = 0  # Counter to assign unique IDs to books
    
    # Method to add a new book to the library's collection
    def add_to_collection(self, title, content):
        new_book = Book(self.id_counter, title, content)
        self.collection[new_book.id] = new_book
        self.id_counter += 1

    # Method to remove a book from the library's collection by its ID
    def remove_from_collection(self, id):
        if id in self.collection:
            del self.collection[id]
            if self.active_book == id:
                self.active_book = None

    # Method to set an active book by its ID
    def set_active_book(self, id):
        if id in self.collection:
            self.active_book = id
            # Reset last_page when switching books
            self.collection[self.active_book].last_page = 0

    # Method to display the current page of the active book
    def display_page(self, page_number=None):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            if page_number is None:
                page_number = active_book.last_page + 1
            return active_book.display_page(page_number)
        else:
            return "No active book selected."

    # Method to turn the page of the active book
    def turn_page(self, page_number=None):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            if page_number is None:
                page_number = active_book.last_page + 2  # Turn to the next page
            return active_book.display_page(page_number)
        else:
            return "No active book selected."
        
    # Method to get information about the currently active book
    def get_active_book_info(self):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            return f"Title: {active_book.title}\n" \
                   f"Current Page: {active_book.last_page + 1}\n" \
                   f"Total Pages: {len(active_book.content)}\n" \
                   f"Bookmarks: {active_book.bookmarks}\n" \
                   f"Ratings: {active_book.ratings}\n" \
                   f"Reviews: {active_book.reviews}"
        else:
            return "No active book selected."

    # Method to add a bookmark to the active book
    def add_bookmark(self, page_number):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            active_book.add_bookmark(page_number)
            return f"Bookmark added to page {page_number} of {active_book.title}"
        else:
            return "No active book selected."

    # Method to remove a bookmark from the active book
    def remove_bookmark(self, page_number):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            active_book.remove_bookmark(page_number)
            return f"Bookmark removed from page {page_number} of {active_book.title}"
        else:
            return "No active book selected."

    # Method to add a rating to the active book
    def add_rating_to_active_book(self, rating):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            active_book.add_rating(rating)
        else:
            return "No active book selected."

    # Method to add a review to the active book
    def add_review_to_active_book(self, review):
        if self.active_book is not None:
            active_book = self.collection[self.active_book]
            active_book.add_review(review)
            print("Review added to active book")
        else:
            return "No active book selected."
        
    # Method to get the titles of all books in the library
    def get_all_books(self):
        return [book.title for book in self.collection.values()]

# Example usage:

# Initialize a Library instance
library = Library()

# Add books to the library
library.add_to_collection("Book 1", ["Page 1 content.", "Page 2 content.", "Page 3 content."])
library.add_to_collection("Book 2", ["Page 1 content.", "Page 2 content."])

# Add short stories to the library
library.add_to_collection("Short Story 1", ["Page 1 content.", "Page 2 content.", "Page 3 content."])
library.add_to_collection("Short Story 2", ["Page 1 content.", "Page 2 content."])

print("")
print("Books in Library:")
all_books = library.get_all_books()
for book_title in all_books:
    print(book_title)

# remove 1 book from the library
# ids start from 0 for books
library.remove_from_collection(3)

print("")
print("Books in Library:")
all_books = library.get_all_books()
for book_title in all_books:
    print(book_title)

# Set an active book
library.set_active_book(1)  # Assuming Book 1 has an ID of 1

# Print active book info
print("")
print("Active Book Details:")
print(library.get_active_book_info())

# # Display the current page of the active book
print("")
print("Display page of current active book:")
current_page = library.display_page()
print(current_page)  # Output: "Page 1 content."

# Turn the page
print("")
print("Display next page of current active book:")
next_page = library.turn_page()
print(next_page)  # Output: "Page 2 content."

# Add a bookmark
print("")
bookmark_message = library.add_bookmark(2)
print(bookmark_message)  # Output: "Bookmark added to page 2 of Book 1"

# Display the current page with a specified page number
print("")
specified_page = library.display_page(1)
print(specified_page)  # Output: "Page 1 content."

# Remove a bookmark
print("")
bookmark_message = library.remove_bookmark(2)
print(bookmark_message)  # Output: "Bookmark removed from page 2 of Book 1"

# Add a rating to the active book
print("")
library.add_rating_to_active_book(5)

# Add a review to the active book
print("")
library.add_review_to_active_book("Nice")

# Print active book info
print("")
print("Active Book Details:")
print(library.get_active_book_info())