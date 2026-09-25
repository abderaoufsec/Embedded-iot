# Master's Thesis Project — Embedded and IoT-Based Electric Motor Condition Monitoring and Predictive Maintenance System

## 1. Proposed Project Title

### **Design and Implementation of an Embedded and IoT-Based System for Electric Motor Condition Monitoring and Predictive Maintenance**

**Field:** Embedded Systems — IoT — Instrumentation — Signal Processing — Predictive Maintenance — Industry 4.0

---

# 2. General Project Description

The objective of this project is to design and implement a **complete prototype for monitoring the condition of an electric motor**.

The system will continuously measure several physical parameters of the motor and analyze their evolution in order to identify abnormal operating conditions before they develop into serious failures.

The system will be built around an **STM32 microcontroller**, connected to several sensors measuring:

* vibration;
* electrical current;
* temperature;
* rotational speed.

The acquired data will initially be processed directly by the embedded system. An **ESP32** will then be used to transmit the information through Wi-Fi.

In a later stage, a **Raspberry Pi 4** can be integrated as an IoT gateway and local server.

The collected data will be stored and visualized through a monitoring platform, allowing the evolution of the motor's condition to be observed over time.

The system will also analyze the measured signals in order to identify abnormal behaviors such as:

* mechanical imbalance;
* abnormal vibration;
* overload;
* overheating;
* abnormal electrical behavior;
* abnormal rotational speed;
* combinations of several abnormal indicators.

The overall objective is to move from maintenance based only on scheduled interventions or failures toward an approach based on the **actual condition of the machine**.

---

# 3. Problem Statement

Electric motors are widely used in industrial systems and can operate continuously for long periods under mechanical, electrical, and thermal stresses.

A motor failure can result in:

* production downtime;
* repair costs;
* loss of productivity;
* damage to other components;
* maintenance delays;
* potential safety problems.

A purely corrective maintenance strategy intervenes only after a failure has occurred.

A conventional preventive maintenance strategy may instead schedule maintenance at fixed intervals, even when the motor is still operating normally.

The main problem addressed by this thesis is therefore:

> **How can a low-cost embedded system continuously monitor multiple parameters of an electric motor, analyze their evolution, and detect early indications of abnormal operating conditions or degradation?**

---

# 4. Main Project Concept

The project will be based on an **experimental electric motor test bench**.

Different controlled operating conditions will be created and measured.

For example:

### Normal operation

```text
Motor
  ↓
Normal vibration
Normal current
Normal temperature
Stable RPM
```

### Mechanical imbalance

```text
Motor
  ↓
Controlled imbalance
  ↓
Change in vibration characteristics
  ↓
Detection
```

### Increased load

```text
Motor
  ↓
Higher load
  ↓
Current ↑
Temperature ↑
Possible RPM ↓
```

The system will record the measurements associated with each condition.

This will allow the creation of an experimental dataset specific to the project.

---

# 5. General System Architecture

The proposed architecture is:

```text
                         ELECTRIC MOTOR
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
         Vibration          Current        Temperature
          Sensor            Sensor           Sensor
              │                │                │
              └────────────────┼────────────────┘
                               │
                               ▼
                       ┌──────────────┐
                       │    STM32     │
                       │              │
                       │ Acquisition  │
                       │ Filtering    │
                       │ Processing   │
                       │ FFT          │
                       └──────┬───────┘
                              │
                            UART
                              │
                              ▼
                       ┌──────────────┐
                       │    ESP32     │
                       │              │
                       │ Wi-Fi        │
                       │ MQTT         │
                       └──────┬───────┘
                              │
                            Wi-Fi
                              │
                              ▼
                    ┌───────────────────┐
                    │   Raspberry Pi 4  │
                    │                   │
                    │ MQTT Broker       │
                    │ InfluxDB          │
                    │ Grafana            │
                    └─────────┬─────────┘
                              │
                              ▼
                       Monitoring Panel
                              │
                              ▼
                           User
```

The Raspberry Pi will **not be required during the initial development**. A PC can temporarily perform its role until the embedded acquisition and communication system is stable.

---

# 6. Embedded System

The **STM32F407VGT6** will be the main embedded controller.

Its responsibilities will include:

### Data acquisition

Reading data from the connected sensors.

### Signal preprocessing

The raw measurements can be:

* filtered;
* normalized;
* converted;
* divided into time windows;
* transformed into the frequency domain.

### Vibration analysis

An important part of the project will focus on vibration analysis.

The STM32 may calculate:

* RMS;
* mean value;
* maximum value;
* standard deviation;
* peak-to-peak value;
* frequency spectrum;
* FFT;
* other signal characteristics.

### Communication

The STM32 will communicate with the ESP32 through UART.

---

# 7. Vibration Measurement

Vibration measurement will be one of the most important parts of the system.

An initial sensor option is:

### ADXL345

The sensor measures acceleration on three axes:

```text
X
Y
Z
```

It supports SPI and I²C communication.

The sensor will be mounted rigidly on the motor structure to measure the vibrations transmitted through the motor housing.

A possible future upgrade is a vibration-specific sensor such as the **IIS3DWB**, depending on availability and budget.

---

# 8. Current Measurement

An **ACS712-5A** module can be used to measure the electrical current consumed by the motor.

The STM32 will acquire the analog signal and calculate parameters such as:

* average current;
* RMS current;
* current variation;
* startup current;
* current evolution under different loads.

These measurements will be compared with vibration and temperature data.

---

# 9. Temperature Measurement

A **DS18B20** temperature sensor will be attached to the motor housing.

It will monitor the thermal evolution of the motor.

For example:

```text
Temperature
     │
     │                 /
     │              __/
     │           __/
     │__________/
     └────────────────── Time
```

An increase in temperature can be studied in relation to:

* increased load;
* increased current;
* mechanical abnormalities;
* operating conditions.

---

# 10. Rotational Speed Measurement

A Hall-effect sensor combined with a small magnet can be used to measure the motor's rotational speed.

The system will count the pulses generated by the sensor and calculate RPM.

For example:

$$
RPM = \frac{N \times 60}{T}
$$

where:

* \(N\) is the number of detected pulses;
* \(T\) is the measurement period.

Rotational speed is also important for vibration analysis.

For example:

$$
3000\ RPM = 50\ Hz
$$

Therefore, the rotational frequency becomes a reference when analyzing the vibration spectrum.

---

# 11. Vibration Signal Analysis

The accelerometer produces a time-domain signal:

```text
Acceleration
     │
     │    /\      /\
     │   /  \    /  \
     │__/    \__/    \____
     └──────────────────── Time
```

The system can then apply a **Fast Fourier Transform (FFT)** to obtain a frequency-domain representation.

```text
Time-domain signal
        │
        ▼
Preprocessing
        │
        ▼
       FFT
        │
        ▼
Frequency spectrum
        │
        ▼
Feature extraction
```

This makes it possible to study rotational frequencies and changes in the vibration spectrum when abnormal conditions are introduced.

---

# 12. Experimental Conditions

The project will not be limited to measuring a normally operating motor.

Several controlled experimental conditions will be studied.

## Condition 1 — Normal Operation

The motor operates under normal conditions.

The measurements provide the baseline reference.

---

## Condition 2 — Mechanical Imbalance

A controlled mechanical imbalance will be introduced into the rotating assembly.

The objective is to study:

* vibration increase;
* changes in the frequency spectrum;
* influence of rotational speed.

---

## Condition 3 — Speed Variation

Several operating speeds will be tested.

For example:

```text
1000 RPM
1500 RPM
2000 RPM
2500 RPM
3000 RPM
```

This is important because the system must distinguish between a naturally high vibration level caused by increased speed and an actual abnormal condition.

---

## Condition 4 — Load Variation

The motor will be tested under different load conditions where possible.

The following parameters will be observed:

* current;
* temperature;
* RPM;
* vibration.

---

## Condition 5 — Thermal Behavior

The temperature evolution will be studied under different operating conditions.

---

# 13. Experimental Dataset

Each experiment will generate a set of measurements.

For example:

```text
timestamp
rpm
temperature
current
accel_x
accel_y
accel_z
rms
frequency_peak
condition
```

Each measurement will be associated with a known operating condition:

```text
NORMAL
IMBALANCE
HIGH_LOAD
OVERHEATING
...
```

This will create a structured experimental dataset for the thesis.

---

# 14. Data Processing

The system will use two main processing levels.

### Embedded level — STM32

Real-time processing such as:

* filtering;
* RMS calculation;
* statistical calculations;
* FFT;
* feature extraction.

### Gateway/server level — PC or Raspberry Pi

More computationally intensive operations such as:

* long-term storage;
* historical analysis;
* statistical analysis;
* visualization;
* trend analysis;
* advanced condition detection.

This separation allows the embedded system to operate within its computational and memory constraints while still providing more advanced analysis at the gateway level.

---

# 15. IoT Communication

The ESP32 will provide network connectivity.

The proposed communication protocol is:

### MQTT

Architecture:

```text
STM32
  │
 UART
  ↓
ESP32
  │
 Wi-Fi
  ↓
MQTT Broker
  │
  ├── InfluxDB
  │
  └── Other services
```

Example message:

```json
{
  "rpm": 2950,
  "temperature": 42.3,
  "current": 1.72,
  "vibration_rms": 0.38,
  "condition": "normal"
}
```

---

# 16. Data Storage

The Raspberry Pi can host:

### InfluxDB

for storing time-series measurements.

For example:

```text
Time → RPM
Time → Temperature
Time → Current
Time → Vibration
```

This allows the evolution of the motor to be analyzed over long periods.

---

# 17. Monitoring Dashboard

**Grafana** can be used to create the monitoring interface.

The dashboard can display:

### Motor condition

```text
NORMAL
```

### RPM

```text
2950 RPM
```

### Temperature

```text
42.3 °C
```

### Current

```text
1.72 A
```

### Vibration

```text
RMS = ...
```

### Frequency spectrum

The vibration spectrum can also be displayed and monitored over time.

---

# 18. Alert System

The system can generate an alert when an abnormal condition is detected.

For example:

```text
WARNING: High temperature
```

or:

```text
WARNING: Unusual vibration increase
```

or:

```text
WARNING: Multiple abnormal parameters detected
```

A Telegram notification system can also be added as an optional feature.

---

# 19. Predictive Maintenance

The final objective is to use the collected data to identify signs that may precede significant degradation.

The objective is not simply:

> "The motor has failed."

Instead, the system should be able to identify changes in the motor's normal behavior.

For example:

```text
Day 1
Vibration RMS = 0.20

Day 10
Vibration RMS = 0.24

Day 20
Vibration RMS = 0.31

Day 30
Vibration RMS = 0.43
```

The system can identify this progressive change and generate a warning before a major failure occurs.

The exact predictive capability will depend on the experimental data obtained during the project.

---

# 20. Signal and Data Analysis Methods

Several methods can be investigated and compared.

### Statistical methods

* thresholds;
* moving averages;
* standard deviation;
* RMS;
* trend analysis.

### Frequency-domain analysis

* FFT;
* dominant frequencies;
* frequency amplitudes;
* evolution of spectral peaks.

### Classification and anomaly-detection methods

Depending on the collected data, different approaches can be studied to distinguish:

```text
NORMAL
    vs.
ABNORMAL
```

or multiple operating conditions:

```text
NORMAL
IMBALANCE
OVERLOAD
OVERHEATING
...
```

The final method will be selected according to the experimental results rather than being fixed in advance.

---

# 21. Why Use Multiple Parameters?

A system based only on vibration measurements can sometimes produce ambiguous results.

For this reason, the project combines several measurements:

```text
              ┌── Vibration
              │
              ├── Current
MOTOR ────────┼── Temperature
              │
              └── RPM
```

For example:

### Vibration ↑

### Current normal

### Temperature normal

may indicate a different situation from:

### Vibration ↑

### Current ↑

### Temperature ↑

Combining several parameters therefore provides a more complete representation of the motor's operating condition.

---

# 22. Planned Hardware

## Initial prototype

| Component          | Function                 |
| ------------------ | ------------------------ |
| STM32F407VGT6      | Main embedded controller |
| ADXL345            | Vibration measurement    |
| ACS712-5A          | Current measurement      |
| DS18B20            | Temperature measurement  |
| Hall-effect sensor | RPM measurement          |
| ESP32              | Wi-Fi communication      |
| 775 12V DC motor   | Experimental motor       |
| PWM controller     | Motor speed control      |
| 12V power supply   | Motor power              |
| Breadboard         | Prototyping              |
| Dupont wires       | Connections              |

## Later infrastructure

| Component      | Function                     |
| -------------- | ---------------------------- |
| Raspberry Pi 4 | IoT gateway / local server   |
| MQTT broker    | Messaging                    |
| InfluxDB       | Time-series database         |
| Grafana        | Monitoring and visualization |

---

# 23. Estimated Budget

The target budget is:

### **30,000–35,000 DZD maximum**

However, the initial hardware purchase can be significantly below this amount.

A reasonable initial estimate for the electronic and experimental components is approximately:

### **15,000–25,000 DZD**

depending on the supplier, shipping costs, and selected components.

The remaining budget can be reserved for:

* improving the mechanical test bench;
* upgrading the vibration sensor;
* additional sensors;
* cables and connectors;
* enclosure;
* power equipment;
* additional experimental components;
* Raspberry Pi 4 at a later stage.

The Raspberry Pi is therefore **not required to start the project**.

---

# 24. Scientific Contribution

The project is not simply a system that connects sensors to a Raspberry Pi.

Its scientific and engineering contribution comes from several aspects.

### 1. Real-world signal acquisition

Obtaining measurements from a physical motor.

### 2. Signal processing

Transforming raw measurements into useful information.

### 3. Vibration analysis

Studying the relationship between motor rotation, frequency and vibration.

### 4. Multi-parameter monitoring

Combining:

* vibration;
* current;
* temperature;
* rotational speed.

### 5. Early anomaly detection

Identifying changes from the normal operating behavior.

### 6. Embedded implementation

Determining which processing operations can be performed directly on the STM32.

### 7. IoT communication

Transmitting measurements to a local monitoring infrastructure.

---

# 25. Expected Final Demonstration

At the end of the project, the prototype should ideally operate as follows:

```text
                 ┌──────────────────┐
                 │      MOTOR       │
                 └────────┬─────────┘
                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
        Vibration      Current    Temperature
          Sensor        Sensor       Sensor
             │            │            │
             └────────────┼────────────┘
                          │
                       ┌──▼───┐
                       │STM32 │
                       └──┬───┘
                          │
                         UART
                          │
                       ┌──▼───┐
                       │ESP32 │
                       └──┬───┘
                          │
                         Wi-Fi
                          │
                  ┌───────▼────────┐
                  │  Raspberry Pi  │
                  │                │
                  │ MQTT           │
                  │ InfluxDB       │
                  │ Grafana        │
                  └───────┬────────┘
                          │
                          ▼
                     MONITORING
                          │
                          ▼
                 CONDITION ANALYSIS
                          │
                          ▼
                        ALERT
```

The final demonstration should allow the user to operate the motor under different controlled conditions and observe the corresponding changes in:

* vibration;
* current;
* temperature;
* RPM;
* frequency spectrum;
* motor condition.

---

# 26. Project Limitations

The prototype will not represent a complete industrial installation.

The motor used will be relatively small, and the abnormal conditions will be introduced under controlled experimental conditions.

Therefore, the results should be presented as **experimental validation of a prototype**, rather than as a guarantee that the system will operate identically on every industrial motor.

Possible future work could involve:

* industrial three-phase motors;
* industrial-grade sensors;
* industrial communication protocols;
* industrial enclosures;
* professional data acquisition systems;
* deployment in a real industrial environment.

---

# 27. Possible Future Extensions

If time and budget permit, the project could later be extended with:

### Remote monitoring

Accessing motor information remotely.

### Notifications

Telegram or another notification service.

### Long-term monitoring

Storing several weeks or months of measurements.

### Multiple motors

Extending the architecture to monitor several machines.

### Industrial gateway

Adding industrial communication protocols.

### Web interface

Developing a dedicated web interface in addition to Grafana.

### Advanced vibration sensor

Replacing the initial sensor with a sensor specifically designed for industrial vibration monitoring.

---

# 28. Final Project Summary

> **This project aims to design and implement an embedded and IoT-based system for monitoring the condition of an electric motor. An STM32 microcontroller will acquire and preprocess measurements from several sensors monitoring vibration, electrical current, temperature, and rotational speed. The measurements will be transmitted through an ESP32 using Wi-Fi and MQTT to a local monitoring platform, which can later be hosted on a Raspberry Pi 4 using InfluxDB and Grafana.**
>
> **An experimental motor test bench will be developed to reproduce different operating conditions, including normal operation, speed variations, load variations, and controlled mechanical abnormalities. The acquired signals will be analyzed in both the time and frequency domains using techniques such as statistical feature extraction and FFT analysis.**
>
> **The main objective is to develop and evaluate a monitoring approach capable of identifying abnormal changes in the motor's operating condition at an early stage and generating appropriate alerts. The project combines embedded systems, instrumentation, signal processing, IoT communication, data storage, visualization, and predictive maintenance in a low-cost experimental prototype.**

## Proposed official title

### **Design and Implementation of an Embedded and IoT-Based System for Electric Motor Condition Monitoring and Predictive Maintenance**
