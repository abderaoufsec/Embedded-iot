# Phase 1 — Computer Fundamentals

> **Goal:** Understand how computers work at the bit level, including binary, hexadecimal, memory, CPU basics, and registers—all essential foundations for embedded systems.
>
> **Prerequisite:** Phase 0 — Orientation
>
> **Outcome:** You can work with binary and hexadecimal numbers, understand computer memory and addressing, and grasp basic CPU concepts needed for embedded programming.

---

## What You Will Learn

By completing this phase, you will understand:

- Binary, decimal, and hexadecimal number systems
- How computers represent and store data
- Bits, bytes, and word sizes
- Signed and unsigned number representation
- Two's complement for negative numbers
- Bitwise operations (AND, OR, XOR, NOT, shifts)
- Boolean logic and logic gates
- CPU architecture basics (registers, ALU, control unit)
- Memory organization (RAM, ROM, Flash)
- Stack and heap memory
- Memory addressing
- Pointers as addresses (conceptual preparation)
- Endianness (big-endian vs little-endian)
- Memory-mapped I/O concepts
- How CPUs execute instructions
- Clock frequency and timing
- Interrupts vs polling
- Why these concepts matter for microcontrollers

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phase 0 — Orientation
- ✅ Basic arithmetic skills (addition, subtraction, multiplication, division)
- ✅ Ability to follow logical instructions
- ✅ Paper and pencil for exercises

**No programming experience is required.**

---

## Learning Outcomes

After completing this phase, you will be able to:

- Convert between binary, decimal, and hexadecimal
- Perform binary arithmetic
- Understand how computers store positive and negative numbers
- Perform bitwise operations on binary numbers
- Understand Boolean logic and truth tables
- Explain basic CPU architecture
- Understand how memory is organized and addressed
- Differentiate between stack and heap memory
- Explain what a register is and why it matters
- Understand the concept of memory-mapped I/O
- Explain how CPUs execute instructions
- Understand the difference between interrupts and polling
- Explain why clock frequency matters
- Apply these concepts to embedded systems

---

## Concepts

### Binary, Decimal, and Hexadecimal

**Decimal (Base 10):** The number system we use in daily life
- Digits: 0-9
- Position: Each digit represents a power of 10
- Example: 123 = 1×10² + 2×10¹ + 3×10⁰

**Binary (Base 2):** The number system computers use
- Digits: 0-1
- Position: Each digit represents a power of 2
- Example: 1010 = 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 0 + 2 + 0 = 10 decimal

**Hexadecimal (Base 16):** A compact way to represent binary
- Digits: 0-9, A-F (where A=10, B=11, C=12, D=13, E=14, F=15)
- Position: Each digit represents a power of 16
- Example: 0x1A = 1×16¹ + 10×16⁰ = 16 + 10 = 26 decimal

**Why hexadecimal matters:** Each hex digit represents exactly 4 bits, making it perfect for representing binary data compactly.

### Bits and Bytes

**Bit:** A single binary digit (0 or 1)
- The smallest unit of data in a computer
- Can represent two states (on/off, true/false)

**Byte:** A group of 8 bits
- Can represent 256 different values (2⁸ = 256)
- Typically the smallest addressable unit in memory
- Range: 0-255 (unsigned) or -128 to +127 (signed)

**Word:** A group of bytes that a CPU processes as a unit
- 16-bit, 32-bit, or 64-bit depending on the CPU
- ESP32 is a 32-bit processor

### Number Representation

**Unsigned Integers:** Only positive numbers
- 8-bit: 0 to 255
- 16-bit: 0 to 65,535
- 32-bit: 0 to 4,294,967,295

**Signed Integers:** Positive and negative numbers
- Uses two's complement representation
- 8-bit: -128 to +127
- 16-bit: -32,768 to +32,767
- 32-bit: -2,147,483,648 to +2,147,483,647

**Two's Complement:** How computers represent negative numbers
- Invert all bits
- Add 1
- Example: -5 in 8-bit two's complement:
  - +5 = 00000101
  - Invert: 11111010
  - Add 1: 11111011 = 251 (unsigned) or -5 (signed)

### Bitwise Operations

**AND (&):** Output 1 only if both inputs are 1
```
1100 AND 1010 = 1000
```

**OR (|):** Output 1 if either input is 1
```
1100 OR 1010 = 1110
```

**XOR (^):** Output 1 if inputs are different
```
1100 XOR 1010 = 0110
```

**NOT (~):** Invert all bits
```
NOT 1100 = 0011
```

**Left Shift (<<):** Shift bits left, multiply by 2
```
1100 << 1 = 11000 (multiply by 2)
```

**Right Shift (>>):** Shift bits right, divide by 2
```
1100 >> 1 = 0110 (divide by 2)
```

**Why bitwise operations matter:** They're essential for embedded systems for manipulating individual bits in registers, controlling GPIO pins, and handling flags.

### Boolean Logic and Logic Gates

**Boolean Logic:** Logic based on true/false values
- Named after George Boole
- Foundation of digital electronics

**Logic Gates:** Electronic circuits that implement Boolean logic
- **AND gate:** Output true only if all inputs are true
- **OR gate:** Output true if any input is true
- **NOT gate:** Output is opposite of input
- **NAND gate:** NOT AND
- **NOR gate:** NOT OR
- **XOR gate:** Output true if inputs are different

**Truth Tables:** Show all possible inputs and outputs
- Essential for understanding digital circuits
- Used to design and debug digital logic

### CPU Architecture Basics

**CPU (Central Processing Unit):** The "brain" of a computer
- Executes instructions
- Performs calculations
- Coordinates all computer operations

**Basic CPU Components:**
- **Control Unit:** Decodes instructions and controls data flow
- **ALU (Arithmetic Logic Unit):** Performs mathematical and logical operations
- **Registers:** Fast internal storage for data and addresses
- **Clock:** Coordinates timing of operations

### Registers

**Registers:** Small, fast storage locations inside the CPU
- Hold data currently being processed
- Much faster than main memory
- Used for temporary storage, addresses, flags
- Each register has a specific purpose

**Common Register Types:**
- **General-purpose registers:** Hold data for calculations
- **Program counter:** Holds address of next instruction
- **Stack pointer:** Points to top of stack
- **Status register:** Holds flags (zero, carry, overflow, etc.)

**Why registers matter:** Understanding registers is crucial for embedded programming because you'll often read and write directly to hardware registers to control peripherals.

### Memory Organization

**RAM (Random Access Memory):** Volatile read/write memory
- Loses data when power is removed
- Used for variables, stack, heap
- Fast read/write access
- Limited size in embedded systems

**ROM (Read-Only Memory):** Non-volatile memory
- Retains data when power is removed
- Contains firmware/boot code
- Cannot be modified during normal operation

**Flash Memory:** A type of EEPROM that can be electrically erased and reprogrammed
- Non-volatile
- Used for firmware storage in embedded systems
- Can be updated in the field
- Limited number of write cycles

### Stack and Heap

**Stack:** Memory region for function calls and local variables
- Grows and shrinks automatically
- Last-in, first-out (LIFO) structure
- Used for function call context
- Limited size, can cause stack overflow

**Heap:** Memory region for dynamic memory allocation
- Manual allocation and deallocation
- Used when memory size is unknown at compile time
- Can cause memory leaks and fragmentation
- Often avoided in embedded systems

### Memory Addressing

**Address:** A unique number that identifies a memory location
- Each byte in memory has a unique address
- CPU uses addresses to access specific memory locations
- Addresses are typically represented in hexadecimal

**Memory Map:** How addresses are organized
- Different memory regions have different address ranges
- Memory-mapped I/O uses addresses to access peripherals
- Understanding memory maps is essential for embedded programming

### Pointers as Addresses (Conceptual)

**Pointer:** A variable that holds a memory address
- Points to data stored at that address
- Allows indirect access to memory
- Essential for efficient data manipulation

**Conceptual example:**
```
Memory address 0x1000 holds value 42
A pointer with value 0x1000 "points to" the data 42
```

**Why pointers matter:** Pointers are essential for embedded systems because they allow you to access hardware registers, pass large data structures efficiently, and implement dynamic data structures.

### Endianness

**Endianness:** The order in which bytes are stored in memory

**Big-Endian:** Most significant byte first
- Address 0x1000: high byte
- Address 0x1001: low byte

**Little-Endian:** Least significant byte first
- Address 0x1000: low byte
- Address 0x1001: high byte

**Example:** The 16-bit value 0x1234
- Big-endian: 0x12 at 0x1000, 0x34 at 0x1001
- Little-endian: 0x34 at 0x1000, 0x12 at 0x1001

**Why endianness matters:** Different processors use different endianness, which matters when communicating between systems or interpreting binary data.

### Memory-Mapped I/O

**Memory-Mapped I/O:** Hardware peripherals are accessed as if they were memory locations
- Each peripheral register has a specific memory address
- Reading/writing to that address controls the peripheral
- Simplifies hardware access from software

**Example:**
```
Address 0x40000000: GPIO output register
Writing 0x01 to this address turns on GPIO pin 0
```

**Why memory-mapped I/O matters:** This is how embedded systems control hardware—you read and write to specific memory addresses to control peripherals.

### Instruction Execution

**Instruction Cycle:** How a CPU executes a program
1. **Fetch:** Read instruction from memory
2. **Decode:** Determine what the instruction does
3. **Execute:** Perform the operation
4. **Repeat:** Move to next instruction

**Clock:** Coordinates the timing of all operations
- Each clock cycle can perform one basic operation
- Higher clock frequency = faster execution
- Measured in Hz (cycles per second)

**Clock Frequency:** How many clock cycles per second
- 1 MHz = 1 million cycles per second
- 240 MHz = 240 million cycles per second (ESP32 typical)

### Interrupts vs Polling

**Polling:** CPU repeatedly checks if an event has occurred
- CPU wastes time checking
- Simple to implement
- Predictable timing

**Interrupts:** CPU is notified when an event occurs
- CPU can do other work until interrupt occurs
- More efficient
- Requires interrupt handling code

**Example:**
- **Polling:** Keep checking if button is pressed
- **Interrupt:** CPU notified when button is pressed

**Why this matters:** Interrupts are essential in embedded systems for handling events efficiently without wasting CPU time.

---

## Exact Resources

### Resource 1: Binary and Hexadecimal
- **Provider:** Khan Academy
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Learn binary and hexadecimal number systems
- **URL:** https://www.khanacademy.org/math/algebra-home/alg-intro-to-algebra

### Resource 2: Two's Complement
- **Provider:** Wikipedia
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Understand how computers represent negative numbers
- **URL:** https://en.wikipedia.org/wiki/Two%27s_complement

### Resource 3: Logic Gates
- **Provider:** Electronics Tutorials
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Learn about logic gates and Boolean algebra
- **URL:** https://www.electronics-tutorials.ws/logic/

### Resource 4: CPU Architecture Basics
- **Provider:** CS50 (Harvard University)
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Understand basic CPU architecture
- **URL:** https://www.youtube.com/watch?v=cN_tuB0V-AY

### Resource 5: Memory and Storage
- **Provider:** Crash Course Computer Science
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Learn about memory, RAM, and storage
- **URL:** https://www.youtube.com/watch?v=fJNDjGWV9Qc

---

## Study Order

Follow this exact sequence:

1. **Study number systems** (binary, decimal, hexadecimal)
2. **Practice number conversions** (between bases)
3. **Learn bits and bytes**
4. **Study signed/unsigned representation**
5. **Learn two's complement**
6. **Practice bitwise operations**
7. **Study Boolean logic and truth tables**
8. **Learn about logic gates**
9. **Study CPU architecture basics**
10. **Learn about registers**
11. **Study memory organization (RAM, ROM, Flash)**
12. **Learn about stack and heap**
13. **Study memory addressing**
14. **Understand pointers conceptually**
15. **Learn about endianness**
16. **Study memory-mapped I/O**
17. **Learn about instruction execution**
18. **Study clock frequency**
19. **Learn about interrupts vs polling**
20. **Complete all exercises**
21. **Take the knowledge test**
22. **Take the practical test**
23. **Review completion checklist**

---

## Exercises

### Exercise 1: Number System Conversions

**Objective:** Practice converting between binary, decimal, and hexadecimal.

**Tasks:**
1. Convert the following decimal numbers to binary:
   - 10
   - 42
   - 127
   - 255

2. Convert the following binary numbers to decimal:
   - 1010
   - 11111111
   - 10000000
   - 1100101

3. Convert the following decimal numbers to hexadecimal:
   - 16
   - 255
   - 42
   - 127

4. Convert the following hexadecimal numbers to decimal:
   - 0x10
   - 0xFF
   - 0x2A
   - 0x7F

5. Convert the following binary numbers to hexadecimal:
   - 10101010
   - 11110000
   - 00001111
   - 10000000

**Expected Outcome:** You can confidently convert between number systems.

### Exercise 2: Two's Complement

**Objective:** Understand how negative numbers are represented.

**Tasks:**
1. Represent the following decimal numbers as 8-bit two's complement:
   - -1
   - -5
   - -128
   - -42

2. What decimal number does each 8-bit two's complement represent?
   - 11111111
   - 11111110
   - 10000000
   - 11010110

3. What is the range of an 8-bit signed integer?
4. What is the range of a 16-bit signed integer?

**Expected Outcome:** You understand two's complement representation.

### Exercise 3: Bitwise Operations

**Objective:** Practice bitwise operations on binary numbers.

**Tasks:**
1. Calculate the result of these operations:
   - 1100 AND 1010
   - 1100 OR 1010
   - 1100 XOR 1010
   - NOT 1100
   - 1100 << 1
   - 1100 >> 1

2. What is the result of:
   - 0x3A & 0x0F
   - 0x3A | 0x0F
   - 0x3A ^ 0x0F
   - ~0x3A (assume 8-bit)
   - 0x3A << 2
   - 0x3A >> 2

3. How would you set bit 3 (counting from 0) to 1 in a byte?
4. How would you clear bit 3 to 0 in a byte?
5. How would you toggle bit 3 in a byte?

**Expected Outcome:** You can perform bitwise operations and understand bit manipulation.

### Exercise 4: Boolean Logic

**Objective:** Practice Boolean logic and truth tables.

**Tasks:**
1. Create truth tables for:
   - AND gate
   - OR gate
   - NOT gate
   - XOR gate

2. Evaluate these Boolean expressions:
   - A AND B (where A=1, B=0)
   - A OR B (where A=0, B=1)
   - NOT A (where A=1)
   - A XOR B (where A=1, B=1)

3. What is the output of this circuit:
   - Input A goes to an AND gate
   - Input B goes to a NOT gate, then to the same AND gate
   - What is the output when A=1, B=1?

**Expected Outcome:** You understand Boolean logic and truth tables.

### Exercise 5: Memory Addressing

**Objective:** Understand memory addresses and data access.

**Tasks:**
1. If a byte at address 0x1000 contains the value 0x42, what do you read when you access address 0x1000?

2. If a 16-bit value 0x1234 is stored at address 0x1000 in little-endian format, what values are at addresses 0x1000 and 0x1001?

3. What is the address of the third byte in a block of memory starting at address 0x2000?

4. If a CPU is 32-bit, what is the addressable memory space (assuming byte-addressable)?

**Expected Outcome:** You understand memory addressing and endianness.

### Exercise 6: Register Operations

**Objective:** Understand register-style operations.

**Tasks:**
1. If register R0 contains 0x10 and register R1 contains 0x20, what is the result of:
   - R0 = R0 + R1
   - R2 = R0 AND R1
   - R0 = R0 << 2

2. If the status register has a zero flag (Z) set when the result of an operation is zero, what will the Z flag be after:
   - 0x10 - 0x10
   - 0x10 - 0x20

3. If the program counter points to address 0x1000 and the instruction at that address is 3 bytes long, what will the program counter be after execution?

**Expected Outcome:** You understand register operations and CPU concepts.

---

## Labs

There are no hardware labs in this phase. Labs begin in Phase 4 (Electronics).

---

## Debugging Tasks

There are no debugging tasks in this phase. Debugging exercises begin in later phases.

---

## Project

**Project: Register Simulator**

**Objective:** Create a simple program that simulates basic CPU register operations.

**Requirements:**
- Simulate 4 general-purpose registers (R0, R1, R2, R3)
- Implement basic operations: ADD, SUB, AND, OR, XOR, NOT
- Implement shift operations: SHL (shift left), SHR (shift right)
- Display register values after each operation
- Include a simple instruction format (e.g., "ADD R0 R1")

**Suggested Implementation (Python or any language you know):**
```python
class RegisterSimulator:
    def __init__(self):
        self.registers = {"R0": 0, "R1": 0, "R2": 0, "R3": 0}
    
    def add(self, dest, src):
        self.registers[dest] = self.registers[dest] + self.registers[src]
    
    def sub(self, dest, src):
        self.registers[dest] = self.registers[dest] - self.registers[src]
    
    def and_op(self, dest, src):
        self.registers[dest] = self.registers[dest] & self.registers[src]
    
    def or_op(self, dest, src):
        self.registers[dest] = self.registers[dest] | self.registers[src]
    
    def xor(self, dest, src):
        self.registers[dest] = self.registers[dest] ^ self.registers[src]
    
    def not_op(self, reg):
        self.registers[reg] = ~self.registers[reg] & 0xFF  # 8-bit
    
    def shl(self, reg, amount):
        self.registers[reg] = (self.registers[reg] << amount) & 0xFF
    
    def shr(self, reg, amount):
        self.registers[reg] = self.registers[reg] >> amount
    
    def display(self):
        print("Registers:", self.registers)

# Example usage
sim = RegisterSimulator()
sim.registers["R0"] = 0x10
sim.registers["R1"] = 0x20
sim.add("R0", "R1")
sim.display()
```

**Extensions (optional):**
- Implement immediate values (e.g., "ADD R0 5")
- Implement MOV instruction
- Implement flags (zero, carry, overflow)
- Implement conditional jumps

**Time Estimate:** 1-2 hours

**Deliverable:** Working register simulator with documentation.

---

## Common Mistakes

### Mistake 1: Confusing Binary and Hexadecimal
**Problem:** Mixing up binary and hexadecimal representations
**Consequence:** Errors in data interpretation
**Solution:** Always be clear about which base you're working in; use prefixes (0b for binary, 0x for hex)

### Mistake 2: Two's Complement Errors
**Problem:** Incorrectly calculating two's complement
**Consequence:** Wrong negative number representation
**Solution:** Follow the two's complement algorithm carefully: invert bits, then add 1

### Mistake 3: Ignoring Word Size
**Problem:** Not considering the bit width (8-bit, 16-bit, 32-bit)
**Consequence:** Overflow and incorrect results
**Solution:** Always be aware of the word size you're working with

### Mistake 4: Endianness Confusion
**Problem:** Assuming big-endian when system is little-endian (or vice versa)
**Consequence:** Incorrect data interpretation
**Solution:** Always check the endianness of the system you're working with

### Mistake 5: Confusing Stack and Heap
**Problem:** Not understanding the difference between stack and heap
**Consequence:** Memory management errors
**Solution:** Stack is automatic (function calls), heap is manual (dynamic allocation)

---

## Troubleshooting

### Conversion Errors
**Problem:** Getting wrong results when converting between number systems
**Solutions:**
- Double-check your calculation
- Verify you're using the correct base
- Use an online converter to verify your results
- Practice with simple numbers first

### Bitwise Operation Errors
**Problem:** Incorrect results from bitwise operations
**Solutions:**
- Write out the binary representation
- Perform the operation manually bit by bit
- Verify with a calculator or program
- Remember that NOT operation inverts all bits

### Memory Addressing Confusion
**Problem:** Not understanding how addresses work
**Solutions:**
- Think of memory as a series of numbered boxes
- Each box has a unique address
- Each box holds one byte
- Addresses start at 0 and increase

### Endianness Issues
**Problem:** Confusion about byte order
**Solutions:**
- Remember: little-endian = least significant byte first (lowest address)
- Big-endian = most significant byte first (lowest address)
- Draw out the bytes to visualize

---

## Knowledge Test

Answer these questions without looking at the materials:

1. Convert decimal 42 to binary.
2. Convert binary 101010 to decimal.
3. Convert decimal 255 to hexadecimal.
4. Convert hexadecimal 0x2A to decimal.
5. What is two's complement used for?
6. What is the result of 1100 AND 1010?
7. What is the result of 1100 OR 1010?
8. What is the result of 1100 XOR 1010?
9. What is the result of NOT 1100?
10. What is the result of 1100 << 1?
11. What is the result of 1100 >> 1?
12. What is a logic gate?
13. What is the difference between AND and OR gates?
14. What is a CPU register?
15. What is the difference between RAM and ROM?
16. What is the stack used for?
17. What is the heap used for?
18. What is a memory address?
19. What is endianness?
20. What is memory-mapped I/O?
21. What is the difference between interrupts and polling?
22. What is clock frequency?
23. Why are bitwise operations important in embedded systems?
24. What is the range of an 8-bit unsigned integer?
25. What is the range of an 8-bit signed integer?

**Passing Score:** 20/25 correct answers

---

## Practical Test

Complete these practical tasks:

1. **Number Conversions:**
   - Convert your age to binary
   - Convert your age to hexadecimal
   - Convert binary 11001100 to decimal
   - Convert hexadecimal 0x1A to binary

2. **Bitwise Operations:**
   - Calculate: 0x3A & 0x0F
   - Calculate: 0x3A | 0x0F
   - Calculate: 0x3A ^ 0x0F
   - Calculate: 0x3A << 2
   - Calculate: 0x3A >> 2

3. **Two's Complement:**
   - Represent -10 as 8-bit two's complement
   - What decimal value does 11111100 represent in 8-bit two's complement?

4. **Boolean Logic:**
   - Create a truth table for an AND gate with 2 inputs
   - What is the output of (A AND B) OR C when A=1, B=0, C=1?

5. **Memory Addressing:**
   - If address 0x1000 contains 0x42 and address 0x1001 contains 0x43, what 16-bit value is stored at 0x1000 in little-endian format?
   - What is the 16-bit value in big-endian format?

6. **Register Operations:**
   - If R0=0x10 and R1=0x20, what is the result of R0 = R0 + R1?
   - What is the result of R0 = R0 AND R1?
   - What is the result of R0 = R0 << 1?

**Passing Criteria:** Complete all tasks with correct results and show your work.

---

## Completion Checklist

Before moving to Phase 2, verify you have:

- [ ] Can convert between binary, decimal, and hexadecimal
- [ ] Understand signed and unsigned number representation
- [ ] Can perform bitwise operations correctly
- [ ] Understand two's complement
- [ ] Can create truth tables for basic logic gates
- [ ] Understand basic CPU architecture
- [ ] Know what registers are and why they matter
- [ ] Understand the difference between RAM, ROM, and Flash
- [ ] Can explain stack vs heap
- [ ] Understand memory addressing
- [ ] Understand pointers conceptually
- [ ] Know what endianness is
- [ ] Understand memory-mapped I/O
- [ ] Can explain the instruction execution cycle
- [ ] Understand clock frequency
- [ ] Can explain interrupts vs polling
- [ ] Completed all exercises
- [ ] Completed the register simulator project
- [ ] Passed the knowledge test (20/25 correct)
- [ ] Passed the practical test
- [ ] Understand why these concepts matter for embedded systems

---

## Do Not Continue Until...

**Do not start Phase 2 until:**

1. You have passed the knowledge test (20/25 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can confidently convert between number systems
5. You understand why these concepts matter for embedded systems
6. You have completed the register simulator project

**These computer fundamentals are essential for understanding C programming, electronics, and microcontrollers. Don't rush through them.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 2 — C Programming**

Phase 2 will teach you C programming specifically for embedded systems, building on the computer fundamentals you learned here. You'll learn about pointers, memory management, bitwise operations, and how C maps to hardware.

---

**Computer fundamentals may seem abstract, but they are the foundation for everything that follows. Take the time to master these concepts—you'll use them throughout embedded systems programming.**
