<template>
  <div v-if="selectedJob">
    <div class="details-header">
      <h1>Job Details</h1>
      <div>
        <font-awesome-icon
          v-if="isEditing.value"
          class="button-hover"
          size="2x"
          :icon="['fas', 'cancel']"
          @click="cancelEdit"
        />
        <font-awesome-icon
          v-else
          class="button-hover"
          size="2x"
          :icon="['fas', 'edit']"
          @click="toggleEditMode"
        />
      </div>
    </div>

    <div class="job-detail">
      <span class="label">Customer Name:</span> <span class="value">{{ selectedJob.customerName }}</span>
      <input v-if="isEditing.value" class="value" v-model="editableJob.customerName" id="customerName" />
    </div>
    <div class="job-detail">
      <span class="label">Job Type:</span> <span class="value">{{ selectedJob.jobType }}</span>
      <input v-if="isEditing.value" class="value" v-model="editableJob.jobType" id="jobType" />
      
    </div>
    <div class="job-detail">
      <span class="label">Status:</span> <span class="value">{{ selectedJob.status }}</span>
      <input v-if="isEditing.value" class="value" v-model="editableJob.status" id="status" />
    </div>
    <div class="job-detail">
      <span class="label">Appointment Date:</span> <span class="value">{{ formatDate(selectedJob.appointmentDate) }}</span>
      <input v-if="isEditing.value" class="value" type="datetime-local" v-model="editableJob.appointmentDate" id="appointmentDate" />
    </div>
    <div class="job-detail">
      <span class="label">Technician:</span> <span class="value">{{ selectedJob.technician }}</span>
      <input v-if="isEditing.value" class="value" v-model="editableJob.technician" id="technician" />
    </div> 
    <div v-if="isEditing.value" class="details-header">
      <button @click="saveChanges">Save</button>
      <button @click="cancelEdit">Cancel</button>
      <button @click="confirmDelete" class="delete-button">Delete</button>

    </div>
  </div>
</template>

<script>
import { store } from '../../store/store.js';
import { computed, reactive } from 'vue';
import { formatDate } from '../../utils/utils.js';


export default {
  name: 'DisplayJob',

  setup() {
    const selectedJob = computed(() => store.getters.getSelectedJob.value);
    
    const isEditing = reactive({ value: false });
    const editableJob = reactive({ ...selectedJob.value });


    const toggleEditMode = () => {
      isEditing.value = !isEditing.value;
      Object.assign(editableJob, selectedJob.value); // Reset editable fields when toggling edit mode
    };

    const saveChanges = async () => {
      await store.actions.updateJob(editableJob.id, editableJob);
      isEditing.value = false;
    };

    const confirmDelete = () => {
      if (confirm("Are you sure you want to delete this job?")) {
        deleteJob();
      }
    };

    const deleteJob = async () => {
      await store.actions.deleteJob(editableJob.id);
      isEditing.value = false;
    };

    const cancelEdit = () => {
      isEditing.value = false;
      Object.assign(editableJob, selectedJob.value); // Reset fields on cancel
    };

  

    return {
      selectedJob,
      formatDate,
      isEditing,
      editableJob,
      toggleEditMode,
      saveChanges,
      cancelEdit,
      confirmDelete
    };
  }
};
</script>


