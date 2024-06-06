import { reactive, computed } from 'vue';
import { fetchJobs, fetchJob, createJob, updateJob, deleteJob } from '../api/jobs';

const state = reactive({
  jobs: [],
  selected_id: null,
  sortBy: 'date', // Default sorting criteria
  sortOrder: 'asc' // Default sorting order (ascending)
});

const getters = {
  getSelectedJob: computed(() => {
    if (isNaN(state.selected_id)) {
      return "newJob";
    }   
    return state.jobs.find(job => job.id === state.selected_id);
  }),
  
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

  getSelectedId: computed(() => state.selected_id),
  getSortBy: computed(() => state.sortBy),
  getSortOrder: computed(() => state.sortOrder)
};

const actions = {
  setSelectedId(newId) {
    state.selected_id = newId;
  },
  setSortBy(sortBy) {
    state.sortBy = sortBy;
  },
  setSortOrder(sortOrder) {
    state.sortOrder = sortOrder;
  },
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

export const store = {
  state,
  getters,
  actions
};
