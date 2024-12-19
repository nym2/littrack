# littrack
LitTrack is a Python-based CLI application designed to help users manage their personal library. It enables users to categorize their books, perform CRUD operations, and effectively keep track of their reading lists.

## Features
1. Create, view, update, and delete books.
2. Categorize books into genres.
3. View all books in a specific category.
4. Interactive and user-friendly command-line interface (CLI).
5. Database management with SQLAlchemy and Alembic for migrations.

## Technologies Used
1. Python
2. SQLAlchemy (ORM)
3. Alembic (Database migrations)
4. SQLite (Database)
5. Pipenv (Virtual environment and dependency management)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd littrack
2. Install dependencies using Pipenv:
   pipenv install
3. Activate the virtual environment:
   pipenv shell
4. Set up the database:
   alembic upgrade head

## Usage   
1. Run the application:
   python main.py
2. Follow the on-screen prompts to manage categories and books.

## Commands Overview
# Main Menu
Manage Categories: Navigate to category management options.
Manage Books: Navigate to book management options.
Exit Application: Exit the program.
# Category Options
Add a new category: Create a new category to organize books.
View all categories: List all categories in the library.
Delete a category: Remove an existing category.
# Book Options
Add a new book: Add a book with title, author, category, and description.
View all books: List all books in the library.
View books by category: List books under a specific category.
Delete a book: Remove a book by title.

## Project Structure
littrack/
│
├── alembic/             # Alembic migrations folder
├── models/              # SQLAlchemy models
│   ├── book.py          # Book model
│   ├── category.py      # Category model
│   └── __init__.py      # Models initializer
│
├── cli/                 # CLI functionality
│   ├── book_cli.py      # Book-related CLI actions
│   ├── category_cli.py  # Category-related CLI actions
│   ├── cli_app.py       # Main CLI menu logic
│   └── main.py          # Entry point for CLI
│
├── database/            # Database setup
│   ├── db.py            # Database connection and session setup
│   └── __init__.py      # Database initializer
│
├── Pipfile              # Pipenv dependencies
├── README.md            # Project description (this file)
└── main.py              # Main entry point for the application

## Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue to suggest enhancements.