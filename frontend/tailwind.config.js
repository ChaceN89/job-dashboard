/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // or 'media' or 'class'
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      screens: {
        'xxs': '400px', // Define your custom breakpoint (e.g., 400px)
      },
    },
  },
  plugins: [],
}

