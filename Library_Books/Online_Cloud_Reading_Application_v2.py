"""
Create an Online reading application
Similar to Amazon Kindle ( for short stories )
We need help designing an actual application ( code that implements this)

A few things we are looking for:
- Users have a library of books that they can add to or remove from
- Users can set a book from their library as active
- The reading application remmebers where a user left off in a given book
- The reading application only displays a page of text at a time in the active book.

Architecture:
- Create a library where users can interact with this library 
- They can look up if a book is active 
- Remember all books in the library
- Remember active books in the library
- Remember last pages in all books in the library
- Display a page in the active book

Classes:
- Class for the library (collection of books)
    - collection of books - {id: Book()}   - we could use title if few books ( not applicable in a real world scenario )
    - active book: str  - variable correspond to a book id
- Class for the book
    - tittle: STR
    - pages/content in the book: LIST OF STRINGS (per page)
    - remember page user looked at: INT ( INDEX  off-by one - naturally book pages start from 1 whereas python from 0)
    - id:  str/int
1qw5ITr3k9E?si
"""

class Book:
    def __init__(self, id, title, content) -> None:
        self.id = id
        self.title = title
        self.content = content # now jsut a long string of chars
        self.last_page = 0

        # self.font_size = 12
        # self.chars_per_page = calculate(self.font_size)
    
    def display_page(self):
        return self.content[self.last_page]
        # start_index = self.chars_per_page * self.last_page
        # end_index = start_index + self.chars_per_page 
        # return self.content[start_index : end_index]

    def turn_page(self):
        self.last_page += 1 
        return self.display_page()
    
class Library:
    def __init__(self):
        self.collection = dict()
        self.active_book = None
        self.id_counter = 0

    
    def add_to_collection(self, title, content):
        new_book = Book(self.id_counter, title, content)
        self.collection[new_book.id] = new_book
        self.id_counter += 1
    

    def remove_from_collection(self, id):
        del self.collection[id]

    def set_active_book(self, id):
        self.active_book = id
    
    def display_page(self):
        return self.collection[self.active_book].display_page()

    def turn_page(self):
        return self.collection[self.active_book].turn_page()

# Initialize a Library instance
library = Library()

# Add books to the library
library.add_to_collection("Book 1", "This is the content of Book 1.")
library.add_to_collection("Book 2", "This is the content of Book 2.")
library.add_to_collection("Book 3", "This is the content of Book 3.")

# Set an active book
library.set_active_book(1)  # Assuming Book 1 has an ID of 1

# Display the current page of the active book
current_page = library.display_page()
print(current_page)  # Output: "This is the content of Book 1."

# Turn the page to read the next page
next_page = library.turn_page()
print(next_page)  # Output: "This is the content of Book 1."

# Let's simulate turning the page multiple times
for _ in range(5):
    next_page = library.turn_page()
    print(next_page)  # Output: "This is the content of Book 1." (repeated 5 times)

# Set a different book as the active book
library.set_active_book(2)  # Assuming Book 2 has an ID of 2

# Display the current page of the new active book
current_page = library.display_page()
print(current_page)  # Output: "This is the content of Book 2."
