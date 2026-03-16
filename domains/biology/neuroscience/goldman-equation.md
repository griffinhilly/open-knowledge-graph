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
stage: advanced
status: draft
---

# The Goldman-Hodgkin-Katz Equation

## Core Idea
Extends Nernst to multiple ions, weighting each by permeability. Explains why resting potential (~−70 mV) lies between K+ and Na+ equilibrium potentials, dominated by K+ permeability.

## Explainer

The Nernst equation, which you've already learned, tells you the equilibrium potential for a single ion species — the voltage at which the electrical and concentration gradients for that ion exactly balance. For K+ in a typical neuron, this is about −90 mV; for Na+, about +60 mV. But real neurons are permeable to multiple ions simultaneously, so the actual membrane potential cannot equal the equilibrium potential for any single ion. The **Goldman-Hodgkin-Katz (GHK) voltage equation** solves this problem by calculating the membrane potential when multiple ions are crossing the membrane at once.

The GHK equation looks similar to the Nernst equation but includes terms for every major permeant ion, each weighted by its **relative permeability** (P). For the three ions that dominate in neurons, it takes the form: V_m = (RT/F) × ln[(P_K[K+]_out + P_Na[Na+]_out + P_Cl[Cl−]_in) / (P_K[K+]_in + P_Na[Na+]_in + P_Cl[Cl−]_out)]. Notice the asymmetry — cations have outside concentrations in the numerator and inside in the denominator, while the negatively charged Cl− is reversed. The key insight is that permeability values act as weights: an ion with high permeability pulls the membrane potential strongly toward its own equilibrium potential, while an ion with low permeability has little influence.

At rest, the neuronal membrane is roughly 40 times more permeable to K+ than to Na+ (P_K/P_Na ≈ 40:1). This is why the resting membrane potential (about −70 mV) sits much closer to E_K (−90 mV) than to E_Na (+60 mV) — potassium dominates the equation. The resting potential doesn't quite reach E_K because the small but non-zero Na+ permeability through leak channels pulls the voltage slightly positive. Cl− permeability contributes but often passively distributes to match the resting potential rather than actively setting it.

The real power of the GHK equation becomes apparent when you consider what happens during neural signaling. When voltage-gated Na+ channels open during an action potential, P_Na suddenly increases by about 500-fold — now Na+ permeability dominates, and the equation predicts the membrane potential will swing toward E_Na (+60 mV), which is exactly what the depolarizing upstroke of the action potential does. When Na+ channels inactivate and K+ channels open, P_K dominates again, driving repolarization. The GHK equation thus provides a unified quantitative framework: give it the permeabilities and concentrations at any moment, and it predicts the membrane voltage. Every change in membrane potential — resting, action potential, synaptic potential — can be understood as a shift in the relative permeabilities that weight each ion's contribution.
