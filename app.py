import logging

from flask import Flask
from flask import request

app = Flask(__name__)

logging.basicConfig(filename='filename.log', level=logging.DEBUG)


@app.route("/")
def hello_world():
    logging.info("Data received is mentioned bellow")
    logging.debug(request.data)
    return "OK"


app.run(debug=False, host='0.0.0.0', port=5000)
