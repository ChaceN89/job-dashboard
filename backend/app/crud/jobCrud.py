# jobCrud.py
# Contains the CRUD operations related to jobs

# imports
from sqlalchemy.orm import Session
from app.models import jobModel as models
from app.schemas import jobSchemas as schemas

# Get all the jobs from the database
def get_jobs():
    return "get job"

# Get a specific job from the database
def get_job(job_id):
    return "all jobs"

# Add a new job to the database
def create_job():
    return "create job "

# Update a job in the database
def update_job(job_id):
    return "update job"

# Delete a job in the database
def delete_job(job_id):
    return "delete job "
