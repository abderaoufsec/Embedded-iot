# Phase 17 — STM32

> **Goal:** Develop professional MCU development skills using STM32, ARM Cortex-M architecture, and register-level programming.
>
> **Prerequisite:** Phase 16 — Cloud and Edge
>
> **Outcome:** You can develop STM32 applications using HAL, LL, or register-level programming with proper debugging and optimization.

---

## What You Will Learn

By completing this phase, you will understand:

- **STM32 Family:** STM32 families, variants, and selection criteria
- **ARM Cortex-M:** Cortex-M architecture, instruction set, modes
- **STM32 Architecture:** Bus matrix, memory map, peripherals
- **GPIO:** GPIO configuration, modes, speed, alternate functions
- **Clocks:** RCC, HSI, HSE, PLL, clock tree
- **Timers:** Basic timers, general-purpose timers, advanced timers
- **PWM:** Timer configuration, duty cycle, frequency
- **ADC:** ADC configuration, sampling, DMA
- **UART:** UART configuration, interrupts, DMA
- **SPI:** SPI configuration, master/slave mode
- **I2C:** I2C configuration, master/slave mode
- **Interrupts:** NVIC, EXTI, interrupt priorities
- **DMA:** DMA configuration, transfers, circular mode
- **Watchdog:** IWDG, WWDG configuration
- **Debugging:** SWD, ST-LINK, GDB, register inspection
- **Development Tools:** STM32CubeIDE, STM32CubeMX
- **Programming Models:** HAL, LL, register-level

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phases 0-16
- ✅ Strong C programming skills (Phase 2)
- ✅ Understanding of microcontrollers (Phase 5)
- ✅ Understanding of debugging (Phase 13)
- ✅ Understanding of RTOS (Phase 14)

**Required Hardware:**
- STM32 development board (STM32F407 Discovery recommended)
- ST-LINK debugger (included with Discovery boards)
- USB cable
- LEDs, resistors, buttons
- I2C sensor (optional)
- UART device or USB-TTL adapter

**Required Software:**
- STM32CubeIDE
- STM32CubeMX
- ST-LINK drivers

---

## Learning Outcomes

After completing this phase, you will be able to:

- Select appropriate STM32 family for application
- Understand ARM Cortex-M architecture
- Configure STM32 clock system
- Use GPIO for digital I/O
- Configure timers for PWM and delays
- Use ADC for analog measurements
- Configure UART, SPI, I2C communication
- Manage interrupts with NVIC
- Use DMA for efficient data transfer
- Configure watchdog timers
- Debug STM32 with ST-LINK and GDB
- Use STM32CubeMX for configuration
- Program with HAL, LL, or registers
- Optimize code for performance and size

---

## Why This Matters

**Professional Development:**
- STM32 is industry-standard for professional embedded systems
- ARM Cortex-M is dominant architecture
- Register-level programming required for optimization
- Professional tools and workflows

**STM32 vs ESP32:**
- **STM32:** Professional, ARM Cortex-M, extensive peripheral set, complex configuration
- **ESP32:** Wi-Fi/Bluetooth, easier to use, ESP-IDF/Arduino, hobbyist-friendly

**Programming Models:**
- **HAL:** High-level, portable, easy to use, larger code size
- **LL:** Low-level, efficient, smaller code size
- **Register-level:** Maximum control, smallest code size, requires deep understanding

**Debugging:**
- Professional debugging tools (ST-LINK, SWD)
- Register inspection
- Real-time debugging
- Performance analysis

---

## Core Concepts

### STM32 Family

**STM32 Families:**
- **STM32F0:** Cortex-M0, low-cost, basic peripherals
- **STM32F1:** Cortex-M3, classic, widely used
- **STM32F4:** Cortex-M4F, DSP, FPU, high performance
- **STM32F7:** Cortex-M7, high performance, graphics
- **STM32G0:** Cortex-M0+, cost-effective
- **STM32G4:** Cortex-M4, mixed-signal
- **STM32H7:** Cortex-M7, very high performance
- **STM32L0/L4:** Ultra-low power

**Selection Criteria:**
- Performance requirements
- Power consumption
- Peripheral requirements
- Cost
- Package size
- Development ecosystem

**STM32F407 (Learning Target):**
- Cortex-M4F at 168MHz
- 1MB Flash, 128KB SRAM
- Extensive peripherals
- Discovery board available

---

### ARM Cortex-M Architecture

**Cortex-M Core:**
- ARMv7-M architecture
- Thumb-2 instruction set
- NVIC (Nested Vectored Interrupt Controller)
- SysTick timer
- Debug support (SWD)

**Processor Modes:**
- Thread mode (normal execution)
- Handler mode (interrupts/exceptions)
- Privileged vs unprivileged access

**Registers:**
- R0-R15: General-purpose registers
- SP: Stack pointer (MSP, PSP)
- LR: Link register
- PC: Program counter
- xPSR: Program status register

**Memory Map:**
- Code region (Flash)
- SRAM regions
- Peripheral regions
- System control region

---

### STM32 Architecture

**Bus Matrix:**
- I-Code bus (instruction fetch)
- D-Code bus (data access)
- System bus (peripheral access)
- DMA buses (DMA transfers)
- Multiple masters, multiple slaves

**Memory Map:**
- 0x00000000: Code (Flash)
- 0x20000000: SRAM
- 0x40000000: Peripherals
- 0x50000000: FSMC
- 0xE0000000: Cortex-M internal

**Clock System:**
- HSI (High Speed Internal): 8MHz RC oscillator
- HSE (High Speed External): Crystal oscillator
- LSI (Low Speed Internal): 32kHz RC oscillator
- LSE (Low Speed External): 32kHz crystal
- PLL (Phase Locked Loop): Clock multiplication
- Clock tree: distributes clocks to peripherals

---

### GPIO

**GPIO Modes:**
- **Input:** Floating, pull-up, pull-down
- **Output:** Push-pull, open-drain
- **Alternate Function:** Peripheral control
- **Analog:** ADC/DAC

**GPIO Configuration:**
- Mode (input, output, alternate, analog)
- Output type (push-pull, open-drain)
- Speed (low, medium, high, very high)
- Pull-up/pull-down
- Alternate function

**GPIO Speed:**
- Low: 2MHz
- Medium: 25MHz
- High: 50MHz
- Very high: 100MHz
- Trade-off: higher speed = higher power consumption

---

### Clocks

**RCC (Reset and Clock Control):**
- Controls all clocks
- Enables/disables peripheral clocks
- Configures PLL
- Switches clock sources

**Clock Configuration:**
- Select clock source (HSI, HSE, PLL)
- Configure PLL multipliers/dividers
- Set AHB, APB1, APB2 prescalers
- Enable peripheral clocks

**System Clock:**
- Typically 168MHz for STM32F407
- Configured via PLL
- AHB clock: system clock / prescaler
- APB1 clock: AHB / prescaler (max 42MHz)
- APB2 clock: AHB / prescaler (max 84MHz)

---

### Timers

**Timer Types:**
- **Basic Timer (TIM6, TIM7):** Simple counter, no GPIO
- **General-Purpose (TIM2-5):** PWM, input capture, output compare
- **Advanced (TIM1, TIM8):** Additional features, complementary outputs

**Timer Configuration:**
- Prescaler: divides clock
- Period: auto-reload value
- Counter mode: up, down, center-aligned
- Clock division

**PWM:**
- Pulse Width Modulation
- Duty cycle = (CCR / ARR) * 100%
- Frequency = timer_clock / (PSC + 1) / (ARR + 1)

---

### ADC

**ADC Features:**
- 12-bit resolution
- Multiple channels
- Scan mode
- Continuous or single conversion
- DMA support

**ADC Configuration:**
- Resolution (12, 10, 8, 6 bits)
- Data alignment (right, left)
- Scan mode
- Continuous mode
- External trigger
- DMA enable

**ADC Conversion:**
- Sampling time
- Conversion time
- Calibration
- Voltage reference (typically 3.3V)

---

### UART

**UART Features:**
- Asynchronous communication
- Configurable baud rate
- 8N1 (8 data bits, no parity, 1 stop bit)
- TX/RX pins
- DMA support

**UART Configuration:**
- Baud rate (9600, 115200, etc.)
- Word length (8 bits)
- Stop bits (1, 2)
- Parity (none, even, odd)
- Flow control (RTS/CTS)

---

### SPI

**SPI Features:**
- Synchronous serial
- Full-duplex
- Master or slave mode
- Configurable clock polarity and phase
- DMA support

**SPI Configuration:**
- Mode (master, slave)
- Baud rate prescaler
- Clock polarity (CPOL)
- Clock phase (CPHA)
- Data frame format (8 or 16 bits)

**SPI Modes:**
- Mode 0: CPOL=0, CPHA=0
- Mode 1: CPOL=0, CPHA=1
- Mode 2: CPOL=1, CPHA=0
- Mode 3: CPOL=1, CPHA=1

---

### I2C

**I2C Features:**
- Two-wire serial (SDA, SCL)
- Multi-master
- 100kHz (standard), 400kHz (fast)
- 7-bit or 10-bit addressing
- SMBus compatible

**I2C Configuration:**
- Mode (master, slave)
- Clock speed
- 7-bit or 10-bit addressing
- Duty cycle (fast mode)
- Analog filter

---

### Interrupts

**NVIC (Nested Vectored Interrupt Controller):**
- Manages all interrupts
- Priority levels (0-15)
- Preemption priority
- Subpriority
- Interrupt nesting

**EXTI (External Interrupt/Event Controller):**
- Configures GPIO as interrupt sources
- Edge detection (rising, falling, both)
- Interrupt lines shared

**Interrupt Configuration:**
- Enable interrupt in NVIC
- Set priority
- Configure EXTI
- Write ISR

**Interrupt Priority:**
- Lower number = higher priority
- Preemption priority allows nesting
- Subpriority for same preemption level

---

### DMA

**DMA (Direct Memory Access):**
- Transfers data without CPU intervention
- Reduces CPU load
- Supports memory-to-memory, peripheral-to-memory, memory-to-peripheral

**DMA Configuration:**
- Channel selection
- Direction (peripheral-to-memory, etc.)
- Peripheral address
- Memory address
- Data size
- Circular mode
- Interrupt on completion

**DMA Streams:**
- DMA1 and DMA2 controllers
- Multiple streams per controller
- Each stream has multiple channels

---

### Watchdog

**IWDG (Independent Watchdog):**
- Uses LSI clock (32kHz)
- Windowed or standard mode
- Reset if not refreshed
- Cannot be disabled

**WWDG (Window Watchdog):**
- Uses APB clock
- Windowed mode
- Must refresh within window
- Can be disabled

**Watchdog Configuration:**
- Prescaler
- Reload value
- Window value (WWDG)
- Enable

---

### Debugging

**SWD (Serial Wire Debug):**
- 2-wire debug interface (SWCLK, SWDIO)
- Supported by ST-LINK
- Real-time debugging
- Register inspection

**ST-LINK:**
- Debug probe
- Supports SWD and JTAG
- Comes with Discovery boards
- Works with STM32CubeIDE

**GDB with ST-LINK:**
- Set breakpoints
- Step through code
- Inspect registers
- Inspect memory
- Real-time debugging

**STM32CubeIDE:**
- Integrated development environment
- Based on Eclipse
- Includes STM32CubeMX
- Includes ST-LINK GDB server

---

### STM32CubeMX

**Configuration Tool:**
- Graphical pinout and peripheral configuration
- Generates initialization code
- Supports HAL, LL
- Middleware selection

**Workflow:**
1. Select MCU
2. Configure peripherals
3. Assign pins
4. Configure clocks
5. Generate code
6. Add application code

---

### Programming Models

**HAL (Hardware Abstraction Layer):**
- High-level API
- Portable across STM32 families
- Easier to use
- Larger code size
- Example: `HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, GPIO_PIN_SET)`

**LL (Low-Level):**
- Lower-level API
- More efficient
- Smaller code size
- Requires more understanding
- Example: `LL_GPIO_SetOutputPin(GPIOA, LL_GPIO_PIN_5)`

**Register-Level:**
- Direct register access
- Maximum control
- Smallest code size
- Requires deep understanding
- Example: `GPIOA->BSRR = GPIO_BSRR_BS5;`

---

## Exercises

### Exercise 1: STM32 Family Selection
**Objective:** Understand STM32 family selection.

**Tasks:**
1. What are the main STM32 families?
2. How do you select an STM32 family?
3. What is the difference between Cortex-M0, M3, M4, M7?
4. What are the selection criteria?
5. Why is STM32F407 a good learning target?

**Expected Outcome:** You understand STM32 family selection.

### Exercise 2: ARM Cortex-M
**Objective:** Understand ARM Cortex-M architecture.

**Tasks:**
1. What is Thumb-2 instruction set?
2. What are the processor modes?
3. What is NVIC?
4. What is SysTick?
5. What is the memory map?

**Expected Outcome:** You understand Cortex-M architecture.

### Exercise 3: GPIO Configuration
**Objective:** Understand GPIO configuration.

**Tasks:**
1. What are the GPIO modes?
2. What is alternate function?
3. What is GPIO speed?
4. How do you configure pull-up/pull-down?
5. What is open-drain output?

**Expected Outcome:** You understand GPIO configuration.

### Exercise 4: Clock Configuration
**Objective:** Understand clock system.

**Tasks:**
1. What is HSI?
2. What is HSE?
3. What is PLL?
4. How do you configure system clock?
5. What are AHB and APB clocks?

**Expected Outcome:** You understand clock configuration.

### Exercise 5: Timer PWM
**Objective:** Understand timer PWM.

**Tasks:**
1. What is PWM?
2. How do you calculate PWM frequency?
3. How do you calculate duty cycle?
4. What is the difference between basic and advanced timers?
5. How do you configure PWM?

**Expected Outcome:** You understand timer PWM.

### Exercise 6: ADC Configuration
**Objective:** Understand ADC.

**Tasks:**
1. What is ADC resolution?
2. What is sampling time?
3. How do you calculate voltage from ADC value?
4. What is scan mode?
5. How do you use DMA with ADC?

**Expected Outcome:** You understand ADC configuration.

### Exercise 7: Interrupts
**Objective:** understand interrupts.

**Tasks:**
1. What is NVIC?
2. What is EXTI?
3. How do you set interrupt priority?
4. What is preemption priority?
5. How do interrupts nest?

**Expected Outcome:** You understand interrupts.

### Exercise 8: DMA
**Objective:** Understand DMA.

**Tasks:**
1. What is DMA?
2. What are DMA streams?
3. What is circular mode?
4. How do you configure DMA?
5. When should you use DMA?

**Expected Outcome:** You understand DMA.

### Exercise 9: HAL vs LL vs Registers
**Objective:** Understand programming models.

**Tasks:**
1. What is HAL?
2. What is LL?
3. What is register-level programming?
4. When would you use each?
5. What are the trade-offs?

**Expected Outcome:** You understand programming models.

### Exercise 10: Debugging
**Objective:** understand STM32 debugging.

**Tasks:**
1. What is SWD?
2. What is ST-LINK?
3. How do you use GDB with STM32?
4. What is STM32CubeIDE?
5. How do you inspect registers?

**Expected Outcome:** You understand STM32 debugging.

---

## Labs

### Lab 1: GPIO Toggle
**Objective:** Configure GPIO and toggle LED.

**Prerequisites:**
- STM32F407 Discovery board
- STM32CubeIDE

**Procedure:**

**1. STM32CubeMX Configuration:**
- Select STM32F407VG
- Configure PD12 (LED) as GPIO_Output
- Configure PD13 (LED) as GPIO_Output
- Configure PD14 (LED) as GPIO_Output
- Configure PD15 (LED) as GPIO_Output
- Generate code (HAL)

**2. Application Code:**
```c
while (1) {
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_12);
  HAL_Delay(500);
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_13);
  HAL_Delay(500);
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_14);
  HAL_Delay(500);
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_15);
  HAL_Delay(500);
}
```

**3. Build and Flash:**
- Build project
- Flash to board
- Observe LEDs

**Expected Behavior:**
- LEDs toggle sequentially
- Timing approximately correct
- No errors

**Completion Criteria:**
- GPIO configuration working
- HAL GPIO functions working
- STM32CubeIDE workflow understood

---

### Lab 2: Button Interrupt
**Objective:** Configure GPIO interrupt.

**Prerequisites:**
- Completed Lab 1

**Procedure:**

**1. STM32CubeMX Configuration:**
- Configure PA0 (User Button) as GPIO_EXTI0
- Enable EXTI interrupt
- Enable NVIC for EXTI0
- Generate code

**2. ISR Code:**
```c
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin) {
  if (GPIO_Pin == GPIO_PIN_0) {
    HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_12);
  }
}
```

**3. Build and Flash:**
- Build project
- Flash to board
- Press button

**Expected Behavior:**
- Button press toggles LED
- Interrupt working
- No bounce issues (or acceptable)

**Completion Criteria:**
- GPIO interrupt working
- EXTI configured
- NVIC configured

---

### Lab 3: Timer PWM
**Objective:** Configure timer for PWM.

**Prerequisites:**
- Completed Lab 1

**Procedure:**

**1. STM32CubeMX Configuration:**
- Configure TIM3
- Channel 1: PWM Generation CH1
- Prescaler: 83 (for 1kHz at 84MHz)
- Counter Period: 999 (for 1kHz)
- Pulse: 500 (50% duty cycle)
- Enable TIM3
- Generate code

**2. Application Code:**
```c
HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_1);

while (1) {
  for (int i = 0; i < 1000; i++) {
    __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_1, i);
    HAL_Delay(1);
  }
}
```

**3. Build and Flash:**
- Build project
- Flash to board
- Connect LED to PWM pin (or measure with oscilloscope)

**Expected Behavior:**
- PWM output working
- Duty cycle changes
- Frequency correct

**Completion Criteria:**
- Timer PWM working
- PWM configuration understood
- Duty cycle control working

---

### Lab 4: UART Communication
**Objective:** Configure UART for communication.

**Prerequisites:**
- Completed Lab 1
- USB-TTL adapter

**Procedure:**

**1. STM32CubeMX Configuration:**
- Configure USART2
- Mode: Asynchronous
- Baud Rate: 115200
- Word Length: 8 Bits
- Stop Bits: 1
- Parity: None
- Enable USART2
- Generate code

**2. Application Code:**
```c
HAL_UART_Transmit(&huart2, "Hello STM32\r\n", 13, HAL_MAX_DELAY);

while (1) {
  uint8_t rx_data;
  if (HAL_UART_Receive(&huart2, &rx_data, 1, 100) == HAL_OK) {
    HAL_UART_Transmit(&huart2, &rx_data, 1, HAL_MAX_DELAY);
  }
}
```

**3. Build and Flash:**
- Build project
- Flash to board
- Connect USB-TTL
- Test with serial terminal

**Expected Behavior:**
- UART transmits message
- UART echoes received data
- Communication reliable

**Completion Criteria:**
- UART communication working
- Baud rate correct
- Transmit and receive working

---

### Lab 5: I2C Sensor
**Objective:** Read I2C sensor.

**Prerequisites:**
- Completed Lab 1
- I2C sensor (e.g., MPU6050)

**Procedure:**

**1. STM32CubeMX Configuration:**
- Configure I2C1
- Mode: I2C
- Speed: 100kHz
- Enable I2C1
- Generate code

**2. Application Code:**
```c
#define MPU6050_ADDR 0x68 << 1

uint8_t who_am_i[] = {0x75};
uint8_t data[1];

HAL_I2C_Master_Transmit(&hi2c1, MPU6050_ADDR, who_am_i, 1, HAL_MAX_DELAY);
HAL_I2C_Master_Receive(&hi2c1, MPU6050_ADDR, data, 1, HAL_MAX_DELAY);
```

**3. Build and Flash:**
- Build project
- Flash to board
- Connect sensor
- Test

**Expected Behavior:**
- I2C communication working
- Sensor responds
- Data read correctly

**Completion Criteria:**
- I2C communication working
- Sensor reading successful
- I2C configuration understood

---

### Lab 6: SPI Communication
**Objective:** Configure SPI for communication.

**Prerequisites:**
- Completed Lab 1
- SPI device

**Procedure:**

**1. STM32CubeMX Configuration:**
- Configure SPI1
- Mode: Master
- Baud Rate Prescaler: 8
- Clock Polarity: Low
- Clock Phase: 1 Edge
- Data Size: 8 Bits
- Enable SPI1
- Generate code

**2. Application Code:**
```c
uint8_t tx_data[2] = {0x01, 0x02};
uint8_t rx_data[2];

HAL_SPI_TransmitReceive(&hspi1, tx_data, rx_data, 2, HAL_MAX_DELAY);
```

**3. Build and Flash:**
- Build project
- Flash to board
- Connect SPI device
- Test

**Expected Behavior:**
- SPI communication working
- Data transmitted and received
- Clock correct

**Completion Criteria:**
- SPI communication working
- SPI configuration understood
- Master mode working

---

### Lab 7: ADC Reading
**Objective:** Read analog value with ADC.

**Prerequisites:**
- Completed Lab 1
- Potentiometer or voltage source

**Procedure:**

**1. STM32CubeMX Configuration:**
- Configure ADC1
- Channel 0 (PA0)
- Resolution: 12 bits
- Scan Conversion Mode: Disabled
- Continuous Conversion Mode: Disabled
- Enable ADC1
- Generate code

**2. Application Code:**
```c
HAL_ADC_Start(&hadc1);

while (1) {
  HAL_ADC_PollForConversion(&hadc1, HAL_MAX_DELAY);
  uint32_t value = HAL_ADC_GetValue(&hadc1);
  float voltage = (value * 3.3) / 4095;
  HAL_Delay(100);
}
```

**3. Build and Flash:**
- Build project
- Flash to board
- Connect potentiometer
- Test

**Expected Behavior:**
- ADC reading working
- Voltage calculation correct
- Values change with potentiometer

**Completion Criteria:**
- ADC reading working
- Voltage calculation correct
- ADC configuration understood

---

### Lab 8: DMA Transfer
**Objective:** Use DMA for memory transfer.

**Prerequisites:**
- Completed Lab 1

**Procedure:**

**1. STM32CubeMX Configuration:**
- Configure DMA2
- Stream 0, Channel 0
- Memory to memory
- Mode: Normal
- Data width: Word
- Enable DMA
- Generate code

**2. Application Code:**
```c
uint32_t src_data[100];
uint32_t dst_data[100];

for (int i = 0; i < 100; i++) {
  src_data[i] = i;
}

HAL_DMA_Start_IT(&hdma_memtomem_dma2_stream0, (uint32_t)src_data, (uint32_t)dst_data, 100);
```

**3. Build and Flash:**
- Build project
- Flash to board
- Verify data transfer

**Expected Behavior:**
- DMA transfer working
- Data copied correctly
- No CPU intervention

**Completion Criteria:**
- DMA transfer working
- DMA configuration understood
- Memory-to-memory transfer

---

### Lab 9: Watchdog
**Objective:** Configure and test watchdog.

**Prerequisites:**
- Completed Lab 1

**Procedure:**

**1. STM32CubeMX Configuration:**
- Configure IWDG
- Prescaler: 256
- Reload: 4095
- Enable IWDG
- Generate code

**2. Application Code:**
```c
HAL_IWDG_Refresh(&hiwdg);

while (1) {
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_12);
  HAL_Delay(500);
  HAL_IWDG_Refresh(&hiwdg);
}
```

**3. Test:**
- Build and flash
- Remove refresh call
- Observe reset

**Expected Behavior:**
- Watchdog refresh working
- No reset when refreshing
- Reset when not refreshing

**Completion Criteria:**
- Watchdog working
- Refresh logic correct
- Reset behavior understood

---

### Lab 10: GDB Debugging
**Objective:** Debug STM32 with GDB.

**Prerequisites:**
- Completed Lab 1
- STM32CubeIDE

**Procedure:**

**1. Set Breakpoint:**
- Open source file
- Click line number to set breakpoint
- Red dot appears

**2. Debug Configuration:**
- Configure debug probe (ST-LINK)
- Set debug configuration

**3. Start Debugging:**
- Click Debug button
- GDB starts
- Breakpoint hit

**4. Debug Commands:**
- Step over (F6)
- Step into (F5)
- Continue (F8)
- Inspect variables
- View registers

**Expected Behavior:**
- GDB connects
- Breakpoints work
- Variables visible
- Registers visible

**Completion Criteria:**
- GDB debugging working
- Breakpoints working
- Variable inspection working

---

## Project

### Project: STM32 Control System

**Objective:** Build a complete STM32-based control system.

**Requirements:**
- GPIO control (LEDs, buttons)
- PWM output (motor control simulation)
- ADC input (sensor reading)
- UART communication
- I2C sensor reading
- Timer-based timing
- DMA for efficient transfers
- Watchdog for reliability
- Debugging with GDB

**Implementation:**
- STM32F407 Discovery board
- HAL or LL programming
- Multiple peripherals
- Interrupt-driven design
- State machine architecture

**Deliverables:**
- Working control system
- Architecture documentation
- Pinout documentation
- Testing documentation
- Debugging notes

**Time Estimate:** 20-24 hours

**Project Structure:**
```
stm32-control-system/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   ├── main.c
│   ├── gpio.c
│   ├── uart.c
│   ├── adc.c
│   ├── timers.c
│   └── dma.c
├── tests/
│   └── test_scenarios.md
├── docs/
│   ├── architecture.md
│   └── register_map.md
└── results/
    └── measurements.md
```

**Note:** This project teaches professional STM32 development, peripheral configuration, register-level understanding, and debugging skills.

---

## Common Mistakes

### Mistake 1: Wrong Clock Configuration
**Problem:** Clock not configured correctly
**Consequence:** Peripherals not working, wrong timing
**Solution:** Verify clock configuration in STM32CubeMX

### Mistake 2: GPIO Mode Wrong
**Problem:** GPIO configured as input instead of output
**Consequence:** No output
**Solution:** Verify GPIO mode in configuration

### Mistake 3: Not Enabling Peripheral Clock
**Problem:** Peripheral clock not enabled
**Consequence:** Peripheral not working
**Solution:** Enable peripheral clock in RCC

### Mistake 4: Wrong Interrupt Priority
**Problem:** Interrupt priority configured incorrectly
**Consequence:** Interrupts not nesting correctly
**Solution:** Understand preemption and subpriority

### Mistake 5: Not Handling Return Value
**Problem:** Ignoring HAL function return values
**Consequence:** Silent failures
**Solution:** Always check return values

### Mistake 6: DMA Not Configured
**Problem:** DMA not configured correctly
**Consequence:** Transfers fail
**Solution:** Verify DMA configuration, memory alignment

### Mistake 7: ADC Not Calibrated
**Problem:** ADC not calibrated
**Consequence:** Inaccurate readings
**Solution:** Calibrate ADC before use

### Mistake 8: Wrong Baud Rate
**Problem:** UART baud rate mismatch
**Consequence:** Garbage data
**Solution:** Match baud rate on both devices

### Mistake 9: Not Using volatile
**Problem:** Variables modified in ISR not volatile
**Consequence:** Compiler optimization breaks code
**Solution:** Use volatile for shared variables

### Mistake 10: Stack Overflow
**Problem:** Stack too small
**Consequence:** Hard fault, crashes
**Solution:** Increase stack size, monitor stack usage

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What are the main STM32 families?
2. What is the difference between Cortex-M0, M3, M4, M7?
3. What is NVIC?
4. What is the difference between HSI and HSE?
5. What is PLL?
6. What are the GPIO modes?
7. How do you calculate PWM frequency?
8. What is ADC resolution?
9. What is the difference between UART and USART?
10. What are the SPI modes?
11. What is DMA?
12. What is the difference between IWDG and WWDG?
13. What is SWD?
14. What is ST-LINK?
15. What is the difference between HAL and LL?
16. What is register-level programming?
17. What is STM32CubeMX?
18. What is EXTI?
19. How do you set interrupt priority?
20. What is the memory map?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **GPIO Toggle:** Configure and toggle GPIO
2. **Button Interrupt:** Configure GPIO interrupt
3. **Timer PWM:** Configure timer for PWM
4. **UART Communication:** Configure and use UART
5. **I2C Sensor:** Read I2C sensor
6. **SPI Communication:** Configure and use SPI
7. **ADC Reading:** Read analog value with ADC
8. **DMA Transfer:** Use DMA for memory transfer
9. **Watchdog:** Configure and test watchdog
10. **GDB Debugging:** Debug with GDB breakpoints

**Documentation Required:**
- Pinout configuration
- Clock configuration
- Peripheral configuration
- Debugging notes
- Test results

**Passing Criteria:** All tasks completed with proper STM32 development demonstrated.

---

## Completion Checklist

Before moving to Phase 18, verify you have:

- [ ] Understand STM32 family selection
- [ ] Understand ARM Cortex-M architecture
- [ ] Can configure GPIO
- [ ] Can configure clocks
- [ ] Can configure timers for PWM
- [ ] Can configure ADC
- [ ] Can configure UART, SPI, I2C
- [ ] Can manage interrupts
- [ ] Can use DMA
- [ ] Can configure watchdog
- [ ] Can debug with GDB
- [ ] Can use STM32CubeMX
- [ ] Understand HAL, LL, register-level programming
- **Completed Lab 1** - GPIO Toggle
- **Completed Lab 2** - Button Interrupt
- **Completed Lab 3** - Timer PWM
- **Completed Lab 4** - UART Communication
- **Completed Lab 5** - I2C Sensor
- **Completed Lab 6** - SPI Communication
- **Completed Lab 7** - ADC Reading
- **Completed Lab 8** - DMA Transfer
- **Completed Lab 9** - Watchdog
- **Completed Lab 10** - GDB Debugging
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Completed the STM32 Control System project

---

## Do Not Continue Until...

**Do not start Phase 18 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can configure STM32 peripherals
5. You can use STM32CubeMX for configuration
6. You can debug with GDB and ST-LINK
7. You understand ARM Cortex-M architecture
8. You can program with HAL, LL, or registers
9. You can configure clocks and timers
10. You can use DMA for efficient transfers

**STM32 is the industry standard for professional embedded development. Mastering STM32 architecture, peripheral configuration, register-level programming, and professional debugging tools is critical before learning industrial IoT concepts, where professional-grade hardware and software are essential.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 18 — Industrial IoT**

Phase 18 will teach you industrial IoT architecture, Modbus, CAN, SCADA concepts, industrial networking, and industrial security, completing the embedded systems and IoT curriculum.

---

**STM32 represents professional embedded development at scale. Understanding ARM Cortex-M architecture, peripheral configuration, register-level programming, and professional debugging tools differentiates hobbyist from professional embedded engineers.**
