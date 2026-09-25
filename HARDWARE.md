# Hardware Requirements Guide

This guide details all hardware required for the Embedded Systems & IoT curriculum, organized by phase and priority.

## Hardware Philosophy

This curriculum is designed to be accessible without requiring expensive equipment. Core concepts can be learned with basic components. Advanced hardware is introduced only when necessary for specific advanced topics.

### Cost Principles
- **Starter hardware:** ~$50-100 USD
- **Intermediate additions:** ~$50-100 USD
- **Advanced additions:** ~$100-200 USD (optional, for advanced phases)

### Substitution Policy
- ESP32 boards can be substituted with other ESP32 variants
- Sensors can be substituted with functionally equivalent alternatives
- Raspberry Pi is optional and can be replaced with any Linux SBC
- STM32 boards can be substituted with other STM32 variants

---

## Required Starter Hardware

**Acquire before starting Phase 04 (Electronics)**

### Core Components

| Component | Specification | Quantity | Purpose | Est. Cost |
|-----------|---------------|----------|---------|-----------|
| ESP32 Development Board | Any common variant (ESP32-DevKitC, NodeMCU, etc.) | 1 | Main MCU platform | $5-15 |
| USB Cable | Micro-USB or USB-C (matching board) | 1 | Programming/power | $3-5 |
| Breadboard | 400+ point, standard size | 1 | Circuit prototyping | $5-10 |
| Jumper Wires | Male-to-male, various lengths | 1 set | Connections | $5-10 |
| LEDs | Red, green, yellow (5mm) | 5+ | Output visualization | $2-5 |
| Resistors | 220Ω, 330Ω, 1kΩ, 10kΩ (1/4W) | 10+ each | Current limiting, pull-ups | $3-5 |
| Push Buttons | Tactile switches, 6mm | 5+ | Digital input | $2-5 |
| Potentiometer | 10kΩ linear | 1 | Analog input | $1-3 |
| Multimeter | Digital, basic functions | 1 | Voltage/current measurement | $15-30 |

### Optional but Recommended Starter Additions

| Component | Specification | Quantity | Purpose | Est. Cost |
|-----------|---------------|----------|---------|-----------|
| Temperature Sensor | DHT11/DHT22 or DS18B20 | 1 | Temperature measurement | $2-5 |
| Light Sensor | Photoresistor (LDR) | 1 | Light measurement | $1-2 |
| Buzzer | Passive or active | 1 | Audio output | $1-3 |
| Servo Motor | SG90 or similar | 1 | Actuator control | $3-5 |

**Total Starter Cost:** ~$40-80 USD

---

## Phase-Specific Hardware

### Phase 04 - Electronics
**Required:** All starter hardware above
**Additional:** None required

### Phase 06 - ESP32
**Required:** Starter hardware
**Additional:** None required (uses existing ESP32)

### Phase 07 - Sensors and Actuators
**Required:** Starter hardware + sensors
**Additional:**

| Component | Specification | Quantity | Purpose | Est. Cost |
|-----------|---------------|----------|---------|-----------|
| OLED Display | 0.96" I2C SSD1306 | 1 | Visual output | $5-10 |
| Accelerometer | MPU6050 or ADXL345 | 1 | Motion sensing | $3-8 |
| Ultrasonic Sensor | HC-SR04 | 1 | Distance measurement | $3-5 |

### Phase 08 - Embedded Communication
**Required:** Previous hardware
**Additional:** None required (uses existing I2C/SPI/UART devices)

### Phase 09 - Networking
**Required:** Previous hardware
**Additional:** None required (uses ESP32 Wi-Fi)

### Phase 10 - MQTT and IoT
**Required:** Previous hardware
**Additional:** None required (uses ESP32 Wi-Fi)

### Phase 11 - Linux for Embedded
**Required:** Computer with Linux or WSL
**Additional:** None required (software phase)

### Phase 12 - Raspberry Pi
**Required:** Raspberry Pi or equivalent SBC
**Additional:**

| Component | Specification | Quantity | Purpose | Est. Cost |
|-----------|---------------|----------|---------|-----------|
| Raspberry Pi | Pi 3B+, Pi 4, or equivalent | 1 | Gateway platform | $35-75 |
| MicroSD Card | 16GB+ Class 10 | 1 | Operating system | $5-10 |
| Power Supply | 5V 2.5A+ (USB-C or Micro-USB) | 1 | Pi power | $5-10 |

### Phase 13 - Debugging
**Required:** Previous hardware
**Additional:**

| Component | Specification | Quantity | Purpose | Est. Cost |
|-----------|---------------|----------|---------|-----------|
| Logic Analyzer | 8+ channels, 24MHz+ | 1 | Protocol debugging | $10-30 |

### Phase 14 - FreeRTOS
**Required:** Previous hardware
**Additional:** None required (software phase)

### Phase 15 - Embedded Security
**Required:** Previous hardware
**Additional:** None required (software phase)

### Phase 16 - Cloud and Edge
**Required:** Previous hardware
**Additional:** None required (software phase)

### Phase 17 - STM32
**Required:** STM32 development board
**Additional:**

| Component | Specification | Quantity | Purpose | Est. Cost |
|-----------|---------------|----------|---------|-----------|
| STM32 Board | Nucleo or Discovery board | 1 | STM32 platform | $15-30 |
| ST-LINK Debugger | If not included with board | 1 | Programming/debugging | $10-20 |

### Phase 18 - Industrial IoT
**Required:** Previous hardware
**Additional:**

| Component | Specification | Quantity | Purpose | Est. Cost |
|-----------|---------------|----------|---------|-----------|
| RS-485 Module | MAX485 or similar | 1 | Industrial communication | $3-5 |
| CAN Module | MCP2515 or similar | 1 | CAN communication | $5-10 |

---

## Optional Advanced Hardware

These components are useful for advanced projects but not required for curriculum completion.

### Advanced Sensors
| Component | Specification | Purpose | Est. Cost |
|-----------|---------------|---------|-----------|
| Current Sensor | ACS712 (5A/20A/30A) | Current measurement | $3-8 |
| Gas Sensor | MQ-2, MQ-5, etc. | Gas detection | $3-8 |
| Pressure Sensor | BMP280/BME280 | Barometric pressure | $3-8 |
| GPS Module | NEO-6M or similar | Location tracking | $10-20 |
| RFID Module | RC522 | RFID reading | $3-5 |

### Advanced Actuators
| Component | Specification | Purpose | Est. Cost |
|-----------|---------------|---------|-----------|
| Relay Module | 1-4 channel, 5V | High-power switching | $3-10 |
| Motor Driver | L298N or similar | Motor control | $5-10 |
| Stepper Motor | NEMA 17 or similar | Precision motion | $10-20 |
| DC Motor | Various sizes | Motion control | $3-10 |

### Power & Protection
| Component | Specification | Purpose | Est. Cost |
|-----------|---------------|---------|-----------|
| Battery Holder | 18650 or AA | Portable power | $2-5 |
| Voltage Regulator | LM2596 or similar | Power regulation | $2-5 |
| Diodes | 1N4007 or similar | Protection | $1-3 |
| Capacitors | Various values | Filtering | $2-5 |

### Development Tools
| Component | Specification | Purpose | Est. Cost |
|-----------|---------------|---------|-----------|
| Oscilloscope | USB or bench type | Signal analysis | $50-300 |
| Better Multimeter | With capacitance, frequency | Advanced measurement | $50-100 |
| Power Supply | Adjustable, 0-30V | Variable power | $30-100 |
| Soldering Iron | Temperature controlled | Permanent circuits | $20-50 |

---

## Hardware Substitution Guide

### ESP32 Board Substitutions
All ESP32 boards are functionally similar for this curriculum. Common options:
- ESP32-DevKitC (Espressif official)
- NodeMCU ESP32
- Wemos D1 Mini ESP32
- FireBeetle ESP32
- Any ESP32 board with USB programming

**Check for:**
- USB programming capability
- Accessible GPIO pins
- Compatible with Arduino-ESP32 and ESP-IDF

### Sensor Substitutions
Sensors can be substituted with functionally equivalent alternatives:

**Temperature:**
- DHT11/DHT22 → DS18B20 → BME280 → Any I2C temperature sensor

**Acceleration:**
- MPU6050 → ADXL345 → Any I2C accelerometer

**Display:**
- SSD1306 OLED → Any I2C OLED (0.96" or 1.3")

**Communication:**
- Any I2C sensor with same functionality
- Any SPI sensor with same functionality

### Raspberry Pi Substitutions
Any single-board computer with:
- ARM CPU
- Linux support
- GPIO pins
- Network connectivity

Examples:
- Raspberry Pi 3B+, 4B, 5
- Orange Pi
- BeagleBone
- Any similar SBC

### STM32 Substitutions
Any STM32 board with:
- ST-LINK or SWD debugging
- Arduino-IDE support or STM32CubeIDE support
- Required peripherals (GPIO, UART, I2C, SPI, CAN)

Examples:
- STM32 Nucleo boards
- STM32 Discovery boards
- Any STM32 development board

---

## Hardware Acquisition Strategy

### Minimum Viable Setup (Phases 0-7)
Cost: ~$40-60
- ESP32 board
- Basic components (LEDs, resistors, buttons)
- Breadboard and wires
- Multimeter
- 1-2 basic sensors

### Intermediate Setup (Phases 8-12)
Cost: ~$80-120 (cumulative)
- Minimum viable setup
- OLED display
- Additional sensors
- Raspberry Pi (for Phase 12)

### Advanced Setup (Phases 13-18)
Cost: ~$150-250 (cumulative)
- Intermediate setup
- Logic analyzer
- STM32 board
- Industrial communication modules
- Advanced sensors/actuators as needed

---

## Hardware Safety Guidelines

### Electrical Safety
- Never exceed component voltage/current ratings
- Always use current limiting for LEDs
- Use appropriate power supplies for components
- Double-check wiring before applying power
- Never work on live circuits unless specifically instructed

### Component Safety
- Handle components by edges, not pins
- Use proper ESD precautions for sensitive components
- Check component polarity before connecting
- Use heat sinks for power components
- Provide adequate ventilation

### Workspace Safety
- Keep workspace clean and organized
- Use appropriate lighting
- Keep flammable materials away from circuits
- Have fire extinguisher nearby
- Use safety glasses when soldering
- Ensure proper ventilation

---

## Hardware Suppliers

### International Suppliers
- **Adafruit** (US) - High-quality tutorials and components
- **SparkFun** (US) - Educational focus, good documentation
- **Seeed Studio** (China/Global) - Wide selection, good prices
- **AliExpress** (China) - Lowest prices, longer shipping
- **Amazon** - Fast shipping, varying quality

### Regional Options
- **Europe:** TME, Farnell, RS Components
- **Asia:** LCSC, Digi-Key (Asia)
- **Local:** Electronics stores, hobby shops

### Quality Considerations
- Official manufacturer boards when possible
- Reputable suppliers for critical components
- Reviews and specifications for unknown brands
- Counterfeit components are common for some items

---

## Hardware Maintenance

### Storage
- Store components in organized containers
- Keep breadboards clean
- Protect boards from static discharge
- Store in dry environment
- Label components for easy identification

### Care
- Clean breadboard contacts periodically
- Check for loose connections
- Inspect for damaged components
- Keep firmware updated
- Calibrate sensors as needed

### Troubleshooting Hardware
- Check power supply first
- Verify ground connections
- Test components individually
- Use multimeter for verification
- Check for short circuits
- Verify component specifications

---

## Hardware Budget Planning

### Phase-by-Phase Budget

| Phase | Required Hardware | Cost Range |
|-------|------------------|------------|
| 00-03 | None (software/concepts) | $0 |
| 04 | Starter hardware | $40-80 |
| 05 | None (uses starter) | $0 |
| 06 | None (uses starter) | $0 |
| 07 | Sensors + display | $15-30 |
| 08-10 | None (uses existing) | $0 |
| 11 | None (software) | $0 |
| 12 | Raspberry Pi setup | $50-100 |
| 13 | Logic analyzer | $10-30 |
| 14-16 | None (software) | $0 |
| 17 | STM32 board + debugger | $25-50 |
| 18 | Industrial modules | $10-20 |

**Total Estimated Cost:** $150-310 USD for complete curriculum

### Cost-Saving Tips
- Buy components in kits when possible
- Use local suppliers to avoid shipping
- Substitute with equivalent components
- Share costs with study groups
- Start with minimum viable setup
- Acquire advanced hardware as needed

---

## Hardware Verification

Before starting each phase, verify you have:
- ✅ All required components
- ✅ Working tools (multimeter, etc.)
- ✅ Proper power supplies
- ✅ Necessary cables and connectors
- ✅ Workspace safety measures
- ✅ Component datasheets/reference

---

## Next Steps

1. Acquire starter hardware (Phase 04 requirements)
2. Set up workspace with safety measures
3. Organize components for easy access
4. Test basic components (LEDs, resistors, etc.)
5. Begin Phase 04 when hardware is ready

**For detailed component specifications and wiring information, refer to individual phase documentation.**
