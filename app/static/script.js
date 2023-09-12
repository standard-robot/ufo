// Populates the table upon loading
function populateList() {
  const ufosList = document.getElementById('ufos-list');
  fetch('/api/ufos')
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

// Function to fetch UFO sightings data by location
function getLocation() {
  const ufosList = document.getElementById('ufos-list');

  var user_input = document.getElementById('location-input').value;
  fetch(`/api/ufos/locations/${user_input}`)
    .then((response) => response.json())
    .then((data) => {
      // Handle the fetched data (e.g., display it on the page)
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

// Function to fetch UFO sightings data by location
function getDate() {
  const ufosList = document.getElementById('ufos-list');

  var user_input = document.getElementById('date-input').value;
  fetch(`/api/ufos/dates/${user_input}`)
    .then((response) => response.json())
    .then((data) => {
      // Handle the fetched data (e.g., display it on the page)
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

var input1 = document.getElementById("location-input");
var input2 = document.getElementById("date-input");
input1.addEventListener("focus", function() {
  if(input1.value != '') {
    input2.disabled = true; 

  }
});

// Add event listener for input2 focus
input2.addEventListener("focus", function() {
  if(input2.value != '') {
    input1.disabled = true;
  }
});

function clear() {
  document.getElementById('location-input').value = '';
  document.getElementById('date-input').nodeValue = '';
}