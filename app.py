
from flask import Flask
engine = create_engine("sqlite:///hawaii.sqlite")
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'


