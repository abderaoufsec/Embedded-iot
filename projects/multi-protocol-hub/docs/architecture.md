# Architecture Documentation

## System Architecture

```
PC (UART)
    ↓
ESP32
    ├─→ I2C Sensor
    ├─→ SPI Device (if available)
    └─→ UART Debug Output
```

## Components

- **UART:** Communication with PC for debugging and data output
- **I2C:** Sensor reading (e.g., OLED, temperature sensor)
- **SPI:** Device communication (e.g., SD card module)
- **Abstraction Layer:** Unified interface for different protocols
- **Error Handling:** Graceful failure recovery
- **Configuration:** Manageable settings

## Flow

1. Initialize all communication interfaces
2. Read I2C sensor
3. Communicate with SPI device (if available)
4. Send data via UART
5. Handle errors gracefully
6. Repeat

## Notes

Architecture and data flow documentation to be expanded during implementation.
