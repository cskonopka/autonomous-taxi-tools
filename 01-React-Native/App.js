import React, { Component } from 'react';
import { Button, View, Image } from 'react-native';

export default class Aptiv extends Component {
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
    alert('servo')
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
    alert('led')
  }

  render() {
    return (
      <View style={styles.container}>
        <Image style={styles.image}
          resizeMode="contain"
          resizeMethod="resize"
          source={{ uri: 'https://i.ibb.co/7twxPvD/aptiv.png' }}>
        </Image>
          <View style={styles.servoContainer} >
            <Button style={{ flex: 1 }}
              title="Low"
              onPress={() => this._onPressServo('0')}
            />
            <Button
              style={{ flex: 1 }}
              title="Med"
              onPress={() => this._onPressServo('1')}
            />
            <Button
              style={{ flex: 1 }}
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
          <View style={{ flex: 1, backgroundColor: '#FFFFFF' }} />
          <View style={{ flex: 3, backgroundColor: '#FFFFFF' }} />
        </View>
    );
  }
}

const styles = {
  container: {
    marginTop: 48,
    justifyContent:'center',
    alignContent:'center',
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
    alignContent:'center', 
    justifyContent:'center'
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
  elementsContainer: {
    backgroundColor: '#FFFFFF',
    marginLeft: 24,
    marginRight: 24,
    marginBottom: 24
  }
}