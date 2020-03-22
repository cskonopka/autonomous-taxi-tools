
from flask import Flask
from flask_cors import CORS
import RPi.GPIO as GPIO
import time
 
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
p.ChangeDutyCycle(5)
time.sleep(0.5)
p.stop()
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)



app=Flask(__name__)
CORS(app)

@app.route('/')
def index():
        return 'this is a beginning'

@app.route('/meow', methods=['GET', 'POST'])
def meow():
        print ("hiiiii servo")
        p.start(2.5) # Initialization
        p.ChangeDutyCycle(5)

        time.sleep(0.5)
        p.stop()
        return 'MEOW.'

@app.route('/led', methods=['POST'])
def led():
	GPIO.output(14, GPIO.HIGH) # Turn on
	time.sleep(1) # Sleep for 1 second
	GPIO.output(14, GPIO.LOW) # Turn off
	time.sleep(1) # Sleep for 1 second
	return 'pressed'

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
