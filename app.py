import logging

from flask import Flask
from flask import request

from PuzzleSolution import PuzzleSolution

app = Flask(__name__)

logging.basicConfig(filename='filename.log', level=logging.DEBUG)
# /?q=Ping&d=Please+return+OK+so+that+I+know+your+service+works.
# /?q=Years&d=How+many+years+of+software+development+experience+do+you+have%3F
# /?q=Degree&d=Please+list+your+relevant+university+degree(s).
# /?q=Email+Address&d=What+is+your+email+address%3F
#  /?q=Puzzle&d=Please+solve+this+puzzle%3A%0A+ABCD%0AA--%3C-%0AB---%3E%0AC--%3D-%0AD--%3E-%0A
# /?q=Source&d=Please+provide+a+URL+where+we+can+download+the+source+code+of+your+resume+submission+web+service.
# /?q=Phone&d=Please+provide+a+phone+number+we+can+use+to+reach+you.
#  /?q=Status&d=Can+you+provide+proof+of+eligibility+to+work+in+the+US%3F
# /?q=Position&d=Which+position+are+you+applying+for%3F
#  /?q=Resume&d=Please+provide+a+URL+where+we+can+download+your+resume+and+cover+letter.
#  /?q=Name&d=What+is+your+full+name%3F
#  /?q=Referrer&d=How+did+you+hear+about+this+position%3F

answers = {
        "Ping": "OK",
        "Years": "I've experience of more than 5 years.",
        "Degree": "I've BS(CS) degree, And my MS is continued. My thesis is pending which will be completed in a month.",
        "Email Address": "arslanarshad07@gmail.com",
        "Puzzle": "-(^^)-",
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
        if answer == '-(^^)-':
            return PuzzleSolution().solve(request.args['d'])
    except:
        answer = "Something went wrong"
    return answer


app.run(debug=False, host='0.0.0.0', port=5000)
