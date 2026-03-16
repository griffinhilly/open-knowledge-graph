---
id: voltage-gated-sodium-channels
title: Voltage-Gated Sodium Channels
domain: biology
course: neuroscience
prerequisites:
- id: resting-membrane-potential
  type: hard
- id: ligand-gated-ion-channels
  type: soft
builds-toward:
- action-potential-depolarization-repolarization
tags:
- ion-channels
- action-potential
stage: advanced
status: draft
---

# Voltage-Gated Sodium Channels

## Core Idea
Open at depolarization (~−55 mV), allowing rapid Na+ influx. Have activation gate (fast) and inactivation gate (faster), producing transient inward current.

## Questions

```yaml
- question: "A neuron's membrane depolarizes past threshold. Which sequence correctly describes what happens to the voltage-gated sodium channel?"
  type: multiple-choice
  options:
    - "Inactivation gate closes first, then activation gate opens, allowing brief Na+ influx"
    - "Activation gate opens rapidly, Na+ rushes in, then inactivation gate closes, terminating the current"
    - "Both gates open simultaneously and stay open as long as the membrane remains depolarized"
    - "The channel opens once and permanently inactivates, preventing any further Na+ entry"
  answer: 1
  explanation: "The activation (m) gate opens quickly at depolarization, allowing rapid Na+ influx. The inactivation (h) gate then closes slightly later, terminating current flow even while the membrane is still depolarized. This sequential mechanism makes the current transient rather than sustained."

- question: "Voltage-gated sodium channels remain open and continue conducting Na+ for as long as the membrane is depolarized above threshold."
  type: true-false
  answer: false
  explanation: "This is false. The inactivation gate closes within milliseconds of the activation gate opening, terminating Na+ influx even if the membrane is still depolarized. The channel enters an inactivated state and cannot reopen until the membrane repolarizes, which is the molecular basis of the absolute refractory period."

- question: "Why can a second action potential not be triggered immediately after the first, even with a very strong stimulus?"
  type: short-answer
  answer: "During the absolute refractory period, voltage-gated sodium channels are in the inactivated state — the inactivation gate is closed and the channel cannot reopen regardless of voltage. Only after repolarization allows the inactivation gate to reset can the channels respond to another stimulus."
  explanation: "The refractory period is not simply about membrane voltage — it is about the conformational state of the channel. Inactivation is voltage-dependent (requires repolarization to recover), so even driving the membrane back to threshold with an external current will not reopen inactivated channels."
```

## Explainer

To understand voltage-gated sodium channels, start with what you know about the resting membrane potential: at rest, the inside of the neuron is about −70 mV relative to the outside, maintained largely by the selective permeability of potassium channels and the sodium-potassium pump. Sodium ions are abundant outside the cell, and there is a strong electrochemical drive pushing them inward — but at rest, voltage-gated sodium channels are closed, so they cannot enter.

When a depolarizing stimulus brings the membrane to threshold (~−55 mV), voltage-gated sodium channels sense the change in electric field and undergo a conformational shift: the activation gate (the m gate) swings open. Sodium ions rush inward down their electrochemical gradient, rapidly depolarizing the membrane further toward +40 mV. This is the rising phase of the action potential. The key feature is that the channel has a second gate — the inactivation gate (h gate) — that responds to depolarization more slowly. Within a millisecond of opening, the inactivation gate swings into the pore and plugs it, terminating Na+ influx even while the membrane is still depolarized. The current is transient precisely because of this dual-gate design.

The inactivated state is fundamentally different from the closed state. A closed channel can open if threshold is reached; an inactivated channel cannot, regardless of voltage. It can only recover — reset to the closed state — after the membrane repolarizes. This recovery takes time, which creates the absolute refractory period: a window after each action potential during which no stimulus, however strong, can trigger another. The refractory period ensures that action potentials travel in only one direction along an axon and limits the maximum firing rate of neurons.

Compare this to ligand-gated channels you've encountered: those open in response to neurotransmitter binding, not voltage, and they don't have the same fast inactivation mechanism. Voltage-gated channels are tuned for speed and precision — the activation and inactivation kinetics are carefully matched to produce the sharp, stereotyped spike that makes action potentials reliable digital signals over long distances.
