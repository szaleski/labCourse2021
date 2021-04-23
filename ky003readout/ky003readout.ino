/****************************************
**
** Author: Sebastian Kock
**
** Date: Apr. 12 2021
**
** Readout Code for KY-003 Hall Sensor:
*  Wiring: sensor -> arduino
*         Signal -> PIN 12
*         +V -> 5V
*         GND -> GND
*/

int hallpin = 12;
int value;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  value = digitalRead(hallpin);
  Serial.println(value);
}
  
