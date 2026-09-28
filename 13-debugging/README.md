# Phase 13 — Debugging

> **Goal:** Develop systematic debugging skills for embedded systems, covering software, hardware, and integration issues.
>
> **Prerequisite:** Phase 12 — Raspberry Pi
>
> **Outcome:** You can systematically diagnose and fix embedded system issues using appropriate tools and methodologies.

---

## What You Will Learn

By completing this phase, you will understand:

- **Debugging Mindset:** Reproduce → Isolate → Measure → Hypothesize → Test → Fix → Verify
- **Software Errors:** Compile errors, linker errors, runtime errors, logic errors
- **Hardware Failures:** GPIO issues, communication failures, power problems
- **Intermittent Issues:** Timing bugs, race conditions, memory corruption
- **System Issues:** Stack overflow, heap problems, watchdog resets, brownouts
- **Debugging Tools:** GDB, breakpoints, watchpoints, backtrace, registers
- **Hardware Tools:** Logic analyzer, oscilloscope, multimeter
- **Software Techniques:** Serial logging, assertions, printf debugging
- **Fault Isolation:** Binary search debugging, minimal reproduction
- **Logging Strategy:** Structured logging, log levels, log analysis
- **Debugging Decision Trees:** Systematic troubleshooting approaches

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phases 0-12
- ✅ Understanding of C programming (Phase 2)
- ✅ Understanding of microcontrollers (Phase 5)
- ✅ Understanding of ESP32 (Phase 6)
- ✅ Understanding of Linux (Phase 11)
- ✅ Understanding of Raspberry Pi (Phase 12)
- ✅ Experience with embedded development
- ✅ Basic electronics knowledge (Phase 4)

**Required Hardware:**
- ESP32 development board
- Raspberry Pi (from Phase 12)
- Logic analyzer (optional but recommended)
- Oscilloscope (optional but recommended)
- Multimeter
- Breadboard and components
- USB-TTL adapter

**Required Software:**
- GDB debugger
- Serial terminal software
- Logic analyzer software (if hardware available)
- Arduino IDE or ESP-IDF
- PlatformIO (optional)

---

## Learning Outcomes

After completing this phase, you will be able to:

- Apply systematic debugging methodology
- Diagnose compile and linker errors
- Debug runtime errors and logic errors
- Identify and fix memory corruption
- Debug timing issues and race conditions
- Use GDB for embedded debugging
- Use hardware tools (logic analyzer, oscilloscope, multimeter)
- Implement effective logging strategies
- Perform fault isolation using binary search
- Create minimal reproductions of issues
- Debug communication failures
- Diagnose power-related issues
- Debug GPIO and peripheral issues

---

## Why This Matters

**Debugging is Engineering:**
- Debugging is not trial-and-error
- Systematic approach saves time
- Understanding root cause prevents recurrence
- Documentation aids future debugging

**Embedded Challenges:**
- Limited visibility (no printf on bare metal)
- Real-time constraints
- Hardware interactions
- Concurrency issues
- Memory constraints

**Debugging Mindset:**
- Reproduce the issue reliably
- Isolate the problem area
- Measure relevant data
- Form hypothesis
- Test hypothesis
- Implement fix
- Verify fix works

---

## Core Concepts

### Debugging Methodology

**Systematic Approach:**
1. **Reproduce:** Make the issue happen consistently
2. **Isolate:** Narrow down the problem area
3. **Measure:** Collect relevant data
4. **Hypothesize:** Form theory of root cause
5. **Test:** Validate hypothesis
6. **Fix:** Implement solution
7. **Verify:** Confirm fix works

**Reproduce:**
- Consistent reproduction is critical
- Document steps to reproduce
- Identify conditions that trigger issue
- Eliminate randomness

**Isolate:**
- Binary search debugging
- Remove non-essential code
- Test components individually
- Minimize reproduction case

**Measure:**
- Collect data without changing system
- Use appropriate tools
- Document measurements
- Compare to expected values

**Hypothesize:**
- Based on measurements
- Specific and testable
- Consider multiple hypotheses
- Rank by likelihood

**Test:**
- Design experiment to validate
- Change one variable at a time
- Document results
- Accept or reject hypothesis

**Fix:**
- Address root cause, not symptoms
- Implement minimal change
- Consider side effects
- Add regression tests

**Verify:**
- Confirm fix resolves issue
- Test in realistic conditions
- Ensure no new issues introduced
- Document fix

---

### Software Errors

**Compile Errors:**
- Syntax errors
- Type mismatches
- Missing includes
- Undefined symbols
- Usually caught by compiler

**Linker Errors:**
- Undefined references
- Multiple definitions
- Library missing
- Wrong architecture
- Usually caught by linker

**Runtime Errors:**
- Segmentation faults
- Bus errors
- Illegal instructions
- Alignment errors
- Occur during execution

**Logic Errors:**
- Incorrect algorithm
- Wrong condition
- Off-by-one errors
- State machine errors
- Program runs but produces wrong results

---

### Hardware Failures

**GPIO Issues:**
- Wrong pin configured
- Pin mode incorrect
- Pull-up/pull-down wrong
- Pin damaged
- Electrical issues

**Communication Failures:**
- Wrong baud rate
- Wiring errors
- Timing issues
- Electrical noise
- Protocol errors

**Power Problems:**
- Insufficient voltage
- Voltage drops under load
- Brownouts
- Current limits exceeded
- Power supply failure

---

### Intermittent Issues

**Timing Bugs:**
- Race conditions
- Incorrect delays
- Clock drift
- Interrupt timing
- Peripheral timing

**Race Conditions:**
- Concurrent access to shared data
- Non-atomic operations
- Interrupt conflicts
- Priority inversion
- Deadlocks

**Memory Corruption:**
- Buffer overflows
- Stack overflow
- Heap corruption
- Use-after-free
- Double-free

**Stack Overflow:**
- Recursion too deep
- Large local variables
- Too many nested calls
- Stack size too small
- Symptoms: crashes, random behavior

**Heap Problems:**
- Memory leaks
- Fragmentation
- Allocation failures
- Use-after-free
- Double-free

---

### System Issues

**Watchdog Resets:**
- Code takes too long
- Infinite loops
- Interrupts disabled too long
- Deadlocks
- Insufficient watchdog timeout

**Brownouts:**
- Voltage drops below threshold
- High current draw
- Insufficient power supply
- Weak power connections
- Long power traces

**GPIO Mistakes:**
- Wrong direction
- Floating inputs
- No current limiting
- Exceeding current limits
- 5V on 3.3V pins

**Sensor Errors:**
- Wrong address
- Wrong protocol
- Timing violations
- Electrical noise
- Sensor malfunction

**Power Problems:**
- Insufficient current
- Voltage drops
- Poor connections
- Wrong voltage
- Power supply issues

**EMI/Noise Symptoms:**
- Random resets
- Communication errors
- ADC noise
- Glitches
- Timing errors

---

### Debugging Tools

**GDB (GNU Debugger):**
- Breakpoints
- Watchpoints
- Stepping
- Backtrace
- Register inspection
- Memory inspection
- Variable inspection

**Serial Logging:**
- Print statements
- Structured logging
- Log levels
- Timestamps
- Non-blocking writes

**Assertions:**
- Runtime checks
- Debug-only code
- Precondition verification
- Postcondition verification
- Invariant checking

**Logic Analyzer:**
- Digital signal capture
- Protocol decoding
- Timing analysis
- Trigger conditions
- Multi-channel capture

**Oscilloscope:**
- Analog signal capture
- Voltage measurement
- Timing measurement
- Signal integrity
- Noise analysis

**Multimeter:**
- Voltage measurement
- Current measurement
- Resistance measurement
- Continuity testing
- Component testing

**Wireshark:**
- Network packet capture
- Protocol analysis
- Traffic inspection
- Debug network issues

---

### GDB for Embedded

**Breakpoints:**
- Stop execution at specific location
- `break main`
- `break function_name`
- `break file.c:line`

**Watchpoints:**
- Stop when variable changes
- `watch variable_name`
- Stop on read or write

**Stepping:**
- `next`: Execute next line (step over functions)
- `step`: Execute next line (step into functions)
- `continue`: Continue execution
- `finish`: Execute until current function returns

**Backtrace:**
- `backtrace` or `bt`: Show call stack
- Identify where crash occurred
- Trace execution path

**Registers:**
- `info registers`: Show CPU registers
- `info registers r0`: Show specific register
- Useful for low-level debugging

**Memory Inspection:**
- `x/10x address`: Examine memory
- `x/10s address`: Examine as strings
- Check for corruption

**Remote Debugging:**
- GDB server on target
- GDB client on host
- Network debugging
- JTAG/SWD debugging

---

### Logging Strategy

**Log Levels:**
- ERROR: Critical errors
- WARNING: Non-critical issues
- INFO: Informational messages
- DEBUG: Detailed debugging info
- TRACE: Very detailed tracing

**Structured Logging:**
- Consistent format
- Timestamps
- Component/module identifiers
- Context information
- Machine-readable when possible

**Log Analysis:**
- Search for errors
- Correlate events
- Identify patterns
- Root cause analysis

**Performance Impact:**
- Logging affects timing
- Disable in production builds
- Use conditional compilation
- Buffer logging when needed

---

### Fault Isolation

**Binary Search Debugging:**
- Divide code in half
- Test which half contains bug
- Repeat on relevant half
- Efficient for large codebases

**Minimal Reproduction:**
- Remove non-essential code
- Simplify to core issue
- Use test cases
- Isolate from external dependencies

**Component Testing:**
- Test individual components
- Unit tests
- Integration tests
- System tests

---

## Exercises

### Exercise 1: Debugging Methodology
**Objective:** Apply systematic debugging approach.

**Tasks:**
1. What are the 7 steps of systematic debugging?
2. Why is consistent reproduction important?
3. How do you isolate a problem?
4. What is binary search debugging?
5. Why verify fix works?

**Expected Outcome:** You understand systematic debugging methodology.

### Exercise 2: Error Types
**Objective:** Distinguish between error types.

**Tasks:**
1. What is the difference between compile and runtime errors?
2. What is a logic error?
3. What causes segmentation faults?
4. What causes linker errors?
5. When do stack overflows occur?

**Expected Outcome:** You understand different error types and causes.

### Exercise 3: Race Conditions
**Objective:** Understand race conditions.

**Tasks:**
1. What is a race condition?
2. How do you prevent race conditions?
3. What is priority inversion?
4. What is a deadlock?
5. How do you debug race conditions?

**Expected Outcome:** You understand concurrency issues.

### Exercise 4: Memory Corruption
**Objective:** Understand memory issues.

**Tasks:**
1. What is a buffer overflow?
2. What is stack overflow?
3. What is heap corruption?
4. What is use-after-free?
5. How do you detect memory corruption?

**Expected Outcome:** You understand memory-related bugs.

### Exercise 5: GDB Commands
**Objective:** Understand GDB usage.

**Tasks:**
1. How do you set a breakpoint?
2. How do you step through code?
3. How do you view backtrace?
4. How do you inspect variables?
5. How do you set a watchpoint?

**Expected Outcome:** You understand GDB debugging.

### Exercise 6: Hardware Tools
**Objective:** Understand hardware debugging tools.

**Tasks:**
1. What is a logic analyzer used for?
2. What is an oscilloscope used for?
3. What is a multimeter used for?
4. When would you use Wireshark?
5. How do you choose between tools?

**Expected Outcome:** You understand hardware debugging tools.

### Exercise 7: Communication Debugging
**Objective:** Understand communication debugging.

**Tasks:**
1. How do you debug UART issues?
2. How do you debug I2C issues?
3. How do you debug SPI issues?
4. What are common communication errors?
5. How do you verify timing?

**Expected Outcome:** You understand communication debugging.

### Exercise 8: Power Debugging
**Objective:** Understand power-related issues.

**Tasks:**
1. What are symptoms of insufficient power?
2. What is a brownout?
3. How do you measure current draw?
4. What causes voltage drops?
5. How do you debug power issues?

**Expected Outcome:** You understand power debugging.

### Exercise 9: Logging Strategy
**Objective:** Understand effective logging.

**Tasks:**
1. What are common log levels?
2. Why is structured logging important?
3. How do logging affect performance?
4. How do you analyze logs?
5. When should you disable logging?

**Expected Outcome:** You understand logging best practices.

### Exercise 10: Minimal Reproduction
**Objective:** Understand creating minimal reproductions.

**Tasks:**
1. Why create minimal reproductions?
2. How do you remove non-essential code?
3. How do you isolate external dependencies?
4. How do you test components individually?
5. What makes a good test case?

**Expected Outcome:** You understand fault isolation techniques.

---

## Labs

### Lab 1: Compile Error Debugging
**Objective:** Diagnose and fix compile errors.

**Prerequisites:**
- C programming knowledge (Phase 2)
- Compiler available

**Procedure:**

**1. Intentional Compile Errors:**
```c
// Missing semicolon
int main() {
    int x = 5
    return 0;
}
```

**2. Diagnose:**
- Compile: `gcc -Wall -o test test.c`
- Read error message
- Identify issue (missing semicolon)
- Fix

**3. More Errors:**
- Undefined variable
- Wrong type
- Missing include
- Wrong function signature

**4. Fix Each:**
- Understand error message
- Identify root cause
- Implement fix
- Verify fix

**Expected Behavior:**
- Compile errors understood
- Error messages interpreted correctly
- All errors fixed

**Completion Criteria:**
- Can diagnose compile errors
- Can fix compile errors
- Understand error messages

---

### Lab 2: Runtime Error Debugging
**Objective:** Diagnose and fix runtime errors.

**Prerequisites:**
- Completed Lab 1

**Procedure:**

**1. Segmentation Fault:**
```c
#include <stdio.h>

int main() {
    int *ptr = NULL;
    *ptr = 5;  // Segmentation fault
    return 0;
}
```

**2. Diagnose with GDB:**
```bash
gcc -g -o test test.c
gdb ./test
(gdb) run
(gdb) backtrace
```

**3. More Runtime Errors:**
- Array out of bounds
- Division by zero
- Stack overflow

**4. Fix Each:**
- Use GDB to identify location
- Understand cause
- Implement fix
- Verify fix

**Expected Behavior:**
- Runtime errors caught by GDB
- Backtrace identifies location
- Fixes prevent crashes

**Completion Criteria:**
- Can use GDB for runtime errors
- Can diagnose segmentation faults
- Can fix runtime errors

---

### Lab 3: Logic Error Debugging
**Objective:** Diagnose and fix logic errors.

**Prerequisites:**
- Completed Lab 2

**Procedure:**

**1. Off-by-One Error:**
```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i <= 5; i++) {  // Off-by-one
        printf("%d\n", arr[i]);
    }
    return 0;
}
```

**2. Diagnose:**
- Run program
- Observe incorrect output
- Add logging
- Identify issue

**3. More Logic Errors:**
- Wrong condition
- Incorrect algorithm
- State machine error

**4. Fix Each:**
- Add debug prints
- Trace execution
- Identify logic error
- Implement fix

**Expected Behavior:**
- Logic errors identified through logging
- Correct behavior after fix
- Understanding of root cause

**Completion Criteria:**
- Can diagnose logic errors
- Can use logging for debugging
- Can fix logic errors

---

### Lab 4: Race Condition Debugging
**Objective:** Diagnose and fix race conditions.

**Prerequisites:**
- Understanding of interrupts/tasks

**Procedure:**

**1. Race Condition Example:**
```c
volatile int counter = 0;

void interrupt_handler() {
    counter++;  // Not atomic
}

int main() {
    // Enable interrupt
    while (1) {
        printf("%d\n", counter);
    }
}
```

**2. Diagnose:**
- Observe incorrect behavior
- Understand race condition
- Identify non-atomic operation

**3. Fix:**
- Disable interrupt during access
- Use atomic operations
- Add mutex (if RTOS)

**Expected Behavior:**
- Race condition understood
- Atomic operations used
- Correct behavior

**Completion Criteria:**
- Understand race conditions
- Can fix race conditions
- Understand atomic operations

---

### Lab 5: Memory Corruption Debugging
**Objective:** Diagnose and fix memory corruption.

**Prerequisites:**
- Understanding of memory management

**Procedure:**

**1. Buffer Overflow:**
```c
#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10];
    strcpy(buffer, "This is too long");  // Overflow
    return 0;
}
```

**2. Diagnose:**
- Run with valgrind (if available)
- Observe crash or corruption
- Identify overflow

**3. More Memory Issues:**
- Stack overflow (deep recursion)
- Use-after-free
- Double-free

**4. Fix Each:**
- Use safe functions (strncpy)
- Check bounds
- Fix memory management

**Expected Behavior:**
- Memory corruption identified
- Safe functions used
- No memory errors

**Completion Criteria:**
- Understand memory corruption
- Can use memory checking tools
- Can fix memory issues

---

### Lab 6: GPIO Debugging
**Objective:** Debug GPIO issues.

**Prerequisites:**
- Raspberry Pi or ESP32

**Procedure:**

**1. GPIO Not Working:**
- Configure GPIO as output
- Set GPIO high
- Measure with multimeter
- No output

**2. Diagnose:**
- Check GPIO pin number
- Check GPIO direction
- Check electrical connection
- Check current limit

**3. More GPIO Issues:**
- Floating input
- Wrong pin mode
- Pin damaged

**4. Fix Each:**
- Correct configuration
- Fix wiring
- Add pull-up/pull-down

**Expected Behavior:**
- GPIO issues diagnosed
- Configuration corrected
- GPIO working correctly

**Completion Criteria:**
- Can debug GPIO issues
- Can use multimeter for debugging
- Understand GPIO configuration

---

### Lab 7: I2C Debugging
**Objective:** Debug I2C communication issues.

**Prerequisites:**
- I2C sensor and microcontroller

**Procedure:**

**1. I2C Device Not Detected:**
- Connect I2C sensor
- Run i2cdetect
- Device not found

**2. Diagnose:**
- Check wiring (SDA, SCL, GND)
- Check pull-up resistors
- Check I2C enabled
- Check device address
- Check power supply

**3. More I2C Issues:**
- Wrong data read
- Communication timeout
- Multiple devices conflict

**4. Fix Each:**
- Fix wiring
- Add pull-up resistors
- Enable I2C
- Verify address

**Expected Behavior:**
- I2C device detected
- Data read correctly
- Communication reliable

**Completion Criteria:**
- Can debug I2C issues
- Can use i2cdetect
- Understand I2C troubleshooting

---

### Lab 8: UART Debugging
**Objective:** Debug UART communication issues.

**Prerequisites:**
- Two devices with UART

**Procedure:**

**1. UART Not Communicating:**
- Configure UART on both devices
- Send data
- No data received

**2. Diagnose:**
- Check baud rate match
- Check TX/RX cross-connection
- Check ground connection
- Check UART enabled
- Check data format (8N1)

**3. More UART Issues:**
- Garbage data
- Data loss
- framing errors

**4. Fix Each:**
- Match baud rate
- Fix wiring
- Enable UART
- Verify configuration

**Expected Behavior:**
- UART communication working
- Data received correctly
- No framing errors

**Completion Criteria:**
- Can debug UART issues
- Can use serial tools
- Understand UART troubleshooting

---

### Lab 9: Power Debugging
**Objective:** Debug power-related issues.

**Prerequisites:**
- Multimeter
- Embedded system

**Procedure:**

**1. System Randomly Resets:**
- System runs
- Randomly resets
- Suspect power issue

**2. Diagnose:**
- Measure voltage under load
- Check current draw
- Check power supply rating
- Check for brownouts
- Check power connections

**3. More Power Issues:**
- Voltage drops
- High current draw
- Insufficient current

**4. Fix Each:**
- Replace power supply
- Improve connections
- Reduce current draw
- Add decoupling capacitors

**Expected Behavior:**
- Voltage adequate under load
- No random resets
- Power supply adequate

**Completion Criteria:**
- Can measure voltage/current
- Can diagnose power issues
- Understand power requirements

---

### Lab 10: Logic Analyzer Usage
**Objective:** Use logic analyzer for debugging.

**Prerequisites:**
- Logic analyzer hardware
- I2C or SPI communication

**Procedure:**

**1. Capture I2C Communication:**
- Connect logic analyzer to SDA, SCL
- Set up trigger (start condition)
- Capture communication
- Decode protocol

**2. Analyze:**
- Check timing
- Check data correctness
- Check for errors
- Check for ACK/NACK

**3. More Captures:**
- SPI communication
- UART communication
- GPIO timing

**4. Diagnose Issues:**
- Identify timing violations
- Identify protocol errors
- Identify electrical issues

**Expected Behavior:**
- Logic analyzer captures signals
- Protocol decoded correctly
- Issues identified

**Completion Criteria:**
- Can use logic analyzer
- Can decode protocols
- Can analyze timing

---

## Project

### Project: Embedded Debugging Lab

**Objective:** Create a comprehensive debugging lab with intentional bugs that must be diagnosed and fixed.

**Requirements:**
- Multiple intentional bugs
- Different bug types (compile, runtime, logic, race condition, memory)
- Debugging scenarios
- Solutions documentation
- Troubleshooting guide

**Implementation:**
- C/C++ code with bugs
- ESP32 or Raspberry Pi target
- GDB debugging exercises
- Hardware debugging exercises
- Documentation for each bug

**Deliverables:**
- Buggy code base
- Bug descriptions
- Expected behavior
- Hints for debugging
- Solutions
- Debugging methodology documentation

**Time Estimate:** 10-15 hours

**Project Structure:**
```
embedded-debugging-lab/
├── README.md
├── src/
│   ├── buggy_code_1.c
│   ├── buggy_code_2.c
│   └── ...
├── tests/
│   └── test_scenarios.md
├── docs/
│   ├── solutions.md
│   └── methodology.md
└── results/
    └── debugging_log.md
```

**Note:** This project teaches systematic debugging methodology through hands-on practice with realistic bugs.

---

## Common Mistakes

### Mistake 1: Trial-and-Error Debugging
**Problem:** Randomly changing code without understanding
**Consequence:** Wastes time, may introduce new bugs
**Solution:** Use systematic debugging methodology

### Mistake 2: Ignoring Error Messages
**Problem:** Not reading or understanding compiler/warning messages
**Consequence:** Miss critical information
**Solution:** Always read and understand error messages

### Mistake 3: Not Reproducing Issue
**Problem:** Trying to fix without consistent reproduction
**Consequence:** Cannot verify fix works
**Solution:** Reproduce issue consistently before fixing

### Mistake 4: Fixing Symptoms Not Root Cause
**Problem:** Making superficial fixes
**Consequence:** Issue recurs
**Solution:** Address root cause

### Mistake 5: Not Using Version Control
**Problem:** No ability to revert changes
**Consequence:** Cannot undo bad changes
**Solution:** Use git, commit frequently

### Mistake 6: Overlooking Simple Causes
**Problem:** Assuming complex issue when simple cause exists
**Consequence:** Wastes time
**Solution:** Check simple things first (power, connections, configuration)

### Mistake 7: Not Measuring
**Problem:** Assuming instead of measuring
**Consequence:** Wrong conclusions
**Solution:** Always measure before concluding

### Mistake 8: Not Documenting
**Problem:** Not documenting debugging process
**Consequence:** Cannot learn or share
**Solution:** Document steps, measurements, conclusions

### Mistake 9: Changing Multiple Things at Once
**Problem:** Changing multiple variables simultaneously
**Consequence:** Cannot identify which change fixed issue
**Solution:** Change one variable at a time

### Mistake 10: Not Verifying Fix
**Problem:** Implementing fix without verification
**Consequence:** Fix may not work or introduces new issues
**Solution:** Always verify fix works in realistic conditions

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What are the 7 steps of systematic debugging?
2. What is the difference between compile and runtime errors?
3. What is a race condition?
4. What is a buffer overflow?
5. How do you set a breakpoint in GDB?
6. What is a watchpoint?
7. What is a logic analyzer used for?
8. What is binary search debugging?
9. What causes stack overflow?
10. How do you debug I2C issues?
11. What are symptoms of insufficient power?
12. What is a brownout?
13. How do you create a minimal reproduction?
14. What is the purpose of assertions?
15. How do you measure current with a multimeter?
16. What is a segmentation fault?
17. How do you debug UART issues?
18. What is priority inversion?
19. What is use-after-free?
20. Why is structured logging important?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **Compile Error:** Diagnose and fix intentional compile errors
2. **Runtime Error:** Use GDB to diagnose and fix segmentation fault
3. **Logic Error:** Diagnose and fix off-by-one error using logging
4. **Race Condition:** Identify and fix race condition
5. **Memory Corruption:** Diagnose and fix buffer overflow
6. **GPIO Issue:** Debug GPIO not working with multimeter
7. **I2C Issue:** Debug I2C device not detected
8. **UART Issue:** Debug UART communication failure
9. **Power Issue:** Diagnose random resets using multimeter
10. **Logic Analyzer:** Use logic analyzer to capture and decode I2C

**Documentation Required:**
- Bug descriptions
- Diagnosis process
- Measurements taken
- Fixes implemented
- Verification results

**Passing Criteria:** All tasks completed with systematic debugging methodology demonstrated.

---

## Completion Checklist

Before moving to Phase 14, verify you have:

- [ ] Understand systematic debugging methodology
- [ ] Can diagnose compile errors
- [ ] Can diagnose runtime errors
- [ ] Can diagnose logic errors
- [ ] Can diagnose race conditions
- [ ] Can diagnose memory corruption
- [ ] Can use GDB for debugging
- [ ] Can use hardware tools (multimeter, logic analyzer)
- [ ] Can debug GPIO issues
- [ ] Can debug communication issues (I2C, SPI, UART)
- [ ] Can debug power issues
- [ ] Can implement effective logging
- [ ] Can perform fault isolation
- [ ] Can create minimal reproductions
- **Completed Lab 1** - Compile Error Debugging
- **Completed Lab 2** - Runtime Error Debugging
- **Completed Lab 3** - Logic Error Debugging
- **Completed Lab 4** - Race Condition Debugging
- **Completed Lab 5** - Memory Corruption Debugging
- **Completed Lab 6** - GPIO Debugging
- **Completed Lab 7** - I2C Debugging
- **Completed Lab 8** - UART Debugging
- **Completed Lab 9** - Power Debugging
- **Completed Lab 10** - Logic Analyzer Usage
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Completed the Embedded Debugging Lab project

---

## Do Not Continue Until...

**Do not start Phase 14 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can apply systematic debugging methodology
5. You can diagnose software errors (compile, runtime, logic)
6. You can diagnose hardware issues (GPIO, communication, power)
7. You can use GDB for debugging
8. You can use hardware debugging tools
9. You can implement effective logging
10. You can perform fault isolation

**Debugging is a critical engineering skill. Systematic debugging methodology, combined with appropriate tools, enables efficient diagnosis and resolution of embedded system issues. Mastering debugging is essential before learning advanced concepts like RTOS and security.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 14 — RTOS / FreeRTOS**

Phase 14 will teach you real-time operating system concepts, task management, synchronization primitives, and concurrent programming for embedded systems, building on the debugging skills you have acquired.

---

**Debugging is not about finding bugs—it's about understanding systems. Systematic debugging methodology, appropriate tools, and structured logging enable efficient diagnosis and resolution of issues, preventing recurrence and improving system reliability.**
