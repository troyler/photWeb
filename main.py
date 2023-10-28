from website import create_app  #website is a python package, will run __init__ on import 

app = create_app()

if __name__ == '__main__':   #only if we run this, not if we import it, this will run 
    app.run(debug = True, host="0.0.0.0")     # without the if statement, importing main would run the web server