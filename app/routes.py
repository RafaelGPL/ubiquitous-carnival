from flask import Flask     # from the flask module import the Flask class
# OOP - object oriented paradigm
app = Flask(__name__)       # create an instance of Flask into app (object)

@app.get("/")               # Flask decorator for defining routes
def index():                # A wrapped function is called a "view function"
    me = {                  # python3 dictionary
        "first_name": "Rafael",
        "last_name": "GPL",
        "hobbies": "DIY stuff",
        "is_online": True
    }
    return me               # when you return a dictionary, it is converted to JSON
