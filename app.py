from flask import Flask
from flask import request
from flask import Response
from flask import status
from datetime import datetime

app = Flask(__name__)

@app.route('/date_service',methods=['GET'])
def date_service_get():

    if 'start_date' in request.args and 'end_date' in request.args:

        start_date = datetime.strptime(request.args.get('start_date'), "%Y-%m-%d")
        end_date = datetime.strptime(request.args.get('end_date'), "%Y-%m-%d")

        return {
            'days':(end_date - start_date).days
        }

    return Response("Error on input", status=400)

app.run()