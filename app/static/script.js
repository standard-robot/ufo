// Populates the table on the frontend
function populateList() {
  const ufosList = document.getElementById('ufos-list');
  fetch('/api/ufos')
    .then((response) => response.json())
    .then((data) => {
      const formattedData = data.map((ufo) => {
        return `
          <tr class="tg">
            <td>${ufo.date_occurred}</td>
            <td>${ufo.date_posted}</td>
            <td>${ufo.city}</td>
            <td>${ufo.state}</td>
            <td>${ufo.country}</td>
            <td>${ufo.shape}</td>
            <td>${ufo.summary}</td>
          </tr>
        `;
      });
      const htmlContent = formattedData.join('');
      ufosList.innerHTML = htmlContent;
    })
    .catch((error) => console.error('Error fetching data:', error));
}

// Function to fetch UFO sightings data by a given location (this endpoint checks whether the city, state, or country include the entry).
function getLocation() {
  const ufosList = document.getElementById('ufos-list');

  var user_input = document.getElementById('location-input').value;
  fetch(`/api/ufos/locations/${user_input}`)
    .then((response) => response.json())
    .then((data) => {
      // Handle the fetched data (e.g., display it on the page)
      const formattedData = data.map((ufo) => {
        return `
          <tr id="data-tr">
            <td>${ufo.date_occurred}</td>
            <td>${ufo.date_posted}</td>
            <td>${ufo.city}</td>
            <td>${ufo.state}</td>
            <td>${ufo.country}</td>
            <td>${ufo.shape}</td>
            <td>${ufo.summary}</td>
          </tr>
        `;
      });
      const htmlContent = formattedData.join('');
      ufosList.innerHTML = htmlContent;
    })
    .catch((error) => console.error('Error fetching data:', error));
}

// Function to fetch UFO sightings data by a given date
function getDate() {
  const ufosList = document.getElementById('ufos-list');
  var user_input = document.getElementById('date-input').value;
  fetch(`/api/ufos/dates/${user_input}`)
    .then((response) => response.json())
    .then((data) => {
      const formattedData = data.map((ufo) => {
        return `
          <tr>
            <td>${ufo.date_occurred}</td>
            <td>${ufo.date_posted}</td>
            <td>${ufo.city}</td>
            <td>${ufo.state}</td>
            <td>${ufo.country}</td>
            <td>${ufo.shape}</td>
            <td>${ufo.summary}</td>
          </tr>
        `;
      });
      const htmlContent = formattedData.join('');
      ufosList.innerHTML = htmlContent;
    })
    .catch((error) => console.error('Error fetching data:', error));
}

// Clears the focused input
function clear() {
  populateList()
  console.log("test")
  document.getElementById('location-input').value = '';
  document.getElementById('date-input').nodeValue = '';
}