---
id: goldman-equation
title: The Goldman-Hodgkin-Katz Equation
domain: biology
course: neuroscience
prerequisites:
- id: nernst-equation
  type: hard
- id: cell-membrane-structure
  type: hard
builds-toward:
- resting-membrane-potential
tags:
- electrophysiology
- membrane-potential
stage: expert
status: validated
---

# The Goldman-Hodgkin-Katz Equation

## Core Idea
Extends Nernst to multiple ions, weighting each by permeability. Explains why resting potential (~−70 mV) lies between K+ and Na+ equilibrium potentials, dominated by K+ permeability.

## Questions

```yaml
- question: "At rest, a neuron has P_K/P_Na ≈ 40:1. The K⁺ equilibrium potential is −90 mV and the Na⁺ equilibrium potential is +60 mV. Which statement best predicts the resting membrane potential according to the Goldman equation?"
  type: multiple-choice
  options:
    - "It equals −90 mV, since K⁺ completely dominates and the membrane potential converges exactly to E_K"
    - "It equals the arithmetic average of −90 and +60 mV (approximately −15 mV), since both ions contribute equally"
    - "It is slightly less negative than −90 mV — close to E_K but pulled a few millivolts toward E_Na by the small Na⁺ permeability"
    - "It equals 0 mV, since the opposing K⁺ and Na⁺ gradients exactly cancel each other out"
  answer: 2
  explanation: "The GHK equation weights each ion's equilibrium potential by its permeability. The large K⁺ permeability pulls V_m strongly toward E_K (−90 mV), but the small residual Na⁺ permeability through leak channels exerts a constant depolarizing pull toward E_Na (+60 mV). The result is approximately −70 mV — dominated by K⁺ but not equal to E_K. Option A is the most tempting misconception: students often equate 'K⁺ dominates' with 'V_m = E_K,' but any nonzero Na⁺ permeability prevents the membrane from reaching the K⁺ equilibrium potential. Options B and D both misunderstand the weighting — the average is not arithmetic, and the contributions do not cancel."

- question: "During the rising phase of an action potential, voltage-gated Na⁺ channels open, increasing P_Na roughly 500-fold. What does the Goldman equation predict for the membrane potential at this moment?"
  type: multiple-choice
  options:
    - "The potential becomes more negative, since Na⁺ influx adds positive charge inside and repels the existing negative interior potential"
    - "The potential swings toward E_Na (+60 mV), since the massive increase in Na⁺ permeability now dominates the weighting"
    - "The potential stays near −70 mV, since the K⁺ concentration gradient is larger and resists displacement"
    - "The potential reaches exactly 0 mV, since equal inward Na⁺ and outward K⁺ currents temporarily balance"
  answer: 1
  explanation: "When P_Na increases 500-fold, it completely overwhelms the previously dominant K⁺ permeability. In the GHK equation, Na⁺ now carries almost all the weight, and the predicted V_m approaches E_Na (+60 mV). This is precisely the depolarizing upstroke of the action potential. The membrane does not reach +60 mV exactly because K⁺ permeability doesn't drop to zero, but the potential swings dramatically positive before Na⁺ channels inactivate. Option A has the direction wrong — Na⁺ ions carry positive charge INTO the cell, depolarizing (making more positive) the interior, not more negative."

- question: "If the concentrations of K⁺ and Na⁺ were suddenly equalized across the membrane (same inside and outside), while all permeabilities remained unchanged, the resting membrane potential would be unaffected."
  type: true-false
  answer: false
  explanation: "The GHK equation depends on the ratio of outside-to-inside ion concentrations inside the logarithm. If all concentrations were equalized, every logarithmic concentration ratio becomes 1, and ln(1) = 0, so the entire equation evaluates to 0 mV regardless of the permeability values. The permeabilities weight the relative influence of each ion, but there must be concentration gradients to generate a potential in the first place. Permeability without concentration difference produces no driving force — the two inputs (concentration gradients and permeabilities) are multiplicative, not additive."

- question: "According to the Goldman equation, an ion with zero membrane permeability contributes nothing to the resting membrane potential, even if it has a steep concentration gradient across the membrane."
  type: true-false
  answer: true
  explanation: "Permeability in the GHK equation acts as a multiplicative weight. If P_ion = 0, the ion's term drops out of both numerator and denominator entirely — its concentration ratio has no effect on V_m. This is physically sensible: if the membrane is completely impermeable to an ion, no current can flow through it, and it exerts no electrochemical driving force on the membrane voltage. Large impermeant anions like proteins and nucleic acids inside neurons contribute to the overall charge balance but not directly to the membrane potential through the GHK mechanism."

- question: "Why does the Goldman equation predict a resting membrane potential of approximately −70 mV rather than the K⁺ equilibrium potential of −90 mV, even though K⁺ dominates membrane permeability at rest?"
  type: short-answer
  answer: "Because the membrane is not exclusively permeable to K⁺ — there is a small but non-zero Na⁺ permeability through leak channels. In the GHK equation, each ion's equilibrium potential is weighted by its permeability. The high K⁺ permeability pulls V_m strongly toward E_K (−90 mV), but the small Na⁺ permeability exerts a constant depolarizing tug toward E_Na (+60 mV). The resting potential (~−70 mV) is the equilibrium where these opposing influences balance, landing closer to E_K than E_Na because K⁺ conductance is about 40 times larger, but not equal to E_K because Na⁺ conductance is not zero."
  explanation: "This is the key conceptual difference between the Nernst and Goldman equations. The Nernst equation gives the potential for a membrane permeable to only one ion; the Goldman equation gives the potential for a membrane with multiple competing permeabilities. At rest, K⁺ 'wins' the competition but does not win completely. This partial victory (~20 mV short of E_K) has important consequences: it means the Na-K ATPase must continuously pump to maintain the concentration gradients, since the small persistent Na⁺ leak keeps driving Na⁺ in, and the K⁺ leak drives K⁺ out."
```

## Explainer

The Nernst equation, which you've already learned, tells you the equilibrium potential for a single ion species — the voltage at which the electrical and concentration gradients for that ion exactly balance. For K+ in a typical neuron, this is about −90 mV; for Na+, about +60 mV. But real neurons are permeable to multiple ions simultaneously, so the actual membrane potential cannot equal the equilibrium potential for any single ion. The **Goldman-Hodgkin-Katz (GHK) voltage equation** solves this problem by calculating the membrane potential when multiple ions are crossing the membrane at once.

The GHK equation looks similar to the Nernst equation but includes terms for every major permeant ion, each weighted by its **relative permeability** (P). For the three ions that dominate in neurons, it takes the form: V_m = (RT/F) × ln[(P_K[K+]_out + P_Na[Na+]_out + P_Cl[Cl−]_in) / (P_K[K+]_in + P_Na[Na+]_in + P_Cl[Cl−]_out)]. Notice the asymmetry — cations have outside concentrations in the numerator and inside in the denominator, while the negatively charged Cl− is reversed. The key insight is that permeability values act as weights: an ion with high permeability pulls the membrane potential strongly toward its own equilibrium potential, while an ion with low permeability has little influence.

At rest, the neuronal membrane is roughly 40 times more permeable to K+ than to Na+ (P_K/P_Na ≈ 40:1). This is why the resting membrane potential (about −70 mV) sits much closer to E_K (−90 mV) than to E_Na (+60 mV) — potassium dominates the equation. The resting potential doesn't quite reach E_K because the small but non-zero Na+ permeability through leak channels pulls the voltage slightly positive. Cl− permeability contributes but often passively distributes to match the resting potential rather than actively setting it.

The real power of the GHK equation becomes apparent when you consider what happens during neural signaling. When voltage-gated Na+ channels open during an action potential, P_Na suddenly increases by about 500-fold — now Na+ permeability dominates, and the equation predicts the membrane potential will swing toward E_Na (+60 mV), which is exactly what the depolarizing upstroke of the action potential does. When Na+ channels inactivate and K+ channels open, P_K dominates again, driving repolarization. The GHK equation thus provides a unified quantitative framework: give it the permeabilities and concentrations at any moment, and it predicts the membrane voltage. Every change in membrane potential — resting, action potential, synaptic potential — can be understood as a shift in the relative permeabilities that weight each ion's contribution.
