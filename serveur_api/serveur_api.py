from flask import Flask, request

app = Flask(__name__)

@app.route("/allo", methods=["POST"])
def index():
    data = request.get_json()
    for player in data:
        print(f"player: {player['player']}, action: {player['action']}")

    return "200"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)