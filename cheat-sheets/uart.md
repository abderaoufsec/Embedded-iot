# UART Cheat Sheet

Quick reference for UART communication protocol.

## Basic UART

### Connections
```
Device A TX ───────── RX Device B
Device A RX ───────── TX Device B
Device A GND ──────── GND Device B
```

### Key Concepts
- **TX**: Transmit (data out)
- **RX**: Receive (data in)
- **Baud Rate**: Speed (bits per second)
- **Data Bits**: Usually 8
- **Parity**: Error checking (usually none)
- **Stop Bits**: Usually 1
- **Cross-connection**: TX connects to RX

## Common Baud Rates

| Baud Rate | Use Case |
|-----------|----------|
| 9600 | Default, slow sensors |
| 115200 | Common for ESP32 debugging |
| 57600 | Some GPS modules |
| 38400 | Some Bluetooth modules |

## Common Operations

### ESP32 Arduino UART

### Setup
```c
Serial.begin(115200);        // USB serial
Serial1.begin(9600, SERIAL_8N1, RX_PIN, TX_PIN); // Hardware serial
```

### Send Data
```c
Serial.print("Hello");       // Send string
Serial.println("World");     // Send string + newline
Serial.write(0x41);          // Send byte
Serial.print(value, HEX);    // Send as hex
```

### Receive Data
```c
if (Serial.available()) {
    char c = Serial.read();  // Read one byte
    String s = Serial.readString(); // Read string
}
```

### Hardware Serial (ESP32)
```c
HardwareSerial Serial1(1);   // Use UART1
Serial1.begin(9600, SERIAL_8N1, RX_PIN, TX_PIN);
Serial1.println("Hello");
```

## Data Format

### Common Configuration
- **8N1**: 8 data bits, no parity, 1 stop bit
- **8E1**: 8 data bits, even parity, 1 stop bit
- **8O1**: 8 data bits, odd parity, 1 stop bit

### ASCII vs Binary
- ASCII: Human-readable (Serial.print)
- Binary: Raw bytes (Serial.write)

## Troubleshooting

### No Data Received
- Check TX/RX cross-connection
- Verify baud rate match
- Check ground connection
- Ensure both devices powered

### Garbage Data
- Baud rate mismatch
- Electrical noise
- Wrong data format
- Ground loops

### Partial Data
- Buffer overflow
- Timing issues
- Blocking operations

## Debugging with UART

### Serial Monitor
```c
void setup() {
    Serial.begin(115200);
    Serial.println("System starting...");
}

void loop() {
    Serial.print("Sensor: ");
    Serial.println(readSensor());
    delay(1000);
}
```

### Debug Messages
```c
Serial.println("DEBUG: Starting initialization");
Serial.print("DEBUG: Sensor value = ");
Serial.println(sensorValue);
Serial.println("ERROR: Sensor read failed");
```

## Best Practices

### For Debugging
- Use high baud rate (115200)
- Add clear debug messages
- Include timestamps if needed
- Use meaningful variable names

### For Communication
- Match baud rates exactly
- Use proper cross-connection
- Implement timeout handling
- Validate received data

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 8 - Embedded Communication.*
