import flask
from flask import request, jsonify
import random
app = flask.Flask(__name__)
app.config["DEBUG"] = True
def reverse(s): 
  str = ""
  for i in s:
    str = i + str
  return str
@app.route('/app/json', methods=['POST','GET'])
def rev():
    new = request.get_json()
    new["message"] = reverse(new["message"])
    new["random"] = round(random.uniform(1.0,100.0),2)
    return jsonify(new)
app.run(port=4000)