---
id: rlc-circuits
title: RLC Circuit Applications of Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: damping-and-resonance
  type: soft
builds-toward:
- laplace-transform-of-derivatives
tags:
- application
- electrical-circuits
- modeling
stage: formal-systems
status: draft
---

# RLC Circuit Applications of Differential Equations

## Core Idea
In an RLC circuit with resistance R, inductance L, and capacitance C, Kirchhoff's voltage law gives L·i'' + R·i' + i/C = V'(t), analogous to the damped spring-mass equation. Solving this ODE predicts transient currents and steady-state response to AC sources.

## How It's Best Learned
Derive the circuit equation from Kirchhoff's laws: V_R + V_L + V_C = V_applied. Identify analogies with mechanical systems: L↔m, R↔c, 1/C↔k. Solve for underdamped and overdamped responses.

## Common Misconceptions
- Confusing voltage across the capacitor (∫i dt / C) with current; the signs matter. - Forgetting the R·i term or misinterpreting its role as energy dissipation. - Not recognizing the mechanical-electrical duality, missing intuition from one domain to the other.

## Questions

```yaml
- question: "In a series RLC circuit, resistance R is very large relative to 4L/C. What behavior does the current exhibit after the circuit is energized?"
  type: multiple-choice
  options:
    - "The current oscillates with exponentially decaying amplitude (ringing)"
    - "The current decays exponentially to zero without oscillating"
    - "The current oscillates indefinitely at the natural frequency"
    - "The current immediately reaches a steady-state constant value"
  answer: 1
  explanation: "When R² > 4L/C, the characteristic equation has two distinct real roots, corresponding to the overdamped case in the spring-mass analogy. The current decays monotonically — like a mass in thick oil that returns slowly to rest without bouncing. The oscillating (ringing) behavior occurs in the underdamped case (R² < 4L/C), where complex roots produce decaying oscillations. The duality to the mechanical system makes this intuitive once the analogy is internalized."

- question: "In the mechanical-electrical duality, which electrical component corresponds to mass in the spring-mass equation?"
  type: multiple-choice
  options:
    - "Resistance R, because both R and mass resist motion"
    - "Capacitance C, because both store energy"
    - "Inductance L, because both resist changes in their respective flow (current / velocity)"
    - "The voltage source, because it drives both systems"
  answer: 2
  explanation: "The duality maps: L (inductance) ↔ m (mass) — both resist changes in flow; R (resistance) ↔ c (damping coefficient) — both dissipate energy; 1/C ↔ k (spring constant) — both provide a restoring force proportional to accumulated displacement or charge. The equation L·i'' + R·i' + (1/C)·i = 0 is structurally identical to m·x'' + c·x' + k·x = 0. Option A is tempting because damping 'resists motion,' but mass specifically resists *changes* in velocity (inertia), and inductance specifically resists changes in current — that's the correct match."

- question: "Resonance in an RLC circuit occurs at ω₀ = 1/√(LC) because at that frequency, the inductive and capacitive impedances cancel, leaving only resistance to limit current."
  type: true-false
  answer: true
  explanation: "This is correct and is the direct electrical analog of mechanical resonance. At the natural frequency, the impedance contribution from the inductor (+jωL) and capacitor (1/jωC) have equal magnitude and opposite sign, canceling each other. Only R remains, so current amplitude is maximized. This is why radio tuning works: adjusting C changes ω₀ until it matches the broadcast frequency, maximizing the current response to that station's signal."

- question: "Increasing resistance R in a series RLC circuit will increase the maximum current amplitude at resonance."
  type: true-false
  answer: false
  explanation: "At resonance, the only impedance limiting current is the resistance R — the inductive and capacitive terms cancel. So current at resonance is V₀/R: it is inversely proportional to R. Larger R means *lower* maximum current at resonance, not higher. This is the opposite of the tempting intuition that 'more R somehow helps.' Larger R increases damping, suppresses oscillatory behavior, and reduces the sharpness (Q-factor) of the resonance peak."

- question: "Explain why the condition R² < 4L/C produces 'ringing' (oscillating current) in an RLC circuit, using the analogy to the mechanical spring-mass system."
  type: short-answer
  answer: "When R² < 4L/C, the characteristic equation Lλ² + Rλ + 1/C = 0 has complex conjugate roots, producing a solution of the form e^(–αt)cos(ωt). This is decaying oscillation: the current swings back and forth with decreasing amplitude. In the mechanical analogy, this corresponds to an underdamped spring-mass system where damping is too weak to prevent the mass from overshooting equilibrium — like a spring with light friction that bounces several times before settling. The inductance (like mass) stores energy and drives overshoot; resistance (like damping) gradually dissipates it."
  explanation: "The key is connecting the sign of the discriminant to the nature of the characteristic roots: real roots → exponential decay (overdamped); complex roots → oscillation with decay (underdamped). The mechanical analogy makes this physically intuitive — once you know what underdamped means for a spring, you immediately know what it means for a circuit."
```

## Explainer

From **second-order linear homogeneous ODEs**, you know how to solve equations of the form ay'' + by' + cy = 0 and how the nature of the characteristic roots — real and distinct, repeated, or complex conjugate — determines whether solutions decay monotonically, decay with critical damping, or oscillate. The RLC circuit is a direct physical realization of exactly this equation, letting you see those three cases play out in measurable voltages and currents.

Applying **Kirchhoff's voltage law** around a series RLC circuit says the voltage drops must sum to the applied voltage: V_R + V_L + V_C = V(t). The component voltage laws are: V_R = Ri (resistor), V_L = L·di/dt (inductor), V_C = q/C = (1/C)∫i dt (capacitor, where q is charge). Differentiating the whole equation with respect to time to work in terms of current i gives **L·i'' + R·i' + (1/C)·i = V'(t)**. This is a second-order linear ODE for i(t) with constant coefficients — precisely the form you solved abstractly, now grounded in physical components. The characteristic equation is Lλ² + Rλ + 1/C = 0.

The **mechanical-electrical duality** is the key intuition bridge. Compare L·i'' + R·i' + (1/C)·i = 0 with the damped spring-mass equation m·x'' + c·x' + k·x = 0. The correspondence is: inductance L ↔ mass m (both resist changes in their respective "flow"), resistance R ↔ damping constant c (both dissipate energy), and 1/C ↔ spring constant k (both provide a restoring force proportional to accumulated displacement or charge). The three qualitative behaviors map perfectly: an **overdamped** circuit (R² > 4L/C) has two real characteristic roots and current decays exponentially without oscillation — like a heavy mass in thick oil. An **underdamped** circuit (R² < 4L/C) has complex roots and produces **ringing** — oscillations that decay exponentially, like a plucked string. A **critically damped** circuit (R² = 4L/C) decays as fast as possible without oscillating — like a car door that closes quickly but without bouncing.

For a driven circuit with AC voltage V(t) = V₀cos(ωt), the particular solution (the **steady-state response**) has the same frequency ω as the driving voltage but may differ in amplitude and phase. **Resonance** occurs when the driving frequency matches the circuit's natural frequency ω₀ = 1/√(LC) — the same condition as mechanical resonance, for the same mathematical reason. At resonance, the impedance from the inductor and capacitor cancel, leaving only the resistance to limit current, so current amplitude is maximized. This principle underlies radio tuning: adjusting C changes ω₀ until it matches the frequency of a desired station.
