from motors import Motors
from time import time, sleep
# Create an instance of the Motors class used in SDP
global mc
mc = Motors()

global toggle_dir
toggle_dir = -1

def move(motor, speed = 100):
    try:
        iterator = iter(motor)
        for m in motor:
            move(m, speed * toggle_dir)
    except TypeError as te:
        mc.move_motor(motor, speed)

def forward(motor, speed = 100):
    move(motor, speed)

def backward(motor, speed = 100):
    move(motor, -speed)

def stop():
    mc.stop_motors()

def stress(motor):
    for i in range(0, 10):
        forward(motor)
        sleep(6)
        backward(motor)
        sleep(6)
    stop()

def get_last_result(filename):
    try:
        with open(filename, 'r') as fh:
            s = fh.readline()
            sensors = [int(x) for x in s.split(' ')]
            left = sensors[0]
            right = sensors[1]
            return (left, right)
    except:
        return None

global default_maximum
default_maximum = 4000
global default_filename
default_filename = "sdp-master/tty_last_result"

def to_thresh(filename = default_filename, maximum = default_maximum):
    while True:
        x = get_last_result(filename)
        if x == None:
            continue
        else:
            left, right = x
            if (max(left, right) > maximum):
                break

def run_to_thresh(motors, filename = default_filename, maximum = default_maximum):
    forward(motors)
    to_thresh(filename, maximum)
    stop()
