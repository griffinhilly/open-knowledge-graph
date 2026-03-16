---
id: transient-response-rlc-circuits
title: Transient Response in RLC Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: transient-response-rc-circuits
  type: hard
- id: transient-response-rl-circuits
  type: hard
builds-toward:
- series-resonance-characteristics
- parallel-resonance-characteristics
- quality-factor-bandwidth-tradeoff
tags:
- transients
- rlc-circuits
- damping
- oscillations
stage: formal-systems
status: draft
---

# Transient Response in RLC Circuits

## Core Idea
RLC circuits exhibit three response modes depending on damping: underdamped (oscillatory), critically damped (fastest non-oscillatory), and overdamped (slow non-oscillatory). The response depends on the damping ratio ζ = R/(2√(L/C)). Understanding RLC transients is essential for pulse response, switching transients, and designing circuits that avoid unwanted oscillations.

## How It's Best Learned
Simulate or build an RLC circuit and observe step response for different resistance values. Start with heavy damping and gradually reduce it to see the transition from overdamped to critically damped to underdamped oscillations.

## Common Misconceptions
Students often think oscillation is always bad or that critical damping is the 'best' response. In reality, some applications prefer underdamped response for faster settling, while others need overdamped response to avoid overshoot.

## Explainer

From your RC and RL circuit work, you know how a first-order circuit responds to a sudden change: it approaches a new steady state exponentially with a single time constant τ. Adding a second energy-storing element creates a second-order system that can do something qualitatively new — **oscillate**. Energy can slosh back and forth between the electric field of the capacitor and the magnetic field of the inductor. The resistor's job is to dissipate that energy. How fast it dissipates determines whether the circuit rings, settles cleanly, or creeps sluggishly to its final value.

The character of the response depends entirely on the **damping ratio** ζ = R/(2√(L/C)). Think of ζ as the ratio of resistive dissipation to reactive energy storage. When ζ < 1 the system is **underdamped**: oscillations are present and decay gradually — like a plucked guitar string or a spring released underwater. The output overshoots its final value, rings back through it, and eventually settles. When ζ = 1 the system is **critically damped**: it reaches its final value as quickly as possible without any overshoot — mathematically, the two poles of the system merge on the negative real axis. When ζ > 1 the system is **overdamped**: it approaches its final value slowly and monotonically, like a door-closing mechanism in thick oil, because the two poles are distinct real values far from the imaginary axis.

The **natural frequency** ω_n = 1/√(LC) sets the time scale of the response. For an underdamped system, the actual oscillation frequency is the **damped natural frequency** ω_d = ω_n√(1 − ζ²), which is always slightly below ω_n. The complete step response of an underdamped RLC circuit is an exponentially decaying sinusoid: a sinusoid at frequency ω_d inside a decaying envelope e^{−ζω_n t}. In the complex s-plane, the two poles sit at s = −ζω_n ± jω_d. Purely imaginary poles (ζ = 0, no resistance) give undamped oscillation. Poles on the negative real axis (ζ ≥ 1) give overdamped or critically damped decay. Poles in the right half-plane would mean growing oscillation — an unstable circuit.

The design implications are concrete and application-driven. A servo motor driver typically targets slight underdamping (ζ ≈ 0.7) to position quickly without overshoot that could damage tooling. A radio receiver's resonant tank circuit is intentionally underdamped (ζ ≪ 1, high Q) so it rings strongly at the desired frequency and rejects nearby ones. A power supply output filter must be overdamped so switching transients decay smoothly without oscillating onto the output rail. Choosing the right damping for an RLC circuit is therefore an engineering decision driven by application requirements — not a question of which mode is intrinsically better.
