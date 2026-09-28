# Linux System Monitor Architecture

## Design Overview

This document describes the architecture of the Linux System Monitor project.

## Components

- **monitor.sh**: Main monitoring script
- **config.conf**: Configuration file for thresholds
- **System commands**: hostname, uptime, lscpu, free, df, ip addr, ps aux

## Data Flow

1. Load configuration from config.conf
2. Query system information using Linux commands
3. Process and format data
4. Display output with optional color coding
5. Check thresholds and generate alerts
6. (Optional) Save measurements to file

## Extensions

- Add C program version using /proc and /sys directly
- Add historical data collection
- Add network monitoring over time
- Add process filtering by name or user

---

*This is a project placeholder. Complete implementation is performed by the learner.*
