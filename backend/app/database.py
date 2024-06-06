# database.py
# Set up the database connection and ORM base class

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.data import initial_job_data
import os

# Database setup URL
DATABASE_URL = "sqlite:///./jobs.db"

# Create the engine, session, and base
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Allows usage across multiple threads
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to populate initial job data
def populate_initial_data(db: Session):
    from app.models.jobModel import Job  # Import inside the function to avoid circular import
    for job_data in initial_job_data:
        job = Job(**job_data)
        db.add(job)
    db.commit()

# Function to initialize the database
def initialize_database():
    db_file_path = "./jobs.db"  # Database path
    db_exists = os.path.exists(db_file_path)  # Check to see if the path exists (i.e., the database exists)

    # If the database doesn't exist, then create it
    if not db_exists:
        from app.models.jobModel import Job  # Import inside the function to avoid circular import
        Base.metadata.create_all(bind=engine)
        db = Session(engine)  # Get session
        populate_initial_data(db)  # Call population function
        db.close()
