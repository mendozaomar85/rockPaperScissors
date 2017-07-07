from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "Secret"

@app.route("/")
def index():

    session["win"] = session.get("win", 0)
    session["loss"] = session.get("loss", 0)
    session["tie"] = session.get("tie", 0)
    return render_template("index.html")

@app.route("/process_play", methods=["POST"])
def process_play():
    opponentHand = random.randint(0,2)
    arrayHand = ["rock", "paper", "scissors"]
    opponent = arrayHand[opponentHand]
    session["opponentOut"] = opponent
    session["playerHand"] = request.form["hand"]
    if session["playerHand"] == opponent:
        session["tie"] += 1
        session["outcome"] = "tie"
    elif session["playerHand"] == "rock":
        if opponent == "paper":
            session["loss"] += 1
            session["outcome"] = "loss"
        elif opponent == "scissors":
            session["win"] += 1
            session["outcome"] = "win"
    elif session["playerHand"] == "paper":
        if opponent == "rock":
            session["win"] += 1
            session["outcome"] = "win"
        elif opponent == "scissors":
            session["loss"] += 1
            session["outcome"] = "loss"
    elif session["playerHand"] == "scissors":
        if opponent == "rock":
            session["loss"] += 1
            session["outcome"] = "loss"
        elif opponent == "paper":
            session["win"] += 1
            session["outcome"] = "win"
    return redirect("/")

@app.route("/endGame", methods=["POST"])
def endGame():
    session.pop("win")
    session.pop("loss")
    session.pop("tie")
    return redirect("/")


app.run(debug=True)
