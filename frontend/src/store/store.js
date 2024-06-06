// store.js
// contains the state and state management for the application 
import { reactive, computed } from 'vue';
import { fetchJobs, fetchJob, createJob, updateJob, deleteJob } from '../utils/jobsAPI';

// create a state with the job infoamtion 
// also decided to keep track or order in this component
const state = reactive({
  jobs: [],
  selected_id: null,
  sortBy: 'date', // Default sorting criteria
  sortOrder: 'asc' // Default sorting order (ascending)
});

// getters to fetch state infomation 
const getters = {
  // the current selected job - this is based on the selected id
  getSelectedJob: computed(() => {
    // if the currently selected job is a string then don't return a job as a new job is being created
    if (isNaN(state.selected_id)) {
      return "newJob";
    }   
    // go through the jobs to get the selected on
    return state.jobs.find(job => job.id === state.selected_id);
  }),
  
  // get the sorted jobs based on sorting by data or ID(most recent created) - also based or order (asc or desc)
  sortedJobs: computed(() => {
    const jobs = [...state.jobs];
    if (state.sortBy === 'date') {
      jobs.sort((a, b) => {
        const dateA = new Date(a.appointmentDate);
        const dateB = new Date(b.appointmentDate);
        return state.sortOrder === 'asc' ? dateA - dateB : dateB - dateA;
      });
    } else if (state.sortBy === 'id') {
      jobs.sort((a, b) => {
        return state.sortOrder === 'asc' ? a.id - b.id : b.id - a.id;
      });
    }
    return jobs;
  }),

  // to get the rest of the infoamiton
  getSelectedId: computed(() => state.selected_id),
  getSortBy: computed(() => state.sortBy),
  getSortOrder: computed(() => state.sortOrder)
};

// functions used to change the states
const actions = {
  // set the new selected ID
  setSelectedId(newId) {
    state.selected_id = newId;
  },
  // cahnge the sorting options
  setSortBy(sortBy) {
    state.sortBy = sortBy;
  },
  setSortOrder(sortOrder) {
    state.sortOrder = sortOrder;
  },

  // async to access data from the backend
  async getJobs() {
    const jobs = await fetchJobs();
    state.jobs = jobs;

  },
  async createJob(jobData) {
    const newJob = await createJob(jobData);
    if (newJob) {
      state.jobs.push(newJob);
      state.selected_id = newJob.id;
    }
  },
  async updateJob(jobId, jobData) {
    const updatedJob = await updateJob(jobId, jobData);
    if (updatedJob) {
      const index = state.jobs.findIndex(job => job.id === jobId);
      if (index !== -1) {
        state.jobs[index] = updatedJob.job;
      }
    }
  },
  async deleteJob(jobId) {
    const deletedJob = await deleteJob(jobId);
    if (deletedJob) {
      state.jobs = state.jobs.filter(job => job.id !== jobId);
      state.selected_id = null;
    }
  },
  async fetchJob(jobId) {
    return await fetchJob(jobId);
  }
};

// export the state, getters and actions 
export const store = {
  state,
  getters,
  actions
};
