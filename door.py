import RPi.GPIO as GPIO

door_state = "unknown"

# define ports used for receiving data
up_port = 23
down_port = 21

def write_state():
        with open("door_state", "w") as  file:
                global door_state
                file.write(door_state)


def writer(func):
        def wrapper(*args, **kwargs):
                func(*args, **kwargs)
                write_state()
        return wrapper
        @writer
def button_down_callback(channel):
        global door_state
        door_state = "closed"

@writer
def button_up_callback(channel):
        global door_state
        door_state = "open"
# setup the ports
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(up_port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down_port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# setup callbacks for rising falling -- door opening closing events
GPIO.add_event_detect(up_port, GPIO.FALLING, callback=button_up_callback)
GPIO.add_event_detect(down_port, GPIO.RISING, callback=button_down_callback)
input("press enter to quit")
GPIO.cleanup()
