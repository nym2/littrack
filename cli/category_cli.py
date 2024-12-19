# cli/category_cli.py

from database.db import SessionLocal, session
from models.category import Category

# Function to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to add a category
def add_category():
    category_name = input("Enter the name of the category: ").strip()
    if not category_name:
        print("Category name cannot be empty.")
        return

    db = next(get_db())

    category = db.query(Category).filter(Category.name == category_name).first()
    if category:
        print(f"Category '{category_name}' already exists.")
        return

    new_category = Category(name=category_name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    print(f"Category '{new_category.name}' added successfully.")

# Function to view all categories
def view_categories():
    db = next(get_db())
    categories = db.query(Category).all()

    if not categories:
        print("No categories found.")
        return

    print("Categories:")
    for category in categories:
        print(f"- {category.name}")

# Function to delete a category
def delete_category(category_name):
    category = session.query(Category).filter(Category.name == category_name).first()

    if category:
        session.delete(category)  
        session.commit()          
        print(f"Category '{category_name}' has been deleted successfully.")
    else:
        print(f"Category '{category_name}' not found.")

# Function to show category management menu
def show_category_menu():
    while True:
        print("\nManage Categories:")
        print("1. Add a new category")
        print("2. View all categories")
        print("3. Delete a category")
        print("4. Back to Main Menu")
        choice = input("Enter a number: ").strip()

        if choice == "1":
            add_category()
        elif choice == "2":
            view_categories()
        elif choice == "3":
            delete_category()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")
