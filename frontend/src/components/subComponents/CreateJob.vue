<!-- CreateJob.vue
  component to use a form to create a new job
-->
<template>
  <div >
    <h1>Create New Job</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="customerName">Customer Name</label>
        <input type="text" v-model="job.customerName" id="customerName" required />
      </div>
      <div class="form-group">
        <label for="jobType">Job Type</label>
        <input type="text" v-model="job.jobType" id="jobType" required />
      </div>
      <div class="form-group">
        <label for="status">Status</label>
        <input type="text" v-model="job.status" id="status" required />
      </div>
      <div class="form-group">
        <label for="appointmentDate">Appointment Date</label>
        <input type="datetime-local" v-model="job.appointmentDate" id="appointmentDate" required />
      </div>
      <div class="form-group">
        <label for="technician">Technician</label>
        <input type="text" v-model="job.technician" id="technician" required />
      </div>
      <button type="submit">Create Job</button>
    </form>
  </div>
</template>

<script>
import { store } from '../../store/store.js';

export default {
  name: 'CreateJob',
  data() {
    return {
      job: {
        customerName: '',
        jobType: '',
        status: '',
        appointmentDate: '',
        technician: ''
      }
    };
  },
  methods: {
    // submit trhough the store to keep track of the state
    async submitForm() {
      const jobData = {
        ...this.job,
        appointmentDate: new Date(this.job.appointmentDate).toISOString()
      };
      await store.actions.createJob(jobData);
      // Optionally reset the form or navigate to a different page
      this.resetForm();
    },

    // reset upon completion
    resetForm() {
      this.job = {
        customerName: '',
        jobType: '',
        status: '',
        appointmentDate: '',
        technician: ''
      };
    }
  }
};
</script>

