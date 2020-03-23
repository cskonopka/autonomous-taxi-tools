from flask import Flask
from flask_cors import CORS
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

# API routes
@app.route('/')
def index():
        return 'this is a beginning'

@app.route('/servo', methods=['GET', 'POST'])
def meow():
        servo_routine()

@app.route('/led', methods=['POST'])
def led():
	led_routine()

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

def servo_routine():
        print ("servo")
        p.start(2.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)
        p.stop()
        return 'The heat is up.'

def led_routine():
        GPIO.output(14, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(14, GPIO.LOW)
        time.sleep(1)
        return 'LED triggered'