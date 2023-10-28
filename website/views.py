from flask import Blueprint, render_template

# going to define the blueprints for our different routes (views)

views = Blueprint('views', __name__)  #does not have to be same name as file 

@views.route('/')   #decorator to define the root  
def landing():   #this runs whenever we go to this endpoint
        return render_template("base.html")

@views.route('/home')   #decorator to define the root  
def home():   #this runs whenever we go to this endpoint
        return render_template("home.html")