# Edge IoT Gateway

> **Status:** Project specification
>
> **Implementation:** Complete implementation is performed by the learner during the course.
>
> **Prerequisite:** Phase 16 — Cloud and Edge

---

## Project Overview

Build a complete edge IoT gateway with cloud integration.

This project applies edge computing, cloud integration, data pipelines, and end-to-end IoT system architecture learned in Phase 16.

---

## Requirements

- Device connection (MQTT)
- Protocol translation
- Local data buffering
- Cloud sync
- Local time-series database
- REST API
- Monitoring and logging
- Offline operation
- Docker containerization
- Security (TLS, authentication)

---

## Project Structure

```
edge-iot-gateway/
├── README.md
├── src/
│   ├── gateway.py
│   ├── mqtt_handler.py
│   ├── data_processor.py
│   ├── api.py
│   └── config.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── tests/
│   └── test_gateway.py
├── docs/
│   ├── architecture.md
│   └── api_docs.md
└── results/
    └── performance.md
```

---

## Time Estimate

20-24 hours
