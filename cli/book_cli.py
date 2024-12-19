# cli/book_cli.py

from database.db import SessionLocal, session
from models.book import Book
from models.author import Author
from models.category import Category

# Function to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to add a book
def add_book(title, author_name, category_name, description=None):
    author = session.query(Author).filter(Author.name == author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)

    category = session.query(Category).filter(Category.name == category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)

    existing_book = session.query(Book).filter(Book.title == title).first()
    if existing_book:
        print(f"The book '{title}' already exists in the collection.")
        return

    new_book = Book(title=title, description=description, author=author, category=category)
    session.add(new_book)
    session.commit()

    print(f"Book '{title}' by {author_name} has been added successfully under category '{category_name}'.")

# Function to view all books
def view_books():
    db = next(get_db())
    books = db.query(Book).all()

    if not books:
        print("No books found.")
        return

    print("Books:")
    for book in books:
        print(f"- Title: {book.title}, Author: {book.author.name}, Category: {book.category.name}")

# Function to view books by category
def view_books_by_category():
    category_name = input("Enter the category to view books: ").strip()
    if not category_name:
        print("Category name cannot be empty.")
        return

    db = next(get_db())
    books = db.query(Book).join(Category).filter(Category.name == category_name).all()

    if not books:
        print(f"No books found in category '{category_name}'.")
        return

    print(f"Books in category '{category_name}':")
    for book in books:
        print(f"- Title: {book.title}, Author: {book.author.name}")

# Function to delete a book
def delete_book(title):
    book = session.query(Book).filter(Book.title == title).first()
    if not book:
        print(f"Book with title '{title}' not found in the collection.")
        return

    session.delete(book)
    session.commit()
    print(f"Book '{title}' has been deleted successfully.")

# Function to show the book management menu
def show_book_menu():
    while True:
        print("\nManage Books:")
        print("1. Add a new book")
        print("2. View all books")
        print("3. View books by category")
        print("4. Delete a book")
        print("5. Back to Main Menu")
        choice = input("Enter a number: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            view_books_by_category()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")
