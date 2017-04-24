from flask import Flask
from data import UNIVS


app = Flask(__name__)


def get_univ(source):
    # univ_name in the following line is only meant to be temporary. The final prodouct will not be hardcoded and will instead take what the user says.
    univ_name = "Georgetown University"
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

# I'm having issues in the following code block. When I try running it with the debugging stuff at the bottom I receive the error 'ValueError: View function did not return a response' from flask.
# @app.route('/')
# @app.route('/index.html')
# def index():
#     univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings = get_univ(UNIVS)
#     return univ_name
#
#     univ_name, city_name, state_name, cost_to_attend, grad_rate, md_earnings

# With this standing after the above and below code blocks are commented out, I receive the desired response in Terminal: ('University of Florida', 'Gainesville', 'Florida', ' $11,778.00 ', '87%', ' $51,100.00 '). This shows that the function I have written works, but something I'm doing with flask doesn't.
test = get_univ(UNIVS)
print test


# if __name__ == '__main__':
#     app.run(debug=True)
