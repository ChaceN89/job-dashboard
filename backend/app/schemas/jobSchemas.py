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

# Used to create jobs - separate from JobBase but can be altered and is more clear which operation it is using
class JobCreate(JobBase):
    pass

# Used to update jobs
class JobUpdate(JobBase):
    pass

# Add an ID to JobBase for database
class JobGet(JobBase):
    id: int
    class Config: # For access to the database
        orm_mode = True

# Return model for a deleted job - with a job and a message as separate entities
class JobMessage(BaseModel):
    job:JobGet
    message: str
    class Config: # For access to the database
        orm_mode = True