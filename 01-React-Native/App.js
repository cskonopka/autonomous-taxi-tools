import React, { Component } from 'react';
import { Button, Switch, StyleSheet, View, Image } from 'react-native';

export default class Aptiv extends Component {
  // HTTP POST to Raspberry Pi --> Servo
  _onPressServo() {
    // fetch('http://10.0.0.197:5000/meow', {
    fetch('http://6250efad.ngrok.io/meow', {
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
    alert('servo')
  }

  // HTTP POST to Raspberry Pi --> LED
  _onPressLED() {
    // fetch('http://10.0.0.197:5000/led', {
    fetch('http://6250efad.ngrok.io/led', {
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
    alert('led')
  }

  render() {
    return (
      <View style={styles.container}>
        <Image style={styles.image}
          source={{ uri: 'https://i.ibb.co/7twxPvD/aptiv.png' }}>
        </Image>
        <View style={styles.buttonContainer}>
          <Button
            onPress={this._onPressServo}
            title="Servo"
          />
        </View>
        <View style={styles.buttonContainer}>
          <Button
            onPress={this._onPressLED}
            title="LED"
          />
        </View>
        <Switch></Switch>
      </View >
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    flexDirection: 'column',
  },
  buttonContainer: {
    flex: 1,
    flexDirection: "column",
    margin: 13,
    paddingBottom: 1
  },
  alternativeLayoutButtonContainer: {
    margin: 20,
    flexDirection: 'row',
    justifyContent: 'space-between'
  },
  image: {
    flexGrow: 1,
    margin: 74,
    resizeMode: "center",
    borderTopWidth: 1,
    height: null,
    width: null,
    alignItems: 'center',
  }
});
