from flask import Flask, abort, render_template, redirect, request, url_for

app = Flask("basic app")

@app.route("/signup")
def signup():
    print("signup here")
    return """
                <style> .div-1 {background-color: black;} </style>
                <div class="div-1">
                    <h1> Sign up Page </h1>
                    <i>this is the sign up page</i><br> <br> 
                    <a href='/login'>Login</a> | 
                    <a href='/'>Home page</a><br> 
                </div>
            """
@app.route("/")
def home():
    print("home here")
    return  """
                <style> .div-1 {background-color: darkred;} </style>
                <div class="div-1">
                    <h1> Home Page </h1>
                    <i>this is the home page</i><br> <br> 
                    <a href='/login'>Login</a> | 
                    <a href='/signup'>Signup</a><br> 
                </div>
            """
        
@app.route("/404")
def error404():
    print("404 error here")
    return aort(404)

@app.route("/template")
def template():
    print("templating")
    return render_template("hi {{ name }}, {{ age }}", name="kris", age=23)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   html_text = """  <html>
                        <body>
                            {% for key in result %}
                            <tr>
                                <th>Key: {{ key }}</th> 
                                <td> | Value: {{ result[key] }}</td> 
                            </tr><br>
                            {% endfor %}
                        </body>
                    </html>"""
   return render_template(html_text, result = dict)
    
@app.route("/redirect_to_home")
def redirect_to_home():
    return redirect(url_for("home"))

@app.route('/blog/<user>/<int:postID>/<float:weight>')
def dynamic(user, postID, weight):
    return f"this user {user} with ID {postID} and weight {weight} kg"
    
@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    print("login here - POST request")
    return f"""Hi, {request.form["name"]} <br> <br> 
                    <a href='/signup'>Login</a> | 
                    <a href='/'>HomePage</a><br> """
  elif request.method == "GET":
    print("login here - GET request")
    return """
            <style> .div-1 {background-color: darkblue;} </style>
            <div class="div-1">
                <h1> Log-in Page </h1>
                <form id="1" action="/login" method="POST">
                    <label for="name">First name:</label><br>
                    <input type="text" id="name" name="name" value="John"><br> <br>
                    <input type="submit" value="Submit">  <br> <br>
                </form>
                <br> <br> 
                    <a href='/signup'>Sign up</a> | 
                    <a href='/'>Home page</a><br> 
            </div>
           """
  return "login here - request method not supported."

if __name__ == '__main__':
    app.run()
    
