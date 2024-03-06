from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  me = {
    "first_name": "cesar",
    "last_name": "cordova",
    "hobbies": "box",
    "online": True
  }
  return me # in flask we can return a dictionary and flask will convert it to a json object

