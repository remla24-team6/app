window.onload = function() {
    document.getElementById("checkButton").addEventListener('click', checkUrl)
    document.getElementById("addButton").addEventListener('click', addTrainingData);
    server_url = location.protocol + '//' + location.host + location.pathname
    csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
    console.log(server_url)
  };
  
  
  
function checkUrl(event) {
const url = document.getElementById("urlfield").value;
if (!url) {
    alert("Please enter a URL to check.");
    return;
}
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

function addTrainingData(event) {
    const newUrl = document.getElementById("newUrl").value;
    const label = document.getElementById("label").value;
    const addToTraining = document.getElementById("addToTraining").checked;
    if (!newUrl || !label) {
        alert("Please enter a URL and select a label.");
        return;
    }
    
    if (addToTraining) {
        fetch(server_url + 'add_training/', {
            method: 'POST',
            body: JSON.stringify({url: newUrl, label: label}),
            headers: {
                'Content-type': 'application/json; charset=UTF-8',
                "X-CSRFToken": csrf_token
            },
            credentials: 'same-origin'
        }).then(response => response.json()).then(responseJson => {
            alert(responseJson.message);
        });
    }
}