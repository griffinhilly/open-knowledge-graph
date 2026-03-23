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
status: validated
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

## Questions

```yaml
- question: "Carbon monoxide (CO) has measurable residual entropy even in a highly purified crystalline sample cooled to near absolute zero. What is the reason?"
  type: multiple-choice
  options:
    - "The sample has not quite reached true absolute zero, so some thermal entropy remains"
    - "Impurities in the crystal prevent perfect ordering, raising W above 1"
    - "CO and OC orientations in the crystal lattice are energetically nearly equivalent, leaving multiple frozen-in arrangements at 0 K"
    - "The third law does not apply to molecular compounds, only to monatomic solids"
  answer: 2
  explanation: "CO and OC have nearly identical lattice energies, so both orientations coexist throughout the crystal even at 0 K — the disordered arrangement becomes kinetically trapped. This means W > 1, so S = k ln(W) > 0. This is genuine residual entropy, not a measurement artifact. The third law sets S = 0 only for perfect crystals (W = 1); imperfect crystals retain residual entropy. Option B is wrong because the residual entropy is intrinsic to CO's molecular symmetry, not extrinsic impurities."

- question: "Before the third law was established, thermochemists working with only the first and second laws could calculate:"
  type: multiple-choice
  options:
    - "Absolute entropy values at any temperature, as long as heat capacity data were available"
    - "Only entropy differences between two states, not the absolute entropy of either"
    - "Neither entropy values nor entropy differences"
    - "Absolute entropy only at room temperature, not at other temperatures"
  answer: 1
  explanation: "The second law gives ΔS = Q_rev/T — a change. Without a reference zero, you can know that going from state A to state B increases entropy by 20 J/mol·K, but you cannot say what the entropy is at either state in absolute terms. The third law provides the reference: S = 0 for a perfect crystal at 0 K. This allows integration of Cₚ/T data from 0 K upward to yield true absolute molar entropies — the S° values tabulated in thermochemistry references."

- question: "The entropy of any solid is exactly zero at absolute zero, regardless of its crystal structure or molecular composition."
  type: true-false
  answer: false
  explanation: "The third law applies only to perfect crystals. Solids with frozen-in orientational or positional disorder — like CO, ice (which has hydrogen-bond disorder), or NO — retain residual entropy at 0 K because their disordered arrangements are energetically equivalent and kinetically trapped. For these materials, W > 1 at 0 K, so S = k ln(W) > 0. The qualifier 'perfect crystal' is not a footnote — it is the entire condition."

- question: "Absolute entropy is calculated by integrating Cₚ/T rather than Cₚ itself because the same quantity of heat generates more entropy at low temperatures than at high temperatures."
  type: true-false
  answer: true
  explanation: "Entropy measures how energy is distributed among accessible microstates. At low temperatures, few microstates are available, so adding heat opens up a large fraction of new states relative to those already occupied — a large entropy increase per joule. At high temperatures, the same joule of heat is spread across many already-accessible states, making a smaller relative contribution. Dividing by T captures this: dS = dQ_rev/T, so the integrand Cₚ/T correctly weights the contribution of each increment of heating by the temperature at which it occurs."

- question: "Why does the third law require a 'perfect crystal' as its reference state, and what distinguishes a material with residual entropy from one with zero entropy at 0 K?"
  type: short-answer
  answer: "A perfect crystal has exactly one possible microstate at 0 K — every atom is in its unique designated position with no ambiguity — so W = 1 and S = k ln(1) = 0. A material with residual entropy has multiple energetically equivalent arrangements that become frozen in as the temperature drops, so W > 1 and S > 0 even at absolute zero. The distinction is whether the system can relax into a unique ground state (perfect crystal) or whether disorder is trapped (residual entropy)."
  explanation: "This question tests whether students understand S = k ln(W) well enough to apply it beyond the textbook example. Students who memorize 'S = 0 at 0 K' without grasping the microstate argument will fail to understand why CO, ice, and similar molecules are exceptions — and why the third law says anything meaningful at all."
```

## Explainer

From your study of entropy, you learned that entropy is a measure of disorder — or more precisely, from statistical mechanics, a measure of the number of ways a system can be arranged at the microscopic level. The statistical definition, S = k ln(W), where W is the number of accessible microstates, is the key to understanding why the third law works. Ask yourself: what does a perfect crystal at absolute zero look like microscopically? Every atom is locked into exactly one position, with exactly one allowed configuration. That means W = 1, so S = k ln(1) = k × 0 = 0. The third law is not an empirical observation tacked on — it follows directly from statistical mechanics when you take the system to its most ordered possible state.

This matters enormously because the first and second laws only ever give you changes in entropy: ΔS = Q_rev/T. They can tell you that a process increases entropy by 20 J/K, but they cannot tell you where you started. The third law provides the **absolute reference point**. By setting S = 0 at absolute zero for a perfect crystal, you can integrate heat capacity data from 0 K up to any temperature to get the **absolute molar entropy**: S(T) = ∫₀ᵀ (Cₚ/T) dT. Every tabulated standard entropy value S° you see in thermochemistry tables (typically at 298 K) was computed this way — it is an absolute quantity, not a difference.

The integration formula deserves a moment's attention. The integrand is Cₚ/T, not just Cₚ. Temperature appears in the denominator because entropy captures how much disorder a given amount of heat produces — and adding heat at low temperatures (when there are few microstates available) creates proportionally more disorder than adding the same heat at high temperatures (when states are already spread widely). This is why entropy rises steeply at low temperatures and flattens at high temperatures.

One subtlety keeps the third law from being trivial: it applies to **perfect crystals** only. Real materials often have **residual entropy** — disorder frozen in at low temperatures because the crystal is not perfectly ordered. Carbon monoxide (CO), for example, can orient as CO or OC in a crystal lattice with nearly equal energy, so many arrangements persist even at 0 K, leaving W > 1 and S > 0. This residual entropy is real, measurable, and important for accurate thermochemical calculations. The third law does not forbid residual entropy; it tells you what the minimum would be if you could achieve perfection.
