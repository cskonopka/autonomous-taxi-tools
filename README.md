<p align="center">
  <img width="65%" height="65%" src="https://i.ibb.co/7twxPvD/aptiv.png"/>  
</p>

A suite of wireless HCI examples.

- pi + react + aptiv logo together






# Requirements

## Mobile
  - Android phone
  - USB-C cable
  - [React-Native](https://reactnative.dev/)
  - [Expo](https://expo.io/)
  
## Hardware
  - Raspberry Pi (in my case: 3B+)
  - LEDs (+ resistors)
  - Buzzer
  - Servo
  - Hookup wire
  - Breadboard
  - USB-C power supply

# React-Native
<p align="center">
  <img width="30%" height="30%" src="https://i.ibb.co/NxhPBXZ/aptiv-taxitools-reactnative.png"/>  
</p>

<<<<<<< HEAD

- Change the heat in the backseat
  - 
- Verify leaving the vehicle
- Rider verification passcode


=======
>>>>>>> 3829979d5c256293ff5f18fc0c391a5eefd16bc5
# Raspberry Pi + Python3 + Flask
<p align="center">
  <img width="85%" height="85%" src="https://i.ibb.co/qCFzDNx/aptiv-taxitools-rpi.png"/>  
</p>

# Workflow
<p align="center">
  <img width="85%" height="85%" src="https://i.ibb.co/ByWBZq5/Aptiv-taxitools-Workflow.png"/>  
</p>


# Task
Your task is to create an interaction that allows the user to provide an input (e.g.
numeric combination, swipe, button press...) on a mobile phone, which results in an
output from more than one external output device connected to an arduino or other
microcontroller. The external output can be in any mode (or a combination of modes)
such as audio, visual, etc.

Feel free to think about any combination of input on the phone, and outputs, as well as
using readily available resources that you have at home.

An example of a desired interaction:

<em>User inputs a 4-digit code on the phone. If the code is correct, an LED turns green and
a speaker plays a “correct” sound. If the code is incorrect, the LED turns red and a
speaker plays an “incorrect” sound.</em>

# Contraints
- [x] Input of interaction is on a mobile phone. Application can be in any form (e.g. native app or web app) 
- [x] Output is on an external output device (which can be as simple as an LED or buzzer) connected to a microcontroller.
- [x] connection between input application and microcontroller can be any wireless form. It does not have to have a server/cloud component.
- [x] Must contain your own code (your choice of language). Can contain third party libraries (please comment those where used).
