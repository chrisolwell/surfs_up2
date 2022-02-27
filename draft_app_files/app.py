#Import Flask
from flask import Flask

#create a new instance
app = Flask(__name__)

#Create route
@app.route('/')
def hello_world():
    return 'Hello World'

