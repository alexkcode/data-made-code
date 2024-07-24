/* TODO: Flesh this out to connect the form to the API and render results
in the #address-results div. */
document.addEventListener('DOMContentLoaded', (event) => {
   console.log('DOM fully loaded and parsed');

   document.getElementById('form').addEventListener('submit', function(event) {
   event.preventDefault();

   const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

   let formData = new FormData(this);
   let queryString = new URLSearchParams(formData).toString();

   console.log('Form submitted!')
   console.log(formData)

   fetch(`http://localhost:8000/api/parse/?${queryString}`, {
         method: 'GET',
         headers: {
         'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
         }
   })
   .then(response => {
         console.log('Response received:', response);
         return response.json();
   })
   .then(parsedAddr => {
      console.log('Success:', parsedAddr);
      if (parsedAddr.status === 'success') {
         addRowToTable(parsedAddr);
      } else {
         alert('Error: ' + parsedAddr.message);
      }
   })
   .catch((error) => {
      console.error('Error:', error)
   });
   });

   function addRowToTable(parsedAddr) {
      const table = document.getElementById('address-results').getElementsByTagName('tbody')[0];
      const newRow = table.insertRow();

      const addrComp = newRow.insertCell(0);
      const addrType = newRow.insertCell(1);

      addrComp.textContent = parsedAddr.address_components;
      addrType.textContent = parsedAddr.address_type;
   }
});