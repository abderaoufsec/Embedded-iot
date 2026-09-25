# Electronics Formulas Cheat Sheet

Quick reference for essential electronics formulas used in embedded systems.

## Basic Formulas

### Ohm's Law
```
V = I × R
I = V / R
R = V / I
```

### Power
```
P = V × I
P = I² × R
P = V² / R
```

### LED Resistor Calculation
```
R = (Vsupply - VLED) / ILED
```

## Series and Parallel

### Series Resistors
```
Rtotal = R1 + R2 + R3 + ...
```

### Parallel Resistors (2)
```
Rtotal = (R1 × R2) / (R1 + R2)
```

### Parallel Resistors (General)
```
1/Rtotal = 1/R1 + 1/R2 + 1/R3 + ...
```

## Voltage Divider
```
Vout = Vin × (R2 / (R1 + R2))
```

## RC Time Constant
```
τ = R × C
```

## Common Values

### LED Forward Voltages
- Red: ~2.0V
- Green: ~2.2V
- Blue: ~3.0V
- White: ~3.0V

### Typical LED Current
- Standard: 20mA
- High brightness: 20-30mA
- Low power: 2-10mA

### Common Resistor Values
- 220Ω, 330Ω, 470Ω, 1kΩ, 2.2kΩ, 4.7kΩ, 10kΩ

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 4 - Electronics.*
