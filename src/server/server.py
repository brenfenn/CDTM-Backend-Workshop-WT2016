#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file,jsonify
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



VERSION =2.0

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




if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)