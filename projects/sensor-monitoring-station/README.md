# Sensor Monitoring and Threshold-Alert Station

**Objective:** Create a sensor monitoring station that reads multiple sensors, implements filtering and thresholds, and provides alerts.

## Requirements

- Read temperature from DS18B20
- Read acceleration from ADXL345 (optional)
- Read potentiometer (analog input)
- Implement moving average filter for at least one sensor
- Implement threshold logic with hysteresis for at least one sensor
- Provide alert via LED or buzzer
- Display sensor data via serial output
- Optionally: Display data on OLED (if available)

## Architecture

```
Sensors (DS18B20, ADXL345, Potentiometer)
    ↓
ESP32 Processing
    ↓
    ├─→ Filtering
    ├─→ Threshold Logic with Hysteresis
    └─→ Alert (LED/Buzzer)
    ↓
Serial Output (for monitoring)
```

## Components

- ESP32 development board
- DS18B20 temperature sensor
- ADXL345 accelerometer (optional)
- Potentiometer (10kΩ)
- LED and resistor (220Ω or 330Ω)
- Buzzer (optional)
- Resistors (4.7kΩ for DS18B20, 1kΩ for transistor if needed)
- Breadboard and jumper wires

## Status

**This is a project placeholder.** Complete implementation will be done during the course.

## Documentation

See `docs/` for detailed documentation.
