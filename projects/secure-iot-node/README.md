# Secure IoT Node

> **Status:** Project specification
>
> **Implementation:** Complete implementation is performed by the learner during the course.
>
> **Prerequisite:** Phase 15 — Embedded Security

---

## Project Overview

Build a secure IoT node implementing security best practices.

This project applies security fundamentals, TLS, authentication, secure storage, and security controls learned in Phase 15.

---

## Requirements

- Device authentication (certificates)
- Secure communication (TLS)
- Secure storage (NVS/encrypted)
- Input validation
- Debug interface protection
- Security monitoring

---

## Project Structure

```
secure-iot-node/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   ├── main.c
│   ├── security.c
│   └── certificates/
├── tests/
│   └── security_tests.md
├── docs/
│   ├── threat_model.md
│   └── security_controls.md
└── results/
    └── security_audit.md
```

---

## Time Estimate

16-20 hours
