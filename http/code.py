from flask import Flask, redirect, url_for, request
app = Flask("test")

@app.route('/')
def homepage():
   return "<h1> Homepage </h1> <i>this is the homepage</i><br> <br> <a href='/login'> Login </a>"

@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    print("login here - POST request")
    return f"Hi, {request.form['name']}"

  elif request.method == "GET":
    print("login here - GET request")
    return """
            <h1> Log-in Page </h1>
            <form id="1" action="/login" method="POST">
                <label for="name">First name:</label><br>
                <input type="text" id="name" name="name" value="kris"><br> <br>
                <input type="submit" value="Submit">  <br> <br>
            </form>
           """
  return "login here - request method not supported."

if __name__ == '__main__':
   app.run()

