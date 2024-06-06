# jobModel.py
# The models for the database containing jobs 

from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

# The model used for each Job in the database table
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    customerName = Column(String, index=True)
    jobType = Column(String, index=True)
    status = Column(String, index=True)
    appointmentDate = Column(DateTime)
    technician = Column(String)