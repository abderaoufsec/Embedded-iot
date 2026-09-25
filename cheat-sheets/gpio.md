# GPIO Cheat Sheet

Quick reference for GPIO (General Purpose Input/Output) operations.

## Basic GPIO Modes

### Input
```c
pinMode(pin, INPUT);           // High impedance
pinMode(pin, INPUT_PULLUP);    // Internal pull-up
pinMode(pin, INPUT_PULLDOWN);  // Internal pull-down
```

### Output
```c
pinMode(pin, OUTPUT);         // Push-pull output
```

## Reading and Writing

### Digital Read
```c
int value = digitalRead(pin);  // Returns HIGH or LOW
```

### Digital Write
```c
digitalWrite(pin, HIGH);   // Set pin high
digitalWrite(pin, LOW);    // Set pin low
```

## Common Patterns

### LED Control
```c
const int LED_PIN = 2;
pinMode(LED_PIN, OUTPUT);
digitalWrite(LED_PIN, HIGH);
```

### Button Reading
```c
const int BUTTON_PIN = 4;
pinMode(BUTTON_PIN, INPUT_PULLUP);
int pressed = (digitalRead(BUTTON_PIN) == LOW);
```

## ESP32 Specific

### GPIO Limitations
- Some pins have special functions at boot
- Check strapping pins before use
- Input-only pins exist on some variants
- Maximum current per pin: ~12mA
- Maximum total current: ~40mA

### ADC Pins
- ESP32 has multiple ADC channels
- ADC1: 8 channels, 12-bit
- ADC2: 10 channels, 12-bit (shares with Wi-Fi)

### PWM (LEDC)
- 16 channels
- Configurable frequency and resolution
- Hardware PWM generation

## Safety Notes

- Never exceed maximum current
- Use current limiting for LEDs
- Check voltage levels (3.3V logic)
- Avoid short circuits
- Use appropriate pull-up/down resistors

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 6 - ESP32.*
