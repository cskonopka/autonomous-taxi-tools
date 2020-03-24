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
# servo_routine --> Control servo via GPIO
def servo_routine():
    data = request.get_json()
    print(data['choice'])
    data = request.get_json()
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

# led_routine --> Control LEDs via GPIO
def led_routine():
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(14, GPIO.LOW)
    time.sleep(1)

# ~~~~~~~~~~~~~~~ API ~~~~~~~~~~~~~~~
# ENDPOINT --> Index test
@app.route('/')
def index():
    return 'this is a beginning'

# ENDPOINT --> Servo
@app.route('/servo', methods=['GET', 'POST'])
def servo():
    data = request.get_json()
    # Start servo operation
    servo_routine()
    # Return prompt
    return jsonify(
        msg='The heat is set to ' + data['choice']
    )

# ENDPOINT --> LED
@app.route('/led', methods=['POST'])
def led():
    # Start LED operation
    led_routine()
    # Return prompt
    return jsonify(
        msg='Thank you for riding with us!'
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
		return jsonify(msg='Success!')
	elif data['answer'] == 'aptiv':
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
		return jsonify(msg='EASTER EGG')
	else:
		for x in range(0, 3):
			GPIO.output(27, GPIO.HIGH)
			GPIO.output(3, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(27, GPIO.LOW)
			GPIO.output(3, GPIO.LOW)
			time.sleep(0.1)
		return jsonify(msg='INCORRECT')

# ~~~~~~~~~~~~~~~ Flask ~~~~~~~~~~~~~~~
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
