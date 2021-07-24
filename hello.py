from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migration
from datetime import datetime

# Create a Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = "My super secret key that only I am supposed to know about"
# Initialise the Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Create a Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    favourite_color = db.Column(db.String(120))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    favourite_color = StringField("Favourite Color")
    submit = SubmitField("Submit")


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.favourite_color = request.form['favourite_color']
        try:
            db.session.commit()
            flash("User Updated Successfully")
            return render_template("update.html", form=form, name_to_update=name_to_update)
        except:
            flash("Error, Looks like there was a problem...try again...")
            return render_template("update.html", form=form, name_to_update=name_to_update)
    else:
        return render_template("update.html", form=form, name_to_update=name_to_update)


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


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data, favourite_color=form.favourite_color.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        form.favourite_color.data = ''

        flash('User Added Successfully!')
    our_users = Users.query.order_by(Users.date_added)

    return render_template("add_user.html", form=form, name=name, our_users=our_users)


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
