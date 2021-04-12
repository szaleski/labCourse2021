/****************************************
**
** Author: Sebastian Kock
**
** Date: Apr. 12 2021
**
** Readout Code for KY-024 Hall Sensor:
*  Wiring: sensor -> arduino
*         D0 -> A0
*         + -> 5V
*         G -> GND
*         A0 -> -
*/

int hallpin = A0;
int value;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  value = analogRead(hallpin);
  Serial.println(value);
}
