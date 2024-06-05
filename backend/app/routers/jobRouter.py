# jobRouter.py
# contains the routes pertaining to the job category 

# imports 
from fastapi import APIRouter
from app.schemas import jobSchemas as schemas
from app.crud import jobCrud

# Set up this router specifically for the job routes
router = APIRouter(
    prefix="/jobs",  
    tags=['jobs']  # Tag for SwaggerUI
)

# GET /jobs - Retrieves all jobs
@router.get("/")
async def get_all_jobs():
    return jobCrud.get_jobs()

# GET /jobs/{job_id} - Retrieves a specific job by ID
@router.get("/{job_id}")
async def get_job(job_id: int ):
    return jobCrud.get_job(job_id)

# POST /jobs - Adds a new job record
@router.post("/")
async def create_job():
    return jobCrud.create_job()

# PUT /jobs/{job_id} - Updates an existing job record
@router.put("/{job_id}")
async def update_job(job_id: int ):
    return jobCrud.update_job(job_id)

# DELETE /jobs/{job_id} - Deletes a job record
@router.delete("/{job_id}", response_model=schemas.Job)
async def delete_job(job_id: int, ):
    return jobCrud.delete_job(job_id)
