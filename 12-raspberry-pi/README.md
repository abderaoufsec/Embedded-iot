# Phase 12 — Raspberry Pi

> **Goal:** Develop practical Raspberry Pi skills for embedded Linux applications, GPIO interfacing, sensor integration, and IoT gateway development.
>
> **Prerequisite:** Phase 11 — Linux for Embedded
>
> **Outcome:** You can configure Raspberry Pi hardware, use GPIO for sensor interfacing, run headless Linux systems, implement services, and build IoT gateways.

---

## What You Will Learn

By completing this phase, you will understand:

- **Raspberry Pi Architecture:** SBC vs MCU, CPU, RAM, storage, boot process
- **Raspberry Pi Hardware:** GPIO, 3.3V logic, pinout, electrical characteristics
- **GPIO Programming:** Input/output, pull-up/pull-down, interrupts, PWM
- **Communication Interfaces:** I2C, SPI, UART on Raspberry Pi
- **Linux GPIO:** sysfs, libgpiod, device tree overlays
- **Raspberry Pi OS:** Installation, configuration, headless operation
- **System Management:** SSH, networking, systemd services, logging
- **Python GPIO:** RPi.GPIO, gpiozero, Python programming
- **C GPIO:** WiringPi, libgpiod, C/C++ interaction
- **MQTT Gateway:** Raspberry Pi as MQTT broker/gateway
- **ESP32 Integration:** Communicating between ESP32 and Raspberry Pi
- **Reliability:** Headless operation, watchdog, auto-restart
- **Troubleshooting:** Hardware debugging, system diagnostics

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phase 0 — Orientation
- ✅ Completed Phase 1 — Computer Fundamentals
- ✅ Completed Phase 2 — C Programming
- ✅ Completed Phase 3 — Digital Electronics
- ✅ Completed Phase 4 — Electronics
- ✅ Completed Phase 5 — Microcontrollers
- ✅ Completed Phase 6 — ESP32
- ✅ Completed Phase 7 — Sensors and Actuators
- ✅ Completed Phase 8 — Embedded Communication
- ✅ Completed Phase 9 — Networking
- ✅ Completed Phase 10 — MQTT and IoT
- ✅ Completed Phase 11 — Linux for Embedded
- ✅ Understanding of Linux CLI from Phase 11
- ✅ Understanding of networking from Phase 9
- ✅ Understanding of MQTT from Phase 10
- ✅ Understanding of C programming from Phase 2

**Required Hardware:**
- Raspberry Pi (any model 3B+, 4, or newer recommended)
- MicroSD card (16GB minimum, Class 10)
- MicroSD card reader
- Power supply (official Raspberry Pi power supply recommended)
- HDMI cable and monitor (for initial setup, optional for headless)
- USB keyboard and mouse (for initial setup, optional for headless)
- Network connection (Ethernet or Wi-Fi)
- Breadboard and jumper wires
- LEDs and resistors (220Ω, 1kΩ)
- I2C sensor (e.g., BME280, MPU6050)
- UART-compatible device or USB-TTL adapter

**Required Software:**
- Raspberry Pi Imager
- SSH client (for headless operation)
- Computer with network access

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain the difference between SBC and MCU
- Install and configure Raspberry Pi OS
- Set up headless Raspberry Pi operation
- Use GPIO for digital input/output
- Configure pull-up/pull-down resistors
- Use I2C, SPI, and UART interfaces
- Program GPIO with Python and C
- Create systemd services
- Configure networking on Raspberry Pi
- Implement MQTT gateway functionality
- Communicate between ESP32 and Raspberry Pi
- Troubleshoot Raspberry Pi hardware and software issues
- Monitor system logs and health
- Ensure reliable headless operation

---

## Why This Matters

**Raspberry Pi vs MCU:**

- **MCU (ESP32, STM32):** Low power, real-time, dedicated I/O, bare-metal or RTOS, suited for control loops, sensor reading, actuator control
- **SBC (Raspberry Pi):** Higher power, Linux OS, general-purpose, suited for data processing, networking, user interfaces, gateways

**When to Use Raspberry Pi:**
- Need Linux environment and tools
- Complex data processing or analytics
- Network gateway functionality
- User interface or display
- Multiple communication protocols
- Database or storage requirements
- Higher-level programming (Python, Node.js, etc.)

**When to Use MCU:**
- Battery-powered or low-power applications
- Real-time control loops
- Minimal hardware requirements
- Cost-sensitive applications
- Simple sensor/actuator control
- Direct hardware interaction

**Gateway Architecture:**
Raspberry Pi often serves as a gateway between MCUs and cloud networks, handling:
- Protocol translation (UART/Modbus → MQTT/HTTP)
- Data aggregation and buffering
- Local processing and edge computing
- Security and authentication
- OTA updates and device management

---

## Core Concepts

### Raspberry Pi Architecture

**Single Board Computer (SBC):**
- Complete computer on single board
- CPU, RAM, storage, I/O integrated
- Runs full operating system (Linux)
- Higher power consumption
- General-purpose computing

**SBC vs MCU:**
- **SBC:** General-purpose, Linux, higher power, complex
- **MCU:** Specialized, bare-metal/RTOS, low power, real-time

**Raspberry Pi Models:**
- **Pi 3B+:** Quad-core ARM Cortex-A53, 1GB RAM, good for basic projects
- **Pi 4:** Quad-core ARM Cortex-A72, 2-8GB RAM, higher performance
- **Pi Zero/Zero W:** Single-core, low power, compact form factor
- **Pi 5:** Quad-core ARM Cortex-A76, higher performance (newer)

**CPU:**
- ARM architecture (Cortex-A53, A72, A76)
- 32-bit or 64-bit depending on model
- Clock rates: 700MHz to 2.4GHz
- Multiple cores for parallel processing

**RAM:**
- 512MB to 8GB depending on model
- Shared with GPU
- Volatile storage
- Limits number of processes

**Storage:**
- MicroSD card (primary)
- USB storage
- Network storage (NFS)
- EMMC on some models

**Boot Process:**
1. Power on
2. GPU loads bootloader from SD card
3. Bootloader loads kernel
4. Kernel mounts root filesystem
5. Init system starts (systemd)
6. Services start

---

### Raspberry Pi Hardware

**GPIO Header:**
- 40-pin header (26 pins on older models)
- 3.3V logic levels
- 5V tolerance on some pins (check documentation)
- Current limits per pin and total
- Multiple functions per pin (GPIO, I2C, SPI, UART, PWM)

**Pinout:**
- Power pins: 5V, 3.3V, GND
- GPIO pins: GPIO0-GPIO27 (numbering varies)
- I2C pins: SDA (GPIO2), SCL (GPIO3)
- SPI pins: MOSI, MISO, SCLK, CE0, CE1
- UART pins: TXD (GPIO14), RXD (GPIO15)
- PWM pins: GPIO12, GPIO13, GPIO18, GPIO19

**GPIO Electrical Characteristics:**
- Logic high: > 1.8V (typically 3.3V)
- Logic low: < 1.3V (typically 0V)
- Max current per pin: 16mA (safe limit)
- Total current limit: 50mA for all GPIO combined
- Absolute maximum: 50mA per pin (do not exceed)

**3.3V GPIO Safety:**
- Do not connect 5V directly to GPIO pins
- Use level shifters for 5V devices
- Use current-limiting resistors for LEDs
- Do not exceed current limits
- Use appropriate pull-up/pull-down resistors

---

### GPIO Programming

**Digital Input:**
- Read digital state (high/low)
- Configure pull-up/pull-down resistors
- Debounce for mechanical switches
- Interrupts for event-driven reading

**Digital Output:**
- Set digital state (high/low)
- Drive LEDs, relays, other devices
- Use current-limiting resistors
- Consider switching speed

**Pull-up/Pull-down:**
- **Pull-up:** Resistor to VCC, default high
- **Pull-down:** Resistor to GND, default low
- Internal pull-up/pull-down available
- External resistors for specific values
- Prevents floating inputs

**Interrupts:**
- Edge detection (rising, falling, both)
- Callback functions
- Debouncing in interrupt handler
- Avoid long processing in ISR

**PWM (Pulse Width Modulation):**
- Hardware PWM on specific pins
- Software PWM on any GPIO
- Duty cycle: 0-100%
- Frequency control
- Used for motor control, LED dimming, servo control

---

### Communication Interfaces

**I2C:**
- Two-wire serial (SDA, SCL)
- Multiple devices on same bus
- 7-bit or 10-bit addressing
- Open-drain with pull-up resistors
- Speed: 100kHz (standard), 400kHz (fast), 1MHz+ (fast-mode plus)
- I2C tools: `i2cdetect`, `i2cget`, `i2cset`

**SPI:**
- Four-wire serial (MOSI, MISO, SCLK, CS)
- Full-duplex communication
- Higher speed than I2C
- Multiple devices with chip select
- SPI tools: `spidev`, Python libraries

**UART:**
- Two-wire serial (TX, RX)
- Point-to-point communication
- Configurable baud rate
- Hardware flow control (RTS, CTS)
- UART tools: `screen`, `minicom`, Python serial library

---

### Linux GPIO

**sysfs (Deprecated but still used):**
- `/sys/class/gpio` interface
- File-based GPIO control
- Slow, being replaced by libgpiod
- Example: `echo 17 > /sys/class/gpio/export`

**libgpiod (Recommended):**
- Character device interface
- Better performance than sysfs
- Lines, requests, events
- GPIO tools: `gpiodetect`, `gpioinfo`, `gpioset`

**Device Tree Overlays:**
- Configure hardware at boot
- Define pin multiplexing
- Enable/disable peripherals
- `/boot/config.txt` configuration

---

### Raspberry Pi OS

**Installation:**
- Raspberry Pi Imager tool
- Choose OS (Raspberry Pi OS Lite for headless)
- Write to microSD card
- Enable SSH headless (create `ssh` file in boot partition)
- Configure Wi-Fi (create `wpa_supplicant.conf` in boot partition)

**Configuration:**
- `raspi-config` tool
- Expand filesystem
- Change hostname
- Enable/disable interfaces (SSH, I2C, SPI, UART)
- Change password
- Overclock settings (caution)

**Headless Operation:**
- SSH access only
- No monitor, keyboard, mouse
- Network configuration critical
- Static IP recommended
- Enable serial console for recovery

---

### System Management

**SSH:**
- Remote access to Raspberry Pi
- Password or key authentication
- Configuration in `/etc/ssh/sshd_config`
- Disable root login for security

**Networking:**
- Ethernet: automatic DHCP
- Wi-Fi: configure via `raspi-config` or `wpa_supplicant`
- Static IP: `/etc/dhcpcd.conf` or `/etc/network/interfaces`
- Check with `ip addr`, `ping`

**systemd Services:**
- Create custom services
- Auto-start applications
- Dependencies management
- Logs via journalctl
- Example: `.service` file in `/etc/systemd/system/`

**Logging:**
- System logs: `journalctl`
- Application logs: custom files
- Rotation to prevent disk exhaustion
- `/var/log/` directory

---

### Python GPIO

**RPi.GPIO:**
- Traditional Python GPIO library
- Simple API
- Broadcom pin numbering
- Example: `GPIO.setmode(GPIO.BCM)`

**gpiozero:**
- Modern, object-oriented API
- Cleaner syntax
- Built-in debounce
- Device-specific classes (LED, Button, etc.)
- Example: `from gpiozero import LED`

**Python GPIO Workflow:**
1. Import library
2. Set pin numbering mode
3. Configure pins as input/output
4. Read/write pins
5. Cleanup on exit

---

### C GPIO

**WiringPi:**
- Arduino-like API for Raspberry Pi
- Pin numbering may differ
- Not actively maintained
- Alternative: libgpiod

**libgpiod:**
- Modern C GPIO library
- Character device interface
- Better performance
- Recommended for new projects

**C GPIO Workflow:**
1. Include headers
2. Open GPIO chip
3. Request GPIO lines
4. Configure direction
5. Read/write values
6. Close and cleanup

---

### MQTT Gateway

**Raspberry Pi as MQTT Broker:**
- Install Mosquitto (covered in Phase 10)
- Configure for local network
- Authentication and TLS
- Persistence and reliability

**Raspberry Pi as MQTT Client:**
- Subscribe to device topics
- Publish to cloud topics
- Protocol translation
- Data aggregation

**Gateway Architecture:**
```
ESP32 → UART/Modbus → Raspberry Pi → MQTT → Cloud
```

**Reliability:**
- Auto-restart on failure
- Data buffering during network outage
- Watchdog monitoring
- Health checks

---

### ESP32 Integration

**Communication Methods:**
- UART: Serial communication
- MQTT: Both as MQTT clients
- HTTP: REST API
- Direct GPIO: Level shifting required

**Use Cases:**
- ESP32 as sensor node, Raspberry Pi as gateway
- ESP32 as actuator controller, Raspberry Pi as interface
- Distributed system with multiple ESP32 nodes

**Data Flow:**
- ESP32 reads sensors
- ESP32 sends data to Raspberry Pi
- Raspberry Pi processes and forwards
- Raspberry Pi stores or publishes to cloud

---

### Reliability

**Headless Operation:**
- SSH configuration backup
- Recovery methods (serial console)
- Network redundancy
- Power management

**Watchdog:**
- Hardware watchdog timer
- Software watchdog
- Auto-restart on hang
- Configuration in `/etc/watchdog.conf`

**Auto-restart:**
- systemd service restart policy
- Crontab-based monitoring
- Custom watchdog scripts
- Health monitoring

---

## Detailed Lessons

### Lesson 1: Raspberry Pi Hardware Fundamentals

**Objectives:**
- Understand Raspberry Pi architecture
- Compare SBC vs MCU
- Identify GPIO pinout and functions
- Understand electrical characteristics

**Content:**
- Raspberry Pi models and specifications
- CPU, RAM, storage overview
- GPIO header and pinout
- Electrical limits and safety
- SBC vs MCU decision framework

**Key Points:**
- Raspberry Pi is a full computer running Linux
- GPIO operates at 3.3V logic levels
- Current limits prevent damage
- Choose Raspberry Pi for Linux, MCU for real-time

---

### Lesson 2: Raspberry Pi OS Installation

**Objectives:**
- Install Raspberry Pi OS
- Configure headless operation
- Enable SSH
- Configure networking

**Content:**
- Raspberry Pi Imager usage
- Choosing OS variant (Lite vs Desktop)
- Headless SSH enablement
- Wi-Fi configuration
- First boot and initial setup

**Key Points:**
- Use Raspberry Pi Imager for reliable installation
- Enable SSH by creating `ssh` file in boot partition
- Configure Wi-Fi via `wpa_supplicant.conf`
- Change default password immediately

---

### Lesson 3: GPIO Digital I/O

**Objectives:**
- Configure GPIO as input/output
- Read digital sensors
- Control LEDs and actuators
- Use pull-up/pull-down resistors

**Content:**
- GPIO pin numbering (BCM vs Board)
- Python GPIO libraries (RPi.GPIO, gpiozero)
- Digital input reading
- Digital output control
- Pull-up/pull-down configuration
- LED control with current limiting

**Key Points:**
- Always use current-limiting resistors with LEDs
- Configure pull-up/pull-down to prevent floating inputs
- Cleanup GPIO on program exit
- Respect current limits

---

### Lesson 4: GPIO Interrupts and PWM

**Objectives:**
- Use GPIO interrupts for event-driven programming
- Implement PWM for motor/LED control
- Understand hardware vs software PWM

**Content:**
- Interrupt concept and edge detection
- Interrupt callback functions
- Debouncing switches
- PWM fundamentals
- Hardware PWM on specific pins
- Software PWM on any pin
- Servo control with PWM

**Key Points:**
- Interrupts enable event-driven programming
- Debounce mechanical switches to prevent false triggers
- Hardware PWM is more accurate than software PWM
- PWM frequency and duty cycle affect output

---

### Lesson 5: I2C Communication

**Objectives:**
- Configure I2C on Raspberry Pi
- Discover I2C devices
- Read/write I2C sensors
- Troubleshoot I2C issues

**Content:**
- I2C protocol overview
- Raspberry Pi I2C configuration
- I2C tools (`i2cdetect`, `i2cget`, `i2cset`)
- Python I2C libraries
- Reading I2C sensors (e.g., BME280)
- Troubleshooting I2C

**Key Points:**
- Enable I2C in `raspi-config`
- Use pull-up resistors for I2C
- Address conflicts prevent multiple devices with same address
- I2C speed affects reliability

---

### Lesson 6: SPI Communication

**Objectives:**
- Configure SPI on Raspberry Pi
- Communicate with SPI devices
- Understand SPI modes and speeds

**Content:**
- SPI protocol overview
- Raspberry Pi SPI configuration
- SPI modes (0-3)
- Python SPI libraries
- Reading SPI sensors
- Troubleshooting SPI

**Key Points:**
- Enable SPI in `raspi-config`
- SPI requires chip select for multiple devices
- SPI speed depends on device capabilities
- SPI is full-duplex (simultaneous send/receive)

---

### Lesson 7: UART Communication

**Objectives:**
- Configure UART on Raspberry Pi
- Communicate with UART devices
- Communicate with ESP32 via UART

**Content:**
- UART protocol overview
- Raspberry Pi UART configuration
- UART tools (`screen`, `minicom`)
- Python serial library
- Communicating with ESP32
- Troubleshooting UART

**Key Points:**
- Enable serial in `raspi-config`
- UART requires matching baud rate
- TX connects to RX, RX connects to TX
- Common ground is required

---

### Lesson 8: systemd Services

**Objectives:**
- Create systemd services
- Auto-start applications
- Manage service lifecycle
- View service logs

**Content:**
- systemd service files
- Service unit structure
- Enable/disable/start/stop services
- Dependencies and ordering
- journalctl for logs
- Auto-restart policies

**Key Points:**
- Systemd manages system services
- Service files go in `/etc/systemd/system/`
- `systemctl enable` for auto-start
- `journalctl -u service` for service logs

---

### Lesson 9: MQTT Gateway

**Objectives:**
- Configure Mosquitto on Raspberry Pi
- Implement MQTT gateway functionality
- Translate between protocols
- Ensure reliability

**Content:**
- Mosquitto installation and configuration
- Authentication and authorization
- Python MQTT client (paho-mqtt)
- Protocol translation (UART → MQTT)
- Data buffering
- Auto-reconnection

**Key Points:**
- Mosquitto provides MQTT broker functionality
- Gateway translates between protocols
- Buffer data during network outages
- Auto-reconnect on connection loss

---

### Lesson 10: ESP32 Integration

**Objectives:**
- Communicate between ESP32 and Raspberry Pi
- Choose appropriate communication method
- Implement distributed system

**Content:**
- ESP32-Raspberry Pi communication options
- UART communication example
- MQTT communication example
- Data aggregation
- System architecture

**Key Points:**
- Choose communication method based on requirements
- UART for direct serial communication
- MQTT for network-based communication
- Raspberry Pi can aggregate data from multiple ESP32 nodes

---

### Lesson 11: Headless Operation

**Objectives:**
- Configure Raspberry Pi for headless operation
- Implement recovery methods
- Ensure reliability

**Content:**
- Headless configuration
- SSH key authentication
- Serial console for recovery
- Static IP configuration
- Watchdog configuration
- Auto-restart on failure

**Key Points:**
- Headless operation requires network reliability
- Serial console provides recovery method
- Static IP prevents address changes
- Watchdog monitors system health

---

### Lesson 12: Troubleshooting

**Objectives:**
- Diagnose Raspberry Pi hardware issues
- Troubleshoot GPIO problems
- Debug system issues
- Use diagnostic tools

**Content:**
- Power supply issues
- SD card corruption
- GPIO troubleshooting
- Network troubleshooting
- System logs
- Diagnostic tools

**Key Points:**
- Insufficient power causes random issues
- SD card quality affects reliability
- Use logs to diagnose issues
- Test components individually

---

## Study Order

Follow this exact sequence:

1. **Study Raspberry Pi hardware fundamentals** (architecture, GPIO, electrical characteristics)
2. **Install and configure Raspberry Pi OS** (headless setup, SSH, networking)
3. **Study GPIO digital I/O** (input/output, pull-up/pull-down, Python GPIO)
4. **Study GPIO interrupts and PWM** (event-driven programming, motor/LED control)
5. **Study I2C communication** (configuration, I2C tools, sensor reading)
6. **Study SPI communication** (configuration, SPI modes, device communication)
7. **Study UART communication** (configuration, ESP32 integration)
8. **Study systemd services** (service creation, auto-start, logging)
9. **Study MQTT gateway** (Mosquitto, protocol translation, reliability)
10. **Study ESP32 integration** (communication methods, distributed systems)
11. **Study headless operation** (reliability, watchdog, recovery)
12. **Study troubleshooting** (hardware, GPIO, system diagnostics)
13. **Complete all exercises**
14. **Complete all labs**
15. **Complete the project**
16. **Take the knowledge test**
17. **Take the practical test**
18. **Review completion checklist**

---

## Exact Resources

### Resource 1: Raspberry Pi Documentation
- **Provider:** Raspberry Pi Foundation (Official)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Official Raspberry Pi documentation
- **URL:** https://www.raspberrypi.com/documentation/

### Resource 2: Raspberry Pi GPIO
- **Provider:** Raspberry Pi Foundation (Official)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** GPIO pinout and reference
- **URL:** https://www.raspberrypi.com/documentation/computers/raspberry-pi.html

### Resource 3: gpiozero Documentation
- **Provider:** gpiozero project (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Python GPIO library documentation
- **URL:** https://gpiozero.readthedocs.io/

### Resource 4: libgpiod Documentation
- **Provider:** libgpiod project (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** C GPIO library documentation
- **URL:** https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about/

### Resource 5: Raspberry Pi OS
- **Provider:** Raspberry Pi Foundation (Official)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Raspberry Pi OS documentation
- **URL:** https://www.raspberrypi.com/software/operating-systems/

### Resource 6: systemd Documentation
- **Provider:** freedesktop.org (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** systemd service management
- **URL:** https://www.freedesktop.org/software/systemd/man/

### Resource 7: Mosquitto Documentation
- **Provider:** Eclipse Foundation (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** MQTT broker documentation
- **URL:** https://mosquitto.org/documentation/

---

## Exercises

### Exercise 1: SBC vs MCU
**Objective:** Understand when to use Raspberry Pi vs MCU.

**Tasks:**
1. What is the difference between SBC and MCU?
2. When would you choose Raspberry Pi over ESP32?
3. When would you choose ESP32 over Raspberry Pi?
4. What are the power consumption differences?
5. What are the real-time capabilities differences?

**Expected Outcome:** You understand the appropriate use cases for SBC vs MCU.

### Exercise 2: GPIO Electrical Characteristics
**Objective:** Understand GPIO electrical limits.

**Tasks:**
1. What is the logic voltage level of Raspberry Pi GPIO?
2. What is the maximum current per GPIO pin?
3. What is the total current limit for all GPIO combined?
4. Why are current-limiting resistors necessary for LEDs?
5. What happens if you connect 5V to a GPIO pin?

**Expected Outcome:** You understand GPIO electrical safety requirements.

### Exercise 3: Pull-up/Pull-down
**Objective:** Understand pull-up/pull-down resistors.

**Tasks:**
1. What is the purpose of a pull-up resistor?
2. What is the purpose of a pull-down resistor?
3. What is a floating input?
4. When should you use internal vs external pull-up/pull-down?
5. How do you configure pull-up/pull-down in Python?

**Expected Outcome:** You understand pull-up/pull-down resistor usage.

### Exercise 4: I2C vs SPI vs UART
**Objective:** Compare communication interfaces.

**Tasks:**
1. What are the advantages of I2C?
2. What are the advantages of SPI?
3. What are the advantages of UART?
4. When would you choose I2C over SPI?
5. When would you choose UART over I2C?

**Expected Outcome:** You can choose appropriate communication interfaces.

### Exercise 5: systemd Services
**Objective:** Understand systemd service management.

**Tasks:**
1. What is a systemd service?
2. What is the difference between enable and start?
3. How do you view service logs?
4. What is auto-restart policy?
5. How do you create a custom service?

**Expected Outcome:** You understand systemd service management.

### Exercise 6: MQTT Gateway
**Objective:** Understand MQTT gateway architecture.

**Tasks:**
1. What is the role of an MQTT gateway?
2. How does protocol translation work?
3. Why is data buffering important?
4. How do you handle network outages?
5. What is the difference between broker and gateway?

**Expected Outcome:** You understand MQTT gateway functionality.

### Exercise 7: Headless Operation
**Objective:** Understand headless Raspberry Pi operation.

**Tasks:**
1. How do you enable SSH headless?
2. How do you configure Wi-Fi headless?
3. What is the serial console used for?
4. Why is static IP recommended for headless?
5. How do you recover a headless system?

**Expected Outcome:** You understand headless operation and recovery.

### Exercise 8: ESP32 Integration
**Objective:** Understand ESP32-Raspberry Pi communication.

**Tasks:**
1. What communication methods can connect ESP32 and Raspberry Pi?
2. What are the advantages of UART communication?
3. What are the advantages of MQTT communication?
4. How do you match baud rates in UART?
5. What is the architecture of a distributed system?

**Expected Outcome:** You understand ESP32-Raspberry Pi integration options.

### Exercise 9: PWM Fundamentals
**Objective:** Understand PWM concepts.

**Tasks:**
1. What is PWM?
2. What is duty cycle?
3. What is PWM frequency?
4. What is the difference between hardware and software PWM?
5. How is PWM used for motor control?

**Expected Outcome:** You understand PWM fundamentals.

### Exercise 10: Troubleshooting
**Objective:** Understand common Raspberry Pi issues.

**Tasks:**
1. What are symptoms of insufficient power?
2. What are symptoms of SD card corruption?
3. How do you check GPIO configuration?
4. How do you check network connectivity?
5. What logs are useful for troubleshooting?

**Expected Outcome:** You understand common issues and troubleshooting methods.

---

## Labs

### Lab 1: Raspberry Pi OS Setup
**Objective:** Install and configure Raspberry Pi OS headless.

**Prerequisites:**
- Raspberry Pi hardware
- MicroSD card
- Computer with network access

**Components:**
- Raspberry Pi
- MicroSD card
- MicroSD card reader
- Power supply
- Network connection

**Procedure:**

**1. Download Raspberry Pi Imager:**
- Download from official Raspberry Pi website
- Install on computer

**2. Write OS to SD Card:**
- Insert microSD card
- Open Raspberry Pi Imager
- Choose OS: Raspberry Pi OS Lite (64-bit)
- Choose storage: microSD card
- Click Write
- Wait for completion

**3. Enable Headless SSH:**
- Eject and reinsert microSD card
- Open boot partition
- Create empty file named `ssh` (no extension)

**4. Configure Wi-Fi (if using Wi-Fi):**
- Create file `wpa_supplicant.conf` in boot partition
- Content:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US
network={
    ssid="YOUR_SSID"
    psk="YOUR_PASSWORD"
}
```

**5. Boot Raspberry Pi:**
- Insert microSD card into Raspberry Pi
- Connect power supply
- Wait for boot (30-60 seconds)

**6. Connect via SSH:**
- Find IP address from router
- SSH: `ssh pi@raspberrypi.local` or `ssh pi@IP_ADDRESS`
- Default password: `raspberry`

**7. Initial Configuration:**
- Change password: `passwd`
- Update system: `sudo apt update && sudo apt upgrade`
- Expand filesystem: `sudo raspi-config` → Advanced Options → Expand Filesystem

**Expected Behavior:**
- Raspberry Pi boots successfully
- SSH connection established
- System updated
- Filesystem expanded

**Troubleshooting:**
- Cannot connect via SSH: Check network, verify SSH file exists
- Cannot find IP: Check router DHCP table
- Boot fails: Check power supply, try different SD card

**Completion Criteria:**
- Raspberry Pi OS installed
- Headless SSH working
- System updated
- Password changed

---

### Lab 2: GPIO Digital Output
**Objective:** Control LED using GPIO.

**Prerequisites:**
- Completed Lab 1
- Raspberry Pi with SSH access

**Components:**
- Raspberry Pi
- LED
- 220Ω resistor
- Breadboard
- Jumper wires

**Procedure:**

**1. Circuit:**
- Connect LED anode to GPIO17
- Connect LED cathode to 220Ω resistor
- Connect resistor to GND
- Verify circuit

**2. Python Code:**
```python
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(17, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
```

**3. Run:**
```bash
nano led_blink.py
# Paste code
python3 led_blink.py
```

**4. Test:**
- LED should blink at 1-second intervals
- Press Ctrl+C to stop

**Expected Behavior:**
- LED blinks continuously
- Clean GPIO cleanup on exit

**Troubleshooting:**
- LED not lighting: Check GPIO pin, check resistor value, check LED orientation
- Permission denied: Use sudo or add user to gpio group
- Module not found: Install RPi.GPIO: `sudo apt install python3-rpi.gpio`

**Completion Criteria:**
- LED blinks successfully
- GPIO cleanup works
- Code runs without errors

---

### Lab 3: GPIO Digital Input with Pull-up
**Objective:** Read button with pull-up resistor.

**Prerequisites:**
- Completed Lab 2

**Components:**
- Raspberry Pi
- Push button
- 10kΩ resistor (for external pull-up, or use internal)
- Breadboard
- Jumper wires

**Procedure:**

**1. Circuit (using internal pull-up):**
- Connect button between GPIO18 and GND
- No external resistor needed

**2. Python Code:**
```python
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(18) == GPIO.LOW:
            print("Button pressed")
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
```

**3. Run:**
```bash
nano button_read.py
# Paste code
python3 button_read.py
```

**4. Test:**
- Press button
- Should print "Button pressed"

**Expected Behavior:**
- Button press detected
- No false triggers from floating input

**Troubleshooting:**
- Always reading pressed: Check wiring, check pull-up configuration
- Not detecting press: Check GPIO pin, check button continuity
- Multiple triggers: Add debounce delay

**Completion Criteria:**
- Button press detected reliably
- Pull-up prevents floating input
- Clean GPIO cleanup

---

### Lab 4: GPIO Interrupts
**Objective:** Use GPIO interrupts for event-driven programming.

**Prerequisites:**
- Completed Lab 3

**Components:**
- Same as Lab 3

**Procedure:**

**1. Circuit:**
- Same as Lab 3

**2. Python Code:**
```python
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_callback(channel):
    print("Button pressed (interrupt)")

GPIO.add_event_detect(18, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    while True:
        print("Waiting for button press...")
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
```

**3. Run:**
```bash
nano button_interrupt.py
# Paste code
python3 button_interrupt.py
```

**4. Test:**
- Press button
- Should trigger interrupt callback

**Expected Behavior:**
- Interrupt triggers on button press
- Bounce time prevents multiple triggers
- Main loop continues while waiting

**Troubleshooting:**
- Multiple triggers: Increase bouncetime
- No interrupt: Check GPIO pin, check edge detection
- Interrupt not triggering: Check pull-up configuration

**Completion Criteria:**
- Interrupt works reliably
- Bounce time prevents false triggers
- Event-driven programming demonstrated

---

### Lab 5: I2C Sensor Reading
**Objective:** Read I2C sensor (e.g., BME280).

**Prerequisites:**
- Completed Lab 1
- I2C sensor module

**Components:**
- Raspberry Pi
- I2C sensor (BME280 or similar)
- Jumper wires

**Procedure:**

**1. Enable I2C:**
```bash
sudo raspi-config
# Interface Options → I2C → Enable
sudo reboot
```

**2. Install I2C tools:**
```bash
sudo apt install i2c-tools python3-smbus
```

**3. Connect Sensor:**
- VCC to 3.3V
- GND to GND
- SDA to GPIO2 (SDA)
- SCL to GPIO3 (SCL)

**4. Detect I2C Device:**
```bash
sudo i2cdetect -y 1
```

**5. Python Code:**
```python
#!/usr/bin/env python3
import smbus
import time

bus = smbus.SMBus(1)
address = 0x76  # BME280 address

try:
    while True:
        # Read from sensor (simplified example)
        data = bus.read_i2c_block_data(address, 0x00, 8)
        print(f"Raw data: {data}")
        time.sleep(1)
except KeyboardInterrupt:
    pass
```

**Expected Behavior:**
- I2C device detected
- Data read from sensor
- No communication errors

**Troubleshooting:**
- Device not detected: Check wiring, check address, check I2C enabled
- Read errors: Check sensor documentation, check I2C speed
- Permission denied: Add user to i2c group

**Completion Criteria:**
- I2C device detected
- Data read successfully
- I2C communication understood

---

### Lab 6: SPI Communication
**Objective:** Communicate with SPI device.

**Prerequisites:**
- Completed Lab 1
- SPI device or SPI sensor

**Components:**
- Raspberry Pi
- SPI device
- Jumper wires

**Procedure:**

**1. Enable SPI:**
```bash
sudo raspi-config
# Interface Options → SPI → Enable
sudo reboot
```

**2. Install SPI library:**
```bash
sudo apt install python3-spidev
```

**3. Connect Device:**
- MOSI to GPIO10 (MOSI)
- MISO to GPIO9 (MISO)
- SCLK to GPIO11 (SCLK)
- CS to GPIO8 (CE0)
- VCC to 3.3V
- GND to GND

**4. Python Code:**
```python
#!/usr/bin/env python3
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

try:
    while True:
        resp = spi.xfer2([0x00, 0x00])
        print(f"SPI response: {resp}")
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    spi.close()
```

**Expected Behavior:**
- SPI communication established
- Data exchanged
- No communication errors

**Troubleshooting:**
- No communication: Check wiring, check SPI enabled, check chip select
- Wrong data: Check SPI mode, check byte order
- Permission denied: Add user to spi group

**Completion Criteria:**
- SPI communication working
- Data read/written successfully
- SPI protocol understood

---

### Lab 7: UART Communication
**Objective:** Communicate via UART.

**Prerequisites:**
- Completed Lab 1
- UART device or USB-TTL adapter

**Components:**
- Raspberry Pi
- UART device or USB-TTL adapter
- Jumper wires

**Procedure:**

**1. Enable Serial:**
```bash
sudo raspi-config
# Interface Options → Serial Port
# Enable serial port hardware
# Disable serial console (if using for UART)
sudo reboot
```

**2. Install serial library:**
```bash
sudo apt install python3-serial
```

**3. Connect Device:**
- TXD (GPIO14) to device RX
- RXD (GPIO15) to device TX
- GND to device GND

**4. Python Code:**
```python
#!/usr/bin/env python3
import serial

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

try:
    while True:
        ser.write(b'Hello\n')
        data = ser.readline()
        if data:
            print(f"Received: {data}")
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    ser.close()
```

**Expected Behavior:**
- UART communication established
- Data sent and received
- No communication errors

**Troubleshooting:**
- No communication: Check TX/RX cross-connection, check baud rate, check serial enabled
- Garbage data: Check baud rate match, check data format
- Permission denied: Add user to dialout group

**Completion Criteria:**
- UART communication working
- Data exchanged successfully
- UART protocol understood

---

### Lab 8: systemd Service
**Objective:** Create auto-start service.

**Prerequisites:**
- Completed Lab 2

**Components:**
- Raspberry Pi
- LED circuit from Lab 2

**Procedure:**

**1. Create Service File:**
```bash
sudo nano /etc/systemd/system/led-blink.service
```

**2. Service Content:**
```ini
[Unit]
Description=LED Blink Service
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi
ExecStart=/usr/bin/python3 /home/pi/led_blink.py
Restart=always

[Install]
WantedBy=multi-user.target
```

**3. Enable and Start:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable led-blink.service
sudo systemctl start led-blink.service
sudo systemctl status led-blink.service
```

**4. View Logs:**
```bash
journalctl -u led-blink.service -f
```

**Expected Behavior:**
- Service starts on boot
- Service auto-restarts on failure
- Logs are viewable

**Troubleshooting:**
- Service fails to start: Check ExecStart path, check permissions
- Service not starting on boot: Check enable status
- No logs: Check journal configuration

**Completion Criteria:**
- Service auto-starts on boot
- Service restarts on failure
- Logs are accessible

---

### Lab 9: MQTT Gateway
**Objective:** Implement MQTT gateway functionality.

**Prerequisites:**
- Completed Lab 1
- Completed Phase 10 (MQTT and IoT)

**Components:**
- Raspberry Pi
- MQTT client (ESP32 or simulation)

**Procedure:**

**1. Install Mosquitto:**
```bash
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

**2. Install Python MQTT Library:**
```bash
sudo apt install python3-pip
pip3 install paho-mqtt
```

**3. Python Gateway Code:**
```python
#!/usr/bin/env python3
import paho.mqtt.client as mqtt

# MQTT broker settings
BROKER = "localhost"
PORT = 1883

# Callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("sensor/#")

def on_message(client, userdata, msg):
    print(f"Received: {msg.topic} {msg.payload}")
    # Forward to cloud or process

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
    client.loop_forever()
except KeyboardInterrupt:
    pass
finally:
    client.disconnect()
```

**4. Run:**
```bash
nano mqtt_gateway.py
# Paste code
python3 mqtt_gateway.py
```

**5. Test:**
- Publish test message: `mosquitto_pub -t sensor/test -m "hello"`
- Should receive message

**Expected Behavior:**
- MQTT broker running
- Gateway subscribes to topics
- Messages received and processed

**Troubleshooting:**
- Cannot connect: Check Mosquitto running, check firewall
- No messages: Check topic subscription, check publish command
- Connection lost: Check network, check broker configuration

**Completion Criteria:**
- MQTT broker operational
- Gateway subscribes and receives
- Protocol translation demonstrated

---

### Lab 10: ESP32 UART Integration
**Objective:** Communicate with ESP32 via UART.

**Prerequisites:**
- Completed Lab 7
- ESP32 with UART code

**Components:**
- Raspberry Pi
- ESP32
- Jumper wires

**Procedure:**

**1. ESP32 Code (Phase 6 knowledge):**
```cpp
#include <HardwareSerial.h>

HardwareSerial Serial1(1); // UART1

void setup() {
  Serial1.begin(115200, SERIAL_8N1, 16, 17); // RX=16, TX=17
}

void loop() {
  Serial1.println("Hello from ESP32");
  delay(1000);
}
```

**2. Connect ESP32 to Raspberry Pi:**
- ESP32 TX (GPIO17) to Raspberry Pi RX (GPIO15)
- ESP32 RX (GPIO16) to Raspberry Pi TX (GPIO14)
- GND to GND

**3. Raspberry Pi Receiver Code:**
```python
#!/usr/bin/env python3
import serial

ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)

try:
    while True:
        data = ser.readline()
        if data:
            print(f"Received: {data.decode().strip()}")
except KeyboardInterrupt:
    pass
finally:
    ser.close()
```

**4. Run:**
```bash
python3 esp32_uart.py
```

**Expected Behavior:**
- ESP32 sends data via UART
- Raspberry Pi receives data
- Data displayed correctly

**Troubleshooting:**
- No data: Check wiring, check baud rate match, check serial enabled
- Garbage data: Check baud rate, check data format
- Permission denied: Add user to dialout group

**Completion Criteria:**
- ESP32-Raspberry Pi UART communication working
- Data received correctly
- Integration architecture understood

---

### Lab 11: Headless Configuration
**Objective:** Configure Raspberry Pi for reliable headless operation.

**Prerequisites:**
- Completed Lab 1

**Components:**
- Raspberry Pi
- Network connection

**Procedure:**

**1. Configure Static IP:**
```bash
sudo nano /etc/dhcpcd.conf
```

**Add:**
```
interface eth0
static ip_address=192.168.1.100/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

**2. Enable SSH Key Authentication:**
```bash
# On computer
ssh-keygen -t rsa
ssh-copy-id pi@raspberrypi.local

# On Raspberry Pi
sudo nano /etc/ssh/sshd_config
# Set: PasswordAuthentication no
sudo systemctl restart ssh
```

**3. Configure Serial Console for Recovery:**
```bash
sudo raspi-config
# Interface Options → Serial Port
# Enable serial console hardware
# Enable serial console
```

**4. Install Watchdog:**
```bash
sudo apt install watchdog
sudo nano /etc/watchdog.conf
# Uncomment: max-load-1 = 24
# Uncomment: watchdog-device = /dev/watchdog
sudo systemctl enable watchdog
sudo systemctl start watchdog
```

**5. Test:**
- Reboot Raspberry Pi
- Connect via SSH key (no password)
- Verify static IP
- Verify watchdog running

**Expected Behavior:**
- Static IP assigned
- SSH key authentication works
- Serial console available for recovery
- Watchdog monitoring system

**Troubleshooting:**
- Cannot connect after static IP: Check IP range, check network
- SSH key not working: Check permissions, check sshd_config
- Watchdog not running: Check configuration, check kernel support

**Completion Criteria:**
- Static IP configured
- SSH key authentication working
- Recovery methods available
- Watchdog monitoring active

---

### Lab 12: Troubleshooting
**Objective:** Diagnose and fix common Raspberry Pi issues.

**Prerequisites:**
- Completed previous labs

**Components:**
- Raspberry Pi
- Various components from previous labs

**Procedure:**

**1. Power Supply Test:**
- Check voltage between 5V and GND pins
- Should be 4.8-5.2V under load
- Symptoms of low power: random reboots, USB failures, undervoltage icon

**2. SD Card Health:**
```bash
sudo dmesg | grep -i mmc
sudo fsck /dev/mmcblk0p2
```

**3. GPIO Test:**
```bash
gpioinfo
gpioset --mode=time 17 1
```

**4. Network Test:**
```bash
ip addr
ping -c 4 8.8.8.8
```

**5. System Logs:**
```bash
journalctl -xe
dmesg | tail
```

**6. Temperature Check:**
```bash
vcgencmd measure_temp
```

**Expected Behavior:**
- Power supply voltage adequate
- SD card healthy
- GPIO functional
- Network operational
- Logs show no critical errors
- Temperature within safe range

**Troubleshooting:**
- Low voltage: Replace power supply, check cable
- SD card errors: Replace SD card, check corruption
- GPIO issues: Check configuration, check hardware
- Network issues: Check cable, check router
- High temperature: Improve cooling, check workload

**Completion Criteria:**
- System health verified
- Common issues diagnosed
- Troubleshooting methods understood

---

## Project

### Project: Raspberry Pi Gateway

**Objective:** Build a Raspberry Pi IoT gateway that collects data from ESP32 nodes, processes it locally, and forwards to MQTT broker.

**Requirements:**
- Collect data from multiple ESP32 nodes via UART or MQTT
- Process and aggregate data
- Forward to MQTT broker
- Local data buffering
- Web interface for monitoring
- Auto-restart on failure
- Headless operation

**Implementation:**
- Python for gateway logic
- systemd for service management
- Mosquitto for MQTT
- Flask for web interface (optional)
- SQLite for local buffering

**Deliverables:**
- Working gateway service
- Configuration documentation
- Testing documentation
- Troubleshooting guide

**Time Estimate:** 8-12 hours

**Project Structure:**
```
raspberry-pi-gateway/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   ├── gateway.py
│   ├── config.py
│   └── web_interface.py (optional)
├── tests/
│   └── test_gateway.py
├── docs/
│   └── architecture.md
└── results/
    └── measurements.md
```

**Note:** This project teaches Raspberry Pi gateway architecture, MQTT integration, and reliable embedded Linux system design.

---

## Common Mistakes

### Mistake 1: Connecting 5V to GPIO
**Problem:** Connecting 5V devices directly to 3.3V GPIO pins
**Consequence:** GPIO pin damage
**Solution:** Use level shifters for 5V devices

### Mistake 2: Exceeding Current Limits
**Problem:** Drawing too much current from GPIO pins
**Consequence:** GPIO damage or unreliable operation
**Solution:** Respect 16mA per pin, 50mA total limit

### Mistake 3: No Current-Limiting Resistor
**Problem:** Connecting LED directly to GPIO
**Consequence:** LED damage, GPIO damage
**Solution:** Always use current-limiting resistor (220Ω typical)

### Mistake 4: Floating Inputs
**Problem:** Unconfigured input pins float randomly
**Consequence:** Unreliable readings
**Solution:** Always configure pull-up or pull-down

### Mistake 5: Forgetting GPIO Cleanup
**Problem:** GPIO configuration persists after program exit
**Consequence:** Conflicts with other programs
**Solution:** Always use GPIO cleanup in finally block

### Mistake 6: Insufficient Power Supply
**Problem:** Using inadequate power supply
**Consequence:** Random reboots, USB failures, undervoltage
**Solution:** Use official Raspberry Pi power supply (5V, 2.5A+)

### Mistake 7: Poor SD Card Quality
**Problem:** Using low-quality SD card
**Consequence:** Corruption, slow performance, failures
**Solution:** Use high-quality name-brand SD card

### Mistake 8: Not Enabling Interfaces
**Problem:** Trying to use I2C/SPI/UART without enabling
**Consequence:** Communication failures
**Solution:** Enable interfaces in raspi-config

### Mistake 9: Wrong Baud Rate
**Problem:** Mismatched baud rate in UART
**Consequence:** Garbage data or no communication
**Solution:** Match baud rate on both devices

### Mistake 10: No Recovery Method
**Problem:** Headless system with no recovery method
**Consequence:** Cannot recover from failure
**Solution:** Enable serial console, keep SSH backup

---

## Safety Notes

**Electrical Safety:**
- Raspberry Pi operates at 5V input, 3.3V GPIO
- Do not connect mains voltage directly
- Use proper power supply
- Check polarity before connecting
- Use current-limiting resistors

**GPIO Safety:**
- 3.3V logic levels only
- Do not exceed 16mA per pin
- Do not exceed 50mA total
- Use level shifters for 5V devices
- Respect current limits

**Power Safety:**
- Use official Raspberry Pi power supply
- Check voltage under load
- Avoid powering high-current devices from GPIO
- Use external power for motors/actuators

**Data Safety:**
- Backup SD card regularly
- Use quality SD cards
- Safely shutdown before power off
- Monitor disk space

**Linux Safety:**
- Careful with rm -rf commands
- Backup configuration files before editing
- Test changes in non-critical environment
- Keep recovery methods available

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is the difference between SBC and MCU?
2. When would you choose Raspberry Pi over ESP32?
3. What is the GPIO logic voltage level of Raspberry Pi?
4. What is the maximum current per GPIO pin?
5. What is the purpose of a pull-up resistor?
6. What is the difference between I2C and SPI?
7. What is PWM?
8. What is the difference between hardware and software PWM?
9. How do you enable I2C on Raspberry Pi?
10. How do you create a systemd service?
11. What is the role of an MQTT gateway?
12. How do you enable SSH headless?
13. What is the serial console used for?
14. What is watchdog used for?
15. How do you configure pull-up in Python RPi.GPIO?
16. What is the difference between RPi.GPIO and gpiozero?
17. What is libgpiod?
18. How do you detect I2C devices?
19. What are symptoms of insufficient power?
20. How do you troubleshoot GPIO issues?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **OS Setup:** Install Raspberry Pi OS headless, enable SSH, configure Wi-Fi
2. **GPIO Output:** Blink LED using GPIO
3. **GPIO Input:** Read button with pull-up resistor
4. **Interrupts:** Use GPIO interrupt for button press
5. **I2C:** Read I2C sensor data
6. **SPI:** Communicate with SPI device
7. **UART:** Communicate with UART device
8. **Service:** Create systemd service that auto-starts
9. **MQTT:** Implement MQTT gateway that subscribes and publishes
10. **Headless:** Configure static IP, SSH key authentication, watchdog

**Documentation Required:**
- Circuit diagrams
- Code listings
- Test results
- Configuration files
- Troubleshooting notes

**Passing Criteria:** All tasks completed with understanding demonstrated.

---

## Completion Checklist

Before moving to Phase 13, verify you have:

- [ ] Understand Raspberry Pi architecture (SBC vs MCU)
- [ ] Can install and configure Raspberry Pi OS headless
- [ ] Can use GPIO for digital input/output
- [ ] Can configure pull-up/pull-down resistors
- [ ] Can use GPIO interrupts
- [ ] Can implement PWM
- [ ] Can use I2C communication
- [ ] Can use SPI communication
- [ ] Can use UART communication
- [ ] Can create systemd services
- [ ] Can implement MQTT gateway
- [ ] Can integrate ESP32 with Raspberry Pi
- [ ] Can configure headless operation
- [ ] Can troubleshoot Raspberry Pi issues
- **Completed Lab 1** - Raspberry Pi OS Setup
- **Completed Lab 2** - GPIO Digital Output
- **Completed Lab 3** - GPIO Digital Input with Pull-up
- **Completed Lab 4** - GPIO Interrupts
- **Completed Lab 5** - I2C Sensor Reading
- **Completed Lab 6** - SPI Communication
- **Completed Lab 7** - UART Communication
- **Completed Lab 8** - systemd Service
- **Completed Lab 9** - MQTT Gateway
- **Completed Lab 10** - ESP32 UART Integration
- **Completed Lab 11** - Headless Configuration
- **Completed Lab 12** - Troubleshooting
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Completed the Raspberry Pi Gateway project

---

## Do Not Continue Until...

**Do not start Phase 13 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can install and configure Raspberry Pi OS headless
5. You can use GPIO for digital I/O and interrupts
6. You can use I2C, SPI, and UART communication
7. You can create systemd services
8. You can implement MQTT gateway functionality
9. You can integrate ESP32 with Raspberry Pi
10. You can configure headless operation with recovery methods
11. You can troubleshoot Raspberry Pi hardware and software issues

**Raspberry Pi provides the Linux foundation for embedded gateway applications. Mastering Raspberry Pi GPIO, communication interfaces, and system management is essential before learning advanced debugging techniques.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 13 — Debugging**

Phase 13 will teach you systematic debugging methodologies, tools, and techniques for embedded systems, building on the hardware and software knowledge you have acquired so far.

---

**Raspberry Pi serves as a bridge between MCU-level embedded systems and cloud/networked applications. Understanding Raspberry Pi hardware, GPIO, communication interfaces, and Linux system management is critical for building IoT gateways and embedded Linux applications.**
