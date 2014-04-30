from flask import Flask, render_template, redirect
from flask.ext.pymongo import PyMongo
from pymongo.errors import DuplicateKeyError
from helpers.forms import SignupForm, UnsubscribeForm
from helpers.util import parse_phone_number, notify_taco_lover, get_taco_pun

app = Flask(__name__)
app.config.from_envvar('WAT_TACO_SETTINGS')

mongo = PyMongo(app)

@app.route('/')
def index():
    signup_form = SignupForm()
    return render_template('index.html', form=signup_form, pun=get_taco_pun())

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/signup', methods=['POST'])
def signup():
    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        try:
            phone_number = parse_phone_number(signup_form.phone_number.data)
            mongo.db.taco_lovers.ensure_index('phone_number', unique=True)
            mongo.db.taco_lovers.insert({
                'phone_number' : phone_number
            })
            notify_taco_lover(phone_number)

            return redirect('/success')
        except DuplicateKeyError:
            signup_form.phone_number.errors.append("You've already registered for notifications!")
        except:
            return redirect('/fail')

    return render_template('index.html', form=signup_form, pun=get_taco_pun())

@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    unsub_form = UnsubscribeForm()

    if unsub_form.validate_on_submit():
        try:
            phone_number = parse_phone_number(unsub_form.phone_number.data)
            taco_lover = mongo.db.taco_lovers.find_one({
                'phone_number' : phone_number
            })

            if not taco_lover:
                unsub_form.phone_number.errors.append("That phone number isn't subscribed.")
            else:
                mongo.db.taco_lovers.remove({
                    'phone_number' : phone_number
                })
                return render_template('unsubscribe_success.html', form=unsub_form)
        except:
            return redirect('/fail')

    return render_template('unsubscribe.html', form=unsub_form)


if __name__ == '__main__':
    app.run()
