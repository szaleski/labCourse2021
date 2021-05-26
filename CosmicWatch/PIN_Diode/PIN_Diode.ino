int sigPin = 2;

int sigCount = 0;
int sigFlag=0;        //flag to listen for signal counts from the PIN circuit
unsigned long currentTime=0;
int prevTime=0;
int seconds=0;


void setup() {
    Serial.begin(9600);

    pinMode(sigPin, INPUT);
    digitalWrite(sigPin, HIGH);

    Serial.println("PIN counter:");
    Serial.println("counts timestamp");
}

void loop() {
    int sig = digitalRead(sigPin);

    if(sig == 0 && sigFlag == 0){
        sigFlag = 1;
        currentTime = millis()/1000.0;        
        sigCount++;

        Serial.print(sigCount); Serial.print(" "); Serial.println(currentTime, 4);
        }
    else if (sig == 1 && sigFlag == 1) {
        sigFlag = 0;
    }

 
    }
