<template>
  <div>
    <div class="sort-controls">
      <button @click="setSort('date')">Sort by Date</button>
      <button @click="setSort('id')">Sort by ID</button>
      <button @click="toggleSortOrder">Toggle Sort Order</button>
    </div>
    <hr class="line py-2">

    <ul>
      <!-- list all the jobs and highlight the active one -->
      <li v-for="(job, index) in jobs" 
        :key="job.id" 
        @click="selectJob(job.id)"
        class="job"
        :class="{'bg-yellow-200 rounded-lg': job.id === selectedJob?.id}" 
      >

      <!-- add better display component here -->
      {{ job.customerName }} - {{ job.jobType }} ({{ job.status }}) 
      | {{ formatDate(job.appointmentDate) }}  | {{ job.technician }}
      

        <hr v-if="index !== jobs.length - 1" class="line">
      </li>
    </ul>

    <div class="add-job" @click="addJob">+</div>

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
    const setSort = (sortBy) => {
      store.actions.setSortBy(sortBy);
    };

    // toggle the order or sorting
    const toggleSortOrder = () => {
      store.actions.setSortOrder(store.state.sortOrder === 'asc' ? 'desc' : 'asc');
    };

    
    const addJob = () => {
      store.actions.setSelectedId('newJob');
    };

    // Fetch the jobs list  when the component is mounted
    onMounted(() => {
      store.actions.initializeJobs();
    });

    return {
      jobs,
      selectedJob,
      selectJob,
      setSort,
      toggleSortOrder,
      addJob,
      formatDate
    };
  }
};
</script>

