---
id: maximum-power-transfer
title: Maximum Power Transfer Theorem
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: thevenin-circuit-equivalent
  type: hard
- id: power-energy-in-circuits
  type: hard
builds-toward:
- sinusoidal-steady-state-analysis
tags:
- maximum-power
- impedance-matching
- power-transfer
stage: formal-systems
status: draft
---

# Maximum Power Transfer Theorem

## Core Idea
Maximum power is delivered to a load when load resistance equals the Thévenin resistance of the source (impedance matching condition). The maximum power available is P_max = V_th²/(4R_th). This result is important for signal transmission systems, though maximum efficiency (R_load >> R_source) is preferred in power delivery applications.

## Questions

```yaml
- question: "A radio transmitter has a Thévenin resistance of 50 Ω. An antenna matching network is being designed to extract maximum signal power from this source. What load resistance should be presented?"
  type: multiple-choice
  options:
    - "0 Ω — minimum resistance maximizes current and therefore power to the load"
    - "50 Ω — matching the load resistance to the source resistance maximizes power transfer"
    - "∞ Ω — maximum load resistance prevents power from being wasted in source resistance"
    - "100 Ω — twice the source resistance avoids the matched-condition efficiency loss"
  answer: 1
  explanation: "The Maximum Power Transfer Theorem: P_L is maximized when R_L = R_th. At R_L = 0, you short the output and deliver zero power to the load. At R_L → ∞, current → 0 and power → 0. The maximum falls between these extremes at R_L = R_th, yielding P_max = V_th²/(4R_th). For signal/communication systems, extracting maximum signal energy from the source is the priority — impedance matching achieves this even though efficiency is only 50%."

- question: "A power utility delivers electricity to homes. Should it design transmission to satisfy the maximum power transfer condition (R_load = R_source)?"
  type: multiple-choice
  options:
    - "Yes — maximum power transfer ensures consumers receive as much electricity as possible"
    - "No — the matched condition wastes 50% of generated power in source resistance; utilities want R_load >> R_source for high efficiency"
    - "Yes — impedance matching is always the optimal condition in electrical engineering"
    - "No — impedance matching applies only to AC complex impedances, not DC power delivery"
  answer: 1
  explanation: "Maximum power transfer and maximum efficiency are fundamentally different goals. At the matched condition (R_L = R_th), exactly half the power is dissipated in the source resistance — efficiency is only 50%. For a power utility, wasting half of generated electricity in transmission resistance would be economically catastrophic. Power systems operate with R_load >> R_source (achieved partly through high-voltage transmission), reaching efficiencies far above 50%. Maximum power transfer is right for signal systems; maximum efficiency is right for power delivery. This is the central engineering tension the theorem reveals."

- question: "At the maximum power transfer condition (R_L = R_th), the power dissipated in the source resistance equals the power delivered to the load — efficiency is exactly 50%."
  type: true-false
  answer: true
  explanation: "When R_L = R_th, the two equal resistances in series share voltage equally. The same current flows through both, so they dissipate equal power: P_source = P_load = V_th²/(4R_th). This 50% efficiency is an inherent consequence of the matched condition, not a flaw to be engineered away. It's why this condition is chosen for signal extraction (where maximum power to the load matters) rather than power delivery (where losing half to source resistance is unacceptable)."

- question: "Maximum power is always delivered to a load when the load resistance is as small as possible, since lower resistance allows more current to flow."
  type: true-false
  answer: false
  explanation: "This intuition is wrong. Power to the load is P_L = I²R_L = V_th²·R_L/(R_th + R_L)². As R_L decreases from large values, current increases but R_L itself decreases — the product is not monotonic. At R_L = 0, the load is shorted and P_L = 0 (all power dissipated in R_th). At R_L → ∞, current → 0 and P_L → 0. The maximum occurs at R_L = R_th — the calculus result of setting dP_L/dR_L = 0. Neither extreme delivers maximum power."

- question: "Explain the fundamental tension between maximum power transfer and maximum efficiency, and describe which goal is appropriate for signal systems versus power delivery systems."
  type: short-answer
  answer: "Maximum power transfer (R_L = R_th) extracts the most power possible from a given source, but at only 50% efficiency — half the total circuit power is lost in the source resistance. Maximum efficiency means R_L >> R_th so nearly all power reaches the load, but this reduces total transferred power (small current through large resistance). Signal systems (antennas, RF amplifiers, audio transmission lines) prioritize extracting maximum signal energy from the source — even 50% efficiency is acceptable when you're working with milliwatts and the goal is signal fidelity. Power delivery systems (electrical grids, motor drives, battery chargers) prioritize efficiency because wasted energy represents real economic and thermodynamic cost at scale — a 50% efficient transmission line would double electricity costs."
  explanation: "The theorem is often misapplied by students who assume 'maximum power' is always the engineering goal. The correct insight is that 'maximum power to the load' and 'maximum fraction of source power reaching the load' are different objectives, satisfied by different load conditions. Choosing the right condition requires understanding the application."
```

## Explainer

From your study of Thévenin equivalents, you know that any linear source network — no matter how complex — reduces to a voltage source V_th in series with a resistance R_th. This simplification sets up a clean optimization problem: given this fixed source, what load resistance R_L extracts the most power?

The analysis is a single-variable calculus problem. Power delivered to the load is P = I²R_L, where current I = V_th/(R_th + R_L). Substituting: P = V_th² × R_L / (R_th + R_L)². Setting dP/dR_L = 0 and solving yields R_L = R_th — the **impedance matching condition**. At this point, P_max = V_th²/(4R_th). The factor of 4 in the denominator reveals something important: when matched, exactly half the total power is dissipated in R_th and half in R_L. The source is only 50% efficient at the maximum-power operating point.

This 50% efficiency exposes the fundamental tension between **maximum power transfer** and **maximum efficiency**. When R_L >> R_th, current is small and little power is lost in R_th — efficiency approaches 100%, but total power delivered is tiny. When R_L = R_th, efficiency is exactly 50%, but power delivered is maximized for the given source. These goals serve different engineering contexts: power delivery systems (electrical grids, motor drives, battery chargers) prioritize efficiency and operate with R_L >> R_th; communication and signal systems (antennas, RF amplifiers, audio transmission lines) want maximum signal extraction and use impedance matching.

A critical subtlety: the theorem assumes R_th is fixed by the source — you are optimizing only over R_L. If R_th could be freely reduced to zero, you would deliver maximum power to any load, which is why low-output-impedance sources are prized in power electronics. In AC circuits, the condition generalizes to complex impedances: maximum power transfer requires Z_L = Z_th* (the complex conjugate of the Thévenin impedance). This cancels the reactive parts and matches the resistive parts, ensuring all available source power is absorbed by the load rather than bounced back — the foundation of transmission line and antenna matching theory.
