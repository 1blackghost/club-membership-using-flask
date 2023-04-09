# imports
from main import app
from flask import request, jsonify, session, abort, make_response
import json
from DBMS import helper

@app.route("/submitForm", methods=["POST", "GET"])
def simple():
    if 'name' not in request.form:
        # Return an error response if 'name' key is not present in the form data
        return make_response('Bad Request: Missing "name" parameter', 400)
    name = request.form["name"]
    print(name)
    email = request.form["email"]
    age = request.form["age"]
    uid = helper.insert_this(name, email, age)
    return jsonify({"status":"ok"})

@app.route("/getAll", methods=["POST", "GET"])
def userAll():
    data = tuple(helper.read_for())
    data_list = []
    for t in data:
        d = {"id": t[0], "name": t[1], "email": t[2], "age": t[3]}
        data_list.append(d)
    data_list=reversed(data_list)
    data_list_reversed = list(data_list)

    response = {"status": data_list_reversed}
    return jsonify(response)
