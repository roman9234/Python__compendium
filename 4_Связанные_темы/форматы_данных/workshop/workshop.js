
// Запрос с параметрами в JSON

fetch('http://127.0.0.1:5000/api/v1/json/order', {
    method: 'POST',
    headers: {
        "Content-Type": 'application/json'
    },
    body: `{
        "client": "Jon Smith",
        "products": [
            {"name": "product A", "price": 20},
            {"name": "product B", "price": 40},
            {"name": "product B", "price": 40}
        ],
        "voucher": {"discount": "20%"}
        }`
})
    .then((r) => r.text())
    .then((body) => console.log(body))

// Ответ:

{"client": "Jon Smith", "total": 80.0, "products": ["product B", "product A"]}

// Запрос с параметрами в XML

fetch('http://127.0.0.1:5000/api/v1/xml/order', {
    method: 'POST',
    headers: {
        "Content-Type": 'application/xml'
    },
    body: `<order client = "Jon Smith">
        <product name ="product A" price = "20"></product>
        <product name ="product B" price = "40"></product>
        <product name ="product B" price = "40"></product>
        <discount>20%</discount>
        </order>`
})
    .then((r) => r.text())
    .then((body) => console.log(body))

// Ответ:

<order total="80" products="product B,product A" client="Jon Smith" />












