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
status: validated
---

# Energy Storage in Capacitors and Inductors

## Core Idea
Capacitors store energy W_C = ½CV² in electric fields; inductors store energy W_L = ½LI² in magnetic fields. Energy storage continuity prevents instantaneous voltage changes in capacitors or current changes in inductors—a fundamental constraint on transient response. These dual elements are complementary in circuit behavior.

## Questions

```yaml
- question: "A capacitor is charged to 10V and connected in a circuit via a switch. At t=0, the switch closes. What is the capacitor voltage at t=0⁺ (immediately after closing)?"
  type: multiple-choice
  options:
    - "0V — the circuit demands current flow, which instantly redistributes the charge"
    - "10V — capacitor voltage cannot change instantaneously because that would require infinite power"
    - "5V — voltage splits evenly between the capacitor and the rest of the circuit"
    - "It depends on the resistance in the circuit — with zero resistance, voltage drops to zero"
  answer: 1
  explanation: "Capacitor voltage cannot change instantaneously. The energy stored is W_C = ½CV², and changing voltage instantly would require instantaneous energy transfer, which demands infinite power (P = dW/dt). Therefore, the capacitor voltage at t=0⁺ equals the voltage at t=0⁻ = 10V. This is the initial condition for transient analysis. Option D contains a subtlety: with zero resistance, you get a theoretical contradiction — the math breaks down, but physically it just means the transition is extremely fast, not truly instantaneous. In practice, all real circuits have some resistance."

- question: "Which statement correctly captures the duality between capacitors and inductors with respect to their continuity constraints?"
  type: multiple-choice
  options:
    - "Both capacitor voltage and inductor current can change instantaneously if the applied voltage or current is large enough"
    - "Capacitor voltage cannot change instantaneously; inductor current cannot change instantaneously — both because stored energy cannot change instantaneously"
    - "Capacitor current cannot change instantaneously; inductor voltage cannot change instantaneously"
    - "Capacitors resist current changes; inductors resist voltage changes"
  answer: 1
  explanation: "The continuity constraints follow directly from energy storage: W_C = ½CV² means voltage cannot jump (that would require infinite current through C = i/(dV/dt)); W_L = ½LI² means current cannot jump (that would require infinite voltage across L = V/(dI/dt)). Option C swaps which quantity is continuous — current through a capacitor CAN change instantly, and voltage across an inductor CAN change instantly; it's voltage across C and current through L that are continuous. Option D inverts the mapping between element and quantity."

- question: "When a switch suddenly opens in a series circuit containing an inductor carrying 2A, the current through the inductor immediately drops to zero."
  type: true-false
  answer: false
  explanation: "Inductor current cannot change instantaneously because W_L = ½LI² — instantaneous change requires infinite power. When the switch opens, the inductor 'fights' to maintain its current. With no path for current to flow through the switch, the inductor generates a very large voltage spike (sometimes thousands of volts) to drive current through whatever path exists — this is why opening inductive circuits without a protection diode or snubber can destroy switches and components. The current does eventually decay to zero, but through a transient process, not instantaneously."

- question: "The energy stored in a capacitor increases quadratically with voltage: doubling the voltage quadruples the stored energy."
  type: true-false
  answer: true
  explanation: "W_C = ½CV², so doubling V (V → 2V) gives W = ½C(2V)² = 4 × ½CV². The stored energy quadruples. This quadratic relationship arises because to push more charge onto the capacitor, you must work against the increasing electric field created by the charge already there — the work required per additional charge scales with the voltage, which itself scales with charge. The same quadratic appears in W_L = ½LI² for inductors and in mechanical energy storage: W_spring = ½kx² and W_kinetic = ½mv², all following from integrating a force (or voltage) that itself grows with displacement (or current)."

- question: "Why can't a capacitor's voltage change instantaneously? Explain using energy storage principles rather than just citing the formula i = C·dv/dt."
  type: short-answer
  answer: "A capacitor stores energy W_C = ½CV² in its electric field. If the voltage were to change instantaneously — say from V₁ to V₂ in zero time — the stored energy would change from ½CV₁² to ½CV₂² in zero time. Power is P = dW/dt; dividing a finite energy change by zero time gives infinite power. No physical circuit can supply or absorb infinite power, so instantaneous voltage change is physically impossible. The circuit's past history (what voltage was stored before t=0) therefore completely determines the initial condition for any transient that follows — the capacitor voltage at t=0⁺ always equals the voltage at t=0⁻."
  explanation: "The energy-based argument is more fundamental than the formula i = C·dv/dt. The formula says instantaneous voltage change requires infinite current, which is true — but the deeper reason is that you cannot transfer infinite power. Understanding this connects the circuit constraint to a universal physical principle: conservation of energy and the finite rate at which energy can be transferred. The same argument applies to inductors with current: instantaneous current change would require infinite power into the magnetic field."
```

## Explainer

From your study of capacitors and inductors individually, you know how each element behaves: a capacitor's current is proportional to the rate of change of its voltage (i = C·dv/dt), and an inductor's voltage is proportional to the rate of change of its current (v = L·di/dt). Now we focus on what these elements actually *store* — energy — and why that stored energy imposes a hard constraint on how circuits can evolve in time.

For a **capacitor**, the stored energy is W_C = ½CV². This has a concrete physical meaning: it is the energy held in the electric field between the plates, built up by the work done to push charge against the repulsion of charges already there. To double the voltage, you must push twice as much charge against twice the electric force — the quadratic relationship W ∝ V² follows from integrating that work. For an **inductor**, the stored energy is W_L = ½LI² — the energy held in the magnetic field around the coil, built up by the work done to drive current against the back-EMF the changing current itself generates. Again the quadratic: double the current, four times the stored energy. These formulas are electromagnetic analogues of mechanical energy storage in springs (½kx²) and moving masses (½mv²), a duality that runs deep through physics and gives circuit analysis its elegance.

The crucial consequence of energy storage is the **continuity constraint**: stored energy cannot change instantaneously, because instantaneous change would require infinite power. For a capacitor, W_C = ½CV² implies that voltage cannot jump discontinuously — that would require instantaneous energy transfer, which demands infinite current. For an inductor, W_L = ½LI² implies that current cannot jump — that would require infinite voltage. These are not approximations or rules of thumb; they are exact physical consequences of finite energy. In practice, when you analyze what happens at the moment a switch opens or closes, these constraints set your initial conditions: the capacitor voltage at t = 0⁺ equals the capacitor voltage at t = 0⁻, and similarly for inductor current. The circuit's past history is encoded in its stored energy.

The **duality** between capacitors and inductors is a powerful analytical tool worth internalizing. Every statement about one element has a dual statement about the other, with voltage and current exchanged: capacitor ↔ inductor, V ↔ I, C ↔ L, charge ↔ flux, open circuit (DC steady state) ↔ short circuit (DC steady state). Once you understand one element deeply, duality gives you the other for free. This duality will become especially vivid when you study resonance: in an LC circuit, energy oscillates back and forth between the capacitor's electric field and the inductor's magnetic field at the natural frequency ω₀ = 1/√LC, exactly as kinetic and potential energy trade off in a spring-mass oscillator. The two storage elements are not just complementary — they are the circuit-theoretic realization of the same underlying physics.
