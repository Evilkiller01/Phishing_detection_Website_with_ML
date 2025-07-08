function checkURL() {
    const url = document.getElementById('url').value;
    fetch('/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('result').innerText = 'Result: ' + data.result;
    })
    .catch(err => {
        document.getElementById('result').innerText = 'Error occurred';
    });
}