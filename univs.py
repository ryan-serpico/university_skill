import logging
from flask import Flask
from flask_ask import Ask, statement, question, session
from data import UNIVS

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def get_univ(source, thing2):
    univ_name = thing2
    for row in source:
        if univ_name.lower() == row["univ_name"].lower():
            univ_name = row["univ_name"]
            city_name = row["city_name"]
            state_name = row["state_name"]
            # row[" cost_to_attend "] needs to have the spaces around the variables because that's how it is the python dictionary sadly. Same for md_earnings.
            cost_to_attend = row[" cost_to_attend "]
            grad_rate = row["grad_rate"]
            md_earnings = row[" md_earnings "]

            return univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings
    # You need to get univ_name, city_name, state_name, cost_to_attend, grad_rate and md_earnings.


@ask.launch
def start_skill():
    welcome_message = 'Welcome to University Explorer. What university would you like to know about?'
    return question(welcome_message).reprompt("What university would you like to know about?")

@ask.intent("testIntent")
def test_intent(univName):
    # Here you just want to pass what Alexa here's into a sentence.
    return statement('I heard you say {}.'.format(univName))

@ask.intent("univSearchIntent")
def share_univs(univName):
    univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings = get_univ(UNIVS, univName)
    univ_message = 'The {} is based in {}, {}.  The average annual cost to attend is {}, the graduation rate is {} and the median salary after graduation is {}.'.format(univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings)
    return statement(univ_message).simple_card("School: {}".format(univName), univ_message)

@ask.intent("gradRateIntent")
def grad_rate_intent(univName):
    univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings = get_univ(UNIVS, univName)
    grad_msg = "The graduation rate of {} is {}.".format(univ_name, grad_rate)
    return statement(grad_msg).simple_card("Graduation rate of {}".format(univName), grad_msg)

@ask.intent("univLocationIntent")
def univ_location_intent(univName):
    univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings = get_univ(UNIVS, univName)
    location_msg = "{} is in {}, {}.".format(univ_name, city_name, state_name)
    return statement(location_msg).simple_card("The location of {}".format(univName), location_msg)

@ask.intent("tuitionIntent")
def tuition_intent(univName):
    univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings = get_univ(UNIVS, univName)
    tuition_msg = "The cost to attend {} each year comes out to be {}.".format(univ_name, cost_to_attend)
    return statement(tuition_msg).simple_card("The cost to attend {}".format(univName), tuition_msg)

@ask.intent("earningsIntent")
def earnings_intent(univName):
    univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings = get_univ(UNIVS, univName)
    earnings_msg = "The median salary after graduating from {} is {}.".format(univ_name, md_earnings)
    return statement(earnings_msg).simple_card("Median earnings after attending {}".format(univName), earnings_msg)

@ask.intent("aboutIntent")
def about_intent():
    return statement("All of my information is from the Department of Education's college scorecard dataset.")

@ask.intent("AMAZON.StopIntent")
def stop():
    return statement("Stopping")





if __name__ == '__main__':

    app.run(debug=True)
