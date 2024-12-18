import sys
from database.db import SessionLocal
from database.models import Category, Book

def main_menu():
    """
    Displays the main menu and handles user input.
    """
    while True:
        print("\n--- Main Menu ---")
        print("1. Manage Categories")
        print("2. Manage Books")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            manage_categories()
        elif choice == "2":
            manage_books()
        elif choice == "3":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def manage_categories():
    """
    Displays the category management menu.
    """
    while True:
        print("\n--- Manage Categories ---")
        print("1. Create a Category")
        print("2. View All Categories")
        print("3. Find a Category")
        print("4. Delete a Category")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            create_category()
        elif choice == "2":
            view_categories()
        elif choice == "3":
            find_category()
        elif choice == "4":
            delete_category()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def create_category():
    """
    Creates a new category.
    """
    name = input("Enter the category name: ")
    session = SessionLocal()
    try:
        # Check for duplicate category
        existing_category = session.query(Category).filter_by(name=name).first()
        if existing_category:
            print(f"Category '{name}' already exists.")
            return

        new_category = Category(name=name)
        session.add(new_category)
        session.commit()
        print(f"Category '{name}' added successfully!")
    except Exception as e:
        print("Error creating category:", e)
    finally:
        session.close()

def view_categories():
    """
    Displays all categories.
    """
    session = SessionLocal()
    try:
        categories = session.query(Category).all()
        if categories:
            print("\n--- Categories ---")
            for category in categories:
                print(f"ID: {category.id}, Name: {category.name}")
        else:
            print("No categories found.")
    finally:
        session.close()

def find_category():
    """
    Finds a category by name or ID.
    """
    session = SessionLocal()
    try:
        search = input("Enter category name or ID: ")
        if search.isdigit():
            category = session.query(Category).filter_by(id=int(search)).first()
        else:
            category = session.query(Category).filter_by(name=search).first()
        
        if category:
            print(f"Category found: ID: {category.id}, Name: {category.name}")
        else:
            print("Category not found.")
    finally:
        session.close()

def delete_category():
    """
    Deletes a category by ID.
    """
    session = SessionLocal()
    try:
        category_id = input("Enter the ID of the category to delete: ")
        category = session.query(Category).filter_by(id=int(category_id)).first()
        if category:
            session.delete(category)
            session.commit()
            print(f"Category '{category.name}' deleted successfully!")
        else:
            print("Category not found.")
    except Exception as e:
        print("Error deleting category:", e)
    finally:
        session.close()

def manage_books():
    """
    Displays the book management menu.
    """
    while True:
        print("\n--- Manage Books ---")
        print("1. Create a Book")
        print("2. View All Books")
        print("3. Find a Book")
        print("4. Delete a Book")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            create_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            find_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def create_book():
    """
    Creates a new book and associates it with a category.
    """
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    category_id = input("Enter the category ID: ")

    session = SessionLocal()
    try:
        category = session.query(Category).filter_by(id=int(category_id)).first()
        if not category:
            print("Category not found. Book not created.")
            return

        new_book = Book(title=title, author=author, category_id=category.id)
        session.add(new_book)
        session.commit()
        print(f"Book '{title}' by {author} added successfully!")
    except Exception as e:
        print("Error creating book:", e)
    finally:
        session.close()

def view_books():
    """
    Displays all books with their details.
    """
    session = SessionLocal()
    try:
        books = session.query(Book).all()
        if books:
            print("\n--- Books ---")
            for book in books:
                print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Category: {book.category.name}")
        else:
            print("No books found.")
    finally:
        session.close()

def find_book():
    """
    Finds a book by title or ID.
    """
    session = SessionLocal()
    try:
        search = input("Enter book title or ID: ")
        if search.isdigit():
            book = session.query(Book).filter_by(id=int(search)).first()
        else:
            book = session.query(Book).filter_by(title=search).first()

        if book:
            print(f"Book found: ID: {book.id}, Title: {book.title}, Author: {book.author}, Category: {book.category.name}")
        else:
            print("Book not found.")
    finally:
        session.close()

def delete_book():
    """
    Deletes a book by ID.
    """
    session = SessionLocal()
    try:
        book_id = input("Enter the ID of the book to delete: ")
        book = session.query(Book).filter_by(id=int(book_id)).first()
        if book:
            session.delete(book)
            session.commit()
            print(f"Book '{book.title}' deleted successfully!")
        else:
            print("Book not found.")
    except Exception as e:
        print("Error deleting book:", e)
    finally:
        session.close()

if __name__ == "__main__":
    main_menu()
