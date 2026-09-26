# Embedded Multi-Protocol Communication Hub

**Objective:** Create an ESP32-based system that demonstrates multiple communication interfaces with abstraction, configuration, and error handling.

## Requirements

- UART communication with PC
- I2C sensor reading
- SPI device communication (if available)
- Communication abstraction layer
- Configuration management
- Error handling
- Debugging output
- Documentation

## Architecture

```
PC (UART)
    ↓
ESP32
    ├─→ I2C Sensor
    ├─→ SPI Device (if available)
    └─→ UART Debug Output
```

## Components

- ESP32 development board
- I2C sensor (e.g., OLED, temperature sensor)
- SPI device (e.g., SD card module, if available)
- USB cable for UART
- Breadboard and jumper wires

## Status

**This is a project placeholder.** Complete implementation will be done during the course.

## Documentation

See `docs/` for detailed documentation.
