from cli.book_cli import add_book, view_books, delete_book, view_books_by_category
from cli.author_cli import add_author, view_authors, delete_author
from cli.category_cli import add_category, view_categories, delete_category


def show_main_menu():
    while True:
        print("\nWelcome to LitTrack!")
        print("Please choose an option by number:")
        print("1. Manage Categories")
        print("2. Manage Books")
        print("3. Manage Authors")
        print("4. Exit Application")
        choice = input("Enter a number: ").strip()

        if choice == "1":
            show_category_menu()
        elif choice == "2":
            show_book_menu()
        elif choice == "3":
            show_author_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

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
            category_name = input("Enter the category name to delete: ").strip()
            if category_name:
                delete_category(category_name)
            else:
                print("Category name cannot be empty.")
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

def show_book_menu():
    print("\nBook Menu:")
    print("1. Add a Book")
    print("2. View Books")
    print("3. Delete a Book")
    print("4. Go Back")

    choice = input("Enter a number: ")

    if choice == "1":
        title = input("Enter the title of the book: ")
        author_name = input("Enter the author of the book: ")
        category_name = input("Enter the category of the book: ")
        description = input("Enter a description of the book (optional): ")
        add_book(title, author_name, category_name, description)
    elif choice == "2":
        view_books()
    elif choice == "3":
        title = input("Enter the title of the book to delete: ")
        delete_book(title)  
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")

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

if __name__ == "__main__":
    show_main_menu()
