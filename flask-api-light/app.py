import os, json
from flask import Flask, request, jsonify

fake_db = [
    {
        "id": 1,
        "name": "Sonny"
    },
    {
        "id": 2,
        "name": "Kane"
    }
]

app = Flask(__name__)

# GET, POST
@app.route("/api/player", methods=['GET', 'POST'])
def create_or_get_player():
    if request.method == 'GET':
        return jsonify(fake_db), 200
    elif request.method == 'POST':
        try:
            # Get Data
            data = request.get_data()
            data = json.loads(data)
            fake_db.append(data)
            return "Complete", 201
        except Exception as e:
            print(e)
            return "bad request", 400
    else:
        return "bad request", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)