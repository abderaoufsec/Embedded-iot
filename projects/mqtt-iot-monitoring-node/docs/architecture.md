# Architecture Documentation

## System Architecture

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

- **Sensor:** Data acquisition (temperature, voltage, etc.)
- **ESP32:** Processing and MQTT communication
- **Wi-Fi:** Network connectivity
- **MQTT Broker:** Message routing
- **Monitoring Dashboard:** Visualization
- **Database:** Data storage

## Flow

1. ESP32 connects to Wi-Fi
2. ESP32 connects to MQTT broker
3. ESP32 reads sensor data
4. ESP32 formats data as JSON
5. ESP32 publishes telemetry to MQTT topic
6. ESP32 publishes status (retained)
7. ESP32 subscribes to command topic
8. Dashboard/Database receives telemetry
9. Dashboard sends commands
10. ESP32 receives commands and controls actuator

## Topic Design

To be documented during implementation.

## Payload Format

To be documented during implementation.

## Notes

Architecture and data flow documentation to be expanded during implementation.
