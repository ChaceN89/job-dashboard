// utils.js
// function to formate the date 
// can add more functions here as needed

export function formatDate(dateString) {
  const options = {
    year: 'numeric', month: 'long', day: 'numeric',
    hour: '2-digit', minute: '2-digit', second: '2-digit',
    timeZoneName: 'short'
  };
  const date = new Date(dateString);
  return date.toLocaleString(undefined, options);
}