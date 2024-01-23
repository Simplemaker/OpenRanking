

const viewList = ['list', 'comparison']

function setView(view) {
    for (const v of viewList) {
        document.getElementById(`${v}View`).style.display = v == view ? "block" : "none"
    }
}
setView('list')

function submitList() {
    // You can access the textarea value and perform actions here
    const textareaValue = document.getElementById('myTextarea').value;
    const items = textareaValue.trim().split('\n')

    // Make a Fetch API POST request
    fetch('/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(items),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Server Response:', data);
            setView('comparison')
            fetchPair()
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle errors
        });
}

document.getElementById('submitButton').addEventListener('click', submitList)

function fetchPair() {
    // fetch pair and then display
    console.log('fetching pair...')
    fetch('/next').then(response => response.json())
        .then(data => {
            console.log(data)
            const [first, second] = data['pair']
            document.getElementById('item1').innerHTML = first
            document.getElementById('item2').innerHTML = second
        })
}

function fetchRankings() {
    console.log('fetching rankings...')
    fetch('/rankings').then(response => response.json())
        .then(data => {
            console.log(data)
            document.querySelector('pre').innerHTML = data.rankings.join('\n')
        })
}

function select(item) {
    const first = document.getElementById('item1').innerHTML
    const second = document.getElementById('item2').innerHTML

    const data = {
        "pair": [first, second],
        "firstBetter": item == 0
    }
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Server Response:', data);
            fetchPair()
            fetchRankings()
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle errors
        });
}

document.getElementById('select0').addEventListener('click', select.bind(null, 0))
document.getElementById('select1').addEventListener('click', select.bind(null, 1))
