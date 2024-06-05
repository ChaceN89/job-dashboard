# Job Management Dashboard

Job Management Dashboard helps users efficiently manage job data. It features a FastAPI backend with RESTful API endpoints and a Vue frontend styled with Tailwind CSS. The backend handles job data management, while the frontend provides an intuitive interface for interacting with the services.

## Environment Variable Setup

If you are running the application locally, you don't need to have an .env file for either the frontend or backend.

## Frontend

### Setting up Vue

Follow the instructions at [Vue CLI Installation Guide](https://cli.vuejs.org/guide/installation.html) to set up Vue.

### Running the Application Locally

1. **Navigate to the frontend folder:**
   ```
   cd frontend
   ```
   
2. **Install Dependencies:**
   ```
   npm install
   ```
   
3. **Start Development Server:**
   ```
   npm run serve
   ```
   

4. **Open your browser and navigate to [http://localhost:8080](http://localhost:8080)**

## Backend

1. **In a new terminal, navigate to the backend folder:**
   ```
   cd backend
   ```

2. **Create a virtual environment. You may create it using any method you prefer for example:**
   ```
   python -m venv env
   ```


3. **Activate the virtual environment:**

  On Windows:
  ```
  .\env\Scripts\activate
  ```
  On macOS/Linux:
  ```
  source env/bin/activate
  ```

4. **Install dependencies:**
```
pip install -r requirements.txt
```



5. **Start the server:**
```
uvicorn main:app --reload
```
The reload command is optional and used to reload the app on changes




## Access

- Once both the frontend and backend servers are running, you can access the Job Management Dashboard(GUI) by navigating to [http://localhost:8080](http://localhost:8080) in your web browser.
- After starting the backend server, you can access the Swagger UI documentation at [http://localhost:8000/docs](http://localhost:8000/docs).




## Considerations

The application used a SQL Lite

## Summary

The Job Management Dashboard provides a convenient solution for managing job data with its FastAPI backend and Vue frontend. Follow the instructions above to set up and run the application locally.




   
