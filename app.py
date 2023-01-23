from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/exercicio1',methods=['GET'])
def get_service(data_inicio, data_fim):
    return Response(response="isto é um get",
        status = 200,mimetype="application/html")

app.run(debug=True)