# C Bitwise Operations Cheat Sheet

Quick reference for bitwise operations in embedded systems.

## Basic Operators

### AND (&)
```c
result = a & b;  // Bitwise AND
```
- Both bits must be 1 for result to be 1
- Used for masking/clearing bits

### OR (|)
```c
result = a | b;  // Bitwise OR
```
- Either bit can be 1 for result to be 1
- Used for setting bits

### XOR (^)
```c
result = a ^ b;  // Bitwise XOR
```
- Bits must be different for result to be 1
- Used for toggling bits

### NOT (~)
```c
result = ~a;     // Bitwise NOT
```
- Inverts all bits
- Used for complement

### Shift Left (<<)
```c
result = a << n; // Shift left by n bits
```
- Equivalent to multiplying by 2^n
- Used for bit positioning

### Shift Right (>>)
```c
result = a >> n; // Shift right by n bits
```
- Equivalent to dividing by 2^n
- Used for bit extraction

## Common Embedded Patterns

### Set a Bit
```c
REG |= (1 << bit_num);     // Set bit_num to 1
```

### Clear a Bit
```c
REG &= ~(1 << bit_num);    // Clear bit_num to 0
```

### Toggle a Bit
```c
REG ^= (1 << bit_num);     // Toggle bit_num
```

### Test a Bit
```c
if (REG & (1 << bit_num))  // Test if bit_num is set
```

### Set Multiple Bits
```c
REG |= (1 << bit0) | (1 << bit1) | (1 << bit2);
```

### Clear Multiple Bits
```c
REG &= ~((1 << bit0) | (1 << bit1) | (1 << bit2));
```

## Register Manipulation

### Read-Modify-Write
```c
uint32_t temp = REG;        // Read
temp |= (1 << 5);          // Modify
REG = temp;                // Write
```

### Atomic Operations
```c
REG |= (1 << 5);           // Set bit 5 atomically
REG &= ~(1 << 5);          // Clear bit 5 atomically
```

## Bit Fields

### Define Bit Field
```c
struct {
    unsigned int bit0 : 1;
    unsigned int bit1 : 1;
    unsigned int reserved : 6;
} flags;
```

### Access Bit Field
```c
flags.bit0 = 1;
if (flags.bit1) { /* ... */ }
```

## Common Masks

### Single Bit Masks
```c
#define BIT0 (1 << 0)
#define BIT1 (1 << 1)
#define BIT2 (1 << 2)
// etc.
```

### Multi-Bit Masks
```c
#define LOWER_NIBBLE 0x0F    // 00001111
#define UPPER_NIBBLE 0xF0    // 11110000
```

## Extraction and Insertion

### Extract Bits
```c
value = (REG >> offset) & mask;
```

### Insert Bits
```c
REG = (REG & ~mask) | ((value << offset) & mask);
```

## Common Pitfalls

- Operator precedence (use parentheses)
- Signed vs unsigned issues
- Shifting beyond data type size
- Endianness considerations
- Volatile for hardware registers

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 2 - C Programming.*
