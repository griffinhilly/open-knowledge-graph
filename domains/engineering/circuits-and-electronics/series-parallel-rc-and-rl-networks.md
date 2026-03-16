---
id: series-parallel-rc-and-rl-networks
title: Series and Parallel RC, RL, and RLC Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: resistive-networks-combinations
  type: hard
- id: capacitor-definition-properties
  type: hard
- id: inductor-definition-properties
  type: hard
builds-toward:
- sinusoidal-steady-state-analysis
- resonance-quality-factor
tags:
- rc-circuits
- rl-circuits
- rlc-circuits
- transient-response
stage: formal-systems
status: draft
---

# Series and Parallel RC, RL, and RLC Networks

## Core Idea
RC, RL, and RLC networks combine resistive and reactive elements to create frequency-dependent and transient behavior. Series RLC circuits are resonant systems with natural frequency ω₀ = 1/√(LC) and damping coefficient dependent on R. Transient response involves exponential time constants and overshoot characterized by damping ratio ζ.

## Explainer

Resistors dissipate energy without memory — their behavior is the same at every frequency and every instant. Capacitors and inductors store energy, and their voltage-current relationships involve time derivatives or integrals. This memory is what makes RC and RL circuits interesting: when conditions change suddenly (a switch closes, a voltage step is applied), the response doesn't jump to a new state instantly. Instead, it evolves over time with a characteristic **time constant** τ.

For a series **RC circuit** responding to a step voltage, the capacitor voltage climbs exponentially: V_C(t) = V_final · (1 − e^{−t/RC}). The time constant τ = RC sets the pace — after one τ the capacitor is 63% charged; after 5τ it's essentially done (99.3%). The resistor limits current, which is what slows the charging: a larger R or larger C means slower charging. The **RL circuit** is the dual: inductors resist sudden changes in current rather than voltage. Current builds as I(t) = (V/R)·(1 − e^{−t/(L/R)}) with time constant τ = L/R. A large inductance or small resistance extends the transient.

The **RLC circuit** combines both reactive elements, producing richer dynamics. The series RLC has a natural frequency ω₀ = 1/√(LC) — where inductive and capacitive effects cancel — and a **damping ratio** ζ = R/(2)·√(C/L) that determines the character of the transient. When ζ < 1 (underdamped), the response oscillates at frequency ωd = ω₀√(1 − ζ²) while decaying, like a pendulum losing energy to friction. When ζ = 1 (critically damped), the response reaches steady state as fast as possible without oscillating. When ζ > 1 (overdamped), the response decays monotonically but more slowly than the critically damped case.

These time-domain behaviors connect directly to frequency-domain analysis in your next topics. The LC natural frequency and the role of R in damping predict how the circuit filters signals: a series RLC passes frequencies near ω₀ strongly (bandpass behavior) and attenuates signals far from resonance. Every parameter you extract from the transient response — ω₀, ζ, τ — reappears in the frequency response. Time and frequency are two views of the same physics, and RLC networks are where that connection becomes concrete.
