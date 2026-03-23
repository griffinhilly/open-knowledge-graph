---
id: electrical-power-conceptual
title: "Electrical Power: P = IV"
domain: physics
course: conceptual-physics
prerequisites:
- id: ohms-law-conceptual
  type: hard
- id: power-concept
  type: soft
- id: electrical-energy-intro
  type: hard
builds-toward:
- electric-power
tags:
- electrical-power
- watts
stage: abstract-reasoning
status: validated
---
# Electrical Power: P = IV

## Core Idea
Electrical power is the rate at which electrical energy is converted into other forms (light, heat, motion). The formula is P = IV, where P is power in watts, I is current in amps, and V is voltage in volts. Using Ohm's Law, this can also be written as P = I²R or P = V²/R. Devices with higher power ratings use energy faster and typically produce more output (brighter light, more heat, stronger motor).

## How It's Best Learned
Read the wattage labels on different household appliances and calculate their current draw. Compare the brightness of different light bulbs using their power ratings. Calculate the cost of running appliances by converting watts to kilowatt-hours.

## Common Misconceptions
- Higher voltage always means higher power. (Power depends on both voltage and current. A high-voltage, low-current circuit might deliver less power than a low-voltage, high-current one.)
- Power and energy are the same thing. (Power is the rate of energy use. A 100 W bulb uses 100 joules per second. The total energy used depends on how long it runs.)
- A device's wattage is fixed regardless of the circuit. (A device's power consumption depends on the actual voltage and current it receives, which can change in different circuit configurations.)
- Watts only apply to electrical devices. (Watts measure any type of power — mechanical, thermal, or electrical. Electrical power just happens to be easily calculated using P = IV.)

## Questions

```yaml
- question: "A toaster draws 10 A from a 120 V outlet. What is its power consumption?"
  type: multiple-choice
  options: ["12 W", "130 W", "1,200 W", "1.2 W"]
  answer: 2
  explanation: "P = IV = 10 A × 120 V = 1,200 W (or 1.2 kW)."

- question: "Doubling the current through a fixed resistor quadruples the power dissipated."
  type: true-false
  answer: true
  explanation: "Using P = I²R, if current doubles then power = (2I)²R = 4I²R, which is four times the original power."

- question: "A 60 W light bulb is on for 2 hours. How much energy does it use in kilowatt-hours?"
  type: short-answer
  answer: "0.12 kWh, because 60 W = 0.06 kW, and 0.06 kW × 2 hours = 0.12 kWh."
  explanation: "Convert watts to kilowatts (60/1000 = 0.06 kW), then multiply by time in hours: 0.06 × 2 = 0.12 kWh."
```

## Explainer
Every electrical device you use — a phone charger, a hair dryer, a refrigerator — converts electrical energy into something useful: light, heat, motion, or computation. **Electrical power** measures how quickly this energy conversion happens. The formula is **P = IV**, where P is power in watts, I is current in amps, and V is voltage in volts.

Think of it this way: voltage tells you how much energy each unit of charge carries, and current tells you how many units of charge flow per second. Multiply them together and you get the total energy delivered per second — which is power. A device drawing 2 amps at 120 volts uses P = 2 × 120 = 240 watts, meaning it converts 240 joules of electrical energy into other forms every second.

By combining P = IV with **Ohm's Law** (V = IR), you can derive two alternative forms. Substituting V = IR into P = IV gives **P = I²R** — useful when you know current and resistance. Substituting I = V/R gives **P = V²/R** — useful when you know voltage and resistance. The P = I²R form reveals something important: power depends on current squared. This means doubling the current through a resistor does not just double the heat — it **quadruples** it. This is why overloaded circuits and bad wiring connections are fire hazards.

Your electricity bill is based on **energy**, not power. The unit is the **kilowatt-hour** (kWh), which is power times time: one kilowatt running for one hour uses 1 kWh. A 2,000 W space heater running for 3 hours uses 2 × 3 = 6 kWh. If electricity costs $0.12 per kWh, that heating session costs $0.72. Understanding power ratings helps you make informed decisions about energy use and costs.

Electrical power also explains why power lines use extremely high voltages (hundreds of thousands of volts) to transmit electricity over long distances. From P = I²R, the energy lost as heat in the wires depends on current squared. By stepping up the voltage and reducing the current (while delivering the same power, since P = IV), the energy lost in transmission drops dramatically. This insight is the reason transformers and the power grid work the way they do.
