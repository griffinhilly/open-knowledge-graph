---
id: action-potential
title: Action Potential
domain: biology
course: physiology
prerequisites:
- id: neuron-structure-and-function
  type: hard
- id: passive-transport
  type: hard
- id: active-transport
  type: hard
- id: electrochemistry-basics
  type: soft
- id: chemical-equilibrium
  type: soft
builds-toward:
- synaptic-transmission
- skeletal-muscle-contraction
- cardiac-cycle-and-heart-function
tags:
- action potential
- membrane potential
- depolarization
- ion channels
- electrophysiology
stage: formal-systems
status: validated
---

# Action Potential

## Core Idea
An action potential is a transient, all-or-none reversal of membrane potential that propagates along an axon without decrement. At rest the membrane is polarized at approximately −70 mV, maintained by the Na⁺/K⁺-ATPase and the selective permeability of leak channels. When membrane potential reaches threshold (~−55 mV), voltage-gated Na⁺ channels open rapidly, causing depolarization toward +40 mV. Voltage-gated K⁺ channels then open and Na⁺ channels inactivate, producing repolarization and brief hyperpolarization (undershoot) before the resting potential is restored. Stimulus intensity is encoded by firing frequency, not action potential amplitude, because the response is all-or-none.

## How It's Best Learned
Plot the action potential on a voltage-time graph, labeling resting potential, threshold, depolarization peak, repolarization, undershoot, and absolute and relative refractory periods. At each phase, identify which ion channels are open or closed and the direction of ion flow. Then explain why the all-or-none principle means a neuron cannot fire a 'half' action potential.

## Common Misconceptions
- The action potential does not travel as a wave of ions along the membrane — it is regenerated locally at each successive membrane patch.
- Na⁺ and K⁺ concentrations barely change after a single action potential; the Na⁺/K⁺ pump restores gradients over many cycles and is not required for each individual spike.
- The refractory period prevents backward propagation, ensuring the signal moves in only one direction.

## Questions

```yaml
- question: "During the depolarization phase of an action potential, the membrane potential overshoots 0 mV and reaches approximately +40 mV. What drives this overshoot?"
  type: multiple-choice
  options:
    - "The Na⁺/K⁺-ATPase temporarily reverses direction, pumping Na⁺ into the cell"
    - "Voltage-gated Na⁺ channels open and Na⁺ rushes in down both its concentration and electrical gradients"
    - "Voltage-gated K⁺ channels open, allowing K⁺ to rush into the cell along its electrical gradient"
    - "Cl⁻ channels open and Cl⁻ exits the cell, making the interior more positive"
  answer: 1
  explanation: "At rest, Na⁺ is both more concentrated outside the cell and electrically attracted inward by the negative interior. When voltage-gated Na⁺ channels open at threshold, both driving forces combine to produce a large inward Na⁺ current that rapidly depolarizes the membrane toward the Na⁺ equilibrium potential (~+60 mV). The membrane doesn't fully reach this value because the channels begin to inactivate, halting the process around +40 mV."

- question: "Stimulus intensity is encoded as action potential amplitude — a stronger stimulus produces a larger action potential."
  type: true-false
  answer: false
  explanation: "The action potential is all-or-none: once threshold is reached, the amplitude is fixed regardless of stimulus strength. A neuron cannot produce a 'half' action potential. Instead, stimulus intensity is encoded by firing frequency (rate coding) — a stronger stimulus causes the neuron to fire more action potentials per second, not larger ones."

- question: "What prevents an action potential from traveling backward along the axon after it is generated?"
  type: short-answer
  answer: "The absolute refractory period. Immediately after depolarization, voltage-gated Na⁺ channels in the just-fired segment undergo inactivation — a conformational change that prevents them from reopening regardless of voltage. Because the membrane behind the advancing wavefront is always in this refractory state, the action potential can only propagate forward into the next unexcited patch of membrane."
  explanation: "Na⁺ channel inactivation is distinct from simply closing: an inactivated channel cannot reopen until the membrane repolarizes, which takes time. This creates a temporal window during which no stimulus can retriger an action potential in that segment. The directional propagation of the action potential is thus a direct consequence of channel kinetics, not a special property of the axon's geometry."
```

## Explainer

From your study of neuron structure, you know that neurons maintain a resting membrane potential of about −70 mV — the inside of the cell is negative relative to the outside. This charge separation is maintained by the Na⁺/K⁺-ATPase, which pumps 3 Na⁺ out and 2 K⁺ in per cycle, and by leak channels that allow K⁺ to slowly diffuse out. Understanding passive and active transport is essential here because the action potential is a carefully orchestrated violation — and then restoration — of this resting state, driven entirely by the movement of ions down their concentration and electrical gradients.

The trigger is depolarization to threshold. When a stimulus brings the membrane from −70 mV up to approximately −55 mV, voltage-gated Na⁺ channels open in a self-reinforcing cascade. Na⁺ is more concentrated outside and electrically attracted inward, so when these channels open, Na⁺ rushes in and makes the interior more positive — which opens more Na⁺ channels, which lets in more Na⁺. This positive feedback drives the membrane potential rapidly to about +40 mV. This is the rising phase of the action potential. The membrane overshoots 0 mV because the driving forces on Na⁺ don't stop at zero — they continue until Na⁺ channels begin to inactivate.

Two events then combine to restore the resting potential. First, voltage-gated Na⁺ channels undergo inactivation — a conformational change distinct from simply closing, which renders them incapable of reopening for a period of time regardless of voltage. Second, voltage-gated K⁺ channels (which open more slowly) allow K⁺ to flow out down its concentration gradient, removing positive charges from the cell. The membrane potential falls rapidly back toward resting. K⁺ channels stay open slightly longer than needed, producing a brief undershoot to about −80 mV (afterhyperpolarization). During this period, it is harder than normal to trigger another spike — this is the relative refractory period.

A critical feature of the action potential is that it is all-or-none: if threshold is not reached, nothing fires; if it is reached, the full-amplitude spike always fires. This means a neuron cannot produce a "small" action potential in response to a weak stimulus. Instead, stimulus intensity is encoded in firing frequency — a more intense stimulus makes the neuron fire at 100 Hz rather than 10 Hz. This rate coding allows an all-or-none mechanism to carry graded information across the nervous system.

Finally, understand that the action potential propagates without decrement because it is not traveling as a passive electrical signal — it is regenerated locally at each successive patch of axon membrane. The segment that just fired is refractory (Na⁺ channels inactivated), so the only direction the action potential can spread is forward into the next unexcited membrane. This directional, regenerative propagation is what allows signals to travel reliably over meters of axon without losing amplitude.
