# I2C Cheat Sheet

Quick reference for I2C communication protocol.

## Basic I2C

### Connections
```
ESP32 SDA ───────── Sensor SDA
ESP32 SCL ───────── Sensor SCL
ESP32 GND ───────── Sensor GND
ESP32 3V3 ───────── Sensor VCC
```

### Key Concepts
- **SDA**: Serial Data (bidirectional)
- **SCL**: Serial Clock (master controls)
- **Address**: Each device has unique address
- **Pull-ups**: Required on SDA and SCL
- **Speed**: Standard (100kHz), Fast (400kHz)

## Common Operations

### Scan for Devices
```c
#include <Wire.h>
Wire.begin();
for (byte addr = 1; addr < 127; addr++) {
    Wire.beginTransmission(addr);
    if (Wire.endTransmission() == 0) {
        // Device found at addr
    }
}
```

### Read from Device
```c
Wire.beginTransmission(device_addr);
Wire.write(register_addr);
Wire.endTransmission();
Wire.requestFrom(device_addr, num_bytes);
while (Wire.available()) {
    byte data = Wire.read();
}
```

### Write to Device
```c
Wire.beginTransmission(device_addr);
Wire.write(register_addr);
Wire.write(data);
Wire.endTransmission();
```

## Common Addresses

| Device | Typical Address |
|--------|----------------|
| OLED SSD1306 | 0x3C or 0x3D |
| MPU6050 | 0x68 |
| BMP280 | 0x76 or 0x77 |
| DS3231 RTC | 0x68 |

## Troubleshooting

### No Devices Found
- Check wiring (SDA, SCL, GND)
- Verify pull-up resistors
- Check I2C speed
- Ensure device is powered

### Data Corruption
- Check for electrical noise
- Verify pull-up resistor values
- Reduce I2C speed
- Check cable length

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 8 - Embedded Communication.*
