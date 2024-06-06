import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export async function fetchJobs() {
  try {
    console.log("fetch ")
    const response = await axios.get(API_URL+"jobs");
    return response.data;
  } catch (error) {
    console.error('Error fetching jobs:', error);
    return [];
  }
}
