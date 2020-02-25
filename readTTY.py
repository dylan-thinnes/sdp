import serial
import time
import sys
import glob

ser = serial.Serial(glob.glob("/dev/ttyACM?")[0], 9600, timeout=1)  

# send start sign to Arduino
for i in range(1, 4):
    ser.write('S'.encode())
    time.sleep(1)

# run main task
try:
    while True:
        try:
            hear = str(ser.readline().decode())
        except UnicodeDecodeError:
            continue

        hear = hear.rstrip() # strip trailing whitespace
        # when the head of received data is 'DATA', read frs and sec
        if hear.startswith('DATA') and hear.endswith('END'):
            sensors = [int(x) for x in hear.split(' ')[1:-1]] # print sensors
            print ' '.join([str(x) for x in sensors])

        sys.stdout.flush()
        sys.stderr.flush()

except KeyboardInterrupt:
    print("Can't read TTY.")
    ser.close()
