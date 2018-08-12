#!/bin/python

from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run(host='192.168.144.141', port=4000)
