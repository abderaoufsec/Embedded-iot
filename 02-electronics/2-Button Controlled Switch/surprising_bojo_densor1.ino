const int LED_PIN = 2;
const int BUTTON_PIN = 3;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT); // Pin 3 listens for input
}

void loop() {
  int buttonState = digitalRead(BUTTON_PIN); // Returns HIGH or LOW
  
  if (buttonState == HIGH) {
    digitalWrite(LED_PIN, HIGH); // Turn LED on while pressed
  } else {
    digitalWrite(LED_PIN, LOW);  // Turn LED off when released
  }
}