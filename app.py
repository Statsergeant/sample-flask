from flask import Flask
application = Flask(__name__)

@application.get("/")
def home():
    return "Hello from Flask on Elastic Beanstalk!"
