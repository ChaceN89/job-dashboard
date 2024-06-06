import { createApp } from 'vue';
import App from './App.vue';
import setupFontAwesome from './plugins/font-awesome';
// import store from './store'; // Import the Vuex store
import './assets/tailwind.css';
import './assets/styles.css';

const app = createApp(App);

setupFontAwesome(app);//use font awesome
// app.use(store); // Use the Vuex store

app.mount('#app');