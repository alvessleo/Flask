// Exercicio1

fetch('http://127.0.0.1:5000/exercicio1', {
  method: 'POST', 
  headers: {
    'Content-Type': 'application/html',
  },
  body: JSON.stringify(data_inicio),
})
  .then((response) => response.json())
  .then((data_inicio) => {
    console.log('Success:', data_inicio);
  })
  .catch((error) => {
    console.error('Error:', error);
  });