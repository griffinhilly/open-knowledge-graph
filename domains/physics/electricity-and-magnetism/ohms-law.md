---
id: ohms-law
title: Ohm's Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-current-and-resistance
  type: hard
builds-toward:
- dc-circuits-series-parallel
- electric-power
tags:
- ohms-law
- voltage
- current
- resistance
- circuits
stage: formal-systems
status: validated
---

# Ohm's Law

## Core Idea
Ohm's law states that for many conducting materials (ohmic materials), the current through a device is proportional to the voltage across it: V = IR. The constant of proportionality R is the resistance, measured in ohms (Ω = V/A). Ohm's law is an empirical relationship, not a fundamental law — it holds for metals over a wide temperature range but breaks down for semiconductors, diodes, and other nonlinear devices.

## How It's Best Learned
Verify Ohm's law experimentally (or through simulation) by plotting V vs. I for resistors — a straight line through the origin with slope R. Then identify non-ohmic devices (LEDs, diodes) where V-I curves are nonlinear.

## Common Misconceptions
- Ohm's law is not universal; many important devices are non-ohmic.
- Voltage causes current, not the other way around — R = V/I is a definition of resistance, not a causal statement.
- Resistance does not depend on V or I for ohmic materials, but it does depend on temperature.

## Questions

```yaml
- question: "A resistor and a diode are each connected to a 5V power supply. You measure 50 mA through the resistor. You then double the voltage to 10V. What do you predict about each device?"
  type: multiple-choice
  options:
    - "Both devices will double their current to 100 mA, since all conductors follow V = IR"
    - "The resistor will double to 100 mA; the diode's current will change in a nonlinear way that cannot be predicted from V = IR alone"
    - "The resistor current is unpredictable because resistance changes with temperature; the diode will double"
    - "Neither device follows a simple rule because real circuits are always more complex than the ideal equation"
  answer: 1
  explanation: "An ohmic resistor has a constant R — doubling V doubles I exactly. A diode is non-ohmic: its V-I relationship is exponential, not linear, and current changes dramatically near a threshold voltage. You cannot calculate the diode's current from V = IR with a fixed R, because R is not fixed. The existence of non-ohmic devices is not a complication to work around — it is precisely what makes diodes useful for rectification, signal processing, and logic circuits."

- question: "The resistance of a metal wire is measured at room temperature and again when it is heated to 200°C. What does Ohm's law and the microscopic picture predict?"
  type: multiple-choice
  options:
    - "Resistance stays the same — Ohm's law says R is a constant property of the material, independent of conditions"
    - "Resistance increases — hotter ions vibrate more, causing more frequent electron scattering and reducing average drift speed"
    - "Resistance decreases — higher temperature gives electrons more kinetic energy to overcome resistance"
    - "The wire stops obeying Ohm's law at high temperatures, so no prediction is possible"
  answer: 1
  explanation: "While R is constant for ohmic materials at a fixed temperature, resistance does depend on temperature. Hotter ions vibrate more vigorously, scattering conduction electrons more frequently and reducing their average drift speed — which raises resistance. This is why incandescent bulb resistance changes dramatically from cold to operating temperature. The wire remains ohmic (its V-I graph is still a straight line) across a temperature range, but R itself is temperature-dependent. Option A confuses 'R is constant at a given temperature' with 'R is constant under all conditions.'"

- question: "In a circuit with a fixed resistor, increasing the current through the resistor causes the voltage across it to increase."
  type: true-false
  answer: false
  explanation: "This reverses the causal direction. Voltage (potential difference, maintained by a power supply or battery) drives current through the resistance. Writing R = V/I is a definition used to measure resistance from applied voltage and resulting current — not a causal statement that current causes voltage. For a fixed ohmic resistor, the ratio V/I equals R, but voltage is the cause and current is the effect. You set the voltage; the current follows from it and the resistance."

- question: "Ohm's law is a fundamental law of physics, like conservation of energy, and applies to most electrical conductors."
  type: true-false
  answer: false
  explanation: "Ohm's law is an empirical relationship — it describes the behavior of certain materials (metals, carbon resistors) under certain conditions, not a universal physical law. Semiconductors, diodes, transistors, electrolytes, and plasmas do not obey V = IR. Even for ohmic materials, the relationship is approximate: resistance depends on temperature, so extreme conditions can cause nonlinearity. The distinction matters because assuming universal applicability leads to incorrect analysis of real-world non-ohmic devices — which include nearly all the components that make modern electronics functional."

- question: "Diodes and transistors violate Ohm's law — their V-I relationships are not linear. Why is this a feature of these devices rather than a flaw?"
  type: short-answer
  answer: "A device that obeys Ohm's law with a fixed resistance can only scale current proportionally to voltage — it is a passive element with no ability to rectify, amplify, or switch. Diodes and transistors are useful precisely because they violate this linearity. A diode's threshold behavior allows it to pass current in only one direction, converting AC to DC (rectification). A transistor's nonlinear response lets a small control voltage modulate a large current — the basis of amplification and digital switching. All of modern electronics depends on non-ohmic devices; if everything were ohmic, logic gates, amplifiers, and rectifiers would be impossible."
  explanation: "The key conceptual move is recognizing that Ohm's law describes passive resistive elements, and that violation of it is precisely what enables active, functional electronic behavior. Understanding where the law applies — and why it fails where it does — is more useful than treating it as a universal rule."
```

## Explainer

You already know that current is the flow of charge and that resistance is opposition to that flow. Ohm's law, **V = IR**, says that in many materials these three quantities are locked in a simple linear relationship: double the voltage, double the current; double the resistance, halve the current. The law is deceptively simple in form but its implications ripple through every circuit you will ever analyze.

The causal direction matters. Voltage (potential difference, maintained by a battery or power supply) *drives* current through a resistance. Writing R = V/I is a *definition* of resistance from a measurement — apply V, measure I, compute R — not a statement that resistance is caused by voltage. For an ohmic material like a metal resistor, R is a constant property of the material and geometry, independent of what V or I you choose. This constancy is what it means to be ohmic: the V-I graph is a straight line through the origin, with slope equal to resistance.

The microscopic picture behind Ohm's law helps explain where it comes from and why it fails. In a metal, free electrons constantly scatter off vibrating ions. Voltage accelerates electrons between collisions, but collisions constantly reset their drift velocity. The result is a steady average drift speed proportional to the applied field — and therefore a current proportional to voltage. Temperature matters because hotter ions vibrate more, causing more frequent collisions and higher resistance. This is why real resistors heat up and why the resistance of incandescent bulbs changes dramatically from cold to operating temperature.

Ohm's law fails for many important devices. A **diode** conducts almost no current until voltage exceeds a threshold, then conducts heavily — its V-I curve is exponential, not linear. A **transistor** uses a small control signal to modulate a large current. Neither is well described by a single fixed resistance. The word "non-ohmic" is not a flaw — diodes and transistors are precisely useful *because* they violate Ohm's law. Understanding where Ohm's law applies (metal resistors, over a limited temperature range) versus where it breaks down (semiconductor devices, plasmas, superconductors) is essential for working with real circuits.
