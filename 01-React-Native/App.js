import React, { Component } from 'react';
import { Button, View, Image, Text, TextInput, Alert } from 'react-native';

export default class Aptiv extends Component {
  constructor(props) {
    super(props)
    this.state = {
      TextInputValue: ''
    }
  }

  // HTTP POST to Raspberry Pi --> Determine servo position: 'Low', 'Med', 'High'
  _onPressServo(key) {
    console.log(key)
    fetch('http://10.0.0.197:5000/servo', {
      // fetch('http://6250efad.ngrok.io/meow', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        language: key,
        framework: 'yourOtherValue',
      }),
    });
    alert('servo');
  }

  // HTTP POST to Raspberry Pi --> Control LED
  _onPressLED() {
    fetch('http://10.0.0.197:5000/led', {
      // fetch('http://6250efad.ngrok.io/led', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        firstParam: 'yourValue',
        secondParam: 'yourOtherValue',
      }),
    });
    alert('led');
  }

  // HTTP POST to Raspberry Pi --> Control LED
  _onPressBuzzer(key) {
    fetch('http://10.0.0.197:5000/buzzer', {
      // fetch('http://6250efad.ngrok.io/meow', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        language: key,
        framework: 'yourOtherValue',
      }),
    });
    alert('servo');
  }

  buttonClickListener = () => {
    const { TextInputValue } = this.state;
    // Alert.alert(TextInputValue);
    fetch('http://10.0.0.197:5000/passcode', {
      // fetch('http://6250efad.ngrok.io/meow', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        language: TextInputValue,
        framework: 'yourOtherValue',
      }),
    });
    alert('passcode');
  }

  render() {
    return (
      <View style={styles.container}>
        <Image style={styles.image}
          resizeMode="contain"
          resizeMethod="resize"
          source={{ uri: 'https://i.ibb.co/nsqfBcb/aptiv.png' }}>
        </Image>
        <View style={styles.servoContainer} >
          <Button
            // style={{ flex: 1 }}
            title="Low"
            onPress={() => this._onPressServo('0')}
          />
          <Button
            // style={{ flex: 1 }}
            title="Med"
            onPress={() => this._onPressServo('1')}
          />
          <Button
            // style={{ flex: 1 }}
            title="High"
            onPress={() => this._onPressServo('2')}
          />
        </View>
        <View style={styles.ledContainer} >
          <Button
            onPress={this._onPressLED}
            title="LED"
          />
        </View>
        <View style={styles.passcodeContainer} >
          <TextInput
            style={{ height: 45, borderColor: "gray", borderWidth: 2 }}
            placeholder="  Enter the passcode"
            //set the value in state.
            onChangeText={TextInputValue => this.setState({ TextInputValue })}
            // Making the Under line Transparent.
            underlineColorAndroid="transparent"
          />
          <Button
            onPress={this.buttonClickListener}
            title="Submit passcode"
          />
        </View>
        {/* <View style={styles.buzzerContainer} >
          <Button
            // style={{ flex: 1 }}
            title="Low"
            onPress={() => this._onPressBuzzer('0')}
          />
          <Button
            // style={{ flex: 1 }}
            title="Med"
            onPress={() => this._onPressBuzzer('1')}
          />
        </View> */}
        <View style={{ flex: 1, backgroundColor: '#FFFFFF' }} />
        <View style={{ flex: 1, backgroundColor: '#FFFFFF' }} />


      </View>
    );
  }
}

const styles = {
  container: {
    marginTop: 48,
    justifyContent: 'center',
    alignContent: 'center',
    flex: 1,
    backgroundColor: '#FFFFFF',
    marginLeft: 24,
    marginRight: 24,
    marginBottom: 24
  },
  image: {
    height: 100,
    width: 300,
    backgroundColor: '#FFFFFF',
    resizeMode: 'contain',
    alignContent: 'center',
    justifyContent: 'center'
  },
  servoContainer: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
  ledContainer: {
    flex: 1,
    backgroundColor: '#FFFFFF'
  },
  passcodeContainer: {
    flex: 5,
    backgroundColor: '#FFFFFF'
  },
  buzzerContainer: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
  elementsContainer: {
    backgroundColor: '#FFFFFF',
    marginLeft: 24,
    marginRight: 24,
    marginBottom: 24
  },
  headerText: {
    fontSize: 20,
    textAlign: "center",
    margin: 10,
    fontWeight: "bold"
  }
}