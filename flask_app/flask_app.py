# Importing the flask module
from flask import Flask, request, jsonify
# import translation and blinky code
import ConvertToMorse

# Create a flask object named app
app = Flask(__name__)

# When someone will enter the IP address of Raspberry Pi in the browser, below code will run.
@app.route("/")
def main():
	return "Howdy!"

# test route
@app.route("/test")
def test():
	ConvertToMorse.blink_morse_message("Howdy")
	return "Test!"

# Route for sending morse messages to the pi
@app.route('/morse', methods=['POST'])
def morse():
	if request.method == 'POST':
		message = request.json['message']
		ConvertToMorse.blink_morse_message(message)

#if code is run from terminal
if __name__ == "__main__":
	# Server will listen to port 80 and will report any errors.
   app.run(host='0.0.0.0', port=80, debug=True)