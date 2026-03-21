---
id: rc-transient-response
title: Transient Response in RC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dc-circuit-analysis
  type: hard
builds-toward:
- rl-transient-response
tags:
- rc-circuit
- transient
- time-constant
stage: formal-systems
status: draft
---

# Transient Response in RC Circuits

## Core Idea
In an RC circuit, capacitor charge evolves as Q(t) = Q₀(1 − e^(−t/τ)) during charging and Q(t) = Q₀e^(−t/τ) during discharging, where τ = RC is the time constant. Current decays exponentially: I(t) = (V/R)e^(−t/τ). The time constant characterizes the speed of charge redistribution; larger R or C gives slower response.

## Questions

```yaml
- question: "An RC circuit is charging through a resistor R. The resistor is then replaced with one of twice the resistance (2R) while the capacitor and battery voltage remain the same. What happens to the final charge on the capacitor and the time to reach it?"
  type: multiple-choice
  options:
    - "The final charge doubles because the larger resistor pushes more charge."
    - "The final charge is unchanged, but the time to charge increases."
    - "Both the final charge and the charging time double."
    - "The final charge halves because less current can flow."
  answer: 1
  explanation: "The final equilibrium charge Q = CV depends only on capacitance and battery voltage — resistance doesn't affect how much charge accumulates, only how quickly. However, the time constant τ = RC doubles when R doubles, so the charging process takes twice as long. This is a key misconception: people conflate the rate of charging with the amount of charging."

- question: "At t = 2τ into the charging process, approximately what fraction of the capacitor's final charge has accumulated?"
  type: multiple-choice
  options:
    - "About 50% — it's halfway through the charging process."
    - "About 63% — one time constant has passed so it's 63% charged."
    - "About 86% — since Q(t) = Q₀(1 − e^(−t/τ)), at t=2τ this gives 1 − e^(−2) ≈ 0.86."
    - "About 99% — five time constants have nearly elapsed."
  answer: 2
  explanation: "Q(t)/Q_final = 1 − e^(−t/τ). At t = 2τ: 1 − e^(−2) ≈ 1 − 0.135 = 0.865. The 63% figure applies at exactly t = τ (one time constant). After 5τ, the capacitor is within 1% of full charge. Understanding the formula means you can evaluate it at any time — not just memorize the one-time-constant benchmark."

- question: "After 5 time constants (t = 5τ), a charging capacitor has reached more than 99% of its final charge."
  type: true-false
  answer: true
  explanation: "At t = 5τ: Q/Q_final = 1 − e^(−5) ≈ 1 − 0.0067 = 0.993, or about 99.3%. This is why 5τ is treated as 'effectively complete' in practice. The exponential never truly reaches 100%, but the remaining gap becomes negligible for engineering purposes after 5 time constants."

- question: "When charging a capacitor through a resistor, the current through the circuit remains approximately constant until the capacitor is almost fully charged, then drops rapidly."
  type: true-false
  answer: false
  explanation: "The current decays exponentially from the very first instant: I(t) = (V/R)e^(−t/τ). At t = 0, all the voltage appears across the resistor (the uncharged capacitor looks like a short), giving maximum current I₀ = V/R. As charge builds on the capacitor, it 'uses up' more of the battery voltage, leaving less for the resistor and reducing current continuously. The drop is gradual and exponential, not sudden near the end."

- question: "Why does the charging current in an RC circuit decrease over time as the capacitor accumulates charge?"
  type: short-answer
  answer: "As charge accumulates on the capacitor, the voltage across it increases. By Kirchhoff's voltage law, the voltage across the resistor equals the battery voltage minus the capacitor voltage. As the capacitor voltage rises, less voltage remains for the resistor, and by Ohm's law (I = V_R/R), less current flows. This is a self-limiting feedback: more charge → higher capacitor voltage → less current → slower charging."
  explanation: "The exponential decay of current is the mathematical signature of this negative feedback. The system is governed by RC(dV_C/dt) = V - V_C: the rate of charging is proportional to how far the capacitor is from its final voltage. This same mathematical structure — restoring rate proportional to displacement — appears in Newton's cooling law, radioactive decay, and many other natural phenomena."
```

## Explainer

From your DC circuit analysis, you know that a capacitor stores charge Q = CV and blocks steady-state current in equilibrium. But what happens between the instant you connect a capacitor to a voltage source and the moment it reaches equilibrium? That interval — the **transient response** — is governed by the interplay between R and C.

Consider charging a capacitor from a battery of voltage V through a resistor R. At the instant the circuit closes (t = 0), the capacitor is uncharged, so it looks like a wire: all the voltage appears across R and the initial current is I₀ = V/R. As charge accumulates on the capacitor, the voltage across it grows, leaving less voltage for the resistor, which reduces the current. Less current means slower charging. The process is self-limiting: the more charge on the capacitor, the harder it is to add more. This feedback is described by the differential equation RC(dV_C/dt) + V_C = V, whose solution is V_C(t) = V(1 − e^(−t/τ)) with **τ = RC** the time constant. The charge follows the same shape: Q(t) = CV(1 − e^(−t/τ)).

The **time constant τ** is the single most important quantity in RC transient analysis. After one time constant, the capacitor has reached about 63% of its final charge (since 1 − e^(−1) ≈ 0.63); after 5τ, it is within 1% of fully charged — effectively complete. A large R means current flows slowly, so charging takes longer. A large C means more charge must be delivered to reach a given voltage, again slowing the process. Both increase τ = RC proportionally.

Discharging is the mirror image. If a fully charged capacitor (initial charge Q₀) is connected to a resistor with the battery removed, the excess charge drives a current that exponentially drains the capacitor: Q(t) = Q₀ e^(−t/τ). The current starts at I₀ = V₀/R and decays at the same rate. In both cases, the exponential curve is the signature of a system with a restoring rate proportional to its displacement from equilibrium — the same mathematical form as Newton's cooling law, population decay, and countless other natural processes. Recognizing this exponential fingerprint and reading off τ from a graph is a core skill that extends directly to RL circuits and, later, to resonant LC circuits.
