# Phase 3 — ESP32 Embedded Development

> **Goal:** Become capable of developing real ESP32 firmware, first with Arduino-ESP32 and then with ESP-IDF.
>
> **Prerequisite:** Phase 2 electronics.
>
> **Outcome:** You can configure GPIO, read sensors, use ADC/PWM/UART/I²C/SPI, connect to Wi-Fi, create a simple HTTP service, debug firmware, and understand the ESP32 development workflow.

---

# 1. Exact resources

## Resource A — Official Arduino-ESP32 documentation

https://docs.espressif.com/projects/arduino-esp32/en/latest/

This is your primary reference.

Use the documentation sections for:

- Getting Started
- GPIO
- Analog Input
- LEDC/PWM
- Serial/UART
- Wire/I²C
- SPI
- Wi-Fi
- WebServer
- BLE/Bluetooth when needed

Do not replace official documentation with random tutorials when the API or pin behavior matters.

## Resource B — Official ESP-IDF documentation

https://docs.espressif.com/projects/esp-idf/en/latest/esp32/

Start with:

https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/

This becomes your advanced framework.

## Resource C — Wokwi

https://wokwi.com/

Use it to prototype circuits and firmware.

## Resource D — Espressif GitHub

https://github.com/espressif

Use official examples when you need a reference implementation.

---

# 2. Why two frameworks?

You will use:

### Arduino-ESP32

Good for:

- learning
- rapid prototypes
- simple sensor projects
- fast experimentation

### ESP-IDF

Good for:

- professional ESP32 development
- lower-level control
- FreeRTOS
- configuration
- networking
- production-oriented architecture

Your progression:

```text
Arduino-ESP32
      ↓
ESP32 fundamentals
      ↓
small projects
      ↓
ESP-IDF
      ↓
FreeRTOS / advanced firmware
```

Do NOT start with advanced ESP-IDF internals on day one.

---

# 3. Hardware preparation

Before programming, identify your exact board.

Record:

- board name
- ESP32 chip/family
- USB interface
- available GPIO
- flash size
- PSRAM if present
- power input
- ADC pins
- boot/reset buttons

Create:

`docs/board-notes.md`

Do not blindly copy GPIO numbers from another ESP32 board.

---

# 4. Install your software

## Arduino IDE

Official:

https://www.arduino.cc/en/software/

Install Arduino IDE.

Then install the Espressif ESP32 board package using the official Arduino-ESP32 getting-started instructions.

Verify:

```text
Tools
→ Board
→ ESP32 board
```

Then select your exact board or appropriate ESP32 family board.

---

# 5. First firmware

Your first program:

```cpp
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);

    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
}
```

Understand every line.

Do not just paste it.

---

# 6. GPIO

Learn:

- INPUT
- OUTPUT
- INPUT_PULLUP
- HIGH
- LOW
- pinMode
- digitalRead
- digitalWrite

Example:

```cpp
const int BUTTON_PIN = 4;
const int LED_PIN = 2;

void setup() {
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    bool pressed = digitalRead(BUTTON_PIN) == LOW;

    digitalWrite(LED_PIN, pressed ? HIGH : LOW);
}
```

Understand why the button is LOW when pressed.

---

# 7. GPIO safety

Some ESP32 GPIOs have special boot/strapping functions or board-specific restrictions.

Therefore:

**Never treat a random GPIO pinout diagram from another ESP32 board as universal.**

For every pin:

1. Check the exact board.
2. Check the ESP32 chip documentation.
3. Check boot/strapping restrictions.
4. Check whether the pin is input-only or has another limitation.
5. Check whether your board already uses it internally.

---

# 8. Serial debugging

Use Serial/UART as your primary debugging tool.

Example:

```cpp
void setup() {
    Serial.begin(115200);
    Serial.println("System starting...");
}

void loop() {
    Serial.println("Running");
    delay(1000);
}
```

Learn to print:

- values
- state
- errors
- timing
- sensor readings

Instead of:

```cpp
if (sensorError) {
}
```

do:

```cpp
if (sensorError) {
    Serial.println("ERROR: sensor read failed");
}
```

Good debugging is an embedded skill.

---

# 9. ADC

Connect your potentiometer from Phase 2.

Read it:

```cpp
int value = analogRead(ADC_PIN);
Serial.println(value);
```

Learn:

```text
physical voltage
      ↓
ADC
      ↓
digital reading
```

Do not assume the numerical range is identical across all ESP32 variants/configurations.

Always check the documentation for your chip/board.

---

# 10. PWM

Use ESP32's LEDC/PWM functionality.

Your objectives:

- set frequency
- set resolution
- set duty cycle
- change duty cycle dynamically

Project:

```text
potentiometer
      ↓
ADC
      ↓
map value
      ↓
PWM
      ↓
LED brightness
```

This is an important embedded pattern:

**input → processing → output**

---

# 11. UART

Learn:

- `Serial`
- hardware serial
- baud rate
- TX/RX
- serial debugging

Connect another UART device later.

Understand that UART is a communication interface, while USB may be used to connect your computer to the board.

---

# 12. I²C

Learn the Arduino Wire library and the concept of an I²C bus.

You need to understand:

```text
SDA
SCL
address
controller
target
pull-ups
```

Build an I²C scanner.

The scanner should:

1. Start I²C.
2. Test addresses.
3. Report devices that acknowledge.

Expected concept:

```text
Scanning...
Device found at 0x3C
```

The exact address depends on the device.

---

# 13. SPI

Learn:

```text
SCK
MOSI
MISO
CS
```

Connect an SPI peripheral if your hardware includes one.

Understand why CS identifies which device is being communicated with.

---

# 14. Sensor libraries

Now learn to use libraries.

Correct workflow:

```text
Datasheet
   ↓
Interface
   ↓
Library
   ↓
Initialization
   ↓
Read value
   ↓
Validate value
```

Do not blindly trust a sensor library.

You should know:

- supply voltage
- communication interface
- address
- measurement range
- resolution
- update rate
- error behavior

---

# 15. Wi-Fi

This is the most important new ESP32 capability for IoT.

Learn:

- station mode
- access point mode
- SSID
- password
- DHCP
- IP address
- gateway
- DNS
- reconnect behavior

Basic architecture:

```text
ESP32
  │
 Wi-Fi
  │
Router
  │
LAN
```

After connection, print:

```text
Connected
IP: 192.168.x.x
RSSI: -xx dBm
```

Do not hard-code assumptions about the user's network.

---

# 16. Wi-Fi project

Build:

**ESP32 Wi-Fi information monitor**

It should display:

- SSID
- local IP
- RSSI
- connection state

Then deliberately disconnect/reconnect the Wi-Fi and observe behavior.

Learn why robust IoT devices need reconnection logic.

---

# 17. HTTP fundamentals

Learn the idea of:

```text
Client
   ↓ HTTP request
Server
   ↓ HTTP response
Client
```

Understand:

- GET
- POST
- status codes
- headers
- JSON

Build an ESP32 HTTP server.

Example endpoints:

```text
GET /
GET /status
GET /sensor
POST /led
```

Return JSON from `/status`.

Example:

```json
{
  "device": "esp32-01",
  "uptime": 123,
  "temperature": 24.5
}
```

---

# 18. ESP32 web server project

Create:

> ESP32 Local IoT Control Panel

Requirements:

- display sensor values
- display device uptime
- display Wi-Fi status
- allow LED control
- expose JSON endpoint

Architecture:

```text
Browser
   ↓ HTTP
ESP32
   ↓
Sensors / GPIO
```

---

# 19. JSON

Learn:

```text
object
array
string
number
boolean
null
```

You will use JSON constantly in IoT.

Example:

```json
{
  "device_id": "esp32-01",
  "temperature": 25.1,
  "humidity": 54.2,
  "motion": true
}
```

---

# 20. Non-blocking programming

Do not build everything around long `delay()` calls.

Bad architecture:

```cpp
delay(10000);
readSensor();
delay(10000);
sendData();
```

Better concept:

```text
loop
 ├── check sensor timer
 ├── check network
 ├── process inputs
 └── perform required action
```

Learn the `millis()` pattern.

Example concept:

```cpp
unsigned long lastRead = 0;

if (millis() - lastRead >= 1000) {
    lastRead = millis();
    readSensor();
}
```

This becomes extremely important when you later use MQTT, FreeRTOS and multiple tasks.

---

# 21. Error handling

Your firmware should not assume everything works.

Handle:

- sensor disconnected
- invalid readings
- Wi-Fi lost
- HTTP failure
- I²C failure
- buffer problems
- timeout
- reboot

For every external component ask:

> What happens if this device disappears?

---

# 22. ESP-IDF introduction

Once your Arduino projects are comfortable, install ESP-IDF.

Official guide:

https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/

Learn the workflow:

```text
create project
    ↓
configure
    ↓
build
    ↓
flash
    ↓
monitor
```

Learn:

- `idf.py`
- project structure
- components
- configuration
- logging
- flashing
- monitoring

---

# 23. ESP-IDF project structure

Understand the basic idea:

```text
project/
├── CMakeLists.txt
├── sdkconfig
├── main/
│   ├── CMakeLists.txt
│   └── main.c
└── components/
```

You don't need to master CMake immediately.

You need to understand where firmware code and components live.

---

# 24. ESP-IDF logging

Learn log levels and structured debugging.

Concept:

```text
ESP_LOGI
ESP_LOGW
ESP_LOGE
```

Use logs to answer:

- Did Wi-Fi start?
- Did the sensor initialize?
- What IP was assigned?
- Did MQTT connect?
- Why did a function fail?

---

# 25. ESP-IDF GPIO project

Rebuild your simple LED/button project using ESP-IDF.

Do not copy your Arduino implementation.

The purpose is to learn the different development model.

---

# 26. Bluetooth/BLE

Learn this after Wi-Fi.

You do NOT need deep BLE development yet.

Understand:

- Bluetooth Classic vs BLE
- advertising
- scanning
- services
- characteristics
- GATT

Use BLE only when your thesis actually benefits from it.

---

# 27. Power concepts

Learn enough to avoid damaging or destabilizing your board:

- USB power
- 3.3 V rail
- current consumption
- regulator
- brownout
- battery basics
- sleep modes

Later, study:

- deep sleep
- light sleep
- wake-up sources

---

# 28. Phase 3 projects

## Project 1 — GPIO Controller

Features:

- button
- LED
- debounce
- serial logs

## Project 2 — Analog Controller

Features:

- potentiometer
- ADC
- PWM
- LED brightness

## Project 3 — I²C Sensor Node

Features:

- sensor
- I²C
- serial output
- error handling

## Project 4 — Wi-Fi Sensor

Features:

- sensor
- Wi-Fi
- IP address
- JSON

## Project 5 — ESP32 Web Server

Features:

- `/`
- `/status`
- `/sensor`
- LED control
- JSON responses

## Project 6 — ESP32 Multi-Function Node

Combine:

```text
Sensor
+
Button
+
LED
+
Buzzer
+
Wi-Fi
+
HTTP
+
JSON
```

---

# 29. Recommended firmware architecture

Start organizing code rather than putting everything in one file.

Example:

```text
src/
├── main.cpp
├── sensors.cpp
├── sensors.h
├── wifi_manager.cpp
├── wifi_manager.h
├── web_server.cpp
├── web_server.h
├── config.h
└── device_state.h
```

You will thank yourself when your thesis grows.

---

# 30. Configuration and secrets

Never commit:

```text
Wi-Fi password
API keys
private certificates
tokens
```

to GitHub.

Use:

- local configuration
- environment/build configuration
- ignored files
- secrets management

Example:

```text
config.example.h
config.h  ← ignored by Git
```

---

# 31. GitHub deliverable

Repository:

`esp32-development-labs`

Structure:

```text
esp32-development-labs/
├── README.md
├── 01-gpio/
├── 02-button/
├── 03-adc/
├── 04-pwm/
├── 05-i2c/
├── 06-spi/
├── 07-uart/
├── 08-wifi/
├── 09-http-server/
├── 10-multifunction-node/
├── esp-idf/
├── docs/
└── photos/
```

Each project needs:

- objective
- hardware
- wiring
- software
- architecture
- code
- test result
- troubleshooting
- lessons learned

---

# 32. Phase 3 final challenge

Build this WITHOUT following a complete tutorial:

## ESP32 Environmental Node

Hardware:

```text
ESP32
+
temperature/humidity sensor
+
light sensor
+
LED
+
button
+
buzzer
```

Firmware:

```text
Boot
 ↓
Initialize peripherals
 ↓
Connect Wi-Fi
 ↓
Read sensors
 ↓
Validate data
 ↓
Update LED/buzzer state
 ↓
Expose JSON over HTTP
 ↓
Continue monitoring
```

Requirements:

- no long blocking delays
- serial logs
- error handling
- Wi-Fi reconnect
- structured code
- GitHub README
- wiring diagram
- photos/video of working system

---

# 33. Phase 3 exam

You should be able to explain:

1. What is a GPIO?
2. INPUT vs OUTPUT?
3. Why use INPUT_PULLUP?
4. What is ADC?
5. What is PWM?
6. What is UART?
7. What are SDA/SCL?
8. What are MOSI/MISO/SCK/CS?
9. How does Wi-Fi connect an ESP32 to a LAN?
10. What is DHCP?
11. What is an IP address?
12. What is RSSI?
13. What is HTTP?
14. GET vs POST?
15. What is JSON?
16. Why should firmware avoid long `delay()` calls?
17. How do you handle Wi-Fi loss?
18. How do you debug a sensor?
19. Arduino-ESP32 vs ESP-IDF?
20. Why should credentials never be committed to GitHub?

### Completion condition

You can independently build the **Environmental Node** project and explain every hardware and software decision.

Then move to **Phase 4 — Sensors, Actuators and Embedded Interfaces**.
