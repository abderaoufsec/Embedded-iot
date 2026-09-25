# SPI Cheat Sheet

Quick reference for SPI communication protocol.

## Basic SPI

### Connections
```
ESP32 SCK  ─── SCK  Sensor
ESP32 MOSI ─── MOSI Sensor
ESP32 MISO ─── MISO Sensor
ESP32 CS   ─── CS   Sensor
GND        ─── GND
```

### Key Concepts
- **SCK**: Serial Clock (master generates)
- **MOSI**: Master Out Slave In (data from master)
- **MISO**: Master In Slave Out (data to master)
- **CS/SS**: Chip Select/Slave Select (device selection)
- **Full-duplex**: Simultaneous send and receive
- **No addressing**: CS selects which device

## Common Operations

### Basic Transfer
```c
digitalWrite(CS_PIN, LOW);    // Select device
byte data = SPI.transfer(0x00); // Send/receive
digitalWrite(CS_PIN, HIGH);   // Deselect device
```

### Read from Register
```c
digitalWrite(CS_PIN, LOW);
SPI.transfer(reg_addr);      // Send register address
byte value = SPI.transfer(0x00); // Read value
digitalWrite(CS_PIN, HIGH);
```

### Write to Register
```c
digitalWrite(CS_PIN, LOW);
SPI.transfer(reg_addr);      // Send register address
SPI.transfer(data);          // Send data
digitalWrite(CS_PIN, HIGH);
```

## SPI Modes

### Mode 0 (Most Common)
- CPOL = 0 (clock idle low)
- CPHA = 0 (sample on leading edge)

### Other Modes
- Mode 1: CPOL=0, CPHA=1
- Mode 2: CPOL=1, CPHA=0
- Mode 3: CPOL=1, CPHA=1

## Multiple Devices

### Sharing Bus
```
SCK  ────────────────────── All devices
MOSI ────────────────────── All devices
MISO ────────────────────── All devices
CS1  ────────────────────── Device 1
CS2  ────────────────────── Device 2
```

### Selection
- Only one CS low at a time
- Each device needs unique CS pin
- Devices can have different SPI modes

## Speed Considerations

### Clock Speed
- ESP32: Up to 80MHz
- Typical sensors: 1-10MHz
- Check device datasheet for maximum

### Trade-offs
- Higher speed = faster communication
- Higher speed = more noise issues
- Lower speed = more reliable

## Troubleshooting

### No Communication
- Check wiring (SCK, MOSI, MISO, CS, GND)
- Verify CS pin control
- Check SPI mode match
- Reduce clock speed

### Wrong Data
- Check SPI mode (CPOL, CPHA)
- Verify bit order (MSB/LSB first)
- Check clock speed
- Verify register addresses

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 8 - Embedded Communication.*
