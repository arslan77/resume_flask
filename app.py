import logging

from flask import Flask
from flask import request

app = Flask(__name__)

logging.basicConfig(filename='filename.log', level=logging.DEBUG)

answers = {
        "Ping": "OK",
        "Years": "I've experience of more than 5 years.",
        "Degree": "I've BS(CS) degree, And my MS is continued. My thesis is pending which will be completed in a month.",
        "Email Address": "arslanarshad07@gmail.com",
        "Puzzle": " ABCD\nA=<<<\nB>=>>\nC><=<\nD><>=",
        "Source": "https://github.com/arslan77/resume_flask",
        "Phone": "+923335472627",
        "Status": "I am not located in USA, Neither I have Visa to come to USA. I am a Pakistan national, I've heard about this oppurtunity from Turing, I can work remotely from my current location or relocate if necessary.",
        "Position": "Full Stack Software Engineer (Backend-heavy)",
        "Resume": "https://drive.google.com/file/d/1TQrQJ13CFeKXB7CjzEigwfVf2_H1EJD-/view?usp=sharing",
        "Name": "Muhammad Arslan Arshad",
        "Referrer": "https://www.turing.com/",
    }

@app.route("/")
def hello_world():
    logging.info("Data received is mentioned bellow")
    logging.debug(request.query_string)
    logging.debug(request.data)
    try:
        answer = answers[request.args['q']]
    except:
        answer = "Something went wrong"
    return answer


app.run(debug=False, host='0.0.0.0', port=5000)
