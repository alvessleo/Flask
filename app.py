from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def date():
    return render_template('date.html')

def calculate_dif_dates(start_date, end_date):
    days = (end_date-start_date).days
    weeks = int(days/7)
    months = 12 * (end_date.year - start_date.year) + end_date.month - start_date.month

    return {
        'days': days,
        'weeks': weeks,
        'months': months
    }


@app.route('/date_service',methods=['GET'])
def date_service_get():

    if request.is_json and 'start_date' in request.args and 'end_date' in request.args:

        start_date = datetime.strptime(request.args.get('start_date'), "%Y-%m-%d")
        end_date = datetime.strptime(request.args.get('end_date'), "%Y-%m-%d")

        return calculate_dif_dates(start_date, end_date)

    return Response("Error on input", status=400)


@app.route('/date_service',methods=['POST'])
def date_service_post():

    if 'start_date' in request.json and 'end_date' in request.json:

        start_date = datetime.strptime(request.args.json['start_date'], "%Y-%m-%d")
        end_date = datetime.strptime(request.args.json['end_date'], "%Y-%m-%d")

        return calculate_dif_dates(start_date, end_date)

    return Response("Error on input", status=400)

app.run()