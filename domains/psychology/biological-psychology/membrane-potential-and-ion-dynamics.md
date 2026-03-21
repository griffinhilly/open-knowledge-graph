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
stage: advanced
status: draft
---

# Membrane Potential and Ion Dynamics

## Core Idea
The resting membrane potential (~−70 mV) arises from two factors: unequal ion distribution (high K+ inside, high Na+ outside) and selective permeability favoring K+ efflux. The Na+/K+-ATPase pump actively maintains this gradient by exchanging 3 Na+ out for 2 K+ in, consuming ATP. This electrochemical gradient is the fundamental energy source for all neural signaling.

## How It's Best Learned
Use the Goldman equation to calculate equilibrium potentials and resting potential from ion concentrations. Study how pump inhibition (ouabain) changes potential over time. Manipulate extracellular K+ concentration and observe membrane potential changes. Perform voltage-clamp recordings to measure ion currents.

## Common Misconceptions
Resting potential is a passive consequence of ion distribution / the pump directly creates the potential / changing one ion concentration has equal effects.

## Questions

```yaml
- question: "A researcher applies ouabain, a Na+/K+-ATPase inhibitor, to a neuron. What are the correct immediate and long-term effects on resting membrane potential?"
  type: multiple-choice
  options:
    - "Immediate large depolarization, because the pump directly generates the negative resting potential"
    - "No immediate change, but gradual depolarization over minutes to hours as ion gradients slowly dissipate"
    - "Immediate hyperpolarization, because blocking the pump allows K+ to accumulate inside"
    - "No change at all, because the pump plays no role in setting resting membrane potential"
  answer: 1
  explanation: "The resting potential is created by passive K+ flow through leak channels, not by the pump directly. Stopping the pump immediately eliminates its small electrogenic contribution (~few mV) but leaves ion gradients — and therefore K+ leak — essentially intact. Over minutes to hours, however, the gradients dissipate (Na+ leaks in, K+ leaks out) because no pump is restoring them, and the membrane potential gradually depolarizes toward zero. Option A represents the key misconception: the pump is not the direct generator of the resting potential."

- question: "Why is the resting membrane potential approximately −70 mV rather than the K+ equilibrium potential of about −90 mV?"
  type: multiple-choice
  options:
    - "The Na+/K+-ATPase pump adds +20 mV directly to the K+ equilibrium potential"
    - "Small but finite membrane permeability to Na+ allows a slight inward Na+ current that partially offsets K+ efflux, pulling the potential toward Na+'s equilibrium of +60 mV"
    - "K+ leak channels are partially blocked at rest, preventing full K+ equilibration"
    - "The cell expends ATP to actively clamp the membrane at −70 mV rather than at the K+ equilibrium"
  answer: 1
  explanation: "The resting potential is a weighted average of the equilibrium potentials for all permeant ions, weighted by their relative permeabilities. At rest, the membrane is highly permeable to K+ (equilibrium ~−90 mV) and slightly permeable to Na+ (equilibrium ~+60 mV). The small Na+ leak pulls the actual potential ~20 mV positive of the K+ equilibrium potential. The Goldman equation formalizes this. The pump's direct electrogenic contribution is only 2–3 mV, not 20 mV."

- question: "The Na+/K+-ATPase pump directly creates the resting membrane potential by pumping charge across the membrane, generating the −70 mV gradient."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about resting membrane potential. The pump's primary role is maintaining ion concentration gradients, not directly generating voltage. The resting potential is created by passive K+ flow through leak channels: K+ moves out down its concentration gradient until the developing electrical force (inside becoming negative) exactly balances the chemical force. Blocking the pump with ouabain has little immediate effect on resting potential — gradients persist and K+ continues to flow passively. The pump's direct electrogenic effect (3 Na+ out for 2 K+ in) contributes only ~2–3 mV."

- question: "If K+ leak channels were suddenly and completely blocked, the resting membrane potential would collapse toward zero even if the Na+/K+-ATPase pump continued operating normally."
  type: true-false
  answer: true
  explanation: "The resting potential exists because K+ flows passively through open leak channels until electrical and chemical forces balance. The pump maintains the concentration gradient that drives this flow, but if the channels are blocked, no K+ movement occurs regardless of the gradient — and without K+ movement, the voltage difference is not created or maintained. The pump cannot substitute for channel-mediated current. This thought experiment reveals that the channels, not the pump, are the proximate generators of the resting potential."

- question: "Why is the resting membrane potential closer to the K+ equilibrium potential than to the Na+ equilibrium potential, even though both ions have steep concentration gradients across the membrane?"
  type: short-answer
  answer: "At rest, the membrane is highly permeable to K+ due to abundant open K+ leak channels, while Na+ channels are mostly closed. K+ flows out down its concentration gradient, generating most of the membrane's negative interior voltage and pulling the potential toward K+'s equilibrium (~−90 mV). Na+ has a large driving force (toward +60 mV) but little membrane permeability at rest, so its influence is minor. Resting potential (~−70 mV) reflects this imbalance — it is weighted primarily by K+ permeability, with a slight positive shift from the small Na+ leak."
  explanation: "The Goldman equation formalizes this: membrane potential is a permeability-weighted average of equilibrium potentials. The dominant K+ permeability at rest makes the potential closely track E_K. During an action potential, Na+ channels open massively, temporarily making Na+ the dominant ion and driving the potential toward +60 mV before K+ repolarizes the cell."
```

## Explainer

The resting membrane potential emerges from two physical forces acting on ions simultaneously: concentration gradients and electrical gradients. Think of ions as tiny charged particles that want to move in two ways at once — down their concentration gradient (from where they're packed tightly to where they're sparse) and toward or away from electrical charge. The resting potential exists at the precise point where these two forces balance for the key ion, potassium.

Potassium (K+) is concentrated inside the cell, roughly 30-fold higher inside than outside. Because the membrane is selectively permeable to K+ at rest through leak channels, K+ flows out down its concentration gradient. As K+ exits, it leaves behind negative charges, making the inside of the cell progressively more negative. This growing negativity pulls K+ back in electrically. The **equilibrium potential** for an ion is the voltage at which these two forces cancel exactly — for K+, around −90 mV. The actual resting potential of about −70 mV is slightly less negative because Na+ and other ions also contribute small currents, shifting the balance modestly toward Na+'s equilibrium potential (around +60 mV).

The **Na+/K+-ATPase pump** is the engine that maintains the ion gradients in the first place. It continuously pushes 3 Na+ out of the cell and pulls 2 K+ in, consuming one ATP per cycle. Because it moves 3 positive charges out for every 2 it brings in, the pump is slightly **electrogenic** — contributing a few mV of negativity directly. But its primary role is maintaining the concentration gradients that drive the passive K+ current which sets the resting potential. Without the pump running continuously, gradients would dissipate over time and the potential would collapse.

A key misconception is that the pump *directly creates* the resting potential. More precisely, the pump maintains the gradient, and passive flow of K+ through leak channels *creates* the potential. You can see this distinction experimentally: blocking leak channels prevents K+ movement and the membrane potential collapses even with the pump intact. Blocking the pump with ouabain has little immediate effect on resting potential — but over minutes to hours, as gradients dissipate, the potential gradually depolarizes toward zero. The resting potential is thus a dynamic equilibrium: concentration gradients (maintained by the pump) drive passive ionic flow until electrical force balances chemical force at −70 mV.
