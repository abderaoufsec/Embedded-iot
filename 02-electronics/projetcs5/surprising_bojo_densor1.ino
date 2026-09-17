const int LED_PIN = 3;
const int BUTTON_PIN = 4;
const int POT_PIN = A0;
const int BUZZER_PIN = 8;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT);
}

void loop() {
  int systemArmed = digitalRead(BUTTON_PIN);

  if (systemArmed == HIGH) {
    // Read speed setting from potentiometer
    int potValue = analogRead(POT_PIN);
    int flashSpeed = map(potValue, 0, 1023, 50, 500); // 50ms to 500ms delay

    // Alarm Triggered Phase
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER_PIN, 1000); // 1000Hz siren tone
    delay(flashSpeed);

    // Alarm Reset Phase
    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER_PIN);     // Turn off sound
    delay(flashSpeed);
  } else {
    // System Standby Phase
    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER_PIN);
  }
}