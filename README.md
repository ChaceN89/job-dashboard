# Job Management Dashboard

Job Management Dashboard helps users efficiently manage job data. It features a FastAPI backend with RESTful API endpoints and a Vue frontend styled with Tailwind CSS. The backend handles job data management, while the frontend provides an intuitive interface for interacting with the services.

## Environment Variable Setup

If you are running the application locally, you don't need to have an .env file for either the frontend or backend as it is optional. 

If you decide to use a .env file the frontend requires:
- REACT_APP_API_URL=http://localhost:8000/api/jobs;

The backend requires:
- CLIENT=http://localhost:8080
- api=http://localhost:8000

If you deploy this application the URLs will need to be changed.

## Other Setup Considerations
A SQLite database is used and will be created when the backend Rest API is started 

## Backend (Rest API)

1. **In a new terminal, navigate to the backend folder:**
   ```
   cd backend
   ```

2. **Create a virtual environment. You may create it using any perfered method, for example:**
   ```
   python3 -m venv myenv
   ```


3. **Activate the virtual environment:**

  On Windows:
  ```
  .\myenv\Scripts\activate
  ```
  On macOS/Linux:
  ```
  source myenv/bin/activate
  ```

4. **Install dependencies from the requirements file:**
```
pip install -r requirements.txt
```


5. **Start the server:**
```
uvicorn main:app --reload
```
The reload flag is optional and used to reload the app on when changes occur.


## Frontend

### Setting up Vue

Follow the instructions at [Vue CLI Installation Guide](https://cli.vuejs.org/guide/installation.html) to set up Vue on your local machine.

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



## Access

- Once both the frontend and backend servers are running, you can access the Job Management Dashboard(GUI) by navigating to [http://localhost:8080](http://localhost:8080) in your web browser.
- After starting the backend server, you can access the Swagger UI documentation at [http://localhost:8000/docs](http://localhost:8000/docs).



## Considerations

The application is comprised of the following components:
- **Vue** for the Web Application
- **FastAPI** for the RestAPI
- **SQLite** for the database
- **Tailwind and CSS** for the frontend style


### Why These Technologies Were Chosen

**Vue:** I have some experience with Vue and wanted to explore using it for making API requests as I have done often in React. Vue's reactive nature and state management make it a great choice for building dynamic web applications that respond to data changes.

**FastAPI:** I am familiar with FastAPI and have enjoyed using its documentation tools, particularly Swagger. FastAPI's ability to automatically generate interactive API documentation with Swagger UI and ReDoc is a significant advantage for showcasing the application's endpoints.

**SQLite:** While a simpler backend could have been implemented using in-memory data structures, I chose to include a simple database to gain experience with SQLite. SQLite's lightweight nature and ease of use make it an excellent choice for managing simple data.

**Tailwind:** I have used Tailwind to style many applications. I find it very simple to use  while building an application. I also like that it can work with standard CSS classes to allow flexibility.

### Application Features

The application includes the following features:
- Add Job Form: A form to submit a new job.
- Update/Delete Jobs: Options to update or delete jobs directly from the interface.
- Responsive Design: The application is responsive and can be accessed on smaller screens.

These features ensure the application is user-friendly and functional across different devices. By combining these technologies, the application benefits from a modern, reactive front-end with Vue, a fast and reliable API with FastAPI, and a lightweight, easy-to-manage database with SQLite.

## API Documentation

FastAPI provides interactive API documentation using Swagger UI and ReDoc. You can access the documentation at the following URLs (assuming you are running the backend):
- [Swagger UI](http://localhost:8000/docs)
- [ReDoc](http://localhost:8000/redoc)

These interfaces display the application's routes and allow users to interact with them directly.

For quick reference, the API routes are listed below and the documentation in openapi.json is further down:

### API Endpoints

- **GET /api/jobs**: Retrieves all jobs.
- **GET /api/jobs/{job_id}**: Retrieves a specific job by ID.
- **POST /api/jobs**: Adds a new job record.
- **PUT /api/jobs/{job_id}**: Updates an existing job record.
- **DELETE /api/jobs/{job_id}**: Deletes a job record.

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/api/jobs/": {
      "get": {
        "tags": [
          "jobs"
        ],
        "summary": "Get All Jobs",
        "operationId": "get_all_jobs_api_jobs__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/JobGet"
                  },
                  "type": "array",
                  "title": "Response Get All Jobs Api Jobs  Get"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "jobs"
        ],
        "summary": "Create Job",
        "operationId": "create_job_api_jobs__post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/JobCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JobGet"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/jobs/{job_id}": {
      "get": {
        "tags": [
          "jobs"
        ],
        "summary": "Get Job",
        "operationId": "get_job_api_jobs__job_id__get",
        "parameters": [
          {
            "name": "job_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Job Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JobGet"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "jobs"
        ],
        "summary": "Update Job",
        "operationId": "update_job_api_jobs__job_id__put",
        "parameters": [
          {
            "name": "job_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Job Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/JobUpdate"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JobMessage"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "jobs"
        ],
        "summary": "Delete Job",
        "operationId": "delete_job_api_jobs__job_id__delete",
        "parameters": [
          {
            "name": "job_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Job Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JobMessage"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "JobCreate": {
        "properties": {
          "customerName": {
            "type": "string",
            "title": "Customername"
          },
          "jobType": {
            "type": "string",
            "title": "Jobtype"
          },
          "status": {
            "type": "string",
            "title": "Status"
          },
          "appointmentDate": {
            "type": "string",
            "format": "date-time",
            "title": "Appointmentdate"
          },
          "technician": {
            "type": "string",
            "title": "Technician"
          }
        },
        "type": "object",
        "required": [
          "customerName",
          "jobType",
          "status",
          "appointmentDate",
          "technician"
        ],
        "title": "JobCreate"
      },
      "JobGet": {
        "properties": {
          "customerName": {
            "type": "string",
            "title": "Customername"
          },
          "jobType": {
            "type": "string",
            "title": "Jobtype"
          },
          "status": {
            "type": "string",
            "title": "Status"
          },
          "appointmentDate": {
            "type": "string",
            "format": "date-time",
            "title": "Appointmentdate"
          },
          "technician": {
            "type": "string",
            "title": "Technician"
          },
          "id": {
            "type": "integer",
            "title": "Id"
          }
        },
        "type": "object",
        "required": [
          "customerName",
          "jobType",
          "status",
          "appointmentDate",
          "technician",
          "id"
        ],
        "title": "JobGet"
      },
      "JobMessage": {
        "properties": {
          "job": {
            "$ref": "#/components/schemas/JobGet"
          },
          "message": {
            "type": "string",
            "title": "Message"
          }
        },
        "type": "object",
        "required": [
          "job",
          "message"
        ],
        "title": "JobMessage"
      },
      "JobUpdate": {
        "properties": {
          "customerName": {
            "type": "string",
            "title": "Customername"
          },
          "jobType": {
            "type": "string",
            "title": "Jobtype"
          },
          "status": {
            "type": "string",
            "title": "Status"
          },
          "appointmentDate": {
            "type": "string",
            "format": "date-time",
            "title": "Appointmentdate"
          },
          "technician": {
            "type": "string",
            "title": "Technician"
          }
        },
        "type": "object",
        "required": [
          "customerName",
          "jobType",
          "status",
          "appointmentDate",
          "technician"
        ],
        "title": "JobUpdate"
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
      }
    }
  }
}
```
   
