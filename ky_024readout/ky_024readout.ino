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
*         
* output in V (for comparability to other voltage measurement methods (e.g ADC1115)
*/

int hallpin = A0;
double value;

//conversion factor dependent on used voltege measurement
float conversion = 5.0 / 4096.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  value = double(analogRead(hallpin));
  value = value * conversion;
  Serial.println(value, 7);  // in V

  delay(100);
}
