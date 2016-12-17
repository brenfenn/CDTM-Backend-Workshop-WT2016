#!/usr/bin/env python
# coding: utf8
from flask import Flask, send_file
import sys

# allow special characters (e.g. üäö ...)
reload(sys)
sys.setdefaultencoding('utf-8')

# Note: Setting static_url_path to '' has the following effect:
#   - Whenever a file is requested and there is no matching route defined
#     the flask server will look whether the file is in the 'static/' folder
#   - As a consequence, everyone can remotely access files within 'static/'
#   - We need this, so that the front-end works properly.
app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def server_return():
    filepath = '/Users/brendanfennessy/Documents/School/Programming/CDTMBackendWorkshop/src/server/static/index.html'
    content = send_file(filepath)
    return content


if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)
