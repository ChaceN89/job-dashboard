<template>
  <div>
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
      

        <hr v-if="index !== jobs.length - 1" class="mx-3 border-t-2 border-gray-800">
      </li>
    </ul>
  </div>
</template>

<script>
import { store } from '../store/store.js';
import { computed } from 'vue';
import { formatDate } from '../utils/utils.js';

export default {
  name: 'JobList',
  setup() {
    // Get all the jobs (computed to recognize that it will change)
    const jobs = computed(() => store.state.jobs);

    // Get the selected job to highlight the active job
    const selectedJob = computed(() => store.getters.getSelectedJob.value);

    // Select job function for this component using the store function
    const selectJob = (id) => {
      store.actions.setSelectedId(id);
    };

    return {
      jobs,
      selectedJob,
      selectJob,
      formatDate
    };
  }
};
</script>

