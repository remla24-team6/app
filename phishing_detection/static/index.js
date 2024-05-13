window.onload = function() {
  document.getElementById("checkButton").addEventListener('click', checkUrl)

    server_url = location.protocol + '//' + location.host + location.pathname
    csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
    console.log(server_url)
};



function checkUrl(event) {
  const url = document.getElementById("urlfield").value;

  fetch(server_url + 'check/', {
      method: 'POST',
      body: JSON.stringify({test_url: url}),
      headers: {
          'Content-type': 'application/json; charset=UTF-8',
          "X-CSRFToken": csrf_token
      },
      credentials : 'same-origin'
  }).then(
      function(response) {
          response.json().then(responseJson => {
            const resultElem = document.getElementById("result");

            resultElem.style.display = 'inline'
            resultElem.innerHTML = event.target.value.slice(12)
            if (responseJson.is_phishing){
                resultElem.innerHTML = "This is a phishing URL!"
            } else {
                resultElem.innerHTML = "This is not a phishing URL!"
            }
          })
      })
}