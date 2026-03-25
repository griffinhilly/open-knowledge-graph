---
id: rc-circuits
title: RC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: kirchhoffs-rules
  type: hard
- id: capacitance
  type: hard
- id: differential-equations-intro-separable
  type: soft
- id: exponential-functions-and-graphs
  type: soft
- id: rc-transient-response
  type: soft
- id: transient-response-rc-circuits-electricity-and-magnetism
  type: soft
builds-toward:
- ac-circuits-fundamentals
- lc-and-rlc-circuits
tags:
- RC-circuit
- time-constant
- charging
- discharging
- transient
stage: formal-systems
status: validated
---
# RC Circuits

## Core Idea
An RC circuit consists of a resistor and capacitor in series. When charging, the voltage across the capacitor rises exponentially: V_C(t) = ε(1 − e^(−t/RC)). When discharging, it decays as V_C(t) = V₀ e^(−t/RC). The time constant τ = RC governs the rate — after one time constant, the capacitor reaches 63% of its final charge. After ~5τ, transient behavior is essentially complete.

## How It's Best Learned
Derive the exponential solutions from Kirchhoff's loop equation using separation of variables. Build intuition by considering limits: t → 0 (capacitor acts as wire) and t → ∞ (capacitor acts as open circuit) to check results.

## Common Misconceptions
- A fully charged capacitor blocks DC current; the current is zero at steady state, not the voltage.
- Larger R slows the charging/discharging rate; larger C also slows it.
- The time constant RC has units of seconds, not ohms or farads individually.

## Explainer

An RC circuit is the simplest example of a system with memory: unlike a pure resistor, its behavior depends not just on the present voltage but on the charge that has accumulated over time. Start with the charging problem. You connect a battery of voltage ε in series with a resistor R and a capacitor C. Kirchhoff's voltage rule (your prerequisite) gives you ε = V_R + V_C = IR + Q/C. Since I = dQ/dt, you have the first-order separable ODE: dQ/dt = (εC − Q)/(RC). The right-hand side is the "gap" between how much charge is on the capacitor and how much it will eventually hold — multiplied by the rate factor 1/RC. Separating variables and integrating gives Q(t) = Cε(1 − e^(−t/RC)), and differentiating yields the current I(t) = (ε/R)e^(−t/RC). The exponential functions you know from prerequisite work are not just convenient — they are the inevitable solution to any first-order linear ODE with a constant driving term.

The quantity **τ = RC** is the **time constant**: the single number that characterizes how quickly the circuit responds. After one time constant, the capacitor has reached 1 − e⁻¹ ≈ 63% of its final charge. After 2τ it reaches 86%; after 5τ it is within 1% of fully charged — effectively complete. Think of it like filling a bathtub: a narrow drain pipe (large R) fills slowly, and a larger tub (large C) also takes longer to fill even with the same pipe. The product RC captures both factors. The units work out: Ω × F = (V/A) × (C/V) = C/(C/s) = s — confirming τ is indeed a time.

Discharging follows exactly the same logic. Remove the battery and let the capacitor drive current through R: now V_C = V_R, so Q/C = IR = −(dQ/dt)R (the negative sign because charge is decreasing). The solution is Q(t) = Q₀e^(−t/RC) — a pure exponential decay. The two limit cases are your sanity checks: at t = 0, the capacitor acts like a battery at full voltage V₀ and drives maximum current; at t → ∞, the capacitor is empty and the current has dropped to zero. Capacitors behave like short circuits (wires) at the first instant and open circuits (breaks in the wire) at steady state — a rule of thumb that carries you far.

The RC circuit is your gateway to understanding all transient circuit behavior. The mathematical structure — an exponential approach to a new equilibrium with time constant set by component values — reappears in RL circuits (where inductance replaces capacitance), RLC oscillators, and thermal systems. Whenever you see "exponential relaxation," you are looking at a first-order system, and the time constant is the key parameter. When you extend to AC circuits, the RC circuit will reappear as a frequency-dependent voltage divider — a **low-pass filter** — because the capacitor's impedance 1/(jωC) shrinks at high frequencies, shorting them to ground while passing low-frequency signals through.

## Questions

```yaml
- question: "An RC circuit has R = 10 kΩ and C = 100 μF. What is the time constant, and how long until the capacitor reaches 95% of its final charge?"
  type: short-answer
  answer: "τ = RC = (10×10³ Ω)(100×10⁻⁶ F) = 1 s. To reach 95%: 1 − e^(−t/τ) = 0.95, so e^(−t/τ) = 0.05, t = −τ ln(0.05) ≈ 3τ = 3 s."
  explanation: "A quick rule of thumb: 1τ ≈ 63%, 2τ ≈ 86%, 3τ ≈ 95%, 5τ ≈ 99%. For most practical purposes, the circuit has 'settled' after 3–5 time constants. The logarithm gives the exact answer; the rule of thumb builds intuition for rapid estimation."

- question: "At t = 0 a fully charged capacitor (V₀ = 12 V) begins discharging through R = 3 kΩ. What is the initial current, and why does current decrease over time?"
  type: short-answer
  answer: "Initial current I₀ = V₀/R = 12/3000 = 4 mA. Current decreases because as charge flows off the capacitor, V_C falls, reducing the driving voltage and therefore the current. The decay follows I(t) = I₀e^(−t/RC)."
  explanation: "The discharging capacitor is the driving source; as it empties, it drives less current. This feedback — less charge → less voltage → less current → charge decreases more slowly — is exactly what produces exponential decay rather than linear decay."
```
