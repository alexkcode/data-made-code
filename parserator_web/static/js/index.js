/* TODO: Flesh this out to connect the form to the API and render results
in the #address-results div. */
document.addEventListener('DOMContentLoaded', (event) => {
   console.log('DOM fully loaded and parsed');

   document.getElementById('form').addEventListener('submit', function(event) {
      event.preventDefault();

      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

      // remove all current table elements
      document.querySelectorAll('.result-row').forEach(element => {
         element.remove()
      });

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
         console.log('Parse Result:', parsedAddr);
         if (parsedAddr.status === 'success') {
            console.log('Parse success!')
            document.getElementById('address-results').setAttribute('style', '');
            document.getElementById('parse-type').textContent = parsedAddr.address_type
            Object.entries(parsedAddr.address_components).map((c) => addRowToTable(c[1], c[0]))
         } else {
            alert('Parse Error: ' + parsedAddr.message);
         }
      })
      .catch((error) => {
         alert('Table Render Error:', error)
      });
   });

   function addRowToTable(comp, type) {
      const table = document.getElementById('address-results').getElementsByTagName('tbody')[0];
      const newRow = table.insertRow();
      newRow.setAttribute('class', 'result-row')

      const addrComp = newRow.insertCell(0);
      const addrType = newRow.insertCell(1);

      addrComp.textContent = comp;
      addrType.textContent = type;

      console.log('Added row: ', addrComp, addrType)
   }
});