from flask import Flask, render_template, redirect
from helpers.forms import SignupForm, UnsubscribeForm
from helpers.util import notify_taco_lover, get_taco_pun
from models.taco_lovers import TacoLover, TacoLoverNotFoundExcpetion, TacoLoverAlreadyExistsExpection

app = Flask(__name__)
app.config.from_envvar('WAT_TACO_SETTINGS')

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
        taco_lover = TacoLover(signup_form.phone_number.data)

        try:
            taco_lover.save()
            notify_taco_lover(taco_lover.phone_number)
            return redirect('/success')
        except TacoLoverAlreadyExistsExpection:
            signup_form.phone_number.errors.append(
                    "You've already registered for notifications!")
        except:
            return redirect('/fail')

    return render_template('index.html', form=signup_form,
                            pun=get_taco_pun())

@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    unsub_form = UnsubscribeForm()

    if unsub_form.validate_on_submit():
        try:
            taco_lover = TacoLover.find_by_phone_number(
                    unsub_form.phone_number.data)
            taco_lover.delete()
            return render_template('unsubscribe_success.html', form=unsub_form)
        except TacoLoverNotFoundExcpetion:
            unsub_form.phone_number.errors.append(
                    "That phone number isn't subscribed.")
            return render_template('unsubscribe.html', form=unsub_form)

    else:
        return render_template('unsubscribe.html', form=unsub_form)



if __name__ == '__main__':
    app.run()
