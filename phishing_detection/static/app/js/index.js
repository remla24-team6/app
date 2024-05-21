window.onload = function() {
    document.getElementById("checkButton").addEventListener('click', checkUrl);
    document.getElementById("correctButton").addEventListener('click', () => submitFeedback(true));
    document.getElementById("incorrectButton").addEventListener('click', () => submitFeedback(false));
    server_url = location.protocol + '//' + location.host + location.pathname;
    csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
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
        credentials: 'same-origin'
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then(responseJson => {
        const resultElem = document.getElementById("result");
        resultElem.style.display = 'inline';
        resultElem.innerHTML = responseJson.is_phishing ? "This is a phishing URL!" : "This is not a phishing URL!";
        document.getElementById("feedbackSection").style.display = 'block';
        document.getElementById("feedbackSection").dataset.url = url;
        document.getElementById("feedbackSection").dataset.isPhishing = responseJson.is_phishing;
    }).catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}

function submitFeedback(isCorrect) {
    const feedbackSection = document.getElementById("feedbackSection");
    const url = feedbackSection.dataset.url;
    const isPhishing = feedbackSection.dataset.isPhishing === 'true';
    const feedbackResult = Number(isCorrect);

    fetch(server_url + 'feedback/', {
        method: 'POST',
        body: JSON.stringify({url: url, label: isPhishing, feedback: feedbackResult}),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
            "X-CSRFToken": csrf_token
        },
        credentials: 'same-origin'
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then(responseJson => {
        alert(responseJson.message);
        document.getElementById("feedbackSection").style.display = 'none';
    }).catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}