
from flask import Flask
from flask_cors import CORS
from flask import request
import time

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
        return 'this is a beginning'


@app.route('/meow', methods=['GET', 'POST'])
def meow():
        data = request.get_json()
        print(data)
        # ... do your business logic, and return some response
        # e.g. below we're just echo-ing back the received JSON data
        return 'MEOW.'


@app.route('/json-example', methods=['POST'])  # GET requests will be blocked
def json_example():
	data = request.get_json()
	if data['language'] == '0':
		print('low')
		i = 0
		while i == 0:
  	  p.ChangeDutyCycle(5)
  	  time.sleep(0.5)
  	  p.ChangeDutyCycle(7.5)
  	  time.sleep(0.5)
  	  p.ChangeDutyCycle(10)
  	  time.sleep(0.5)
  	  p.ChangeDutyCycle(12.5)
  	  time.sleep(0.5)
  	  p.ChangeDutyCycle(10)
  	  time.sleep(0.5)
  	  p.ChangeDutyCycle(7.5)
  	  time.sleep(0.5)
  	  p.ChangeDutyCycle(5)
  	  time.sleep(0.5)
  	  p.ChangeDutyCycle(2.5)
  	  time.sleep(0.5)
	elif data['language'] == '1':
		print('med')
	elif data['language'] == '2':
		print('high')

	return 'tester'

@app.route('/led', methods=['POST'])
def led():
	return 'pressed'

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
