from flask import Flask
from flask_cors import CORS
from flask import request
import RPi.GPIO as GPIO
import time

# Servo setup 
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)

# LED setup
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)

# GPIO extras
GPIO.setwarnings(False) # Ignore warning for now

# p.start(2.5)
# p.ChangeDutyCycle(5)
# time.sleep(0.5)
# p.stop()

# Flask app
app=Flask(__name__)

CORS(app)

def servo_routine():
	data = request.get_json()
	print(data['language'])
	print(data['framework'])
	print ("servo")
	p.start(2.5)
	p.ChangeDutyCycle(10)
	time.sleep(0.5)
	p.ChangeDutyCycle(2.5)
	time.sleep(0.5)
	p.stop()

def led_routine():
        GPIO.output(14, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(14, GPIO.LOW)
        time.sleep(1)

# API routes
@app.route('/')
def index():
        return 'this is a beginning'

@app.route('/servo', methods=['GET', 'POST'])
<<<<<<< HEAD
def meow():
        servo_routine()
=======
def servo():
	servo_routine()
	return 'the head is up!'
>>>>>>> b751b855570f499b9c7a265b2a47b41b905c1c83

@app.route('/led', methods=['POST'])
def led():
	led_routine()
	return 'it is up'

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

