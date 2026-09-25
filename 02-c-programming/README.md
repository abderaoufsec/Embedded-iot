# Phase 2 — C Programming for Embedded Systems

> **Goal:** Develop embedded-focused C programming skills including pointers, memory management, bit manipulation, and understanding how C maps to hardware.
>
> **Prerequisite:** Phase 1 — Computer Fundamentals
>
> **Outcome:** You can write, compile, and debug C programs with embedded-specific considerations, understanding how C code interacts with hardware.

---

## What You Will Learn

By completing this phase, you will understand:

- C program structure and compilation
- Variables, data types, and operators
- Control flow (conditions, loops)
- Functions and scope
- Arrays and strings
- Pointers and pointer arithmetic
- Structs, enums, unions, and typedef
- Bitwise operators and bit manipulation
- const, static, and volatile keywords
- Memory concepts (stack vs heap)
- Dynamic allocation and why embedded systems often avoid it
- Header/source file organization
- Preprocessor and macros
- Compilation and linking basics
- Make/CMake build systems
- Debugging C programs
- Embedded-oriented coding style
- Defensive programming practices
- How C maps to hardware registers and peripherals

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phase 0 — Orientation
- ✅ Completed Phase 1 — Computer Fundamentals
- ✅ Understanding of binary and hexadecimal
- ✅ Understanding of basic computer architecture
- ✅ Understanding of memory addressing concepts

**No prior programming experience is required.**

---

## Learning Outcomes

After completing this phase, you will be able to:

- Write, compile, and run C programs
- Use appropriate data types for embedded systems
- Implement control flow and loops
- Write and use functions
- Work with arrays and strings
- Understand and use pointers effectively
- Use bitwise operations for hardware control
- Define and use structs, enums, and unions
- Understand const, static, and volatile keywords
- Differentiate between stack and heap memory
- Organize code into header and source files
- Use the preprocessor and macros appropriately
- Understand compilation and linking
- Use basic build systems (Make/CMake)
- Debug C programs effectively
- Write embedded-oriented C code
- Understand how C maps to hardware registers

---

## Concepts

### C Program Structure

**Basic C Program:**
```c
#include <stdio.h>

int main(void) {
    printf("Hello, Embedded World!\n");
    return 0;
}
```

**Components:**
- **Preprocessor directives:** Lines starting with # (processed before compilation)
- **Header files:** Provide function declarations and constants
- **main function:** Entry point of the program
- **Statements:** Instructions executed by the program
- **Comments:** Ignored by the compiler (// for single-line, /* */ for multi-line)

### Variables and Data Types

**Variables:** Named storage locations for data
- **Declaration:** Specifying the type and name
- **Initialization:** Giving an initial value
- **Scope:** Where the variable is accessible

**Basic Data Types:**
- **int:** Integer (typically 32-bit)
- **char:** Character (1 byte)
- **float:** Single-precision floating point
- **double:** Double-precision floating point
- **void:** No type (used for functions returning nothing)

**Size Modifiers:**
- **short:** Smaller integer (typically 16-bit)
- **long:** Larger integer (typically 32-bit or 64-bit)
- **long long:** Very large integer (typically 64-bit)

**Signed vs Unsigned:**
- **signed:** Can represent positive and negative numbers (default)
- **unsigned:** Can represent only positive numbers

**Embedded-Specific Types:**
- **uint8_t, uint16_t, uint32_t:** Unsigned integers of specific sizes
- **int8_t, int16_t, int32_t:** Signed integers of specific sizes
- **Defined in stdint.h for portability**

### Operators

**Arithmetic Operators:** +, -, *, /, %
**Relational Operators:** ==, !=, <, >, <=, >=
**Logical Operators:** && (AND), || (OR), ! (NOT)
**Bitwise Operators:** & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)
**Assignment Operator:** =
**Compound Assignment:** +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=
**Increment/Decrement:** ++, --

### Control Flow

**Conditions (if/else):**
```c
if (condition) {
    // executed if condition is true
} else {
    // executed if condition is false
}
```

**Switch:**
```c
switch (value) {
    case 1:
        // executed if value == 1
        break;
    case 2:
        // executed if value == 2
        break;
    default:
        // executed if no case matches
}
```

**Loops:**
```c
// While loop
while (condition) {
    // executed while condition is true
}

// For loop
for (int i = 0; i < 10; i++) {
    // executed 10 times
}

// Do-while loop
do {
    // executed at least once
} while (condition);
```

### Functions

**Function Declaration (prototype):**
```c
return_type function_name(parameter_types);
```

**Function Definition:**
```c
return_type function_name(parameter_types) {
    // function body
    return value;
}
```

**Function Call:**
```c
result = function_name(arguments);
```

**Scope:** Where a variable is accessible
- **Local scope:** Inside a function
- **Global scope:** Outside all functions
- **Block scope:** Inside a block (within braces)

### Arrays

**Array Declaration:**
```c
int numbers[10];  // Array of 10 integers
char text[100];   // Array of 100 characters
```

**Array Access:**
```c
numbers[0] = 42;    // First element
numbers[9] = 100;   // Last element
```

**Array Initialization:**
```c
int numbers[5] = {1, 2, 3, 4, 5};
char text[] = "Hello";  // String is an array of characters
```

**Why arrays matter:** Used for buffers, sensor data storage, and text processing in embedded systems.

### Strings

**C Strings:** Arrays of characters terminated by null character ('\0')
```c
char text[] = "Hello";  // Actually 6 characters: H e l l o \0
```

**String Functions (string.h):**
- `strlen()`: Get string length
- `strcpy()`: Copy string
- `strcat()`: Concatenate strings
- `strcmp()`: Compare strings

**Why strings matter:** Used for communication protocols, user interfaces, and data formatting.

### Pointers

**Pointer:** Variable that holds a memory address
```c
int value = 42;
int *ptr = &value;  // ptr holds address of value
```

**Dereferencing:** Accessing the value at the address
```c
int value = *ptr;  // Get value at address stored in ptr
```

**Pointer Arithmetic:** Adding/subtracting from pointers
```c
ptr++;  // Move to next integer (add sizeof(int))
ptr--;  // Move to previous integer
```

**Why pointers matter:** Essential for:
- Hardware register access
- Efficient data passing
- Dynamic memory allocation
- Array manipulation
- Implementing data structures

### Pointer Arithmetic

**Array-Pointer Relationship:**
```c
int array[5] = {1, 2, 3, 4, 5};
int *ptr = array;  // Points to array[0]
ptr[1] = 20;  // Same as array[1] = 20
*(ptr + 2) = 30;  // Same as array[2] = 30
```

**Pointer Arithmetic Rules:**
- Adding 1 to a pointer moves it by the size of the pointed-to type
- `ptr + 1` for int* moves by sizeof(int) bytes
- `ptr + 1` for char* moves by sizeof(char) bytes (1 byte)

### Structs

**Struct:** User-defined data type that groups related variables
```c
struct SensorData {
    int temperature;
    int humidity;
    int timestamp;
};

struct SensorData sensor;
sensor.temperature = 25;
sensor.humidity = 60;
```

**Struct Pointers:**
```c
struct SensorData *ptr = &sensor;
ptr->temperature = 30;  // Access struct member through pointer
```

**Why structs matter:** Model hardware registers, sensor data, and device configurations.

### Enums

**Enum:** User-defined type with named integer constants
```c`
enum State {
    STATE_IDLE,
    STATE_RUNNING,
    STATE_ERROR
};

enum State current_state = STATE_IDLE;
```

**Why enums matter:** Make code more readable than using magic numbers.

### Unions

**Union:** Special struct that stores different data types in the same memory location
```c
union Data {
    int value;
    bytes bytes[4];
};
```

**Why unions matter:** Access data in different formats (e.g., as bytes or as an integer).

### Typedef

**Typedef:** Create an alias for a data type
```c
typedef unsigned char uint8_t;
typedef unsigned short uint16_t;
```

**Why typedef matters:** Improves code readability and portability.

### Const, Static, Volatile

**const:** Value cannot be modified
```c
const int MAX_VALUE = 100;
```

**static:**
- **On global variable:** Only accessible within this file
- **On local variable:** Retains value between function calls

**volatile:** Tells the compiler that a variable can change unexpectedly
```c
volatile int *register_ptr = (int *)0x40000000;
```

**Why volatile matters:** Essential for hardware registers and interrupt handlers—prevents compiler optimizations that could break embedded code.

### Bitwise Operators in Detail

**Setting a bit:**
```c
value |= (1 << bit_position);
```

**Clearing a bit:**
```c
value &= ~(1 << bit_position);
```

**Toggling a bit:**
```c
value ^= (1 << bit_position);
```

**Testing a bit:**
```c
if (value & (1 << bit_position)) {
    // bit is set
}
```

**Why bitwise operations matter:** Essential for hardware control—GPIO pins, configuration registers, flags.

### Memory Concepts

**Stack:** Automatic memory for function calls and local variables
- Grows and shrinks automatically
- Limited size
- Fast allocation
- Used for local variables and function call context

**Heap:** Dynamic memory allocation
- Manual allocation and deallocation
- Larger size than stack
- Slower than stack
- Can cause fragmentation
- Often avoided in embedded systems

**Why memory concepts matter:** Understanding memory prevents crashes, leaks, and stack overflows.

### Dynamic Allocation

**malloc():** Allocate memory from heap
```c
int *ptr = (int *)malloc(sizeof(int) * 10);
```

**free():** Deallocate memory
```c
free(ptr);
```

**Why avoid in embedded systems:**
- Can cause fragmentation
- Unpredictable timing
- Risk of memory leaks
- Stack allocation is preferred when possible

### Header/Source Separation

**Header (.h):** Contains declarations
- Function prototypes
- Type definitions
- Constant declarations
- Included by multiple source files

**Source (.c):** Contains implementations
- Function definitions
- Global variables
- Compiled separately

**Why separation matters:** Organizes code, enables separate compilation, and improves build times.

### Preprocessor and Macros

**#define:** Create symbolic constants and macros
```c
#define MAX_VALUE 100
#define SET_BIT(reg, bit) ((reg) |= (1 << (bit)))
```

**Macros with arguments:**
```c
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

**Why preprocessor matters:** Code configuration, conditional compilation, and platform-specific code.

### Compilation and Linking

**Compilation:** Converting source code to object code
- Each .c file compiled separately
- Generates .o (object) files

**Linking:** Combining object files into executable
- Resolves references between files
- Generates final executable

**Build Process:**
```
source.c → preprocessor → compiler → assembler → linker → executable
```

**Why understanding compilation matters:** Helps debug build errors and understand the development process.

### Make/CMake Basics

**Make:** Build automation tool
```makefile
target: dependencies
    command
```

**CMake:** Cross-platform build system
- Generates build files for different platforms
- Handles dependencies
- Modern alternative to Make

**Why build systems matter:** Automate the build process and manage complex projects.

### Debugging C Programs

**Compilation Errors:** Syntax errors that prevent compilation
- Missing semicolons
- Type mismatches
- Undefined variables

**Runtime Errors:** Errors that occur during execution
- Segmentation faults
- Memory leaks
- Logic errors

**Debugging Techniques:**
- Add print statements
- Use a debugger (gdb)
- Check compiler warnings
- Use static analysis tools

**Why debugging matters:** Essential for finding and fixing errors in embedded systems.

### Embedded-Oriented Coding Style

**Characteristics:**
- Efficient use of memory
- Minimal dynamic allocation
- Clear hardware interaction
- Good error handling
- Consistent naming conventions
- Well-commented hardware-specific code

**Why coding style matters:** Makes code maintainable and reliable in resource-constrained environments.

### Defensive Programming

**Principles:**
- Always check return values
- Validate input data
- Handle error conditions
- Use assertions for debugging
- Avoid assumptions
- Consider edge cases

**Why defensive programming matters:** Embedded systems must be reliable—they often cannot be easily updated or debugged in the field.

### How C Maps to Hardware

**Memory-mapped I/O:**
```c
volatile uint32_t *GPIO_REGISTER = (uint32_t *)0x40000000;
*GPIO_REGISTER = 0x01;  // Turn on GPIO pin
```

**Bit fields:**
```c
struct {
    unsigned int pin0 : 1;
    unsigned int pin1 : 1;
    unsigned int reserved : 6;
} gpio_config;
```

**Structs for hardware:**
```c
struct TimerRegisters {
    volatile uint32_t CR1;
    volatile uint32_t CR2;
    volatile uint32_t SMCR;
};
```

**Why mapping matters:** This is how you control hardware in C—reading and writing to specific memory addresses.

---

## Exact Resources

### Resource 1: C Programming Language
- **Provider:** Kernighan and Ritchie (official reference)
- **Level:** Advanced
- **Cost:** Free
- **Purpose:** Comprehensive C language reference
- **URL:** https://www.cs.yale.edu/homes/aspnes/classes/223/notes.html

### Resource 2: GNU C Reference
- **Provider:** Free Software Foundation
- **Level:** Intermediate
- **Cost:** Free
- **Purpose:** Standard C library reference
- **URL:** https://www.gnu.org/software/gnu-c-manual/

### Resource 3: C Tutorial
- **Provider:** Learn-C.org
- **Level:** Beginner
- **Cost:** Free
- **Purpose:** Interactive C programming tutorial
- **URL:** https://www.learn-c.org/

### Resource 4: Embedded C Programming
- **Provider:** Embedded.com
- **Level:** Intermediate
- **Cost:** Free
- **Purpose:** C specifically for embedded systems
- **URL:** https://www.embedded.com/

### Resource 5: Bit Twiddling Hacks
- **Provider:** Bit Twiddling Hacks (Sean Eron Anderson)
- **Level:** Advanced
- **Cost:** Free
- **Purpose:** Bit manipulation techniques
- **URL:** https://graphics.stanford.edu/~seander/bits.html

---

## Study Order

Follow this exact sequence:

1. **Set up C development environment** (compiler, editor)
2. **Study C program structure**
3. **Learn variables and data types**
4. **Study operators and expressions**
5. **Learn control flow (if/else, switch, loops)**
6. **Study functions and scope**
7. **Learn arrays and strings**
8. **Study pointers (this is critical)**
9. **Practice pointer arithmetic**
10. **Study structs, enums, unions, typedef**
11. **Learn const, static, volatile keywords**
12. **Study bitwise operations in detail**
13. **Practice bit manipulation**
14. **Study memory concepts (stack vs heap)**
15. **Learn about dynamic allocation (and why to avoid it)**
16. **Study header/source file organization**
17. **Learn preprocessor and macros**
18. **Understand compilation and linking**
19. **Learn basic Make/CMake**
20. **Study debugging techniques**
21. **Learn embedded-oriented coding style**
22. **Study defensive programming**
23. **Understand how C maps to hardware**
24. **Complete all exercises**
25. **Complete the projects**
26. **Take the knowledge test**
27. **Take the practical test**
28. **Review completion checklist**

---

## Exercises

### Exercise 1: Basic C Program

**Objective:** Write, compile, and run your first C program.

**Tasks:**
1. Write a "Hello, World!" program
2. Compile it using your C compiler
3. Run the executable
4. Modify it to print multiple lines
5. Add comments explaining each line

**Expected Outcome:** You can compile and run a basic C program.

### Exercise 2: Variables and Data Types

**Objective:** Practice using different data types.

**Tasks:**
1. Declare variables of types: int, char, float, double
2. Assign values and print them
3. Try sizeof() to see the size of each type
4. Use uint8_t, uint16_t, uint32_t from stdint.h
5. Experiment with signed vs unsigned

**Expected Outcome:** You understand C data types and their sizes.

### Exercise 3: Control Flow

**Objective:** Practice conditions and loops.

**Tasks:**
1. Write a program that checks if a number is positive/negative
2. Write a program that uses a for loop to print numbers 0-9
3. Write a program that uses a while loop to read input until 0
4. Write a switch statement that handles different characters
5. Combine conditions and loops

**Expected Outcome:** You can implement control flow in C.

### Exercise 4: Functions

**Objective:** Write and use functions.

**Tasks:**
1. Write a function that adds two numbers
2. Write a function that finds the maximum of three numbers
3. Write a function that takes a pointer as parameter
4. Practice function scope with local and global variables
5. Write recursive function to calculate factorial

**Expected Outcome:** You can write and use functions effectively.

### Exercise 5: Arrays

**Objective:** Practice working with arrays.

**Tasks:**
1. Create an array of 10 integers
2. Fill it with values using a loop
3. Find the maximum value in the array
4. Reverse the array in place
5. Create a string and print its length

**Expected Outcome:** You can work with arrays and strings.

### Exercise 6: Pointers

**Objective:** Understand and use pointers.

**Tasks:**
1. Create a variable and a pointer to it
2. Modify the variable through the pointer
3. Create an array and a pointer to it
4. Access array elements using pointer arithmetic
5. Pass a pointer to a function and modify the original value

**Expected Outcome:** You understand pointers and pointer arithmetic.

### Exercise 7: Structs

**Objective:** Create and use structs.

**Tasks:**
1. Define a struct for a simple sensor (temperature, humidity, timestamp)
2. Create an instance and fill it with data
3. Create a pointer to the struct
4. Pass the struct to a function
5. Define an enum for sensor states

**Expected Outcome:** You can use structs to model data.

### Exercise 8: Bitwise Operations

**Objective:** Practice bit manipulation.

**Tasks:**
1. Write functions to set, clear, toggle, and test specific bits
2. Use these functions on example values
3. Extract specific bits from a value
4. Combine bits from multiple values
5. Practice left and right shifts

**Expected Outcome:** You can manipulate individual bits in registers.

### Exercise 9: Memory Management

**Objective:** Understand stack vs heap.

**Tasks:**
1. Create a large local array and observe stack usage
2. Allocate memory dynamically and free it
3. Create a memory leak intentionally and observe
4. Compare stack vs heap allocation speed
5. Understand when to use each

**Expected Outcome:** You understand memory management and when to avoid dynamic allocation.

### Exercise 10: Const, Static, Volatile

**Objective:** Understand these important keywords.

**Tasks:**
1. Create a const variable and try to modify it (should fail)
2. Create a static variable and observe its persistence
3. Use volatile in a simple example
4. Understand when to use each keyword
5. Practice using volatile for hardware register simulation

**Expected Outcome:** You understand when and why to use const, static, and volatile.

---

## Labs

There are no hardware labs in this phase. Labs begin in Phase 4 (Electronics).

---

## Debugging Tasks

There are no debugging tasks in this phase. Debugging exercises begin in later phases.

---

## Projects

### Project 1: CLI Calculator

**Objective:** Create a command-line calculator that demonstrates basic C concepts.

**Requirements:**
- Accept mathematical expressions from user input
- Support basic operations: +, -, *, /
- Handle parentheses
- Show intermediate results
- Handle errors gracefully
- Use functions for each operation

**Suggested Structure:**
```c
// Functions
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);
int parse_expression(char *expression);

// Main
int main() {
    char input[100];
    printf("Enter expression: ");
    fgets(input, sizeof(input), stdin);
    double result = parse_expression(input);
    printf("Result: %f\n", result);
    return 0;
}
```

**Time Estimate:** 2-3 hours

### Project 2: Bit Manipulation Utility

**Objective:** Create a utility that demonstrates bit manipulation operations.

**Requirements:**
- Functions to set, clear, toggle, test bits
- Work with both 8-bit and 16-bit values
- Display binary representation
- Support multiple operations in one call
- Include comprehensive documentation

**Suggested Functions:**
```c
uint8_t set_bit(uint8_t value, uint8_t bit);
uint8_t clear_bit(uint8_t value, uint8_t bit);
uint8_t toggle_bit(uint8_t value, uint8_t bit);
bool test_bit(uint8_t value, uint8_t bit);
void print_binary(uint8_t value);
```

**Time Estimate:** 1-2 hours

### Project 3: Register Simulator

**Objective:** Enhance the register simulator from Phase 1 with more features.

**Requirements:**
- Support immediate values (e.g., ADD R0 5)
- Implement MOV instruction
- Implement flags (zero, carry, overflow)
- Implement conditional jumps
- Support multiple instructions in sequence
- Display complete CPU state

**Suggested Extensions:**
- Support 16-bit operations
- Implement more instructions (SUB, MUL, DIV)
- Add simple program file format

**Time Estimate:** 2-3 hours

### Project 4: Sensor Data Simulator

**Objective:** Create a program that simulates sensor data generation and processing.

**Requirements:**
- Simulate temperature sensor readings with noise
- Implement moving average filter
- Implement threshold detection
- Generate structured output
- Include configuration parameters

**Suggested Structure:**
```c
struct SensorData {
    int temperature;
    int humidity;
    int timestamp;
};

int generate_temperature(int base, int noise);
int moving_average(int *buffer, int size, int new_value);
bool check_threshold(int value, int threshold);
```

**Time Estimate:** 2-3 hours

### Project 5: State Machine

**Objective:** Implement a simple state machine in C.

**Requirements:**
- Define states for a simple system (e.g., traffic light)
- Implement state transitions
- Handle state-specific behavior
- Include input triggers
- Document state diagram

**Suggested Example:**
```c
enum State {
    STATE_RED,
    STATE_YELLOW,
    STATE_GREEN
};

enum State transition_state(enum State current, int trigger);
void execute_state(enum State state);
```

**Time Estimate:** 2-3 hours

---

## Common Mistakes

### Mistake 1: Forgetting Semicolons
**Problem:** Missing semicolons at end of statements
**Consequence:** Compilation errors
**Solution:** Always end statements with semicolons

### Mistake 2: Confusing = and ==
**Problem:** Using assignment operator instead of comparison
**Consequence:** Logic errors in conditions
**Solution:** Use == for comparison, = for assignment

### Mistake 3: Array Index Out of Bounds
**Problem:** Accessing array elements outside valid range
**Consequence:** Undefined behavior, crashes
**Solution:** Always check array bounds

### Mistake 4: Uninitialized Pointers
**Problem:** Using pointers without initializing them
**Consequence:** Crashes, undefined behavior
**Solution:** Always initialize pointers, set to NULL if unused

### Mistake 5: Memory Leaks
**Problem:** Allocating memory without freeing it
**Consequence:** Memory exhaustion over time
**Solution:** Always free allocated memory, match malloc with free

### Mistake 6: Not Using volatile for Hardware
**Problem:** Compiler optimizes away hardware register access
**Consequence:** Code doesn't work as expected
**Solution:** Use volatile for hardware registers and shared variables

### Mistake 7: Confusing Pointers and Arrays
**Problem:** Treating arrays and pointers as identical
**Consequence:** Confusion and errors
**Solution:** Understand they're related but different

### Mistake 8: Integer Overflow
**Problem:** Exceeding the range of a data type
**Consequence:** Incorrect results
**Solution:** Use appropriate data types, check for overflow

### Mistake 9: Stack Overflow
**Problem:** Exceeding stack size with large local variables or deep recursion
**Consequence:** Crashes, undefined behavior
**Solution:** Limit stack usage, avoid deep recursion

### Mistake 10: Ignoring Compiler Warnings
**Problem:** Treating warnings as harmless
**Consequence:** Hidden bugs and errors
**Solution:** Treat warnings as errors, fix all warnings

---

## Troubleshooting

### Compilation Errors
**Problem:** Code won't compile
**Solutions:**
- Read the error message carefully
- Check for missing semicolons
- Check for undeclared variables
- Check for type mismatches
- Check for missing header files

### Runtime Errors
**Problem:** Program crashes or behaves incorrectly
**Solutions:**
- Add print statements to trace execution
- Use a debugger (gdb)
- Check for null pointers
- Check array bounds
- Check for stack overflow

### Memory Issues
**Problem:** Memory-related errors
**Solutions:**
- Check for memory leaks
- Check for stack overflow
- Verify pointer arithmetic
- Check for buffer overflows
- Use memory debugging tools

### Logic Errors
**Problem:** Program runs but produces wrong results
**Solutions:**
- Add debug output
- Verify logic with test cases
- Check operator precedence
- Check for off-by-one errors
- Step through with debugger

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is the difference between int and uint8_t?
2. What is the difference between = and ==?
3. What is a pointer?
4. How do you declare a pointer?
5. What does the & operator do?
6. What does the * operator do?
7. What is a struct?
8. What is an enum?
9. What is the difference between const and #define?
10. What does static do on a global variable?
11. What does static do on a local variable?
12. What is volatile and why is it important in embedded systems?
13. What is the difference between stack and heap?
14. Why should dynamic allocation be avoided in embedded systems?
15. What is the difference between a header file and a source file?
16. What is the preprocessor?
17. What is a macro?
18. What is the result of 0x3A & 0x0F?
19. What is the result of 0x3A | 0�x0F?
20. How do you set bit 3 in a byte?
21. How do you clear bit 3 in a byte?
22. How do you toggle bit 3 in a byte?
23. What is a function prototype?
24. What is function scope?
25. What is the difference between *ptr++ and (*ptr)++?

**Passing Score:** 20/25 correct answers

---

## Practical Test

Complete these practical tasks:

1. **Write a C program that:**
   - Takes two numbers as input
   - Performs addition, subtraction, multiplication, and division
   - Handles division by zero
   - Uses functions for each operation
   - Demonstrates good coding practices

2. **Write a C program that:**
   - Creates an array of 10 integers
   - Fills it with random values
   - Finds the maximum and minimum values
   - Sorts the array
   - Prints the sorted array

3. **Write a C program that:**
   - Defines a struct for student data (name, age, grade)
   - Creates an array of 5 students
   - Fills it with sample data
   - Calculates the average age
   - Finds the student with the highest grade

4. **Write a C program that:**
   - Uses bitwise operations to set, clear, toggle, and test bits
   - Demonstrates each operation with examples
   - Shows the binary representation before and after each operation

5. **Write a C program that:**
   - Demonstrates stack vs heap allocation
   - Measures time difference between stack and heap allocation
   - Shows memory usage differences
   - Explains why embedded systems prefer stack allocation

**Passing Criteria:** All programs compile, run correctly, and demonstrate understanding of the concepts.

---

## Completion Checklist

Before moving to Phase 3, verify you have:

- [ ] Can write, compile, and run C programs
- [ ] Understand C data types and their sizes
- [ ] Can use control flow effectively
- [ ] Can write and use functions
- [ ] Can work with arrays and strings
- [ ] Understand pointers and pointer arithmetic
- [ ] Can use structs, enums, and unions
- [ ] Understand const, static, and volatile keywords
- [ ] Can perform bitwise operations
- [ ] Understand stack vs heap memory
- [ ] Understand why dynamic allocation is often avoided in embedded systems
- [ ] Can organize code into header and source files
- [ ] Understand the preprocessor and macros
- [ ] Understand compilation and linking
- [ ] Can use basic build systems
- [ ] Can debug C programs
- [ ] Write embedded-oriented code
- [ ] Practice defensive programming
- [ ] Understand how C maps to hardware
- [ ] Completed all exercises
- [ ] Completed at least 3 projects
- [ ] Passed the knowledge test (20/25 correct)
- [ ] Passed the practical test
- [ ] Can explain why each concept matters for embedded systems

---

## Do Not Continue Until...

**Do not start Phase 3 until:**

1. You have passed the knowledge test (20/25 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can write C programs without constantly referencing materials
5. You understand pointers and pointer arithmetic
6. You understand why volatile is important for embedded systems
7. You have completed at least 3 projects
8. You understand how C maps to hardware

**C programming is the foundation for embedded systems development. You will use these concepts throughout embedded programming. Don't rush through them.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 3 — Digital Electronics**

Phase 3 will teach you digital electronics fundamentals, logic gates, Boolean algebra, and how digital circuits work—essential foundation for understanding how computers and microcontrollers process data.

---

**C programming skills are essential for embedded systems. Take the time to master pointers, bitwise operations, and memory management—these concepts will be used constantly in embedded programming.**
