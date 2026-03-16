---
id: resting-membrane-potential
title: Resting Membrane Potential
domain: biology
course: neuroscience
prerequisites:
- id: goldman-equation
  type: hard
- id: neuron-structure-and-function
  type: hard
- id: active-transport
  type: hard
- id: equilibrium-expression-kc-kp-constants
  type: soft
- id: electrochemistry-basics
  type: soft
builds-toward:
- voltage-gated-sodium-channels
- voltage-gated-potassium-channels
tags:
- electrophysiology
- membrane-potential
stage: advanced
status: draft
---

# Resting Membrane Potential

## Core Idea
Steady-state voltage (~−70 mV) maintained by Na+/K+ ATPase gradients and differential permeability. At rest, K+ conductance dominates.

## Questions

```yaml
- question: "At rest, the neuron membrane is most permeable to which ion, and what is the consequence for membrane potential?"
  type: multiple-choice
  options:
    - "Na+, driving the potential toward +60 mV"
    - "K+, driving the potential toward −90 mV because K+ leaks out down its concentration gradient"
    - "Cl−, driving the potential toward 0 mV"
    - "Na+ and K+ equally, so the potential sits at 0 mV"
  answer: 1
  explanation: "At rest, leak K+ channels dominate conductance. K+ is concentrated inside and flows out down its gradient, leaving net negative charge inside. The resting potential (~−70 mV) sits between the K+ equilibrium potential (−90 mV) and the Na+ equilibrium potential (+60 mV), pulled toward K+ because K+ permeability is far greater."

- question: "The Na+/K+ ATPase directly generates most of the resting membrane potential by actively electrogenic pumping."
  type: true-false
  answer: false
  explanation: "The Na+/K+ ATPase contributes a small direct electrogenic effect (pumps 3 Na+ out and 2 K+ in per cycle, net −1 charge per cycle), but its primary role is maintaining the concentration gradients that K+ and Na+ leak channels then exploit. The gradients — not the pump's direct current — account for the bulk of the −70 mV resting potential."

- question: "Explain why the resting membrane potential is closer to the K+ equilibrium potential than to the Na+ equilibrium potential."
  type: short-answer
  answer: "Because resting membrane permeability to K+ far exceeds permeability to Na+. The Goldman equation weights each ion's contribution by its conductance; since K+ conductance dominates, the membrane potential is pulled strongly toward E_K (~−90 mV) and only weakly toward E_Na (+60 mV), yielding a net resting potential near −70 mV."
  explanation: "The Goldman equation (which generalizes the Nernst equation to multiple ions) shows that each ion's equilibrium potential is weighted by that ion's permeability. A high K+ permeability means K+ movement dominates the electrical behavior of the resting membrane."
```

## Explainer

To understand the resting membrane potential, start with what the Na+/K+ ATPase has already accomplished: it has used ATP to pump Na+ out and K+ in against their respective concentration gradients, creating a cell interior that is high in K+ (~140 mM) and low in Na+ (~15 mM) relative to the extracellular fluid. This pump runs continuously and is the engine that makes everything else possible. Without it, the gradients — and the resting potential — would collapse.

With those gradients in place, consider what happens at the membrane. At rest, the membrane contains many open K+ leak channels and very few open Na+ channels. K+ ions, driven by their concentration gradient (high inside → low outside), flow outward through the leak channels. As positive charges leave, the inside of the membrane becomes increasingly negative. This growing negativity exerts an electrical pull back on K+ — and at some point the outward chemical drive and the inward electrical pull balance exactly. That balance point is the K+ equilibrium potential, approximately −90 mV.

The resting membrane potential sits at about −70 mV rather than −90 mV because the membrane is not perfectly impermeable to Na+. A small but nonzero Na+ conductance allows a trickle of Na+ to flow inward (driven by both its concentration gradient and the negative interior), nudging the potential slightly positive of E_K. The Goldman equation formalizes this: the resting potential is a conductance-weighted average of all ion equilibrium potentials, dominated by K+ but slightly offset by Na+ and Cl−.

A common misconception is that the Na+/K+ ATPase is directly pumping the membrane to −70 mV the way a battery charges a capacitor. In reality, the pump's direct electrogenic contribution (3 Na+ out, 2 K+ in per cycle — net −1 charge per cycle) accounts for only a few millivolts. What the pump actually does is maintain the concentration gradients that the leak channels then convert into voltage. If you block the pump with ouabain, the resting potential does not collapse immediately — the gradients can sustain the potential for some time before dissipating.

Understanding the resting membrane potential is essential for what comes next: action potentials. The −70 mV resting state is like a compressed spring. When voltage-gated Na+ channels open (e.g., upon sufficient depolarization), Na+ rushes inward down both its concentration and electrical gradients, and the membrane rapidly depolarizes toward +60 mV. The resting potential you have just studied is the baseline from which that explosive reversal begins.
