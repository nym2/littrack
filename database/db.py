from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database for simplicity
DATABASE_URL = "sqlite:///./littrack.db"

# Create engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Base class for models
Base = declarative_base()

# Function to create all tables
def create_db():
    Base.metadata.create_all(bind=engine)
