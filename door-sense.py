import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt # Uses the paho Client which needs to be installed through pip

# Uses grounds to verify if there is an open or close circuit

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
gPin = 24 #Green LED Pin
rPin = 23 #Red LED Pin
bPin = 18 #Blue LED PIN
fiPin = 17 # Front Door Input
biPin = 27 # Back Door Input
siPin = 22 # Shed Door Input
broker = “HASSIO IP ADDRESS”
user = “USER”
passwd = “PASSWORD”
frPublish = “pi/doors/front”
bkPublish = “pi/doors/back”
sdPublish = “pi/doors/shed”
openPayload = “1”
closePayload = “0”

GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.setup(fiPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(biPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(siPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

haClient = mqtt.Client()
haClient.username_pw_set(user, passwd)

haClient.connect(broker, 1883)
haClient.loop_start()

try:
    frcheck =0
    bkcheck =0
    sdcheck =0
    while 1:
        #Front Door Input:
        if GPIO.input(fiPin):
            GPIO.output(gPin, GPIO.HIGH) # Green Led On
        if frcheck != 1:
            haClient.publish(frPublish, openPayload)
            frcheck = 1
        else:
            GPIO.output(gPin, GPIO.LOW) # Green Led Off
        if frcheck !=2:
            haClient.publish(frPublish, closePayload)
            frcheck = 2
    
        #Back Door Input:
        if GPIO.input(biPin):
            GPIO.output(rPin, GPIO.HIGH) # Red Led On
        if bkcheck !=1:
            haClient.publish(bkPublish, openPayload)
            bkcheck = 1
        else:
            GPIO.output(rPin, GPIO.LOW) # Red Led Off
        if bkcheck !=2:
            haClient.publish(bkPublish, closePayload)
            bkcheck = 2
        #Shed Door Input:
        if GPIO.input(siPin):
            GPIO.output(bPin, GPIO.HIGH) # Blue Led On
        if sdcheck !=1:
            haClient.publish(sdPublish, openPayload)
            sdcheck = 1
        else:
            GPIO.output(bPin, GPIO.LOW) # Blue Led Off
        if sdcheck !=2:
            haClient.publish(sdPublish, closePayload)
            sdcheck = 2


GPIO.cleanup() # cleanup all GPIO
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
