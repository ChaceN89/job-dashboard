<template>
  <div>
    <div v-if="isCreatingNewJob">
      <CreateJob />
    </div>
    <div v-else>
      <p>Selected Job ID: {{ store.state.selected_id }}</p>
      <hr>
      <p>Selected Job: {{ selectedJob ? selectedJob : 'None' }}</p>
    </div>
  </div>
</template>

<script>
import { store } from '../store/store.js';
import { computed } from 'vue';
import CreateJob from '../components/subComponents/CreateJob.vue';

export default {
  name: 'JobDetails',
  components: {
    CreateJob
  },
  setup() {
    const selectedJob = computed(() => store.getters.getSelectedJob.value);
    const isCreatingNewJob = computed(() => isNaN(store.state.selected_id));

    return {
      store,
      selectedJob,
      isCreatingNewJob
    };
  }
};
</script>
