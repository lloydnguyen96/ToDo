# This module is like a layer between client and the database server.
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper


# These decorations wrap the corresponding functions and indicate that the
# functions are endtry points of the server to requests sent from clients.
@app.route("/delete/<int:task_id>", methods=['DELETE'])
def delete(task_id):
    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)


# Each route have their own logic to process data sent from client side.
@app.route("/edit/<int:task_id>", methods=['PUT'])
def update(task_id):
    data = request.get_json()
    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)


# Client requests -> corresponding route -> logic -> database -> response
@app.route("/create", methods=['PUT'])
def create():
    # get requested data as json (Python dictionary)
    data = request.get_json()
    # call to some database interface functions, it's like our DBAPI for
    # Datastore
    db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)  # serialize to JSON-format object as responses


@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)
