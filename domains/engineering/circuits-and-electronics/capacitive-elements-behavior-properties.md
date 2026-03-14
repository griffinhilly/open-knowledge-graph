---
id: capacitive-elements-behavior-properties
title: 'Capacitive Elements: Behavior and Properties'
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-element-types-and-definitions
  type: hard
builds-toward:
- rc-circuit-charging-and-discharging
- rlc-circuit-transient-analysis-overview
- complex-impedance-networks-ac
tags:
- capacitors
- energy-storage
- reactive-elements
stage: formal-systems
status: draft
---

# Capacitive Elements: Behavior and Properties

## Core Idea
A capacitor stores electrical energy in an electric field; its capacitance C relates charge Q to voltage: Q = CV. The current through a capacitor is proportional to the rate of change of voltage: i = C(dv/dt). Capacitors act as open circuits to DC steady state but pass AC signals; they oppose sudden voltage changes.

## How It's Best Learned
Build simple RC circuits and observe charging with a meter or oscilloscope. Derive the differential equation for charging from first principles using Kirchhoff's voltage law and the definition of capacitive current.

## Common Misconceptions
- Capacitors pass DC current; they only pass transients. - A capacitor acts as a short circuit; it has impedance that depends on frequency. - Capacitance is always positive and independent of frequency for ideal capacitors.
