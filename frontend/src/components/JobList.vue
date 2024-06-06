<!-- jobList.vue
  lists all the jobs and alows button to sort them 
  each job can be selected which affects the state
-->
<template>
  <div>
    <div class="sort-controls">
      <button @click="setSort('id')">
        Sort by Created
        <font-awesome-icon v-if="sortBy === 'id' && sortOrder ==='desc'"  :icon="['fas', 'sort-down']"   />
        <font-awesome-icon v-if="sortBy === 'id' && sortOrder ==='asc'"  :icon="['fas', 'sort-up']" />
      </button>

      <button @click="setSort('date')">
        <font-awesome-icon v-if="sortBy === 'date' && sortOrder ==='desc'"  :icon="['fas', 'sort-down']"   />
        <font-awesome-icon v-if="sortBy === 'date' && sortOrder ==='asc'"  :icon="['fas', 'sort-up']"   />
        Sort by Date
      </button>
      <button @click="addJob">
        <font-awesome-icon  :icon="['fas', 'plus']"   />
      </button>
    </div>
    <hr class="line">

    <ul>
      <!-- list all the jobs and highlight the active one -->
      <li v-for="(job, index) in jobs" 
        :key="job.id" 
        @click="selectJob(job.id)"
        class="job"
        :class="{'bg-yellow-200 dark:bg-slate-600 rounded-lg': job.id === selectedJob?.id}" 
      >
        <div>{{ job.customerName }} - {{ job.jobType }} ({{ job.status }}) </div>
        <div>{{ formatDate(job.appointmentDate) }} </div>
        <div> Technician: {{ job.technician }}</div>

        <hr v-if="index !== jobs.length - 1" class="line">
      </li>
    </ul>

  </div>
</template>

<script>
import { store } from '../store/store.js';
import { computed, onMounted } from 'vue';
import { formatDate } from '../utils/utils.js';

export default {
  name: 'JobList',
  setup() {
    // Get the sorted jobs (computed to recognize that it will change)
    const jobs = computed(() => store.getters.sortedJobs.value);

    // Get the selected job to highlight the active job
    const selectedJob = computed(() => store.getters.getSelectedJob.value);

    // Select job function for this component using the store function
    const selectJob = (id) => {
      store.actions.setSelectedId(id);
    };
    // set the Sort by attribute in the store
    const setSort = (newSortBy) => {
      const currentSortBy = sortBy.value;
      if (currentSortBy === newSortBy) {
        toggleSortOrder();
      } else {
        store.actions.setSortBy(newSortBy);
      }
    };

    // toggle the order or sorting
    const toggleSortOrder = () => {
      store.actions.setSortOrder(store.state.sortOrder === 'asc' ? 'desc' : 'asc');
    };

    // get the sorting options
    const sortBy = computed(() => store.getters.getSortBy.value);
    const sortOrder = computed(() => store.getters.getSortOrder.value);
    
    // function to add a job
    const addJob = () => {
      store.actions.setSelectedId('newJob');
    };

    // Fetch the jobs list  when the component is mounted
    onMounted(() => {
      store.actions.getJobs();
    });

    return {
      jobs,
      selectedJob,
      selectJob,
      setSort,
      toggleSortOrder,
      addJob,
      sortBy,
      sortOrder,
      formatDate
    };
  }
};
</script>

