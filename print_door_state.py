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
pi@Seadramon:~/sdp-master $ cat print_door_state.py
from time import sleep

while True:
	with open("system_state_files/door_state", "r") as file:
		res = file.read()
		print(res)		
	
	sleep(0.1)
