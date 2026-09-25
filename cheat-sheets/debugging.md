# Debugging Cheat Sheet

Quick reference for debugging techniques in embedded systems.

## Systematic Debugging Process

### Debugging Methodology
1. **Reproduce** - Make the problem repeatable
2. **Isolate** - Narrow down the cause
3. **Hypothesize** - Form a theory
4. **Test** - Verify the hypothesis
5. **Fix** - Implement the solution
6. **Verify** - Confirm the fix works

## Common Debugging Tools

### Serial Debugging
```c
Serial.begin(115200);
Serial.println("Debug message");
Serial.print("Variable: ");
Serial.println(variable);
```

### LED Debugging
```c
digitalWrite(LED_PIN, HIGH);  // Indicate state
delay(100);
digitalWrite(LED_PIN, LOW);
```

### Logic Analyzer
- Capture digital signals
- Analyze protocol timing
- Verify communication

## Common Issues and Solutions

### Code Not Running
**Symptoms:** Device appears dead
**Check:**
- Power supply connected
- Reset button pressed
- Correct board selected
- Boot mode correct
- Watchdog not triggering

### GPIO Not Working
**Symptoms:** Pin not changing state
**Check:**
- Correct pin number
- Pin mode set correctly
- Pin not used by other function
- Hardware connected properly
- Pin not damaged

### Sensor Not Responding
**Symptoms:** Readings incorrect or missing
**Check:**
- Power to sensor
- Ground connection
- Communication wiring
- Correct I2C/SPI address
- Sensor initialized properly
- Timing requirements met

### Communication Failures
**Symptoms:** No data or corrupted data
**Check:**
- Baud rate match
- TX/RX cross-connection
- Ground connection
- Cable length
- Electrical noise
- Protocol timing

### Memory Issues
**Symptoms:** Crashes, weird behavior
**Check:**
- Stack overflow
- Heap fragmentation
- Array bounds
- Pointer errors
- Memory corruption

## GDB Basics

### Common GDB Commands
```bash
gdb <executable>
(gdb) break main           # Set breakpoint
(gdb) run                  # Start program
(gdb) step                 # Step into function
(gdb) next                 # Step over function
(gdb) print variable       # Print variable
(gdb) continue             # Continue execution
(gdb) backtrace            # Show call stack
(gdb) quit                 # Exit GDB
```

## Electrical Debugging

### Multimeter Checks
- **Voltage:** Measure VCC and signal levels
- **Continuity:** Check connections
- **Current:** Measure power consumption
- **Resistance:** Check pull-up/down values

### Signal Issues
- Check for noise with oscilloscope
- Verify signal levels (3.3V vs 5V)
- Check signal timing
- Look for crosstalk

## Protocol Debugging

### I2C Issues
- Use I2C scanner to find devices
- Check pull-up resistors
- Verify address
- Reduce clock speed
- Check for bus lockup

### SPI Issues
- Verify clock phase/polarity
- Check chip select timing
- Verify bit order
- Reduce clock speed
- Check signal integrity

### UART Issues
- Verify baud rate
- Check TX/RX cross-connection
- Verify data format
- Check for framing errors
- Reduce baud rate

## Performance Debugging

### Timing Issues
- Use logic analyzer
- Check interrupt latency
- Measure execution time
- Profile code sections
- Check for blocking operations

### Optimization
- Remove unnecessary delays
- Use efficient algorithms
- Minimize floating point
- Use lookup tables
- Optimize critical sections

## Common Pitfalls

### Not Testing Incrementally
- Test each component separately
- Verify hardware before software
- Start with simple code

### Ignoring Warnings
- Compiler warnings often indicate bugs
- Enable all warnings
- Fix warning messages

### Assuming Hardware Works
- Verify hardware independently
- Test with known-good code
- Check component specifications

### Not Isolating Problems
- Change one thing at a time
- Keep records of changes
- Revert if change doesn't help

## Debugging Checklist

### Before Debugging
- [ ] Power supply connected
- [ ] Ground connections made
- [ ] Components within specifications
- [ ] Code compiles without warnings
- [ ] Hardware tested independently

### During Debugging
- [ ] Problem reproducible
- [ ] Hypothesis formed
- [ ] Test planned
- [ ] Results recorded
- [ ] Changes documented

### After Fixing
- [ ] Fix verified
- [ ] No new issues introduced
- [ ] Root cause understood
- [ ] Documentation updated
- [ ] Test added to prevent regression

## Best Practices

### Code Organization
- Keep functions small
- Use meaningful names
- Add debug output
- Implement error handling
- Use assertions

### Testing
- Test boundary conditions
- Test error paths
- Use hardware-in-the-loop testing
- Automate tests when possible
- Keep test records

### Documentation
- Document debug findings
- Record solutions
- Share knowledge with team
- Update design documents
- Maintain troubleshooting guide

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 13 - Debugging.*
