/*Program name: send sensor value to raspberry PI
 *1,Wiring instructions:  
 *  Arduino 5v(3v3) --> firstFSR one_of_the_leads
 *  Arduino A0      --> firstFSR another_leads
 *  Arduino 5v(3v3) --> sencondFSR one_of_the_leads
 *  Arduino A5      --> sencondFSR one_of_the_leads
 *  Arduino USB     --> raspberryPI USB
 * 2,Used libraries: none
 * 3,Program results:
 *  open the serial monitor, you will see KxxxxxxxxC is printing circularly(x represents a number)
 */
#define fsrPin  A0      // the FSR and 10K pulldown are connected to A0
#define secPin  A5      // the SEC and 10K pulldown are connected to A5
int fsrSensorVal = 9;   // the FSR analog Value
int secSensorVal = 9;   // the SEC analog Value
int mappedFsrSensorVal = 9;   // the mapped FSR analog Value
int mappedSecSensorVal = 9;   // the mapped SEC analog Value
int State = 0;

void makeUp(int data);
void setup(void) {
// Setting the baundrate as 9600
// We'll send debugging information via the Serial monitor and communicate with the raspberry PI  
  Serial.begin(9600);   
}

void loop(void) {
  if(State == 0){
    if(Serial.available()){
      if(Serial.read() == 'S'){      
         State = 1;
      }
    }
  }
  if(State == 1){
    //Data start symbol with 'K'
    Serial.print('K');
    
    //read the first sensor value
    fsrSensorVal = analogRead(fsrPin);
    //map the read value to [0,5000], as voltage(unit: mv)
    mappedFsrSensorVal = map(fsrSensorVal, 0, 1023, 0, 5000);
    //send the value to raspberryPI  
    makeUpAndSend(mappedFsrSensorVal);

    //read the second sensor value
    secSensorVal = analogRead(secPin);
    //map the read value to [0,5000], as voltage(unit: mv)
    mappedFsrSensorVal = map(secSensorVal, 0, 1023, 0, 5000);   
    //send the value to raspberryPI
    makeUpAndSend(mappedFsrSensorVal);
    
    //Data termination symbol with "/n"
    Serial.println('C');                               
    delay(400);     
  }
  delay(100);
}

//To make the raspberry PI read data easily,we complete the sensor value with '0' as four digits and then send it to raspberry PI
void makeUpAndSend(int data){
  if(data < 10){
    Serial.print(0);
    Serial.print(0);
    Serial.print(0); 
    Serial.print(data);     
  }
  else if(data < 100){
    Serial.print(0);
    Serial.print(0); 
    Serial.print(data);     
  }
  else if(data < 1000){
    Serial.print(0);
    Serial.print(data);     
  }
  else{ 
    Serial.print(data);     
  }
}
