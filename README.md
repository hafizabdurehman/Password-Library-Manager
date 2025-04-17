# Password-Library-ManagerOverview
The Personal Library Manager is a Python-based command-line application that allows you to manage a personal library. With this app, you can add, remove, and search for books, as well as view statistics about your collection. It also supports saving and loading your library from a library.json file to persist your data between sessions.

Key Features
Add Books: Add new books with title, author, publication year, genre, and read status.
Remove Books: Remove books by title (supports multiple books with the same title).
Search Books: Search for books by title or author.
Display Library: View all books in the library sorted by title.
Library Statistics: View total books, read books, unread books, and genre breakdown.
Persistent Data: Save the library to a library.json file, automatically loaded on startup.
Sample Books: On first run, the app automatically adds sample books for demonstration.
Requirements
Python 3.x
No additional libraries are required. It uses only built-in Python modules like os, json, and datetime.
How to Run
Clone or download the project to your local machine.

Make sure Python 3.x is installed on your system.

Run the script by executing:

python library_manager.py
This will start the application and prompt you with the main menu.

How to Use
Upon running the application, you will be greeted with the main menu. The available actions are:

Add a book: Allows you to add a new book to your library.
Remove a book: Lets you remove a book by title.
Search for a book: Search for a book by title or author.
Display all books: View all books in the library, sorted by title.
Display statistics: View your library's statistics such as total books, read/unread status, and genre breakdown.
Exit: Exit the application.
After any action, you will be given the option to either return to the main menu or exit the application.

File Structure
- library_manager.py        # Main Python script with the library manager logic
- library.json              # JSON file storing the library data (automatically created after first run)
Code Explanation
Core Functions:
load_library(): Loads the library data from the library.json file (if it exists).
save_library(): Saves the current library to the library.json file.
add_sample_books(): Adds sample books to the library on the first run.
display_books(): Displays the books in the library sorted by title.
add_book(): Prompts the user to add a book to the library.
remove_book(): Prompts the user to remove a book by title.
search_book(): Allows the user to search for books by title or author.
display_statistics(): Displays statistics about the library such as total books, read/unread status, and genre breakdown.
main_menu(): Displays the main menu with options.
run(): Starts the application, showing the main menu and handling user inputs.
show_exit_option(): After performing any action, this method gives the user the option to return to the main menu or exit.
Data Storage:
The library data is stored in a library.json file in JSON format. This file is created automatically the first time the application runs. The data includes each book's title, author, year, genre, and read status.
Example Interaction
Welcome to your Personal Library Manager!

1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit

Enter your choice (1-6): 1
--- Add a Book ---
Enter the book title: The Catcher in the Rye
Enter the author: J.D. Salinger
Enter the publication year: 1951
Enter the genre: Fiction
Have you read this book? (yes/no): yes
Book added: 'The Catcher in the Rye' by J.D. Salinger

Press 'E' to exit or 'M' to go back to the main menu: M
Notes
The app automatically saves the library data after each action (add, remove, etc.).
Books are stored in a sorted order by title.
The program will display an error message if an invalid input is entered.
License
This project is licensed under the MIT License.
