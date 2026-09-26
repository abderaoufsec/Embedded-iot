# Phase 3 — Digital Electronics

> **Goal:** Understand digital electronics fundamentals, logic gates, Boolean algebra, and how digital circuits work—essential foundation for understanding how microcontrollers process data.
>
> **Prerequisite:** Phase 2 — C Programming
>
> **Outcome:** You can design and analyze digital circuits, understand logic gates and Boolean algebra, and grasp how microcontrollers use digital electronics internally.

---

## What You Will Learn

By completing this phase, you will understand:

- Voltage and current concepts for digital systems
- Analog vs digital signals
- HIGH/LOW logic states
- Logic levels and voltage thresholds
- Boolean algebra and logic expressions
- Truth tables for all basic gates
- AND, OR, NOT, NAND, NOR, XOR gates
- Combinational logic circuits
- Sequential logic circuits
- Flip-flops and memory elements
- Registers and counters
- Clock signals and timing
- Pull-up and pull-down resistors
- GPIO electrical concepts
- Button debouncing
- ADC (Analog-to-Digital Converter) concepts
- DAC (Digital-to-Analog Converter) concepts
- PWM (Pulse Width Modulation) concepts
- How all these concepts relate to microcontrollers

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phase 0 — Orientation
- ✅ Completed Phase 1 — Computer Fundamentals
- ✅ Completed Phase 2 — C Programming
- ✅ Understanding of binary and hexadecimal
- ✅ Understanding of basic Boolean logic
- ✅ Basic arithmetic skills

**No prior electronics knowledge is required.**

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain the difference between analog and digital signals
- Understand logic levels and voltage thresholds
- Create truth tables for logic gates
- Simplify Boolean expressions
- Design simple combinational logic circuits
- Understand sequential logic and timing
- Explain how flip-flops work
- Understand the role of clocks in digital systems
- Explain pull-up and pull-down resistors
- Understand GPIO electrical behavior
- Explain button debouncing and why it's needed
- Understand the basic concepts of ADC, DAC, and PWM
- Explain how digital electronics concepts apply to microcontrollers
- Design simple digital logic circuits
- Analyze existing digital circuits

---

## Concepts

### Voltage and Current Concepts

**Voltage:** Electrical potential difference between two points
- Measured in volts (V)
- Analogous to water pressure in a pipe
- Digital systems use specific voltage levels to represent 0 and 1

**Current:** Flow of electric charge
- Measured in amperes (A)
- Analogous to water flow rate
- Digital circuits consume current when switching states

**Why this matters for microcontrollers:** Microcontrollers operate at specific voltage levels (typically 3.3V or 5V). Understanding voltage and current is essential for connecting peripherals safely.

### Analog vs Digital Signals

**Analog Signal:** Continuous signal that can take any value within a range
- Example: Temperature sensor output (0-5V representing 0-100°C)
- Infinite possible values
- Susceptible to noise

**Digital Signal:** Discrete signal with only specific values
- Example: GPIO pin (0V or 3.3V only)
- Finite number of values (typically just 0 and 1)
- More resistant to noise

**Why this matters:** Microcontrollers are digital devices but often interact with the analog world. Understanding the difference is crucial for sensor integration and communication.

### HIGH/LOW Logic States

**HIGH (Logic 1):** Represents the "on" or "true" state
- Typically 3.3V or 5V depending on the microcontroller
- May be defined as voltage above a threshold

**LOW (Logic 0):** Represents the "off" or "false" state
- Typically 0V (ground)
- May be defined as voltage below a threshold

**Why this matters:** All digital communication in microcontrollers uses HIGH/LOW states. You need to understand what voltage levels constitute valid logic states.

### Logic Levels and Voltage Thresholds

**Logic Levels:** Specific voltage ranges that represent valid logic states

**3.3V Logic Levels (typical):**
- Logic HIGH: > 2.0V
- Logic LOW: < 0.8V
- Undefined region: 0.8V - 2.0V (avoid this region)

**5V Logic Levels (typical):**
- Logic HIGH: > 2.4V
- Logic LOW: < 0.8V
- Undefined region: 0.8V - 2.4V

**Why this matters:** When connecting components to a microcontroller, you must ensure they use compatible logic levels. Mismatched logic levels can cause incorrect operation or damage.

### Boolean Algebra

**Boolean Algebra:** Mathematical system for logic operations
- Variables can only be true (1) or false (0)
- Operations: AND, OR, NOT, NAND, NOR, XOR
- Used to design and simplify digital circuits

**Basic Laws:**
- **Identity:** A + 0 = A, A · 1 = A
- **Complement:** A + A' = 1, A · A' = 0
- **Idempotent:** A + A = A, A · A = A
- **Commutative:** A + B = B + A, A · B = B · A
- **Associative:** (A + B) + C = A + (B + C)
- **Distributive:** A · (B + C) = A·B + A·C
- **De Morgan's:** (A + B)' = A' · B', (A · B)' = A' + B'

**Why this matters:** Boolean algebra is used to design and optimize digital circuits. Understanding it helps you create efficient logic for microcontroller programs.

### Truth Tables

**Truth Table:** Table showing all possible inputs and corresponding outputs for a logic gate or circuit

**Example for AND gate:**
| A | B | Output |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   0    |
| 1 | 0 |   0    |
| 1 | 1 |   1    |

**Why this matters:** Truth tables help you understand and verify logic behavior. They're essential for designing and debugging digital circuits.

### Logic Gates

**AND Gate:** Output is 1 only if all inputs are 1
- Symbol: D-shaped
- Boolean: A · B
- Truth table: Output = 1 only when A=1 AND B=1

**OR Gate:** Output is 1 if any input is 1
- Symbol: Curved shape
- Boolean: A + B
- Truth table: Output = 1 when A=1 OR B=1

**NOT Gate:** Output is the inverse of input
- Symbol: Triangle with circle
- Boolean: A'
- Truth table: Output = NOT A

**NAND Gate:** NOT AND (output is 0 only if all inputs are 1)
- Symbol: AND with circle on output
- Boolean: (A · B)'
- Truth table: Output = 0 only when A=1 AND B=1

**NOR Gate:** NOT OR (output is 1 only if all inputs are 0)
- Symbol: OR with circle on output
- Boolean: (A + B)'
- Truth table: Output = 1 only when A=0 AND B=0

**XOR Gate:** Output is 1 if inputs are different
- Symbol: OR with extra curved line
- Boolean: A ⊕ B = A·B' + A'·B
- Truth table: Output = 1 when A≠B

**Why this matters:** Logic gates are the building blocks of all digital circuits, including microcontrollers. Understanding them is fundamental to digital electronics.

### Combinational Logic

**Combinational Logic:** Output depends only on current inputs
- No memory of past inputs
- No clock signal required
- Examples: Adders, multiplexers, decoders

**Example: Simple combinational circuit**
```
A ──┬── AND ──┬── OR ── Output
    │         │
B ──┴─────────┘
```

**Why this matters:** Combinational logic is used for decision-making in microcontrollers. Understanding it helps you design efficient logic in your code.

### Sequential Logic

**Sequential Logic:** Output depends on current inputs AND past inputs
- Has memory of past states
- Requires clock signal
- Examples: Flip-flops, counters, shift registers

**Key difference from combinational:** Sequential logic can "remember" previous states, enabling circuits to perform tasks over time.

**Why this matters:** Sequential logic is the foundation of memory and state machines in microcontrollers. Counters, timers, and state machines all use sequential logic.

### Flip-Flops

**Flip-Flop:** Basic memory element that can store one bit
- Has two stable states (0 and 1)
- Changes state based on clock and input signals
- The building block of registers and memory

**D Flip-Flop (Data Flip-Flop):**
- Input: D (data), CLK (clock)
- Output: Q (current state), Q' (inverse)
- On clock edge, Q takes the value of D
- Used for registers and memory

**Why this matters:** Flip-flops are used throughout microcontrollers for registers, memory, and state machines. Understanding them is essential for timing-sensitive operations.

### Registers

**Register:** Group of flip-flops that store multiple bits
- Typically 8, 16, 32, or 64 bits
- Used to store data, addresses, or control information
- Can be read from and written to

**CPU Registers:** Fast storage inside the CPU for data and addresses
- General-purpose registers
- Program counter
- Stack pointer
- Status register

**Why this matters:** CPU registers are fundamental to how microcontrollers execute instructions. Understanding registers is crucial for efficient embedded programming.

### Counters

**Counter:** Sequential circuit that counts clock pulses
- Can count up, down, or both
- Can be binary or decimal
- Used for timing, frequency division, event counting

**Types:**
- **Ripple counter:** Simple but slow
- **Synchronous counter:** Faster but more complex
- **Modulo counter:** Counts to a specific value then resets

**Why this matters:** Counters are used in microcontrollers for timers, PWM generation, and measuring time intervals.

### Clock Signals

**Clock:** Periodic signal that synchronizes digital circuits
- Square wave with fixed frequency
- Coordinates timing of all operations
- Measured in Hz (cycles per second)

**Clock Edge:** Transition from 0 to 1 (rising edge) or 1 to 0 (falling edge)
- Many circuits change state on clock edges
- Rising edge more common

**Why this matters:** Clock signals coordinate all operations in a microcontroller. Understanding clock timing is essential for synchronization and timing-sensitive operations.

### Pull-Up and Pull-Down Resistors

**Pull-Up Resistor:** Resistor connecting a signal to VCC (positive supply)
- Ensures signal is HIGH when not actively driven
- Typical value: 10kΩ
- Used with buttons, switches, I2C buses

**Pull-Down Resistor:** Resistor connecting a signal to ground
- Ensures signal is LOW when not actively driven
- Typical value: 10kΩ
- Used with buttons, switches

**Why they're needed:** When a button is open (not pressed), the signal is "floating" (undefined). Pull-up/pull-down resistors ensure the signal has a defined state.

**Why this matters:** Pull-up/pull-down resistors are essential for reliable GPIO input. Without them, buttons and switches will produce unpredictable readings.

### GPIO Electrical Concepts

**GPIO (General Purpose Input/Output):** Microcontroller pins that can be configured as inputs or outputs

**Input Mode:**
- Reads the voltage on the pin
- Can use internal or external pull-up/pull-down
- High impedance (doesn't drive the pin)

**Output Mode:**
- Drives the pin HIGH or LOW
- Can source or sink current
- Limited current capability (typically 20mA per pin)

**Why this matters:** GPIO pins are how microcontrollers interact with the physical world. Understanding their electrical characteristics is essential for connecting components safely.

### Button Debouncing

**Debounce:** Removing transient signal changes when a mechanical switch changes state

**Problem:** Mechanical switches "bounce" when pressed/released
- Contact makes/breaks multiple times rapidly
- Causes multiple transitions that look like multiple presses
- Can last several milliseconds

**Solution:**
- **Hardware debounce:** RC filter (resistor + capacitor)
- **Software debounce:** Wait a few milliseconds after initial transition before reading again

**Why this matters:** Without debouncing, a single button press might register as multiple presses. This is a common source of bugs in embedded systems.

### ADC (Analog-to-Digital Converter) Concepts

**ADC:** Converts analog voltage to digital value
- Continuous voltage → discrete digital value
- Resolution: Number of bits (e.g., 10-bit, 12-bit)
- Sampling rate: How fast it can convert

**Example: 10-bit ADC with 3.3V reference**
- Range: 0-3.3V
- Resolution: 1024 steps (2¹⁰)
- Each step: 3.3V / 1024 ≈ 3.2mV

**Why this matters:** Microcontrollers use ADCs to read analog sensors (temperature, light, etc.). Understanding ADC concepts is essential for sensor integration.

### DAC (Digital-to-Analog Converter) Concepts

**DAC:** Converts digital value to analog voltage
- Discrete digital value → continuous voltage
- Resolution: Number of bits
- Used for generating analog signals

**Example: 8-bit DAC with 3.3V reference**
- Range: 0-3.3V
- Resolution: 256 steps (2⁸)
- Each step: 3.3V / 256 ≈ 12.9mV

**Why this matters:** DACs are used to generate analog signals (audio, control voltages). Understanding DAC concepts is useful for audio and control applications.

### PWM (Pulse Width Modulation) Concepts

**PWM:** Technique for generating analog-like signals using digital pulses
- Vary the width (duty cycle) of pulses
- Average voltage varies with duty cycle
- Used for dimming LEDs, motor speed control, etc.

**Duty Cycle:** Percentage of time signal is HIGH
- 0% duty cycle: Always LOW (0V average)
- 50% duty cycle: Half HIGH, half LOW (1.65V average for 3.3V)
- 100% duty cycle: Always HIGH (3.3V average)

**Frequency:** How fast pulses repeat
- Higher frequency = smoother output
- Too high = hardware limitations
- Too low = visible flicker (for LEDs)

**Why this matters:** PWM is used extensively in embedded systems for LED dimming, motor control, and generating analog signals. It's a fundamental technique you'll use constantly.

---

## Exact Resources

### Resource 1: Logic Gates Tutorial
- **Provider:** Electronics Tutorials
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Learn about logic gates and Boolean algebra
- **URL:** https://www.electronics-tutorials.ws/logic/

### Resource 2: Digital Electronics Tutorial
- **Provider:** All About Circuits
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Comprehensive digital electronics fundamentals
- **URL:** https://www.allaboutcircuits.com/textbook/digital/

### Resource 3: Pull-Up/Pull-Down Resistors
- **Provider:** SparkFun Electronics
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Understand pull-up and pull-down resistors
- **URL:** https://learn.sparkfun.com/tutorials/pull-up-resistors

### Resource 4: ADC and DAC Basics
- **Provider:** Adafruit Learning System
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Understand analog-to-digital and digital-to-analog conversion
- **URL:** https://learn.adafruit.com/adc-basics

### Resource 5: PWM Tutorial
- **Provider:** SparkFun Electronics
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Learn about pulse width modulation
- **URL:** https://learn.sparkfun.com/tutorials/pulse-width-modulation

---

## Study Order

Follow this exact sequence:

1. **Study voltage and current concepts**
2. **Understand analog vs digital signals**
3. **Learn HIGH/LOW logic states**
4. **Study logic levels and voltage thresholds**
5. **Learn Boolean algebra basics**
6. **Study truth tables**
7. **Learn each logic gate (AND, OR, NOT, NAND, NOR, XOR)**
8. **Practice creating truth tables**
9. **Study combinational logic**
10. **Learn sequential logic**
11. **Understand flip-flops**
12. **Study registers**
13. **Learn counters**
14. **Understand clock signals**
15. **Study pull-up and pull-down resistors**
16. **Learn GPIO electrical concepts**
17. **Understand button debouncing**
18. **Study ADC concepts**
19. **Learn DAC concepts**
20. **Study PWM concepts**
21. **Complete all exercises**
22. **Complete the project**
23. **Take the knowledge test**
24. **Take the practical test**
25. **Review completion checklist**

---

## Exercises

### Exercise 1: Truth Tables

**Objective:** Create truth tables for all basic logic gates.

**Tasks:**
1. Create a truth table for AND gate with 2 inputs
2. Create a truth table for OR gate with 2 inputs
3. Create a truth table for NOT gate
4. Create a truth table for NAND gate with 2 inputs
5. Create a truth table for NOR gate with 2 inputs
6. Create a truth table for XOR gate with 2 inputs
7. Create a truth table for XNOR gate with 2 inputs

**Expected Outcome:** You can create truth tables for any logic gate.

### Exercise 2: Boolean Expressions

**Objective:** Practice Boolean algebra and simplification.

**Tasks:**
1. Simplify: A + A·B
2. Simplify: (A + B)·(A + C)
3. Simplify: A·B + A·B'
4. Simplify: (A + B)'·C
5. Apply De Morgan's law to: (A·B)'
6. Apply De Morgan's law to: (A + B)'
7. Convert the expression A·B + A'·C to a truth table

**Expected Outcome:** You can simplify Boolean expressions using Boolean algebra.

### Exercise 3: Logic Gate Reasoning

**Objective:** Analyze simple logic circuits.

**Tasks:**
1. Given inputs A=1, B=0, C=1, what is the output of (A AND B) OR C?
2. Given inputs A=1, B=1, what is the output of NOT (A XOR B)?
3. Given inputs A=0, B=1, what is the output of (A NAND B) AND C (where C=1)?
4. Design a circuit that outputs 1 only when A=1 AND B=0
5. Design a circuit that outputs 1 when A=1 OR B=1, but not both

**Expected Outcome:** You can analyze and design simple logic circuits.

### Exercise 4: Pull-Up/Pull-Down Reasoning

**Objective:** Understand when to use pull-up or pull-down resistors.

**Tasks:**
1. A button connects a GPIO pin to ground when pressed. Should you use pull-up or pull-down?
2. A button connects a GPIO pin to VCC when pressed. Should you use pull-up or pull-down?
3. An I2C line is open when not actively driven. Should you use pull-up or pull-down?
4. What happens if you don't use a pull-up/pull-down resistor with a button?
5. What is a typical value for pull-up/pull-down resistors?

**Expected Outcome:** You understand when and how to use pull-up/pull-down resistors.

### Exercise 5: Debounce Reasoning

**Objective:** Understand button debouncing.

**Tasks:**
1. Why do mechanical switches bounce?
2. How long does switch bounce typically last?
3. What is hardware debouncing?
4. What is software debouncing?
5. If a button bounces for 5ms, how long should you wait in software before reading the button again?
6. What happens if you don't debounce a button?

**Expected Outcome:** You understand the debouncing problem and solutions.

### Exercise 6: GPIO Reasoning

**Objective:** Understand GPIO electrical characteristics.

**Tasks:**
1. A GPIO pin is configured as input. What is its impedance?
2. A GPIO pin is configured as output HIGH. What is the typical voltage?
3. If a GPIO pin can source 20mA, how many 10mA LEDs can it drive?
4. What happens if you exceed the current limit of a GPIO pin?
5. Why do you need current-limiting resistors with LEDs?

**Expected Outcome:** You understand GPIO electrical limitations and how to use them safely.

### Exercise 7: ADC/DAC Concepts

**Objective:** Understand analog-to-digital and digital-to-analog conversion.

**Tasks:**
1. A 10-bit ADC has a 3.3V reference. What is the resolution in volts?
2. A 12-bit ADC has a 3.3V reference. What is the resolution in volts?
3. An ADC reads the value 512 on a 10-bit ADC with 3.3V reference. What is the input voltage?
4. An 8-bit DAC has a 3.3V reference. What is the output voltage for value 128?
5. What is the difference between ADC and DAC?

**Expected Outcome:** You understand ADC and DAC concepts and calculations.

### Exercise 8: PWM Concepts

**Objective:** Understand pulse width modulation.

**Tasks:**
1. A PWM signal has 50% duty cycle and 3.3V amplitude. What is the average voltage?
2. A PWM signal has 25% duty cycle and 3.3V amplitude. What is the average voltage?
3. You want to dim an LED to 50% brightness. What duty cycle should you use?
4. What happens if PWM frequency is too low for an LED?
5. What happens if PWM frequency is too high for an LED?

**Expected Outcome:** You understand PWM concepts and calculations.

---

## Labs

There are no hardware labs in this phase. Labs begin in Phase 4 (Electronics).

---

## Debugging Tasks

There are no debugging tasks in this phase. Debugging exercises begin in later phases.

---

## Project

**Project: Digital Logic Simulator**

**Objective:** Create a simple program that simulates basic logic gates and circuits.

**Requirements:**
- Implement AND, OR, NOT, NAND, NOR, XOR gates as functions
- Allow chaining of gates (output of one gate as input to another)
- Display truth tables for any gate
- Allow the user to build simple circuits
- Include documentation explaining each gate

**Suggested Implementation (Python or any language you know):**
```python
def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return (a and not b) or (not a and b)

def truth_table(gate_func, name):
    print(f"Truth table for {name}:")
    print("A | B | Output")
    print("--|---|-------")
    for a in [0, 1]:
        for b in [0, 1]:
            output = int(gate_func(a, b))
            print(f"{a} | {b} |   {output}")

# Example usage
truth_table(AND, "AND")
```

**Extensions (optional):**
- Implement more complex circuits (half adder, full adder)
- Implement flip-flop simulation
- Add graphical output
- Allow saving and loading circuits

**Time Estimate:** 2-3 hours

**Deliverable:** Working logic simulator with documentation.

---

## Common Mistakes

### Mistake 1: Confusing Analog and Digital
**Problem:** Treating analog signals as digital
**Consequence:** Incorrect sensor readings or communication errors
**Solution:** Always understand whether a signal is analog or digital before using it

### Mistake 2: Ignoring Logic Levels
**Problem:** Assuming any voltage above 0V is logic HIGH
**Consequence:** Incorrect logic interpretation
**Solution:** Always check voltage thresholds for the specific logic family

### Mistake 3: Forgetting Pull-Up/Pull-Down
**Problem:** Not using pull-up/pull-down resistors with buttons
**Consequence:** Unpredictable button readings
**Solution:** Always use pull-up or pull-down resistors with mechanical switches

### Mistake 4: Not Debouncing Buttons
**Problem:** Treating button bounce as multiple presses
**Consequence:** Multiple unintended actions
**Solution:** Always implement debouncing (hardware or software)

### Mistake 5: Exceeding GPIO Current Limits
**Problem:** Drawing too much current from a GPIO pin
**Consequence:** Damage to the microcontroller
**Solution:** Always check current limits and use appropriate current-limiting resistors

### Mistake 6: Confusing Combinational and Sequential Logic
**Problem:** Treating sequential logic as combinational
**Consequence:** Incorrect circuit behavior
**Solution:** Understand whether a circuit needs memory (sequential) or not (combinational)

---

## Troubleshooting

### Logic Circuit Not Working
**Problem:** Logic circuit produces incorrect output
**Solutions:**
- Verify truth table
- Check gate connections
- Verify input values
- Check for floating inputs (use pull-up/pull-down)
- Verify voltage levels

### Button Readings Unpredictable
**Problem:** Button gives random readings
**Solutions:**
- Add pull-up or pull-down resistor
- Implement debouncing
- Check wiring
- Verify voltage levels

### ADC Readings Incorrect
**Problem:** ADC gives unexpected values
**Solutions:**
- Verify reference voltage
- Check input voltage range
- Verify ADC resolution
- Check for noise on input
- Verify proper grounding

### PWM Not Working as Expected
**Problem:** PWM output doesn't produce expected behavior
**Solutions:**
- Verify duty cycle calculation
- Check PWM frequency
- Verify voltage levels
- Check load impedance
- Verify proper pin configuration

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is the difference between analog and digital signals?
2. What are logic levels?
3. What is a truth table?
4. What is the output of AND gate when inputs are A=1, B=0?
5. What is the output of OR gate when inputs are A=1, B=0?
6. What is the output of NOT gate when input is 1?
7. What is the output of XOR gate when inputs are A=1, B=1?
8. What is the difference between combinational and sequential logic?
9. What is a flip-flop?
10. What is a register?
11. What is a clock signal?
12. What is a pull-up resistor used for?
13. What is a pull-down resistor used for?
14. Why do buttons need debouncing?
15. What is an ADC?
16. What is a DAC?
17. What is PWM?
18. What is duty cycle?
19. What is the resolution of a 10-bit ADC with 3.3V reference?
20. Why are pull-up/pull-down resistors important for GPIO?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **Truth Table Creation:**
   - Create a truth table for the expression: (A AND B) OR C
   - Create a truth table for the expression: NOT (A XOR B)
   - Create a truth table for a 3-input AND gate

2. **Boolean Simplification:**
   - Simplify: A + A·B
   - Simplify: (A + B)·(A + B')
   - Simplify: A·B + A·B' + A'·B

3. **Logic Circuit Design:**
   - Design a circuit that outputs 1 when A=1, B=0, C=1
   - Design a circuit that outputs 1 when at least two inputs are 1
   - Design a circuit that outputs 1 when inputs are different (XOR)

4. **ADC/DAC Calculations:**
   - Calculate the resolution of a 12-bit ADC with 3.3V reference
   - What input voltage produces an ADC reading of 1024 on a 10-bit ADC with 3.3V reference?
   - What is the output voltage of an 8-bit DAC with value 200 and 3.3V reference?

5. **PWM Calculations:**
   - What duty cycle produces 1.65V average voltage from a 3.3V PWM signal?
   - What is the average voltage of a 75% duty cycle PWM signal with 3.3V amplitude?
   - What duty cycle should you use to dim an LED to 25% brightness?

**Passing Criteria:** Complete all tasks with correct results and show your work.

---

## Completion Checklist

Before moving to Phase 4, verify you have:

- [ ] Understand voltage and current concepts
- [ ] Can explain analog vs digital signals
- [ ] Understand HIGH/LOW logic states
- [ ] Understand logic levels and voltage thresholds
- [ ] Can create truth tables
- [ ] Understand Boolean algebra
- [ ] Can simplify Boolean expressions
- [ ] Understand all basic logic gates (AND, OR, NOT, NAND, NOR, XOR)
- [ ] Can analyze simple logic circuits
- [ ] Understand combinational vs sequential logic
- [ ] Understand flip-flops and registers
- [ ] Understand counters and clock signals
- [ ] Understand pull-up and pull-down resistors
- [ ] Understand GPIO electrical concepts
- [ ] Understand button debouncing
- [ ] Understand ADC concepts
- [ ] Understand DAC concepts
- [ ] Understand PWM concepts
- [ ] Completed all exercises
- [ ] Completed the logic simulator project
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Understand how these concepts relate to microcontrollers

---

## Do Not Continue Until...

**Do not start Phase 4 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can create truth tables for any logic gate
5. You understand why pull-up/pull-down resistors are necessary
6. You understand why button debouncing is necessary
7. You have completed the logic simulator project
8. You understand the relationship between digital electronics and microcontrollers

**Digital electronics is the foundation for understanding how microcontrollers work internally. Take the time to master these concepts.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 4 — Electronics**

Phase 4 will teach you practical electronics fundamentals including voltage, current, resistance, Ohm's law, components, and hands-on labs with real hardware at safe low-voltage levels.

---

**Digital electronics concepts are used throughout embedded systems. From logic gates to PWM, these concepts form the basis of how microcontrollers process and generate signals. Understanding them is essential for effective embedded programming.**
