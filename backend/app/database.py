# database.py
# Set up the database connection and ORM base class

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.data import initial_job_data
from datetime import datetime
import os

# Database setup URL
DATABASE_URL = "sqlite:///./jobs.db"

# Create the engine, session, and base
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Allows usage across multiple threads
)
SessionLocal = sessionmaker(
    autocommit=False,  # Disable autocommit to ensure explicit control over transactions
    autoflush=False,   # Disable autoflush to prevent premature flushes of pending changes
    bind=engine        # Bind the session to the engine, so it uses the SQLite database specified
)
Base = declarative_base() # Base class for our ORM models

# Function to get the database session - used as dependency for the routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to populate initial job data
def populate_initial_data(db: Session):
    from app.models.jobModel import Job # prevetn circular import by importing this after

    # for all the initial data add it to the database
    for job_data in initial_job_data:
        # Convert appointmentDate from string to datetime from initial data (to use the original formated data)
        job_data['appointmentDate'] = datetime.fromisoformat(job_data['appointmentDate'].replace('Z', '+00:00'))
        job = Job(**job_data)
        db.add(job)
    # commit changes 
    db.commit()

# Function to initialize the database
def initialize_database():
    db_file_path = "./jobs.db"  # Database path
    db_exists = os.path.exists(db_file_path)  # Check to see if the path exists (i.e., the database exists)

    # If the database doesn't exist, then create it
    if not db_exists:
        Base.metadata.create_all(bind=engine)
        db = Session(engine)  # Get session
        populate_initial_data(db)  # Call population function
        db.close() # close the database 
