from flask import Flask, render_template, request, jsonify
from words import get_word

app = Flask(__name__)

game_state = {
    "word": "",
    "guessed": [],
    "lives": 6
}

@app.route("/")
def start():
    return render_template("start.html")
@app.route("/game")
def game():
    return render_template("game.html")
@app.route("/win")
def win():
    return render_template("win.html")
@app.route("/lose")
def lose():
    return render_template("lose.html")


@app.route("/start", methods=["POST"])
def start_game():
    data = get_word()
    game_state["word"] = data["word"]
    game_state["clue"] = data["clue"]
    game_state["guessed"] = []
    game_state["lives"] = 6

    display_word = ["_" for _ in game_state["word"]]

    return jsonify(
        display=" ".join(display_word),
        lives=6,
        clue=game_state["clue"]
    )



@app.route("/guess", methods=["POST"])
def guess():
    letter = request.json["letter"]

    if letter not in game_state["guessed"]:
        game_state["guessed"].append(letter)
        if letter not in game_state["word"]:
            game_state["lives"] -= 1

    display_word = [
        l if l in game_state["guessed"] else "_"
        for l in game_state["word"]
    ]

    return jsonify(
        display=" ".join(display_word),
        lives=game_state["lives"],
        won="_" not in display_word,
        lost=game_state["lives"] <= 0
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

