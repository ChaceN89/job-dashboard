<template>
  <div v-if="selectedJob">
    <div class="details-header">
      <h1>Job Details </h1>
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
import Swal from 'sweetalert2';

export default {
  name: 'DisplayJob',

  setup() {
    // get the select jobfrom the store - refresh it as it changes
    const selectedJob = computed(() => store.getters.getSelectedJob.value);
    
    // create two variables for bool is editing and the editted value of the object
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
      Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#39C55E',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.isConfirmed) {
          deleteJob();
          Swal.fire(
            'Deleted!',
            'The job has been deleted.',
            'success'
          )
        }
      })
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


