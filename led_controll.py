import threading
import RPi.GPIO as GPIO
import time

blue_switch, red_switch, green_switch = 8, 10, 12



def b_but_callback(channel):
	if GPIO.input(b_but_port):
		GPIO.output(blue_switch, True)
	else:
		GPIO.output(blue_switch, False)

def r_but_callback(channel):
	if GPIO.input(r_but_port):
		GPIO.output(red_switch, True)
	else:
    GPIO.output(red_switch, False)

def g_but_callback(channel):
	if GPIO.input(g_but_port):
		GPIO.output(green_switch, True)
	else:
		GPIO.output(green_switch, False)

# setup the ports
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# ports
GPIO.setup(blue_switch, GPIO.OUT)
GPIO.setup(red_switch, GPIO.OUT)
GPIO.setup(green_switch, GPIO.OUT)

#GPIO.setup(b_but_port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(r_but_port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(g_but_port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#GPIO.add_event_detect(b_but_port, GPIO.BOTH, callback=b_but_callback)
#GPIO.add_event_detect(r_but_port, GPIO.BOTH, callback=r_but_callback)
#GPIO.add_event_detect(g_but_port, GPIO.BOTH, callback=g_but_callback)


try:
	while True:
		with open('system_state_files/colour', 'r') as colourFile:
			colour = colourFile.read().rstrip()
			if colour == 'red':
				GPIO.output(blue_switch, False)
				GPIO.output(red_switch, True)
				GPIO.output(green_switch, False)
			if colour == 'blue':
        			GPIO.output(blue_switch, True)
        			GPIO.output(red_switch, False)
        			GPIO.output(green_switch, False)
			if colour == 'green':
        			GPIO.output(blue_switch, False)
       				GPIO.output(red_switch, False)
        			GPIO.output(green_switch, True)

		time.sleep(0.1)
except Exception, e:
  print(str(e))	
finally:
	GPIO.cleanup()
