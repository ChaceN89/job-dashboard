<!-- JobDetails.vue
  desides to show the create job form or the display job component depending on selected job or pressnew job button 
-->
<template>
  <div>
    <div v-if="isCreatingNewJob">
      <CreateJob />
    </div>
    <div v-else>
			<DisplayJob />
    </div>
  </div>
</template>

<script>
import { store } from '../store/store.js';
import { computed } from 'vue';
import CreateJob from '../components/subComponents/CreateJob.vue';
import DisplayJob from '../components/subComponents/DisplayJob.vue';

export default {
  name: 'JobDetails',
  components: {
    CreateJob,
		DisplayJob
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
