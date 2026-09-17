# Phase 4 — Sensors, Actuators & Embedded Interfaces

> **Goal:** Turn the ESP32 from a development board into a reliable physical IoT device.
>
> **Prerequisite:** Phase 2 electronics + Phase 3 ESP32.
>
> **Outcome:** You can select, wire, read, validate and integrate sensors; control actuators safely; understand datasheets; handle I²C/SPI/UART devices; and design a reusable sensor/actuator subsystem for the thesis.

---

# 1. Exact resources

## Resource A — Espressif Arduino-ESP32 documentation

https://docs.espressif.com/projects/arduino-esp32/en/latest/

Use it as the reference for:

- GPIO
- ADC
- PWM/LEDC
- I²C
- SPI
- UART

## Resource B — ESP-IDF Programming Guide

https://docs.espressif.com/projects/esp-idf/en/latest/esp32/

Use it when you need lower-level peripheral control.

## Resource C — Wokwi

https://wokwi.com/

Use it for circuit/firmware simulation before hardware experiments.

## Resource D — Adafruit Learning System

https://learn.adafruit.com/

Use individual sensor tutorials when your exact component is supported.

The important rule:

**Use tutorials for wiring examples; use the component's datasheet for electrical truth.**

## Resource E — SparkFun tutorials

https://learn.sparkfun.com/tutorials

Use these for practical electronics explanations, especially:

- I²C
- SPI
- UART
- sensors
- pull-ups
- breakout boards

---

# 2. The sensor mindset

Never approach a sensor as:

> "Which library do I install?"

Instead:

```text
What am I measuring?
        ↓
What physical quantity?
        ↓
Accuracy required?
        ↓
Measurement range?
        ↓
Interface?
        ↓
Voltage?
        ↓
Current?
        ↓
Sampling rate?
        ↓
Environmental limitations?
        ↓
How will I validate it?
```

This is the mindset you need for a thesis.

---

# 3. Sensor categories

Learn the difference between:

### Digital sensors

They communicate using a protocol.

Examples:

- I²C
- SPI
- UART
- 1-Wire

### Analog sensors

They output a voltage/current that represents a physical quantity.

The ESP32 reads it using an ADC or appropriate external converter.

### Smart sensors

They may contain their own:

- ADC
- compensation
- calibration
- digital interface
- processing

---

# 4. Sensor specifications

For every sensor, learn to find these in the datasheet:

- supply voltage
- current consumption
- operating temperature
- measurement range
- accuracy
- resolution
- sampling rate
- interface
- address
- timing
- startup requirements
- calibration requirements
- error behavior

Example:

Do not write:

> "This sensor is accurate."

Write:

> "According to its datasheet, the specified accuracy is X under the stated conditions."

That difference matters in academic work.

---

# 5. Datasheet reading

A datasheet is not something you read from beginning to end.

For a new component, find:

1. Absolute maximum ratings
2. Recommended operating conditions
3. Pinout
4. Electrical characteristics
5. Communication protocol
6. Timing
7. Register map if applicable
8. Typical application circuit
9. Calibration/accuracy information

---

# 6. GPIO sensors

Start with simple digital sensors/devices.

Examples:

- PIR motion sensor
- digital switch
- limit switch
- digital alarm output

Typical:

```text
Sensor VCC → appropriate supply
Sensor GND → GND
Sensor OUT → ESP32 GPIO
```

Test:

```text
LOW → no event
HIGH → event
```

Do not assume the polarity; verify the module's documentation.

---

# 7. Analog sensors

Connect an analog output to an appropriate ADC input.

Architecture:

```text
Physical quantity
      ↓
Sensor
      ↓
Analog voltage
      ↓
ESP32 ADC
      ↓
digital value
      ↓
calculation
      ↓
measurement
```

You must understand that the raw ADC value is not automatically a temperature, light level or pressure value.

You need a conversion relationship.

---

# 8. Calibration

Real sensors are not perfect.

You may have:

- offset error
- gain error
- noise
- drift
- environmental effects

Simple calibration:

```text
measured = raw × scale + offset
```

Your thesis may eventually need more advanced calibration.

---

# 9. Noise

Sensor readings may look like:

```text
24.1
24.3
24.0
24.8
23.9
24.2
```

This does not necessarily mean the physical environment changed that much.

Learn:

- electrical noise
- quantization
- sensor noise
- interference
- sampling effects

---

# 10. Filtering

Start with:

## Moving average

Example:

```text
samples:
24.1
24.3
24.0
24.2
24.4

average:
24.2
```

Learn:

- moving average
- median filter
- exponential moving average

Do not blindly filter everything. Filtering introduces delay and can hide real changes.

---

# 11. Sampling

Understand:

- sampling frequency
- sampling interval
- aliasing conceptually
- response time
- sensor update rate

Example:

If you only need room temperature, measuring every 1 ms is usually unnecessary.

For motion detection, response requirements may be very different.

Your sampling rate should come from the application's requirements.

---

# 12. I²C sensor integration

For an I²C sensor:

```text
ESP32
 │
 ├── SDA
 ├── SCL
 ├── VCC
 └── GND
       │
       Sensor
```

Workflow:

```text
Wire
 ↓
I²C scanner
 ↓
confirm address
 ↓
initialize sensor
 ↓
read data
 ↓
validate data
 ↓
log data
```

Do this for at least one real sensor.

---

# 13. I²C pull-ups

I²C normally requires pull-up resistors on SDA and SCL.

Many breakout boards already include them.

This means:

**Do not automatically add another pair of pull-ups.**

Too many parallel pull-ups can make the effective resistance too low.

Learn to check the module schematic/documentation.

---

# 14. Multiple I²C devices

One of the strengths of I²C is multiple devices on one bus.

Example:

```text
              ┌── Temp sensor
              │
SDA ──────────┼── OLED
              │
              └── Light sensor

SCL ────────── same bus
```

But devices need unique addresses.

If two devices use the same fixed address, possible solutions include:

- alternate address pin
- I²C multiplexer
- separate bus
- different device

---

# 15. SPI sensor integration

Understand:

```text
SCK
MOSI
MISO
CS
```

For multiple SPI devices:

```text
SCK  ─────────────── all devices
MOSI ─────────────── all devices
MISO ─────────────── all devices
CS1  ─────────────── Device 1
CS2  ─────────────── Device 2
```

Only one device should normally be selected at a time.

---

# 16. UART sensors

Some modules communicate through UART.

Learn:

- baud rate
- framing
- TX/RX
- message format
- checksum if used
- timeout
- packet parsing

Do not assume that receiving bytes means the data is valid.

Parse and validate the packet.

---

# 17. Sensor data validation

Every reading should have sanity checks.

Example:

```text
Temperature:
valid range = application-dependent

if impossible:
    reject reading
```

Also detect:

- NaN
- missing data
- communication timeout
- CRC/checksum failure
- out-of-range data

---

# 18. Sensor state machine

A robust sensor subsystem can use states:

```text
UNINITIALIZED
      ↓
INITIALIZING
      ↓
READY
      ↓
READING
      ↓
VALIDATING
      ↓
VALID
```

On failure:

```text
ERROR
 ↓
RETRY
 ↓
READY
```

This is much better than:

```cpp
readSensor();
```

with no error handling.

---

# 19. Actuators

Now move from measuring to controlling.

Common actuators:

- LED
- buzzer
- relay
- servo
- DC motor
- fan
- solenoid

---

# 20. GPIO current limits

A GPIO is a logic output.

It is NOT a general-purpose power supply.

Do not use a GPIO to directly drive:

- large motor
- fan
- pump
- solenoid
- high-current relay coil

Use a suitable driver.

---

# 21. Transistor/MOSFET switching

Basic concept:

```text
ESP32 GPIO
    ↓
Gate/Base
    ↓
MOSFET/Transistor
    ↓
Load
    ↓
External supply
```

The microcontroller controls the switch.

The load receives power from an appropriate supply.

---

# 22. Relay

A relay provides electrical isolation in appropriate designs and allows low-voltage control of a separate load.

But a relay module may itself contain:

- transistor
- diode
- optocoupler
- regulator
- indicator LED

Read the module documentation.

Never assume every relay board is safe or isolated simply because it has a relay.

---

# 23. Inductive loads

Motors, solenoids and relay coils are inductive.

When switched off, they can generate a voltage spike.

Use appropriate suppression such as a flyback diode for suitable DC coil circuits.

Concept:

```text
Supply ───── Coil ───── Switch
             │
             └─ Flyback protection
```

Use a proper driver design.

---

# 24. Buzzer

Distinguish:

### Active buzzer

Often produces a tone when powered.

### Passive buzzer

Requires a changing signal/PWM to generate a tone.

Use PWM when appropriate.

---

# 25. Servo

A hobby servo typically expects a control pulse signal.

You need to understand:

- pulse timing
- PWM/servo control
- external power
- common ground

Important:

Do not assume the ESP32 board's 3.3 V pin can supply whatever current the servo needs.

Power the servo according to its requirements.

---

# 26. Motors

A motor requires a driver.

Architecture:

```text
ESP32
 ↓
Motor driver
 ↓
Motor
 ↑
External power
```

Learn the difference between:

- H-bridge
- MOSFET low-side switch
- motor controller

For your thesis, you do not need advanced motor control unless the application requires it.

---

# 27. Displays

If your hardware includes an OLED/LCD, learn:

- I²C/SPI interface
- display initialization
- text
- numbers
- simple graphics

A display is useful for debugging sensor systems without a computer.

---

# 28. Real sensor project

Build:

# Environmental Monitoring Node

Hardware:

```text
ESP32
├── Temperature/Humidity sensor
├── Light sensor
├── OLED
├── Button
├── LED
└── Buzzer
```

Behavior:

```text
Boot
 ↓
Initialize hardware
 ↓
Check each device
 ↓
Read sensors
 ↓
Filter/validate
 ↓
Display readings
 ↓
Evaluate thresholds
 ↓
LED/buzzer alert
 ↓
Repeat
```

---

# 29. Add thresholds

Example:

```text
temperature > threshold
       ↓
LED ON
       ↓
buzzer
```

But don't hard-code everything.

Use configuration:

```cpp
float temperatureHighThreshold = 30.0;
```

Later move configuration to a dedicated structure/file.

---

# 30. Add hysteresis

Suppose:

```text
fan ON at 30°C
fan OFF at 29°C
```

This prevents rapid switching around one threshold.

Without hysteresis:

```text
29.9
30.0
29.9
30.0
29.9
```

could repeatedly switch the actuator.

With hysteresis:

```text
ON threshold = 30
OFF threshold = 29
```

the system is more stable.

---

# 31. Sensor fusion — introduction

Later your thesis may combine multiple measurements.

Example:

```text
Temperature
Humidity
Light
Motion
      ↓
Decision logic
      ↓
System state
```

You do not need machine learning yet.

Start with deterministic rules.

---

# 32. Timing architecture

Avoid:

```text
read everything
delay(10000)
read everything
delay(10000)
```

Instead assign intervals:

```text
Temperature → every 2 s
Light       → every 1 s
Display     → every 500 ms
Health      → every 5 s
Network     → continuously
```

Use non-blocking timing or later FreeRTOS tasks.

---

# 33. Device health monitoring

Your device should know if something is wrong.

Track:

```text
uptime
free heap
Wi-Fi status
sensor status
last successful reading
error count
reboot count
```

Example JSON:

```json
{
  "device_id": "esp32-01",
  "uptime": 5421,
  "wifi": true,
  "sensor_ok": true,
  "sensor_errors": 0
}
```

This will become valuable in later IoT/security phases.

---

# 34. Power budgeting

Create a simple table:

| Component | Voltage | Typical current | Peak/current concern |
|---|---:|---:|---|
| ESP32 | board-specific | measure/check datasheet | Wi-Fi peaks |
| Sensor | datasheet | datasheet | usually low |
| OLED | datasheet | datasheet | depends on display |
| Buzzer | datasheet | datasheet | check |
| Servo | datasheet | datasheet | can be high |

Never design power from guesses.

For every component, consult its documentation.

---

# 35. Practical lab sequence

Do these in order.

## Lab 1

Digital motion/event sensor → GPIO.

## Lab 2

Analog sensor → ADC.

## Lab 3

I²C sensor → ESP32.

## Lab 4

Two I²C devices → same bus.

## Lab 5

SPI peripheral.

## Lab 6

UART peripheral.

## Lab 7

OLED display.

## Lab 8

Buzzer threshold alert.

## Lab 9

Relay/MOSFET controlled load.

## Lab 10

Complete monitoring node.

---

# 36. Troubleshooting procedure

When a sensor doesn't work, NEVER immediately rewrite the entire program.

Use this order:

```text
1. Power
 ↓
2. Ground
 ↓
3. Wiring
 ↓
4. Correct GPIO
 ↓
5. Communication address
 ↓
6. Bus speed
 ↓
7. Library initialization
 ↓
8. Raw communication
 ↓
9. Data conversion
 ↓
10. Application logic
```

For I²C:

```text
Power
 ↓
I²C scanner
 ↓
Address
 ↓
Device initialization
 ↓
Read register/data
```

This saves enormous amounts of time.

---

# 37. Logic analyzer — optional but recommended

Later, buy/use a cheap logic analyzer if your budget permits.

It can help visualize:

- UART
- I²C
- SPI
- PWM

For example, instead of guessing whether I²C works:

```text
SCL: _|-|_|-|_|-|_
SDA: __|___|__|___
```

you can inspect actual bus activity.

Do not buy one immediately if your current hardware budget is already fixed. It is an optional later tool.

---

# 38. Datasheet assignment

Choose **one sensor you actually own**.

Create:

`docs/datasheet-analysis.md`

Answer:

1. Exact part number?
2. Manufacturer?
3. Supply voltage?
4. Maximum voltage?
5. Current consumption?
6. Interface?
7. Address?
8. Measurement range?
9. Accuracy?
10. Resolution?
11. Sampling rate?
12. Operating temperature?
13. Required pull-ups?
14. Startup time?
15. Calibration requirements?
16. Known limitations?

This is a very good thesis skill.

---

# 39. Final project

# ESP32 Smart Monitoring & Control Node

## Hardware

Use your actual purchased components.

Target:

```text
                ┌──────────────┐
                │    ESP32     │
                └──────┬───────┘
                       │
       ┌───────────────┼────────────────┐
       ↓               ↓                ↓
   Sensors          Display          Inputs
       │               │                │
       └───────────────┼────────────────┘
                       ↓
                  Decision Logic
                       ↓
                ┌──────┴──────┐
                ↓             ↓
              LED          Buzzer/Relay
```

## Requirements

The final project must:

- initialize all hardware
- detect initialization failures
- read sensors
- validate readings
- apply basic filtering where justified
- display values
- control an actuator
- use thresholds
- use hysteresis where appropriate
- expose device health
- log errors
- avoid unnecessary blocking delays
- document the wiring
- document the power budget

---

# 40. GitHub repository

Create:

`esp32-sensor-actuator-lab`

Structure:

```text
esp32-sensor-actuator-lab/
├── README.md
├── hardware/
│   ├── wiring.md
│   ├── power-budget.md
│   └── diagrams/
├── firmware/
│   ├── src/
│   └── include/
├── sensors/
│   ├── sensor-1.md
│   └── sensor-2.md
├── datasheets/
├── tests/
├── photos/
└── docs/
```

README must contain:

```text
Project overview
Architecture
Hardware list
Wiring
Power budget
Sensor specifications
Firmware architecture
Data validation
Actuator safety
Testing
Known limitations
Future improvements
```

---

# 41. Testing checklist

Test:

### Sensor

- normal value
- minimum/maximum expected value
- disconnected sensor
- invalid data
- repeated readings

### Button

- press
- release
- rapid press
- bounce behavior

### Actuator

- ON
- OFF
- repeated switching
- power stability

### Network preparation

Even before MQTT, verify:

- Wi-Fi remains connected
- device continues operating if Wi-Fi disappears
- sensors continue working without the network

This separation is important:

**Physical sensing should not completely depend on Internet connectivity.**

---

# 42. Phase 4 final exam

You should be able to answer:

1. What is a sensor?
2. Analog vs digital sensor?
3. What is a transducer?
4. What is ADC?
5. What is sensor resolution?
6. Accuracy vs precision?
7. What is calibration?
8. What is sensor noise?
9. Why filter sensor data?
10. What is sampling frequency?
11. Why are I²C pull-ups needed?
12. Why can two I²C devices conflict?
13. What does CS do in SPI?
14. What are UART framing parameters?
15. Why shouldn't a GPIO drive a motor directly?
16. Why does an inductive load need protection?
17. What is a MOSFET used for?
18. What is a relay?
19. What is hysteresis?
20. Why is power budgeting important?
21. How would you troubleshoot a dead sensor?
22. How would you detect a disconnected sensor?
23. Why should actuator power sometimes be separate from MCU power?
24. What information should you extract from a datasheet?
25. Why shouldn't a library be treated as a substitute for a datasheet?

---

# 43. Phase 4 completion criteria

You are DONE only when you can independently build and explain:

### Required

- Digital input
- Digital output
- ADC sensor
- PWM actuator
- I²C device
- UART device
- at least one SPI device if available
- sensor validation
- threshold + hysteresis
- actuator control
- basic power budget

### Final deliverable

A working:

**ESP32 Smart Monitoring & Control Node**

with a professional GitHub repository and documentation.

After this phase you are ready for:

# Phase 5 — Networking for IoT

You should then connect your physical ESP32 system to your existing networking knowledge and begin the transition from an embedded device to a genuine IoT system.
