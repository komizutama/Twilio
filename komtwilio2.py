from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

callers = {
	"+13364149088" : "Dad",
	"+13364060621" : "Mom",
	"+17275129636" : "Master",
	"+13523320185" : "Alice",
	"+19178434509" : "Alicia",
	"+18285056243" : "Evan",
	"+19176407335" : "Robin",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

	#get the caller's phone number from incoming twilio request
	from_number = request.values.get('From', None)

	"""Respond to incoming requests."""
	resp = twilio.twiml.Response()

	if from_number in callers:
		resp.say("hello" + callers[from_number])
	else:
		resp.say("Hello mostly hairless ape, ")

	resp.say("Allan watts said, You and I are all as much continuous with the physical universe as a wave is continuous with the ocean. ")
	resp.say(" But, Biggie Smalls said, I love it when you call me Big Pop uh. ")
	resp.say("Throw your hands in the air if use a true play uh. ")
	resp.say("I'm just a computer, I don't understand!")
	return str(resp)
if __name__ == "__main__":
    app.run(debug=True)