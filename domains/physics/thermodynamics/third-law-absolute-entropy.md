---
id: third-law-absolute-entropy
title: The Third Law of Thermodynamics and Absolute Entropy
domain: physics
course: thermodynamics
prerequisites:
- id: entropy-intro
  type: hard
- id: statistical-interpretation-of-entropy
  type: soft
builds-toward: []
tags:
- entropy
- third-law
- absolute-values
stage: formal-systems
status: draft
---
# The Third Law of Thermodynamics and Absolute Entropy

## Core Idea
The third law of thermodynamics states that the entropy of a perfect crystal at absolute zero is zero: S(T=0) = 0. This allows the calculation of absolute entropy values S(T) = S(0) + ∫(C_p/T)dT from absolute zero to any temperature, rather than only entropy differences. The third law, combined with statistical mechanics, shows that entropy quantifies the number of accessible microstates and provides a natural definition of absolute entropy.

## How It's Best Learned
Use heat capacity data to integrate S(T) from 0 K to any temperature. Compare calculated absolute entropies with tabulated values.

## Common Misconceptions
- Thinking the third law forbids reaching absolute zero (it forbids reaching it in finite steps, not absolutely).
- Confusing the third law with energy conservation (first law).
- Assuming non-perfect crystals have exactly zero entropy at 0 K (residual entropy can exist).

## Explainer

From your study of entropy, you learned that entropy is a measure of disorder — or more precisely, from statistical mechanics, a measure of the number of ways a system can be arranged at the microscopic level. The statistical definition, S = k ln(W), where W is the number of accessible microstates, is the key to understanding why the third law works. Ask yourself: what does a perfect crystal at absolute zero look like microscopically? Every atom is locked into exactly one position, with exactly one allowed configuration. That means W = 1, so S = k ln(1) = k × 0 = 0. The third law is not an empirical observation tacked on — it follows directly from statistical mechanics when you take the system to its most ordered possible state.

This matters enormously because the first and second laws only ever give you changes in entropy: ΔS = Q_rev/T. They can tell you that a process increases entropy by 20 J/K, but they cannot tell you where you started. The third law provides the **absolute reference point**. By setting S = 0 at absolute zero for a perfect crystal, you can integrate heat capacity data from 0 K up to any temperature to get the **absolute molar entropy**: S(T) = ∫₀ᵀ (Cₚ/T) dT. Every tabulated standard entropy value S° you see in thermochemistry tables (typically at 298 K) was computed this way — it is an absolute quantity, not a difference.

The integration formula deserves a moment's attention. The integrand is Cₚ/T, not just Cₚ. Temperature appears in the denominator because entropy captures how much disorder a given amount of heat produces — and adding heat at low temperatures (when there are few microstates available) creates proportionally more disorder than adding the same heat at high temperatures (when states are already spread widely). This is why entropy rises steeply at low temperatures and flattens at high temperatures.

One subtlety keeps the third law from being trivial: it applies to **perfect crystals** only. Real materials often have **residual entropy** — disorder frozen in at low temperatures because the crystal is not perfectly ordered. Carbon monoxide (CO), for example, can orient as CO or OC in a crystal lattice with nearly equal energy, so many arrangements persist even at 0 K, leaving W > 1 and S > 0. This residual entropy is real, measurable, and important for accurate thermochemical calculations. The third law does not forbid residual entropy; it tells you what the minimum would be if you could achieve perfection.
