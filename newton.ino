import serial
import time
from motors import Motors

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  


mc = Motors()
global upMotor
upMotor = 5

global spinMotor1
spinMotor1 = 1

global spinMotor2
spinMotor2 = 2

global spinMotor3
spinMotor3 = 3

global spinMotor4
spinMotor4 = 4

global speed
speed = 100

global littleSpeed
littleSpeed = -100

S = 'S'  # arduino start sign
# send  start sign to Arduino
for i in range(1, 4):
    ser.write(
        S.encode())  # why encode, refer to: https://blog.csdn.net/you23hai45/article/details/71516031?utm_source=itdadao&utm_medium=referral
    time.sleep(1)


def count_(voltage):
    if voltage == 0:
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


def runLittleBack(motorId, runTime):
    mc.move_motor(motorId, littleSpeed)
    time.sleep(1)
    mc.stop_motor(motorId)


global flag
flag = 1

global newFlag
newFlag = 1

global frs
frs = 1

global sec
sec = 1

# run main task
try:
    
    while True:
       
        hear = str(ser.readline().decode())  # right received hear look like KxxxxxxxxC,the character 'x' is numnber,
        # the use of ser.readline, refer to https://blog.csdn.net/huayucong/article/details/48729907
        if hear.startswith('K'):  # when the head of received data is 'K', reading the frs and sec value
          
            frs = int(hear[1:5])  # from the second to the forth is the content of frc value
            sec = int(hear[5:9])  # from the fifth to the eighth is the content of sec value
            print(count_(sec))  # print the sec value
        if frs < 200 and flag == 1:
            mc.move_motor(upMotor, 100)
        else:
            if flag == 1:
                runLittleBack(upMotor, 1)
                flag = 0
            else:
                if sec < 400 and newFlag == 1:
                    mc.move_motor(spinMotor1, speed)
                    mc.move_motor(spinMotor2, speed)
                else:
                    mc.stop_motors()
                    newFlag = 0

except KeyboardInterrupt:
    ser.close()
