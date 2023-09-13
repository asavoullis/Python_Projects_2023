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
        self.content = content 
        self.last_page = 0

 
    def display_page(self):
        return self.content[self.last_page]
        

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
