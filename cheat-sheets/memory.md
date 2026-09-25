# Memory Cheat Sheet

Quick reference for memory concepts in embedded systems.

## Memory Types

### RAM (Random Access Memory)
- Volatile (loses data without power)
- Fast read/write access
- Used for variables, stack, heap
- Limited size on microcontrollers

### Flash/ROM
- Non-volatile (retains data without power)
- Stores firmware/program code
- Slower than RAM
- Limited write cycles

### EEPROM
- Non-volatile
- Byte-erasable
- Used for configuration data
- Very limited write cycles

## Memory Layout

### Typical MCU Memory Map
```
0x00000000 ────────────── Flash (Program)
0x08000000 ────────────── SRAM (Data)
0x20000000 ────────────── Peripherals
```

### Stack vs Heap
- **Stack**: Automatic storage, function calls, local variables
- **Heap**: Dynamic allocation, manual management
- **Embedded preference**: Avoid dynamic allocation when possible

## Addressing

### Pointers and Addresses
```c
int x = 10;
int *ptr = &x;        // ptr holds address of x
printf("%p", ptr);    // Print address
```

### Memory-Mapped I/O
```c
volatile uint32_t *reg = (uint32_t *)0x40021000;
*reg = 0x12345678;    // Write to hardware register
```

## Common Issues

### Stack Overflow
- Too many nested function calls
- Large local variables
- Recursion without limits

### Memory Leaks
- Forgot to free allocated memory
- Lost pointer to allocated memory
- Rare in embedded if avoiding dynamic allocation

### Fragmentation
- Heap becomes fragmented
- Cannot allocate large blocks
- Avoid by using static allocation

## Best Practices

### Embedded Memory Management
- Prefer static allocation
- Use stack for small, short-lived data
- Avoid malloc/free when possible
- Use memory pools if dynamic allocation needed
- Monitor stack usage
- Use const for data in Flash

### Size Optimization
- Use smallest appropriate data type
- Use bit fields for flags
- Pack structs if needed
- Avoid unnecessary global variables

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 2 - C Programming and Phase 5 - Microcontrollers.*
