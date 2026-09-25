# Phase 0 — Orientation

> **Goal:** Set up your learning environment, understand embedded systems and IoT, and learn how to use this curriculum effectively.
>
> **Prerequisite:** None
>
> **Outcome:** You understand what embedded systems are, have your development environment ready, and know how to progress through this curriculum.

---

## What You Will Learn

By completing this phase, you will understand:

- What embedded systems are and how they differ from computers
- What IoT means and where embedded systems fit in
- The relationship between hardware and software in embedded systems
- The development workflow for embedded systems
- How to use this curriculum effectively
- Basic safety considerations
- What hardware you'll need

---

## Prerequisites

**Before starting this phase, you need:**

- Basic computer literacy (using files, folders, applications)
- Ability to follow technical instructions
- Access to the internet for resources
- A computer (Windows, Mac, or Linux)

**No prior programming or electronics knowledge is required.**

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain what an embedded system is
- Distinguish between embedded systems, computers, and IoT devices
- Understand the role of microcontrollers and microprocessors
- Describe the embedded development workflow
- Set up your development environment
- Use Git for basic repository operations
- Navigate this curriculum structure
- Understand the learning methodology
- Identify required hardware for the curriculum
- Follow safety guidelines for electronics work

---

## Concepts

### What is an Embedded System?

An embedded system is a computer system—a combination of a computer processor, computer memory, and input/output peripheral devices—that has a dedicated function within a larger mechanical or electrical system.

**Key characteristics:**
- **Dedicated purpose:** Designed for specific tasks, not general computing
- **Resource-constrained:** Limited memory, processing power, and power consumption
- **Real-time requirements:** Often must respond within strict time constraints
- **Reliability:** Must operate reliably for long periods
- **Integration:** Typically integrated into larger systems

**Examples:**
- Microwave oven controller
- Car engine control unit (ECU)
- Thermostat
- Digital camera
- Smart watch

### Embedded System vs Computer vs IoT Device

**Computer (General Purpose):**
- Designed for multiple purposes
- Runs operating systems (Windows, macOS, Linux)
- Powerful processor, lots of memory
- User interface (keyboard, mouse, monitor)
- Programmable by the user

**Embedded System:**
- Single purpose or limited purposes
- Often no traditional operating system (or real-time OS)
- Resource-constrained processor and memory
- No traditional user interface
- Pre-programmed or field-updatable firmware

**IoT Device (Internet of Things):**
- Embedded system with network connectivity
- Can communicate with other devices or cloud services
- Often collects sensor data or controls actuators remotely
- Example: Smart thermostat, connected sensor

### MCU vs MPU

**MCU (Microcontroller Unit):**
- Contains processor, memory, and peripherals on single chip
- Self-contained computer system
- Low power consumption
- Lower cost
- Limited processing power and memory
- Used in embedded systems

**MPU (Microprocessor Unit):**
- Just the processor on a chip
- Requires external memory and peripherals
- Higher processing power
- More complex system design
- Used in computers and high-performance systems

**This curriculum focuses on MCUs (specifically ESP32) because they're ideal for learning embedded systems.**

### Firmware

Firmware is software that is embedded in hardware. Unlike regular software that you install on a computer, firmware:

- Is typically stored in non-volatile memory (Flash)
- Is tightly coupled to the hardware
- Controls the device's basic functions
- Is often updated through special procedures
- May be difficult or impossible to modify by end users

**Think of firmware as the "brain" of an embedded system.**

### Hardware/Software Relationship

In embedded systems, hardware and software are tightly integrated:

```
Hardware ←→ Software
    ↓          ↓
Capabilities Implementation
```

- **Hardware determines capabilities:** What sensors, communication interfaces, processing power are available
- **Software determines behavior:** How the hardware is used to perform specific functions
- **You must understand both** to build effective embedded systems

### Sensors and Actuators

**Sensors:** Devices that measure physical quantities
- Temperature, humidity, light, motion, acceleration, etc.
- Convert physical signals to electrical signals
- Provide data to the embedded system

**Actuators:** Devices that take actions
- Motors, relays, LEDs, displays, speakers, etc.
- Convert electrical signals to physical actions
- Allow the embedded system to affect the physical world

### Communication Interfaces

Embedded systems communicate through various interfaces:

- **GPIO:** General Purpose Input/Output (digital on/off)
- **ADC:** Analog-to-Digital Converter (reads analog voltages)
- **PWM:** Pulse Width Modulation (variable power control)
- **UART:** Serial communication (simple point-to-point)
- **I²C:** Inter-Integrated Circuit (multi-device serial bus)
- **SPI:** Serial Peripheral Interface (high-speed serial)
- **CAN:** Controller Area Network (industrial automotive)

### Edge Computing

Edge computing means processing data close to where it's generated (the "edge") rather than sending everything to the cloud:

**Traditional:**
```
Sensor → Cloud → Processing → Response
```

**Edge Computing:**
```
Sensor → Local Processing → Cloud (if needed)
```

**Benefits:**
- Faster response times
- Reduced bandwidth usage
- Better privacy
- Can work offline

### Embedded Development Workflow

The embedded development cycle differs from regular software development:

```
1. Write Code
   ↓
2. Compile
   ↓
3. Link
   ↓
4. Generate Firmware
   ↓
5. Flash to Device
   ↓
6. Boot and Execute
   ↓
7. Debug
   ↓
8. Repeat
```

**Key differences from regular software:**
- Code runs on different hardware than your development machine
- Cross-compilation is often required
- Physical hardware testing is essential
- Debugging often requires special tools
- Firmware updates require special procedures

### Toolchain Concept

A toolchain is the set of software tools used to develop embedded applications:

- **Compiler:** Converts your code to machine code
- **Linker:** Combines compiled code into executable firmware
- **Debugger:** Helps find and fix errors
- **Flash tool:** Programs the device with firmware
- **Libraries:** Pre-written code for common functions

### Git Basics for This Repository

Git is a version control system. For this curriculum, you need to know:

**Clone the repository:**
```bash
git clone https://github.com/abderaoufsec/Embedded-iot.git
cd Embedded-iot
```

**Check for updates:**
```bash
git pull
```

**Check current version:**
```bash
git log --oneline -1
```

**Basic workflow:**
1. Work on your phase
2. Track your progress in completion checklists
3. Don't commit changes unless you're contributing improvements

### How to Study Using This Repository

## The Learning Loop

This curriculum follows a specific learning loop:

```
LEARN → EXERCISE → LAB → DEBUG → PROJECT → TEST → DOCUMENT → ADVANCE
```

**Each step is essential:**

1. **LEARN:** Study the concepts and resources
2. **EXERCISE:** Practice the concepts with focused exercises
3. **LAB:** Build practical circuits and code
4. **DEBUG:** Fix problems intentionally introduced
5. **PROJECT:** Apply knowledge to a complete project
6. **TEST:** Verify your understanding with assessments
7. **DOCUMENT:** Record what you learned
8. **ADVANCE:** Move to the next phase only when ready

## Study Methodology

### Before Starting a Phase
1. Read the entire phase README
2. Understand the prerequisites
3. Check the learning outcomes
4. Review the required resources
5. Ensure you have the necessary hardware

### During a Phase
1. Follow the exact study order
2. Complete all exercises (don't skip)
3. Build all labs on real hardware when possible
4. Work through debugging exercises
5. Complete the phase project
6. Take notes on what you learn

### After Completing a Phase
1. Take the knowledge test
2. Complete the practical test
3. Review the completion checklist
4. Only advance if you pass all assessments
5. If you fail, revisit the relevant sections

### Important Principles

**Don't skip assessments:** The tests verify you actually understand the material. Moving forward without understanding will cause problems later.

**Don't copy code without understanding:** If you use example code, make sure you understand every line.

**Don't rush:** Embedded systems build on previous knowledge. Take the time to understand each phase thoroughly.

**Don't skip hardware:** Whenever possible, build circuits and test on real hardware. Simulation is useful but not a replacement.

**Don't skip debugging:** The debugging exercises teach you problem-solving skills that are essential for embedded development.

---

## Exact Resources

### Resource 1: Embedded Systems Overview
- **Provider:** NXP (semiconductor manufacturer)
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Understand what embedded systems are
- **URL:** https://www.nxp.com/docs/en/application-note/AN3460.pdf

### Resource 2: Microcontroller Basics
- **Provider:** SparkFun Electronics
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Learn about microcontrollers and their uses
- **URL:** https://learn.sparkfun.com/tutorials/microcontrollers

### Resource 3: Git Basics
- **Provider:** Git Official Documentation
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Learn basic Git commands for this repository
- **URL:** https://git-scm.com/docs/gittutorial

### Resource 4: Electronics Safety
- **Provider:** SparkFun Electronics
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Learn basic electrical safety
- **URL:** https://learn.sparkfun.com/tutorials/safety

---

## Study Order

Follow this exact sequence:

1. **Read this entire orientation README** (you're here!)
2. **Set up your development environment**
3. **Review the hardware requirements** (see HARDWARE.md)
4. **Acquire or verify you have the starter hardware**
5. **Practice basic Git operations** (clone, pull, log)
6. **Review the ROADMAP.md** to understand the complete curriculum
7. **Read the README.md** to understand the overall approach
8. **Review the RESOURCE_INDEX.md** to understand available resources**
9. **Complete the exercises below**
10. **Take the knowledge test**
11. **Take the practical test**
12. **Review the completion checklist**
13. **Only then proceed to Phase 1**

---

## Exercises

### Exercise 1: Repository Setup

**Objective:** Set up your development environment and verify repository access.

**Tasks:**
1. Clone this repository if you haven't already
2. Navigate to the repository directory
3. Run `git log --oneline -5` to see recent commits
4. Run `git status` to check repository state
5. Create a test file named `setup-test.txt` with the current date
6. Run `git status` again to see the untracked file
7. Delete the test file
8. Verify the repository is clean again

**Expected Outcome:** You can clone, navigate, and check the status of the repository.

### Exercise 2: Hardware Inventory

**Objective:** Identify what hardware you have and what you need.

**Tasks:**
1. Read HARDWARE.md completely
2. Create a list of hardware you currently have
3. Identify missing starter hardware
4. Note any alternatives you might use
5. Plan how to acquire missing components
6. Identify which phases you can start with current hardware

**Expected Outcome:** You know exactly what hardware you have and what you need to acquire.

### Exercise 3: Concept Check

**Objective:** Verify you understand the basic concepts.

**Tasks:**
1. Write a 2-3 sentence explanation of what an embedded system is
2. List 3 examples of embedded systems in everyday life
3. Explain the difference between an MCU and MPU
4. Describe what firmware is
5. Explain the relationship between hardware and software in embedded systems
6. List 3 common sensors and 3 common actuators

**Expected Outcome:** You can articulate the basic concepts in your own words.

### Exercise 4: Development Workflow

**Objective:** Understand the embedded development process.

**Tasks:**
1. Draw or describe the embedded development workflow
2. Explain each step in the workflow
3. Identify how this differs from regular software development
4. Explain why hardware testing is essential
5. Describe what a toolchain is

**Expected Outcome:** You understand how embedded development differs from regular software development.

---

## Labs

There are no hardware labs in this orientation phase. Labs begin in Phase 4 (Electronics).

---

## Debugging Tasks

There are no debugging tasks in this orientation phase. Debugging exercises begin in later phases.

---

## Project

**Project: Learning Plan Creation**

**Objective:** Create a personalized learning plan for completing this curriculum.

**Tasks:**
1. Review the complete curriculum in ROADMAP.md
2. Estimate how much time you can dedicate per week
3. Create a timeline for completing phases 0-5 (foundation)
4. Identify potential obstacles (time, hardware, etc.)
5. Plan how to overcome obstacles
6. Set specific goals for the first month
7. Create a simple tracking method (notebook, spreadsheet, etc.)

**Deliverable:** A written learning plan document (can be simple text file).

**Time Estimate:** 30-60 minutes

---

## Common Mistakes

### Mistake 1: Skipping the Setup
**Problem:** Rushing through orientation without proper setup
**Consequence:** Frustration later when tools don't work
**Solution:** Complete all setup tasks thoroughly

### Mistake 2: Ignoring Hardware Requirements
**Problem:** Assuming you can learn without the hardware
**Consequence:** Unable to complete labs and projects
**Solution:** Acquire the starter hardware before Phase 4

### Mistake 3: Not Understanding the Learning Loop
**Problem:** Trying to read only, skipping exercises and labs
**Consequence:** Limited practical skills
**Solution:** Follow the complete LEARN → EXERCISE → LAB → DEBUG → PROJECT → TEST → DOCUMENT → ADVANCE loop

### Mistake 4: Rushing Through Phases
**Problem:** Moving to the next phase without completing assessments
**Consequence:** Knowledge gaps compound in later phases
**Solution:** Only advance when you pass all assessments

### Mistake 5: Skipping Safety Guidelines
**Problem:** Not reading or following safety instructions
**Consequence:** Risk of injury or equipment damage
**Solution:** Always read and follow safety guidelines, especially when working with electricity

---

## Troubleshooting

### Repository Access Issues
**Problem:** Cannot clone or access the repository
**Solutions:**
- Check your internet connection
- Verify the GitHub URL is correct
- Check if GitHub is experiencing outages
- Try using Git instead of the web interface

### Hardware Acquisition Issues
**Problem:** Cannot acquire required hardware
**Solutions:**
- Check local electronics suppliers
- Look for alternative components that serve the same purpose
- Check if friends or colleagues have components to borrow
- Start with phases that don't require specific hardware (0-3)

### Time Management Issues
**Problem:** Not enough time to dedicate to learning
**Solutions:**
- Set realistic expectations
- Focus on consistency over intensity (30 minutes daily is better than 5 hours once a week)
- Use spare moments for review (reading notes, flashcards)
- Adapt the timeline to your schedule

### Motivation Issues
**Problem:** Losing motivation or feeling overwhelmed
**Solutions:**
- Remember why you started learning embedded systems
- Break down large tasks into smaller steps
- Celebrate small victories
- Join embedded systems communities for support
- Take breaks when needed, but return consistently

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is an embedded system?
2. Give 3 examples of embedded systems.
3. What is the difference between an MCU and MPU?
4. What is firmware?
5. How does embedded development differ from regular software development?
6. What is the embedded development workflow?
7. What is a toolchain?
8. What is the purpose of this curriculum?
9. What is the learning loop for this curriculum?
10. Why are assessments important in this curriculum?
11. What is edge computing?
12. What is the difference between a sensor and an actuator?
13. List 3 common communication interfaces in embedded systems.
14. Why is hardware testing essential in embedded development?
15. What should you do if you fail an assessment?

**Passing Score:** 12/15 correct answers

---

## Practical Test

Complete these practical tasks:

1. **Repository Operations:**
   - Clone the repository (or verify you have the latest version)
   - Run `git log --oneline -3` and describe what you see
   - Create a file named `orientation-test.md` with today's date
   - Add it to git staging
   - Unstage it
   - Delete the file
   - Verify repository is clean

2. **Hardware Inventory:**
   - List all the hardware you currently have
   - Identify which starter hardware you're missing
   - Estimate the cost to acquire missing hardware
   - Identify which phases you can start with current hardware

3. **Concept Explanation:**
   - Explain to yourself (or write down) what an embedded system is
   - Explain the difference between hardware and software in embedded systems
   - Describe why you want to learn embedded systems

4. **Learning Plan:**
   - Create a simple learning plan for the next month
   - Include specific goals
   - Include time commitments
   - Include how you'll track progress

**Passing Criteria:** Complete all tasks successfully and demonstrate understanding of the concepts.

---

## Completion Checklist

Before moving to Phase 1, verify you have:

- [ ] Read and understood this entire orientation README
- [ ] Cloned the repository successfully
- [ ] Can perform basic Git operations (clone, status, log)
- [ ] Reviewed and understood the ROADMAP.md
- [ ] Reviewed and understood the README.md
- [ ] Reviewed and understood the HARDWARE.md
- [ ] Reviewed and understood the RESOURCE_INDEX.md
- [ ] Created a hardware inventory
- [ ] Identified missing hardware and acquisition plan
- [ ] Completed all exercises
- [ ] Created a learning plan
- [ ] Passed the knowledge test (12/15 correct)
- [ ] Passed the practical test
- [ ] Understand the learning loop (LEARN → EXERCISE → LAB → DEBUG → PROJECT → TEST → DOCUMENT → ADVANCE)
- [ ] Committed to following the methodology
- [ ] Ready to start Phase 1

---

## Do Not Continue Until...

**Do not start Phase 1 until:**

1. You have passed the knowledge test (12/15 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You understand the learning methodology
5. You have a plan for acquiring missing hardware
6. You have set aside time for consistent study

**The foundation you build in orientation will determine your success in later phases. Don't rush it.**

---

## Next Step

Once you have completed this orientation phase successfully, proceed to:

**Phase 1 — Computer Fundamentals**

Phase 1 will teach you the foundational knowledge needed to understand how computers work at the bit level, which is essential for embedded systems programming.

---

**You are now ready to begin your embedded systems and IoT learning journey. Take your time with this orientation phase—it will pay off throughout the entire curriculum.**
