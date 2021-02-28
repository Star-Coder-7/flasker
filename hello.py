from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "My super secret key that only I know about"


class NamerForm(FlaskForm):
    name = StringField("What's you name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a route decorator

# def index():
#     return "<h1>Hello World!</h1>"


# FILTERS!!!
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags
# reverse


@app.route('/')
def index():
    firstName = "Shiven"
    stuff = '<strong>This is bold text</strong>'

    favoritePizza = ["Pepperoni", "Cheese and Tomato", "Margarita", 77.77]
    return render_template("index.html", first_name=firstName, stuff=stuff, favorite_pizza=favoritePizza)


# localhost:5000/user/Shiven
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def pageNotFound(e):
    return render_template("500.html"), 500
