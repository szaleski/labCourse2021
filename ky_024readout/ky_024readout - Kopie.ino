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
int count = 0;

//conversion factor dependent on used voltege measurement
float conversion = 5.0 / 4096.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  count++;
  value = double(analogRead(hallpin));
  value = value * conversion;
  Serial.print(value, 7);  // in V
  Serial.print(" ");
  Serial.print(count);
  Serial.print(' ');
  Serial.println(1/value, 7);

  delay(500);
}
