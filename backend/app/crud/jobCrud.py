# jobCrud.py
# Contains the CRUD operations related to jobs

# imports
from sqlalchemy.orm import Session
from app.models.jobModel import Job
from app.schemas.jobSchemas import JobCreate, JobUpdate 

# Get all the jobs from the database
def get_jobs(db: Session):
    return db.query(Job).all()

# Get a specific job from the database
def get_job(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()

# Add a new job to the database
def create_job(db: Session, job: JobCreate):
    db_job = Job(**job.dict())  # Convert JobCreate Pydantic model to Job SQLAlchemy model instance
    db.add(db_job)
    db.commit()
    db.refresh(db_job) # refresh for changes 
    return db_job

# Update a job in the database
def update_job(db: Session, job_id: int, job: JobUpdate):
    # get the job in question and make changes if it exists 
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if db_job:
        # loop through changes to job and set the attributes
        for key, value in job.dict().items():
            setattr(db_job, key, value)
        db.commit()
        db.refresh(db_job)
        return {
            "job":db_job,
            "message":"Job updated successfully"
        }
    
    return None

# Delete a job in the database
def delete_job(db: Session, job_id: int):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if db_job:
        db.delete(db_job)
        db.commit()
        # add a return message
        return {
            "job":db_job,
            "message":"Job deleted successfully"
        }
    return None