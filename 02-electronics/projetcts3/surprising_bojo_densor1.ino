const int LED_PIN = 3; // Must be a PWM pin (~3)
const int POT_PIN = A0;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  // Analog pins are INPUT by default
}

void loop() {
  int rawValue = analogRead(POT_PIN); // Reads 0 to 1023 (10-bit ADC)
  int pwmValue = rawValue / 4;        // Scales 0-1023 down to 0-255 (8-bit PWM)
  
  analogWrite(LED_PIN, pwmValue);    // Simulates lower voltage using PWM
}