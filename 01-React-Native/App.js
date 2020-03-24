import React, { Component } from 'react';
import { Button, View, Image, TextInput } from 'react-native';

export default class Aptiv extends Component {
  // Defining state for TextInput
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
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        choice: key,
      }),
    })
      .then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson.msg);
      })
      .catch((error) => {
        alert("something went wrong :/");
      });
  }

  // HTTP POST to Raspberry Pi --> Control LED
  _onPressLED() {
    fetch('http://10.0.0.197:5000/led', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      }
    })
      .then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson.msg);
      })
      .catch((error) => {
        alert("something went wrong :/");
      });
  }

  // HTTP POST to Raspberry Pi --> Passcode submission
  _onPressPasscode = () => {
    const { TextInputValue } = this.state;
    fetch('http://10.0.0.197:5000/passcode', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        answer: TextInputValue
      })
    })
    .then((response) => response.json())
    .then((responseJson) => {
      alert(responseJson.msg);
    })
    .catch((error) => {
      alert("something went wrong :/");
    });
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
            title="Low"
            onPress={() => this._onPressServo('Low')}
          />
          <Button
            title="Medium"
            onPress={() => this._onPressServo('Medium')}
          />
          <Button
            title="High"
            onPress={() => this._onPressServo('High')}
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
  }
}