import RPi.GPIO as GPIO
import time
            
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)     # Pin usage GPIO Pin 18
GPIO.setup(17,GPIO.OUT)     # Pin usage GPIO Pin 17
GPIO.setup(27,GPIO.OUT)     # Pin usage GPIO Pin 27

while True:                 # Loop for ever
    
 print('START')             # Say in Terminal
 GPIO.output(18,GPIO.HIGH)  # Set GPIO Pin "High"
 print('LED RED ON')        # Say in Terminal
 print('WAIT 5s')           # Say in Terminal
 time.sleep(5)              # Waiting 
 print('DONE WAITING')      # Say in Terminal

 GPIO.output(17,GPIO.HIGH)
 print('LED YELLOW ON')
 print('WAIT 1s')
 time.sleep(1)
 print('DONE WAITING')

 GPIO.output(17,GPIO.LOW)
 print('LED YELLOW OFF')
 GPIO.output(18,GPIO.LOW)
 print('LED RED OFF')

 GPIO.output(27,GPIO.HIGH)
 print('LED GREEN ON')
 print('WAIT 5s')
 time.sleep(5)
 print('DONE WAITING')

 GPIO.output(27,GPIO.LOW)
 print('LED GREEN OFF')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(27,GPIO.HIGH)
 print('LED GREEN ON')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(27,GPIO.LOW)
 print('LED GREEN OFF')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(27,GPIO.HIGH)
 print('LED GREEN ON')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(27,GPIO.LOW)
 print('LED GREEN OFF')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(27,GPIO.HIGH)
 print('LED GREEN ON')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(27,GPIO.LOW)
 print('LED GREEN OFF')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(27,GPIO.HIGH)
 print('LED GREEN ON')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(27,GPIO.LOW)
 print('LED GREEN OFF')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(17,GPIO.HIGH)
 print('LED YELLOW ON')
 print('WAIT 1s')
 time.sleep(1)

 GPIO.output(17,GPIO.LOW)
 print('LED YELLOW OFF')
 print('WAIT 1s')
 print('END')

 GPIO.output(17,GPIO.LOW)
 GPIO.output(18,GPIO.LOW)
 GPIO.output(27,GPIO.LOW)

