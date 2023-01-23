// Exercicio1

let url = 'http://127.0.0.1:5000/date_service'
const data = {"start_date":"2021-03-03", "end_date":"2023-03-03"}

fetch(url, {
  method: "POST",
  headers: {
    'Content-Type':'application/json'
  },
  body:JSON.stringify(data)
})
.then(response => response.json())
.then(json => {
  console.log(json)

})
.catch(error => console.error(error))

