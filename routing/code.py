from flask import Flask, abort, render_template, redirect, request, url_for

app = Flask("basic app")

@app.route("/signup")
def signup():
    print("signup here")
    return """
                <h1> Sign Up Page </h1>
                <i>this is the sign up page</i><br> <br> 
                <a href='/login'> Login </a> | <a href='/'> Homepage </a><br> 
            """

@app.route("/login")
def signup():
    print("login here")
    return """
                <h1> Login Page </h1>
                <i>this is the login page</i><br> <br>
                <a href='/signup'> Signup </a> | <a href='/'> Homepage </a><br> 
            """

@app.route("/")
def home():
    print("home here")
    return  """
                <h1> Homepage </h1>
                <i>this is the homepage</i><br> <br> 
                <a href='/login'> Login </a> | <a href='/signup'> Signup </a><br> 
            """
