from flask import Flask, abort
app = Flask(__name__)

@app.route("/400")
def errorBadRequest():
    print("400 error here")
    return abort(400)

@app.route("/401")
def errorUnauthenticated():
    print("401 error here")
    return abort(401)
        
@app.route("/404")
def errorNotFound():
    print("404 error here")
    return abort(404)
 
"""  
All Supported Error Codes
    400 − for Bad Request
    
    401 − for Unauthenticated
    
    403 − for Forbidden
    
    404 − for Not Found
    
    406 − for Not Acceptable
    
    415 − for Unsupported Media Type
    
    429 − Too Many Requests
"""

@app.route("/")
def home():
    return "this is home"

if __name__ == '__main__':
   app.run()
