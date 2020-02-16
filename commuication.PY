Import serial
Ser = serial.Serial(‘/dev/ttyACM0’,9600,timeout =1)
Ser.wirte(‘a’);  
try:
 while 1:
  response=ser.readall() 
  print response
Except KeyBoardInterrupt:
 ser.close()
