# Phase 14 — RTOS / FreeRTOS

> **Goal:** Understand real-time operating system concepts and implement multitasking embedded applications using FreeRTOS.
>
> **Prerequisite:** Phase 13 — Debugging
>
> **Outcome:** You can design and implement RTOS-based embedded systems with tasks, synchronization, and proper resource management.

---

## What You Will Learn

By completing this phase, you will understand:

- **RTOS Fundamentals:** Bare metal vs RTOS, scheduler, determinism
- **Tasks:** Task creation, priorities, states, context switching
- **Scheduling:** Preemptive scheduling, time slicing, tick rate
- **Synchronization:** Queues, semaphores, mutexes, event groups
- **Resource Management:** Critical sections, memory management
- **Concurrency Issues:** Race conditions, deadlocks, priority inversion
- **FreeRTOS Architecture:** Kernel structure, API design
- **ESP32 FreeRTOS:** Integration with ESP-IDF, dual-core considerations
- **Debugging RTOS:** Task monitoring, stack analysis, deadlock detection

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phases 0-13
- ✅ Strong C programming skills (Phase 2)
- ✅ Understanding of microcontrollers (Phase 5)
- ✅ Understanding of ESP32 (Phase 6)
- ✅ Understanding of interrupts (from previous phases)
- ✅ Understanding of debugging (Phase 13)

**Required Hardware:**
- ESP32 development board
- LEDs and resistors
- Push buttons
- I2C sensor (optional)
- UART for debugging

**Required Software:**
- ESP-IDF or Arduino with FreeRTOS
- PlatformIO (recommended)
- Serial terminal

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain when to use RTOS vs bare metal
- Create and manage FreeRTOS tasks
- Implement task priorities and scheduling
- Use queues for inter-task communication
- Use semaphores for synchronization
- Use mutexes for mutual exclusion
- Use event groups for signaling
- Implement critical sections
- Manage memory in RTOS
- Debug RTOS applications
- Avoid common concurrency issues
- Design deterministic real-time systems

---

## Why This Matters

**RTOS vs Bare Metal:**
- **Bare Metal:** Simple, deterministic, single-threaded, manual scheduling
- **RTOS:** Complex scheduling, multitasking, resource management, synchronization

**When to Use RTOS:**
- Multiple concurrent operations
- Complex timing requirements
- Resource sharing between operations
- Need for modularity and separation of concerns
- Complex state machines

**Real-Time Requirements:**
- Deterministic timing
- Predictable response times
- Priority-based scheduling
- Deadline awareness

**Concurrency Challenges:**
- Race conditions
- Deadlocks
- Priority inversion
- Resource starvation

---

## Core Concepts

### RTOS Fundamentals

**Real-Time Operating System:**
- Operating system designed for real-time applications
- Deterministic behavior
- Priority-based scheduling
- Resource management
- Synchronization primitives

**Bare Metal vs RTOS:**
- **Bare Metal:** Single loop, manual state management, no context switching overhead
- **RTOS:** Multiple tasks, automatic scheduling, context switching overhead, modularity

**Determinism:**
- Predictable timing
- Bounded response times
- No unbounded delays
- Critical for real-time systems

**Scheduler:**
- Decides which task runs
- Preemptive: higher priority tasks preempt lower priority
- Cooperative: tasks yield voluntarily
- Time slicing: tasks share CPU time

**Tick:**
- System clock interrupt
- Scheduler ticks at regular intervals
- Tick rate affects resolution and overhead
- Typical tick rates: 1kHz (1ms), 10kHz (100μs)

---

### Tasks

**Task:**
- Independent thread of execution
- Has its own stack
- Has priority
- Can be in different states

**Task States:**
- **Running:** Currently executing on CPU
- **Ready:** Ready to run, waiting for CPU
- **Blocked:** Waiting for event (time, semaphore, queue)
- **Suspended:** Not scheduled

**Task Creation:**
```c
xTaskCreate(
    task_function,    // Task function
    "Task Name",      // Task name
    stack_size,       // Stack size in words
    parameter,        // Task parameter
    priority,         // Task priority
    &task_handle      // Task handle
);
```

**Task Priorities:**
- Higher priority tasks run before lower priority
- Priorities are numerical (configurable base)
- Same priority tasks share CPU (time slicing)
- Priority inheritance for mutexes

**Context Switch:**
- Saving current task state
- Loading next task state
- Overhead: time to switch tasks
- Typically tens to hundreds of microseconds

---

### Scheduling

**Preemptive Scheduling:**
- Higher priority tasks preempt lower priority
- Deterministic priority-based
- Real-time requirements met

**Time Slicing:**
- Same priority tasks share CPU
- Each task gets time slice
- Prevents starvation
- Configurable time slice

**Tick Rate:**
- Frequency of scheduler tick
- Higher tick rate: better resolution, more overhead
- Lower tick rate: less overhead, coarser resolution
- Typical: 1kHz to 10kHz

**Idle Task:**
- Lowest priority task
- Runs when no other task ready
- Can put CPU to sleep
- Measures CPU utilization

---

### Queues

**Queue:**
- Thread-safe data structure
- Pass data between tasks
- First-in-first-out (FIFO)
- Blocking operations

**Queue Operations:**
- `xQueueSend`: Send to queue (blocks if full)
- `xQueueReceive`: Receive from queue (blocks if empty)
- `xQueuePeek`: Peek without removing
- `uxQueueMessagesWaiting`: Count messages

**Queue Use Cases:**
- Producer-consumer pattern
- Data buffering
- Inter-task communication
- Event notification

---

### Semaphores

**Semaphore:**
- Synchronization primitive
- Counting resource
- Signal events
- Blocking operations

**Binary Semaphore:**
- Two states: available/unavailable
- Used for signaling
- Can be given/taken from ISR

**Counting Semaphore:**
- Count of available resources
- Used for resource pooling
- Tracks multiple instances

**Semaphore Operations:**
- `xSemaphoreCreateBinary`: Create binary semaphore
- `xSemaphoreCreateCounting`: Create counting semaphore
- `xSemaphoreTake`: Take semaphore (blocks if unavailable)
- `xSemaphoreGive`: Give semaphore
- `xSemaphoreGiveFromISR`: Give from interrupt

---

### Mutexes

**Mutex (Mutual Exclusion):**
- Protects shared resources
- Only one task can hold at a time
- Priority inheritance
- Ownership (task that took must give)

**Mutex vs Semaphore:**
- **Mutex:** Ownership, priority inheritance, mutual exclusion
- **Semaphore:** No ownership, no priority inheritance, signaling

**Priority Inheritance:**
- Low-priority task holding mutex
- High-priority task waiting for mutex
- Low-priority task temporarily inherits high priority
- Prevents priority inversion

**Mutex Operations:**
- `xSemaphoreCreateMutex`: Create mutex
- `xSemaphoreTake`: Take mutex
- `xSemaphoreGive`: Give mutex
- Only task that took can give

---

### Event Groups

**Event Group:**
- Set of event bits
- Tasks wait on combination of bits
- Efficient for complex signaling
- Can be set from ISR

**Event Group Operations:**
- `xEventGroupCreate`: Create event group
- `xEventGroupSetBits`: Set bits
- `xEventGroupWaitBits`: Wait for bits
- `xEventGroupClearBits`: Clear bits
- `xEventGroupSetBitsFromISR`: Set from ISR

**Event Group Use Cases:**
- Waiting for multiple events
- Complex state synchronization
- Peripheral readiness signaling

---

### Interrupt Interaction

**ISR-Safe APIs:**
- Many FreeRTOS APIs have ISR-safe versions
- End with `FromISR`
- Cannot block in ISR
- Use deferred processing

**Deferred Processing:**
- ISR does minimal work
- ISR signals task via semaphore/queue
- Task processes data
- Prevents ISR blocking

**FromISR APIs:**
- `xQueueSendFromISR`
- `xSemaphoreGiveFromISR`
- `xEventGroupSetBitsFromISR`
- Use portYIELD_FROM_ISR to request context switch

---

### Critical Sections

**Critical Section:**
- Code that must not be interrupted
- Disables interrupts
- Very short duration
- Protects shared data

**Critical Section Operations:**
- `taskENTER_CRITICAL`: Enter critical section
- `taskEXIT_CRITICAL`: Exit critical section
- Keep critical sections short
- No blocking operations in critical section

**Use Cases:**
- Protecting shared variables
- Atomic operations
- Hardware register access

---

### Memory Management

**Heap Allocation:**
- FreeRTOS heap allocation schemes
- heap_1: Only allocates, no free
- heap_2: Allocates and frees, fragmentation
- heap_3: Coalescing free blocks
- heap_4: Coalescing with alignment
- heap_5: Multiple memory regions

**Stack Sizing:**
- Each task has its own stack
- Stack overflow detection
- `uxTaskGetStackHighWaterMark`: Check stack usage
- `uxTaskStackHighWaterMark`: Check stack high water mark

**Static vs Dynamic Allocation:**
- **Static:** Compile-time allocation, no fragmentation
- **Dynamic:** Runtime allocation, risk of fragmentation
- Static allocation preferred for reliability

---

### Concurrency Issues

**Race Condition:**
- Concurrent access to shared data
- Unpredictable results
- Protected by mutex or critical section

**Deadlock:**
- Two or more tasks waiting for each other
- System halts
- Prevention: acquire locks in consistent order

**Priority Inversion:**
- High-priority task blocked by low-priority task
- Medium-priority task runs
- Prevented by priority inheritance (mutex)

**Resource Starvation:**
- Task cannot acquire needed resource
- Never gets CPU time
- Prevention: fair scheduling, timeouts

---

### FreeRTOS Architecture

**Kernel Structure:**
- Scheduler
- Task management
- Queue management
- Semaphore management
- Timer management
- Memory management

**API Design:**
- Consistent naming convention
- Return types (BaseType_t, bool)
- Error handling
- ISR-safe variants

**Configuration:**
- FreeRTOSConfig.h
- Tick rate
- Heap size
- Task priorities
- Queue sizes

---

### ESP32 FreeRTOS

**Dual-Core:**
- ESP32 has two cores (Pro, App)
- FreeRTOS runs on both cores
- Tasks can be pinned to specific core
- Inter-core communication via queues

**ESP-IDF Integration:**
- FreeRTOS built into ESP-IDF
- Extended features
- WiFi, Bluetooth use FreeRTOS
- Event loops

**Task Pinning:**
- `xTaskCreatePinnedToCore`
- Specify core (0 or 1)
- `tskNO_AFFINITY` for any core

**ESP32-Specific APIs:**
- FreeRTOS with ESP-IDF extensions
- Event loops
- Timer groups
- Hardware-specific synchronization

---

### Debugging RTOS

**Task Monitoring:**
- `vTaskList`: List all tasks
- `vTaskGetRunTimeStats`: Task runtime statistics
- `uxTaskGetNumberOfTasks`: Count tasks
- Task state inspection

**Stack Analysis:**
- `uxTaskGetStackHighWaterMark`: Check stack usage
- Detect stack overflow
- Adjust stack sizes

**Deadlock Detection:**
- Enable deadlock detection in config
- Timeout on mutex take
- Avoid circular dependencies

**Performance Analysis:**
- CPU utilization
- Task runtime
- Interrupt latency
- Context switch overhead

---

## Exercises

### Exercise 1: RTOS vs Bare Metal
**Objective:** Understand when to use RTOS.

**Tasks:**
1. What is the difference between bare metal and RTOS?
2. When would you choose bare metal over RTOS?
3. When would you choose RTOS over bare metal?
4. What is determinism?
5. What is the cost of using RTOS?

**Expected Outcome:** You understand RTOS use cases.

### Exercise 2: Task States
**Objective:** Understand task states.

**Tasks:**
1. What are the four task states?
2. How does a task transition between states?
3. What is context switching?
4. What is the idle task?
5. How does the scheduler choose which task to run?

**Expected Outcome:** You understand task state management.

### Exercise 3: Queues
**Objective:** Understand queue usage.

**Tasks:**
1. What is a queue used for?
2. What happens when queue is full?
3. What happens when queue is empty?
4. How do you send to a queue?
5. How do you receive from a queue?

**Expected Outcome:** You understand queue operations.

### Exercise 4: Semaphores
**Objective:** Understand semaphore usage.

**Tasks:**
1. What is a binary semaphore?
2. What is a counting semaphore?
3. How do semaphores differ from mutexes?
4. When would you use a semaphore?
5. How do you give a semaphore from ISR?

**Expected Outcome:** You understand semaphore operations.

### Exercise 5: Mutexes
**Objective:** Understand mutex usage.

**Tasks:**
1. What is a mutex used for?
2. What is priority inheritance?
3. How do mutexes differ from semaphores?
4. What is priority inversion?
5. How does mutex prevent priority inversion?

**Expected Outcome:** You understand mutex operations.

### Exercise 6: Event Groups
**Objective:** Understand event group usage.

**Tasks:**
1. What is an event group?
2. How do event groups differ from semaphores?
3. When would you use event groups?
4. How do you wait for multiple events?
5. How do you set event bits from ISR?

**Expected Outcome:** You understand event group operations.

### Exercise 7: Critical Sections
**Objective:** Understand critical sections.

**Tasks:**
1. What is a critical section?
2. When should you use critical sections?
3. What happens during critical section?
4. Why keep critical sections short?
5. Can you block in a critical section?

**Expected Outcome:** You understand critical section usage.

### Exercise 8: Race Conditions
**Objective:** Understand race conditions.

**Tasks:**
1. What is a race condition?
2. How do you prevent race conditions?
3. What is atomic operation?
4. How do mutexes prevent race conditions?
5. How do critical sections prevent race conditions?

**Expected Outcome:** You understand race condition prevention.

### Exercise 9: Deadlocks
**Objective:** Understand deadlocks.

**Tasks:**
1. What is a deadlock?
2. What are the conditions for deadlock?
3. How do you prevent deadlocks?
4. What is circular wait?
5. How do timeouts help prevent deadlocks?

**Expected Outcome:** You understand deadlock prevention.

### Exercise 10: ESP32 FreeRTOS
**Objective:** Understand ESP32 FreeRTOS specifics.

**Tasks:**
1. How many cores does ESP32 have?
2. What is task pinning?
3. How do you pin a task to a core?
4. What is tskNO_AFFINITY?
5. How do tasks communicate between cores?

**Expected Outcome:** You understand ESP32 FreeRTOS integration.

---

## Labs

### Lab 1: First Task
**Objective:** Create and run first FreeRTOS task.

**Prerequisites:**
- ESP32 development board
- ESP-IDF or Arduino with FreeRTOS

**Procedure:**

**1. Task Function:**
```c
void task1(void *pvParameters) {
    while(1) {
        printf("Task 1 running\n");
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}
```

**2. Create Task:**
```c
void app_main() {
    xTaskCreate(
        task1,
        "Task1",
        2048,
        NULL,
        1,
        NULL
    );
}
```

**3. Build and Flash:**
- Compile project
- Flash to ESP32
- Monitor serial output

**Expected Behavior:**
- Task runs continuously
- Prints every second
- No crashes

**Completion Criteria:**
- Task created successfully
- Task runs as expected
- FreeRTOS working

---

### Lab 2: Multiple Tasks
**Objective:** Create and run multiple tasks.

**Prerequisites:**
- Completed Lab 1

**Procedure:**

**1. Two Tasks:**
```c
void task1(void *pvParameters) {
    while(1) {
        printf("Task 1\n");
        vTaskDelay(500 / portTICK_PERIOD_MS);
    }
}

void task2(void *pvParameters) {
    while(1) {
        printf("Task 2\n");
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}
```

**2. Create Both Tasks:**
```c
void app_main() {
    xTaskCreate(task1, "Task1", 2048, NULL, 1, NULL);
    xTaskCreate(task2, "Task2", 2048, NULL, 1, NULL);
}
```

**3. Run:**
- Build and flash
- Monitor output

**Expected Behavior:**
- Both tasks run
- Output interleaved
- No crashes

**Completion Criteria:**
- Multiple tasks running
- Tasks scheduled correctly
- Understanding of multitasking

---

### Lab 3: Task Priorities
**Objective:** Implement task priorities.

**Prerequisites:**
- Completed Lab 2

**Procedure:**

**1. High and Low Priority Tasks:**
```c
void high_priority_task(void *pvParameters) {
    while(1) {
        printf("High priority\n");
        vTaskDelay(100 / portTICK_PERIOD_MS);
    }
}

void low_priority_task(void *pvParameters) {
    while(1) {
        printf("Low priority\n");
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}
```

**2. Create with Different Priorities:**
```c
void app_main() {
    xTaskCreate(high_priority_task, "High", 2048, NULL, 3, NULL);
    xTaskCreate(low_priority_task, "Low", 2048, NULL, 1, NULL);
}
```

**3. Observe Scheduling:**
- High priority task runs more frequently
- Low priority task starved if high priority never blocks

**Expected Behavior:**
- High priority task preempts low priority
- Priority-based scheduling observed

**Completion Criteria:**
- Task priorities working
- Preemptive scheduling observed
- Understanding of priority effects

---

### Lab 4: Queue Communication
**Objective:** Use queue for inter-task communication.

**Prerequisites:**
- Completed Lab 2

**Procedure:**

**1. Create Queue:**
```c
QueueHandle_t queue;

void producer_task(void *pvParameters) {
    int value = 0;
    while(1) {
        xQueueSend(queue, &value, portMAX_DELAY);
        printf("Sent: %d\n", value);
        value++;
        vTaskDelay(500 / portTICK_PERIOD_MS);
    }
}

void consumer_task(void *pvParameters) {
    int value;
    while(1) {
        xQueueReceive(queue, &value, portMAX_DELAY);
        printf("Received: %d\n", value);
    }
}
```

**2. Initialize:**
```c
void app_main() {
    queue = xQueueCreate(10, sizeof(int));
    xTaskCreate(producer_task, "Producer", 2048, NULL, 1, NULL);
    xTaskCreate(consumer_task, "Consumer", 2048, NULL, 1, NULL);
}
```

**Expected Behavior:**
- Producer sends data
- Consumer receives data
- Queue provides synchronization

**Completion Criteria:**
- Queue communication working
- Producer-consumer pattern implemented
- Understanding of queue blocking

---

### Lab 5: Mutex Protection
**Objective:** Use mutex to protect shared resource.

**Prerequisites:**
- Completed Lab 2

**Procedure:**

**1. Shared Resource with Mutex:**
```c
SemaphoreHandle_t mutex;
int shared_counter = 0;

void task1(void *pvParameters) {
    while(1) {
        xSemaphoreTake(mutex, portMAX_DELAY);
        shared_counter++;
        printf("Task 1: %d\n", shared_counter);
        xSemaphoreGive(mutex);
        vTaskDelay(100 / portTICK_PERIOD_MS);
    }
}

void task2(void *pvParameters) {
    while(1) {
        xSemaphoreTake(mutex, portMAX_DELAY);
        shared_counter++;
        printf("Task 2: %d\n", shared_counter);
        xSemaphoreGive(mutex);
        vTaskDelay(100 / portTICK_PERIOD_MS);
    }
}
```

**2. Initialize:**
```c
void app_main() {
    mutex = xSemaphoreCreateMutex();
    xTaskCreate(task1, "Task1", 2048, NULL, 1, NULL);
    xTaskCreate(task2, "Task2", 2048, NULL, 1, NULL);
}
```

**Expected Behavior:**
- Counter increments correctly
- No corruption
- Mutual exclusion enforced

**Completion Criteria:**
- Mutex working
- Shared resource protected
- Understanding of mutual exclusion

---

### Lab 6: Semaphore Signaling
**Objective:** Use semaphore for signaling.

**Prerequisites:**
- Completed Lab 2

**Procedure:**

**1. Binary Semaphore:**
```c
SemaphoreHandle_t semaphore;

void task1(void *pvParameters) {
    while(1) {
        xSemaphoreTake(semaphore, portMAX_DELAY);
        printf("Task 1 signaled\n");
    }
}

void task2(void *pvParameters) {
    while(1) {
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        xSemaphoreGive(semaphore);
        printf("Task 2 signaled\n");
    }
}
```

**2. Initialize:**
```c
void app_main() {
    semaphore = xSemaphoreCreateBinary();
    xTaskCreate(task1, "Task1", 2048, NULL, 1, NULL);
    xTaskCreate(task2, "Task2", 2048, NULL, 1, NULL);
    xSemaphoreGive(semaphore);  // Initial signal
}
```

**Expected Behavior:**
- Task 2 signals task 1
- Task 1 wakes on signal
- Synchronization working

**Completion Criteria:**
- Semaphore signaling working
- Task synchronization understood
- Binary semaphore usage

---

### Lab 7: Interrupt and Task
**Objective:** Use semaphore to signal task from ISR.

**Prerequisites:**
- Completed Lab 6
- Button or timer interrupt

**Procedure:**

**1. ISR Signals Task:**
```c
SemaphoreHandle_t semaphore;

void IRAM_ATTR button_isr(void* arg) {
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    xSemaphoreGiveFromISR(semaphore, &xHigherPriorityTaskWoken);
    if (xHigherPriorityTaskWoken) {
        portYIELD_FROM_ISR();
    }
}

void button_task(void *pvParameters) {
    while(1) {
        xSemaphoreTake(semaphore, portMAX_DELAY);
        printf("Button pressed\n");
    }
}
```

**2. Initialize:**
```c
void app_main() {
    semaphore = xSemaphoreCreateBinary();
    xTaskCreate(button_task, "Button", 2048, NULL, 1, NULL);
    // Configure GPIO interrupt
}
```

**Expected Behavior:**
- ISR signals task
- Task processes button press
- Deferred processing working

**Completion Criteria:**
- ISR-task communication working
- Deferred processing understood
- FromISR API usage

---

### Lab 8: Timer Task
**Objective:** Use software timer.

**Prerequisites:**
- Completed Lab 1

**Procedure:**

**1. Timer Callback:**
```c
void timer_callback(TimerHandle_t timer) {
    printf("Timer expired\n");
}
```

**2. Create Timer:**
```c
void app_main() {
    TimerHandle_t timer = xTimerCreate(
        "Timer",
        pdMS_TO_TICKS(1000),
        pdTRUE,  // Auto-reload
        0,
        timer_callback
    );
    xTimerStart(timer, 0);
    vTaskStartScheduler();
}
```

**Expected Behavior:**
- Timer expires periodically
- Callback executes
- Auto-reload working

**Completion Criteria:**
- Software timer working
- Timer callback understood
- Auto-reload understood

---

### Lab 9: Stack Monitoring
**Objective:** Monitor task stack usage.

**Prerequisites:**
- Completed Lab 2

**Procedure:**

**1. Monitor Stack:**
```c
void monitor_task(void *pvParameters) {
    UBaseType_t high_water_mark;
    while(1) {
        high_water_mark = uxTaskGetStackHighWaterMark(NULL);
        printf("Stack high water mark: %u\n", high_water_mark);
        vTaskDelay(5000 / portTICK_PERIOD_MS);
    }
}
```

**2. Create Monitor Task:**
```c
void app_main() {
    xTaskCreate(task1, "Task1", 2048, NULL, 1, NULL);
    xTaskCreate(monitor_task, "Monitor", 2048, NULL, 1, NULL);
}
```

**Expected Behavior:**
- Stack usage reported
- High water mark decreases as stack used
- No stack overflow

**Completion Criteria:**
- Stack monitoring working
- Stack sizing understood
- Stack overflow detection

---

### Lab 10: Task Statistics
**Objective:** Monitor task runtime statistics.

**Prerequisites:**
- Completed Lab 2

**Procedure:**

**1. Enable Statistics:**
```c
#define configGENERATE_RUN_TIME_STATS 1
#define configUSE_STATS_FORMATTING_FUNCTIONS 1
```

**2. Print Statistics:**
```c
void print_stats() {
    char stats_buffer[512];
    vTaskGetRunTimeStats(stats_buffer);
    printf("%s\n", stats_buffer);
}
```

**3. Periodic Reporting:**
```c
void stats_task(void *pvParameters) {
    while(1) {
        print_stats();
        vTaskDelay(10000 / portTICK_PERIOD_MS);
    }
}
```

**Expected Behavior:**
- Task runtime reported
- CPU utilization shown
- Task performance visible

**Completion Criteria:**
- Runtime statistics working
- CPU utilization understood
- Task performance analysis

---

## Project

### Project: FreeRTOS Multitask Node

**Objective:** Build a multitask embedded monitoring node using FreeRTOS.

**Requirements:**
- Sensor reading task
- Data processing task
- Communication task (MQTT/UART)
- Display/UI task (optional)
- Proper synchronization
- Resource protection
- Error handling
- Stack monitoring

**Implementation:**
- ESP32 with FreeRTOS
- I2C sensor
- MQTT or UART communication
- Queues for inter-task communication
- Mutexes for resource protection
- Semaphores for signaling

**Deliverables:**
- Working multitask system
- Architecture documentation
- Task design documentation
- Testing documentation
- Performance analysis

**Time Estimate:** 12-16 hours

**Project Structure:**
```
freertos-multitask-node/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   ├── main.c
│   ├── sensor_task.c
│   ├── processing_task.c
│   ├── communication_task.c
│   └── freertos_config.h
├── tests/
│   └── test_scenarios.md
├── docs/
│   └── architecture.md
└── results/
    └── measurements.md
```

**Note:** This project teaches RTOS system design, task decomposition, synchronization, and resource management for real-time embedded systems.

---

## Common Mistakes

### Mistake 1: Blocking in ISR
**Problem:** Calling blocking functions in ISR
**Consequence:** System hangs or crashes
**Solution:** Use FromISR APIs, defer processing to task

### Mistake 2: Not Protecting Shared Data
**Problem:** Concurrent access to shared data without protection
**Consequence:** Race conditions, corruption
**Solution:** Use mutex or critical section

### Mistake 3: Infinite Loop Without Delay
**Problem:** Task never yields CPU
**Consequence:** Starves other tasks
**Solution:** Use vTaskDelay or blocking operations

### Mistake 4: Stack Overflow
**Problem:** Stack too small for task
**Consequence:** Crash, corruption
**Solution:** Monitor stack usage, allocate sufficient stack

### Mistake 5: Priority Inversion
**Problem:** High-priority task blocked by low-priority task
**Consequence:** Missed deadlines
**Solution:** Use mutex with priority inheritance

### Mistake 6: Deadlock
**Problem:** Circular wait for resources
**Consequence:** System halts
**Solution:** Acquire locks in consistent order, use timeouts

### Mistake 7: Not Checking Return Values
**Problem:** Ignoring API return values
**Consequence:** Silent failures
**Solution:** Always check return values, handle errors

### Mistake 8: Wrong Queue Size
**Problem:** Queue too small for data rate
**Consequence:** Data loss, blocking
**Solution:** Size queue appropriately

### Mistake 9: Critical Section Too Long
**Problem:** Long critical section
**Consequence:** Missed interrupts, poor real-time performance
**Solution:** Keep critical sections very short

### Mistake 10: Not Using Tick Appropriately
**Problem:** Wrong tick rate for application
**Consequence:** Poor resolution or high overhead
**Solution:** Choose tick rate based on requirements

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is the difference between bare metal and RTOS?
2. What are the four task states?
3. What is context switching?
4. What is a queue used for?
5. What is the difference between semaphore and mutex?
6. What is priority inheritance?
7. What is a deadlock?
8. What is a critical section?
9. What is priority inversion?
10. How do you create a task in FreeRTOS?
11. What is the idle task?
12. How do you send to a queue?
13. How do you take a mutex?
14. What is a binary semaphore?
15. How do you signal from ISR?
16. What is stack overflow?
17. How do you monitor stack usage?
18. What is time slicing?
19. How do you prevent race conditions?
20. What is the tick rate?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **First Task:** Create and run simple FreeRTOS task
2. **Multiple Tasks:** Create multiple tasks with different priorities
3. **Queue Communication:** Implement producer-consumer with queue
4. **Mutex Protection:** Protect shared resource with mutex
5. **Semaphore Signaling:** Use semaphore for task synchronization
6. **ISR Signaling:** Signal task from interrupt using semaphore
7. **Software Timer:** Create and use software timer
8. **Stack Monitoring:** Monitor task stack usage
9. **Task Statistics:** Collect and display task runtime statistics
10. **Multitask System:** Design and implement multitask sensor node

**Documentation Required:**
- Task design
- Synchronization design
- Stack sizing analysis
- Performance analysis
- Test results

**Passing Criteria:** All tasks completed with proper RTOS design demonstrated.

---

## Completion Checklist

Before moving to Phase 15, verify you have:

- [ ] Understand RTOS vs bare metal
- [ ] Can create and manage FreeRTOS tasks
- [ ] Can implement task priorities
- [ ] Can use queues for communication
- [ ] Can use semaphores for synchronization
- [ ] Can use mutexes for mutual exclusion
- [ ] Can use event groups for signaling
- [ ] Can implement critical sections
- [ ] Can manage memory in RTOS
- [ ] Can debug RTOS applications
- [ ] Understand concurrency issues
- [ ] Can design deterministic systems
- [ ] Understand ESP32 FreeRTOS integration
- **Completed Lab 1** - First Task
- **Completed Lab 2** - Multiple Tasks
- **Completed Lab 3** - Task Priorities
- **Completed Lab 4** - Queue Communication
- **Completed Lab 5** - Mutex Protection
- **Completed Lab 6** - Semaphore Signaling
- **Completed Lab 7** - Interrupt and Task
- **Completed Lab 8** - Timer Task
- **Completed Lab 9** - Stack Monitoring
- **Completed Lab 10** - Task Statistics
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Completed the FreeRTOS Multitask Node project

---

## Do Not Continue Until...

**Do not start Phase 15 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can design and implement RTOS-based systems
5. You can use FreeRTOS synchronization primitives
6. You can protect shared resources
7. You can debug RTOS applications
8. You understand concurrency issues
9. You can design deterministic real-time systems
10. You can analyze RTOS performance

**RTOS is essential for complex embedded systems requiring multitasking, determinism, and resource management. Mastering FreeRTOS concepts, tasks, synchronization, and debugging is critical before learning embedded security, where concurrency and resource protection are fundamental.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 15 — Embedded Security**

Phase 15 will teach you embedded security fundamentals, threat modeling, secure communication, secure storage, and security best practices for embedded systems, building on the RTOS knowledge you have acquired.

---

**RTOS enables sophisticated embedded systems with multitasking, determinism, and modularity. Understanding RTOS concepts, proper synchronization, and resource management is essential for building reliable, maintainable, and scalable embedded applications.**
