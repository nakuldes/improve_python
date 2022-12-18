from flask import Flask, jsonify
from markupsafe import escape
from adder import AddTwoDigits as ad
import os


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/arm/<string:n>")
def first_api(n):
    build_cmd()
    return f"Hello, {escape(n)}!"

def build_cmd():
    global cmd
    cmd = "python .\\Networking\\file_server.py"
    
    print(cmd)
    execute_cmd()

def execute_cmd():
    os.system(cmd)

if __name__=='__main__':
    app.run(debug=True)