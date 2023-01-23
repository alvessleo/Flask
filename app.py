from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/html')
def html():
    return "<html><body><h1>Formulário datas</h1></body></html>"

app.run(debug=True)