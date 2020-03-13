import subprocess

door_state = subprocess.Popen(["python", "/home/pi/sdp-master/door.py"])
bottom_gripper_in = subprocess.Popen(["python", "/home/pi/sdp-master/bottom_grippers_in.py"])

