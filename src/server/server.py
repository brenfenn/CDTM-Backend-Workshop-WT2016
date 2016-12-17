#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file,jsonify, json
import sys

from task import Task
from list import List

# allow special characters (e.g. üäö ...)
reload(sys)
sys.setdefaultencoding('utf-8')

myList = List('Inbox', id='0')
myTasks = [
    Task('Think about lunch', '1', id='0', status=Task.COMPLETED),
    Task('Become a pro in backend development', '0', id='1', status=Task.NORMAL),
    Task('CONQUER THE WORLD!', '0', id='2', status=Task.NORMAL)
]

# Note: Setting static_url_path to '' has the following effect:
#   - Whenever a file is requested and there is no matching route defined
#     the flask server will look whether the file is in the 'static/' folder
#   - As a consequence, everyone can remotely access files within 'static/'
#   - We need this, so that the front-end works properly.
app = Flask(__name__, static_url_path='')



VERSION =5.0

@app.route('/', methods=['GET'])
def frontEnd():
    return send_file('static/index.html')

@app.route('/api/version', methods =['GET'])
def API_JSON_VERSION():
    return jsonify({'version': VERSION})

@app.route('/api/lists', methods = ['GET'])
def API_JSON_LIST():
    dict_list=myList.__dict__
    return jsonify({'lists': [dict_list]})

@app.route('/api/lists/<string:list_id>/tasks', methods = ['GET'])
def API_JSON_task(list_id):
    dict_task= {}
    dict_task['tasks'] = [t.__dict__ for t in myTasks if t.list == list_id]
    return jsonify(dict_task)


# CREATE ROUTE
@app.route('/api/lists/<string:list_id>/tasks', methods=['POST'])
def create_task(list_id):
    ''' creates a new task for a list '''

    # 1. Check whether the specified list exists
    if (len([l for l in myLists if l.id == list_id]) < 1):
        json_abort(404, 'List not found')

    # 2. Check whether the required parameters have been sent
    try:
         data = request.get_json()
    except:
        json_abort(400, 'No JSON provided')

    if data == None:
        json_abort(400, 'Invalid Content-Type')

    title = data.get('title', None)
    if title == None:
        json_abort(400, 'Invalid request parameters')

    # 3. calculate the next id
    id = max([int(t.id) for t in myTasks]+[-1]) + 1
    newTask = Task(title, list_id, id=str(id), status = Task.NORMAL)

    # 4. append task to array
    myTasks.append(newTask)

    # 5. return new task
    return jsonify(newTask.__dict__)


@app.route('/api/lists/<string:list_id>/tasks/<string:task_id>', methods=['DELETE'])
def delete_task(list_id,task_id):
    # check if there is a real task to be deleted


    if (len([l for l in myLists if l.id == list_id]) < 1)
        json_abort(404, 'List not found')

    if task_id > len(t for t in myTasks)
        json_abort(404,"Task not found")

    tasks = [t for t in myTasks if t.list == list_id and t.id == task_id]



    dict_task['tasks'] = [t.__dict__ for t in myTasks if t.list == list_id and t.id !=task_id]

    return jsonify(dict_task)




if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)