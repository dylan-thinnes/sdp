int fsrPin = 0; 
int secPin=5;   // the FSR and 10K pulldown are connected to a0
int fsrReading;
int secReading; // the analog reading from the FSR resistor divider
int fsrVoltage;
int secVoltage;  // the analog reading converted to voltage
unsigned long fsrResistance;
unsigned long secResistance;// The voltage converted to resistance, can be very big so make "long"
unsigned long fsrConductance; 
unsigned long secConductance; 
long fsrForce;
long secForce;// Finally, the resistance converted to force
 
void setup(void) {
  Serial.begin(9600);   // We'll send debugging information via the Serial monitor
}
 
void loop(void) {
   if(Serial.available()){
    if('a'==Serial.read())
    
  fsrReading = analogRead(fsrPin);  
 
  // analog voltage reading ranges from about 0 to 1023 which maps to 0V to 5V (= 5000mV)
  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
 
  if (fsrVoltage == 0) {
  } else {
    // The voltage = Vcc * R / (R + FSR) where R = 10K and Vcc = 5V
    // so FSR = ((Vcc - V) * R) / V        yay math!
    fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
    fsrResistance *= 10000;                // 10K resistor
    fsrResistance /= fsrVoltage;
 
    fsrConductance = 1000000;           // we measure in micromhos so 
    fsrConductance /= fsrResistance;
 
    // Use the two FSR guide graphs to approximate the force
    if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
      
      Serial.println(fsrForce);      
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30;
   
      Serial.println(fsrForce);            
    }
  }
   secReading = analogRead(secPin);  
 
  // analog voltage reading ranges from about 0 to 1023 which maps to 0V to 5V (= 5000mV)
  secVoltage = map(secReading, 0, 1023, 0, 5000);
 
  if (secVoltage == 0) {
  } else {
    // The voltage = Vcc * R / (R + FSR) where R = 10K and Vcc = 5V
    // so FSR = ((Vcc - V) * R) / V        yay math!
    secResistance = 5000 - secVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
    secResistance *= 10000;                // 10K resistor
    secResistance /= secVoltage;
 
    secConductance = 1000000;           // we measure in micromhos so 
    secConductance /= secResistance;
 
    // Use the two FSR guide graphs to approximate the force
    if (secConductance <= 1000) {
      secForce = secConductance / 80;
      
      Serial.println(secForce);      
    } else {
      secForce = secConductance - 1000;
      secForce /= 30;
   
      Serial.println(secForce);            
    }
  }
  
  
  

  
  
  
  Serial.println("--------------------");}
 
  delay(1000);
}
