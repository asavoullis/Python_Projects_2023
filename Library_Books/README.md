# Online Reading Application

Welcome to the Online Reading Application, a platform designed to provide users with a seamless and enjoyable reading experience for short stories. Similar to Amazon Kindle, this application caters specifically to the world of concise narratives. Whether you're an avid reader or just looking for a quick literary escape, our platform offers an array of features to enhance your reading journey.

## Description

The Online Reading Application is an exercise in creating an efficient and user-friendly platform for reading short stories. It's not just a code implementation but a vision of what a complete reading application could offer. Here's a deeper dive into what this application is all about:

## Features

### 1. **User-Centric Library Management**

- **Library of Short Stories**: Users have a personal library where they can curate their collection of short stories.
- **Add and Remove**: Easily add new short stories to your library or remove stories that you've completed or are no longer interested in.

### 2. **Reading Convenience**

- **Set Active Story**: Choose an active short story from your library. This allows you to pick up where you left off and maintain separate reading progress for different stories.
- **Reading Progress Tracking**: The application remembers your last-read page in each short story, so you can seamlessly resume reading.

### 3. **Focused Reading Experience**

- **Single Page Display**: The application displays only one page of text at a time for the active short story, reducing distractions and enhancing concentration.
- **Page Navigation**: Effortlessly turn pages forward, allowing you to read at your own pace.

### 4. **Bookmarks and Annotations**

- **Add Bookmarks**: Bookmark your favorite pages or passages to revisit them easily or make notes.
- **Remove Bookmarks**: If you change your mind or want to keep your notes tidy, remove bookmarks as needed.

### 5. **Rich Short Story Collection**

- **Diverse Content**: Explore a diverse collection of short stories covering various genres, themes, and styles.
- **Discover New Stories**: As an evolving platform, new short stories are continually added to the library for your enjoyment.

### 6. **User-Friendly Interface**

- **Intuitive Design**: The application boasts an intuitive and user-friendly interface, making it accessible to readers of all levels of tech-savviness.
- **Seamless Navigation**: Easily switch between stories, pages, and bookmarks with minimal effort.

## Code Implementation

The application's functionality is implemented using Python, featuring two primary classes: `Book` and `Library`. These classes work in harmony to create the core features of the Online Reading Application.

### Book Class

The `Book` class represents individual short stories and provides methods for displaying pages, adding bookmarks, and more. Each book instance is designed to encapsulate the essence of a unique story.

### Library Class

The `Library` class manages the user's collection of short stories, tracks the active story, and facilitates page navigation. It is responsible for creating and maintaining the library's overall structure.

## Example Usage

To help you get started, we provide example usage of the application's core features in Python. You can build upon this code to create your own online reading application, tailored to your specific requirements.

```python
# Initialize a Library instance
library = Library()

# Add short stories to the library
library.add_to_collection("Short Story 1", ["Page 1 content.", "Page 2 content.", "Page 3 content."])
library.add_to_collection("Short Story 2", ["Page 1 content.", "Page 2 content."])

# Set an active short story
library.set_active_book(1)  # Assuming Short Story 1 has an ID of 1

# Display the current page of the active short story
current_page = library.display_page()
print(current_page)  # Output: "Page 1 content."

# Turn the page
next_page = library.turn_page()
print(next_page)  # Output: "Page 2 content."

# Add a bookmark
bookmark_message = library.add_bookmark(2)
print(bookmark_message)  # Output: "Bookmark added to page 2 of Short Story 1"

# Display the current page with a specified page number
specified_page = library.display_page(1)
print(specified_page)  # Output: "Page 1 content."

# Remove a bookmark
bookmark_message = library.remove_bookmark(2)
print(bookmark_message)  # Output: "Bookmark removed from page 2 of Short Story 1"
```

Feel free to use this code as a foundation for building your own online reading application for short stories, expanding on its features, and customizing it to meet your specific needs. Enjoy your journey into the world of short stories!

## Credits:

Charilaos Savoullis
