# jobSchemas.py
# Contains the schemas used for accepting and returning job data

# imports
from pydantic import BaseModel
from datetime import datetime

# Simple job class to be used by other schemas/classes
class JobBase(BaseModel):
    customerName: str
    jobType: str
    status: str
    appointmentDate: datetime
    technician: str

# Used to create jobs
class JobCreate(JobBase):
    pass

# Add an ID to JobBase
class Job(JobBase):
    id: int

    # For access to the database
    class Config:
        orm_mode = True
