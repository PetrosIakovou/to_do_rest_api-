from flask import Blueprint, request, jsonify, abort
# import uuid # i use it to ccreate unique id before insert the database
from extensions import db
from models.tasks import Tasks
from sqlalchemy import text
import pandas  

from error_handlers import handle_404, handle_401, handle_500

tasks = Blueprint("tasks", __name__)

tasks_data = {} # i use this before insert the data base now i can deleted


#abort and try except
# use abort for http errors - use try except for program logic errors
# see decorator with put method when task_id == 1
# without the decorator the abort(4xx) will return a default message for the code (for ex 401)
# using the decorator the json will return where error.description in the default error messafe for the code
# @tasks.errorhandler(401)
# def handle_401(error):
#     return jsonify({
#         "error": "Not Found",
#         "message": error.description or "The id == 1"
#     }), 401

# Register error handlers with Flask. for not having the error handlers in a file, a error_handler file can created and import the error it needed
tasks.register_error_handler(404, handle_404)


@tasks.route("/")
def get_tasks():

    # Using SQL
    result = db.session.execute(text("SELECT * FROM tasks"))  # Execute raw SQL
    rows = result.fetchall()  # Fetch all rows
    tasks_json = [row._asdict() for row in rows]  # Convert rows to dictionaries
    return jsonify(tasks_json)
    
    # Using SQL and Pandas
    # result = db.session.execute(text("SELECT * FROM tasks"))  # Execute raw SQL
    # rows = result.fetchall()  # Fetch all rows
    # df = pandas.DataFrame(rows, columns=result.keys())
    # tasks_dict = df.to_dict(orient="records")
    # return tasks_dict

    # Using Class Tasks
    # result = db.session.query(Tasks).all()
    # tasks = [task.to_dict() for task in result]
    # return jsonify(tasks)
     
   

@tasks.route("/", methods=["POST"])
def create_task():

    # task_id = uuid.uuid4().hex   --> when i use dictionary , not database
    # tasks_data[task_id] = task  --> when i use dictionary , not database
    task =  Tasks(**request.get_json()) # data = request.get_json() and task_db = Tasks(title= data['title'], date=data['date'])
    db.session.add(task)
    db.session.commit()
    # return jsonify(tasks_data)
    return {"message": "task in db"}

@tasks.route("/update/<task_id>", methods=["PUT"])
def update_task(task_id):
   
    if int(task_id) == 1:
        abort (404)
    query = text("""UPDATE tasks SET title = :title, date = :date WHERE id = :task_id""")
    data = request.get_json()
    db.session.execute(query, {
        "title": data.get("title", None),
        "date": data.get("date", None),
        "task_id": task_id
    })


    db.session.commit()

    return {"message": "task updated"}

@tasks.route("/delete/<store_id>", methods=["DELETE"])
def delete_task(store_id):
    
    # Using Class Tasks
    # result = db.session.query(Tasks).all()
    # tasks = [task.to_dict() for task in result]
    # return jsonify(tasks)

    task = Tasks.query.get_or_404(store_id)
    db.session.delete(task)
    db.session.commit()
    return {"message": "Store deleted"}
