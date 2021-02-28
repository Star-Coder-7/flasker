from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "My super secret key that only I know about"


class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

    # BooleanField
    # DateField
    # DateTimeField
    # DecimalField
    # FileField
    # HiddenField
    # MultipleField
    # FieldList
    # FloatField
    # FormField
    # IntegerField
    # PasswordField
    # RadioField
    # SelectField
    # SelectMultipleField
    # SubmitField
    # StringField
    # TextAreaField

    # Validators
    # DataRequired
    # Email
    # EqualTo
    # InputRequired
    # IPAddress
    # Length
    # MacAddress
    # NumberRange
    # Optional
    # Regexp
    # URL
    # UUID
    # AnyOf
    # NoneOf

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
    # flash("Welcome to our website!!")
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


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!")

    return render_template("name.html", name=name, form=form)