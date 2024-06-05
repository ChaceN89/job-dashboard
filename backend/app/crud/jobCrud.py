# jobCrud.py
# Contains the CRUD operations related to jobs

# imports
from sqlalchemy.orm import Session
from app.models import jobModel as models
from app.schemas import jobSchemas as schemas

# Get all the jobs from the database
def get_jobs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Job).offset(skip).limit(limit).all()

# Get a specific job from the database
def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

# Add a new job to the database
def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

# Update a job in the database
def update_job(db: Session, job_id: int, job: schemas.JobCreate):
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if db_job:
        for key, value in job.dict().items():
            setattr(db_job, key, value)
        db.commit()
        db.refresh(db_job)
        return db_job
    return None

# Delete a job in the database
def delete_job(db: Session, job_id: int):
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if db_job:
        db.delete(db_job)
        db.commit()
        return db_job
    return None
