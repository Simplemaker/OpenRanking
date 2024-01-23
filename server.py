from flask import Flask, request, jsonify
from ranking import Ranking

app = Flask(__name__)

# Data storage to simulate server state
server_data = {
    "ranking": None
}


@app.route('/start', methods=['POST'])
def start():
    # Simulate starting a new session or quiz
    data = request.json

    if data and isinstance(data, list):
        # Assuming the first item in the array is the initial question
        server_data['ranking'] = Ranking(data)
        response = {'status': 'Session started successfully'}
    else:
        response = {
            'status': 'Invalid request. Please provide a JSON array with items to compare.'}

    return jsonify(response)


@app.route('/next', methods=['GET'])
def next_question():
    pair = server_data['ranking'].getNextPair()
    print(pair)
    return jsonify({'pair': pair})


@app.route('/rankings', methods=['GET'])
def rankings():
    rankings = server_data['ranking'].getRankings()
    return jsonify({'rankings': rankings})


@app.route('/submit', methods=['POST'])
def submit_answer():
    data = request.json
    first, second = data.get('pair')
    firstBetter = data.get('firstBetter')
    if firstBetter is None:
        firstBetter = True
    server_data['ranking'].processPair(first, second, firstBetter)

    response = {'status': 'Pair added'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
