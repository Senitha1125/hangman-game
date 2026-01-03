import random

def get_word():
    with open("static/words.txt", "r") as file:
        lines = file.readlines()

    chosen = random.choice(lines)
    word, clue = chosen.strip().split("|")

    return {
        "word": word.lower(),
        "clue": clue
    }
