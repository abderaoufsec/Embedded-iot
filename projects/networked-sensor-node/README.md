# ESP32 Networked Sensor Node

**Objective:** Create an ESP32-based networked sensor node that transmits sensor data over TCP/UDP with error handling and reconnection logic.

## Requirements

- Read sensor (I2C or analog)
- Connect to Wi-Fi
- Implement TCP server for data access
- Implement UDP for data streaming (optional)
- Implement error handling
- Implement reconnection logic
- Display sensor data via serial
- Document configuration

## Architecture

```
Sensors
    ↓
ESP32
    ↓
Wi-Fi
    ↓
IP Network
    ↓
TCP/UDP
    ↓
PC/Server
    ↓
Data Display/Logging
```

## Components

- ESP32 development board
- Sensor (I2C or analog, e.g., DS18B20, potentiometer)
- Wi-Fi network
- PC or server for receiving data
- Breadboard and jumper wires

## Status

**This is a project placeholder.** Complete implementation will be done during the course.

## Documentation

See `docs/` for detailed documentation.
