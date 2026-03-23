---
id: ideal-voltage-and-current-sources
title: Ideal Voltage and Current Sources
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: electric-potential-and-voltage
  type: hard
- id: charge-and-current-flow
  type: hard
builds-toward:
- circuit-laws-kvl-and-kcl
- thevenin-circuit-equivalent
tags:
- sources
- voltage-source
- current-source
- ideal
- dependent
stage: formal-systems
status: validated
---

# Ideal Voltage and Current Sources

## Core Idea
Ideal voltage sources maintain constant voltage independent of current drawn; ideal current sources maintain constant current independent of voltage across them. Dependent sources have their output determined by another circuit voltage or current. These idealized elements are fundamental to circuit theory, with real devices having internal impedance.

## Questions

```yaml
- question: "An ideal 9V voltage source is connected to three different resistive loads: 10Ω, 100Ω, and 1kΩ. What remains constant across all three connections?"
  type: multiple-choice
  options:
    - "The current supplied to each load (all three draw the same current)"
    - "The power delivered to each load (all three consume the same power)"
    - "The terminal voltage of the source (it stays at 9V regardless of load)"
    - "The internal resistance of the source, which adjusts to stabilize the output"
  answer: 2
  explanation: "By definition, an ideal voltage source maintains a fixed potential difference across its terminals regardless of what current the load demands. With 10Ω it supplies 0.9A (9W), with 100Ω it supplies 90mA (810mW), with 1kΩ it supplies 9mA (81mW). The current and power all differ; only the 9V terminal voltage stays constant. This is the defining property of an ideal voltage source: zero internal resistance means no voltage drop inside the source, so all of the source voltage appears at the terminals."

- question: "A 10 mA ideal current source is connected first to a 100Ω load, then to a 10kΩ load. What changes between the two configurations?"
  type: multiple-choice
  options:
    - "The current through the load (it adjusts downward to stay within the source's rating)"
    - "The voltage across the source terminals (it rises from 1V to 100V to maintain 10mA)"
    - "The internal resistance of the current source (it adjusts to deliver constant current)"
    - "Nothing changes — an ideal current source behaves identically regardless of load"
  answer: 1
  explanation: "An ideal current source enforces constant current regardless of terminal voltage. With a 100Ω load, V = IR = (10mA)(100Ω) = 1V. With a 10kΩ load, V = (10mA)(10kΩ) = 100V. The current stays at 10mA; the voltage adjusts automatically. This is the dual of a voltage source: where a voltage source holds V constant and lets I vary, a current source holds I constant and lets V vary. The current source's infinite internal resistance is what allows it to present whatever voltage the circuit requires."

- question: "An ideal current source, like an ideal voltage source, has zero internal resistance."
  type: true-false
  answer: false
  explanation: "This reverses the duality. An ideal voltage source has zero internal resistance so that no voltage drops across its internal path — all voltage appears at the terminals regardless of current. An ideal current source has infinite internal resistance so that all current is forced through the external load — none is diverted through the internal path. Infinite internal resistance means the source resists any deviation from its specified current by presenting an arbitrarily high impedance. The two are exact duals: zero vs. infinite internal resistance, fixed voltage vs. fixed current."

- question: "A real battery's terminal voltage drops as more current is drawn from it, which is why the ideal voltage source model is most accurate when the load resistance is much larger than the battery's internal resistance."
  type: true-false
  answer: true
  explanation: "A real battery is modeled as an ideal voltage source in series with a small internal resistance r. The terminal voltage is V_terminal = V_source − I × r. When load resistance R_load >> r, the current I = V_source / (R_load + r) ≈ V_source / R_load is small, and the drop I × r is negligible. The terminal voltage ≈ V_source, and the ideal model is accurate. When a large current is drawn (small load resistance), I × r becomes significant, terminal voltage sags, and the ideal model breaks down. This is why batteries feel 'weak' under heavy load."

- question: "What is a dependent source, and why must circuit analysis methods account for dependent sources when modeling transistors and operational amplifiers?"
  type: short-answer
  answer: "A dependent (controlled) source has its output — voltage or current — set by another voltage or current elsewhere in the circuit, rather than being a fixed value. There are four types: voltage-controlled voltage source (VCVS), current-controlled voltage source (CCVS), voltage-controlled current source (VCCS), and current-controlled current source (CCCS). Transistors and op-amps are modeled using dependent sources because their behavior is inherently relational: a BJT's collector current is proportional to its base-emitter voltage (a VCCS with transconductance g_m), and an op-amp's output voltage is proportional to its differential input voltage (a VCVS with high gain). Without dependent sources, there is no way to represent amplification — the defining property of active devices."
  explanation: "This is why dependent sources are not a theoretical curiosity but the bridge between passive circuit analysis and electronics. Nodal and mesh analysis methods apply unchanged with dependent sources, but the dependent source's controlling quantity must be expressed in terms of node voltages or mesh currents — adding an algebraic constraint that ties parts of the circuit together. Mastering this is the prerequisite for analyzing any amplifier circuit."
```

## Explainer

From your study of electric potential and current flow, you know that voltage is the energy per unit charge driving current around a circuit, and that current is the rate of charge movement. Sources are the elements that supply this energy — they are the "pumps" that push charge through the network. Understanding ideal sources precisely is essential because every circuit analysis method (KVL, KCL, Thévenin equivalents, node voltage, mesh current) assumes you can characterize sources exactly.

An **ideal voltage source** enforces a fixed potential difference across its terminals, regardless of how much current flows through it. Imagine a 9V battery that stays at exactly 9V whether you connect a 1 kΩ resistor (drawing 9 mA) or a 10 Ω resistor (drawing 0.9 A) — the voltage never wavers. The source simply supplies whatever current the external circuit demands to maintain that voltage. This means an ideal voltage source has **zero internal resistance**: no energy is lost inside it, and no voltage drops across it internally. In practice, every real source has some internal resistance (a battery has internal resistance of a few tenths of an ohm), and its terminal voltage sags as more current is drawn. The ideal model is accurate when the load resistance is much larger than the internal resistance.

An **ideal current source** is the dual: it enforces a fixed current through itself, regardless of the voltage that appears across its terminals. A 2 mA ideal current source pushes exactly 2 mA through the circuit whether the load is 100 Ω or 10 kΩ — the voltage across it adjusts automatically to whatever the circuit requires. An ideal current source has **infinite internal resistance**: it resists any change in current by presenting an arbitrarily high impedance. Real approximations include transistor circuits biased to behave as nearly constant current sources. Voltage and current sources are duals of each other — every property of one has a mirror-image statement for the other, and Thévenin's theorem (voltage source + series resistance) and Norton's theorem (current source + parallel resistance) formalize this duality.

**Dependent sources** (also called controlled sources) are a distinct and important category. Unlike independent sources whose output is fixed, a dependent source's output is proportional to some other voltage or current elsewhere in the circuit. There are four types: voltage-controlled voltage source (VCVS, output voltage = μ·v_x), current-controlled voltage source (CCVS), voltage-controlled current source (VCCS, output current = g_m·v_x), and current-controlled current source (CCCS, output current = β·i_x). These models are not exotic abstractions — they are the circuit-theoretic representations of active devices. A BJT's collector current g_m·v_be is a VCCS. An op-amp's output is modeled as a VCVS with very high gain. Mastery of dependent sources is the bridge between passive circuit analysis and electronic amplifier design; you cannot analyze transistor circuits without them.
