import os
import json
from datetime import datetime


class LibraryManager:

    def __init__(self):

        self.library = []

        self.filename = "library.json"

        self.load_library()

        self.add_sample_books()

    def load_library(self):

        if os.path.exists(self.filename):

            try:
                
                with open(self.filename, 'r') as file:
                    
                    self.library = json.load(file)
                    
                print(f"Library loaded from {self.filename}")
                
            except Exception as e:
                
                print(f"Error loading library: {e}")

    def save_library(self):
        
        try:
            
            with open(self.filename, 'w') as file:
                
                json.dump(self.library, file, indent=4)
                
            print(f"Library saved to {self.filename}")
            
        except Exception as e:
            
            print(f"Error saving library: {e}")

    def add_sample_books(self):
        
        if not self.library:
            
            sample_books = [
                {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction", "read_status": True},
                {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian", "read_status": True},
                {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction", "read_status": True},
                {"title": "Dune", "author": "Frank Herbert", "year": 1965, "genre": "Science Fiction", "read_status": False}
            ]
            
            self.library.extend(sample_books)
            
            self.save_library()
            
            print("Sample books added!")

    def display_books(self):
        
        print("\n--- Your Library ---")
        
        if not self.library:
            
            print("Your library is empty.")
            
            return
            
        for i, book in enumerate(sorted(self.library, key=lambda x: x["title"]), 1):

            status = "Read" if book["read_status"] else "Unread"

            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

    def add_book(self):

        print("\n--- Add a Book ---")

        title = input("Enter the book title: ")

        if not title: print("Title cannot be empty!"); return

        author = input("Enter the author: ")

        if not author: print("Author cannot be empty!"); return

        try:

            year = int(input("Enter the publication year: "))

            if year < 1000 or year > datetime.now().year: print(f"Enter a valid year between 1000 and {datetime.now().year}"); return

        except ValueError: print("Please enter a valid year!"); return

        genre = input("Enter the genre: ")

        read_status = input("Have you read this book? (yes/no): ").lower() in ["yes", "y"]

        self.library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})

        self.save_library()

        print(f"Book added: '{title}' by {author}")

    def remove_book(self):

        print("\n--- Remove a Book ---")

        if not self.library: print("Your library is empty."); return

        title = input("Enter the title of the book to remove: ")

        matching_books = [book for book in self.library if book["title"].lower() == title.lower()]

        if not matching_books: print(f"No book found with title '{title}'"); return

        if len(matching_books) == 1:

            book = matching_books[0]

            self.library.remove(book)

            self.save_library()

            print(f"Book removed: '{book['title']}' by {book['author']}")

        else:

            print(f"Found {len(matching_books)} books with title '{title}':")

            for i, book in enumerate(matching_books, 1): print(f"{i}. {book['title']} by {book['author']}")

            try:

                choice = int(input("Enter the number of the book to remove: "))

                if 1 <= choice <= len(matching_books):

                    book = matching_books[choice - 1]

                    self.library.remove(book)

                    self.save_library()

                    print(f"Book removed: '{book['title']}' by {book['author']}")

                else: print("Invalid selection.")

            except ValueError: print("Invalid number.")

    def search_book(self):

        print("\n--- Search for a Book ---")

        if not self.library: print("Your library is empty."); return

        search_field = input("Search by (1) Title or (2) Author: ").strip()

        if search_field not in ['1', '2']: print("Invalid choice."); return

        search_term = input("Enter the search term: ")

        matching_books = [book for book in self.library if search_term.lower() in book['title' if search_field == '1' else 'author'].lower()]

        if not matching_books: print(f"No books found matching '{search_term}'"); return

        for book in matching_books: print(f"{book['title']} by {book['author']}")

    def display_statistics(self):

        print("\n--- Library Statistics ---")

        if not self.library: print("Your library is empty."); return

        total_books = len(self.library)

        read_books = sum(1 for book in self.library if book["read_status"])

        print(f"Total books: {total_books}\nRead books: {read_books}\nUnread books: {total_books - read_books}")

        print("\nGenre breakdown:")

        genres = {}

        for book in self.library:

            genre = book["genre"] if book["genre"] else "Unspecified"

            genres[genre] = genres.get(genre, 0) + 1

        for genre, count in sorted(genres.items(), key=lambda x: x[1], reverse=True):

            print(f"  {genre}: {count} books")

    def main_menu(self):

        print("\n1. Add a book\n2. Remove a book\n3. Search for a book\n4. Display all books\n5. Display statistics\n6. Exit")

    def run(self):

        print("\nWelcome to your Personal Library Manager!")

        while True:

            self.main_menu()

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.add_book()
                self.show_exit_option()

            elif choice == "2":
                self.remove_book()
                self.show_exit_option()

            elif choice == "3":
                self.search_book()
                self.show_exit_option()

            elif choice == "4":
                self.display_books()
                self.show_exit_option()

            elif choice == "5":
                self.display_statistics()
                self.show_exit_option()

            elif choice == "6":
                print("\nGoodbye! Thank you for using the Library Manager.")

                self.save_library()

                break

            else:
                print("Invalid choice. Please select a number between 1 and 6.")

    def show_exit_option(self):

        """Shows only the exit option after any action is performed"""

        while True:

            exit_choice = input("\nPress 'E' to exit or 'M' to go back to the main menu: ").strip().upper()

            if exit_choice == 'E':

                break

            elif exit_choice == 'M':

                return
            
            else:

                print("Invalid input. Please press 'E' to exit or 'M' to return to the menu.")


if __name__ == "__main__":

    app = LibraryManager()
    
    app.run()
