---
id: diode-fundamentals
title: Diode Characteristics and Models
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: band-theory-intro
  type: soft
- id: electrical-properties-of-materials
  type: soft
- id: electrochemistry-basics
  type: soft
- id: electric-current-and-resistance
  type: soft
builds-toward:
- diode-circuit-applications
- bjt-transistor-fundamentals
- mosfet-transistor-fundamentals
tags:
- diode
- PN-junction
- I-V-characteristic
- forward-bias
- reverse-bias
- Shockley-equation
- Zener
stage: formal-systems
status: draft
---

# Diode Characteristics and Models

## Core Idea
A diode is a two-terminal semiconductor device based on a PN junction that conducts strongly in one direction (forward bias) and blocks in the other (reverse bias). Three models of increasing accuracy are commonly used: the ideal diode model (short circuit forward, open circuit reverse), the constant-voltage-drop model (0.7 V forward drop for silicon), and the Shockley equation I = I_s(e^(V/nV_T) − 1) capturing the exponential I-V relationship. Reverse breakdown (Zener effect) at a specified voltage is exploited for voltage regulation. The choice of model depends on the required accuracy and the circuit's signal levels.

## How It's Best Learned
Plot and interpret the I-V characteristic curve for a real silicon diode, noting the forward voltage threshold, the reverse leakage current, and the breakdown region. Analyze several circuits with each model and compare results to understand when simplifications are valid.

## Common Misconceptions
- Assuming a diode always drops exactly 0.7 V — this is an approximation for silicon at moderate currents; it varies with current and temperature.
- Forgetting to verify assumed on/off states after solving — an inconsistent assumption must be corrected by trying another assumption.
- Confusing Zener breakdown (engineered, controlled, reversible) with avalanche breakdown damage from exceeding the maximum rated current.
