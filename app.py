"""Flask Web Application"""
"""render_template: used to initialise the html template in the flask app"""


from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])                                     # index page
def rootpage():
    weight = ''
    height = ''
    bmi = ''
    if request.method == "POST" and 'weight' in request.form and 'height' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
    return render_template('index.html',
                            weight=weight,
                            height=height,
                            bmi=bmi)


def calc_bmi(weight, height):
    return round((weight/((height / 100)**2)), 2)


app.run()
