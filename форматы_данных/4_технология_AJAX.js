
//AJAX - "Аякс"
//Asynchronous Javascript and XML

//Позволяет асинхронно пысылать докуметы

//Пример кода на JavaScript

var xhr = new XMLHttpRequest();
xhr.open("GET", "/bar/foo.txt", true);
xhr.onload = function(e) {
  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      console.log(xhr.responseText);
    } else {
      console.error(xhr.statusText);
    }
  }
};
xhr.onerror = function(e) {
  console.error(xhr.statusText);
};
xhr.send(null);

// Теперь есть fetch-API
//Ей ме передаём url запрос и метаданные


fetch(url, {
  method: "POST",
  mode: "cors",
  headers: {
    "Content-Type": "application/json",
  },
  body: {"keyA": 1,
    "keyB": 2
  }’
}).then((response) = >response.json()).then((body) = >console.log(body)).
catch((e) = >console.error(e));

// Аборт контроллер. Позволяет оборвать соединение и разблокировать клиент для пользователя

const controller = new AbortController();
const signal = controller.signal;
fetch(url, {
  signal
}) controller.abort();






































































































































