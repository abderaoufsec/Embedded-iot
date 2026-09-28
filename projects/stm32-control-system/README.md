# STM32 Control System

> **Status:** Project specification
>
> **Implementation:** Complete implementation is performed by the learner during the course.
>
> **Prerequisite:** Phase 17 — STM32

---

## Project Overview

Build a complete STM32-based control system.

This project applies STM32 peripheral configuration, register-level programming, and professional debugging tools learned in Phase 17.

---

## Requirements

- GPIO control (LEDs, buttons)
- PWM output (motor control simulation)
- ADC input (sensor reading)
- UART communication
- I2C sensor reading
- Timer-based timing
- DMA for efficient transfers
- Watchdog for reliability
- Debugging with GDB

---

## Project Structure

```
stm32-control-system/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   ├── main.c
│   ├── gpio.c
│   ├── uart.c
│   ├── adc.c
│   ├── timers.c
│   └── dma.c
├── tests/
│   └── test_scenarios.md
├── docs/
│   ├── architecture.md
│   └── register_map.md
└── results/
    └── measurements.md
```

---

## Time Estimate

20-24 hours
