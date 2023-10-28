from flask import Blueprint

# going to define the blueprints for our different routes (views)

auth = Blueprint('auth', __name__)  #does not have to be same name as file 

@auth.route("/login")
def login():
    return "<p>Login</p>"


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/signup")
def signup():
    return "<p>Sign Up</p>"