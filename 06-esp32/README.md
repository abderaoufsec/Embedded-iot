# Phase 6 — ESP32 Embedded Development

> **Goal:** Apply the universal MCU concepts from Phase 5 to practical ESP32 development using both Arduino-ESP32 and ESP-IDF frameworks.
>
> **Prerequisite:** Phase 5 — Microcontrollers
>
> **Outcome:** You can develop ESP32 firmware, use GPIO/ADC/PWM/UART/I2C/SPI, connect to Wi-Fi, understand the difference between Arduino and ESP-IDF, and debug ESP32 applications.

---

## What You Will Learn

By completing this phase, you will understand:

- **Universal MCU concepts applied to ESP32:** How the architecture from Phase 5 maps to a real MCU
- **ESP32-specific features:** Dual-core Xtensa processors, Wi-Fi, Bluetooth, specific peripherals
- **Development environments:** Arduino-ESP32 vs ESP-IDF and when to use each
- **Toolchain:** Source code → compilation → linking → firmware → flashing → execution
- **GPIO:** Digital I/O, pull-up/pull-down, safe usage (ESP32-specific limits)
- **PWM:** LED brightness control, frequency, duty cycle (ESP32 LEDC)
- **ADC:** Analog input, ESP32 ADC limitations, voltage interpretation
- **UART:** Serial communication, debugging, TX/RX
- **I2C:** SDA/SCL, addresses, pull-ups, sensor communication
- **SPI:** SCK/MOSI/MISO/CS, high-speed communication
- **Wi-Fi:** Station mode, AP mode, DHCP/IP, network connection
- **BLE:** Basic concepts, GATT/GAP at introductory level
- **NVS:** Non-volatile storage for configuration persistence
- **OTA:** Firmware update concepts and safe workflow
- **Debugging:** Serial logs, common flashing/boot problems, troubleshooting

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phase 0 — Orientation
- ✅ Completed Phase 1 — Computer Fundamentals
- ✅ Completed Phase 2 — C Programming
- ✅ Completed Phase 3 — Digital Electronics
- ✅ Completed Phase 4 — Electronics
- ✅ Completed Phase 5 — Microcontrollers
- ✅ Understanding of MCU architecture (from Phase 5)
- ✅ Understanding of memory-mapped I/O (from Phase 5)
- ✅ Understanding of interrupts and polling (from Phase 5)
- ✅ Understanding of GPIO, timers, ADC, PWM concepts (from Phase 5)
- ✅ Understanding of UART, I2C, SPI concepts (from Phase 5)

**Hardware required:**
- ESP32 development board (e.g., ESP32 DevKit, NodeMCU-ESP32, or similar)
- USB cable for programming and power
- LED and resistor (220Ω or 330Ω)
- Push button
- Potentiometer (10kΩ)
- I2C sensor (e.g., OLED display, temperature sensor)
- Breadboard and jumper wires
- Multimeter

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain how ESP32 implements the universal MCU concepts from Phase 5
- Distinguish between universal embedded concepts and ESP32-specific behavior
- Set up Arduino-ESP32 development environment
- Set up ESP-IDF development environment
- Understand the differences between Arduino and ESP-IDF frameworks
- Configure and use ESP32 GPIO safely
- Implement PWM for LED brightness control
- Read analog sensors using ESP32 ADC
- Use UART for serial communication and debugging
- Communicate with I2C devices
- Communicate with SPI devices
- Connect ESP32 to Wi-Fi networks
- Implement basic BLE functionality
- Use NVS for persistent configuration storage
- Understand OTA firmware update concepts
- Debug common ESP32 problems (flashing, boot, GPIO, power)
- Choose between Arduino-ESP32 and ESP-IDF for different applications

---

## Concepts

### Universal MCU Concepts Applied to ESP32

**From Phase 5, you learned:**
- CPU, memory, peripherals
- Memory-mapped I/O
- Registers and register maps
- Interrupts and polling
- Timers, PWM, ADC
- Communication protocols (UART, I2C, SPI)

**ESP32 Implementation:**
- **CPU:** Dual-core Xtensa LX6 (32-bit), not ARM Cortex-M
- **Memory:** 520KB SRAM, external Flash (4MB typical)
- **Peripherals:** Similar concepts but ESP32-specific registers and APIs
- **Communication:** Same protocols but ESP32-specific hardware controllers

**Key Point:** The concepts are universal, but the implementation details (register addresses, APIs, capabilities) vary by MCU. ESP32 implements these concepts differently than STM32 or other MCUs.

### ESP32 Overview

**What is ESP32:**
- System-on-chip (SoC) by Espressif
- Dual-core Xtensa LX6 processor (240MHz typical)
- Integrated Wi-Fi (802.11 b/g/n)
- Integrated Bluetooth (Classic + BLE)
- Rich peripheral set (GPIO, ADC, DAC, PWM, UART, I2C, SPI, I2S, etc.)
- Low power consumption
- Low cost

**Universal vs ESP32-Specific:**
- **Universal:** Has CPU, memory, GPIO, timers, ADC, communication protocols (like any MCU)
- **ESP32-Specific:** Dual-core Xtensa (not ARM), integrated Wi-Fi/BLE, specific peripheral capabilities, ESP-IDF SDK

**Why this matters:** You apply the universal concepts from Phase 5 to a real MCU, while learning ESP32-specific details that differ from other platforms.

### CPU and Memory Overview

**CPU (ESP32-Specific):**
- Dual-core Xtensa LX6 (32-bit RISC)
- Each core can run at up to 240MHz
- Cores can execute code independently
- Note: Different from ARM Cortex-M architecture used in STM32

**Memory (ESP32-Specific):**
- **SRAM:** 520KB internal (divided between instructions and data)
- **Flash:** External (4MB typical), stores firmware
- **ROM:** Boot ROM contains boot code
- **RTC Memory:** Low-power memory for RTC functions

**Universal Concept:** Memory organization (Flash for code, SRAM for data) is universal. ESP32 specifics (sizes, layout) vary from other MCUs.

**Why this matters:** Understanding ESP32's memory layout helps you understand code placement, stack/heap usage, and firmware size limitations.

### GPIO Overview

**Universal Concept (from Phase 5):**
- GPIO pins can be inputs or outputs
- Memory-mapped registers control GPIO
- Pull-up/pull-down resistors prevent floating inputs

**ESP32-Specific:**
- ~30 GPIO pins (varies by board)
- 3.3V logic levels (not 5V tolerant on most pins)
- Maximum current per pin: ~40mA (check specific board)
- Total current limit: ~1200mA for all GPIO combined
- Strapping pins have special functions at boot
- Some pins are input-only or output-only
- RTC GPIOs can wake from deep sleep

**Safe Usage:**
- Never apply 5V to ESP32 GPIO (will damage the chip)
- Don't exceed per-pin current limit (~40mA)
- Don't exceed total GPIO current limit (~1200mA)
- Use current-limiting resistors with LEDs
- Check datasheet for your specific ESP32 board variant

**Why this matters:** GPIO limits are MCU-specific. ESP32 has different limits than STM32 or other MCUs. Exceeding these limits can damage the chip.

### Peripherals Overview

**Universal Concepts (from Phase 5):**
- Timers for timing and PWM
- ADC for analog input
- DAC for analog output
- UART, I2C, SPI for communication
- Interrupt controller for event handling

**ESP32-Specific Implementation:**
- **Timers:** 4 hardware timers, LEDC controller for PWM
- **ADC:** 2 SAR ADC units, 12-bit resolution, specific channels
- **DAC:** 2 DAC channels (8-bit)
- **UART:** 3 UART controllers
- **I2C:** 2 I2C controllers
- **SPI:** 4 SPI controllers (SPI + 3 HSPI)
- **Interrupt Controller:** Xtensa interrupt architecture

**Why this matters:** The concepts are universal, but ESP32 has specific capabilities, limitations, and APIs. You need to understand both the universal concepts and ESP32-specific implementation.

### Development Environments

**Arduino-ESP32:**
- **What it is:** Arduino framework ported to ESP32
- **Pros:** Easy to use, large community, many libraries, simple API
- **Cons:** Less control over hardware, limited to Arduino capabilities, less efficient
- **When to use:** Quick prototyping, simple projects, when Arduino libraries are needed
- **Universal vs Specific:** Arduino provides MCU-agnostic API, but ESP32-specific features may not be exposed

**ESP-IDF (Espressif IoT Development Framework):**
- **What it is:** Official Espressif framework for ESP32
- **Pros:** Full hardware access, optimized performance, all features available, freeRTOS-based
- **Cons:** More complex, steeper learning curve, more verbose code
- **When to use:** Production applications, when full hardware access is needed, optimized performance
- **Universal vs Specific:** ESP-IDF is ESP32-specific, not portable to other MCUs

**Key Difference:** Arduino provides abstraction (easier, less control), ESP-IDF provides direct access (harder, more control). This is a universal trade-off, but the specific frameworks are ESP32-specific.

**Why this matters:** Choosing the right framework affects development complexity, performance, and capabilities. Understanding both helps you make informed decisions.

### Toolchain Overview

**Universal Concept (from Phase 5):**
- Source code → Preprocess → Compile → Assemble → Link → Firmware → Flash → Boot → Execute

**ESP32-Specific Toolchain:**

**Arduino-ESP32 Toolchain:**
- Arduino IDE manages toolchain automatically
- Compiles C++ code (Arduino uses C++, not pure C)
- Links with Arduino libraries
- Generates firmware image (.bin)
- Flashes via esptool
- Serial monitor for debugging

**ESP-IDF Toolchain:**
- Xtensa toolchain (not ARM toolchain)
- CMake build system
- IDF.py or idf.py build command
- Generates multiple binary files (app, bootloader, partition table)
- Flashes via esptool.py
- Monitor for debugging

**Why this matters:** The build process is universal, but ESP32 uses a different toolchain (Xtensa vs ARM) and different build systems. Understanding the toolchain helps you troubleshoot build problems.

### GPIO in Practice

**Universal Concept (from Phase 5):**
- Configure direction (input/output)
- Set output value
- Read input value
- Use pull-up/pull-down resistors

**Arduino-ESP32 Implementation:**
```cpp
// Set pin as output
pinMode(5, OUTPUT);

// Set pin HIGH
digitalWrite(5, HIGH);

// Set pin as input with pull-up
pinMode(4, INPUT_PULLUP);

// Read pin
int value = digitalRead(4);
```

**ESP-IDF Implementation:**
```c
// Configure GPIO as output
gpio_config_t io_conf = {
    .pin_bit_mask = (1ULL << GPIO_NUM_5),
    .mode = GPIO_MODE_OUTPUT,
    .pull_up_en = GPIO_PULLUP_DISABLE,
    .pull_down_en = GPIO_PULLDOWN_DISABLE,
    .intr_type = GPIO_INTR_DISABLE
};
gpio_config(&io_conf);

// Set pin HIGH
gpio_set_level(GPIO_NUM_5, 1);

// Configure GPIO as input with pull-up
io_conf.mode = GPIO_MODE_INPUT;
io_conf.pull_up_en = GPIO_PULLUP_ENABLE;
gpio_config(&io_conf);

// Read pin
int value = gpio_get_level(GPIO_NUM_4);
```

**ESP32-Specific Notes:**
- Pin numbers vary by board (use GPIO_NUM_X constants in ESP-IDF)
- Some pins have restrictions (strapping pins, input-only, etc.)
- Always check your board's pinout diagram

**Why this matters:** Arduino provides simple API, ESP-IDF provides direct register access. Understanding both helps you work with either framework.

### PWM in Practice

**Universal Concept (from Phase 5):**
- PWM varies duty cycle to control average voltage
- Used for LED brightness, motor speed, etc.
- Frequency and duty cycle are key parameters

**ESP32-Specific Implementation (LEDC):**
- ESP32 uses LEDC (LED Control) peripheral for PWM
- 16 channels, 8 timers
- Resolution configurable (1-16 bits)
- Frequency configurable (up to ~40MHz)

**Arduino-ESP32:**
```cpp
// Setup PWM on channel 0, pin 5, 5000Hz, 8-bit resolution
ledcSetup(0, 5000, 8);

// Attach PWM channel to pin
ledcAttachPin(5, 0);

// Set duty cycle (0-255 for 8-bit)
ledcWrite(0, 128);  // 50% duty cycle
```

**ESP-IDF:**
```c
// Configure LEDC timer
ledc_timer_config_t timer_conf = {
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .duty_resolution = LEDC_TIMER_8_BIT,
    .timer_num = LEDC_TIMER_0,
    .freq_hz = 5000,
    .clk_cfg = LEDC_AUTO_CLK
};
ledc_timer_config(&timer_conf);

// Configure LEDC channel
ledc_channel_config_t channel_conf = {
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .channel = LEDC_CHANNEL_0,
    .timer_sel = LEDC_TIMER_0,
    .intr_type = LEDC_INTR_DISABLE,
    .gpio_num = GPIO_NUM_5,
    .duty = 0,
    .hpoint = 0
};
ledc_channel_config(&channel_conf);

// Set duty cycle
ledc_set_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_0, 128);
ledc_update_duty(LEDC_LOW_SPEED_MODE, LEDC_CHANNEL_0);
```

**Why this matters:** ESP32's LEDC peripheral is ESP32-specific. Understanding it allows you to use PWM effectively. Arduino abstracts this, ESP-IDF requires explicit configuration.

### ADC in Practice

**Universal Concept (from Phase 5):**
- ADC converts analog voltage to digital value
- Resolution determines precision
- Voltage range determines input range

**ESP32-Specific Limitations:**
- 12-bit resolution (0-4095)
- Non-linear behavior (especially at low voltages)
- Attenuation settings for different voltage ranges
- Specific ADC channels per GPIO pin
- Noise and variability between units

**Voltage Ranges (ESP32-Specific):**
- 0dB attenuation: 0-1.1V
- 2.5dB attenuation: 0-1.5V
- 6dB attenuation: 0-2.2V
- 11dB attenuation: 0-3.3V

**Arduino-ESP32:**
```cpp
// Read ADC on pin 34 (ADC1_CH6)
int value = analogRead(34);

// Convert to voltage (assuming 3.3V max)
float voltage = value * 3.3 / 4095.0;
```

**ESP-IDF:**
```c
// Configure ADC
adc1_config_width(ADC_WIDTH_BIT_12);
adc1_config_channel_atten(ADC1_CHANNEL_6, ADC_ATTEN_DB_11);

// Read ADC
int value = adc1_get_raw(ADC1_CHANNEL_6);

// Convert to voltage
float voltage = value * 3.3 / 4095.0;
```

**ESP32-Specific Notes:**
- ADC is non-linear, especially at low voltages
- Calibration may be needed for accurate measurements
- WiFi and Bluetooth can affect ADC readings
- Some pins are ADC1 only, some are ADC2 only

**Why this matters:** ESP32's ADC has specific limitations and non-linear behavior. Understanding these limitations is essential for accurate sensor readings.

### UART in Practice

**Universal Concept (from Phase 5):**
- UART is serial communication
- TX (transmit), RX (receive)
- Baud rate, data bits, parity, stop bits
- Point-to-point communication

**ESP32-Specific:**
- 3 UART controllers (UART0, UART1, UART2)
- UART0 used for USB programming/debugging
- Baud rates up to 5Mbps
- Hardware flow control available (RTS/CTS)

**Arduino-ESP32:**
```cpp
// Initialize Serial (UART0 for USB)
Serial.begin(115200);

// Send data
Serial.println("Hello ESP32");

// Receive data
if (Serial.available()) {
    char c = Serial.read();
}

// Use UART1 on specific pins
Serial1.begin(115200, SERIAL_8N1, 16, 17);
```

**ESP-IDF:**
```c
// Configure UART
uart_config_t uart_config = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE
};
uart_param_config(UART_NUM_1, &uart_config);
uart_driver_install(UART_NUM_1, 256, 0, 0, NULL, 0);

// Send data
uart_write_bytes(UART_NUM_1, "Hello ESP32", 12, portMAX_DELAY);

// Receive data
uint8_t data[256];
int len = uart_read_bytes(UART_NUM_1, data, 256, 100 / portTICK_PERIOD_MS);
```

**Why this matters:** UART is essential for debugging and communication. ESP32 has specific UART controllers and pin assignments. Arduino abstracts this, ESP-IDF requires explicit configuration.

### I2C in Practice

**Universal Concept (from Phase 5):**
- I2C is two-wire serial bus (SDA, SCL)
- Master-slave architecture
- Devices have addresses
- Requires pull-up resistors

**ESP32-Specific:**
- 2 I2C controllers (I2C0, I2C1)
- 400kHz (Fast Mode) or 1MHz (Fast Mode Plus)
- Specific GPIO pins for I2C
- Hardware pull-ups available on some pins

**Arduino-ESP32:**
```cpp
#include <Wire.h>

// Initialize I2C
Wire.begin(21, 22);  // SDA=21, SCL=22

// Write to device
Wire.beginTransmission(0x48);  // Device address
Wire.write(0x00);              // Register address
Wire.write(0x01);              // Data
Wire.endTransmission();

// Read from device
Wire.requestFrom(0x48, 1);
byte data = Wire.read();
```

**ESP-IDF:**
```c
// Configure I2C
i2c_config_t conf = {
    .mode = I2C_MODE_MASTER,
    .sda_io_num = GPIO_NUM_21,
    .scl_io_num = GPIO_NUM_22,
    .sda_pullup_en = GPIO_PULLUP_ENABLE,
    .scl_pullup_en = GPIO_PULLUP_ENABLE,
    .master.clk_speed = 400000
};
i2c_param_config(I2C_NUM_0, &conf);
i2c_driver_install(I2C_NUM_0, &conf, 0, 0, 0);

// Write to device
uint8_t data[2] = {0x00, 0x01};
i2c_master_write_to_device(I2C_NUM_0, 0x48, data, 2, 1000 / portTICK_PERIOD_MS);

// Read from device
uint8_t data_read;
i2c_master_read_from_device(I2C_NUM_0, 0x48, &data_read, 1, 1000 / portTICK_PERIOD_MS);
```

**ESP32-Specific Notes:**
- Some boards have built-in pull-ups on I2C pins
- Default I2C pins: SDA=GPIO21, SCL=GPIO22 (can be reassigned)
- Scan I2C bus to find connected devices

**Why this matters:** I2C is essential for sensor communication. ESP32 has specific I2C controllers and pin assignments. Understanding these is essential for connecting I2C devices.

### SPI in Practice

**Universal Concept (from Phase 5):**
- SPI is high-speed serial bus
- SCK (clock), MOSI (master out slave in), MISO (master in slave out), CS (chip select)
- Master-slave architecture
- Full-duplex communication

**ESP32-Specific:**
- 4 SPI controllers (SPI, HSPI, VSPI, reserved)
- Up to 80MHz clock speed
- Specific GPIO pins for SPI
- SPI and I2S share pins

**Arduino-ESP32:**
```cpp
#include <SPI.h>

// Initialize SPI
SPI.begin(18, 19, 23, 5);  // SCK=18, MISO=19, MOSI=23, CS=5

// Select device
digitalWrite(5, LOW);

// Transfer data
uint8_t data = SPI.transfer(0x00);

// Deselect device
digitalWrite(5, HIGH);
```

**ESP-IDF:**
```c
// Configure SPI
spi_bus_config_t bus_config = {
    .mosi_io_num = GPIO_NUM_23,
    .miso_io_num = GPIO_NUM_19,
    .sclk_io_num = GPIO_NUM_18,
    .quadwp_io_num = -1,
    .quadhd_io_num = -1
};
spi_bus_initialize(HSPI_HOST, &bus_config, 1);

spi_device_interface_config_t dev_config = {
    .clock_speed_hz = 1000000,
    .mode = 0,
    .spics_io_num = GPIO_NUM_5,
    .queue_size = 7
};
spi_bus_add_device(HSPI_HOST, &dev_config, &spi_handle);

// Transfer data
spi_transaction_t trans = {
    .length = 8,
    .flags = 0
};
spi_device_polling_transmit(spi_handle, &trans);
```

**Why this matters:** SPI is used for high-speed communication with displays, sensors, and storage. ESP32 has specific SPI controllers and pin assignments.

### Wi-Fi Overview

**Universal Concept (from Phase 4):**
- Network communication
- IP addresses
- TCP/IP protocol stack

**ESP32-Specific:**
- Integrated 802.11 b/g/n Wi-Fi
- Station mode (connect to existing network)
- AP mode (create network)
- Station+AP mode (both simultaneously)
- WPA/WPA2/WEP security
- DHCP client (automatic IP assignment)

**Station Mode (Connect to Network):**
```cpp
// Arduino-ESP32
#include <WiFi.h>

WiFi.begin("SSID", "password");
while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
}
Serial.println(WiFi.localIP());
```

**AP Mode (Create Network):**
```cpp
// Arduino-ESP32
WiFi.softAP("ESP32-AP", "password");
Serial.println(WiFi.softAPIP());
```

**ESP32-Specific Notes:**
- Wi-Fi uses significant power
- WiFi and Bluetooth can interfere (coexistence issues)
- Some GPIO pins have restrictions when Wi-Fi is enabled
- ESP32 supports various security modes

**Why this matters:** Wi-Fi is essential for IoT applications. ESP32's integrated Wi-Fi is a key feature, but it has specific behaviors and limitations.

### BLE Overview

**Universal Concept:** Wireless communication protocol

**BLE (Bluetooth Low Energy):**
- Low power consumption
- Short range
- GATT (Generic Attribute Profile) for data organization
- GAP (Generic Access Profile) for connection management

**ESP32-Specific:**
- Dual-mode Bluetooth (Classic + BLE)
- BLE controller and host
- GATT server and client roles
- Advertising and scanning

**Basic BLE (ESP32):**
```cpp
// Arduino-ESP32 with BLE library
#include <BLEDevice.h>
#include <BLEServer.h>

BLEDevice::init("ESP32");
BLEServer *pServer = BLEDevice::createServer();
BLEService *pService = pServer->createService(SERVICE_UUID);
BLECharacteristic *pCharacteristic = pService->createCharacteristic(
    CHARACTERISTIC_UUID,
    BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE
);
pService->start();
pServer->getAdvertising()->start();
```

**Note:** This is introductory level. Advanced BLE (services, characteristics, notifications) is beyond this phase.

**Why this matters:** BLE is essential for low-power wireless applications. ESP32's BLE support is a key feature for IoT.

### NVS (Non-Volatile Storage)

**Universal Concept (from Phase 5):**
- Flash memory stores data persistently
- EEPROM concept for configuration data

**ESP32-Specific:**
- NVS (Non-Volatile Storage) library
- Key-value storage in Flash
- Partitioned storage
- Limited write cycles (Flash wear)

**NVS Usage (ESP-IDF):**
```c
#include "nvs_flash.h"
#include "nvs.h"

// Initialize NVS
nvs_handle_t nvs_handle;
nvs_open("storage", NVS_READWRITE, &nvs_handle);

// Write value
nvs_set_i32(nvs_handle, "key", 42);
nvs_commit(nvs_handle);

// Read value
int32_t value;
nvs_get_i32(nvs_handle, "key", &value);

// Close
nvs_close(nvs_handle);
```

**Why this matters:** Persistent storage is essential for configuration data. ESP32's NVS provides a simple key-value interface.

### OTA (Over-The-Air) Updates

**Universal Concept:** Firmware update mechanism

**OTA (ESP32-Specific):**
- Update firmware over Wi-Fi
- Multiple app partitions
- Rollback capability
- Security considerations

**Basic OTA Concept:**
1. ESP32 connects to server
2. Downloads new firmware
3. Writes to unused app partition
4. Sets boot partition to new firmware
5. Resets and boots new firmware

**Note:** This is an introductory concept. Full OTA implementation with security, rollback, and error handling is beyond this phase.

**Why this matters:** OTA is essential for remote firmware updates in IoT devices. ESP32 has built-in OTA support.

### Debugging ESP32

**Common Problems:**

**Flashing Problems:**
- Wrong COM port selected
- USB driver not installed
- Boot mode not entered (hold BOOT button when powering on)
- Cable issues

**Boot Problems:**
- Wrong boot mode
- Corrupted firmware
- Hardware issues

**GPIO Problems:**
- Wrong pin number (varies by board)
- Pin mode not configured
- Current limit exceeded
- Strapping pin issues

**Power Problems:**
- Insufficient power supply current
- USB port current limitation
- Short circuit

**Debugging Techniques:**
- Use serial monitor for debug output
- Check ESP32 boot messages
- Use multimeter to measure voltages
- Simplify code to isolate problem
- Check datasheet for specific board variant

**Why this matters:** Debugging is essential for development. ESP32 has specific common problems and debugging techniques.

---

## Exact Resources

### Resource 1: Arduino-ESP32 Documentation
- **Provider:** Espressif (Official)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Official Arduino-ESP32 API reference
- **URL:** https://docs.espressif.com/projects/arduino-esp32/en/latest/

### Resource 2: ESP-IDF Programming Guide
- **Provider:** Espressif (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Official ESP-IDF documentation
- **URL:** https://docs.espressif.com/projects/esp-idf/en/latest/esp32/

### Resource 3: ESP32 Datasheet
- **Provider:** Espressif (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Complete ESP32 technical specifications
- **URL:** https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf

### Resource 4: ESP32 Technical Reference Manual
- **Provider:** Espressif (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** ESP32 register-level documentation
- **URL:** https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf

### Resource 5: ESP32 Pinout Reference
- **Provider:** Espressif (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** ESP32 GPIO pin assignments and functions
- **URL:** https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-pins.html

---

## Study Order

Follow this exact sequence:

1. **Study ESP32 overview** (how it implements universal MCU concepts)
2. **Understand ESP32 CPU and memory** (differences from ARM)
3. **Study ESP32 GPIO** (limits, safe usage)
4. **Learn about development environments** (Arduino vs ESP-IDF)
5. **Understand the toolchain** (build process)
6. **Study GPIO in practice** (Arduino and ESP-IDF)
7. **Learn PWM in practice** (LEDC peripheral)
8. **Study ADC in practice** (limitations, non-linearity)
9. **Learn UART in practice** (serial communication)
10. **Study I2C in practice** (sensor communication)
11. **Learn SPI in practice** (high-speed communication)
12. **Study Wi-Fi** (station mode, AP mode)
13. **Learn BLE basics** (introductory level)
14. **Study NVS** (persistent storage)
15. **Understand OTA concepts** (firmware updates)
16. **Study debugging techniques** (common problems)
17. **Complete all exercises**
18. **Complete all labs**
19. **Complete the project**
20. **Take the knowledge test**
21. **Take the practical test**
22. **Review completion checklist**

---

## Exercises

### Exercise 1: Universal vs ESP32-Specific

**Objective:** Distinguish between universal MCU concepts and ESP32-specific implementation.

**Tasks:**
1. List 5 universal MCU concepts that apply to all MCUs
2. List 5 ESP32-specific features or behaviors
3. Explain how ESP32's CPU differs from ARM Cortex-M
4. Explain how ESP32's memory organization differs from a typical STM32
5. Explain why understanding universal concepts is important even when learning ESP32

**Expected Outcome:** You can distinguish between universal concepts and ESP32-specific details.

### Exercise 2: Arduino vs ESP-IDF

**Objective:** Understand the differences between Arduino-ESP32 and ESP-IDF.

**Tasks:**
1. List 3 advantages of Arduino-ESP32
2. List 3 advantages of ESP-IDF
3. When would you choose Arduino-ESP32?
4. When would you choose ESP-IDF?
5. Can Arduino code run on ESP-IDF? Why or why not?

**Expected Outcome:** You understand when to use each framework and their trade-offs.

### Exercise 3: GPIO Safety Calculations

**Objective:** Calculate safe GPIO usage for ESP32.

**Tasks:**
1. If an LED requires 15mA and ESP32 GPIO limit is 40mA, can you drive it directly? (assuming appropriate resistor)
2. If you need to drive 10 LEDs at 15mA each from ESP32 GPIO, is this safe? Why or why not?
3. What is the total GPIO current limit for ESP32 (typical)?
4. What happens if you exceed the per-pin current limit?
5. What happens if you exceed the total GPIO current limit?

**Expected Outcome:** You can calculate safe GPIO usage and understand ESP32 limits.

### Exercise 4: ADC Calculations

**Objective:** Calculate ADC readings and voltages for ESP32.

**Tasks:**
1. ESP32 ADC is 12-bit. What is the maximum digital value?
2. If ADC reads 2048 with 3.3V reference, what is the input voltage?
3. If input voltage is 1.65V with 3.3V reference, what is the ADC reading?
4. Why is ESP32 ADC non-linear at low voltages?
5. What attenuation setting would you use for 3.3V input range?

**Expected Outcome:** You can perform ADC calculations and understand ESP32 ADC limitations.

### Exercise 5: PWM Calculations

**Objective:** Calculate PWM parameters for ESP32 LEDC.

**Tasks:**
1. You want 1kHz PWM frequency with 8-bit resolution. What is the timer divider value? (Assume 80MHz APB clock)
2. For 50% duty cycle with 8-bit resolution, what is the duty value?
3. For 25% duty cycle with 8-bit resolution, what is the duty value?
4. What happens if PWM frequency is too low for an LED?
5. What happens if PWM frequency is too high for an LED?

**Expected Outcome:** You can calculate PWM parameters and understand LEDC configuration.

---

## Labs

### Lab 1: ESP32 LED

**Objective:** Build and program an ESP32 LED circuit, reinforcing Phase 4 electronics concepts.

**Prerequisites:**
- Completed Phase 4 (Electronics)
- Understanding of current limiting resistors
- ESP32 development board set up

**Components:**
- ESP32 development board
- LED
- Resistor (220Ω or 330Ω)
- Breadboard
- Jumper wires

**Theory:**
- Reinforces current limiting from Phase 4
- ESP32 GPIO drives LED (similar to Phase 4 transistor circuit, but GPIO can directly drive small loads)
- ESP32 GPIO current limit: ~40mA per pin
- LED requires ~10-20mA

**Wiring:**
```
ESP32 GPIO (e.g., GPIO2)
    │
   Resistor (220Ω or 330Ω)
    │
   LED (anode +)
    │
   LED (cathode -)
    │
ESP32 GND
```

**Arduino-ESP32 Code:**
```cpp
const int ledPin = 2;  // Built-in LED on many boards

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
```

**Expected Behavior:**
- LED blinks once per second
- Brightness depends on resistor value

**Measurements:**
- Measure voltage across LED (should be ~2V)
- Measure voltage across resistor
- Calculate current
- Verify current is within ESP32 GPIO limit

**Troubleshooting:**
- LED not lighting: Check wiring, check pin number, measure voltage
- LED always on: Check code, check GPIO configuration
- Wrong GPIO pin: Check board pinout diagram

**Common Mistakes:**
- Wrong GPIO pin number (varies by board)
- Forgetting current limiting resistor
- Wrong resistor value
- Poor breadboard connections

**Safety:**
- Use 3.3V or 5V supply as appropriate for your board
- Don't exceed GPIO current limit
- Ensure correct polarity

**Completion Criteria:**
- LED blinks reliably
- Current is within ESP32 GPIO limits
- Understand how this reinforces Phase 4 concepts
- Can troubleshoot basic GPIO problems

---

### Lab 2: ESP32 Button

**Objective:** Build an ESP32 button circuit with debounce, reinforcing Phase 3 digital electronics concepts.

**Prerequisites:**
- Completed Lab 1
- Understanding of pull-up/pull-down from Phase 3
- Understanding of debounce from Phase 3

**Components:**
- ESP32 development board
- Push button
- Resistor (10kΩ for pull-up, or use internal pull-up)
- Breadboard
- Jumper wires

**Theory:**
- Reinforces pull-up/pull-down from Phase 3
- Reinforces debounce from Phase 3
- ESP32 has internal pull-up/pull-down resistors
- Software debounce (delay or timer)

**Wiring (External Pull-Up):**
```
ESP32 3.3V
    │
   Resistor (10kΩ)
    │
ESP32 GPIO (e.g., GPIO4)
    │
   Button
    │
ESP32 GND
```

**Arduino-ESP32 Code (with debounce):**
```cpp
const int buttonPin = 4;
int lastState = HIGH;
int currentState;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  currentState = digitalRead(buttonPin);
  
  if (currentState != lastState) {
    lastDebounceTime = millis();
  }
  
  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (currentState == LOW) {
      Serial.println("Button pressed");
    }
  }
  
  lastState = currentState;
}
```

**Expected Behavior:**
- Button press registered once (not multiple times)
- Clean debouncing
- Serial output when button pressed

**Measurements:**
- Measure GPIO voltage when button not pressed (should be ~3.3V)
- Measure GPIO voltage when button pressed (should be ~0V)
- Observe voltage bounce with multimeter (if possible)

**Troubleshooting:**
- Button not registering: Check wiring, check pull-up, check pin number
- Multiple registrations: Increase debounce delay
- Always HIGH: Check wiring, check pull-up connection

**Common Mistakes:**
- Wrong GPIO pin number
- Not using pull-up/pull-down
- Insufficient debounce delay
- Poor breadboard connections

**Safety:**
- Use 3.3V or 5V as appropriate
- Ensure proper connections

**Completion Criteria:**
- Button debounces reliably
- Serial output shows single press per button press
- Understand how this reinforces Phase 3 concepts
- Can use internal pull-up if available

---

### Lab 3: PWM LED Brightness

**Objective:** Use ESP32 PWM to control LED brightness, reinforcing Phase 3 PWM concepts.

**Prerequisites:**
- Completed Lab 1
- Understanding of PWM from Phase 3
- Understanding of duty cycle from Phase 3

**Components:**
- ESP32 development board
- LED
- Resistor (220Ω or 330Ω)
- Breadboard
- Jumper wires

**Theory:**
- Reinforces PWM from Phase 3
- ESP32 uses LEDC peripheral for PWM
- Duty cycle controls average voltage
- Frequency affects smoothness

**Wiring:** Same as Lab 1

**Arduino-ESP32 Code:**
```cpp
const int ledPin = 2;
const int pwmChannel = 0;
const int pwmFreq = 5000;
const int pwmResolution = 8;

void setup() {
  ledcSetup(pwmChannel, pwmFreq, pwmResolution);
  ledcAttachPin(ledPin, pwmChannel);
}

void loop() {
  // Fade in
  for (int duty = 0; duty <= 255; duty++) {
    ledcWrite(pwmChannel, duty);
    delay(10);
  }
  
  // Fade out
  for (int duty = 255; duty >= 0; duty--) {
    ledcWrite(pwmChannel, duty);
    delay(10);
  }
}
```

**Expected Behavior:**
- LED fades in and out smoothly
- No visible flicker
- Brightness varies with duty cycle

**Measurements:**
- Observe brightness at different duty cycles
- Measure average voltage with multimeter (if possible)

**Troubleshooting:**
- LED not changing brightness: Check LEDC configuration, check pin
- Visible flicker: Increase PWM frequency
- LED always on: Check duty cycle calculation

**Common Mistakes:**
- Wrong PWM channel
- Wrong frequency or resolution
- Using pin that doesn't support PWM
- Not calling ledcAttachPin

**Safety:**
- Use appropriate current limiting resistor
- Don't exceed GPIO current limit

**Completion Criteria:**
- LED brightness varies smoothly
- No visible flicker
- Understand how this reinforces Phase 3 PWM concepts
- Can configure ESP32 LEDC peripheral

---

### Lab 4: Potentiometer ADC

**Objective:** Read potentiometer using ESP32 ADC, reinforcing Phase 4 electronics and Phase 3 ADC concepts.

**Prerequisites:**
- Completed Phase 4 potentiometer lab
- Understanding of voltage division from Phase 4
- Understanding of ADC from Phase 3

**Components:**
- ESP32 development board
- Potentiometer (10kΩ)
- Breadboard
- Jumper wires

**Theory:**
- Reinforces voltage division from Phase 4
- Reinforces ADC from Phase 3
- ESP32 ADC limitations (non-linearity, attenuation)
- ADC resolution (12-bit)

**Wiring:**
```
ESP32 3.3V
    │
Potentiometer (left terminal)
    │
Potentiometer (wiper/middle terminal) → ESP32 ADC pin (e.g., GPIO34)
    │
Potentiometer (right terminal)
    │
ESP32 GND
```

**Arduino-ESP32 Code:**
```cpp
const int adcPin = 34;  // ADC1_CH6

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);  // 12-bit resolution
}

void loop() {
  int adcValue = analogRead(adcPin);
  float voltage = adcValue * 3.3 / 4095.0;
  
  Serial.print("ADC: ");
  Serial.print(adcValue);
  Serial.print(" Voltage: ");
  Serial.print(voltage, 3);
  Serial.println("V");
  
  delay(100);
}
```

**Expected Behavior:**
- ADC value varies as potentiometer is turned
- Voltage reading varies from 0V to 3.3V
- Serial output shows values

**Measurements:**
- Measure voltage at ADC pin with multimeter
- Compare multimeter reading to ADC reading
- Note any non-linearity at low voltages

**Troubleshooting:**
- ADC always 0: Check wiring, check pin is ADC-capable
- ADC always 4095: Check wiring, check voltage range
- Non-linear readings: Normal for ESP32 ADC at low voltages
- ADC affected by WiFi: Turn off WiFi for accurate readings

**Common Mistakes:**
- Using pin that is not ADC-capable
- Not setting ADC resolution
- Using wrong attenuation
- Not accounting for non-linearity

**Safety:**
- Use 3.3V only (don't exceed ADC input range)
- Check pin is ADC-capable for your board

**Completion Criteria:**
- ADC readings vary with potentiometer
- Understand ESP32 ADC limitations
- Can calculate voltage from ADC value
- Understand how this reinforces Phase 3 and 4 concepts

---

### Lab 5: UART Serial Debugging

**Objective:** Use ESP32 UART for serial communication and debugging.

**Prerequisites:**
- Understanding of UART from Phase 5
- ESP32 development environment set up

**Components:**
- ESP32 development board
- USB cable (for programming and serial)

**Theory:**
- Reinforces UART from Phase 5
- ESP32 has 3 UART controllers
- UART0 used for USB programming/debugging
- Baud rate must match on both ends

**Arduino-ESP32 Code:**
```cpp
void setup() {
  Serial.begin(115200);
  Serial.println("ESP32 UART Debugging");
}

void loop() {
  Serial.print("Millis: ");
  Serial.println(millis());
  delay(1000);
}
```

**Expected Behavior:**
- Serial monitor shows debug output
- Messages appear every second

**Troubleshooting:**
- No serial output: Check baud rate, check COM port, check USB driver
- Garbled output: Wrong baud rate
- Port not found: USB driver not installed, wrong COM port

**Common Mistakes:**
- Wrong baud rate
- Wrong COM port
- Not opening serial monitor
- USB driver not installed

**Completion Criteria:**
- Serial output works reliably
- Can use serial monitor for debugging
- Understand UART communication basics

---

### Lab 6: I2C Device Scan

**Objective:** Scan I2C bus to find connected devices, reinforcing Phase 5 I2C concepts.

**Prerequisites:**
- Understanding of I2C from Phase 5
- I2C device (e.g., OLED display, sensor)

**Components:**
- ESP32 development board
- I2C device (e.g., SSD1306 OLED, BME280 sensor)
- Jumper wires

**Theory:**
- Reinforces I2C from Phase 5
- I2C devices have addresses
- ESP32 has 2 I2C controllers
- Default I2C pins: SDA=GPIO21, SCL=GPIO22

**Wiring:**
```
ESP32 GPIO21 (SDA) ─── I2C device SDA
ESP32 GPIO22 (SCL) ─── I2C device SCL
ESP32 GND ────────── I2C device GND
ESP32 3.3V ───────── I2C device VCC
```

**Arduino-ESP32 Code (I2C Scanner):**
```cpp
#include <Wire.h>

void setup() {
  Wire.begin(21, 22);
  Serial.begin(115200);
  Serial.println("I2C Scanner");
}

void loop() {
  byte error, address;
  int nDevices = 0;
  
  Serial.println("Scanning...");
  
  for (address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();
    
    if (error == 0) {
      Serial.print("I2C device found at address 0x");
      if (address < 16) Serial.print("0");
      Serial.println(address, HEX);
      nDevices++;
    }
  }
  
  if (nDevices == 0) {
    Serial.println("No I2C devices found");
  } else {
    Serial.print(nDevices);
    Serial.println(" device(s) found");
  }
  
  delay(5000);
}
```

**Expected Behavior:**
- Scanner finds I2C device addresses
- Serial output shows detected devices

**Troubleshooting:**
- No devices found: Check wiring, check pull-ups, check power
- Wrong address: Check device datasheet
- Scanner crashes: Check I2C pins, check pull-ups

**Common Mistakes:**
- Wrong I2C pins
- No pull-up resistors (check if board has them)
- Power not connected to device
- Wrong SDA/SCL connection

**Safety:**
- Use 3.3V for I2C device (check device voltage requirement)
- Ensure correct wiring

**Completion Criteria:**
- I2C scanner finds connected devices
- Understand I2C addressing
- Can troubleshoot I2C connections

---

### Lab 7: I2C Sensor Reading

**Objective:** Read data from I2C sensor (e.g., OLED display or temperature sensor).

**Prerequisites:**
- Completed Lab 6
- I2C sensor with known address
- Library for sensor (if using Arduino)

**Components:**
- ESP32 development board
- I2C sensor (e.g., SSD1306 OLED, BME280)
- Jumper wires

**Theory:**
- Reinforces I2C communication from Phase 5
- Read/write operations to I2C device
- Sensor-specific registers and data format

**Wiring:** Same as Lab 6

**Arduino-ESP32 Code (SSD1306 OLED Example):**
```cpp
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  Wire.begin(21, 22);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,0);
  display.println("ESP32 I2C");
  display.display();
}

void loop() {
  delay(1000);
}
```

**Expected Behavior:**
- Display shows text
- I2C communication works

**Troubleshooting:**
- Display not working: Check address, check wiring, check library
- Wrong display size: Check display dimensions
- Garbled output: Check I2C speed, check wiring

**Common Mistakes:**
- Wrong I2C address
- Wrong display dimensions
- Not calling display.display()
- Wiring errors

**Completion Criteria:**
- I2C sensor/display works
- Understand I2C read/write operations
- Can read sensor-specific data

---

### Lab 8: Wi-Fi Connection

**Objective:** Connect ESP32 to Wi-Fi network, reinforcing Phase 4 networking concepts.

**Prerequisites:**
- Understanding of IP addresses from Phase 4
- Wi-Fi network available

**Components:**
- ESP32 development board
- USB cable

**Theory:**
- Reinforces networking from Phase 4
- ESP32 integrated Wi-Fi
- Station mode (connect to existing network)
- DHCP (automatic IP assignment)

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

void setup() {
  Serial.begin(115200);
  
  Serial.println("Connecting to WiFi");
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  delay(1000);
}
```

**Expected Behavior:**
- ESP32 connects to Wi-Fi
- Serial output shows IP address

**Troubleshooting:**
- Cannot connect: Check SSID/password, check network range, check power
- Wrong IP: Check DHCP is working, check network
- Connection drops: Check signal strength, check power

**Common Mistakes:**
- Wrong SSID or password
- Network out of range
- 5GHz network (ESP32 supports 2.4GHz only)
- Network security not supported

**Safety:**
- Use appropriate network
- Don't hardcode credentials in production code

**Completion Criteria:**
- ESP32 connects to Wi-Fi reliably
- Obtains IP address via DHCP
- Understand station mode
- Can troubleshoot Wi-Fi connection problems

---

### Lab 9: Simple HTTP Endpoint

**Objective:** Create a simple HTTP server on ESP32.

**Prerequisites:**
- Completed Lab 8
- Understanding of HTTP from Phase 4

**Components:**
- ESP32 development board
- USB cable

**Theory:**
- Reinforces HTTP from Phase 4
- ESP32 as web server
- HTTP requests and responses

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);

void handleRoot() {
  server.send(200, "text/plain", "Hello from ESP32!");
}

void setup() {
  Serial.begin(115200);
  WiFi.begin("YOUR_SSID", "YOUR_PASSWORD");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println(WiFi.localIP());
  
  server.on("/", handleRoot);
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
```

**Expected Behavior:**
- HTTP server starts
- Browser can access ESP32 IP address
- "Hello from ESP32!" displayed

**Troubleshooting:**
- Cannot access: Check IP address, check firewall, check client on same network
- 404 error: Check server routes
- Server not responding: Check Wi-Fi connection

**Common Mistakes:**
- Wrong IP address
- Client on different network
- Firewall blocking connection
- Not calling server.handleClient()

**Completion Criteria:**
- HTTP server works
- Can access from browser
- Understand basic HTTP server concepts

---

### Lab 10: NVS Configuration Storage

**Objective:** Use ESP32 NVS to store configuration data persistently.

**Prerequisites:**
- Understanding of Flash memory from Phase 5
- ESP-IDF environment (NVS is ESP-IDF specific)

**Components:**
- ESP32 development board
- USB cable

**Theory:**
- Reinforces Flash memory from Phase 5
- NVS provides key-value storage
- Data persists across reboots
- Limited write cycles (Flash wear)

**ESP-IDF Code:**
```c
#include "nvs_flash.h"
#include "nvs.h"

void app_main() {
  // Initialize NVS
  nvs_handle_t nvs_handle;
  esp_err_t err = nvs_flash_init();
  if (err == ESP_ERR_NVS_NO_FREE_PAGES || err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
    ESP_ERROR_CHECK(nvs_flash_erase());
    err = nvs_flash_init();
  }
  ESP_ERROR_CHECK(err);
  
  // Open NVS
  ESP_ERROR_CHECK(nvs_open("storage", NVS_READWRITE, &nvs_handle));
  
  // Write value
  int32_t counter = 0;
  nvs_get_i32(nvs_handle, "counter", &counter);
  counter++;
  nvs_set_i32(nvs_handle, "counter", counter);
  nvs_commit(nvs_handle);
  
  printf("Counter: %d\n", counter);
  
  nvs_close(nvs_handle);
}
```

**Expected Behavior:**
- Counter increments each boot
- Value persists across reboots

**Troubleshooting:**
- Value not persisting: Check nvs_commit, check NVS partition
- NVS init error: Check partition table, erase NVS
- Wrong value: Check key name, check data type

**Common Mistakes:**
- Forgetting nvs_commit
- Wrong key name
- Wrong data type
- Not initializing NVS correctly

**Completion Criteria:**
- NVS stores data persistently
- Data survives reboots
- Understand Flash memory concepts
- Understand NVS limitations

---

## Projects

### Project: ESP32 Environmental Telemetry Node

**Objective:** Create an ESP32-based environmental monitoring node that demonstrates core ESP32 capabilities.

**Requirements:**
- Read temperature sensor (I2C or analog)
- Read potentiometer (ADC)
- Control LED brightness (PWM)
- Monitor button (GPIO with debounce)
- Send data via UART (serial output)
- Connect to Wi-Fi
- Provide simple HTTP endpoint with sensor data
- Store configuration in NVS (ESP-IDF) or preferences (Arduino)

**Suggested Architecture:**
```
Sensors (I2C/ADC)
    ↓
ESP32 Processing
    ↓
Serial Output (UART)
    ↓
Wi-Fi
    ↓
HTTP Server
```

**Deliverables:**
- Working firmware (Arduino-ESP32 or ESP-IDF)
- Circuit documentation
- Code with comments
- Serial output showing sensor data
- HTTP endpoint accessible from browser
- Configuration persistence

**Time Estimate:** 4-6 hours

**Project Structure:**
```
esp32-telemetry-node/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   └── main.ino (or main.c for ESP-IDF)
├── docs/
│   └── architecture.md
└── results/
    └── measurements.md
```

**Note:** This project prepares for the eventual thesis architecture (sensor → MCU → communication → IoT).

---

## Common Mistakes

### Mistake 1: Confusing Universal Concepts with ESP32-Specific
**Problem:** Assuming ESP32 behavior represents all MCUs
**Consequence:** Difficulty working with other MCUs (STM32, etc.)
**Solution:** Clearly distinguish universal concepts from ESP32-specific implementation

### Mistake 2: Exceeding GPIO Current Limits
**Problem:** Drawing too much current from ESP32 GPIO
**Consequence:** Chip damage, unreliable operation
**Solution:** Always check ESP32 GPIO limits (~40mA per pin, ~1200mA total)

### Mistake 3: Applying 5V to ESP32 GPIO
**Problem:** Connecting 5V devices to 3.3V ESP32
**Consequence:** Chip damage
**Solution:** Use level shifters or 3.3V-compatible devices

### Mistake 4: Ignoring ADC Non-Linearity
**Problem:** Assuming ESP32 ADC is perfectly linear
**Consequence:** Inaccurate sensor readings
**Solution:** Understand ESP32 ADC limitations, calibrate if needed

### Mistake 5: Wrong GPIO Pin Numbers
**Problem:** Using pin numbers that don't match the board
**Consequence:** Code doesn't work, confusing debugging
**Solution:** Always check your specific board's pinout diagram

### Mistake 6: Not Debouncing Buttons
**Problem:** Treating button bounce as multiple presses
**Consequence:** Unintended multiple actions
**Solution:** Always implement debounce (hardware or software)

### Mistake 7: WiFi Interference with ADC
**Problem:** WiFi affecting ADC readings
**Consequence:** Inaccurate sensor readings
**Solution:** Turn off WiFi during ADC reading, or accept inaccuracy

### Mistake 8: Wrong I2C Address
**Problem:** Using wrong I2C device address
**Consequence:** I2C communication fails
**Solution:** Check device datasheet for correct address

### Mistake 9: Hardcoding Wi-Fi Credentials
**Problem:** SSID and password in source code
**Consequence:** Security risk, difficult to change
**Solution:** Use NVS/preferences for credentials (production)

### Mistake 10: Choosing Wrong Framework
**Problem:** Using Arduino when ESP-IDF is needed (or vice versa)
**Consequence:** Limited capabilities or unnecessary complexity
**Solution:** Choose framework based on project requirements

---

## Troubleshooting

### Flashing Problems
**Problem:** Cannot flash firmware to ESP32
**Solutions:**
- Check COM port selection
- Hold BOOT button when powering on
- Check USB driver installation
- Try different USB cable
- Check boot mode (GPIO0, GPIO2, GPIO12 states)

### Boot Problems
**Problem:** ESP32 doesn't boot after flashing
**Solutions:**
- Check firmware is correct for your board
- Check boot mode (strapping pins)
- Check for corrupted firmware (erase and reflash)
- Check power supply

### GPIO Problems
**Problem:** GPIO not working as expected
**Solutions:**
- Check pin number (varies by board)
- Check pin mode (input/output)
- Check if pin is input-only or output-only
- Check for strapping pin issues
- Check if pin is used by other peripheral

### Wi-Fi Problems
**Problem:** Cannot connect to Wi-Fi
**Solutions:**
- Check SSID and password
- Check network is 2.4GHz (ESP32 doesn't support 5GHz)
- Check signal strength
- Check network security type
- Check antenna connection

### I2C Problems
**Problem:** I2C communication fails
**Solutions:**
- Check wiring (SDA, SCL, power, ground)
- Check pull-up resistors
- Check I2C address
- Check if both devices are on same I2C bus
- Scan I2C bus to find devices

### Power Problems
**Problem:** ESP32 resets or behaves erratically
**Solutions:**
- Check power supply current capability
- Check USB port current limitation
- Check for short circuits
- Check for voltage drops
- Use external power supply if needed

---

## Knowledge Test

Answer these questions without looking at the materials:

1. How does ESP32's CPU differ from ARM Cortex-M?
2. What is the difference between Arduino-ESP32 and ESP-IDF?
3. When would you choose Arduino-ESP32 over ESP-IDF?
4. What is the ESP32 GPIO current limit per pin (typical)?
5. What is the ESP32 total GPIO current limit (typical)?
6. Can you apply 5V to ESP32 GPIO? Why or why not?
7. What is ESP32's ADC resolution?
8. Why is ESP32 ADC non-linear at low voltages?
9. What is the ESP32 PWM peripheral called?
10. What are the default I2C pins on ESP32?
11. What is NVS used for?
12. What is OTA?
13. What is the difference between Wi-Fi station mode and AP mode?
14. What is BLE?
15. What is a universal MCU concept that applies to ESP32?
16. What is an ESP32-specific feature?
17. What happens if you exceed ESP32 GPIO current limits?
18. Why is it important to distinguish universal concepts from ESP32-specific details?
19. What is the purpose of debounce?
20. How do you scan the I2C bus to find devices?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **GPIO Setup:**
   - Configure an ESP32 GPIO as output
   - Blink an LED
   - Measure the current and verify it's within ESP32 limits

2. **ADC Reading:**
   - Connect a potentiometer to ESP32 ADC
   - Read the ADC value
   - Calculate the voltage
   - Verify with multimeter

3. **I2C Communication:**
   - Connect an I2C device (sensor or display)
   - Scan the I2C bus to find the device
   - Read data from the device
   - Display the data

4. **Wi-Fi Connection:**
   - Connect ESP32 to a Wi-Fi network
   - Print the obtained IP address
   - Verify connectivity (e.g., ping the ESP32)

5. **Framework Comparison:**
   - Explain when you would use Arduino-ESP32
   - Explain when you would use ESP-IDF
   - Give a specific example for each

**Passing Criteria:** All tasks completed successfully with understanding demonstrated.

---

## Completion Checklist

Before moving to Phase 7, verify you have:

- [ ] Understand how ESP32 implements universal MCU concepts
- [ ] Can distinguish universal concepts from ESP32-specific behavior
- [ ] Understand Arduino-ESP32 vs ESP-IDF differences
- [ ] Understand ESP32 GPIO limits (current, voltage)
- [ ] Can configure and use ESP32 GPIO safely
- [ ] Can implement PWM using ESP32 LEDC
- [ ] Can read analog sensors using ESP32 ADC
- [ ] Understand ESP32 ADC limitations
- [ ] Can use UART for serial communication
- [ ] Can communicate with I2C devices
- [ ] Can communicate with SPI devices
- [ ] Can connect ESP32 to Wi-Fi
- [ ] Understand basic BLE concepts
- [ ] Can use NVS for persistent storage
- [ ] Understand OTA concepts
- [ ] Can debug common ESP32 problems
- [ ] Completed all exercises
- [ ] Completed at least 5 labs
- [ ] Completed the telemetry node project
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Understand how to choose between Arduino and ESP-IDF

---

## Do Not Continue Until...

**Do not start Phase 7 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can distinguish universal concepts from ESP32-specific details
5. You understand ESP32 GPIO limits and safe usage
6. You have completed at least 5 labs
7. You have completed the telemetry node project
8. You understand when to use Arduino vs ESP-IDF

**ESP32 development builds on the universal MCU concepts from Phase 5. Take the time to understand both the universal concepts and ESP32-specific implementation before moving to sensors and actuators.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 7 — Sensors and Actuators**

Phase 7 will teach you how to work with various sensors and actuators, applying the ESP32 skills you learned here to build practical sensor-based systems that prepare for the eventual IoT thesis project.

---

**ESP32 is a powerful platform, but it's just one of many MCUs. The universal concepts you learned in Phase 5 apply to all MCUs, while the ESP32-specific details you learned here are valuable for ESP32 development. Understanding both makes you a more versatile embedded systems developer.**
