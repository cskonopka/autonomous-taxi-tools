# ~~~~~~~~~~~~~~~ Imports ~~~~~~~~~~~~~~~
# Flask
from flask import Flask
from flask_cors import CORS
from flask import request
from flask import jsonify

# Raspberry Pi
import RPi.GPIO as GPIO

# General
import time

# ~~~~~~~~~~~~~~~ Flask ~~~~~~~~~~~~~~~
app = Flask(__name__)
CORS(app)

# ~~~~~~~~~~~~~~~ RPi GPIO Setup ~~~~~~~~~~~~~~~
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Servo setup
GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 50)

# Buzzer setup
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)

# LED setup
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)  # press
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)  # passcode yes
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)  # passcode no

# ~~~~~~~~~~~~~~~ RPi GPIO Functions ~~~~~~~~~~~~~~~
# ac_routine --> Control servo via GPIO
def ac_routine():
    data = request.get_json()
    print(data['choice'])
    if data['choice'] == 'Low':
        print('low')
        p.start(2.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        p.stop()
    elif data['choice'] == 'Medium':
        print('med')
        p.start(5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.stop()
    elif data['choice'] == 'High':
        print('high')
        p.start(7)
        p.ChangeDutyCycle(12.5)
        time.sleep(0.5)
        p.stop()

# dropoff_routine --> Control LEDs via GPIO
def dropoff_routine():
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(14, GPIO.LOW)
    time.sleep(1)

# ~~~~~~~~~~~~~~~ API ~~~~~~~~~~~~~~~
# ENDPOINT --> Ambient Cooling
@app.route('/ac', methods=['POST'])
def ac():
    data = request.get_json()
    # Start servo operation
    ac_routine()
    # Return alert
    return jsonify(
        msg='Ambient Cooling set to ' + data['choice']
    )

# ENDPOINT --> Dropoff
@app.route('/dropoff', methods=['POST'])
def dropoff():
    # Start LED operation
    dropoff_routine()
    # Return alert
    return jsonify(
        msg='Thank you for riding with Aptiv!'
    )

# ENDPOINT --> Passcode
@app.route('/passcode', methods=['POST'])
def passcode():
	data = request.get_json()
	if data['answer'] == '1994':
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(2, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(2, GPIO.LOW)
		time.sleep(0.1)
		return jsonify(msg='Enjoy the ride!')
	elif data['answer'] == 'Aptiv':
		for x in range(0, 10):
			GPIO.output(2, GPIO.HIGH)
			GPIO.output(3, GPIO.LOW)
			time.sleep(0.1)
			GPIO.output(2, GPIO.LOW)
			GPIO.output(3, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(2, GPIO.LOW)
			GPIO.output(3, GPIO.LOW)
			time.sleep(0.1)
		return jsonify(msg='Did you miss the light show?')
	else:
		for x in range(0, 3):
			GPIO.output(27, GPIO.HIGH)
			GPIO.output(3, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(27, GPIO.LOW)
			GPIO.output(3, GPIO.LOW)
			time.sleep(0.1)
		return jsonify(msg='Invalid passcode!')

# ~~~~~~~~~~~~~~~ Flask ~~~~~~~~~~~~~~~
if __name__ == '__main__':
    app.run(debug=False	, host='0.0.0.0')