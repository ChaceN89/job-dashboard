// store.js
import { reactive, computed } from 'vue';

const state = reactive({
  jobs: [
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
      "appointmentDate": "2024-05-21T14:00:00Z",
      "technician": "Bob Brown"
    },
    {
      "id": 3,
      "customerName": "Dan Smith Johnson",
      "jobType": "Electrical",
      "status": "Completed",
      "appointmentDate": "2024-05-20T12:00:00Z",
      "technician": "bobby jones "
    },
    {
      "id": 4,
      "customerName": "Mr Knowbody ",
      "jobType": "Electrical",
      "status": "Completed",
      "appointmentDate": "2024-05-20T14:00:00Z",
      "technician": "Dana adklashjdkasjkld aldj jaskl jdkld sajdklajsdjksajd jlaj  adjslkjdjslj  adlkjasdkljdasjkl kladjkl ajkdkajd jasj akdj klajkdl jklakjalkdsjkljkjsajd kljaskj klasjk jsakdj ksaj kljaklsdj klsjdkl jakldsj"
    },

  ],
  selected_id: 1,
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
  }
};

export const store = {
  state,
  getters,
  actions
};
