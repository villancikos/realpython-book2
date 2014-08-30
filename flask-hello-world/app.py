# --- Flask Hello World --- #

#import the Flask class from the flask module
from flask import Flask
#create the application object

app = Flask(__name__)

#error handling
app.config["DEBUG"] = True
#use decorators to link the function to a url

#@app.route("/")
#@app.route("/hello")

#dynamic route

@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string

def hello_world():
	return "Hello, World?!?!?!?!"


@app.route("/test/<search_query>")

def search(search_query):
	return "Your query is: {}".format(search_query)
	#return search_query


#start the development server using the run() method
if __name__ == "__main__":
	app.run()


##then run in terminal inside the ~/Virtualenv/flask command python app.py
