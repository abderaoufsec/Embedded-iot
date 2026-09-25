# Embedded Systems & IoT Learning Roadmap

This roadmap shows the complete learning path from beginner to advanced embedded/IoT development.

## Curriculum Structure

```
00-orientation          ──► Setup, safety, methodology
01-computer-fundamentals ──► Binary, hex, memory, CPU
02-c-programming        ──► Embedded C programming
03-digital-electronics  ──► Logic gates, digital circuits
04-electronics          ──► Circuits, components, measurement
05-microcontrollers     ──► MCU architecture, peripherals
06-esp32                ──► ESP32 development
07-sensors-and-actuators ──► Sensor integration
08-embedded-communication ──► UART, I2C, SPI, CAN
09-networking           ──► TCP/IP, HTTP, networking
10-mqtt-and-iot         ──► MQTT, IoT architecture
11-linux-for-embedded  ──► Linux for gateways
12-raspberry-pi         ──► Raspberry Pi gateway
13-debugging            ──► Systematic debugging
14-rtos-freertos        ──► Real-time operating systems
15-embedded-security    ──► Security fundamentals
16-cloud-and-edge       ──► Cloud integration
17-stm32                ──► Professional STM32
18-industrial-iot       ──► Industrial systems
```

## Phase-by-Phase Overview

### Foundation Phases (0-5)

#### 00 - Orientation
**Duration:** 1-2 days
**Goal:** Setup environment, understand methodology, safety basics
**Output:** Ready to begin learning

#### 01 - Computer Fundamentals
**Duration:** 1-2 weeks
**Goal:** Understand how computers work at the bit level
**Key Topics:** Binary, hex, memory, CPU, registers, compilation
**Project:** Binary/hex manipulation program

#### 02 - C Programming
**Duration:** 3-4 weeks
**Goal:** Embedded-focused C programming skills
**Key Topics:** Pointers, memory, structs, bit manipulation, compilation
**Projects:** CLI utility, circular buffer, state machine

#### 03 - Digital Electronics
**Duration:** 1-2 weeks
**Goal:** Understand digital logic and circuits
**Key Topics:** Logic gates, Boolean algebra, flip-flops, clocks
**Project:** Digital logic simulator

#### 04 - Electronics
**Duration:** 2-3 weeks
**Goal:** Practical electronics skills for embedded systems
**Key Topics:** Ohm's law, components, measurement, safety
**Labs:** LED, button, potentiometer, PWM, transistor switching

#### 05 - Microcontrollers
**Duration:** 2-3 weeks
**Goal:** Understand MCU architecture before platform-specific APIs
**Key Topics:** Architecture, registers, memory map, peripherals, HAL
**Project:** Register-level GPIO simulation

### Core Embedded Development (6-10)

#### 06 - ESP32
**Duration:** 4-6 weeks
**Goal:** Practical ESP32 development skills
**Key Topics:** GPIO, ADC, PWM, timers, Wi-Fi, Arduino framework, ESP-IDF
**Projects:** GPIO controller, sensor reader, Wi-Fi device, HTTP server

#### 07 - Sensors and Actuators
**Duration:** 3-4 weeks
**Goal:** Integrate sensors and actuators reliably
**Key Topics:** Sensor principles, datasheets, calibration, filtering, noise
**Project:** Environmental monitoring node

#### 08 - Embedded Communication
**Duration:** 3-4 weeks
**Goal:** Deep understanding of communication protocols
**Key Topics:** UART, I2C, SPI, CAN, framing, addressing, error detection
**Projects:** Multi-protocol communication system

#### 09 - Networking
**Duration:** 3-4 weeks
**Goal:** Embedded networking fundamentals
**Key Topics:** TCP/IP, HTTP, sockets, DNS, DHCP, embedded networking
**Projects:** TCP client, UDP telemetry, HTTP server

#### 10 - MQTT and IoT
**Duration:** 3-4 weeks
**Goal:** IoT architecture and MQTT implementation
**Key Topics:** MQTT, publish/subscribe, telemetry, commands, security
**Projects:** MQTT sensor node, MQTT command node, secure MQTT

### Advanced Topics (11-18)

#### 11 - Linux for Embedded
**Duration:** 2-3 weeks
**Goal:** Linux skills for embedded gateways
**Key Topics:** Linux basics, scripting, services, networking, Git
**Project:** Linux service for sensor processing

#### 12 - Raspberry Pi
**Duration:** 2-3 weeks
**Goal:** Raspberry Pi as IoT gateway
**Key Topics:** GPIO, Python/C, services, MQTT, Docker
**Project:** MQTT gateway with storage

#### 13 - Debugging
**Duration:** 2-3 weeks
**Goal:** Systematic debugging skills
**Key Topics:** Debugging methodology, tools, electrical debugging
**Project:** Debug intentionally broken systems

#### 14 - FreeRTOS
**Duration:** 3-4 weeks
**Goal:** Real-time operating system concepts
**Key Topics:** Tasks, scheduling, queues, semaphores, race conditions
**Projects:** Multi-task sensor system, event-driven controller

#### 15 - Embedded Security
**Duration:** 2-3 weeks
**Goal:** Security fundamentals for embedded systems
**Key Topics:** Threat modeling, secure boot, TLS, credentials, OTA security
**Project:** Secure device with OTA

#### 16 - Cloud and Edge
**Duration:** 2-3 weeks
**Goal:** Cloud integration and edge computing
**Key Topics:** Edge vs cloud, APIs, databases, time-series, containers
**Project:** Edge gateway with cloud integration

#### 17 - STM32
**Duration:** 4-6 weeks
**Goal:** Professional STM32 development
**Key Topics:** STM32 architecture, Cube ecosystem, HAL, LL, debugging
**Projects:** STM32 motor controller, CAN communication

#### 18 - Industrial IoT
**Duration:** 3-4 weeks
**Goal:** Industrial systems and protocols
**Key Topics:** Industrial architecture, Modbus, SCADA, OPC UA, reliability
**Project:** Industrial edge gateway

## Project Progression

### Beginner (Phases 4-7)
1. LED blinker
2. Button-controlled LED
3. Traffic light simulator
4. Potentiometer reader
5. PWM dimmer
6. Temperature reader
7. UART monitor
8. OLED display

### Intermediate (Phases 6-10)
9. Environmental monitor
10. Data logger
11. Wi-Fi sensor node
12. ESP32 HTTP server
13. OLED sensor station
14. Threshold alert system

### IoT (Phases 10-12)
15. MQTT sensor node
16. MQTT command node
17. Secure MQTT node
18. Raspberry Pi gateway
19. Dashboard integration
20. Multi-node IoT system

### Advanced (Phases 13-18)
21. FreeRTOS multi-task system
22. Secure OTA system
23. STM32 motor controller
24. Modbus/CAN system
25. Industrial edge gateway

### Capstone
Complete motor monitoring/predictive maintenance IoT system

## Time Estimates

- **Foundation (0-5):** 10-14 weeks
- **Core Embedded (6-10):** 17-24 weeks
- **Advanced (11-18):** 21-30 weeks
- **Total:** 48-68 weeks (approximately 1-1.5 years at part-time pace)

*Time estimates vary based on prior experience and study intensity.*

## Prerequisites Flow

```
None
 ↓
00-orientation
 ↓
01-computer-fundamentals
 ↓
02-c-programming
 ↓
03-digital-electronics
 ↓
04-electronics
 ↓
05-microcontrollers
 ↓
06-esp32
 ↓
07-sensors-and-actuators
 ↓
08-embedded-communication
 ↓
09-networking
 ↓
10-mqtt-and-iot
 ↓
11-linux-for-embedded ← Can be taken in parallel with 10-12
 ↓
12-raspberry-pi
 ↓
13-debugging ← Can be taken earlier as needed
 ↓
14-rtos-freertos
 ↓
15-embedded-security
 ↓
16-cloud-and-edge
 ↓
17-stm32
 ↓
18-industrial-iot
 ↓
Capstone Project
```

## Skill Development Progression

### Technical Skills
- **Phase 0-2:** Programming fundamentals, computer architecture
- **Phase 3-5:** Electronics, digital logic, MCU architecture
- **Phase 6-8:** Embedded development, communication protocols
- **Phase 9-10:** Networking, IoT architecture
- **Phase 11-12:** Linux, gateway development
- **Phase 13-14:** Debugging, real-time systems
- **Phase 15-18:** Security, cloud integration, professional development

### Practical Skills
- **Phase 0-2:** Setup, programming environment, debugging basics
- **Phase 3-5:** Circuit building, measurement, datasheet reading
- **Phase 6-8:** Hardware integration, protocol implementation
- **Phase 9-10:** Network programming, IoT system design
- **Phase 11-12:** System administration, service management
- **Phase 13-14:** Advanced debugging, system optimization
- **Phase 15-18:** Security implementation, professional workflows

## Assessment Gates

Each phase requires:
- ✅ Knowledge test pass
- ✅ Practical test pass
- ✅ Completion checklist verified
- ✅ Project(s) completed
- ✅ Documentation submitted

**Do not skip assessments.** Gaps will compound in later phases.

## Hardware Acquisition Timeline

### Initial (Phase 0-5)
- ESP32 board
- Basic components (LEDs, resistors, buttons)
- Breadboard, wires
- Multimeter

### Intermediate (Phase 6-10)
- Additional sensors
- OLED display
- Logic analyzer (optional)

### Advanced (Phase 11-18)
- Raspberry Pi
- STM32 board
- Industrial components (as needed)

See [HARDWARE.md](HARDWARE.md) for detailed requirements.

## Learning Path Customization

### For Complete Beginners
Follow the sequence exactly. Do not skip phases.

### For Programmers (New to Embedded)
- Complete 00-orientation
- Take assessments for 01-02
- Focus on 03-05 (embedded-specific)
- Continue sequentially

### For Electronics/EE Background
- Complete 00-orientation
- Take assessments for 03-04
- Focus on 01-02, 05 (programming/MCU)
- Continue sequentially

### For Embedded Developers (New to IoT)
- Complete 00-orientation
- Take assessments for 01-08
- Focus on 09-10 (networking/IoT)
- Continue to advanced phases

## Success Metrics

You are progressing successfully when:
- You can explain concepts without notes
- You can build projects without tutorials
- You can debug issues systematically
- You can read and understand datasheets
- You can design simple systems independently
- You complete phase assessments without assistance

## Next Steps

1. Complete [00-orientation](00-orientation/)
2. Begin your learning journey
3. Track progress with completion checklists
4. Build projects systematically
5. Develop deep understanding through practice

---

**This roadmap is your guide. Follow it, complete each phase thoroughly, and you will develop genuine embedded/IoT expertise.**
