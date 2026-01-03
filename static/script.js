const keyboard = document.getElementById("keyboard");
const wordDiv = document.getElementById("word");
const livesDiv = document.getElementById("lives");
const clueDiv = document.getElementById("clue");
const parts = document.querySelectorAll(".part");


function createKeyboard() {
    keyboard.innerHTML = "";
    for (let i = 65; i <= 90; i++) {
        const btn = document.createElement("button");
        btn.textContent = String.fromCharCode(i);
        btn.onclick = () => makeGuess(btn.textContent.toLowerCase(), btn);
        keyboard.appendChild(btn);
    }
}

function startGame() {
    fetch("/start", { method: "POST" })
        .then(res => res.json())
        .then(data => {
            wordDiv.textContent = data.display;
            livesDiv.textContent = "❤️ " + data.lives;
            clueDiv.textContent = "💡 Clue: " + data.clue;
            parts.forEach(part => {
    part.style.display = "none";
});

            createKeyboard();
        });
}


function makeGuess(letter, button) {
    button.disabled = true;

    fetch("/guess", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ letter })
    })
    .then(res => res.json())
    .then(data => {
    wordDiv.textContent = data.display;
    livesDiv.textContent = "❤️ " + data.lives;

    const wrongGuesses = 6 - data.lives;

    parts.forEach((part, index) => {
        if (index < wrongGuesses) {
            part.style.display = "block";
        }
    });

    if (data.won) {
    window.location.href = "/win";
}

if (data.lost) {
    window.location.href = "/lose";
}

});

}

startGame();
