# MQTT IoT Monitoring Node

**Objective:** Create a complete IoT monitoring node that publishes telemetry, receives commands, and integrates into an IoT system.

## Requirements

- Wi-Fi connection with reconnection logic
- MQTT connection with reconnection logic
- Sensor telemetry publishing (JSON payload)
- Device status publishing (retained)
- Command subscription for actuator control
- Error handling and fault tolerance
- Documentation

## Architecture

```
Sensor
    ↓
ESP32
    ↓
Wi-Fi
    ↓
MQTT Broker
    ↓
    ↓                    ↓
Monitoring Dashboard   Database
```

## Components

- ESP32 development board
- Sensor (temperature sensor DS18B20 or potentiometer)
- LED and resistor (220Ω or 330Ω)
- Mosquitto MQTT broker
- MQTT client tool (MQTTX or mosquitto_sub)

## Status

**This is a project placeholder.** Complete implementation will be done during the course.

## Documentation

See `docs/` for detailed documentation.
