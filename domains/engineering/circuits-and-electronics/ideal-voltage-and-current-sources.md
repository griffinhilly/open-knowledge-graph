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
status: draft
---

# Ideal Voltage and Current Sources

## Core Idea
Ideal voltage sources maintain constant voltage independent of current drawn; ideal current sources maintain constant current independent of voltage across them. Dependent sources have their output determined by another circuit voltage or current. These idealized elements are fundamental to circuit theory, with real devices having internal impedance.

## Explainer

From your study of electric potential and current flow, you know that voltage is the energy per unit charge driving current around a circuit, and that current is the rate of charge movement. Sources are the elements that supply this energy — they are the "pumps" that push charge through the network. Understanding ideal sources precisely is essential because every circuit analysis method (KVL, KCL, Thévenin equivalents, node voltage, mesh current) assumes you can characterize sources exactly.

An **ideal voltage source** enforces a fixed potential difference across its terminals, regardless of how much current flows through it. Imagine a 9V battery that stays at exactly 9V whether you connect a 1 kΩ resistor (drawing 9 mA) or a 10 Ω resistor (drawing 0.9 A) — the voltage never wavers. The source simply supplies whatever current the external circuit demands to maintain that voltage. This means an ideal voltage source has **zero internal resistance**: no energy is lost inside it, and no voltage drops across it internally. In practice, every real source has some internal resistance (a battery has internal resistance of a few tenths of an ohm), and its terminal voltage sags as more current is drawn. The ideal model is accurate when the load resistance is much larger than the internal resistance.

An **ideal current source** is the dual: it enforces a fixed current through itself, regardless of the voltage that appears across its terminals. A 2 mA ideal current source pushes exactly 2 mA through the circuit whether the load is 100 Ω or 10 kΩ — the voltage across it adjusts automatically to whatever the circuit requires. An ideal current source has **infinite internal resistance**: it resists any change in current by presenting an arbitrarily high impedance. Real approximations include transistor circuits biased to behave as nearly constant current sources. Voltage and current sources are duals of each other — every property of one has a mirror-image statement for the other, and Thévenin's theorem (voltage source + series resistance) and Norton's theorem (current source + parallel resistance) formalize this duality.

**Dependent sources** (also called controlled sources) are a distinct and important category. Unlike independent sources whose output is fixed, a dependent source's output is proportional to some other voltage or current elsewhere in the circuit. There are four types: voltage-controlled voltage source (VCVS, output voltage = μ·v_x), current-controlled voltage source (CCVS), voltage-controlled current source (VCCS, output current = g_m·v_x), and current-controlled current source (CCCS, output current = β·i_x). These models are not exotic abstractions — they are the circuit-theoretic representations of active devices. A BJT's collector current g_m·v_be is a VCCS. An op-amp's output is modeled as a VCVS with very high gain. Mastery of dependent sources is the bridge between passive circuit analysis and electronic amplifier design; you cannot analyze transistor circuits without them.
