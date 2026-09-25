void setup() {
  pinMode(2, OUTPUT); // Configure Pin 2 to send voltage out
}

void loop() {
  digitalWrite(2, HIGH); // Send 5V to Pin 2 (LED ON)
  delay(500);            // Wait 500ms
  digitalWrite(2, LOW);  // Send 0V to Pin 2 (LED OFF)
  delay(500);            // Wait 500ms
}