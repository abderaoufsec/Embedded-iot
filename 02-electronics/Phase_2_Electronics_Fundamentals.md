# Phase 2 — Electronics Fundamentals for Embedded IoT

> **Goal:** Understand enough electronics to safely build, debug, and modify ESP32-based embedded systems.
>
> **Prerequisite:** Phase 1 C fundamentals. You do **not** need advanced physics.
>
> **Outcome:** You can read a simple schematic, use a breadboard and multimeter, calculate resistor values, understand 3.3 V logic, use GPIO/ADC/PWM, and understand UART/I²C/SPI at a practical level.

---

## 1. What you must be able to do

By the end of this phase you should be able to:

- Explain voltage, current, resistance, power and ground.
- Use Ohm's law and the electrical power equations.
- Distinguish series and parallel circuits.
- Read resistor values and choose safe LED resistors.
- Understand why LEDs need current limiting.
- Explain digital HIGH/LOW and analog values.
- Understand 3.3 V logic and why 5 V can be dangerous for some ESP32 pins.
- Use pull-up and pull-down resistors.
- Understand floating inputs and switch debouncing.
- Explain ADC, DAC and PWM.
- Explain UART, I²C and SPI.
- Use a breadboard correctly.
- Measure voltage, resistance and continuity with a multimeter.
- Recognize common wiring mistakes before powering a circuit.

---

# 2. Exact learning resources

## Resource A — Main video

### freeCodeCamp — Arduino Course for Beginners

https://www.youtube.com/watch?v=zJ-LqeX_fLU

Use the course for its electronics/microcontroller foundations:

1. Electricity basics
2. Voltage
3. Current
4. Resistance
5. Ohm's law
6. Power
7. Breadboards
8. Digital vs analog
9. GPIO
10. ADC
11. PWM

Do not try to memorize every Arduino-specific API yet. Your objective is electronics.

## Resource B — ESP32 official documentation

### Espressif Arduino-ESP32 documentation

https://docs.espressif.com/projects/arduino-esp32/en/latest/

Use it later in this phase to connect the electronics concepts to the ESP32:

- GPIO
- ADC
- PWM
- I2C
- SPI
- UART

## Resource C — Practical circuit simulation

### Wokwi

https://wokwi.com/

Use Wokwi whenever you want to test a circuit before connecting real hardware.

It is especially useful for:

- LEDs
- buttons
- potentiometers
- buzzers
- ESP32
- I2C displays
- sensors

---

# 3. Electricity fundamentals

## 3.1 Voltage

Voltage is electrical potential difference.

Think of it as the "push" that drives current through a circuit.

Unit:

**Volt (V)**

Examples:

- USB: commonly 5 V
- ESP32 logic: commonly 3.3 V
- AA battery: about 1.5 V nominal

Important:

**Voltage is measured between two points.**

A multimeter measuring voltage needs two probes.

---

## 3.2 Current

Current is the flow of electric charge.

Unit:

**Ampere (A)**

Small embedded circuits often use:

- mA = milliampere
- µA = microampere

1 A = 1000 mA.

---

## 3.3 Resistance

Resistance opposes current.

Unit:

**Ohm (Ω)**

The larger the resistance, the less current flows for the same voltage.

---

# 4. Ohm's law

Memorize:

**V = I × R**

Therefore:

**I = V / R**

**R = V / I**

Example:

You have a 3.3 V source and want approximately 10 mA through an LED.

I = 0.010 A

R = 3.3 / 0.010

R = 330 Ω

So a 330 Ω resistor is a reasonable starting value.

For an actual LED, remember that the LED itself has a forward voltage. A more accurate calculation is:

**R = (Vsupply − VLED) / I**

Example:

Vsupply = 3.3 V

VLED = 2.0 V

I = 0.005 A

R = (3.3 − 2.0) / 0.005

R = 260 Ω

Use the next common value, such as 270 Ω or 330 Ω.

---

# 5. Electrical power

Memorize:

**P = V × I**

Also:

**P = I²R**

**P = V²/R**

Unit:

**Watt (W)**

Example:

5 V × 0.2 A = 1 W.

This matters because components and power supplies have limits.

---

# 6. Ground

Ground (GND) is the reference point of a circuit.

For normal low-voltage embedded circuits, components communicating with an ESP32 usually need a common ground.

Example:

```text
ESP32 GND ───────── Sensor GND
ESP32 3V3 ───────── Sensor VCC
ESP32 GPIO ───────── Sensor signal
```

If two modules have separate grounds and no appropriate common reference, signals may not behave as expected.

---

# 7. Series vs parallel

## Series

```text
V+ ── R1 ── R2 ── LED ── GND
```

The same current flows through the series components.

Resistances:

**Rtotal = R1 + R2 + ...**

## Parallel

```text
       ┌── R1 ──┐
V+ ────┤        ├── GND
       └── R2 ──┘
```

Parallel branches share the same voltage.

For two resistors:

**1/Rtotal = 1/R1 + 1/R2**

---

# 8. Breadboards

Learn the internal connections of your breadboard before plugging anything in.

Typical layout:

```text
Power rail
+ + + + + + + +

Terminal area

a b c d e     f g h i j
• • • • •     • • • • •
• • • • •     • • • • •
• • • • •     • • • • •

Power rail
- - - - - - - -
```

The center gap normally separates the two sides.

## Rules

- Do not assume every breadboard's rails are connected end-to-end.
- Check the actual breadboard.
- Keep wiring short and organized.
- Turn power off before changing wiring.
- Never use a breadboard as a substitute for understanding the schematic.

---

# 9. Resistors

You should recognize:

- resistor symbol
- resistance value
- tolerance
- power rating
- color code

Learn the 4-band and 5-band resistor color codes.

At minimum, be able to identify common values:

- 100 Ω
- 220 Ω
- 330 Ω
- 470 Ω
- 1 kΩ
- 4.7 kΩ
- 10 kΩ
- 100 kΩ

These appear constantly in embedded work.

---

# 10. LEDs

An LED is a diode.

It has polarity.

Typical:

```text
Anode (+) ── LED ── Cathode (-)
```

Do not connect an LED directly to a GPIO without current limiting.

Typical beginner circuit:

```text
ESP32 GPIO
    │
   330Ω
    │
   LED
    │
   GND
```

---

# 11. Buttons

A basic button can connect a GPIO to HIGH or LOW.

Problem:

An input without a defined state can float.

Example:

```text
GPIO ───── Button ───── GND
```

Use a pull-up:

```text
3.3V
 │
10kΩ
 │
GPIO ───── Button ───── GND
```

When the button is open:

GPIO ≈ HIGH.

When pressed:

GPIO ≈ LOW.

The ESP32 also has internal pull-up/pull-down functionality for many GPIOs, so an external resistor is not always necessary.

---

# 12. Pull-up and pull-down resistors

## Pull-up

```text
3.3V
 │
 R
 │
GPIO
 │
Switch
 │
GND
```

Default = HIGH.

Pressed = LOW.

## Pull-down

```text
3.3V
 │
Switch
 │
GPIO
 │
 R
 │
GND
```

Default = LOW.

Pressed = HIGH.

You need to understand the electrical reason, not merely memorize the diagrams.

---

# 13. Switch debouncing

Mechanical switches do not transition perfectly once.

They can produce:

```text
HIGH
LOW
HIGH
LOW
LOW
```

within a very short time.

The microcontroller may interpret one press as multiple presses.

Solutions:

- software debounce
- hardware RC debounce
- state-change timing
- interrupt + debounce logic

For your first projects, software debounce is sufficient.

---

# 14. Digital vs analog

## Digital

Normally represents discrete states:

```text
LOW
HIGH
```

## Analog

Represents a continuous range.

Example:

A potentiometer can produce a range of voltages.

The ESP32 ADC converts voltage into a digital number.

Conceptually:

```text
Physical voltage
       ↓
      ADC
       ↓
Digital number
       ↓
Your program
```

---

# 15. ADC

ADC = Analog-to-Digital Converter.

It lets a microcontroller measure an analog voltage within the supported input range.

Example:

```text
Potentiometer
     │
     ↓
ESP32 ADC pin
     │
     ↓
digital reading
```

Do not assume every ESP32 ADC pin has identical behavior. Always check the exact board/chip documentation.

---

# 16. PWM

PWM = Pulse Width Modulation.

The output rapidly switches between HIGH and LOW.

Instead of:

```text
HIGH permanently
```

you produce:

```text
HIGH LOW HIGH LOW HIGH LOW
```

The ratio of HIGH time to the total period is the duty cycle.

Example:

```text
20% duty cycle
████....................

50%
██████████..............

80%
████████████████........
```

PWM is commonly used for:

- LED brightness
- motor control
- servo control
- power control

---

# 17. UART

UART is a simple serial communication method.

Typical:

```text
Device A TX ───────── RX Device B
Device A RX ───────── TX Device B
Device A GND ──────── GND Device B
```

Important concepts:

- TX
- RX
- baud rate
- data bits
- parity
- stop bits

Common baud rates:

- 9600
- 115200

TX and RX are normally crossed between two devices.

---

# 18. I²C

I²C normally uses two signal lines:

- SDA = data
- SCL = clock

Typical:

```text
ESP32 SDA ───────── Sensor SDA
ESP32 SCL ───────── Sensor SCL
ESP32 GND ───────── Sensor GND
```

I²C supports multiple devices on the same bus using addresses.

Example:

```text
             ┌── Temperature sensor
SDA ─────────┼── OLED
             └── Other sensor

SCL ───────── same bus
```

Learn:

- address
- master/controller
- target/peripheral
- SDA
- SCL
- pull-up resistors
- bus speed

---

# 19. SPI

SPI commonly uses:

- SCK
- MOSI
- MISO
- CS/SS

Typical:

```text
ESP32 SCK  ─── SCK  Sensor
ESP32 MOSI ─── MOSI Sensor
ESP32 MISO ─── MISO Sensor
ESP32 CS   ─── CS   Sensor
GND        ─── GND
```

SPI is generally faster than I²C and is common for displays, storage and sensors.

Learn:

- clock
- MOSI
- MISO
- chip select
- multiple devices
- clock polarity/phase conceptually

---

# 20. Multimeter skills

You should own/use a digital multimeter.

Learn these modes:

### DC voltage

Measure:

```text
V+ ↔ GND
```

### Resistance

Power must normally be OFF.

Never measure resistance on a powered circuit.

### Continuity

Use it to discover whether two points are electrically connected.

### Current

Be very careful.

Incorrect current measurement can short a power supply.

For now, focus on voltage, resistance and continuity.

---

# 21. Practical labs

Do these in order.

## Lab 1 — LED

Build:

```text
ESP32 GPIO → 330Ω → LED → GND
```

Goal:

- understand polarity
- understand resistor
- understand GPIO

## Lab 2 — Button

Build:

```text
GPIO → button → GND
```

Use an internal pull-up.

Goal:

- understand input
- understand HIGH/LOW
- understand pull-up

## Lab 3 — Potentiometer

Connect:

```text
3.3V
 │
Potentiometer
 │
GND

Wiper → ADC
```

Read the ADC.

Goal:

- analog voltage
- ADC

## Lab 4 — PWM LED

Use PWM to vary brightness.

Goal:

- frequency
- duty cycle
- output control

## Lab 5 — UART

Send sensor/debug messages through serial.

Goal:

- TX/RX
- baud rate
- serial debugging

## Lab 6 — I²C

Connect an I²C sensor or OLED.

Goal:

- SDA
- SCL
- address
- bus

## Lab 7 — SPI

Connect an SPI device if included in your hardware.

Goal:

- MOSI
- MISO
- SCK
- CS

---

# 22. Safety rules

Memorize these.

1. Never blindly connect 5 V to an ESP32 GPIO.
2. Check the exact ESP32 board's pin/input limits.
3. Always identify GND and VCC before wiring.
4. Never power a circuit when unsure about polarity.
5. Do not short 3.3 V to GND.
6. Do not connect an LED without current limiting.
7. Do not drive motors directly from a GPIO.
8. Use a suitable transistor/MOSFET/driver for higher-current loads.
9. Use a flyback diode where appropriate for inductive loads.
10. Turn power off before changing wiring.
11. Measure first if you are unsure.
12. Read the component datasheet.

---

# 23. Project — Electronics Test Board

Create one reusable breadboard setup containing:

- ESP32
- LED
- resistor
- button
- potentiometer
- buzzer
- one sensor
- optional OLED

Demonstrate:

```text
Button → LED
Potentiometer → ADC → Serial
PWM → LED brightness
Sensor → Serial
I²C → sensor/OLED
```

---

# 24. GitHub deliverable

Repository:

`embedded-electronics-labs`

Structure:

```text
embedded-electronics-labs/
├── README.md
├── 01-led/
├── 02-button/
├── 03-potentiometer-adc/
├── 04-pwm/
├── 05-uart/
├── 06-i2c/
├── 07-spi/
├── diagrams/
└── photos/
```

Every lab README should contain:

```text
Objective
Components
Circuit
Wiring table
How it works
Code
Expected result
Problems encountered
What I learned
```

---

# 25. Phase 2 final exam

Do not move to Phase 3 until you can answer these without searching:

1. What is voltage?
2. What is current?
3. What is resistance?
4. State Ohm's law.
5. Calculate the resistor for an LED.
6. Why does an LED need a resistor?
7. What is GND?
8. What is a floating GPIO?
9. Pull-up vs pull-down?
10. Why do buttons bounce?
11. What is ADC?
12. What is PWM?
13. What is UART?
14. What are SDA/SCL?
15. What are MOSI/MISO/SCK/CS?
16. Why can 5 V be dangerous to a 3.3 V GPIO?
17. Why can't a GPIO directly drive a large motor?
18. Why do devices communicating digitally normally need a common reference?
19. How would you troubleshoot an LED that does not turn on?
20. How would you troubleshoot an I²C sensor that is not detected?

### Completion condition

You are DONE when you can build the five core circuits without copying a tutorial:

- LED
- button
- potentiometer/ADC
- PWM LED
- I²C sensor

Then move to **Phase 3 — ESP32**.
