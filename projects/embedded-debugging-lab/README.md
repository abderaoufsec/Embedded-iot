# Embedded Debugging Lab

> **Status:** Project specification
>
> **Implementation:** Complete implementation is performed by the learner during the course.
>
> **Prerequisite:** Phase 13 — Debugging

---

## Project Overview

Create a comprehensive debugging lab with intentional bugs that must be diagnosed and fixed using systematic debugging methodology.

This project applies debugging techniques, GDB usage, hardware tools, and systematic troubleshooting learned in Phase 13.

---

## Requirements

### Core Features
- Multiple intentional bugs (compile, runtime, logic, race condition, memory)
- Different bug types to demonstrate various issues
- Debugging scenarios with hints
- Solutions documentation
- Troubleshooting methodology documentation

### Bug Categories
- Compile errors
- Runtime errors (segmentation faults, etc.)
- Logic errors (off-by-one, etc.)
- Race conditions
- Memory corruption (buffer overflows, etc.)
- Hardware issues (GPIO, communication, power)

---

## Implementation

Create code base with intentional bugs, documentation for each bug, and debugging exercises.

---

## Project Structure

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

---

## Deliverables

1. **Buggy code base** with intentional errors
2. **Bug descriptions** explaining each issue
3. **Expected behavior** for each scenario
4. **Hints** for debugging each bug
5. **Solutions** showing fixes
6. **Debugging methodology** documentation

---

## Time Estimate

10-15 hours

---

## Learning Objectives

This project teaches:
- Systematic debugging methodology
- GDB debugging techniques
- Hardware debugging tools
- Fault isolation strategies
- Minimal reproduction techniques
