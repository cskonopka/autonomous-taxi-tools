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
        GPIO.output(8, GPIO.HIGH) # Turn on
        sleep(1) # Sleep for 1 second
        GPIO.output(8, GPIO.LOW) # Turn off
        sleep(1) # Sleep for 1 second

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
