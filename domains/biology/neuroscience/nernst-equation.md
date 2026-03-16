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

## Explainer

From your study of cell membrane structure, you know that the lipid bilayer is selectively permeable — ions can only cross through specific channel proteins, and different ions are distributed unevenly across the membrane. Potassium (K⁺) is concentrated inside the cell, sodium (Na⁺) and calcium (Ca²⁺) are concentrated outside, and chloride (Cl⁻) is mostly extracellular. The **Nernst equation** answers a deceptively simple question: if the membrane were permeable to only one ion, what voltage would develop across it?

The answer emerges from a tug-of-war between two forces. Consider potassium: because K⁺ is more concentrated inside the cell, there is a **concentration gradient** driving it outward. But as K⁺ ions leave, they carry positive charge with them, making the inside of the cell progressively more negative. This growing voltage difference creates an **electrical gradient** that opposes further K⁺ efflux — the negative interior starts pulling positive ions back in. At some voltage, these two forces exactly balance: the concentration gradient pushing K⁺ out equals the electrical gradient pulling it back in. That voltage is the **equilibrium potential** (E) for potassium, and it is the value the Nernst equation calculates.

The equation itself is E = (RT/zF) × ln([ion]outside/[ion]inside), where R is the gas constant, T is absolute temperature, z is the ion's charge (including sign), and F is Faraday's constant. At body temperature (37°C), this simplifies to approximately E = (61.5 mV / z) × log₁₀([out]/[in]) when using base-10 logarithms. For K⁺ with typical concentrations of 5 mM outside and 140 mM inside, you get E_K ≈ (61.5/1) × log(5/140) ≈ −89 mV. For Na⁺ (145 mM outside, 12 mM inside), E_Na ≈ +67 mV. Notice that the sign of the equilibrium potential depends on which side of the membrane has the higher concentration and on the charge of the ion — this is captured automatically by the math.

The Nernst equation gives you the equilibrium potential for one ion at a time, which is a simplification — real membranes are permeable to multiple ions simultaneously. That is why the resting membrane potential (around −70 mV in a typical neuron) does not exactly equal E_K or E_Na but falls between them, weighted by relative permeabilities. The **Goldman equation**, which you will encounter next, handles this multi-ion case. But the Nernst equation remains indispensable because it tells you the **driving force** on any individual ion: the difference between the actual membrane potential and that ion's equilibrium potential (V_m − E_ion). If V_m is more positive than E_K, potassium will flow outward; if V_m is more negative than E_Na, sodium will flow inward. This concept of electrochemical driving force is the foundation for understanding every electrical event in neurons — from resting potentials to action potentials to synaptic currents.
