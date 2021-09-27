# Door Sensors - For HASS / Home Assitant
## A simple door sensor python app to send data through mqtt

### How does it work?
- A Reed sensor that is either open/ closed based on state, sends a signal the raspberry PI reads
- The raspberry PI, then takes the signal running python with a few plugins, to send a MQTT message
- HassOS/ Home Assistant takes the message, changing states / waiting to notify after a time.

The original plan was to use home assitant to send a message to my phone that the backdoor / shed was open. But that was too expensive, buying the app and such (for now) or it meant ended up having to program an app that went through Googles services, and having them know everytime my backdoor was left open... seemed... questionable 


The setup is pretty straight forward the code is extremely basic, uses paho MQTT Client, to connect to the MQTT broker on Home Assistant. It has a delay and a simple switch so it doesn't spam Home Assistant that it is open / closed.

It will also turn on the LED's to say if the door is open or clsoed. One limitation if HassOS / Home Assistant restarts, The states / entities will be blank. Currently the MQTT isn't bi-directional -*Possible future fix later* Until the doors are open /closed again / the python script restarts.

But, this did worked perfectly for months without a need to restart anything, was very useful to make sure the front / back / shed doors were properly closed during the specifically during the winter months to stop wildlife / heatloss.



### The Raspberry PI Setup:
- Was built on a very old Raspbery Pi Model B, the pins are pretty easy to see which are which in the config
- Used a POE USB Spliter to power the Raspberry PI + Supply Ethernet Signal, so no power bricks were used / needed
- Required just 2 Wires to each REED Sensor (Simple NO / NC Sensors), mounted each sensor to the door frames

### How to use this Code:
- Install paho client using pip3, install python using the normal means with the Raspbian OS. 
- Install ground pins to GPIO Pins 17, 27, 22, optionally install LED Power to Pins to GPIO Pins 24, 23, 18
- Set the connection information for ip address, user, password.
- You can use the publish strings I used, pi/doors/front or you can set your own
- Start by typing python door-sensors.py (in the directory you installed)

Note, GPIO Pins can be different depending on how the board is laid out / configutation used. (IE the GPIO.setmode(GPIO.BCM))
