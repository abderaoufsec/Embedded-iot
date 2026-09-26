# Phase 7 — Sensors and Actuators

> **Goal:** Develop practical skills for working with sensors and actuators, including reading datasheets, calibrating sensors, filtering data, and driving loads safely—preparing for the IoT thesis project.
>
> **Prerequisite:** Phase 6 — ESP32
>
> **Outcome:** You can select, wire, and integrate sensors and actuators, understand datasheets, implement filtering and thresholds, and drive loads safely with appropriate protection.

---

## What You Will Learn

By completing this phase, you will understand:

- **Sensors vs Actuators:** Distinguishing between input and output devices
- **Analog vs Digital Sensors:** Different sensor types and interfaces
- **Sensor Measurements:** Voltage, current, resistance-based sensing
- **Sensor Datasheets:** How to read and interpret specifications
- **Sensor Specifications:** Range, resolution, accuracy, precision, sampling rate
- **Calibration:** How to calibrate sensors for accurate readings
- **Noise and Filtering:** Understanding signal noise and implementing filters
- **Thresholds and Hysteresis:** Implementing reliable trigger conditions
- **Pull-up Requirements:** When and why pull-up resistors are needed
- **Power Requirements:** Supply voltage, current consumption for sensors
- **Communication Interfaces:** I2C, SPI, UART, 1-Wire for sensors
- **Specific Sensors:** Potentiometer, DS18B20, ADXL345, ACS712
- **Actuators:** LED, buzzer, relay, DC motor
- **Motor Control:** PWM motor control, safe driving techniques
- **Protection Circuits:** Flyback diodes, current limiting, transistor ratings
- **Safety Considerations:** Never drive motors directly from GPIO, separate power supplies, common ground

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
- ✅ Understanding of ADC from Phase 6
- ✅ Understanding of I2C/SPI/UART from Phase 6
- ✅ Understanding of GPIO limits from Phase 6
- ✅ Understanding of transistor switching from Phase 4
- ✅ Understanding of flyback diodes from Phase 4

**Hardware required for labs:**
- ESP32 development board
- Potentiometer (10kΩ)
- Push button
- DS18B20 temperature sensor
- ADXL345 accelerometer
- ACS712 current sensor (5A or 20A module)
- LED and resistor (220Ω or 330Ω)
- Buzzer (passive or active)
- Small DC motor (low current, <500mA)
- Transistor (NPN, e.g., 2N2222 or BC547)
- Diode (1N4007 or 1N4148)
- Resistors (1kΩ, 10kΩ, etc.)
- Breadboard and jumper wires
- Multimeter
- Power supply (3-6V for motor, separate from ESP32)

---

## Learning Outcomes

After completing this phase, you will be able to:

- Distinguish between sensors and actuators
- Understand analog vs digital sensor interfaces
- Read and interpret sensor datasheets
- Understand sensor specifications (range, resolution, accuracy, precision)
- Calibrate sensors for accurate measurements
- Implement noise filtering for sensor data
- Implement thresholds with hysteresis to prevent false triggers
- Use appropriate pull-up resistors for sensors
- Calculate and provide adequate power for sensors
- Communicate with sensors via I2C, SPI, UART, and 1-Wire
- Read DS18B20 temperature sensor
- Read ADXL345 accelerometer
- Read ACS712 current sensor
- Implement sensor data filtering
- Drive LEDs and buzzers
- Drive relays and motors safely
- Implement PWM motor control
- Design protection circuits for inductive loads
- Integrate sensors and actuators into a complete system

---

## Concepts

### Sensors vs Actuators

**Sensors:** Devices that convert physical quantities to electrical signals
- **Input devices:** Provide data to the system
- **Examples:** Temperature, humidity, light, acceleration, current, voltage
- **Output:** Analog voltage, digital data, resistance change

**Actuators:** Devices that convert electrical signals to physical actions
- **Output devices:** Take actions based on system commands
- **Examples:** LEDs, buzzers, relays, motors, displays
- **Input:** Electrical signals (voltage, current, digital data)

**Why this matters:** Understanding the distinction is fundamental to embedded systems. Sensors provide data for the system to process; actuators allow the system to affect the physical world.

### Analog vs Digital Sensors

**Analog Sensors:** Provide continuous analog voltage output
- **Examples:** Potentiometer, thermistor, photoresistor, ACS712 current sensor
- **Interface:** ADC (analog-to-digital converter)
- **Characteristics:** Continuous output, susceptible to noise, require calibration

**Digital Sensors:** Provide digital data via communication protocols
- **Examples:** DS18B20 (1-Wire), ADXL345 (I2C/SPI), BME280 (I2C)
- **Interface:** I2C, SPI, UART, 1-Wire
- **Characteristics:** Digital output, less susceptible to noise, often include calibration

**Why this matters:** Different sensor types require different interfaces and processing techniques. Understanding both allows you to work with any sensor.

### Voltage/Current/Resistance Based Measurements

**Voltage-Based Sensors:** Output voltage proportional to measured quantity
- **Examples:** Potentiometer, thermistor (in voltage divider)
- **Interface:** ADC
- **Calculation:** Vout = f(measured quantity)

**Current-Based Sensors:** Output current proportional to measured quantity
- **Examples:** ACS712 current sensor (outputs voltage proportional to current)
- **Interface:** ADC (sensor includes current-to-voltage conversion)
- **Calculation:** I = f(Vout)

**Resistance-Based Sensors:** Change resistance based on measured quantity
- **Examples:** Thermistor, photoresistor
- **Interface:** Voltage divider with ADC
- **Calculation:** R = f(measured quantity), then Vout = f(R)

**Why this matters:** Understanding the underlying measurement principle helps you select appropriate sensors and interface circuits.

### Sensor Datasheets

**Key Sections in Datasheets:**
- **Electrical Characteristics:** Supply voltage, current consumption
- **Operating Conditions:** Temperature range, humidity range
- **Measurement Range:** Minimum and maximum measurable values
- **Accuracy:** How close reading is to true value
- **Resolution:** Smallest detectable change
- **Interface Specifications:** Pinout, communication protocol, timing
- **Application Notes:** Circuit examples, calibration procedures

**How to Read:**
1. Identify the measurement range (ensure it covers your application)
2. Check accuracy and resolution (ensure they meet your requirements)
3. Check supply voltage and current (ensure your system can provide)
4. Check interface requirements (ensure ESP32 can communicate)
5. Check application notes for recommended circuits

**Why this matters:** Datasheets contain all the information you need to use a sensor correctly. Reading them is essential for reliable sensor integration.

### Sensor Specifications

**Measurement Range:** Minimum and maximum values the sensor can measure
- **Example:** DS18B20: -55°C to +125°C
- **Why:** Ensures sensor covers your application's operating range

**Resolution:** Smallest detectable change in measurement
- **Example:** DS18B20: 0.0625°C (12-bit)
- **Why:** Determines precision of measurements

**Accuracy:** How close reading is to true value
- **Example:** DS18B20: ±0.5°C (typical)
- **Why:** Determines measurement error

**Precision:** Repeatability of measurements
- **Example:** DS18B20: ±0.1°C (typical)
- **Why:** Determines consistency of readings

**Sampling Rate:** How fast sensor can provide new measurements
- **Example:** ADXL345: up to 3200Hz
- **Why:** Determines how fast you can capture changes

**Why this matters:** Understanding specifications helps you select the right sensor for your application and interpret sensor data correctly.

### Calibration

**What is Calibration:** Adjusting sensor output to match known reference values

**Types of Calibration:**
- **Offset Calibration:** Add constant to correct zero error
- **Gain Calibration:** Multiply by factor to correct scale error
- **Multi-point Calibration:** Use multiple reference points for better accuracy

**Calibration Process:**
1. Measure known reference values
2. Compare to sensor readings
3. Calculate correction factors
4. Apply correction factors to future readings

**Example:**
- Known temperature: 25°C (thermometer)
- Sensor reads: 26°C
- Offset error: +1°C
- Correction: subtract 1°C from all readings

**Why this matters:** Calibration improves measurement accuracy. Many sensors require calibration for accurate readings.

### Noise and Filtering

**Noise:** Unwanted random variations in sensor data
- **Sources:** Electrical interference, thermal noise, electromagnetic interference
- **Effect:** Inaccurate readings, unreliable operation

**Filtering:** Reducing noise to improve data quality

**Simple Moving Average:**
```c
#define FILTER_SIZE 5
int buffer[FILTER_SIZE];
int index = 0;
int sum = 0;

int filter(int new_value) {
  sum = sum - buffer[index] + new_value;
  buffer[index] = new_value;
  index = (index + 1) % FILTER_SIZE;
  return sum / FILTER_SIZE;
}
```

**Why this matters:** Filtering improves sensor data quality. Most real-world sensor data contains noise that must be filtered for reliable operation.

### Thresholds and Hysteresis

**Threshold:** A value that triggers an action when crossed
- **Example:** Alert when temperature > 30°C

**Hysteresis:** Different thresholds for rising and falling values
- **Purpose:** Prevent rapid switching when signal is near threshold
- **Example:** Turn on heater at 25°C, turn off at 27°C (2°C hysteresis)

**Without Hysteresis:**
```
Temperature = 25.1°C → Turn on heater
Temperature = 24.9°C → Turn off heater
Temperature = 25.1°C → Turn on heater
Rapid switching!
```

**With Hysteresis:**
```
Temperature = 25.1°C → Turn on heater
Temperature = 27.0°C → Turn off heater
Temperature = 24.9°C → Turn on heater
Stable operation!
```

**Why this matters:** Hysteresis prevents rapid switching and improves system stability. Essential for control systems.

### Pull-up Requirements

**When Pull-ups are Needed:**
- Open-drain outputs (I2C SDA/SCL)
- Buttons and switches
- 1-Wire interface (DS18B20)
- Some sensor outputs

**Internal vs External Pull-ups:**
- **Internal:** ESP32 has built-in pull-up/pull-down resistors (typically 10kΩ-50kΩ)
- **External:** Physical resistors on the board (typically 4.7kΩ for I2C)

**I2C Pull-ups:**
- Required for I2C bus
- Typical value: 4.7kΩ
- Connected to VCC (3.3V)
- Some ESP32 boards have built-in pull-ups on I2C pins

**Why this matters:** Without pull-ups, open-drain outputs and buttons will float, causing unpredictable readings.

### Power Requirements

**Supply Voltage:** Voltage required for sensor operation
- **Example:** DS18B20: 3.0V to 5.5V
- **Check:** Sensor datasheet
- **Match:** Ensure ESP32 or external supply can provide required voltage

**Current Consumption:** Current drawn by sensor
- **Example:** DS18B20: 1mA (active), <1µA (standby)
- **Check:** Sensor datasheet
- **Ensure:** Power supply can provide required current

**Low-Power Sensors:**
- Many sensors have low-power modes
- Useful for battery-powered applications
- ESP32 can wake sensors on demand

**Why this matters:** Inadequate power supply causes sensor malfunction or failure. ESP32 has limited current capability—external power may be needed for high-current sensors.

### Sensor Communication Interfaces

**I2C:**
- **Characteristics:** 2-wire (SDA, SCL), multi-device, moderate speed
- **Examples:** ADXL345, BME280, OLED displays
- **Pull-ups:** Required (typically 4.7kΩ)
- **ESP32:** 2 I2C controllers

**SPI:**
- **Characteristics:** 4-wire (SCK, MOSI, MISO, CS), high speed, point-to-point
- **Examples:** SD cards, high-speed sensors
- **No pull-ups needed:** Synchronous with clock
- **ESP32:** 4 SPI controllers

**UART:**
- **Characteristics:** TX/RX, point-to-point, moderate speed
- **Examples:** GPS modules, some sensors
- **No pull-ups needed**
- **ESP32:** 3 UART controllers

**1-Wire:**
- **Characteristics:** Single wire + ground, low speed, multi-device
- **Examples:** DS18B20 temperature sensor
- **Pull-up:** Required (typically 4.7kΩ)
- **ESP32:** Software implementation (not hardware peripheral)

**Why this matters:** Different sensors use different interfaces. Understanding each interface allows you to integrate any sensor.

---

## Specific Sensors

### Potentiometer

**Type:** Analog (voltage-based)
**Measurement:** Position (variable resistance)
**Interface:** ADC
**Range:** 0% to 100% (or angle in degrees)
**Resolution:** Limited by ADC resolution (ESP32: 12-bit = 4096 steps)
**Circuit:** Voltage divider
**Applications:** User input, adjustable reference, calibration

**ESP32 Implementation:**
```cpp
const int potPin = 34;  // ADC1_CH6

void setup() {
  analogReadResolution(12);
}

void loop() {
  int adcValue = analogRead(potPin);
  float voltage = adcValue * 3.3 / 4095.0;
  float percentage = adcValue * 100.0 / 4095.0;
}
```

**Why this matters:** Potentiometers are simple analog sensors that teach voltage division and ADC concepts.

### Push Button

**Type:** Digital (switch)
**Measurement:** State (pressed/not pressed)
**Interface:** GPIO
**Range:** Binary (0 or 1)
**Circuit:** Pull-up or pull-down resistor
**Applications:** User input, mode selection, triggers

**ESP32 Implementation:**
```cpp
const int buttonPin = 4;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    // Button pressed
  }
}
```

**Why this matters:** Buttons are fundamental input devices that teach GPIO input and debouncing.

### DS18B20 Temperature Sensor

**Type:** Digital (1-Wire)
**Measurement:** Temperature
**Interface:** 1-Wire
**Range:** -55°C to +125°C
**Resolution:** 9 to 12 bits (configurable)
**Accuracy:** ±0.5°C (typical)
**Supply:** 3.0V to 5.5V
**Pull-up:** Required (4.7kΩ typically)
**Applications:** Temperature monitoring, environmental sensing

**Circuit:**
```
ESP32 GPIO (e.g., GPIO4)
    │
   Resistor (4.7kΩ pull-up)
    │
DS18B20 Data
    │
DS18B20 VCC (3.3V or 5V)
    │
DS18B20 GND
ESP32 GND (common)
```

**ESP32 Implementation (Arduino-ESP32):**
```cpp
#include <OneWire.h>
#include <DallasTemperature.h>

OneWire oneWire(4);
DallasTemperature sensors(&oneWire);

void setup() {
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  Serial.println(tempC);
}
```

**Why this matters:** DS18B20 is a popular digital temperature sensor. It teaches 1-Wire communication and digital sensor interfacing.

### ADXL345 Accelerometer

**Type:** Digital (I2C or SPI)
**Measurement:** Acceleration (X, Y, Z axes)
**Interface:** I2C or SPI
**Range:** ±2g, ±4g, ±8g, ±16g (configurable)
**Resolution:** 10-bit or 13-bit (configurable)
**Supply:** 2.0V to 3.6V
**Pull-ups:** Required for I2C (4.7kΩ)
**Applications:** Motion detection, tilt sensing, vibration monitoring

**Circuit (I2C):**
```
ESP32 GPIO21 (SDA) ─── ADXL345 SDA
ESP32 GPIO22 (SCL) ─── ADXL345 SCL
ESP32 3.3V ────────── ADXL345 VCC
ESP32 GND ────────── ADXL345 GND
CS ────────────────── ADXL345 CS (to 3.3V for I2C)
```

**ESP32 Implementation (Arduino-ESP32):**
```cpp
#include <Wire.h>
#include <Adafruit_ADXL345.h>

Adafruit_ADXL345 accel = Adafruit_ADXL345(12345);

void setup() {
  Wire.begin(21, 22);
  accel.begin();
  accel.setRange(ADXL345_RANGE_2_G);
}

void loop() {
  accel.read();
  Serial.print("X: "); Serial.print(accel.x);
  Serial.print(" Y: "); Serial.print(accel.y);
  Serial.print(" Z: "); Serial.println(accel.z);
}
```

**Why this matters:** ADXL345 is a popular accelerometer for motion sensing. It teaches I2C communication and multi-axis sensor reading.

### ACS712 Current Sensor

**Type:** Analog (current-to-voltage)
**Measurement:** Current
**Interface:** ADC
**Range:** Depends on model (5A, 20A, 30A)
**Resolution:** Depends on ADC resolution
**Sensitivity:** 185mV/A (5A model), 100mV/A (20A model), 66mV/A (30A model)
**Supply:** 5V (typical)
**Output:** 2.5V at 0A (VCC/2), varies ±185mV/A
**Applications:** Current monitoring, power measurement, motor monitoring

**Circuit:**
```
ACS712
    │
Current (through integrated conductor)
    │
VCC (5V)
    │
GND
    │
VOUT (to ESP32 ADC)
```

**ESP32 Implementation:**
```cpp
const int currentPin = 34;  // ADC1_CH6
const float sensitivity = 0.185;  // 185mV/A for 5A model

void setup() {
  analogReadResolution(12);
}

void loop() {
  int adcValue = analogRead(currentPin);
  float voltage = adcValue * 5.0 / 4095.0;  // Assuming 5V reference
  float offset = 2.5;  // VCC/2
  float current = (voltage - offset) / sensitivity;
  Serial.println(current);
}
```

**Important Notes:**
- ACS712 requires 5V supply
- ESP32 ADC is 3.3V max—voltage divider or level shifter may be needed
- Check if ACS712 output exceeds ESP32 ADC range
- Calibration may be needed for zero-current offset

**Why this matters:** ACS712 is used for current monitoring in the thesis project. It teaches current sensing and ADC calibration.

---

## Actuators

### LED

**Type:** Actuator (light output)
**Control:** Digital (on/off) or PWM (brightness)
**Interface:** GPIO or PWM
**Current:** 10-20mA typical
**Voltage:** 1.8V to 3.3V forward voltage
**Circuit:** Current limiting resistor required
**Applications:** Indication, user feedback, lighting

**ESP32 Implementation:**
```cpp
const int ledPin = 2;

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

**Safety:**
- Always use current limiting resistor
- Don't exceed GPIO current limit

**Why this matters:** LEDs are the simplest actuators. They teach GPIO output and PWM control.

### Buzzer

**Type:** Actuator (sound output)
**Control:** Digital (on/off) or PWM (tone/frequency)
**Interface:** GPIO or PWM
**Types:**
- **Active buzzer:** Has oscillator, drive with DC voltage
- **Passive buzzer:** No oscillator, drive with PWM signal
**Current:** 10-30mA typical
**Voltage:** 3V to 12V (check datasheet)
**Circuit:** May need transistor if current exceeds GPIO limit
**Applications:** Audible alerts, user feedback

**ESP32 Implementation (Active Buzzer):**
```cpp
const int buzzerPin = 2;

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  digitalWrite(buzzerPin, HIGH);
  delay(100);
  digitalWrite(buzzerPin, LOW);
  delay(1000);
}
```

**ESP32 Implementation (Passive Buzzer with PWM):**
```cpp
const int buzzerPin = 2;
const int pwmChannel = 0;

void setup() {
  ledcSetup(pwmChannel, 2000, 8);  // 2kHz tone
  ledcAttachPin(buzzerPin, pwmChannel);
}

void loop() {
  ledcWrite(pwmChannel, 128);  // 50% duty cycle
  delay(500);
  ledcWrite(pwmChannel, 0);
  delay(500);
}
```

**Safety:**
- Check buzzer voltage and current requirements
- Use transistor if current exceeds GPIO limit
- Check if buzzer requires PWM or DC

**Why this matters:** Buzzers provide audible feedback. They teach PWM signal generation and current considerations.

### Relay

**Type:** Actuator (switch)
**Control:** Digital (on/off)
**Interface:** GPIO (with transistor if needed)
**Coil Voltage:** 5V or 12V typical
**Coil Current:** 50-100mA typical
**Contact Rating:** Depends on relay (e.g., 10A 250V AC)
**Circuit:** Requires transistor and flyback diode
**Applications:** Switching high-power loads, AC mains, high-current DC

**Circuit:**
```
ESP32 GPIO
    │
   Resistor (1kΩ)
    │
   Transistor base
    │
Transistor emitter ─── GND
    │
Transistor collector
    │
   Relay coil
    │
Relay power supply positive (+)
    │
   Diode (cathode to relay +, anode to collector)
```

**ESP32 Implementation:**
```cpp
const int relayPin = 2;

void setup() {
  pinMode(relayPin, OUTPUT);
}

void loop() {
  digitalWrite(relayPin, HIGH);  // Relay on
  delay(1000);
  digitalWrite(relayPin, LOW);   // Relay off
  delay(1000);
}
```

**Safety:**
- Never drive relay coil directly from GPIO
- Use transistor to switch relay coil
- Always use flyback diode (inductive load)
- Separate power supply for relay coil
- Common ground required
- Check relay contact rating for load

**Why this matters:** Relays allow switching high-power loads. They teach inductive load protection and transistor switching.

### DC Motor

**Type:** Actuator (motion)
**Control:** Digital (on/off) or PWM (speed)
**Interface:** GPIO (with transistor or motor driver)
**Voltage:** 3V to 12V typical
**Current:** 100-500mA typical (depends on motor)
**Startup Current:** 2-3x running current
**Circuit:** Requires transistor or motor driver, flyback diode
**Applications:** Robotics, fans, pumps, motion control

**Critical Safety Rules:**
1. **NEVER drive motor directly from ESP32 GPIO**
2. **Use transistor or motor driver**
3. **Separate motor power supply when required**
4. **Common ground between ESP32 and motor supply**
5. **Flyback diode required** (inductive load)
6. **Check transistor current rating** (including startup current)
7. **Check motor current requirements**

**Circuit (with transistor):**
```
ESP32 GPIO
    │
   Resistor (1kΩ)
    │
   Transistor base
    │
Transistor emitter ─── GND (common with motor supply GND)
    │
Transistor collector
    │
   Motor ─── Motor power supply positive (+)
    │
   Diode (cathode to motor +, anode to collector, in parallel with motor)
```

**ESP32 Implementation (PWM Speed Control):**
```cpp
const int motorPin = 2;
const int pwmChannel = 0;

void setup() {
  ledcSetup(pwmChannel, 1000, 8);  // 1kHz PWM
  ledcAttachPin(motorPin, pwmChannel);
}

void loop() {
  // 50% speed
  ledcWrite(pwmChannel, 128);
  delay(2000);
  
  // Stop
  ledcWrite(pwmChannel, 0);
  delay(1000);
}
```

**Transistor Selection:**
- **2N2222:** Up to 800mA
- **BC547:** Up to 100mA
- **MOSFET (e.g., IRF540):** Higher current
- **Motor Driver Module:** Simplifies design

**Base Resistor Calculation:**
```
Rbase = (Vgpio - Vbe) / (Imotor / hFE)
```

**Example:**
- Motor current: 500mA
- Transistor hFE: 100
- Required base current: 5mA
- Vgpio: 3.3V, Vbe: 0.7V
- Rbase = (3.3 - 0.7) / 0.005 = 520Ω (use 1kΩ for safety)

**Safety:**
- Never connect motor directly to GPIO
- Use transistor rated for motor current (including startup current)
- Always use flyback diode
- Separate power supply if motor current exceeds supply capability
- Common ground is required
- Keep fingers away from moving parts

**Why this matters:** Motors are used in the thesis project. Understanding safe motor control is essential for safety and reliability.

---

## Exact Resources

### Resource 1: DS18B20 Datasheet
- **Provider:** Maxim Integrated (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Complete DS18B20 specifications
- **URL:** https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf

### Resource 2: ADXL345 Datasheet
- **Provider:** Analog Devices (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Complete ADXL345 specifications
- **URL:** https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf

### Resource 3: ACS712 Datasheet
- **Provider:** Allegro MicroSystems (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Complete ACS712 specifications
- **URL:** https://www.allegromicro.com/en/products/acs712

### Resource 4: Arduino-ESP32 Sensor Libraries
- **Provider:** Various library authors
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Pre-written code for common sensors
- **URL:** https://www.arduino.cc/reference/en/libraries

### Resource 5: Adafruit Sensor Guides
- **Provider:** Adafruit
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Wiring and code examples for sensors
- **URL:** https://learn.adafruit.com/

---

## Study Order

Follow this exact sequence:

1. **Study sensors vs actuators**
2. **Understand analog vs digital sensors**
3. **Study voltage/current/resistance based measurements**
4. **Learn how to read sensor datasheets**
5. **Study sensor specifications (range, resolution, accuracy, precision)**
6. **Understand calibration**
7. **Study noise and filtering**
8. **Learn thresholds and hysteresis**
9. **Study pull-up requirements**
10. **Understand power requirements**
11. **Study sensor communication interfaces**
12. **Study potentiometer**
13. **Study push button**
14. **Study DS18B20**
15. **Study ADXL345**
16. **Study ACS712**
17. **Study LED actuator**
18. **Study buzzer actuator**
19. **Study relay actuator**
20. **Study DC motor actuator and safety**
21. **Complete all exercises**
22. **Complete all labs**
23. **Complete the project**
24. **Take the knowledge test**
25. **Take the practical test**
26. **Review completion checklist**

---

## Exercises

### Exercise 1: Sensor Datasheet Reading

**Objective:** Practice reading and interpreting sensor datasheets.

**Tasks:**
1. Find the DS18B20 datasheet (link in resources)
2. What is the temperature measurement range?
3. What is the typical accuracy?
4. What is the resolution at 12-bit?
5. What is the supply voltage range?
6. What is the standby current?

**Expected Outcome:** You can extract key information from sensor datasheets.

### Exercise 2: Sensor Calibration

**Objective:** Practice sensor calibration calculations.

**Tasks:**
1. A temperature sensor reads 26°C when the actual temperature is 25°C. What is the offset error?
2. A sensor reads 98 when the actual value is 100. What is the gain error (as a percentage)?
3. If the offset error is +2°C, what correction should you apply?
4. If the gain error is -5%, what correction should you apply?
5. Why is calibration important?

**Expected Outcome:** You can calculate calibration corrections.

### Exercise 3: Filtering Implementation

**Objective:** Implement simple moving average filter.

**Tasks:**
1. Write C code for a 5-element moving average filter
2. What happens to the filter response if you increase the window size?
3. What happens if you decrease the window size?
4. What is the trade-off between noise reduction and response time?
5. When would you use a filter?

**Expected Outcome:** You can implement and understand filtering.

### Exercise 4: Threshold and Hysteresis

**Objective:** Design threshold logic with hysteresis.

**Tasks:**
1. Design a temperature threshold system:
   - Turn on heater at 25°C
   - Turn off heater at 27°C
   - What is the hysteresis width?
2. What would happen if hysteresis was 0°C?
3. Why is hysteresis important?
4. What hysteresis width would you use for a system that needs ±0.5°C accuracy?

**Expected Outcome:** You can design threshold logic with hysteresis.

### Exercise 5: Motor Safety Calculations

**Objective:** Calculate safe motor driving parameters.

**Tasks:**
1. A motor draws 300mA running current. What is the approximate startup current?
2. If the motor hFE is 100, what base current is needed?
3. If Vgpio is 3.3V and Vbe is 0.7V, what base resistor value should you use?
4. If the motor requires 6V, can you power it from ESP32 3.3V? Why or why not?
5. Why is a flyback diode required?

**Expected Outcome:** You can calculate safe motor driving parameters.

---

## Labs

### Lab 1: Potentiometer ADC

**Objective:** Read potentiometer using ESP32 ADC, reinforce Phase 6 ADC concepts.

**Prerequisites:**
- Completed Phase 6 (ESP32)
- Understanding of voltage division from Phase 4

**Components:**
- ESP32 development board
- Potentiometer (10kΩ)
- Breadboard
- Jumper wires

**Theory:**
- Reinforces voltage division from Phase 4
- Reinforces ADC from Phase 6
- Potentiometer as variable voltage divider

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
const int potPin = 34;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
}

void loop() {
  int adcValue = analogRead(potPin);
  float voltage = adcValue * 3.3 / 4095.0;
  float percentage = adcValue * 100.0 / 4095.0;
  
  Serial.print("ADC: ");
  Serial.print(adcValue);
  Serial.print(" Voltage: ");
  Serial.print(voltage, 3);
  Serial.print("V Percentage: ");
  Serial.print(percentage, 1);
  Serial.println("%");
  
  delay(100);
}
```

**Expected Behavior:**
- ADC value varies as potentiometer is turned
- Voltage reading varies from 0V to 3.3V
- Serial output shows values

**Troubleshooting:**
- ADC always 0: Check wiring, check pin is ADC-capable
- ADC always 4095: Check wiring, check voltage range
- Non-linear readings: Normal for potentiometer (verify with multimeter)

**Completion Criteria:**
- Potentiometer reading works reliably
- Understand voltage division
- Can calculate percentage from ADC value

---

### Lab 2: DS18B20 Temperature Sensor

**Objective:** Read temperature from DS18B20 using 1-Wire interface.

**Prerequisites:**
- Completed Phase 6 (ESP32)
- Understanding of 1-Wire communication

**Components:**
- ESP32 development board
- DS18B20 temperature sensor
- Resistor (4.7kΩ pull-up)
- Breadboard
- Jumper wires

**Theory:**
- DS18B20 uses 1-Wire digital interface
- Requires pull-up resistor
- 12-bit resolution = 0.0625°C steps
- Range: -55°C to +125°C

**Wiring:**
```
ESP32 GPIO (e.g., GPIO4)
    │
   Resistor (4.7kΩ pull-up)
    │
DS18B20 Data
    │
DS18B20 VCC (3.3V or 5V)
    │
DS18B20 GND
ESP32 GND (common)
```

**Arduino-ESP32 Code:**
```cpp
#include <OneWire.h>
#include <DallasTemperature.h>

OneWire oneWire(4);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(115200);
  sensors.begin();
  sensors.setResolution(12);  // 12-bit resolution
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  
  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.println("°C");
  
  delay(1000);
}
```

**Expected Behavior:**
- Temperature reading updates every second
- Accurate to ±0.5°C (typical)

**Troubleshooting:**
- No sensor found: Check wiring, check pull-up resistor, check GPIO pin
- Reading -127°C: Sensor not connected or wiring error
- Reading 85°C: Communication error

**Common Mistakes:**
- Missing pull-up resistor
- Wrong GPIO pin
- Not calling sensors.requestTemperatures()
- Using VCC outside sensor range

**Safety:**
- Use 3.3V or 5V as appropriate
- Ensure correct wiring polarity

**Completion Criteria:**
- DS18B20 reads temperature accurately
- Understand 1-Wire communication
- Can troubleshoot DS18B20 connections

---

### Lab 3: ADXL345 Accelerometer

**Objective:** Read acceleration data from ADXL345 using I2C.

**Prerequisites:**
- Completed Phase 6 (ESP32)
- Completed Lab 6 (I2C scan)
- Understanding of I2C from Phase 6

**Components:**
- ESP32 development board
- ADXL345 accelerometer
- Breadboard
- Jumper wires

**Theory:**
- ADXL345 measures acceleration on X, Y, Z axes
- I2C interface (SPI also available)
- Configurable range (±2g, ±4g, ±8g, ±16g)
- Used for motion detection, tilt sensing

**Wiring (I2C):**
```
ESP32 GPIO21 (SDA) ─── ADXL345 SDA
ESP32 GPIO22 (SCL) ─── ADXL345 SCL
ESP32 3.3V ────────── ADXL345 VCC
ESP32 GND ────────── ADXL345 GND
CS ────────────────── ADXL345 CS (to 3.3V for I2C)
```

**Arduino-ESP32 Code:**
```cpp
#include <Wire.h>
#include <Adafruit_ADXL345.h>

Adafruit_ADXL345 accel = Adafruit_ADXL345(12345);

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  accel.begin();
  accel.setRange(ADXL345_RANGE_2_G);
}

void loop() {
  accel.read();
  Serial.print("X: "); Serial.print(accel.x);
  Serial.print(" Y: "); Serial.print(accel.y);
  Serial.print(" Z: "); Serial.println(accel.z);
  delay(100);
}
```

**Expected Behavior:**
- X, Y, Z acceleration values update continuously
- Z-axis shows ~1g when sensor is flat (gravity)
- X and Y axes show ~0g when sensor is flat

**Troubleshooting:**
- No data: Check I2C address, check wiring, check library
- Wrong values: Check range setting, check sensor orientation
- Sensor not found: Scan I2C bus to verify address

**Common Mistakes:**
- Wrong I2C address (ADXL345 default: 0x53)
- CS not connected to VCC for I2C mode
- Wrong range setting
- Not calling accel.read()

**Safety:**
- Use 3.3V supply (ADXL345 max is 3.6V)
- Ensure correct wiring

**Completion Criteria:**
- ADXL345 reads acceleration correctly
- Understand I2C sensor communication
- Can interpret acceleration data

---

### Lab 4: ACS712 Current Measurement

**Objective:** Measure current using ACS712 current sensor.

**Prerequisites:**
- Completed Phase 6 (ESP32)
- Understanding of ADC from Phase 6
- Understanding of current sensing

**Components:**
- ESP32 development board
- ACS712 current sensor (5A, 20A, or 30A model)
- Load (e.g., LED with resistor, or motor)
- Breadboard
- Jumper wires

**Theory:**
- ACS712 outputs voltage proportional to current
- Sensitivity: 185mV/A (5A), 100mV/A (20A), 66mV/A (30A)
- Output centered at VCC/2 (2.5V at 0A for 5V supply)
- Requires 5V supply
- Calibration may be needed for zero-current offset

**Circuit:**
```
ACS712
    │
Current (through integrated conductor)
    │
VCC (5V)
    │
GND
    │
VOUT ─── Voltage divider (if needed) ─── ESP32 ADC
```

**CRITICAL - Voltage Conditioning:**
- ACS712 requires 5V supply
- ESP32 ADC is 3.3V max
- ACS712 output is centered at VCC/2 = 2.5V at 0A
- With positive current, VOUT = 2.5V + (current × sensitivity)
- **For 5A model at full scale:** 2.5V + (5A × 0.185V/A) = 3.425V (exceeds 3.3V)
- **For 20A model at full scale:** 2.5V + (20A × 0.1V/A) = 4.5V (exceeds 3.3V)
- **For 30A model at full scale:** 2.5V + (30A × 0.066V/A) = 4.48V (exceeds 3.3V)

**Voltage Divider Required:**
- A voltage divider is required to scale ACS712 output to ESP32 ADC range
- Example divider: 10kΩ from VOUT to ADC, 22kΩ from ADC to GND
- This scales ~4.5V max to ~3.3V max
- Software must account for divider ratio in current calculation

**Alternative:**
- Use ACS712 module with built-in voltage divider (check module specs)
- Use ESP32 with external ADC that supports 5V input
- Limit measured current range to stay within 3.3V (e.g., for 5A model, limit to ~4.3A max)

**This lab:** Assumes you have implemented appropriate voltage conditioning (voltage divider or level shifter) between ACS712 VOUT and ESP32 ADC.

**ESP32 Implementation (if VOUT within 3.3V):**
```cpp
const int currentPin = 34;
const float sensitivity = 0.185;  // 185mV/A for 5A model

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
}

void loop() {
  int adcValue = analogRead(currentPin);
  float voltage = adcValue * 5.0 / 4095.0;  // Assuming 5V reference
  float offset = 2.5;  // VCC/2
  float current = (voltage - offset) / sensitivity;
  
  Serial.print("Current: ");
  Serial.print(current, 3);
  Serial.println("A");
  
  delay(100);
}
```

**Expected Behavior:**
- Current reading updates continuously
- Zero current reads approximately 0A (may have small offset)
- Positive current reads positive values

**Troubleshooting:**
- Readings always positive: Check current direction, check offset
- Readings wrong magnitude: Check sensitivity value for your model
- No reading: Check wiring, check ADC pin
- Readings saturated: VOUT exceeds ADC range (need voltage divider)

**Safety:**
- ACS712 requires 5V supply
- Check if VOUT exceeds ESP32 ADC range
- Use appropriate current model for your application
- Ensure correct current direction through ACS712

**Completion Criteria:**
- ACS712 measures current accurately
- Understand current sensing principles
- Understand ACS712 limitations

---

### Lab 5: Sensor Filtering

**Objective:** Implement filtering for sensor data (using potentiometer or DS18B20).

**Prerequisites:**
- Completed Lab 1 or Lab 2
- Understanding of filtering

**Components:**
- Same as Lab 1 or Lab 2

**Theory:**
- Sensor data contains noise
- Moving average filter reduces noise
- Trade-off: larger window = more filtering but slower response

**Arduino-ESP32 Code (Moving Average Filter):**
```cpp
const int sensorPin = 34;
#define FILTER_SIZE 5
int buffer[FILTER_SIZE];
int index = 0;
int sum = 0;

int filter(int new_value) {
  sum = sum - buffer[index] + new_value;
  buffer[index] = new_value;
  index = (index + 1) % FILTER_SIZE;
  return sum / FILTER_SIZE;
}

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
  
  // Initialize buffer
  for (int i = 0; i < FILTER_SIZE; i++) {
    buffer[i] = analogRead(sensorPin);
    sum += buffer[i];
  }
}

void loop() {
  int rawValue = analogRead(sensorPin);
  int filteredValue = filter(rawValue);
  
  Serial.print("Raw: ");
  Serial.print(rawValue);
  Serial.print(" Filtered: ");
  Serial.println(filteredValue);
  
  delay(100);
}
```

**Expected Behavior:**
- Filtered value is smoother than raw value
- Response is slower than raw value
- Noise is reduced

**Troubleshooting:**
- Filter output lags behind input: Normal, increase filter size for more filtering
- Filter not working: Check filter implementation, check buffer initialization

**Completion Criteria:**
- Filter reduces noise in sensor data
- Understand trade-off between filtering and response time
- Can implement moving average filter

---

### Lab 6: Threshold and Hysteresis

**Objective:** Implement threshold logic with hysteresis (using temperature or potentiometer).

**Prerequisites:**
- Completed Lab 2 (DS18B20) or Lab 1 (potentiometer)
- Understanding of thresholds and hysteresis

**Components:**
- Same as Lab 2 or Lab 1
- LED and resistor for alert

**Theory:**
- Threshold triggers action when crossed
- Hysteresis prevents rapid switching
- Different thresholds for rising and falling

**Arduino-ESP32 Code (Temperature with Hysteresis):**
```cpp
#include <OneWire.h>
#include <DallasTemperature.h>

OneWire oneWire(4);
DallasTemperature sensors(&oneWire);

const int ledPin = 2;
float thresholdHigh = 27.0;  // Turn off at 27°C
float thresholdLow = 25.0;   // Turn on at 25°C
bool heaterState = false;

void setup() {
  pinMode(ledPin, OUTPUT);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  
  if (!heaterState && tempC < thresholdLow) {
    heaterState = true;
    digitalWrite(ledPin, HIGH);
  } else if (heaterState && tempC > thresholdHigh) {
    heaterState = false;
    digitalWrite(ledPin, LOW);
  }
  
  delay(1000);
}
```

**Expected Behavior:**
- LED turns on when temperature drops below 25°C
- LED turns off when temperature rises above 27°C
- No rapid switching at 26°C

**Troubleshooting:**
- LED flickers: Increase hysteresis width
- LED doesn't turn on: Check threshold values, check sensor reading
- LED doesn't turn off: Check threshold values, check sensor reading

**Completion Criteria:**
- Threshold logic works reliably
- Hysteresis prevents rapid switching
- Understand why hysteresis is important

---

### Lab 7: Buzzer Alert

**Objective:** Control buzzer for audible alerts.

**Prerequisites:**
- Completed Phase 6 (ESP32)
- Understanding of PWM from Phase 6

**Components:**
- ESP32 development board
- Buzzer (active or passive)
- Resistor (if needed)
- Transistor (if buzzer current exceeds GPIO limit)
- Breadboard
- Jumper wires

**Theory:**
- Active buzzer: DC voltage generates sound
- Passive buzzer: PWM signal generates sound
- Frequency determines pitch
- Duty cycle affects volume (for passive buzzer)

**Wiring (Active Buzzer - Low Current):**
```
ESP32 GPIO
    │
   Resistor (if needed)
    │
Buzzer +
    │
Buzzer -
    │
ESP32 GND
```

**Wiring (Passive Buzzer with PWM):**
```
ESP32 PWM GPIO
    │
Buzzer +
    │
Buzzer -
    │
ESP32 GND
```

**Arduino-ESP32 Code (Active Buzzer):**
```cpp
const int buzzerPin = 2;

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  digitalWrite(buzzerPin, HIGH);
  delay(100);
  digitalWrite(buzzerPin, LOW);
  delay(1000);
}
```

**Arduino-ESP32 Code (Passive Buzzer with PWM):**
```cpp
const int buzzerPin = 2;
const int pwmChannel = 0;

void setup() {
  ledcSetup(pwmChannel, 2000, 8);  // 2kHz tone
  ledcAttachPin(buzzerPin, pwmChannel);
}

void loop() {
  ledcWrite(pwmChannel, 128);  // 50% duty cycle
  delay(500);
  ledcWrite(pwmChannel, 0);
  delay(500);
}
```

**Expected Behavior:**
- Active buzzer: Beeps periodically
- Passive buzzer: Generates tone at specified frequency

**Troubleshooting:**
- No sound: Check wiring, check buzzer type (active vs passive)
- Low volume: Increase duty cycle (passive), check power
- Wrong frequency: Change PWM frequency

**Safety:**
- Check buzzer voltage and current requirements
- Use transistor if current exceeds GPIO limit
- Check buzzer type (active vs passive)

**Completion Criteria:**
- Buzzer produces sound reliably
- Understand difference between active and passive buzzers
- Can control buzzer with GPIO or PWM

---

### Lab 8: Motor Control

**Objective:** Control DC motor safely with transistor and flyback diode.

**Prerequisites:**
- Completed Phase 4 (transistor switching)
- Completed Phase 6 (ESP32)
- Understanding of motor safety

**Components:**
- ESP32 development board
- Small DC motor (low current, <500mA)
- NPN transistor (rated for motor current)
- Diode (1N4007 or 1N4148)
- Resistor (1kΩ for base)
- Breadboard
- Jumper wires
- Motor power supply (3-6V, separate from ESP32)

**Theory:**
- Motor is inductive load
- Flyback diode protects transistor from voltage spike
- Startup current is 2-3x running current
- Transistor must be rated for motor current
- Separate power supply required for motor
- Common ground required

**Safety Rules:**
1. **NEVER drive motor directly from ESP32 GPIO**
2. Use transistor rated for motor current (including startup)
3. Use flyback diode (cathode to motor+, anode to transistor collector)
4. Separate motor power supply if current exceeds ESP32 supply capability
5. Common ground between ESP32 and motor supply

**Wiring:**
```
ESP32 GPIO (e.g., GPIO2)
    │
   Resistor (1kΩ)
    │
   Transistor base
    │
Transistor emitter ─── GND (common with motor supply GND)
    │
Transistor collector
    │
   Motor ─── Motor power supply positive (+)
    │
   Diode (cathode to motor power supply +, anode to transistor collector)
    │
   (Diode in parallel with motor)
```

**Arduino-ESP32 Code (PWM Speed Control):**
```cpp
const int motorPin = 2;
const int pwmChannel = 0;

void setup() {
  ledcSetup(pwmChannel, 1000, 8);  // 1kHz PWM
  ledcAttachPin(motorPin, pwmChannel);
}

void loop() {
  // 50% speed
  ledcWrite(pwmChannel, 128);
  delay(2000);
  
  // Stop
  ledcWrite(pwmChannel, 0);
  delay(1000);
}
```

**Expected Behavior:**
- Motor runs at varying speed based on PWM duty cycle
- Motor stops when duty cycle is 0
- No voltage spikes damage transistor (flyback diode protects)

**Measurements:**
- Measure motor current at different PWM values
- Verify transistor is not overheating
- Verify flyback diode orientation

**Troubleshooting:**
- Motor doesn't run: Check wiring, check transistor, check power supply
- Motor runs poorly: Check power supply current, check PWM frequency
- Transistor hot: Check current, check transistor rating, check flyback diode
- Motor always runs: Check GPIO state, check transistor

**Common Mistakes:**
- Motor connected directly to GPIO (DANGEROUS)
- Missing flyback diode (damages transistor)
- Wrong diode orientation (doesn't protect)
- Transistor not rated for motor current
- No common ground
- Base resistor wrong value

**Safety:**
- **CRITICAL:** Never connect motor directly to ESP32 GPIO
- Use transistor rated for motor current (including startup current)
- Always use flyback diode
- Separate power supply if needed
- Common ground required
- Keep fingers away from moving parts

**Completion Criteria:**
- Motor runs reliably with PWM speed control
- Flyback diode protects transistor
- Understand motor safety requirements
- Can calculate appropriate transistor and base resistor

---

### Lab 9: Sensor + Actuator Combined System

**Objective:** Combine sensor reading, threshold logic, and actuator control.

**Prerequisites:**
- Completed Lab 2 (DS18B20)
- Completed Lab 6 (threshold and hysteresis)
- Completed Lab 7 (buzzer or LED)

**Components:**
- ESP32 development board
- DS18B20 temperature sensor
- LED and resistor (or buzzer)
- Resistor (4.7kΩ for DS18B20)
- Breadboard
- Jumper wires

**Theory:**
- Read sensor data
- Apply threshold logic with hysteresis
- Control actuator based on threshold
- Complete sensor-actuator loop

**Circuit:**
- DS18B20 wiring (from Lab 2)
- LED wiring (from Phase 6 or Phase 4)

**Arduino-ESP32 Code:**
```cpp
#include <OneWire.h>
#include <DallasTemperature.h>

OneWire oneWire(4);
DallasTemperature sensors(&oneWire);

const int alertPin = 2;
float thresholdHigh = 30.0;
float thresholdLow = 28.0;
bool alertState = false;

void setup() {
  pinMode(alertPin, OUTPUT);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  
  if (!alertState && tempC > thresholdHigh) {
    alertState = true;
    digitalWrite(alertPin, HIGH);
  } else if (alertState && tempC < thresholdLow) {
    alertState = false;
    digitalWrite(alertPin, LOW);
  }
  
  delay(1000);
}
```

**Expected Behavior:**
- Temperature monitored continuously
- Alert LED turns on when temperature exceeds 30°C
- Alert LED turns off when temperature drops below 28°C
- No rapid LED switching

**Troubleshooting:**
- LED flickers: Increase hysteresis width
- LED never turns on: Check threshold values, check sensor reading
- LED never turns off: Check threshold values, check sensor reading

**Completion Criteria:**
- Complete sensor-actuator loop works
- Threshold logic with hysteresis works reliably
- Understand complete sensor-actuator system
- Prepared for thesis project architecture

---

## Projects

### Project: Sensor Monitoring and Threshold-Alert Station

**Objective:** Create a sensor monitoring station that reads multiple sensors, implements filtering and thresholds, and provides alerts.

**Requirements:**
- Read temperature from DS18B20
- Read acceleration from ADXL345 (optional)
- Read potentiometer (analog input)
- Implement moving average filter for at least one sensor
- Implement threshold logic with hysteresis for at least one sensor
- Provide alert via LED or buzzer
- Display sensor data via serial output
- Optionally: Display data on OLED (if available)

**Suggested Architecture:**
```
Sensors (DS18B20, ADXL345, Potentiometer)
    ↓
ESP32 Processing
    ↓
    ├─→ Filtering
    ├─→ Threshold Logic with Hysteresis
    └─→ Alert (LED/Buzzer)
    ↓
Serial Output (for monitoring)
```

**Deliverables:**
- Working firmware (Arduino-ESP32)
- Circuit documentation
- Code with comments
- Serial output showing sensor data and alerts
- Alert system working reliably
- Filter implemented and verified

**Time Estimate:** 4-6 hours

**Project Structure:**
```
sensor-monitoring-station/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   └── main.ino
├── docs/
│   └── architecture.md
└── results/
    └── measurements.md
```

**Note:** This project prepares for the thesis architecture (sensor → MCU → actuator → IoT).

---

## Common Mistakes

### Mistake 1: Not Reading Datasheets
**Problem:** Assuming sensor works without reading specifications
**Consequence:** Incorrect wiring, wrong interface, inaccurate readings
**Solution:** Always read sensor datasheet before implementation

### Mistake 2: Ignoring Power Requirements
**Problem:** Sensor doesn't work due to inadequate power
**Consequence:** Malfunction, incorrect readings
**Solution:** Check supply voltage and current requirements

### Mistake 3: Forgetting Pull-up Resistors
**Problem:** I2C or 1-Wire devices don't work
**Consequence:** Communication failure
**Solution:** Always check if pull-up is required (I2C, 1-Wire, buttons)

### Mistake 4: Not Calibrating Sensors
**Problem:** Sensor readings have offset or gain errors
**Consequence:** Inaccurate measurements
**Solution:** Calibrate sensors against known references

### Mistake 5: No Filtering
**Problem:** Sensor data is noisy and unreliable
**Consequence:** False triggers, inaccurate control
**Solution:** Implement appropriate filtering (moving average, etc.)

### Mistake 6: No Hysteresis
**Problem:** Rapid switching near threshold
**Consequence:** System instability, component wear
**Solution:** Always implement hysteresis for threshold logic

### Mistake 7: Driving Motor Directly from GPIO
**Problem:** Motor connected directly to ESP32 GPIO
**Consequence:** ESP32 damage, GPIO pin failure
**Solution:** ALWAYS use transistor or motor driver

### Mistake 8: Missing Flyback Diode
**Problem:** Inductive load without protection
**Consequence:** Transistor damage from voltage spikes
**Solution:** ALWAYS use flyback diode with inductive loads

### Mistake 9: Wrong Transistor Rating
**Problem:** Transistor cannot handle motor current
**Consequence:** Transistor overheating, failure
**Solution:** Check transistor current rating (including startup current)

### Mistake 10: No Common Ground
**Problem:** ESP32 and motor supply not sharing ground
**Consequence:** Incorrect behavior, communication failure
**Solution:** Always ensure common ground between supplies

---

## Troubleshooting

### Sensor Not Detected
**Problem:** I2C/1-Wire sensor not found
**Solutions:**
- Check wiring (SDA/SCL/DATA, power, ground)
- Check pull-up resistor
- Scan I2C bus to find device address
- Check sensor power supply
- Check GPIO pin capability

### Inaccurate Readings
**Problem:** Sensor readings don't match actual values
**Solutions:**
- Calibrate sensor
- Check sensor specifications (range, accuracy)
- Check ADC reference voltage
- Check for noise (implement filtering)
- Check supply voltage stability

### Actuator Not Working
**Problem:** LED, buzzer, or motor doesn't work
**Solutions:**
- Check wiring and polarity
- Check GPIO pin configuration
- Check current requirements
- Check power supply
- For motors: check transistor, check flyback diode

### Rapid Switching
**Problem:** LED or relay switches rapidly
**Solutions:**
- Increase hysteresis width
- Check threshold values
- Add delay in logic
- Check for noise

### Motor Issues
**Problem:** Motor doesn't run or runs poorly
**Solutions:**
- Check power supply current capability
- Check transistor rating
- Check flyback diode orientation
- Check common ground
- Check for short circuit

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is the difference between a sensor and an actuator?
2. What is the difference between an analog and a digital sensor?
3. What is sensor calibration?
4. What is sensor resolution?
5. What is sensor accuracy?
6. What is the difference between accuracy and precision?
7. Why is filtering important for sensor data?
8. What is hysteresis and why is it important?
9. When are pull-up resistors required?
10. What is the DS18B20 temperature range?
11. What is the DS18B20 resolution at 12-bit?
12. What interface does DS18B20 use?
13. What is the ADXL345 acceleration range?
14. What interface does ADXL345 use?
15. What is the ACS712 sensitivity (5A model)?
16. Why should you never drive a motor directly from ESP32 GPIO?
17. What is a flyback diode used for?
18. What is motor startup current compared to running current?
19. How do you calculate the base resistor for a transistor?
20. What is the purpose of a moving average filter?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **Sensor Datasheet:**
   - Read the DS18B20 datasheet
   - Extract: temperature range, accuracy, resolution, supply voltage, operating current
   - Explain why each specification is important

2. **Sensor Calibration:**
   - Implement calibration for a sensor (potentiometer or DS18B20)
   - Measure known reference values
   - Calculate and apply correction factor
   - Verify improved accuracy

3. **Filtering Implementation:**
   - Implement a moving average filter for sensor data
   - Demonstrate noise reduction
   - Explain the trade-off between filter size and response time

4. **Threshold with Hysteresis:**
   - Implement threshold logic with hysteresis for temperature or potentiometer
   - Demonstrate that rapid switching is prevented
   - Explain why hysteresis is important

5. **Motor Safety:**
   - Calculate the required base resistor for a motor driving circuit
   - Explain why a flyback diode is required
   - Explain why a separate power supply might be needed
   - List all safety considerations for motor control

**Passing Criteria:** All tasks completed with understanding demonstrated.

---

## Completion Checklist

Before moving to Phase 8, verify you have:

- [ ] Understand sensors vs actuators
- [ ] Understand analog vs digital sensors
- [ ] Can read and interpret sensor datasheets
- [ ] Understand sensor specifications (range, resolution, accuracy, precision)
- [ ] Can calibrate sensors
- [ ] Can implement noise filtering
- [ ] Understand thresholds and hysteresis
- [ ] Understand when pull-up resistors are required
- [ ] Understand sensor power requirements
- [ ] Can communicate with sensors via I2C, SPI, UART, 1-Wire
- [ ] Can read DS18B20 temperature sensor
- [ ] Can read ADXL345 accelerometer
- [ ] Can read ACS712 current sensor
- [ ] Can implement sensor filtering
- [ ] Can implement threshold logic with hysteresis
- [ ] Can drive LEDs and buzzers
- [ ] Can drive relays and motors safely
- [ ] Understand motor safety requirements
- [ ] Always use flyback diodes with inductive loads
- [ ] Never drive motors directly from GPIO
- [ ] Completed all exercises
- [ ] Completed at least 5 labs
- [ ] Completed the sensor monitoring station project
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Prepared for thesis project sensor integration

---

## Do Not Continue Until...

**Do not start Phase 8 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can read and interpret sensor datasheets
5. You understand motor safety requirements
6. You have completed at least 5 labs
7. You have completed the sensor monitoring station project
8. You always use flyback diodes with inductive loads
9. You never drive motors directly from GPIO

**Sensors and actuators are the interface between your embedded system and the physical world. Take the time to master safe sensor integration and actuator control—these skills are essential for the thesis project and all embedded systems work.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 8 — Embedded Communication**

Phase 8 will teach you about advanced communication protocols and networking, building on the sensor and actuator skills you learned here to create complete IoT systems.

---

**Sensors provide data to your system, and actuators allow your system to affect the physical world. Mastering both is essential for any embedded systems project, especially the IoT thesis project you're building toward.**
