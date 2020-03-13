import RPi.GPIO as GPIO
import time

door_state = "unknown"

# define ports used for receiving data
port = 23

def write_state():
	with open("system_state_files/door_state", "w") as  file:
		global door_state
		file.write(door_state)


def writer(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		write_state()
	return wrapper

@writer
def button_callback(channel):
	global door_state
	if GPIO.input(port):
		door_state = "closed"
	else:
		door_state = "open"


# setup the ports
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# setup callbacks for rising falling -- door opening closing events
GPIO.add_event_detect(port, GPIO.BOTH, callback=button_callback)

try:
	while True:
		time.sleep(0.1)
finally:
	GPIO.cleanup()
