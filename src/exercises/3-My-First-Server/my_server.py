from flask import Flask

app= Flask(__name__)

#define all accessible routes
@app.route('/')
def hello_world():
        return 'Hello World!'


app.run(host="localhost",port=2345,debug=1)
