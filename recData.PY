
import serial
import time

ser = serial.Serial('/dev/ttyACM2', 9600, timeout=1)  
S = 'S'  # arduino start sign


def count_(voltage):
	if voltage == 0 :
		return voltage
	else:
	    Resistance = 5000 - voltage
	    Resistance *= 10000
	    Resistance /= voltage
	    Conductance = 1000000
	    Conductance /= Resistance
	    if Conductance <= 1000:
	        Force = Conductance / 80
	    else:
	        Force = Conductance - 1000
	        Force /= 30
	    return Force


# send  start sign to Arduino
for i in range(1, 4):
    ser.write(S.encode())  # why encode, refer to: https://blog.csdn.net/you23hai45/article/details/71516031?utm_source=itdadao&utm_medium=referral
    time.sleep(1)

# run main task
try:
    # print("OK,TRY")
    while True:
        # print("OK,while")                             # debug information
        hear = str(ser.readline().decode())  # right received hear look like KxxxxxxxxC,the character 'x' is numnber,
        # the use of ser.readline, refer to https://blog.csdn.net/huayucong/article/details/48729907
        if hear.startswith('K'):  # when the head of received data is 'K', reading the frs and sec value
            # print("OK,if")                            # debug information
            # print(hear.strip('\n'))                   # debug information ,print hear without \n in head and tail
            frs = int(hear[1:5])  # from the second to the forth is the content of frc value
            sec = int(hear[5:9])  # from the fifth to the eighth is the content of sec value
            print(count_(frs))  # print the frc value
            print(count_(sec))  # print the sec value

except KeyboardInterrupt:
    ser.close()
