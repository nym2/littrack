# littrack
LitTrack is a Python-based CLI application that helps users manage their personal library. It enables users to categorize their books, carry out CRUD operations, and effectively keep track of their reading lists.

# Features
 1. Create, view, update, and delete books.
 2. Categorize books into genres.
 3. View all books in a specific category.
 4. User-friendly command-line interface (CLI).
 5. Database management with SQLAlchemy and Alembic for migrations.

# Technologies Used
 1. Python
 2. SQLAlchemy (ORM)
 3. Alembic (Database migrations)
 4. SQLite (Database)
 5. Pipenv (Virtual environment and dependency management)

# Installation
 1. Clone the repository:
 git clone <repository-url>
 cd littrack

  2. Install dependencies using Pipenv:
  pipenv install

 3. Activate the virtual environment:
  pipenv shell

 4. Set up the database:
  alembic upgrade head

# Usage
 1. Run the application:
  python cli.py
 2. Follow the on-screen prompts to manage categories and books.


 
 
 


