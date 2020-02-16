Import serial
Ser = serial.Serial(‘/dev/ttyACM0’,9600,timeout =1)
Ser.wirte(‘a’);   #给arduno输入 a，告诉它准备好了
try:
 while 1:
  response=ser.readall() #读取所有ardunio的数据
  print response
Except KeyBoardInterrupt:
 ser.close()