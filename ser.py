
from flask import Flask
from flask_cors import CORS
from flask import request
import time

app=Flask(__name__)
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

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    data = request.get_json()
    print(data['language'])
    print(data['framework'])
    return 'fuck'

@app.route('/led', methods=['POST'])
def led():
	return 'pressed'

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
