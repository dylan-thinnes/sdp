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
        hear = str(ser.readline().decode())
        if hear.startswith('K'):  # when the head of received data is 'K', read frs and sec
            fst = int(hear[1:5])  # from 2nd to 4th is first value
            snd = int(hear[5:9])  # from 5th to 8th is second value
            print("%i %i %f" % (fst, snd, time.time())
            sys.stdout.flush()
            sys.stderr.flush()

except KeyboardInterrupt:
    print("Can't read TTY.")
    ser.close()
