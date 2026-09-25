# Embedded Systems & IoT Self-Study Curriculum

A complete, beginner-to-advanced curriculum for learning embedded systems and IoT development through practical, project-based learning.

## Who This Is For

This curriculum is designed for:

- **Complete beginners** with no embedded systems background
- **Students** wanting to build practical embedded/IoT skills
- **Hobbyists** moving from Arduino to professional embedded development
- **Engineers** transitioning into embedded/IoT fields
- **Anyone** who wants to understand embedded systems deeply, not just copy code

## Learning Philosophy

This curriculum follows a structured learning loop:

```
LEARN → EXERCISE → LAB → DEBUG → PROJECT → TEST → DOCUMENT → ADVANCE
```

**This is NOT a collection of articles.** You will build real systems, debug real problems, and develop genuine understanding.

### Key Principles

1. **Understanding Before Libraries** - Learn WHY something works before using APIs that hide it
2. **Progressive Complexity** - Start simple, build complexity gradually
3. **Practical Application** - Every concept is applied in labs and projects
4. **Debugging Skills** - Intentional debugging exercises develop problem-solving
5. **Assessment Gates** - Prove competence before advancing

## Curriculum Overview

The curriculum progresses from absolute fundamentals to advanced industrial IoT:

### Foundation Phases (0-5)
- **00-orientation** - Setup, safety, and how to use this curriculum
- **01-computer-fundamentals** - Binary, hex, memory, CPU basics
- **02-c-programming** - Embedded-focused C programming
- **03-digital-electronics** - Logic gates, Boolean algebra, digital circuits
- **04-electronics** - Circuits, components, measurement, safety
- **05-microcontrollers** - MCU architecture, registers, peripherals

### Core Embedded Development (6-10)
- **06-esp32** - ESP32 development (Arduino framework + ESP-IDF)
- **07-sensors-and-actuators** - Sensor integration, datasheets, calibration
- **08-embedded-communication** - UART, I2C, SPI, CAN protocols
- **09-networking** - TCP/IP, HTTP, embedded networking
- **10-mqtt-and-iot** - MQTT, IoT architecture, device communication

### Advanced Topics (11-18)
- **11-linux-for-embedded** - Linux for embedded gateways
- **12-raspberry-pi** - Raspberry Pi as IoT gateway
- **13-debugging** - Systematic debugging techniques
- **14-rtos-freertos** - Real-time operating systems
- **15-embedded-security** - Security fundamentals for embedded systems
- **16-cloud-and-edge** - Cloud integration and edge computing
- **17-stm32** - Professional STM32 development
- **18-industrial-iot** - Industrial protocols and architecture

## Hardware Requirements

### Required Starter Hardware
- ESP32 development board (any common variant)
- USB cable for programming
- Breadboard and jumper wires
- LEDs and resistors
- Buttons
- Potentiometer
- Basic sensors (temperature, light)
- Multimeter

### Optional Hardware
- OLED display
- Additional sensors (accelerometer, current sensor, etc.)
- Logic analyzer
- Raspberry Pi (for later phases)
- STM32 development board (for advanced phases)

See [HARDWARE.md](HARDWARE.md) for detailed hardware requirements by phase.

## Project Progression

### Beginner Projects
1. LED blinker
2. Button-controlled LED
3. Traffic light simulator
4. Potentiometer reader
5. PWM dimmer
6. Temperature reader
7. UART monitor
8. OLED display

### Intermediate Projects
9. Environmental monitor
10. Data logger
11. Wi-Fi sensor node
12. ESP32 HTTP server
13. OLED sensor station
14. Threshold alert system

### IoT Projects
15. MQTT sensor node
16. MQTT command node
17. Secure MQTT node
18. Raspberry Pi gateway
19. Dashboard integration
20. Multi-node IoT system

### Advanced Projects
21. FreeRTOS multi-task system
22. Secure OTA system
23. STM32 motor controller
24. Modbus/CAN system
25. Industrial edge gateway

### Capstone
A complete motor monitoring/predictive maintenance IoT system integrating sensors, signal processing, networking, MQTT, edge processing, and security.

See [projects/](projects/) for complete project implementations.

## How to Use This Curriculum

### Starting From Zero

1. Begin with **00-orientation** - Complete the setup checklist
2. Progress sequentially through phases 0-5
3. Complete ALL exercises, labs, and projects in each phase
4. Pass the knowledge and practical assessments
5. Use the completion checklist before advancing

### If You Have Some Experience

1. Take the assessments for early phases
2. Skip phases where you demonstrate competence
3. Focus on gaps in your knowledge
4. Don't skip the project work - it builds practical skills

### Study Methodology

For each phase:

1. **Read** the phase README completely
2. **Study** the listed resources in the exact order specified
3. **Complete** all exercises
4. **Build** all labs on real hardware
5. **Debug** the intentional debugging exercises
6. **Complete** the phase project
7. **Pass** the knowledge test
8. **Pass** the practical test
9. **Review** the completion checklist
10. **Advance** to the next phase

## Assessment

Every phase includes:

- **Knowledge Test** - Conceptual understanding
- **Practical Test** - Build-from-scratch verification
- **Completion Checklist** - Skill verification

**Do not advance until you pass all assessments.** This curriculum builds progressively - gaps will cause problems later.

## Resources

- [ROADMAP.md](ROADMAP.md) - Complete learning path visualization
- [HARDWARE.md](HARDWARE.md) - Detailed hardware requirements
- [RESOURCE_INDEX.md](RESOURCE_INDEX.md) - Centralized resource directory
- [cheat-sheets/](cheat-sheets/) - Quick reference materials
- [labs/](labs/) - Cross-phase lab repository
- [resources/](resources/) - Datasheets, diagrams, and reference materials

## Platform Strategy

This curriculum uses:

- **ESP32** as the main beginner/intermediate platform
- **Arduino framework** for gentle introduction
- **ESP-IDF** for professional development
- **STM32** for advanced professional development
- **Raspberry Pi** for gateway/edge computing

You will learn both easy APIs AND what they hide.

## Prerequisites

### Before Starting
- Basic computer literacy
- Ability to follow technical instructions
- Willingness to debug and solve problems
- Patience with hardware and software

### No Prior Knowledge Required
- No programming experience needed
- No electronics experience needed
- No embedded systems knowledge needed
- No networking knowledge needed

Everything is taught from first principles.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

See [LICENSE](LICENSE) for license information.

## Safety

**Electrical safety is critical.** Each phase includes safety guidelines relevant to its content. Always:

- Never work on live circuits unless specifically instructed
- Double-check wiring before applying power
- Use appropriate current limiting for LEDs and other components
- Never exceed component voltage/current ratings
- Keep flammable materials away from circuits
- Have a fire extinguisher nearby when working with power

## Getting Started

1. Clone this repository
2. Read [00-orientation/README.md](00-orientation/README.md)
3. Complete the orientation setup checklist
4. Begin Phase 1

## Support

This is a self-study curriculum. If you encounter issues:

1. Check the troubleshooting section in the relevant phase
2. Review the debugging phase (13-debugging)
3. Consult the resource index for official documentation
4. Check project documentation for common issues

## Progress Tracking

Track your progress through each phase's completion checklist. When you complete the entire curriculum, you will have:

- Built 25+ practical projects
- Developed deep embedded systems understanding
- Created a portfolio of working systems
- Gained skills applicable to professional embedded/IoT development

---

**Start your journey in [00-orientation/](00-orientation/).**
