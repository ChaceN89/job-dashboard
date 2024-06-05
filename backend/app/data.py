# data.py
# Load environment variables from .env file

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variables with fallback values for local development
client = os.getenv('CLIENT', 'http://localhost:8080')
api = os.getenv('API', 'http://localhost:8000')

# Initial job data for testing
initial_job_data = [
    {
        "id": 1,
        "customerName": "John Doe",
        "jobType": "Plumbing",
        "status": "Scheduled",
        "appointmentDate": "2024-06-15T09:00:00Z",
        "technician": "Jane Smith"
    },
    {
        "id": 2,
        "customerName": "Alice Johnson",
        "jobType": "Electrical",
        "status": "Completed",
        "appointmentDate": "2024-05-20T14:00:00Z",
        "technician": "Bob Brown"
    }
]
