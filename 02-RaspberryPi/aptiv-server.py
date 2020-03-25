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
import os

# ~~~~~~~~~~~~~~~ Flask ~~~~~~~~~~~~~~~
app = Flask(__name__)
CORS(app)

# ~~~~~~~~~~~~~~~ RPi GPIO Setup ~~~~~~~~~~~~~~~
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO pins
servoPin=17
buzzerPin=27
bluePin=14
greenPin=2
redPin=3

# Servo setup
GPIO.setup(servoPin, GPIO.OUT)
p = GPIO.PWM(servoPin, 50)

# Buzzer setup
GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)

# LED setup
GPIO.setup(bluePin, GPIO.OUT, initial=GPIO.LOW)  # press
GPIO.setup(greenPin, GPIO.OUT, initial=GPIO.LOW)  # passcode yes
GPIO.setup(redPin, GPIO.OUT, initial=GPIO.LOW)  # passcode no

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
    GPIO.output(bluePin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(bluePin, GPIO.LOW)
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
	if data['answer'] == os.getenv('APTIV_PASSCODE'):
		GPIO.output(buzzerPin, GPIO.HIGH)
		GPIO.output(greenPin, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(buzzerPin, GPIO.LOW)
		GPIO.output(greenPin, GPIO.LOW)
		time.sleep(0.1)
		return jsonify(msg='Enjoy the ride!')
	elif data['answer'] == 'Aptiv':
		for x in range(0, 10):
			GPIO.output(greenPin, GPIO.HIGH)
			GPIO.output(redPin, GPIO.LOW)
			time.sleep(0.1)
			GPIO.output(greenPin, GPIO.LOW)
			GPIO.output(redPin, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(greenPin, GPIO.LOW)
			GPIO.output(redPin, GPIO.LOW)
			time.sleep(0.1)
		return jsonify(msg='Did you miss the light show?')
	else:
		for x in range(0, 3):
			GPIO.output(buzzerPin, GPIO.HIGH)
			GPIO.output(redPin, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(27, GPIO.LOW)
			GPIO.output(redPin, GPIO.LOW)
			time.sleep(0.1)
		return jsonify(msg='Invalid passcode!')

# ~~~~~~~~~~~~~~~ Flask ~~~~~~~~~~~~~~~
if __name__ == '__main__':
    app.run(debug=False	, host='0.0.0.0')