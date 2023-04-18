"""A madlib game that compliments its users."""

from random import choice, sample
from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]

@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)
    #compliment = ["wowza","oh-so-not-meh","brilliant"]

    return render_template("compliment.html", person=player, compliments=compliments)


    
@app.route("/game")
def show_madlib_form():
    """Show form to play game """
    response = request.args.get("user-choice")
    if response == "yes":
        return render_template("game.html")
    else: 
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    person = request.args.get("person")
    email =  request.args.get("email")
    date =  request.args.get("date")
    password =  request.args.get("password")
    
    payment = request.args.getlist("payment")
    

    return render_template("madlib.html", color = color, noun = noun, adjective = adjective, person = person,email = email, date = date,password = password, payment = payment) 


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
