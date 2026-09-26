# ESP32 Environmental Telemetry Node

**Objective:** Create an ESP32-based environmental monitoring node that demonstrates core ESP32 capabilities.

## Requirements

- Read temperature sensor (I2C or analog)
- Read potentiometer (ADC)
- Control LED brightness (PWM)
- Monitor button (GPIO with debounce)
- Send data via UART (serial output)
- Connect to Wi-Fi
- Provide simple HTTP endpoint with sensor data
- Store configuration in NVS (ESP-IDF) or preferences (Arduino)

## Architecture

```
Sensors (I2C/ADC)
    ↓
ESP32 Processing
    ↓
Serial Output (UART)
    ↓
Wi-Fi
    ↓
HTTP Server
```

## Components

- ESP32 development board
- Temperature sensor (I2C or analog)
- Potentiometer (10kΩ)
- LED and resistor (220Ω or 330Ω)
- Push button
- Breadboard and jumper wires

## Status

**This is a project placeholder.** Complete implementation will be done during the course.

## Documentation

See `docs/` for detailed documentation.
