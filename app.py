from flask import Flask
import logging
from flask import request

app = Flask(__name__)

logging.basicConfig(filename='filename.log', level=logging.DEBUG)


@app.route("/")
def hello_world():
    logging.info("Data received is mentioned bellow")
    logging.debug(request.data)
    return "Hi there, My name is Arslan Arshad"


app.run()
