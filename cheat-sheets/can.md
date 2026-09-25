# CAN Cheat Sheet

Quick reference for CAN (Controller Area Network) communication protocol.

## Basic CAN

### Key Concepts
- **Differential signaling**: CAN_H and CAN_L
- **Multi-master**: Any node can transmit
- **Message-based**: No addresses, message IDs instead
- **Priority**: Lower ID = higher priority
- **Error detection**: Built-in CRC and error handling

### Connections
```
CAN_H ─────────────────────── CAN_H (all nodes)
CAN_L ─────────────────────── CAN_L (all nodes)
GND   ─────────────────────── GND (all nodes)
120Ω termination at both ends of bus
```

## CAN Frames

### Standard Frame (11-bit ID)
- Start of frame
- ID (11 bits)
- Control field
- Data (0-8 bytes)
- CRC
- ACK
- End of frame

### Extended Frame (29-bit ID)
- Same structure with 29-bit ID

## Common Operations

### Initialize CAN
```c
// Pseudocode - varies by platform
CAN_init(500000);  // 500kbps baud rate
CAN_filter(id, mask);
```

### Send Message
```c
CAN_message_t msg;
msg.id = 0x123;
msg.len = 8;
msg.data[0] = 0x01;
// ... fill data
CAN_send(&msg);
```

### Receive Message
```c
if (CAN_receive(&msg)) {
    // Process msg.id and msg.data
}
```

## Message Filtering

### Accept All
```c
CAN_filter(0x000, 0x000);  // Mask 0 = accept all
```

### Accept Specific ID
```c
CAN_filter(0x123, 0x7FF);  // Only ID 0x123
```

### Accept Range
```c
CAN_filter(0x100, 0x700);  // IDs 0x100-0x1FF
```

## Baud Rates

| Baud Rate | Use Case |
|-----------|----------|
| 125 kbps | Automotive comfort |
| 250 kbps | Automotive body |
| 500 kbps | Automotive powertrain |
| 1 Mbps | High-speed applications |

## Termination

### Bus Termination
- 120Ω resistor at each end
- Prevents signal reflections
- Required for proper operation

### Termination Calculation
```c
R_total = (R1 * R2) / (R1 + R2)
```

## Troubleshooting

### No Communication
- Check termination resistors
- Verify baud rate match
- Check CAN_H/CAN_L connections
- Ensure proper ground connection

### Error States
- Bus-off: Too many errors, node stops
- Error passive: Reduced error tolerance
- Error active: Normal operation

### Signal Issues
- Check voltage levels (CAN_H ~3.5V, CAN_L ~1.5V)
- Verify differential voltage
- Check for shorts

## Best Practices

### For Reliable Communication
- Use proper termination
- Match baud rates exactly
- Implement error handling
- Use appropriate message priority
- Keep messages short (8 bytes max)

### For Automotive
- Follow automotive CAN standards
- Use appropriate baud rates
- Implement diagnostic messages
- Handle error states properly

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 18 - Industrial IoT.*
