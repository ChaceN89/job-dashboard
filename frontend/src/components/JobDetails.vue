<template>
  <div>
    Selected Job ID: {{ store.state.selected_id }}
    <hr>
    Selected Job: {{ selectedJob ? selectedJob : 'None' }}
  </div>
</template>

<script>
import { store } from '../store/store.js';
import { computed } from 'vue';

export default {
  name: 'JobDetails',
  setup() {
    const selectedJob = computed(() => store.getters.getSelectedJob.value );
    return {
      store,
      selectedJob
    };
  }
};
</script>
