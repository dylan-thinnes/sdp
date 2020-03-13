import time
from motors import Motors

mc = Motors()

while True:
	with open('door_state', 'r') as doorState:
		state = doorState.read().rstrip()
		if state == 'unknown' or 'open':
			mc.stop_motors()
			# kill motors
	time.sleep(0.1)
