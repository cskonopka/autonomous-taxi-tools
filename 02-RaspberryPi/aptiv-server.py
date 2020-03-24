# ~~~~~~~~~~~~~~~ Imports ~~~~~~~~~~~~~~~
# Flask
from flask import Flask
from flask_cors import CORS
from flask import request

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
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)

# ~~~~~~~~~~~~~~~ RPi GPIO Functions ~~~~~~~~~~~~~~~
# servo_routine --> Control servo via GPIO
def servo_routine():
        data = request.get_json()
        print(data['language'])
        print(data['framework'])
        data = request.get_json()
        if data['language'] == '0':
                print('low')
                p.start(2.5)
                p.ChangeDutyCycle(2.5)
                time.sleep(1)
                p.stop()
        elif data['language'] == '1':
                print('med')
                p.start(5)
                p.ChangeDutyCycle(7.5)
                time.sleep(0.5)
                p.stop()
        elif data['language'] == '2':
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

# buzzer_routine --> Control LEDs via GPIO
def buzzer_routine():
        data = request.get_json()
        print(data['language'])
        print(data['framework'])
        data = request.get_json()
        if data['language'] == '0':
                print('low')
                GPIO.output(27, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(27, GPIO.LOW)
                time.sleep(0.1)
        elif data['language'] == '1':
                for x in range(0, 3):
                        GPIO.output(27, GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(27, GPIO.LOW)
                        time.sleep(0.1)
						
# passcode_routine --> Verify passcode with a buzzer
def passcode_routine():
    data = request.get_json()
    print(data['language'])
    print(data['framework'])
    data = request.get_json()
    if data['language'] == '1994':
        GPIO.output(27, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(27, GPIO.LOW)
        time.sleep(0.1)
    else:
        for x in range(0, 3):
            GPIO.output(27, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(27, GPIO.LOW)
            time.sleep(0.1)

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
        return 'the heat is set to ' + data['language']

# ENDPOINT --> LED
@app.route('/led', methods=['POST'])
def led():
        # Start LED operation
        led_routine()
        # Return prompt
        return 'Thank you for riding with us!'

# ENDPOINT --> Buzzer
@app.route('/buzzer', methods=['POST'])
def buzzer():
        # Start LED operation
        buzzer_routine()
        # Return prompt
        return 'buzzed!'

# ENDPOINT --> Passcode
@app.route('/passcode', methods=['POST'])
def passcode():
    # Start LED operation
    passcode_routine()
    # Return prompt
    return 'passcode there'

# ~~~~~~~~~~~~~~~ Flask ~~~~~~~~~~~~~~~
if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')