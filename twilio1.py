from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("You and I are all as much continuous with the physical universe as a wave is continuous with the ocean.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)