import flask, json
import requests
from flask import request, jsonify
import random
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['POST','GET'])
def retrieve():
    data = request.get_json()
    try:
        error=json.loads('"{}"'.format(data))
        #print(data)
    except TypeError:
        return "Not json"
    if "message" in data:
        url = 'http://localhost:4000/app/json'
        response = requests.post(url,json=data)
        return response.json()
    else: 
        return "No message key"
app.run(port=8000)