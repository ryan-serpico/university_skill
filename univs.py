import logging
from flask import Flask
from flask_ask import Ask, statement, question, session
from data import UNIVS

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def get_univ(source):
    univ_name = "University of Florida"
    for row in source:
        if univ_name == row["univ_name"]:
            univ_name = row["univ_name"]
            city_name = row["city_name"]
            state_name = row["state_name"]
            # row[" cost_to_attend "] needs to have the spaces around the variables because that's how it is the python dictionary sadly. Same for md_earnings.
            cost_to_attend = row[" cost_to_attend "]
            grad_rate = row["grad_rate"]
            md_earnings = row[" md_earnings "]

            return univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings
    # You need to get univ_name, city_name, state_name, cost_to_attend, grad_rate and md_earnings.

test = get_univ(UNIVS)
print test

@ask.launch
def start_skill():
    welcome_message = 'Welcome to University Explorer. What university would you like to know about?'
    return question(welcome_message)

@ask.intent(testIntent)
def test_intent():
    # Here you just want to pass what Alexa here's into a sentence.
    return statement('I heard you say {}.'.format(univ_name))

@ask.intent(univSearchIntent)
def share_univs():
    univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings = get_univ()
    univ_message = 'The {} is based in {}, {}.  The average annual cost to attend is {}, the graduation rate is {} and the median salary after attending is {}.'.format(univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings)
    return statement(univ_message)





















if __name__ == '__main__':

    app.run(debug=True)
