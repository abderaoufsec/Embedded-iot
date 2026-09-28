# FreeRTOS Multitask Node

> **Status:** Project specification
>
> **Implementation:** Complete implementation is performed by the learner during the course.
>
> **Prerequisite:** Phase 14 — RTOS / FreeRTOS

---

## Project Overview

Build a multitask embedded monitoring/control system using FreeRTOS.

This project applies RTOS concepts, task management, synchronization primitives, and concurrent programming learned in Phase 14.

---

## Requirements

- Multiple FreeRTOS tasks
- Queue-based inter-task communication
- Mutex for resource protection
- Semaphore for signaling
- Proper stack sizing
- Error handling
- Stack monitoring

---

## Project Structure

```
freertos-multitask-node/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   ├── main.c
│   ├── sensor_task.c
│   ├── processing_task.c
│   └── communication_task.c
├── tests/
│   └── test_scenarios.md
├── docs/
│   └── architecture.md
└── results/
    └── measurements.md
```

---

## Time Estimate

12-16 hours
