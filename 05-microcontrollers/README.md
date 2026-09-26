# Phase 5 — Microcontrollers

> **Goal:** Understand microcontroller architecture, registers, memory maps, interrupts, and the embedded development workflow—independent of any specific platform.
>
> **Prerequisite:** Phase 4 — Electronics
>
> **Outcome:** You understand MCU architecture, the development workflow, and how software interacts with hardware through registers and memory-mapped peripherals.

---

## What You Will Learn

By completing this phase, you will understand:

- What a microcontroller is and how it differs from a microprocessor
- MCU architecture (CPU, memory, peripherals)
- Registers and register files
- Memory organization (Flash, SRAM, EEPROM)
- Memory maps and addressing
- GPIO (General Purpose Input/Output)
- Timers and counters
- PWM (Pulse Width Modulation) hardware
- ADC (Analog-to-Digital Converter) hardware
- DAC (Digital-to-Analog Converter) hardware
- UART, SPI, I2C communication peripherals
- Interrupt controller and interrupt handling
- Clock system and clock distribution
- Watchdog timer
- Reset and boot process
- Firmware and startup code
- Linker and memory layout
- Peripheral registers and memory-mapped I/O
- Polling vs interrupts
- DMA (Direct Memory Access) concept
- Bare-metal programming
- HAL (Hardware Abstraction Layer)
- BSP (Board Support Package)
- Drivers and device drivers
- Embedded development workflow

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phase 0 — Orientation
- ✅ Completed Phase 1 — Computer Fundamentals
- ✅ Completed Phase 2 — C Programming
- ✅ Completed Phase 3 — Digital Electronics
- ✅ Completed Phase 4 — Electronics
- ✅ Understanding of binary and hexadecimal
- ✅ Understanding of memory addressing
- ✅ Understanding of pointers in C
- ✅ Understanding of basic electronics

**No prior microcontroller experience is required.**

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain the difference between MCU and MPU
- Describe typical MCU architecture
- Understand memory organization and memory maps
- Explain how peripheral registers control hardware
- Understand the embedded development workflow
- Explain the boot process and startup code
- Understand interrupts and interrupt handling
- Explain polling vs interrupts
- Understand DMA and when to use it
- Explain the role of HAL, BSP, and drivers
- Read and understand memory maps
- Perform register-based calculations
- Design simple register-based control code
- Understand the firmware build process
- Explain how software interacts with hardware

---

## Concepts

### What is a Microcontroller?

**Microcontroller (MCU):** A complete computer system on a single chip
- Contains CPU, memory, and peripherals
- Designed for specific control applications
- Resource-constrained (limited memory, processing power)
- Low power consumption
- Low cost

**Key characteristics:**
- Integrated CPU, memory, and peripherals
- Single-chip solution
- Optimized for control tasks
- Real-time operation often required
- Typically used in embedded systems

**Note:** Specific peripherals and their availability vary by MCU vendor and family. Not all MCUs have all peripherals. This phase teaches universal concepts—check your specific MCU datasheet for available peripherals.

**Example applications:**
- Microwave oven controller
- Thermostat
- Car engine control unit
- Digital camera
- Remote control

**Why this matters:** Understanding what an MCU is and how it differs from a general-purpose computer is fundamental to embedded systems development.

### MCU vs MPU

**MCU (Microcontroller Unit):**
- CPU + memory + peripherals on single chip
- Limited memory and processing power
- Low power consumption
- Low cost
- Used for specific control tasks
- Example: ESP32, STM32, Arduino (ATmega)

**MPU (Microprocessor Unit):**
- CPU only on chip
- Requires external memory and peripherals
- Higher processing power
- Higher power consumption
- Higher cost
- Used for general-purpose computing
- Example: Intel Core, ARM Cortex-A

**Key difference:** MCUs are self-contained systems, while MPUs require external components. MCUs are optimized for control tasks, while MPUs are optimized for general computing.

**Why this matters:** Understanding the difference helps you choose the right platform for your application and understand the design trade-offs.

### MCU Architecture

**Typical MCU Architecture:**
```
┌─────────────────────────────────────┐
│          CPU Core                   │
│  (ALU, Control Unit, Registers)    │
└──────────────┬──────────────────────┘
               │
       ┌───────┴───────┐
       │               │
┌──────┴──────┐  ┌────┴─────┐
│   Memory    │  │ Peripherals │
│  (Flash,    │  │ (GPIO,    │
│   SRAM,     │  │  UART,    │
│   EEPROM)   │  │  SPI,     │
│             │  │  I2C,     │
│             │  │  Timers,  │
│             │  │  ADC,     │
│             │  │  PWM)     │
└─────────────┘  └───────────┘
```

**Components:**
- **CPU Core:** Executes instructions
- **Memory:** Stores program and data
- **Peripherals:** Interface with external world
- **Bus System:** Connects components
- **Clock System:** Provides timing
- **Power Management:** Controls power consumption

**Why this matters:** Understanding MCU architecture helps you understand how software interacts with hardware and how to optimize your code.

### CPU Core

**CPU Core:** The processing unit that executes instructions
- **ALU (Arithmetic Logic Unit):** Performs mathematical and logical operations
- **Control Unit:** Decodes instructions and controls data flow
- **Registers:** Fast internal storage for data and addresses
- **Program Counter:** Holds address of next instruction
- **Stack Pointer:** Points to top of stack
- **Status Register:** Holds flags (zero, carry, overflow, etc.)

**Types:**
- **8-bit:** Simple, limited (e.g., ATmega, Arduino)
- **16-bit:** Moderate capability (e.g., MSP430)
- **32-bit:** High capability (e.g., ARM Cortex-M, ESP32)
- **64-bit:** Very high capability (rare in MCUs)

**Why this matters:** The CPU core determines the processing capability of the MCU. Understanding it helps you write efficient code and understand performance limitations.

### Registers

**Registers:** Fast internal storage locations inside the CPU
- Hold data currently being processed
- Much faster than main memory
- Used for temporary storage, addresses, flags
- Each register has a specific purpose

**Types:**
- **General-purpose registers:** Hold data for calculations
- **Special-purpose registers:** Program counter, stack pointer, status register
- **Peripheral registers:** Control and monitor peripherals

**Example:**
```
R0 = 0x10        // Load value into register
R1 = 0x20        // Load value into register
R0 = R0 + R1     // Add registers
```

**Why this matters:** Registers are fundamental to CPU operation. Understanding registers is essential for writing efficient code and understanding how peripherals are controlled.

### Memory Organization

**Flash Memory:** Non-volatile program memory
- Stores firmware/code
- Retains data when power is removed
- Slower read than SRAM
- Limited write cycles
- Large capacity (typically 32KB - 2MB)

**SRAM (Static RAM):** Volatile data memory
- Stores variables, stack, heap
- Fast read/write access
- Loses data when power is removed
- Limited capacity (typically 2KB - 512KB)

**EEPROM (Electrically Erasable Programmable ROM):** Non-volatile data memory
- Stores configuration data, calibration data
- Can be written and erased electrically
- Slower than Flash
- Limited write cycles
- Small capacity (typically 512B - 4KB)

**Why this matters:** Understanding memory organization is essential for efficient memory usage and understanding where to store different types of data.

### Memory Map

**Memory Map:** How memory addresses are organized
- Different memory regions have different address ranges
- Each byte has a unique address
- Memory-mapped peripherals use specific address ranges

**Example Memory Map:**
```
0x00000000 - 0x0007FFFF: Flash (512KB)
0x3FFB0000 - 0x3FFBFFFF: SRAM (256KB)
0x40000000 - 0x40000FFF: GPIO registers
0x40001000 - 0x40001FFF: UART registers
0x40002000 - 0x40002FFF: Timer registers
```

**Why this matters:** Memory maps show you where everything is located. Understanding memory maps is essential for memory-mapped I/O and understanding peripheral addressing.

### GPIO (General Purpose Input/Output)

**GPIO:** Pins that can be configured as inputs or outputs
- **Input mode:** Read external signals
- **Output mode:** Drive external signals
- **Alternate function mode:** Special functions (UART, SPI, I2C, etc.)
- **Analog mode:** ADC/DAC

**GPIO Registers:**
- **Direction register:** Configure pin as input or output
- **Output data register:** Set output value
- **Input data register:** Read input value
- **Pull-up/pull-down register:** Enable pull-up/pull-down resistors
- **Alternate function register:** Select alternate function

**Example:**
```c
// Set GPIO pin 5 as output
GPIO_DIR |= (1 << 5);

// Set GPIO pin 5 HIGH
GPIO_OUT |= (1 << 5);

// Read GPIO pin 2
if (GPIO_IN & (1 << 2)) {
    // Pin is HIGH
}
```

**Why this matters:** GPIO is how microcontrollers interact with the physical world. Understanding GPIO registers is essential for controlling hardware.

### Timers and Counters

**Timer:** Hardware that counts clock cycles
- Can count up or down
- Can generate interrupts on overflow or compare match
- Used for timing, PWM generation, delay measurement

**Counter:** Similar to timer but counts external events
- Counts pulses on external pin
- Used for frequency measurement, event counting

**Timer Registers:**
- **Control register:** Enable timer, configure mode
- **Counter register:** Current count value
- **Prescaler register:** Divide clock frequency
- **Compare register:** Compare value for interrupts
- **Capture register:** Capture count on external event

**Why this matters:** Timers are essential for timing, PWM generation, and measuring time intervals. Understanding timers is crucial for many embedded applications.

### PWM Hardware

**PWM (Pulse Width Modulation) Hardware:** Hardware that generates PWM signals
- Timer-based generation
- Configurable frequency and duty cycle
- Multiple channels
- Hardware generation (no CPU overhead)

**PWM Registers:**
- **Control register:** Enable PWM, configure mode
- **Period register:** Set PWM period (frequency)
- **Duty cycle register:** Set duty cycle
- **Compare register:** Compare value for duty cycle

**Why this matters:** PWM hardware allows efficient generation of PWM signals without CPU intervention. Understanding PWM hardware is essential for LED dimming, motor control, and power control.

### ADC Hardware

**ADC (Analog-to-Digital Converter) Hardware:** Converts analog voltage to digital value
- Multiple channels
- Configurable resolution (8-bit, 10-bit, 12-bit)
- Configurable sampling rate
- Can trigger conversions automatically

**ADC Registers:**
- **Control register:** Enable ADC, configure mode
- **Channel select register:** Select input channel
- **Data register:** Conversion result
- **Status register:** Conversion complete flag

**Why this matters:** ADC hardware allows accurate analog-to-digital conversion. Understanding ADC hardware is essential for reading sensors and analog inputs.

### DAC Hardware

**DAC (Digital-to-Analog Converter) Hardware:** Converts digital value to analog voltage
- Multiple channels
- Configurable resolution
- Can update automatically

**DAC Registers:**
- **Control register:** Enable DAC, configure mode
- **Data register:** Digital value to convert
- **Trigger register:** Trigger conversion

**Why this matters:** DAC hardware allows generation of analog signals. Understanding DAC hardware is useful for audio generation and control applications.

### Communication Peripherals

**UART (Universal Asynchronous Receiver-Transmitter):**
- Serial communication
- Asynchronous (no clock signal)
- Point-to-point
- Configurable baud rate, data bits, parity, stop bits

**SPI (Serial Peripheral Interface):**
- Serial communication
- Synchronous (has clock signal)
- Master-slave architecture
- High speed
- Multiple devices

**I2C (Inter-Integrated Circuit):**
- Serial communication
- Synchronous (has clock signal)
- Multi-master, multi-slave
- Two wires (SDA, SCL)
- Lower speed than SPI

**Peripheral Registers:** Each peripheral has specific registers for configuration and operation.

**Why this matters:** Communication peripherals are essential for interfacing with sensors, displays, and other devices. Understanding these peripherals is crucial for embedded systems.

### Interrupt Controller

**Interrupt Controller:** Hardware that manages interrupts
- Prioritizes interrupts
- Masks/unmasks interrupts
- Provides interrupt vector table
- Handles nested interrupts

**Interrupt Registers:**
- **Enable register:** Enable specific interrupts
- **Flag register:** Interrupt pending flags
- **Priority register:** Set interrupt priority
- **Vector register:** Interrupt handler address

**Why this matters:** Interrupts are essential for real-time response to events. Understanding the interrupt controller is crucial for interrupt-driven programming.

### Clock System

**Clock System:** Provides timing for the MCU
- **Main oscillator:** High-frequency crystal
- **Internal oscillator:** Lower frequency RC oscillator
- **PLL (Phase-Locked Loop):** Multiplies clock frequency
- **Clock dividers:** Divide clock frequency for peripherals
- **Clock gating:** Disable clocks to unused peripherals (power saving)

**Clock Registers:**
- **Control register:** Select clock source, enable PLL
- **Divider register:** Set clock division
- **Gating register:** Enable/disable peripheral clocks

**Why this matters:** The clock system determines the speed of the MCU and peripherals. Understanding clock configuration is essential for performance and power optimization.

### Watchdog Timer

**Watchdog Timer:** Hardware that resets the MCU if it hangs
- Counts down automatically
- Must be periodically reset by software ("feeding the dog")
- If not reset, triggers MCU reset
- Used for reliability in critical systems

**Watchdog Registers:**
- **Control register:** Enable watchdog, set timeout
- **Reload register:** Reset watchdog counter
- **Status register:** Watchdog triggered flag

**Why this matters:** Watchdog timers are essential for reliability in critical systems. Understanding them is important for robust embedded system design.

### Reset and Boot Process

**Reset:** MCU initialization to known state
- **Power-on reset:** MCU powers up
- **External reset:** Reset button pressed
- **Watchdog reset:** Watchdog timer expired
- **Software reset:** Software triggers reset

**Boot Process:**
1. MCU resets
2. Reads reset vector from Flash
3. Jumps to startup code
4. Startup code initializes:
   - Stack pointer
   - Data section (copy from Flash to SRAM)
   - BSS section (zero-initialized)
   - System clocks
   - Peripheral clocks
5. Jumps to main()

**Why this matters:** Understanding the boot process helps you understand how the MCU starts up and where to place initialization code.

### Firmware and Startup Code

**Firmware:** Software stored in Flash memory
- Includes your application code
- Includes startup code
- Includes libraries
- Includes bootloader (if present)

**Startup Code:** Code that runs before main()
- Initializes stack pointer
- Copies data section from Flash to SRAM
- Zero-initializes BSS section
- Initializes system clocks
- Initializes peripheral clocks
- Calls main()

**Why this matters:** Understanding startup code helps you understand the initialization process and where to place custom initialization code.

### Linker and Memory Layout

**Linker:** Combines compiled object files into executable firmware
- Resolves symbols and references
- Assigns addresses to code and data
- Generates memory map
- Creates final firmware image

**Memory Layout:**
```
Flash:
  0x00000000: Interrupt vector table
  0x000000XX: Code (text section)
  0x0000XXXX: Read-only data (rodata section)

SRAM:
  0x3FFB0000: Data section (initialized data)
  0x3FFBXXXX: BSS section (zero-initialized data)
  0x3FFBYYYY: Heap (grows up)
  0x3FFBZZZZ: Stack (grows down)
```

**Linker Script:** Tells linker how to organize memory
- Defines memory regions
- Defines section placement
- Defines stack size
- Defines heap size

**Why this matters:** Understanding the linker and memory layout helps you understand where your code and data are placed and how to optimize memory usage.

### Peripheral Registers and Memory-Mapped I/O

**Memory-Mapped I/O:** Peripherals accessed as memory locations
- Each peripheral register has a specific memory address
- Reading/writing to that address controls the peripheral
- Simplifies hardware access from software

**Example:**
```c
#define GPIO_BASE 0x40000000
#define GPIO_DIR (*(volatile uint32_t *)(GPIO_BASE + 0x00))
#define GPIO_OUT (*(volatile uint32_t *)(GPIO_BASE + 0x04))
#define GPIO_IN  (*(volatile uint32_t *)(GPIO_BASE + 0x08))

// Set GPIO pin 5 as output
GPIO_DIR |= (1 << 5);

// Set GPIO pin 5 HIGH
GPIO_OUT |= (1 << 5);
```

**Note:** The base address and register offsets in this example are conceptual. Actual addresses and offsets vary by MCU vendor and family. Always consult your specific MCU's datasheet and reference manual for the correct memory map.

**Why this matters:** Memory-mapped I/O is how you control hardware in C. Understanding it is essential for embedded programming.

### Polling vs Interrupts

**Polling:** CPU repeatedly checks if an event has occurred
- CPU wastes time checking
- Simple to implement
- Predictable timing
- High CPU usage

**Interrupts:** CPU is notified when an event occurs
- CPU can do other work until interrupt occurs
- More efficient
- Requires interrupt handling code
- Lower CPU usage

**Example:**
- **Polling:** Keep checking if button is pressed
- **Interrupt:** CPU notified when button is pressed

**Why this matters:** Interrupts are essential for efficient event handling. Understanding when to use polling vs interrupts is crucial for embedded system design.

### DMA (Direct Memory Access)

**DMA:** Hardware that transfers data without CPU intervention
- Transfers data between memory and peripherals
- Reduces CPU overhead
- Can transfer large blocks of data
- Configurable for various transfer modes

**DMA Registers:**
- **Control register:** Enable DMA, configure mode
- **Source address register:** Source of data
- **Destination address register:** Destination of data
- **Transfer count register:** Number of bytes to transfer
- **Status register:** Transfer complete flag

**Why this matters:** DMA is essential for high-speed data transfer (e.g., ADC sampling, SPI communication). Understanding DMA helps you optimize performance.

### Bare-Metal Programming

**Bare-Metal Programming:** Programming without an operating system
- Direct hardware access
- No OS abstraction
- Full control over hardware
- Requires understanding of hardware details
- Common in embedded systems

**Characteristics:**
- Direct register access
- Manual interrupt handling
- Manual memory management
- Real-time constraints
- Resource constraints

**Why this matters:** Most embedded systems use bare-metal programming. Understanding it is essential for embedded development.

### HAL (Hardware Abstraction Layer)

**HAL:** Layer of software that abstracts hardware details
- Provides consistent API across different hardware
- Hides register-level details
- Simplifies application code
- Portable across different MCUs (within same vendor or with abstraction)

**Note:** HAL APIs vary by vendor. This is a conceptual example—actual HAL functions and naming conventions differ between vendors (STM32 HAL, ESP-IDF, Arduino, etc.).

**Example:**
```c
// Without HAL (register-level)
GPIO_DIR |= (1 << 5);
GPIO_OUT |= (1 << 5);

// With HAL (example syntax varies by vendor)
HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, GPIO_PIN_SET);
```

**Why this matters:** HALs simplify development and improve portability. Understanding HALs helps you write portable code.

### BSP (Board Support Package)

**BSP:** Software that supports a specific board
- Includes drivers for board-specific components
- Includes board initialization code
- Includes pin configuration
- Specific to a particular board

**Why this matters:** BSPs provide board-specific support. Understanding BSPs helps you work with specific development boards.

### Drivers

**Driver:** Software that controls a specific peripheral or device
- Provides API for peripheral/device
- Hides hardware details
- May be part of HAL or BSP
- Can be vendor-provided or custom

**Types:**
- **Peripheral drivers:** GPIO, UART, SPI, I2C, etc.
- **Device drivers:** Sensors, displays, etc.

**Why this matters:** Drivers simplify peripheral and device access. Understanding drivers helps you integrate hardware components.

---

## Embedded Software Architecture

### Layered Architecture

```
┌─────────────────────────────────┐
│     Application Layer           │
│  (Your application code)        │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│     Application Logic           │
│  (Business logic, algorithms)   │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│        Drivers                  │
│  (Peripheral drivers, device    │
│   drivers)                      │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│        HAL/BSP                  │
│  (Hardware abstraction, board   │
│   support)                      │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│    Peripheral Registers         │
│  (Memory-mapped hardware)       │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│         Hardware                │
│  (MCU, peripherals, sensors)    │
└─────────────────────────────────┘
```

**Note:** This is a conceptual architecture. Actual implementations may have fewer or more layers depending on the system complexity and vendor conventions. Bare-metal systems may skip HAL/BSP layers entirely.

**Why this matters:** Understanding the layered architecture helps you organize your code and understand how different software layers interact with hardware.

---

## Embedded Development Workflow

### Build Process

```
1. Write Source Code
   ↓
2. Preprocess
   (Handle #include, #define, #ifdef)
   ↓
3. Compile
   (Convert C to assembly)
   ↓
4. Assemble
   (Convert assembly to machine code)
   ↓
5. Link
   (Combine object files, resolve symbols)
   ↓
6. Generate Firmware
   (Create final binary/hex file)
   ↓
7. Flash
   (Program firmware to MCU)
   ↓
8. Reset/Boot
   (MCU resets and starts execution)
   ↓
9. Execute
   (Firmware runs on MCU)
   ↓
10. Debug
    (Fix errors and optimize)
```

**Why this matters:** Understanding the development workflow helps you understand how your code becomes firmware and runs on the MCU.

---

## Exact Resources

### Resource 1: Microcontroller Basics
- **Provider:** Embedded.com
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Understand microcontroller fundamentals
- **URL:** https://www.embedded.com/

### Resource 2: ARM Architecture
- **Provider:** ARM Developer
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Understand ARM processor architecture
- **URL:** https://developer.arm.com/documentation/

### Resource 3: Memory-Mapped I/O
- **Provider:** Wikipedia
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Secondary reference
- **Purpose:** Understand memory-mapped I/O concepts
- **URL:** https://en.wikipedia.org/wiki/Memory-mapped_I/O

### Resource 4: Interrupts Guide
- **Provider:** Embedded.com
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Understand interrupt handling
- **URL:** https://www.embedded.com/interrupts/

### Resource 5: DMA Tutorial
- **Provider:** Embedded.com
- **Level:** Advanced
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Understand Direct Memory Access
- **URL:** https://www.embedded.com/dma/

---

## Study Order

Follow this exact sequence:

1. **Study what a microcontroller is**
2. **Understand MCU vs MPU**
3. **Study MCU architecture**
4. **Learn about CPU core**
5. **Study registers**
6. **Understand memory organization (Flash, SRAM, EEPROM)**
7. **Study memory maps**
8. **Learn about GPIO**
9. **Study timers and counters**
10. **Learn about PWM hardware**
11. **Study ADC hardware**
12. **Learn about DAC hardware**
13. **Study communication peripherals (UART, SPI, I2C)**
14. **Understand interrupt controller**
15. **Study clock system**
16. **Learn about watchdog timer**
17. **Understand reset and boot process**
18. **Study firmware and startup code**
19. **Learn about linker and memory layout**
20. **Understand peripheral registers and memory-mapped I/O**
21. **Study polling vs interrupts**
22. **Learn about DMA**
23. **Understand bare-metal programming**
24. **Study HAL, BSP, and drivers**
25. **Understand embedded software architecture**
26. **Study embedded development workflow**
27. **Complete all exercises**
28. **Complete the project**
29. **Take the knowledge test**
30. **Take the practical test**
31. **Review completion checklist**

---

## Exercises

### Exercise 1: Memory Map Exercise

**Objective:** Understand memory maps and address ranges.

**Tasks:**
1. Given a memory map with Flash at 0x00000000-0x0007FFFF (512KB) and SRAM at 0x3FFB0000-0x3FFBFFFF (256KB), calculate:
   - Size of Flash in bytes
   - Size of SRAM in bytes
   - Address of last byte in Flash
   - Address of last byte in SRAM

2. If a peripheral register is at address 0x40001000, is it in Flash, SRAM, or peripheral space?

3. If a variable is stored at address 0x3FFB1234, is it in Flash or SRAM?

**Expected Outcome:** You can read and understand memory maps.

### Exercise 2: Register Map Exercise

**Objective:** Understand register maps and bit manipulation.

**Tasks:**
1. Given a GPIO output register at address 0x40000004:
   - What is the address of the register?
   - If the register value is 0x00000010, which GPIO pin is HIGH?
   - What value would set GPIO pin 3 HIGH?
   - What value would clear GPIO pin 3?

2. Given a GPIO direction register at address 0x40000000:
   - What value would set GPIO pin 5 as output?
   - What value would set GPIO pin 5 as input?
   - What value would set GPIO pins 0-3 as outputs and pins 4-7 as inputs?

**Expected Outcome:** You can perform register-based calculations.

### Exercise 3: GPIO Register Exercise

**Objective:** Practice GPIO register manipulation.

**Tasks:**
1. Write C code to:
   - Set GPIO pin 2 as output
   - Set GPIO pin 2 HIGH
   - Wait 100ms
   - Set GPIO pin 2 LOW
   - Wait 100ms

2. Write C code to:
   - Set GPIO pin 5 as input with pull-up
   - Read GPIO pin 5
   - If pin is HIGH, set GPIO pin 6 HIGH
   - If pin is LOW, set GPIO pin 6 LOW

**Expected Outcome:** You can write register-based GPIO control code.

### Exercise 4: Timer Exercise

**Objective:** Understand timer configuration and operation.

**Tasks:**
1. Given a timer with 1MHz clock frequency:
   - What is the period of one clock cycle?
   - What prescaler value would give 100kHz timer clock?
   - What compare value would give 1ms interrupt interval with 100kHz timer clock?

2. Given a 16-bit timer with 10MHz clock:
   - What is the maximum count value?
   - What is the maximum time before overflow?
   - What prescaler value would give approximately 1ms maximum count?

**Expected Outcome:** You can calculate timer configurations.

### Exercise 5: Interrupt Exercise

**Objective:** Understand interrupt handling and priority.

**Tasks:**
1. Given two interrupts:
   - Interrupt A occurs every 1ms
   - Interrupt B occurs every 10ms
   - Which should have higher priority? Why?

2. Given an interrupt handler:
   - What should the handler do?
   - What should it avoid doing?
   - How long should it execute?

3. Explain the difference between:
   - Enabling an interrupt
   - Masking an interrupt
   - Clearing an interrupt flag

**Expected Outcome:** You understand interrupt handling concepts.

### Exercise 6: Polling vs Interrupt Exercise

**Objective:** Understand when to use polling vs interrupts.

**Tasks:**
1. For each scenario, choose polling or interrupts and explain why:
   - Reading a button press
   - Reading a temperature sensor every second
   - Handling UART incoming data
   - Monitoring a safety-critical signal
   - Generating PWM output

2. What are the advantages of polling?
3. What are the advantages of interrupts?
4. What are the disadvantages of polling?
5. What are the disadvantages of interrupts?

**Expected Outcome:** You can choose appropriate event handling methods.

### Exercise 7: DMA Reasoning Exercise

**Objective:** Understand when to use DMA.

**Tasks:**
1. For each scenario, determine if DMA is appropriate and explain why:
   - Transferring 1KB from ADC to memory
   - Transferring 1 byte from UART to memory
   - Transferring 100KB from memory to SPI
   - Reading a button press
   - Generating PWM output

2. What are the advantages of DMA?
3. What are the disadvantages of DMA?
4. When would you not use DMA?

**Expected Outcome:** You understand when DMA is appropriate.

### Exercise 8: Firmware Build Flow Exercise

**Objective:** Understand the firmware build process.

**Tasks:**
1. List the steps in the firmware build process in order.
2. What does the preprocessor do?
3. What does the compiler do?
4. What does the linker do?
5. What is a linker script?
6. What is the difference between .o files and .hex files?

**Expected Outcome:** You understand the firmware build process.

---

## Labs

There are no hardware labs in this phase. Labs begin in Phase 6 (ESP32).

---

## Debugging Tasks

There are no debugging tasks in this phase. Debugging exercises begin in later phases.

---

## Project

**Project: Conceptual MCU Simulator**

**Objective:** Create a simple program that simulates basic MCU architecture and register operations.

**Requirements:**
- Simulate a simple MCU with:
  - 4 general-purpose registers (R0-R3)
  - 8 GPIO pins
  - GPIO direction register
  - GPIO output register
  - GPIO input register
- Implement basic operations:
  - LOAD (load value into register)
  - STORE (store register to memory)
  - ADD (add registers)
  - SUB (subtract registers)
  - AND (bitwise AND registers)
  - OR (bitwise OR registers)
  - GPIO_SET (set GPIO output)
  - GPIO_GET (get GPIO input)
- Display MCU state after each operation
- Include documentation explaining each operation

**Suggested Implementation (Python or any language you know):**
```python
class MCUSimulator:
    def __init__(self):
        self.registers = {"R0": 0, "R1": 0, "R2": 0, "R3": 0}
        self.gpio_dir = 0x00      # 0=input, 1=output
        self.gpio_out = 0x00      # Output values
        self.gpio_in = 0x00       # Input values
    
    def load(self, reg, value):
        self.registers[reg] = value
    
    def store(self, reg, address):
        # Simplified: just store in a dictionary
        pass
    
    def add(self, dest, src):
        self.registers[dest] = self.registers[dest] + self.registers[src]
    
    def sub(self, dest, src):
        self.registers[dest] = self.registers[dest] - self.registers[src]
    
    def gpio_set_dir(self, pin, direction):
        if direction == "output":
            self.gpio_dir |= (1 << pin)
        else:
            self.gpio_dir &= ~(1 << pin)
    
    def gpio_set_output(self, pin, value):
        if value:
            self.gpio_out |= (1 << pin)
        else:
            self.gpio_out &= ~(1 << pin)
    
    def display_state(self):
        print("Registers:", self.registers)
        print("GPIO_DIR:", bin(self.gpio_dir))
        print("GPIO_OUT:", bin(self.gpio_out))
        print("GPIO_IN:", bin(self.gpio_in))

# Example usage
mcu = MCUSimulator()
mcu.load("R0", 0x10)
mcu.load("R1", 0x20)
mcu.add("R0", "R1")
mcu.gpio_set_dir(5, "output")
mcu.gpio_set_output(5, 1)
mcu.display_state()
```

**Extensions (optional):**
- Implement more instructions (MUL, DIV, SHIFT)
- Implement timer simulation
- Implement interrupt simulation
- Add simple program file format
- Implement memory

**Time Estimate:** 3-4 hours

**Deliverable:** Working MCU simulator with documentation.

---

## Common Mistakes

### Mistake 1: Confusing MCU and MPU
**Problem:** Treating microcontrollers like general-purpose computers
**Consequence:** Inefficient code, incorrect expectations
**Solution:** Understand the differences and design for MCU constraints

### Mistake 2: Ignoring Memory Constraints
**Problem:** Not considering limited memory
**Consequence:** Memory exhaustion, crashes
**Solution:** Always consider memory usage, use appropriate data types

### Mistake 3: Not Using volatile for Registers
**Problem:** Compiler optimizes away register access
**Consequence:** Code doesn't work as expected
**Solution:** Always use volatile for memory-mapped registers

### Mistake 4: Misunderstanding Interrupts
**Problem:** Treating interrupts like function calls
**Consequence:** Unpredictable behavior, crashes
**Solution:** Understand interrupt context, keep handlers short

### Mistake 5: Overusing Polling
**Problem:** Using polling when interrupts are appropriate
**Consequence:** Inefficient CPU usage, poor response time
**Solution:** Use interrupts for event-driven applications

### Mistake 6: Not Understanding Memory Layout
**Problem:** Not understanding where code and data are placed
**Consequence:** Memory corruption, crashes
**Solution:** Understand linker script and memory map

### Mistake 7: Ignoring Clock Configuration
**Problem:** Not configuring clocks correctly
**Consequence:** Peripherals don't work, incorrect timing
**Solution:** Always configure clocks for required peripherals

### Mistake 8: Not Considering Power Consumption
**Problem:** Not optimizing for low power
**Consequence:** Short battery life, overheating
**Solution:** Use sleep modes, clock gating, low-power modes

---

## Troubleshooting

### Firmware Not Running
**Problem:** Firmware doesn't execute on MCU
**Solutions:**
- Check firmware is correctly flashed
- Check reset vector is correct
- Check stack pointer is initialized
- Check startup code is correct
- Verify clock configuration

### Interrupts Not Working
**Problem:** Interrupts don't trigger
**Solutions:**
- Check interrupt is enabled
- Check peripheral is enabled
- Check interrupt flag is cleared
- Check interrupt priority
- Check global interrupt enable

### Peripherals Not Working
**Problem:** Peripheral doesn't respond
**Solutions:**
- Check peripheral clock is enabled
- Check peripheral is configured correctly
- Check registers are set correctly
- Check GPIO pins are configured for alternate function
- Verify hardware connections

### Memory Corruption
**Problem:** Data gets corrupted unexpectedly
**Solutions:**
- Check for stack overflow
- Check for buffer overflow
- Check for incorrect pointer usage
- Check for interrupt modifying shared data
- Use memory protection if available

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is the difference between MCU and MPU?
2. What are the main components of MCU architecture?
3. What is the difference between Flash and SRAM?
4. What is a memory map?
5. What is memory-mapped I/O?
6. What are GPIO registers used for?
7. What is a timer used for?
8. What is PWM used for?
9. What is an ADC used for?
10. What is the difference between UART, SPI, and I2C?
11. What is an interrupt controller?
12. What is the clock system?
13. What is a watchdog timer?
14. What happens during the boot process?
15. What is startup code?
16. What does the linker do?
17. What is the difference between polling and interrupts?
18. What is DMA used for?
19. What is bare-metal programming?
20. What is a HAL?
21. What is a BSP?
22. What is a driver?
23. What is the embedded software architecture?
24. What are the steps in the firmware build process?
25. Why is volatile important for register access?

**Passing Score:** 20/25 correct answers

---

## Practical Test

Complete these practical tasks:

1. **Memory Map Analysis:**
   - Given a memory map, identify where code, data, and peripherals are located
   - Calculate address ranges
   - Determine if a given address is in Flash, SRAM, or peripheral space

2. **Register Manipulation:**
   - Write C code to set GPIO pin 3 as output
   - Write C code to set GPIO pin 3 HIGH
   - Write C code to read GPIO pin 5
   - Write C code to set GPIO pins 0-3 as outputs

3. **Timer Configuration:**
   - Calculate the prescaler and compare value for a 1ms interrupt with a 10MHz clock
   - Calculate the maximum count for a 16-bit timer with 1MHz clock
   - Explain how to generate PWM with 50% duty cycle

4. **Interrupt Handling:**
   - Explain the steps to handle an interrupt
   - Explain what should and shouldn't be done in an interrupt handler
   - Explain interrupt priority

5. **Architecture Analysis:**
   - Explain the layered software architecture
   - Explain how data flows from application to hardware
   - Explain the role of HAL, BSP, and drivers

**Passing Criteria:** All tasks completed correctly with clear explanations demonstrating understanding.

---

## Completion Checklist

Before moving to Phase 6, verify you have:

- [ ] Understand MCU vs MPU
- [ ] Understand MCU architecture
- [ ] Understand CPU core and registers
- [ ] Understand memory organization (Flash, SRAM, EEPROM)
- [ ] Can read and understand memory maps
- [ ] Understand GPIO and GPIO registers
- [ ] Understand timers and counters
- [ ] Understand PWM hardware
- [ ] Understand ADC hardware
- [ ] Understand DAC hardware
- [ ] Understand communication peripherals (UART, SPI, I2C)
- [ ] Understand interrupt controller and interrupt handling
- [ ] Understand clock system
- [ ] Understand watchdog timer
- [ ] Understand reset and boot process
- [ ] Understand firmware and startup code
- [ ] Understand linker and memory layout
- [ ] Understand peripheral registers and memory-mapped I/O
- [ ] Understand polling vs interrupts
- [ ] Understand DMA
- [ ] Understand bare-metal programming
- [ ] Understand HAL, BSP, and drivers
- [ ] Understand embedded software architecture
- [ ] Understand embedded development workflow
- [ ] Completed all exercises
- [ ] Completed the MCU simulator project
- [ ] Passed the knowledge test (20/25 correct)
- [ ] Passed the practical test
- [ ] Understand how software interacts with hardware

---

## Do Not Continue Until...

**Do not start Phase 6 until:**

1. You have passed the knowledge test (20/25 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You have completed all exercises
5. You have completed the MCU simulator project
6. You understand memory-mapped I/O
7. You understand the embedded development workflow
8. You understand the layered software architecture

**Microcontroller architecture is the bridge between electronics and actual programming. Understanding MCU concepts before diving into ESP32 will make ESP32 programming much easier. Take the time to master these concepts.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 6 — ESP32**

Phase 6 will teach you ESP32-specific development using both Arduino-ESP32 and ESP-IDF, applying the MCU architecture concepts you learned here to a real microcontroller platform.

---

**Microcontroller architecture concepts are universal. Even though Phase 6 focuses on ESP32, the concepts you learned here apply to any microcontroller platform. This foundation will serve you throughout your embedded systems career.**
