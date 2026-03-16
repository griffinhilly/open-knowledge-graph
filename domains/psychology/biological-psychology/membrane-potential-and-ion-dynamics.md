---
id: membrane-potential-and-ion-dynamics
title: Membrane Potential and Ion Dynamics
domain: psychology
course: biological-psychology
prerequisites:
- id: neuron-morphology-and-classification
  type: hard
- id: sodium-potassium-atpase
  type: soft
- id: resting-membrane-potential
  type: hard
builds-toward:
- action-potential-generation-and-propagation
tags:
- bioelectricity
- ions
- transport
- potential
stage: formal-systems
status: draft
---

# Membrane Potential and Ion Dynamics

## Core Idea
The resting membrane potential (~−70 mV) arises from two factors: unequal ion distribution (high K+ inside, high Na+ outside) and selective permeability favoring K+ efflux. The Na+/K+-ATPase pump actively maintains this gradient by exchanging 3 Na+ out for 2 K+ in, consuming ATP. This electrochemical gradient is the fundamental energy source for all neural signaling.

## How It's Best Learned
Use the Goldman equation to calculate equilibrium potentials and resting potential from ion concentrations. Study how pump inhibition (ouabain) changes potential over time. Manipulate extracellular K+ concentration and observe membrane potential changes. Perform voltage-clamp recordings to measure ion currents.

## Common Misconceptions
Resting potential is a passive consequence of ion distribution / the pump directly creates the potential / changing one ion concentration has equal effects.

## Explainer

The resting membrane potential emerges from two physical forces acting on ions simultaneously: concentration gradients and electrical gradients. Think of ions as tiny charged particles that want to move in two ways at once — down their concentration gradient (from where they're packed tightly to where they're sparse) and toward or away from electrical charge. The resting potential exists at the precise point where these two forces balance for the key ion, potassium.

Potassium (K+) is concentrated inside the cell, roughly 30-fold higher inside than outside. Because the membrane is selectively permeable to K+ at rest through leak channels, K+ flows out down its concentration gradient. As K+ exits, it leaves behind negative charges, making the inside of the cell progressively more negative. This growing negativity pulls K+ back in electrically. The **equilibrium potential** for an ion is the voltage at which these two forces cancel exactly — for K+, around −90 mV. The actual resting potential of about −70 mV is slightly less negative because Na+ and other ions also contribute small currents, shifting the balance modestly toward Na+'s equilibrium potential (around +60 mV).

The **Na+/K+-ATPase pump** is the engine that maintains the ion gradients in the first place. It continuously pushes 3 Na+ out of the cell and pulls 2 K+ in, consuming one ATP per cycle. Because it moves 3 positive charges out for every 2 it brings in, the pump is slightly **electrogenic** — contributing a few mV of negativity directly. But its primary role is maintaining the concentration gradients that drive the passive K+ current which sets the resting potential. Without the pump running continuously, gradients would dissipate over time and the potential would collapse.

A key misconception is that the pump *directly creates* the resting potential. More precisely, the pump maintains the gradient, and passive flow of K+ through leak channels *creates* the potential. You can see this distinction experimentally: blocking leak channels prevents K+ movement and the membrane potential collapses even with the pump intact. Blocking the pump with ouabain has little immediate effect on resting potential — but over minutes to hours, as gradients dissipate, the potential gradually depolarizes toward zero. The resting potential is thus a dynamic equilibrium: concentration gradients (maintained by the pump) drive passive ionic flow until electrical force balances chemical force at −70 mV.
