fetch('https://raw.githubusercontent.com/Mayumi767/junk/main/data.json')
  .then(response => response.json())
  .then(data => {
    console.log(data); // JSON data
    // Do something with the JSON data here
  })
  .catch(error => {
    console.log('Error:', error);
  });
