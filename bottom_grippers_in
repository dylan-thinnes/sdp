import time
from motors import Motors
from repl import run_to_thresh

mc = Motors()
speed = 100
m1 = 1
m2 = 2

def read_bottom_gripper_pos():
	state = "unknown"
	with open('system_state_files/bottom_gripper_pos', 'r') as pos:
		state = pos.read().rstrip()
	return state

def read_door_state():
        state = "unknown"
        with open('system_state_files/door_state', 'r') as pos:
                state = pos.read().rstrip()
        return state

while True:
	gripper_pos = read_bottom_gripper_pos()
	door_state = read_door_state()
	if gripper_pos == 'in':
		break
	if door_state == 'closed' and gripper_pos == 'out':
		#run_to_thresh([m1, m2])
		mc.move_motor(m1, speed)
		mc.move_motor(m2, speed)
		with open('system_state_files/bottom_gripper_pos', 'w') as pos:
			pos.write('in')
		# run a script that will move the motors in until
		# a threshold
