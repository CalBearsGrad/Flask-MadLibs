"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Get user response to the question "Would you like to play a game?" form"""

    gamer = request.args.get("Radio1")

    if gamer == "No":
        return render_template("goodbye.html")
    elif gamer == "Yes":
        return render_template("game.html")
    else:
        return render_template("confused.html")


@app.route('/madlib')
def show_madlib():
    """Will fill the person, color, noun and adjective provided by the user into a MadLibs-style story"""

    madlibPerson = request.args.get("madlibPerson")
    color = request.args.get("color")
    madlibNoun = request.args.get("madlibNoun")
    madlibAdjective = request.args.get("madlibAdjective")
    if madlibPerson and color and madlibNoun and madlibAdjective:
        return render_template("madlib.html",
                madlibPerson=madlibPerson,
                color=color,
                madlibNoun=madlibNoun,
                madlibAdjective=madlibAdjective)
    else:
        return render_template("confused.html")

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
