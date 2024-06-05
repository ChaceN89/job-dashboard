# main.py
# Entry point into the application

# Imports 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data import client
from app.routers import jobRouter

# Create a FastAPI app
app = FastAPI()

# Set up middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[client],  # Replace with your frontend's URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Add the routers to the system
app.include_router(jobRouter.router, prefix="/api")  # Include jobRouter with /api prefix

# Start the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)