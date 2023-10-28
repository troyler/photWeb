from flask import Flask

def create_app():
    app = Flask(__name__)  #this convention represents the name of the file that was ran 
    app.config['SECRET_KEY'] = 'justtypesomerandomstringhere' #will be used to secure the cookies and session data 

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = "/") #all of the urls stored in the blueprints file, prefix will go in front of blueprint path
    app.register_blueprint(auth, url_prefix = "/")


    return app #at this point, we have intialized the app and returned the key 