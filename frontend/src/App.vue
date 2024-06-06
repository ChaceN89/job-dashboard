<template>
  <div class="app">
    <div class="header">Job Dashboard</div>
    <div class="app-body">
      <JobList class="box"/>
      <JobDetails class="box"/>
    </div>
    <AppSettings class="settings"/>
    <BreakPointVisualVue/>  <!-- Breakpoint is for testing -->

  </div>
</template>

<script>
import AppSettings from './components/AppSettings.vue'
import BreakPointVisualVue from './components/BreakPointVisual.vue'
import JobDetails from './components/JobDetails.vue'
import JobList from './components/JobList.vue'

export default {
  name: 'App',
  components: {
    AppSettings,
    JobDetails,
    JobList,
    BreakPointVisualVue
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

}
</style>
