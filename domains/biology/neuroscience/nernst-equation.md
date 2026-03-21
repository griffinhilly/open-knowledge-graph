---
id: nernst-equation
title: The Nernst Equation
domain: biology
course: neuroscience
prerequisites:
- id: cell-membrane-structure
  type: hard
- id: cell-signaling-intro
  type: soft
builds-toward:
- goldman-equation
- resting-membrane-potential
tags:
- electrophysiology
- ion-channels
stage: advanced
status: draft
---

# The Nernst Equation

## Core Idea
The Nernst equation predicts the equilibrium potential for a single ion: V = (RT/zF) × ln([out]/[in]). It quantifies the voltage at which that ion has no net electrochemical drive.

## Questions

```yaml
- question: "A neuron has a resting membrane potential of −70 mV. The equilibrium potential for K⁺ is −89 mV. What is the electrochemical driving force on potassium, and in which direction will K⁺ flow?"
  type: multiple-choice
  options:
    - "Driving force = −19 mV; K⁺ flows inward because the inside is more negative than E_K"
    - "Driving force = +19 mV; K⁺ tends to flow outward because V_m is more positive than E_K, meaning the electrical force holding K⁺ inside is insufficient to counteract the concentration gradient"
    - "Driving force = 0; K⁺ is at equilibrium at −70 mV"
    - "Driving force = +19 mV; K⁺ flows inward because the concentration gradient overpowers the electrical gradient"
  answer: 1
  explanation: "Driving force = V_m − E_K = −70 − (−89) = +19 mV. A positive driving force for a monovalent cation means the net force pushes K⁺ outward. At −89 mV, K⁺ would be perfectly balanced; at −70 mV (less negative), the electrical pull inward is weaker than at equilibrium, so the concentration gradient pushing K⁺ out wins. K⁺ flows out of the cell through open K⁺ channels — this outward current is what maintains the resting membrane potential near (but not equal to) E_K."

- question: "What does the Nernst equilibrium potential E_Na ≈ +67 mV represent for sodium?"
  type: multiple-choice
  options:
    - "The membrane voltage required to pump sodium out of the cell against its concentration gradient"
    - "The voltage at which the concentration gradient driving Na⁺ inward and the electrical gradient driving Na⁺ outward exactly cancel, so there is no net electrochemical force on sodium"
    - "The resting membrane potential contribution from sodium channels"
    - "The threshold membrane voltage at which sodium channels open during an action potential"
  answer: 1
  explanation: "E_Na is the single-ion equilibrium potential: the membrane voltage at which the Na⁺ concentration gradient (pointing inward, because Na⁺ is more concentrated outside) is exactly balanced by the electrical gradient (at +67 mV, the positive interior repels incoming positive ions). At this voltage, Na⁺ has zero net electrochemical driving force. At the resting potential of −70 mV, V_m is far below E_Na, so the driving force (V_m − E_Na = −70 − 67 = −137 mV) is large and negative, meaning Na⁺ is powerfully driven inward whenever Na⁺ channels open."

- question: "If the actual membrane potential equals the Nernst equilibrium potential for a given ion, there is no net electrochemical driving force on that ion."
  type: true-false
  answer: true
  explanation: "The equilibrium potential is defined as the membrane voltage at which the concentration gradient and electrical gradient for that ion exactly cancel. At E_ion, the chemical potential difference driving the ion down its concentration gradient is exactly offset by the electrical potential difference, so the net electrochemical driving force is zero and there is no net ion flux. This is the condition the Nernst equation calculates."

- question: "The Nernst equation can directly calculate the resting membrane potential of a neuron, since it relates membrane voltage to ion concentration gradients."
  type: true-false
  answer: false
  explanation: "The Nernst equation calculates the equilibrium potential for a single ion in isolation — the voltage that would develop if the membrane were permeable to only that one ion. Real neuron membranes are permeable to multiple ions (K⁺, Na⁺, Cl⁻, and others) simultaneously, and the resting potential reflects all of them weighted by their relative permeabilities. The Goldman equation handles the multi-ion case. The resting potential (≈ −70 mV) falls between E_K (≈ −89 mV) and E_Na (≈ +67 mV), closer to E_K because resting potassium permeability greatly exceeds sodium permeability."

- question: "Explain why the resting membrane potential of a typical neuron (around −70 mV) is close to E_K (−89 mV) but not equal to it. What determines where between E_K and E_Na the resting potential falls?"
  type: short-answer
  answer: "The Nernst equation gives the equilibrium potential for each ion individually. At rest, the membrane is much more permeable to K⁺ than to Na⁺ (due to leak channels), so the resting potential is dominated by K⁺ and falls close to E_K. However, there is a small but non-zero resting Na⁺ permeability that pulls the potential toward E_Na (+67 mV), shifting it from −89 mV toward a less negative value. The Goldman equation formalizes this: the resting potential is a permeability-weighted average of the equilibrium potentials. If P_K >> P_Na, the result is close to E_K but not exactly equal. The Na⁺/K⁺-ATPase pump also makes a small direct contribution by pumping 3 Na⁺ out for every 2 K⁺ in (electrogenic)."
  explanation: "This explains why disrupting K⁺ channels affects resting potential more than disrupting Na⁺ channels at rest — the resting potential is fundamentally a potassium equilibrium perturbed by minor sodium permeability. During an action potential, the relationship reverses: sodium permeability spikes and the membrane potential rushes toward E_Na."
```

## Explainer

From your study of cell membrane structure, you know that the lipid bilayer is selectively permeable — ions can only cross through specific channel proteins, and different ions are distributed unevenly across the membrane. Potassium (K⁺) is concentrated inside the cell, sodium (Na⁺) and calcium (Ca²⁺) are concentrated outside, and chloride (Cl⁻) is mostly extracellular. The **Nernst equation** answers a deceptively simple question: if the membrane were permeable to only one ion, what voltage would develop across it?

The answer emerges from a tug-of-war between two forces. Consider potassium: because K⁺ is more concentrated inside the cell, there is a **concentration gradient** driving it outward. But as K⁺ ions leave, they carry positive charge with them, making the inside of the cell progressively more negative. This growing voltage difference creates an **electrical gradient** that opposes further K⁺ efflux — the negative interior starts pulling positive ions back in. At some voltage, these two forces exactly balance: the concentration gradient pushing K⁺ out equals the electrical gradient pulling it back in. That voltage is the **equilibrium potential** (E) for potassium, and it is the value the Nernst equation calculates.

The equation itself is E = (RT/zF) × ln([ion]outside/[ion]inside), where R is the gas constant, T is absolute temperature, z is the ion's charge (including sign), and F is Faraday's constant. At body temperature (37°C), this simplifies to approximately E = (61.5 mV / z) × log₁₀([out]/[in]) when using base-10 logarithms. For K⁺ with typical concentrations of 5 mM outside and 140 mM inside, you get E_K ≈ (61.5/1) × log(5/140) ≈ −89 mV. For Na⁺ (145 mM outside, 12 mM inside), E_Na ≈ +67 mV. Notice that the sign of the equilibrium potential depends on which side of the membrane has the higher concentration and on the charge of the ion — this is captured automatically by the math.

The Nernst equation gives you the equilibrium potential for one ion at a time, which is a simplification — real membranes are permeable to multiple ions simultaneously. That is why the resting membrane potential (around −70 mV in a typical neuron) does not exactly equal E_K or E_Na but falls between them, weighted by relative permeabilities. The **Goldman equation**, which you will encounter next, handles this multi-ion case. But the Nernst equation remains indispensable because it tells you the **driving force** on any individual ion: the difference between the actual membrane potential and that ion's equilibrium potential (V_m − E_ion). If V_m is more positive than E_K, potassium will flow outward; if V_m is more negative than E_Na, sodium will flow inward. This concept of electrochemical driving force is the foundation for understanding every electrical event in neurons — from resting potentials to action potentials to synaptic currents.
