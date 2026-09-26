# Phase 4 — Electronics

> **Goal:** Develop practical electronics skills including voltage, current, resistance, Ohm's law, components, and hands-on labs with safe low-voltage hardware.
>
> **Prerequisite:** Phase 3 — Digital Electronics
>
> **Outcome:** You can build safe low-voltage circuits, use a multimeter, calculate component values, understand GPIO electrical characteristics, and drive basic loads.

---

## What You Will Learn

By completing this phase, you will understand:

- Voltage, current, and resistance concepts
- Ohm's law and power calculations
- Series and parallel circuits
- Resistors, capacitors, diodes, and LEDs
- Transistors and MOSFETs
- Voltage regulators
- Breadboards and multimeters
- Power supplies and ground
- Current limiting and GPIO protection
- Driving loads (LEDs, motors, relays)
- Flyback diodes for inductive loads
- Electrical safety for low-voltage circuits
- Practical lab skills with real hardware

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phase 0 — Orientation
- ✅ Completed Phase 1 — Computer Fundamentals
- ✅ Completed Phase 2 — C Programming
- ✅ Completed Phase 3 — Digital Electronics
- ✅ Understanding of logic levels and GPIO concepts
- ✅ Understanding of pull-up/pull-down resistors
- ✅ Basic arithmetic skills

**Hardware required for labs:**
- Breadboard
- Jumper wires
- LEDs (red, green, yellow)
- Resistors (220Ω, 330Ω, 1kΩ, 10kΩ)
- Push buttons
- Potentiometer (10kΩ)
- Transistor (e.g., 2N2222 or BC547)
- Small DC motor (optional)
- Diode (e.g., 1N4007)
- Multimeter
- Power supply (3.3V or 5V safe source)

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain voltage, current, and resistance
- Apply Ohm's law to calculate component values
- Calculate power dissipation in components
- Design series and parallel circuits
- Read resistor color codes
- Calculate current-limiting resistors for LEDs
- Use a breadboard correctly
- Use a multimeter to measure voltage, current, and resistance
- Understand transistor and MOSFET switching
- Drive inductive loads safely with flyback diodes
- Follow electrical safety guidelines
- Build and debug basic electronic circuits
- Troubleshoot common circuit problems

---

## Concepts

### Voltage

**Voltage:** Electrical potential difference between two points
- Measured in volts (V)
- Analogous to water pressure in a pipe
- "Push" that drives current through a circuit
- Measured between two points (not absolute)

**Common voltages in embedded systems:**
- 3.3V: Common logic level for modern microcontrollers
- 5V: Traditional logic level, Arduino standard
- 1.5V: AA battery nominal voltage
- 12V: Common for motors and higher-power devices

**Why this matters:** Understanding voltage is essential for connecting components safely. Mismatched voltage levels can damage components.

### Current

**Current:** Flow of electric charge
- Measured in amperes (A)
- Analogous to water flow rate
- Determined by voltage and resistance (Ohm's law)

**Common current units:**
- mA (milliampere): 0.001 A
- µA (microampere): 0.000001 A

**Typical currents:**
- LED: 10-20 mA
- Small motor: 100-500 mA
- GPIO pin: 20 mA maximum (typical)

**Why this matters:** Exceeding current limits can damage components. Understanding current is essential for choosing components and designing circuits.

### Resistance

**Resistance:** Opposition to current flow
- Measured in ohms (Ω)
- Higher resistance = less current for same voltage
- Used to limit current, divide voltage, pull signals

**Resistor color code:** System for reading resistor values
- First band: First digit
- Second band: Second digit
- Third band: Multiplier
- Fourth band: Tolerance

**Common resistor values:**
- 220Ω, 330Ω, 470Ω, 1kΩ, 4.7kΩ, 10kΩ, 100kΩ

**Why this matters:** Resistors are used extensively for current limiting, pull-up/pull-down, and voltage division. Understanding resistance is fundamental.

### Ohm's Law

**Ohm's Law:** V = I × R

**Forms:**
- V = I × R (voltage = current × resistance)
- I = V / R (current = voltage / resistance)
- R = V / I (resistance = voltage / current)

**Example:** Calculate resistor for LED
- Vsupply = 3.3V
- VLED = 2.0V
- I = 10mA = 0.01A
- R = (3.3 - 2.0) / 0.01 = 130Ω

**Why this matters:** Ohm's law is used constantly in electronics design. You'll use it to calculate resistor values, verify circuit behavior, and troubleshoot.

### Power

**Power:** Rate of energy transfer
- Measured in watts (W)
- P = V × I (power = voltage × current)
- Also: P = I²R, P = V²/R

**Example:** LED power
- V = 2.0V
- I = 0.01A
- P = 2.0 × 0.01 = 0.02W = 20mW

**Why this matters:** Components have power limits. Exceeding power limits can overheat and damage components.

### Series Circuits

**Series Circuit:** Components connected end-to-end
- Same current flows through all components
- Voltages add: Vtotal = V1 + V2 + V3
- Resistances add: Rtotal = R1 + R2 + R3

**Example:**
```
V+ ── R1 ── R2 ── LED ── GND
```

**Why this matters:** Series circuits are used for voltage division and current limiting. Understanding series connections is essential for circuit design.

### Parallel Circuits

**Parallel Circuit:** Components connected across the same voltage
- Same voltage across all branches
- Currents add: Itotal = I1 + I2 + I3
- Resistances: 1/Rtotal = 1/R1 + 1/R2 + 1/R3

**Example:**
```
       ┌── R1 ──┐
V+ ────┤        ├── GND
       └── R2 ──┘
```

**Why this matters:** Parallel circuits are used for connecting multiple loads to the same power source. Understanding parallel connections is essential for power distribution.

### Resistors

**Resistor:** Component that provides resistance
- Used for current limiting, voltage division, pull-up/pull-down
- Value indicated by color code or printed text
- Power rating (1/4W, 1/2W, etc.)
- Tolerance (5%, 1%, etc.)

**Types:**
- Carbon film: Common, inexpensive
- Metal film: More precise
- Wire-wound: High power

**Why this matters:** Resistors are the most common electronic component. You'll use them constantly for current limiting and signal conditioning.

### Capacitors

**Capacitor:** Component that stores electrical charge
- Measured in farads (F)
- Used for filtering, timing, energy storage
- Blocks DC, passes AC

**Common values:**
- 0.1µF (104): Decoupling
- 10µF: Power supply filtering
- 1000µF: Energy storage

**Why this matters:** Capacitors are used for power supply filtering, signal coupling, and timing. Understanding capacitors is essential for stable circuits.

### Diodes

**Diode:** Component that allows current flow in only one direction
- Has polarity (anode +, cathode -)
- Forward voltage drop (typically 0.7V for silicon)
- Used for rectification, protection, LEDs

**LED (Light Emitting Diode):**
- Emits light when forward biased
- Requires current limiting resistor
- Forward voltage: 1.8-3.3V depending on color

**Why this matters:** Diodes are used for protection, rectification, and indicators. Understanding diodes is essential for LED circuits and protection circuits.

### Transistors

**Transistor:** Semiconductor device that amplifies or switches signals
- Three terminals: base, collector, emitter (BJT) or gate, drain, source (MOSFET)
- Used as switches or amplifiers
- Can control higher current/voltage with small control signal

**BJT (Bipolar Junction Transistor):**
- Current-controlled device
- Common types: NPN, PNP
- Example: 2N2222, BC547

**MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor):**
- Voltage-controlled device
- High input impedance
- Common types: N-channel, P-channel
- Example: IRF540

**Why this matters:** Transistors are used to switch higher-current loads (motors, relays) from GPIO pins. Understanding transistors is essential for driving loads.

### Voltage Regulators

**Voltage Regulator:** Component that maintains constant output voltage
- Types: Linear (LM7805), Switching (buck converters)
- Provides stable voltage despite input variations
- Used to power microcontrollers and sensors

**Why this matters:** Voltage regulators provide stable power for microcontrollers and sensors. Understanding them is essential for reliable power supply design.

### Breadboards

**Breadboard:** Tool for prototyping circuits without soldering
- Internal connections allow easy component placement
- Power rails: Connected rows for VCC and GND
- Terminal area: Component placement

**Rules:**
- Understand internal connections before use
- Keep wiring organized
- Turn power off before changing wiring
- Not suitable for high currents or high frequencies

**Why this matters:** Breadboards are essential for prototyping and learning. Understanding how to use them correctly prevents short circuits and damaged components.

### Multimeter

**Multimeter:** Tool for measuring electrical quantities
- DC voltage: Measure voltage between two points
- AC voltage: Measure AC voltage (not needed for embedded)
- Resistance: Measure component resistance
- Continuity: Check if two points are connected
- Current: Measure current flow (be careful!)

**Safety:**
- Never measure resistance on powered circuit
- Be careful with current measurement (can short power supply)
- Start with higher range, then reduce

**Why this matters:** A multimeter is essential for debugging circuits. Understanding how to use it correctly prevents damage and enables effective troubleshooting.

### Power Supplies

**Power Supply:** Source of electrical power
- Types: Bench supply, USB, battery, wall adapter
- Provides voltage and current
- Must match circuit requirements

**Ground (GND):** Reference point for voltage measurements
- All components in a circuit should share common ground
- Voltage is measured relative to ground
- Common ground required for communication between devices

**Why this matters:** Proper power supply and grounding are essential for reliable circuit operation. Understanding power supplies prevents damage and ensures correct operation.

### Current Limiting

**Current Limiting:** Restricting current to safe levels
- Resistors used to limit current
- Protects components from overcurrent
- Essential for LEDs, transistors, GPIO pins

**Example:** LED current limiting
- Without resistor: LED draws too much current, burns out
- With resistor: Current limited to safe value (10-20mA)

**Why this matters:** Current limiting is essential for protecting components. Understanding it prevents damage and ensures reliable operation.

### GPIO Protection

**GPIO Protection:** Protecting microcontroller GPIO pins
- Current limiting resistors
- Voltage level shifting
- Protection diodes
- Not exceeding voltage/current limits

**Typical GPIO limits:**
- Voltage: 0V to VCC (e.g., 0-3.3V)
- Current: 20mA per pin (typical)
- Total current: Limited per port

**Why this matters:** GPIO pins can be easily damaged. Understanding protection prevents damage to the microcontroller.

### Driving Loads

**Driving Loads:** Controlling higher-power devices from GPIO
- GPIO pins cannot directly drive high-current loads
- Use transistors or MOSFETs as switches
- Use relay modules for AC loads
- Use motor drivers for motors

**Example:** Driving LED from GPIO
- GPIO → resistor → LED → GND
- Resistor limits current to safe value

**Example:** Driving motor from GPIO
- GPIO → transistor → motor → power supply
- Transistor switches higher current for motor

**Why this matters:** Most real-world loads (motors, relays, high-power LEDs) cannot be driven directly from GPIO. Understanding load driving is essential for practical projects.

### Relays

**Relay:** Electromechanical switch
- Control high voltage/current with low voltage/current
- Electrically isolated control circuit
- Can switch AC or DC
- Requires flyback diode for inductive kickback

**Why this matters:** Relays are used to switch high-power loads (AC mains, high-current DC) from microcontrollers. Understanding relays is essential for controlling high-power devices safely.

### Motors

**Motor:** Converts electrical energy to mechanical motion
- Types: DC, stepper, servo
- Requires driver circuit
- Inductive load (flyback diode needed)
- Can draw high current

**Why this matters:** Motors are common in embedded projects (robotics, automation). Understanding motor control is essential for motion control projects.

### Flyback Diode

**Flyback Diode:** Protection diode for inductive loads
- Placed across inductive load (motor, relay)
- Protects transistor from voltage spike when load turns off
- Also called freewheeling diode or snubber diode

**Why it's needed:** Inductive loads generate voltage spike when current is interrupted (Lenz's law). Without flyback diode, this spike can damage the switching transistor.

**Why this matters:** Flyback diodes are essential when driving inductive loads (motors, relays). Understanding them prevents damage to components.

### Electrical Safety

**Low-Voltage Safety:**
- Keep circuits below 24V DC for beginner work
- Never work on mains voltage (120V/230V AC)
- Use isolated power supplies
- Double-check polarity before powering
- Turn power off before changing wiring

**Component Safety:**
- Never exceed voltage/current ratings
- Use appropriate power ratings for resistors
- Use heat sinks for high-power components
- Provide adequate ventilation

**Why this matters:** Electrical safety prevents injury and equipment damage. Understanding safety guidelines is essential for working with electronics.

---

## Exact Resources

### Resource 1: Electronics Tutorials
- **Provider:** SparkFun Electronics
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Comprehensive electronics fundamentals
- **URL:** https://learn.sparkfun.com/

### Resource 2: Circuit Basics
- **Provider:** All About Circuits
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** DC circuit theory and components
- **URL:** https://www.allaboutcircuits.com/textbook/direct-current/

### Resource 3: Multimeter Tutorial
- **Provider:** SparkFun Electronics
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Learn to use a multimeter
- **URL:** https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter

### Resource 4: Transistor Basics
- **Provider:** SparkFun Electronics
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Understand transistors for switching
- **URL:** https://learn.sparkfun.com/tutorials/transistors

### Resource 5: Component Guide
- **Provider:** SparkFun Electronics
- **Level:** Beginner
- **Cost:** Free
- **Type:** Secondary reference
- **Purpose:** Identify and understand electronic components
- **URL:** https://www.sparkfun.com/categories/126

---

## Study Order

Follow this exact sequence:

1. **Study voltage, current, and resistance concepts**
2. **Learn Ohm's law and power calculations**
3. **Understand series and parallel circuits**
4. **Study resistors and color codes**
5. **Learn about capacitors**
6. **Study diodes and LEDs**
7. **Learn about transistors and MOSFETs**
8. **Study voltage regulators**
9. **Learn about breadboards**
10. **Study multimeter usage**
11. **Understand power supplies and ground**
12. **Study current limiting**
13. **Learn GPIO protection**
14. **Study driving loads**
15. **Learn about relays**
16. **Study motors**
17. **Understand flyback diodes**
18. **Study electrical safety**
19. **Complete Lab 1: LED**
20. **Complete Lab 2: Button**
21. **Complete Lab 3: Potentiometer**
22. **Complete Lab 4: PWM LED**
23. **Complete Lab 5: Transistor-controlled load**
24. **Complete Lab 6: Basic motor/load control**
25. **Complete the project**
26. **Take the knowledge test**
27. **Take the practical test**
28. **Review completion checklist**

---

## Labs

### Lab 1: LED Circuit

**Objective:** Build a basic LED circuit and understand current limiting.

**Prerequisites:**
- Understanding of voltage, current, resistance
- Understanding of Ohm's law

**Components:**
- LED (any color)
- Resistor (220Ω or 330Ω)
- Breadboard
- Jumper wires
- Power supply (3.3V or 5V)

**Theory:**
- LEDs require current limiting resistors
- Calculate resistor: R = (Vsupply - VLED) / I
- Example: (3.3V - 2.0V) / 0.01A = 130Ω (use 220Ω or 330Ω)
- Note: When connecting LED to GPIO pin later, ensure total current is within GPIO limits (typically 20mA per pin)

**Wiring:**
```
Power supply positive (+)
    │
   Resistor (220Ω or 330Ω)
    │
   LED (anode +)
    │
   LED (cathode -)
    │
Power supply negative (-/GND)
```

**Expected Behavior:**
- LED lights up when power is applied
- LED brightness depends on current (resistor value)

**Measurements:**
- Measure voltage across LED (should be ~2V)
- Measure voltage across resistor
- Calculate current from resistor voltage
- Verify current is within LED rating (10-20mA)

**Troubleshooting:**
- LED not lighting: Check polarity, check connections, measure voltage
- LED too dim: Decrease resistor value (within limits)
- LED too bright: Increase resistor value

**Common Mistakes:**
- Reversing LED polarity
- Forgetting current limiting resistor
- Using wrong resistor value
- Poor breadboard connections

**Safety:**
- Use low voltage (3.3V or 5V)
- Don't exceed LED current rating
- Ensure proper polarity

**Completion Criteria:**
- LED lights up reliably
- Current is within safe limits (10-20mA)
- Can calculate appropriate resistor value
- Can measure voltages correctly

---

### Lab 2: Button Circuit

**Objective:** Build a button circuit with pull-up resistor and understand debouncing.

**Prerequisites:**
- Understanding of pull-up/pull-down resistors
- Understanding of GPIO input mode

**Components:**
- Push button
- Resistor (10kΩ for pull-up)
- Breadboard
- Jumper wires
- Power supply (3.3V or 5V)
- Multimeter

**Theory:**
- Buttons need pull-up or pull-down resistors to prevent floating inputs
- Pull-up: Default HIGH, LOW when pressed
- Pull-down: Default LOW, HIGH when pressed
- Buttons bounce and require debouncing

**Wiring (Pull-up):**
```
Power supply positive (+)
    │
   Resistor (10kΩ)
    │
   └── Button ─── Power supply negative (-/GND)
    │
   GPIO pin (for measurement)
```

**Expected Behavior:**
- GPIO reads HIGH when button is not pressed
- GPIO reads LOW when button is pressed
- Clean transitions (after debouncing)

**Measurements:**
- Measure voltage at GPIO when button not pressed (should be ~VCC)
- Measure voltage at GPIO when button pressed (should be ~0V)
- Observe voltage bounce with multimeter (rapid fluctuations)

**Troubleshooting:**
- Floating readings: Check pull-up resistor connection
- Always LOW: Check button wiring, check for short
- Always HIGH: Check button is functioning

**Common Mistakes:**
- Forgetting pull-up/pull-down resistor
- Incorrect button wiring
- Not accounting for button bounce

**Safety:**
- Use low voltage (3.3V or 5V)
- Ensure proper connections

**Completion Criteria:**
- Button circuit works reliably
- Understand pull-up/pull-down concept
- Can measure button state with multimeter
- Understand debouncing requirement

---

### Lab 3: Potentiometer

**Objective:** Use a potentiometer as a variable voltage divider and understand analog signals.

**Prerequisites:**
- Understanding of voltage division
- Understanding of analog vs digital signals

**Components:**
- Potentiometer (10kΩ linear)
- Breadboard
- Jumper wires
- Power supply (3.3V or 5V)
- Multimeter

**Theory:**
- Potentiometer is a variable voltage divider
- Wiper position determines output voltage
- Output voltage varies continuously (analog)
- ADC converts analog voltage to digital value

**Wiring:**
```
Power supply positive (+)
    │
Potentiometer (left terminal)
    │
Potentiometer (wiper/middle terminal) → Output/ADC
    │
Potentiometer (right terminal)
    │
Power supply negative (-/GND)
```

**Expected Behavior:**
- Output voltage varies from 0V to VCC as potentiometer is turned
- Smooth voltage variation (analog signal)
- Linear relationship between position and voltage (for linear potentiometer)

**Measurements:**
- Measure output voltage at minimum (should be ~0V)
- Measure output voltage at maximum (should be ~VCC)
- Measure output voltage at midpoint (should be ~VCC/2)
- Verify smooth voltage variation

**Troubleshooting:**
- No voltage variation: Check wiper connection, check potentiometer
- Voltage always 0V: Check power supply, check connections
- Voltage always VCC: Check wiper connection, check potentiometer

**Common Mistakes:**
- Incorrect potentiometer wiring
- Not using wiper terminal
- Poor breadboard connections

**Safety:**
- Use low voltage (3.3V or 5V)
- Ensure proper connections

**Completion Criteria:**
- Potentiometer works as variable voltage divider
- Can measure voltage variation
- Understand analog signal concept
- Can calculate expected voltage

---

### Lab 4: PWM LED

**Objective:** Use PWM to control LED brightness and understand duty cycle.

**Prerequisites:**
- Understanding of PWM concept
- Understanding of duty cycle
- Completed Lab 1 (LED circuit)

**Components:**
- LED
- Resistor (220Ω or 330Ω)
- Breadboard
- Jumper wires
- Power supply (3.3V or 5V)
- Multimeter (optional, to measure average voltage)

**Theory:**
- PWM rapidly switches output between HIGH and LOW
- Duty cycle determines average voltage
- Higher duty cycle = brighter LED
- Frequency should be high enough to avoid visible flicker

**Wiring:**
```
PWM output pin
    │
   Resistor (220Ω or 330Ω)
    │
   LED
    │
   GND
```

**Expected Behavior:**
- LED brightness varies with duty cycle
- Smooth brightness variation (no visible flicker)
- 0% duty cycle = LED off
- 100% duty cycle = LED full brightness
- 50% duty cycle = LED half brightness

**Measurements:**
- Observe LED brightness at different duty cycles
- Measure average voltage with multimeter (should vary with duty cycle)
- Verify no visible flicker

**Troubleshooting:**
- LED always on: Check PWM configuration, check pin
- LED always off: Check PWM configuration, check connections
- Visible flicker: Increase PWM frequency

**Common Mistakes:**
- PWM frequency too low (visible flicker)
- Incorrect duty cycle calculation
- Wrong pin configuration

**Safety:**
- Use low voltage (3.3V or 5V)
- Ensure current limiting resistor

**Completion Criteria:**
- PWM controls LED brightness smoothly
- Understand duty cycle concept
- Can calculate expected brightness
- No visible flicker

---

### Lab 5: Transistor-Controlled Load

**Objective:** Use a transistor to switch a higher-current load from a GPIO pin.

**Prerequisites:**
- Understanding of transistors as switches
- Understanding of current limiting
- Completed Lab 1 (LED circuit)

**Components:**
- NPN transistor (e.g., 2N2222, BC547)
- LED (load)
- Resistor for LED (220Ω or 330Ω)
- Resistor for transistor base (1kΩ)
- Breadboard
- Jumper wires
- Power supply (3.3V or 5V)
- Multimeter

**Theory:**
- Transistor acts as switch controlled by base current
- Small base current controls larger collector current
- Base resistor limits base current to safe level
- Load connected to collector
- Base resistor calculation: Rbase = (Vgpio - Vbe) / (Icollector / hFE)
- Example: For 20mA LED with hFE=100, minimum Ib = 0.2mA, Rbase ≈ (3.3V - 0.7V) / 0.0002A = 13kΩ
- Using 1kΩ provides more base current (2.6mA) for reliable saturation (fully ON state)
- Note: hFE varies by transistor and current—consult datasheet
- Ensure GPIO can provide required base current (typically 20mA max per pin)

**Wiring:**
```
GPIO pin
    │
   Resistor (1kΩ)
    │
   Transistor base
    │
Transistor emitter ─── GND
    │
Transistor collector
    │
   LED
    │
   Resistor (220Ω or 330Ω)
    │
Power supply positive (+)
```

**Expected Behavior:**
- LED off when GPIO is LOW
- LED on when GPIO is HIGH
- Transistor switches LED current
- GPIO provides only small base current

**Measurements:**
- Measure base current (should be small, ~1-5mA)
- Measure collector current (LED current, ~10-20mA)
- Verify transistor switching behavior

**Troubleshooting:**
- LED always on: Check transistor wiring, check GPIO state
- LED always off: Check transistor wiring, check base resistor
- Transistor hot: Check current limits, check load

**Common Mistakes:**
- Incorrect transistor pinout
- Missing base resistor
- Wrong transistor type (NPN vs PNP)
- Exceeding transistor ratings

**Safety:**
- Use low voltage (3.3V or 5V)
- Don't exceed transistor current ratings
- Use appropriate base resistor

**Completion Criteria:**
- Transistor switches load reliably
- GPIO provides only small control current
- Understand transistor as switch concept
- Can calculate base resistor value

---

### Lab 6: Basic Motor/Load Control

**Objective:** Control a small DC motor with transistor and flyback diode.

**Prerequisites:**
- Understanding of transistors as switches
- Understanding of inductive loads and flyback diodes
- Completed Lab 5 (Transistor-controlled load)

**Components:**
- NPN transistor rated for motor current (e.g., 2N2222 for <800mA, BC547 for <100mA)
- Small DC motor (low current, <500mA, check transistor rating)
- Diode (e.g., 1N4007 or 1N4148)
- Resistor for transistor base (1kΩ, calculate based on transistor hFE)
- Breadboard
- Jumper wires
- Power supply (3-6V for motor, must share common GND with GPIO)
- Multimeter

**Theory:**
- Motor is inductive load
- Flyback diode protects transistor from voltage spike when motor turns off
- Transistor switches motor current
- Motor may require separate power supply if current exceeds GPIO supply capability
- Motor startup current can be 2-3x running current
- Common ground is required between GPIO supply and motor supply
- Transistor must be rated for motor current (including startup current)
- Base resistor calculation: Rbase = (Vgpio - Vbe) / (Imotor / hFE)
- Example: For 500mA motor with hFE=100, Ib = 5mA, Rbase ≈ (3.3V - 0.7V) / 0.005A = 520Ω (use 1kΩ for safety)

**Wiring:**
```
GPIO pin
    │
   Resistor (1kΩ)
    │
   Transistor base
    │
Transistor emitter ─── GND (common with motor power supply GND)
    │
Transistor collector
    │
   Motor ─── Motor power supply positive (+)
    │
   Diode (cathode to motor power supply +, anode to transistor collector)
    │
   (Diode in parallel with motor)
```

**Expected Behavior:**
- Motor off when GPIO is LOW
- Motor on when GPIO is HIGH
- Motor runs smoothly
- No voltage spikes damage transistor

**Measurements:**
- Measure motor current
- Measure transistor current
- Verify flyback diode protection

**Troubleshooting:**
- Motor not running: Check power supply, check transistor, check connections
- Transistor getting hot: Check current, check flyback diode
- Motor runs poorly: Check power supply, check motor rating

**Common Mistakes:**
- Missing flyback diode
- Incorrect diode polarity
- Insufficient transistor current rating
- Insufficient power supply current

**Safety:**
- Use low voltage for motor (3-6V)
- Don't exceed motor current rating
- Ensure flyback diode is correctly installed
- Keep fingers away from moving motor parts

**Completion Criteria:**
- Motor runs reliably
- Flyback diode protects transistor
- Understand inductive load protection
- Can troubleshoot motor circuit

---

## Projects

### Project: Low-Voltage Electronics Test Board

**Objective:** Create a reusable breadboard setup demonstrating multiple electronic concepts.

**Requirements:**
- LED circuit with current limiting
- Button circuit with pull-up resistor
- Potentiometer as voltage divider
- PWM LED brightness control
- Transistor switching demonstration
- All circuits on single breadboard
- Documentation of each circuit
- Measurements and observations

**Suggested Layout:**
- Power rails on breadboard
- LED circuit in one section
- Button circuit in another section
- Potentiometer in another section
- Transistor circuit in another section
- Clear labeling of each section

**Deliverables:**
- Working breadboard with all circuits
- Documentation of each circuit (schematic, explanation)
- Measurements for each circuit
- Troubleshooting notes
- What you learned from each circuit

**Time Estimate:** 3-4 hours

**Note:** This project uses safe low-voltage circuits only. No mains voltage or high-power circuits.

---

## Common Mistakes

### Mistake 1: Exceeding Voltage Ratings
**Problem:** Applying voltage higher than component rating
**Consequence:** Component damage or failure
**Solution:** Always check voltage ratings before connecting

### Mistake 2: Forgetting Current Limiting
**Problem:** Not using current limiting resistors
**Consequence:** Component damage (especially LEDs)
**Solution:** Always calculate and use appropriate current limiting

### Mistake 3: Reversing Polarity
**Problem:** Connecting components backwards (LEDs, diodes, capacitors)
**Consequence:** Component damage or incorrect operation
**Solution:** Always check polarity before connecting

### Mistake 4: Poor Breadboard Connections
**Problem:** Components not making good contact
**Consequence:** Circuit doesn't work or works intermittently
**Solution:** Ensure components are fully inserted, check connections

### Mistake 5: Short Circuits
**Problem:** Accidentally connecting VCC to GND
**Consequence:** Component damage, power supply shutdown
**Solution:** Double-check wiring before powering, use multimeter to check for shorts

### Mistake 6: Measuring Resistance on Powered Circuit
**Problem:** Using multimeter in resistance mode on powered circuit
**Consequence:** Multimeter damage, incorrect readings
**Solution:** Always turn power off before measuring resistance

### Mistake 7: Exceeding GPIO Current Limits
**Problem:** Drawing too much current from GPIO pin
**Consequence:** Microcontroller damage
**Solution:** Use transistors for higher-current loads, check GPIO current limits

### Mistake 8: Missing Flyback Diode
**Problem:** Not using flyback diode with inductive loads
**Consequence:** Transistor damage from voltage spikes
**Solution:** Always use flyback diode with motors, relays, and other inductive loads

---

## Troubleshooting

### Circuit Not Working
**Problem:** Circuit doesn't work as expected
**Solutions:**
- Check power supply (voltage, connections)
- Check component values (resistors, etc.)
- Check polarity (LEDs, diodes, transistors)
- Check wiring (verify connections)
- Use multimeter to measure voltages
- Check for short circuits

### LED Not Lighting
**Problem:** LED doesn't light up
**Solutions:**
- Check LED polarity (reverse anode/cathode)
- Check current limiting resistor
- Measure voltage across LED
- Check power supply
- Verify LED is not damaged

### Button Not Working
**Problem:** Button doesn't register presses
**Solutions:**
- Check pull-up/pull-down resistor
- Check button wiring
- Measure voltage at GPIO
- Check for button bounce
- Verify button is not damaged

### Motor Not Running
**Problem:** Motor doesn't run
**Solutions:**
- Check power supply (voltage, current capacity)
- Check transistor wiring
- Check flyback diode
- Measure motor current
- Verify motor is not damaged

### Transistor Getting Hot
**Problem:** Transistor overheats
**Solutions:**
- Check current through transistor
- Verify transistor current rating
- Check for proper heatsinking
- Check base resistor value
- Verify load is not shorted

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is voltage?
2. What is current?
3. What is resistance?
4. State Ohm's law.
5. Calculate the resistor for an LED with Vsupply=3.3V, VLED=2.0V, I=10mA.
6. Why does an LED need a current limiting resistor?
7. What is ground?
8. What is a floating input?
9. What is the difference between pull-up and pull-down?
10. Why do buttons need debouncing?
11. What is a transistor used for?
12. What is a flyback diode and why is it needed?
13. What is PWM?
14. What is duty cycle?
15. Why can't a GPIO pin directly drive a large motor?
16. What is the difference between series and parallel circuits?
17. What is the purpose of a voltage regulator?
18. Why is current limiting important?
19. What safety precautions should you follow when working with electronics?
20. How do you use a multimeter to measure voltage?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **LED Circuit:**
   - Build an LED circuit with appropriate current limiting resistor
   - Calculate the resistor value for Vsupply=3.3V, VLED=2.0V, I=15mA
   - Measure the voltage across the LED and resistor
   - Verify the current is within safe limits

2. **Button Circuit:**
   - Build a button circuit with pull-up resistor
   - Measure the voltage at the GPIO when button is not pressed
   - Measure the voltage at the GPIO when button is pressed
   - Explain why the pull-up resistor is needed

3. **Potentiometer:**
   - Build a potentiometer circuit as a voltage divider
   - Measure the output voltage at minimum, midpoint, and maximum
   - Explain why the output voltage varies

4. **Transistor Circuit:**
   - Build a transistor circuit to switch an LED
   - Calculate the base resistor value for a desired base current
   - Measure the base current and collector current
   - Explain why the transistor is needed

5. **Troubleshooting:**
   - Given a non-working LED circuit, identify the problem
   - Given a non-working button circuit, identify the problem
   - Explain your troubleshooting approach

**Passing Criteria:** All circuits work correctly, measurements are accurate, and explanations demonstrate understanding.

---

## Completion Checklist

Before moving to Phase 5, verify you have:

- [ ] Understand voltage, current, and resistance
- [ ] Can apply Ohm's law to calculate component values
- [ ] Understand power calculations
- [ ] Can design series and parallel circuits
- [ ] Can read resistor color codes
- [ ] Can calculate current-limiting resistors for LEDs
- [ ] Can use a breadboard correctly
- [ ] Can use a multimeter to measure voltage, current, and resistance
- [ ] Understand transistors and MOSFETs
- [ ] Can drive loads with transistors
- [ ] Understand flyback diodes
- [ ] Follow electrical safety guidelines
- [ ] Completed Lab 1: LED
- [ ] Completed Lab 2: Button
- [ ] Completed Lab 3: Potentiometer
- [ ] Completed Lab 4: PWM LED
- [ ] Completed Lab 5: Transistor-controlled load
- [ ] Completed Lab 6: Basic motor/load control
- [ ] Completed the electronics test board project
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Can troubleshoot basic circuit problems

---

## Do Not Continue Until...

**Do not start Phase 5 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You have completed all 6 labs
5. You have completed the electronics test board project
6. You can build basic circuits without copying a tutorial
7. You understand electrical safety
8. You can use a multimeter effectively

**Electronics skills are essential for working with microcontrollers. Take the time to master these practical skills—you'll use them constantly in embedded systems development.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 5 — Microcontrollers**

Phase 5 will teach you microcontroller architecture, registers, memory maps, interrupts, and the embedded development workflow—bridging the gap between electronics and actual MCU programming.

---

**Practical electronics skills are essential for embedded systems development. The labs you've completed provide hands-on experience with real circuits. These skills will be used throughout your embedded systems journey.**
