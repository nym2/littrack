# cli/author_cli.py

from database.db import SessionLocal
from models.author import Author
from database.db import session

# Function to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to add an author
def add_author(author_name):
    db = next(get_db())
    existing_author = db.query(Author).filter(Author.name == author_name).first()
    if existing_author:
        print(f"Author '{author_name}' already exists.")
        return
    new_author = Author(name=author_name)
    db.add(new_author)
    db.commit()
    print(f"Author '{author_name}' added successfully.")


# Function to view all authors
def view_authors():
    db = next(get_db())
    authors = db.query(Author).all()

    if not authors:
        print("No authors found.")
        return

    print("Authors:")
    for author in authors:
        print(f"- Author: {author.name}")

# Function to delete an author
def delete_author(author_name):
    """Delete an author by name."""
    author = session.query(Author).filter(Author.name == author_name).first()
    if author:
        session.delete(author)
        session.commit()
        print(f"Author '{author_name}' deleted successfully.")
    else:
        print(f"No author found with the name '{author_name}'.")

# Function to show the author management menu
def show_author_menu():
    while True:
        print("\nManage Authors:")
        print("1. Add a new author")
        print("2. View all authors")
        print("3. Delete an author")
        print("4. Back to Main Menu")
        choice = input("Enter a number: ").strip()

        if choice == "1":
            author_name = input("Enter the author's name: ").strip()
            if author_name:
                add_author(author_name)  
            else:
                print("Author name cannot be empty.")
        elif choice == "2":
            view_authors()
        elif choice == "3":
            author_name = input("Enter the author's name to delete: ").strip()
            if author_name:
                delete_author(author_name)
            else:
                print("Author name cannot be empty.")
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")


