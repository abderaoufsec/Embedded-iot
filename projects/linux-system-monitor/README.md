# Linux System Monitor

> **Status:** Project specification
>
> **Implementation:** Complete implementation is performed by the learner during the course.
>
> **Prerequisite:** Phase 11 — Linux for Embedded

---

## Project Overview

Create a command-line system monitoring tool that reports Linux system information including hostname, uptime, CPU, memory, disk, network, and process information.

This project applies Linux CLI skills, Bash scripting, text processing, and system monitoring concepts learned in Phase 11.

---

## Requirements

### Core Features

- **Hostname:** Display system hostname
- **Uptime:** Display system uptime
- **CPU Information:** Display CPU model, cores, architecture
- **Memory Usage:** Display memory usage statistics
- **Disk Usage:** Display disk usage for mounted filesystems
- **Network Interfaces:** Display network interface information
- **Process Information:** Display top processes by CPU/memory
- **Timestamp:** Display current timestamp

### Optional Extensions

- **Color-coded output:** Use colors for alerts and warnings
- **Alert thresholds:** Alert when CPU > 80%, memory > 90%, disk > 90%
- **Process filtering:** Filter processes by name or user
- **Configuration file:** Load thresholds and settings from config file
- **Historical data:** Save measurements to file over time

---

## Implementation Options

### Option 1: Bash Script (Recommended)

Implement as a Bash script using:
- `hostname`, `uptime`
- `lscpu`, `free`, `df`
- `ip addr`, `ps aux`
- Conditional logic for alerts
- Text processing with grep, awk, sed

### Option 2: C Program (Extension)

Implement as a C program using:
- Standard library for file I/O
- System calls to read /proc and /sys
- Color output with ANSI escape codes
- Structured data handling

---

## Project Structure

```
linux-system-monitor/
├── README.md
├── src/
│   ├── monitor.sh (Bash script)
│   └── monitor.c (optional C version)
├── config/
│   └── config.conf (configuration file)
├── docs/
│   └── architecture.md (design documentation)
└── results/
    └── measurements.md (sample output)
```

---

## Deliverables

1. **Working script or program** that reports system information
2. **Configuration documentation** explaining any config file format
3. **Usage documentation** explaining how to run the tool
4. **Testing documentation** showing sample output

---

## Time Estimate

4-6 hours for basic implementation (Bash script)
Additional 2-3 hours for C program extension

---

## Learning Objectives

This project teaches:
- Linux system monitoring commands
- Bash scripting for automation
- Text processing and data extraction
- Configuration file handling
- Alert logic and thresholds
- Structured output formatting

---

## Next Steps

After completing this project, you will have:
- Practical experience with Linux system monitoring
- A reusable system monitoring tool
- Foundation for embedded Linux monitoring applications
- Skills applicable to Phase 12 (Raspberry Pi) and beyond
