# FreeRTOS Cheat Sheet

Quick reference for FreeRTOS concepts and API.

## Core Concepts

### Tasks
- Independent execution threads
- Each task has its own stack
- Scheduler switches between tasks
- Priority-based preemptive scheduling

### Scheduling
- **Preemptive**: Higher priority tasks preempt lower
- **Time Slicing**: Equal priority tasks share CPU
- **Cooperative**: Tasks yield voluntarily

## Task Management

### Create Task
```c
xTaskCreate(
    taskFunction,        // Task function
    "TaskName",          // Task name
    stackSize,           // Stack size (words)
    parameter,           // Task parameter
    priority,            // Priority (1- configMAX_PRIORITIES-1)
    &taskHandle          // Task handle
);
```

### Task Function Template
```c
void taskFunction(void *parameter) {
    while(1) {
        // Task code
        vTaskDelay(pdMS_TO_TICKS(100));  // Delay 100ms
    }
}
```

### Delete Task
```c
vTaskDelete(taskHandle);
vTaskDelete(NULL);  // Delete self
```

### Delay
```c
vTaskDelay(pdMS_TO_TICKS(100));     // Delay 100ms
vTaskDelayUntil(&lastWakeTime, pdMS_TO_TICKS(100));  // Periodic
```

## Synchronization

### Semaphores
```c
// Create
SemaphoreHandle_t sem = xSemaphoreCreateBinary();

// Give
xSemaphoreGive(sem);

// Take
if (xSemaphoreTake(sem, pdMS_TO_TICKS(100))) {
    // Semaphore obtained
}
```

### Mutex
```c
// Create
SemaphoreHandle_t mutex = xSemaphoreCreateMutex();

// Lock
if (xSemaphoreTake(mutex, pdMS_TO_TICKS(100))) {
    // Critical section
    xSemaphoreGive(mutex);
}
```

### Queues
```c
// Create
QueueHandle_t queue = xQueueCreate(10, sizeof(int));

// Send
xQueueSend(queue, &data, pdMS_TO_TICKS(100));

// Receive
int received;
if (xQueueReceive(queue, &received, pdMS_TO_TICKS(100))) {
    // Data received
}
```

## Task Notifications

### Send Notification
```c
xTaskNotifyGive(taskHandle);
```

### Wait for Notification
```c
ulTaskNotifyTake(pdTRUE, pdMS_TO_TICKS(100));
```

## Timers

### Create Timer
```c
TimerHandle_t timer = xTimerCreate(
    "Timer",
    pdMS_TO_TICKS(1000),  // Period
    pdTRUE,              // Auto-reload
    0,                   // Timer ID
    timerCallback        // Callback
);
```

### Start Timer
```c
xTimerStart(timer, 0);
```

### Timer Callback
```c
void timerCallback(TimerHandle_t timer) {
    // Timer expired
}
```

## Common Patterns

### Producer-Consumer
```c
// Producer
void producer(void *param) {
    int data = 42;
    xQueueSend(queue, &data, portMAX_DELAY);
}

// Consumer
void consumer(void *param) {
    int received;
    xQueueReceive(queue, &received, portMAX_DELAY);
}
```

### Mutual Exclusion
```c
if (xSemaphoreTake(mutex, portMAX_DELAY)) {
    // Critical section
    sharedResource++;
    xSemaphoreGive(mutex);
}
```

### Task Synchronization
```c
// Task 1 waits
xSemaphoreTake(syncSem, portMAX_DELAY);

// Task 2 signals
xSemaphoreGive(syncSem);
```

## Memory Management

### Stack Size
- Start with larger stacks
- Monitor stack usage
- Use `uxTaskGetStackHighWaterMark()`

### Heap
- FreeRTOS has its own heap
- Use `pvPortMalloc()` and `vPortFree()`
- Monitor heap usage with `xPortGetFreeHeapSize()`

## Troubleshooting

### Stack Overflow
- Increase stack size
- Reduce local variables
- Check for deep recursion

### Priority Inversion
- Use mutexes with priority inheritance
- Use priority ceiling protocol

### Deadlock
- Avoid circular wait
- Use timeouts
- Keep critical sections short

## Best Practices

### Task Design
- Keep tasks focused
- Use appropriate priorities
- Avoid busy-wait loops
- Use delays appropriately

### Resource Sharing
- Protect shared data with mutexes
- Use queues for data passing
- Minimize critical sections

### Memory
- Allocate memory at startup
- Avoid dynamic allocation in tasks
- Monitor stack and heap usage

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 14 - FreeRTOS.*
