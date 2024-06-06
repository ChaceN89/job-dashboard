import { createApp } from 'vue';
import App from './App.vue';
import setupFontAwesome from './plugins/font-awesome';
import './assets/tailwind.css';
import './assets/styles.css';
import './assets/componentStyles.css';

const app = createApp(App);
setupFontAwesome(app); //use font awesome
app.mount('#app');