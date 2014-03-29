from flask import Flask, render_template, redirect
from flask.ext.pymongo import PyMongo
from pymongo.errors import DuplicateKeyError
from helpers.forms import SignupForm
from helpers.util import parse_phone_number

app = Flask(__name__)
app.config.from_envvar('WAT_TACO_SETTINGS')

mongo = PyMongo(app)

@app.route('/')
def index():
    signup_form = SignupForm()
    return render_template('index.html', form=signup_form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/signup', methods=['POST'])
def signup():
    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        try:
            mongo.db.taco_lovers.ensure_index('phone_number', unique=True)
            mongo.db.taco_lovers.insert({
                'phone_number' : parse_phone_number(signup_form.phone_number.data)
            })
            return redirect('/success')
        except DuplicateKeyError:
            signup_form.phone_number.errors.append("You've already registered for notifications!")
        except:
            return redirect('/fail')

    return render_template('index.html', form=signup_form)


if __name__ == '__main__':
    app.run()
