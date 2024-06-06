import { reactive, computed } from 'vue';
import { fetchJobs } from '../api/jobs';

const state = reactive({
  jobs: [],
  selected_id: null,
  sortBy: 'date', // Default sorting criteria
  sortOrder: 'asc' // Default sorting order (ascending)
});

const getters = {
  getSelectedJob: computed(() => {
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
  })
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
  async initializeJobs() {
    const jobs = await fetchJobs();
    state.jobs = jobs;
    if (jobs.length > 0) {
      state.selected_id = jobs[0].id;
    }
  }
};

export const store = {
  state,
  getters,
  actions
};
