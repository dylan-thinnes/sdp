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

void makeUp(int data);
void setup(void) {
// Setting the baundrate as 9600
// We'll send debugging information via the Serial monitor and communicate with the raspberry PI  
  Serial.begin(9600);   
}

void loop(void) {
  //Data start symbol with 'K'
  Serial.print("DATA");
  
  for (int pin = A0; pin <= A5; pin++) {
    Serial.print(' ');
    //read the first sensor value
    int val = analogRead(pin);
    //map the read value to [0,5000], as voltage(unit: mv)
    val = map(val, 0, 1023, 0, 5000);
    //send the value to raspberryPI
    makeUpAndSend(val);
  }
  
  //Data termination symbol with "/n"
  Serial.println(" END");                             
  delay(100);
}

//To make the raspberry PI read data easily,we complete the sensor value with '0' as four digits and then send it to raspberry PI
void makeUpAndSend(int data){
  if(data < 10) Serial.print(0);
  if(data < 100) Serial.print(0);
  if(data < 1000) Serial.print(0);
  Serial.print(data);
}
