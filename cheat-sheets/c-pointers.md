# C Pointers Cheat Sheet

Quick reference for C pointer concepts in embedded systems.

## Pointer Basics

### Declaration
```c
int *ptr;           // Pointer to int
char *str;          // Pointer to char
void *generic;      // Generic pointer
```

### Address Operator
```c
int x = 10;
int *ptr = &x;      // ptr holds address of x
```

### Dereferencing
```c
int x = 10;
int *ptr = &x;
int value = *ptr;   // value = 10
```

## Pointer Arithmetic

### Array Indexing
```c
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;
int first = *ptr;       // arr[0]
int second = *(ptr+1);  // arr[1]
```

### Pointer Increment
```c
int arr[5];
int *ptr = arr;
ptr++;    // Moves by sizeof(int) bytes
```

## Common Embedded Patterns

### Register Access
```c
#define GPIO_BASE 0x40020000
volatile uint32_t *GPIO_ODR = (uint32_t *)(GPIO_BASE + 0x14);
*GPIO_ODR |= (1 << 5);  // Set bit 5
```

### Memory-Mapped I/O
```c
volatile uint32_t *reg = (uint32_t *)0x40021000;
*reg = 0x12345678;
```

### Function Pointers
```c
void (*callback)(void);
callback = my_function;
callback();
```

## Common Pitfalls

- Uninitialized pointers
- Dangling pointers
- Memory leaks
- Pointer arithmetic on wrong types
- Missing volatile for hardware registers

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 2 - C Programming.*
