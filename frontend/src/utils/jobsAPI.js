// jobsAPI.js
// functions to fetch data from the jobsAPI and return the results 
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/jobs';

// get all the jobs 
export async function fetchJobs() {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching jobs:', error);
    return [];
  }
}

// get a single job using the job ID
export async function fetchJob(jobId) {
  try {
    const response = await axios.get(`${API_URL}/${jobId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching job:', error);
    return null;
  }
}

// create a single job
export async function createJob(jobData) {
  try {
    const response = await axios.post(API_URL, jobData);
    return response.data;
  } catch (error) {
    console.error('Error creating job:', error);
    return null;
  }
}

// update a job using its id
export async function updateJob(jobId, jobData) {
  try {
    const response = await axios.put(`${API_URL}/${jobId}`, jobData);
    return response.data;
  } catch (error) {
    console.error('Error updating job:', error);
    return null;
  }
}

// delete a job using its id
export async function deleteJob(jobId) {
  try {
    const response = await axios.delete(`${API_URL}/${jobId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting job:', error);
    return null;
  }
}
