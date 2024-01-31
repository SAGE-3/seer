import json
from flask import Flask

app = Flask(__name__)

@app.route("/nl2code")
def nl2code():
    data = json.dumps({"code": "print(\"hello world\")"})
    return data
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()