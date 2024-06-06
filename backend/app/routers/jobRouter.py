# jobRouter.py
# contains the routes pertaining to the job category 
# all depend on the database being connected else they will return an errorr

# imports 
from fastapi import APIRouter, Depends, HTTPException
from app.crud import jobCrud # crud operations 
from app.schemas.jobSchemas import JobGet, JobCreate, JobMessage, JobUpdate #schemas

# database session and get deb function
from sqlalchemy.orm import Session
from app.database import get_db

# Set up this router specifically for the job routes
router = APIRouter(
    prefix="/jobs",  
    tags=['jobs']  # Tag for SwaggerUI
)

# GET /jobs - Retrieves all jobs and returns a list of jobs
@router.get("/", response_model=list[JobGet])
async def get_all_jobs(db: Session = Depends(get_db)):
    return jobCrud.get_jobs(db)

# GET /jobs/{job_id} - Retrieves a specific job by ID
@router.get("/{job_id}", response_model=JobGet)
async def get_job(job_id: int, db: Session = Depends(get_db)):
    job = jobCrud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

# POST /jobs - Adds a new job record
@router.post("/", response_model=JobGet)
async def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return jobCrud.create_job(db, job)

# PUT /jobs/{job_id} - Updates an existing job record
@router.put("/{job_id}", response_model=JobMessage)
async def update_job(job_id: int, job: JobUpdate, db: Session = Depends(get_db)):
    db_job = jobCrud.update_job(db, job_id, job)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

# DELETE /jobs/{job_id} - Deletes a job record
@router.delete("/{job_id}", response_model=JobMessage)
async def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = jobCrud.delete_job(db, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job