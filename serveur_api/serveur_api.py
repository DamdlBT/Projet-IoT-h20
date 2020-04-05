from datetime import datetime

from flask import Flask, request
import dataset


app = Flask(__name__)
db = dataset.connect('sqlite:///db.sqlite')

actions = db['actions']

@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    for action in data:
        # print(f"player: {player['player']}, action: {player['action']}")
        action["time"] = datetime.now()
        actions.insert(action)
    return "200"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)