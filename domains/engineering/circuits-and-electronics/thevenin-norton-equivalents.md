---
id: thevenin-norton-equivalents
title: Thevenin and Norton Equivalent Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: node-voltage-method
  type: hard
- id: superposition-theorem-circuits
  type: soft
- id: mesh-current-method
  type: soft
builds-toward:
- first-order-transient-circuits
- ac-circuit-analysis-methods
- bjt-amplifier-configurations
tags:
- thevenin
- norton
- source-transformation
- maximum-power-transfer
- equivalent-circuits
stage: formal-systems
status: validated
---

# Thevenin and Norton Equivalent Circuits

## Core Idea
Any linear two-terminal network can be replaced by a Thevenin equivalent — a single voltage source V_th in series with a resistance R_th — or a Norton equivalent — a current source I_N in parallel with R_th, where I_N = V_th / R_th. The Thevenin voltage equals the open-circuit terminal voltage and the Norton current equals the short-circuit terminal current. For circuits with only independent sources, R_th is found by deactivating all sources and computing the equivalent resistance; circuits with dependent sources require applying a test source. Maximum power is transferred to a load when R_load = R_th.

## How It's Best Learned
Practice finding Thevenin equivalents using all three methods: (1) open-circuit voltage and short-circuit current, (2) source deactivation for R_th, and (3) test-source injection. Use the test-source method whenever dependent sources are present. Verify by connecting a load and computing the load voltage two ways.

## Common Misconceptions
- Deactivating dependent sources when finding R_th — this gives incorrect results; use the test-source method.
- Confusing which terminal pair the equivalent is referenced to.
- Assuming the Thevenin equivalent preserves internal branch voltages and currents — only the external terminal behavior is preserved.
