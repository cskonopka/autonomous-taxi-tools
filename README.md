<p align="center">
  <img width="65%" height="65%" src="https://i.ibb.co/7twxPvD/aptiv.png"/>  
</p>

*ATT* or "autonomous-taxi-tools" is a suite of interactive prototypes exploring various HMI interactions using a React Native mobile application and a Raspberry Pi running a Flask server. The purpose is to experiment with creating wireless solutions to enhance the passenger experience.


# Requirements

### React Native

  - Android phone
  - USB-C cable
  - [React-Native](https://reactnative.dev/)
  - [Expo](https://expo.io/)

### Raspberry Pi

  - Raspberry Pi (in my case: 3B+)
  - Raspbian OS
  - Python3
  - Flask
  - USB-C power supply
  - Hookup wire
  - Breadboard
  - LEDs (+ resistors)
  - Buzzer
  - Servo
  - USB WiFi adapter (optional)

# Design Ideas

### *Ambient Cooling* 

Set the mode of AC when a ride has started. A servo motor is used to represent a servo that would increase or decrease the flow of air by the AC during a ride.

### *Dropoff*

A trigger used by the passenger to end the current ride and drop a passenger off at the current location.

### *Rider Verification Passcode* 

When the vehicle arrives, the passenger uses a passcode interface to verify that it is the correct passenger and the correct vehicle.



# Workflow Overview

<p align="center">
  <img width="85%" height="85%" src="https://i.ibb.co/GPWnYtB/Aptiv-taxitools-Workflow3.png"/>  
</p>

The project comprises two main sections:

- *React-Native*: A cross-platform application for taking human input and sending the interaction data to a server using HTTP POST request. 
- *Raspberry Pi Server*: A remote hardware server and API that receives HTTP POST requests from a React-Native application. Each request has a dedicated API route which triggers a specific hardware response. Once the hardware routine is complete, it sends a JSON response to the React-Native application and appears as an *alert*.

# React-Native

<p align="center">
  <img width="30%" height="30%" src="https://i.ibb.co/NxhPBXZ/aptiv-taxitools-reactnative.png"/>  
</p>

The primary file for the React-Native application is *App.js*. Find all interactions within this file.

### Ambient Cooling

<p align="center">
  <img width="50%" height="50%" src="https://i.ibb.co/cttzNyh/aptiv-taxitools-ambientcooling.png"/>  
</p>

A rider can select from three settings of "Ambient Cooling"; Low, Medium and High.

```javascript
<View style={styles.textContainer} >
  <Text style={{ fontSize: 24 }}>Ambient Cooling</Text>
</View>
<View style={styles.acContainer} >
  <Button
    title="Low"
    onPress={() => this._onPressAC('Low')}
  />
  <Button
    title="Medium"
    onPress={() => this._onPressAC('Medium')}
  />
  <Button
    title="High"
    onPress={() => this._onPressAC('High')}
  />
</View>
```

- Each choice (*Low*, *Medium*, *High*) creates an HTTP POST request and passes the choice to the server. When complete, it sends a JSON response to the mobile application and creates an alert.

  ``` javascript
  _onPressAC(key) {
    console.log(key)
    fetch(url+'/ac', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        choice: key,
      }),
    })
      // Server response
      .then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson.msg);
      })
      .catch((error) => {
        alert("something went wrong :/");
      });
  }
  ```

  - *Low*

    <p align="center">
      <img width="50%" height="50%" src="https://i.ibb.co/xzPq4T0/Aptiv-taxitools-Response-Low.png"/>  
    </p>

  - *Medium*

    <p align="center">
    <img width="50%" height="50%" src="https://i.ibb.co/w74bQx2/Aptiv-taxitools-Response-Medium.png"/>  
    </p>

  - *High*

    <p align="center">
    <img width="50%" height="50%" src="https://i.ibb.co/Yb9s3LC/Aptiv-taxitools-Response-High.png"/>  
    </p>

### Dropoff

<p align="center">
  <img width="50%" height="50%" src="https://i.ibb.co/HYBDkg0/aptiv-taxitools-Arrived.png"/>  
</p>

A rider decides they would like to end the ride before arriving at the destination. The rider selects the *Dropoff* button, triggering an HTTP request.

```javascript
<View style={styles.textContainer} >
  <Text style={{ fontSize: 24 }}>Arrived?</Text>
</View>
<View style={styles.ledContainer} >
  <Button
    onPress={this._onPressLED}
    title="Dropoff"
  />
</View>
```

- On press the function creates an HTTP POST request and illuminates an LED. When complete, it sends a JSON response to the mobile application and creates an alert.

  ```javascript
  _onPressDropoff() {
    fetch(url+'/dropoff', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      }
    })
      // Server response
      .then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson.msg);
      })
      .catch((error) => {
        alert("something went wrong :/");
      });
  }
  ```

  <p align="center">
    <img width="50%" height="50%" src="https://i.ibb.co/ygkN2W5/Aptiv-taxitools-Response-LED.png"/>  
  </p>

### Rider Verification Passcode

<p align="center">
  <img width="50%" height="50%" src="https://i.ibb.co/GnMktCy/aptiv-taxitools-passcode.png"/>  
</p>

When a vehicle arrives, it will prompt the rider to enter a passcode received previously. The goal is to verify if the current passenger is the correct passenger.

- *Enter a passcode*: Enter a valid passcode and set the state of the associated variable.

  ```javascript
  <View style={styles.textContainer} >
    <Text style={{ fontSize: 24 }}>Rider Passcode Verification</Text>
  </View>
  <View style={styles.passcodeContainer} >
    <TextInput
      style={{ height: 45, borderColor: "black", borderWidth: 2 }}
      placeholder="  Enter the passcode"
      onChangeText={TextInputValue => this.setState({ TextInputValue })}
      underlineColorAndroid="transparent"
    />
    <Button
      onPress={this._onPressPasscode}
      title="Submit"
    />
  </View>
  ```

- *Submit*: HTTP POST request to */passcode* on press to validate the passcode. When complete, it sends a JSON response to the mobile application and creates an alert.

  ```javascript 
  _onPressPasscode = () => {
    const { TextInputValue } = this.state;
    fetch(url+'/passcode', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        answer: TextInputValue
      })
    })
      // Server response
      .then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson.msg);
      })
      .catch((error) => {
        alert("something went wrong :/");
      });
  }
  ```

  <p align="center">
    <img width="50%" height="50%" src="https://i.ibb.co/7JHsx9j/Aptiv-taxitools-Response-Incorrect.png"/>  
  </p>

  <p align="center">
    <img width="50%" height="50%" src="https://i.ibb.co/qN3gdPB/Aptiv-taxitools-Response-Success.png"/>  
  </p>

# Raspberry Pi + Python3 + Flask

<p align="center">
  <img width="85%" height="85%" src="https://i.ibb.co/rM8djv3/aptiv-taxitools-rpi.png"/>  
</p>

On the Raspberry Pi is a Flask server running an API that receives HTTP POST requests from the React-Native application. When a user presses a button or submits a passcode, it sends the request to the Flask server. Mobile interactions link to Python functions, which hardware processes via API routes. When the Python function finishes, it sends a JSON response to the React-Native application and creates an alert.

### API routes

#### /ac

Receive the *Ambient Cooling* choice and change the position of the servo motor. Send a JSON response to the React-Native application.

```python
@app.route('/ac', methods=['POST'])
def ac():
    data = request.get_json()
    # Start servo operation
    ac_routine()
    # Return alert
    return jsonify(
        msg='Ambient Cooling set to ' + data['choice']
    )

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
```

#### /dropoff

Receive the trigger to end the ride and illuminate an LED. Send a JSON response to the React-Native application.

```python
@app.route('/dropoff', methods=['POST'])
def dropoff():
    # Start LED operation
    dropoff_routine()
    # Return alert
    return jsonify(
        msg='Thank you for riding with Aptiv!'
    )
  
def dropoff_routine():
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(14, GPIO.LOW)
    time.sleep(1)
```

#### /passcode

Verify the passcode submitted by the rider. Send a JSON response to the React-Native application.

```python
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
```



# How to run?

## React-Native

- Connect the mobile device (in this case, Android) to the computer using an USB-C cable.

- Open a terminal window.

- Change the directory to the *01-React-Native* folder within the repository.

- Start the application. 

  ```bash
  npm start
  ```

  <p align="center">
    <img width="70%" height="70%" src="https://i.ibb.co/d580Ln5/Aptiv-taxitools-expo.png"/>  
  </p>

- A browser window will open, displaying the *Metro Bundler*. Press *Run on Android device/emulator*. The application will create a new bundle and upload the application to the Android device.

  ![](https://i.ibb.co/5Bbbbvf/Aptiv-taxitools-metrobuilder.png)



## Raspberry Pi

- Follow the workflow diagram in the previous section when connecting peripherals.
- Plug in the USB-C 5v power supply and wait for the device to boot up.

### Current Prototype

- The Raspberry Pi automatically starts the file *aptiv-server.py* in the *02-RaspberryPi* folder. The current prototype uses a static to make it easier to test in various locations.
- After waiting about a minute, go to the React-Native application and select a process to test. 

### Starting from scratch

- Open a new terminal window.

- Ping for the Raspberry Pi using *ping* to find the IP address of the board.

  ```bash
  ping raspberrypi.local
  ```

- SSH into the operating system using the IP address.

  ```bash
  ssh pi@x.x.x.x
  ```

- When prompted, supply the password for the operating system. If it is a fresh install, the password will be *raspberry*. 

- Install the *[aptiv-install.sh](https://gist.github.com/cskonopka/89bd1a6c414429852057e783e8bf46ae)* script. It is a bash script for installing updating the pi and installing git, python3 and flask. The process may take a while. This is the perfect time to grab a coffee and read a wiki article.

  ```bash
  sh aptiv-install.sh
  ```

- Clone the repository.

  ```bash
  git clone https://github.com/cskonopka/aptiv-taxi-tools.git
  ```

- Change the directory to *02-RaspberryPi*.

- Start the server. The Raspberry Pi can now receive HTTP POST requests from the React Native application.

  ```bash
  python3 aptiv-server.py
  ```
