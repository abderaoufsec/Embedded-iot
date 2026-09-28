# Raspberry Pi Gateway - Circuit Wiring

This document describes the circuit wiring for the Raspberry Pi Gateway project.

## Components
- Raspberry Pi 3B+/4
- ESP32 development board
- LEDs and resistors
- USB-TTL adapter (for UART)

## Wiring Diagram
- ESP32 TX to Raspberry Pi RX (GPIO15)
- ESP32 RX to Raspberry Pi TX (GPIO14)
- Common ground
- LED with 220Ω resistor to GPIO (e.g., GPIO17)

## Notes
- Use voltage level conversion if needed (ESP32 is 3.3V, Raspberry Pi is 3.3V)
- Verify pin mappings for your specific Raspberry Pi model
