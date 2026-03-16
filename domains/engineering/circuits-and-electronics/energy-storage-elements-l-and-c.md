---
id: energy-storage-elements-l-and-c
title: Energy Storage in Capacitors and Inductors
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: capacitor-definition-properties
  type: hard
- id: inductor-definition-properties
  type: hard
- id: power-energy-in-circuits
  type: hard
builds-toward:
- series-parallel-rc-and-rl-networks
- resonance-quality-factor
tags:
- energy-storage
- capacitive-energy
- inductive-energy
- duality
stage: formal-systems
status: draft
---

# Energy Storage in Capacitors and Inductors

## Core Idea
Capacitors store energy W_C = ½CV² in electric fields; inductors store energy W_L = ½LI² in magnetic fields. Energy storage continuity prevents instantaneous voltage changes in capacitors or current changes in inductors—a fundamental constraint on transient response. These dual elements are complementary in circuit behavior.

## Explainer

From your study of capacitors and inductors individually, you know how each element behaves: a capacitor's current is proportional to the rate of change of its voltage (i = C·dv/dt), and an inductor's voltage is proportional to the rate of change of its current (v = L·di/dt). Now we focus on what these elements actually *store* — energy — and why that stored energy imposes a hard constraint on how circuits can evolve in time.

For a **capacitor**, the stored energy is W_C = ½CV². This has a concrete physical meaning: it is the energy held in the electric field between the plates, built up by the work done to push charge against the repulsion of charges already there. To double the voltage, you must push twice as much charge against twice the electric force — the quadratic relationship W ∝ V² follows from integrating that work. For an **inductor**, the stored energy is W_L = ½LI² — the energy held in the magnetic field around the coil, built up by the work done to drive current against the back-EMF the changing current itself generates. Again the quadratic: double the current, four times the stored energy. These formulas are electromagnetic analogues of mechanical energy storage in springs (½kx²) and moving masses (½mv²), a duality that runs deep through physics and gives circuit analysis its elegance.

The crucial consequence of energy storage is the **continuity constraint**: stored energy cannot change instantaneously, because instantaneous change would require infinite power. For a capacitor, W_C = ½CV² implies that voltage cannot jump discontinuously — that would require instantaneous energy transfer, which demands infinite current. For an inductor, W_L = ½LI² implies that current cannot jump — that would require infinite voltage. These are not approximations or rules of thumb; they are exact physical consequences of finite energy. In practice, when you analyze what happens at the moment a switch opens or closes, these constraints set your initial conditions: the capacitor voltage at t = 0⁺ equals the capacitor voltage at t = 0⁻, and similarly for inductor current. The circuit's past history is encoded in its stored energy.

The **duality** between capacitors and inductors is a powerful analytical tool worth internalizing. Every statement about one element has a dual statement about the other, with voltage and current exchanged: capacitor ↔ inductor, V ↔ I, C ↔ L, charge ↔ flux, open circuit (DC steady state) ↔ short circuit (DC steady state). Once you understand one element deeply, duality gives you the other for free. This duality will become especially vivid when you study resonance: in an LC circuit, energy oscillates back and forth between the capacitor's electric field and the inductor's magnetic field at the natural frequency ω₀ = 1/√LC, exactly as kinetic and potential energy trade off in a spring-mass oscillator. The two storage elements are not just complementary — they are the circuit-theoretic realization of the same underlying physics.
