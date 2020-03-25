// Stock React-Native libraries
import React, { Component } from 'react';
import { Button, View, Image, TextInput, Text } from 'react-native';
const url = 'http://10.0.0.197:5000';

export default class Aptiv extends Component {
  
  // Defining state for TextInput
  constructor(props) {
    super(props)
    this.state = {
      TextInputValue: ''
    }
  }

  // Ambient Cooling selection --> HTTP POST to Rpi (ac) 
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

  // Dropoff --> HTTP POST to Rpi (dropoff)
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

  // Rider Passcode Verification --> HTTP POST to Rpi (/passcode)
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

  render() {
    return (
      // App container 
      <View style={styles.container}>
        {/* BLOCK --> Aptiv logo */}
        <Image style={styles.image}
          resizeMode="contain"
          resizeMethod="resize"
          source={{ uri: 'https://i.ibb.co/nsqfBcb/aptiv.png' }}>
        </Image>
        {/* BLOCK --> Ambient Cooling (ac) */}
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
        {/* BLOCK -->  Dropoff (dropoff)*/}
        <View style={styles.textContainer} >
          <Text style={{ fontSize: 24 }}>Arrived?</Text>
        </View>
        <View style={styles.dropoffContainer} >
          <Button
            onPress={this._onPressDropoff}
            title="Dropoff"
          />
        </View>
        {/* BLOCK -->  Rider Passcode Verification (passcode) */}
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
      </View>
    );
  }
}

// App styles
const styles = {
  container: {
    marginTop: 48,
    justifyContent: 'center',
    alignContent: 'center',
    flex: 1,
    backgroundColor: '#FFFFFF',
    marginLeft: 24,
    marginRight: 24,
    marginBottom: 0
  },
  image: {
    height: 100,
    width: 300,
    marginLeft: 3,
    backgroundColor: '#FFFFFF',
    resizeMode: 'contain',
    alignContent: 'center',
    justifyContent: 'center'
  },
  textContainer: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
  acContainer: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 0,
    marginBottom: 10,
  },
  dropoffContainer: {
    flex: 1,
    marginBottom: 10,
    backgroundColor: '#FFFFFF',
    marginBottom: 10
  },
  passcodeContainer: {
    marginBottom: 10,
    flex: 3,
    backgroundColor: '#FFFFFF',
  }
}