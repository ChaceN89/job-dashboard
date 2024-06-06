<!-- AppSetting.vue
  settings - only for dark mode toggle 
-->
<template>
  <div>
    <font-awesome-icon class="button-hover" :icon="['fas', 'gear']" size="2x" @click="togglePopup" />
    <transition name="dropdown">
      <div v-if="showPopup" class="popup">
        <p class="underline text-lg">Settings</p>
        <div class="setting-item">
          <span>Dark Mode</span>
          <label class="toggle-switch">
            <input type="checkbox" v-model="darkMode" @change="toggleDarkMode" />
            <span class="slider"></span>
          </label>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'AppSettings',

  data() {
    return {
      showPopup: false,
      darkMode: false,
    };
  },

  mounted() {
    // Initialize theme based on darkMode value
    if (this.darkMode) {
      this.applyDark();
    } else {
      this.applyLight();
    }
  },
  methods: {
    togglePopup() {
      this.showPopup = !this.showPopup;
    },
    applyLight(){
      document.documentElement.classList.remove('dark');
      document.documentElement.classList.add('light');
    },
    applyDark(){
      document.documentElement.classList.remove('light');
      document.documentElement.classList.add('dark');
    },
    toggleDarkMode() {
      if (this.darkMode) {
        this.applyDark();
      } else {
        this.applyLight();
      }
      console.log('Dark mode toggled:', this.darkMode);
    },
  }
}
</script>

<style scoped>
.popup {
  position: absolute;
  top: 100%;
  left: -200px; /* Adjust this value as needed */
  border: 1px solid #ccc;
  padding: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  z-index: 1000;
  width: 200px; /* Set the desired width */
  @apply shadow-2xl bg-white dark:bg-zinc-400 rounded-lg;
}

.setting-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 20px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 16px;
  width: 16px;
  left: 2px;
  bottom: 2px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:checked + .slider:before {
  transform: translateX(20px);
}

input[type=range] {
  -webkit-appearance: none;
  width: 100%;
  height: 6px;
  background: #ddd;
  outline: none;
  opacity: 0.7;
  -webkit-transition: .2s;
  transition: opacity .2s;
}

input[type=range]:hover {
  opacity: 1;
}

input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  background: #2196F3;
  cursor: pointer;
  border-radius: 50%;
}

input[type=range]::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: #2196F3;
  cursor: pointer;
  border-radius: 50%;
}

.dropdown-enter-active, .dropdown-leave-active {
  transition: opacity 0.3s;
}

.dropdown-enter, .dropdown-leave-to {
  opacity: 0;
}
</style>
