const int BUZZER_PIN = 8;
const int POT_PIN = A0;

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  int potValue = analogRead(POT_PIN); 
  
  // Map 0-1023 range to 100Hz - 2000Hz frequency range
  int frequency = map(potValue, 0, 1023, 100, 2000); 
  
  tone(BUZZER_PIN, frequency); // Generates square wave frequency
  delay(10);                   // Small stability delay
}