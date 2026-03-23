---
id: action-potential-and-neural-signaling
title: 'Action Potential: Generation and Propagation'
domain: psychology
course: biological-psychology
prerequisites:
- id: ion-channels-and-neural-excitability
  type: hard
- id: resting-membrane-potential
  type: hard
- id: action-potential
  type: hard
- id: voltage-gated-sodium-channels
  type: hard
- id: membrane-potential-and-ion-dynamics
  type: hard
- id: ion-channels-selectivity
  type: hard
builds-toward:
- synaptic-transmission-neurotransmitter-release
- myelin-and-saltatory-conduction
tags:
- electrical-signaling
- neurophysiology
- propagation
stage: formal-systems
status: validated
---

# Action Potential: Generation and Propagation

## Core Idea
The action potential is a rapid, temporary change in membrane potential that allows neurons to transmit signals over long distances. It involves sequential opening of voltage-gated sodium channels (depolarization) followed by potassium channels (repolarization). The all-or-none principle means subthreshold stimuli don't trigger action potentials, creating a threshold for neural signaling.

## How It's Best Learned
Use voltage-clamp simulations to observe individual channel currents, then integrate to see whole-cell behavior. Graph the phases of the action potential against ion channel conductances to understand causation.

## Questions

```yaml
- question: "A neuron receives a stimulus at twice the threshold voltage. Compared to a stimulus exactly at threshold, what happens to the resulting action potential?"
  type: multiple-choice
  options:
    - "It has twice the amplitude, reaching roughly +80 mV instead of +40 mV"
    - "It has the same amplitude but propagates twice as fast along the axon"
    - "It has the same amplitude and the same propagation speed"
    - "It fails to propagate because excessive depolarization inactivates too many channels at once"
  answer: 2
  explanation: "This is the all-or-none principle: once the threshold is reached, the action potential goes to completion regardless of stimulus strength. The peak amplitude (~+40 mV) is determined by the Na⁺ equilibrium potential and channel properties, not stimulus size. A stimulus twice the threshold does not produce a larger or faster spike — it produces an identical one. Information about stimulus intensity is encoded in firing *frequency*, not spike amplitude."

- question: "Why can't a second action potential be triggered during the absolute refractory period, even with a very strong stimulus?"
  type: multiple-choice
  options:
    - "The membrane potential is too negative (hyperpolarized) for threshold to be reached"
    - "Voltage-gated Na⁺ channels are in an inactivated state and cannot reopen regardless of membrane potential"
    - "The Na⁺/K⁺-ATPase pump is actively hyperpolarizing the membrane"
    - "Voltage-gated K⁺ channels are still open and prevent depolarization"
  answer: 1
  explanation: "The absolute refractory period is defined by Na⁺ channel inactivation. After depolarization, these channels enter a closed, inactivated state that differs from their resting closed state — they cannot be reopened by voltage until they have had time to recover. This is a physical constraint on the channel protein itself, not just a matter of voltage. Even if you artificially push the membrane potential back to −55 mV, no action potential can fire. This is why the absolute refractory period places an upper limit on firing frequency."

- question: "A stronger stimulus to a sensory neuron produces a subjectively more intense sensation because it generates action potentials with larger amplitudes."
  type: true-false
  answer: false
  explanation: "Action potentials obey the all-or-none principle — they are always the same amplitude. Stimulus intensity is encoded in the *frequency* and *pattern* of firing, not in spike size. A strong stimulus causes the neuron to fire more action potentials per second; a weak stimulus produces fewer. The brain reads frequency as intensity, not amplitude."

- question: "During action potential propagation, the absolute refractory period in the previously fired axon segment ensures the signal travels in only one direction."
  type: true-false
  answer: true
  explanation: "When a segment fires, depolarization spreads by local circuit currents to the adjacent resting membrane, triggering a new action potential there. But it also spreads back toward the segment that just fired — however, those Na⁺ channels are inactivated (absolutely refractory), so that segment cannot re-fire. The wave is therefore forced to advance only into previously resting tissue, producing unidirectional propagation from the initial stimulation site toward the axon terminal."

- question: "Why does a neuron encode the strength of a stimulus through firing frequency rather than through varying action potential amplitude, and what structural feature makes this possible?"
  type: short-answer
  answer: "Because action potentials are all-or-none events — channel kinetics and electrochemical gradients determine a fixed peak amplitude, not stimulus strength. The neuron instead varies how often it fires: a strong stimulus depolarizes the cell above threshold repeatedly, producing a high-frequency train of identical spikes. The relative refractory period (during which a stronger-than-normal stimulus can trigger a second spike) sets the range over which frequency can be modulated."
  explanation: "The all-or-none constraint is a feature, not a bug: it ensures that signals arrive at the synaptic terminal with the same waveform they started with, regardless of axon length. Analog encoding of intensity by amplitude would degrade over long distances. Frequency coding is distance-invariant — each spike is refreshed to full amplitude at every segment of the axon, preserving signal fidelity across the entire length of the neuron."
```

## Explainer

You already know that neurons sit at a resting membrane potential of approximately −70 mV, maintained by selective ion permeability and the Na⁺/K⁺-ATPase pump. You also know that **voltage-gated ion channels** open in response to changes in membrane potential — unlike the leak channels that maintain the resting state, these channels are sensitive to voltage and open or close based on it. The action potential is what happens when those channels interact in sequence.

When a stimulus depolarizes the membrane toward the **threshold potential** (roughly −55 mV), a critical number of **voltage-gated sodium channels** open. Na⁺ rushes in along its electrochemical gradient — high outside concentration, and a strongly negative interior that attracts positive ions. This inward Na⁺ current further depolarizes the membrane, which opens more sodium channels, which causes more depolarization. This **positive feedback loop** — called the Hodgkin cycle — drives the membrane potential from −70 mV to approximately +40 mV in less than a millisecond. This is the **depolarization phase** of the action potential, and once it begins above threshold, it goes to completion regardless of how large the original stimulus was. That is the **all-or-none principle**: either the threshold is reached and the full spike occurs, or nothing happens. A stimulus twice the threshold does not produce twice the action potential.

At the peak of depolarization, two processes converge to reverse it. Voltage-gated sodium channels enter an **inactivated state** — they close and cannot immediately reopen, no matter how depolarized the membrane is. Simultaneously, **voltage-gated potassium channels** (which open more slowly than sodium channels) reach full opening, allowing K⁺ to rush out along its electrochemical gradient. This outward K⁺ current brings the membrane back toward the potassium equilibrium potential, overshooting −70 mV slightly (the **hyperpolarization phase**, or afterhyperpolarization). During this period, the inactivated sodium channels cannot reopen, creating the **absolute refractory period** — the neuron physically cannot fire again, no matter how strong the stimulus.

**Propagation** exploits the local circuit currents generated by each spike. The depolarization at one segment of the axon causes current to flow into adjacent, still-resting membrane, which depolarizes that region above threshold and triggers its own action potential. Because the sodium channels in the just-fired region are inactivated, the wave can only travel in one direction — away from the initial site toward the terminal. This unidirectional propagation, combined with the all-or-none spike amplitude, means the signal arrives at the synaptic terminal with the same waveform it started with, regardless of distance. Neural signaling is thus a relay of identical pulses, with information encoded in the **frequency** and **pattern** of firing rather than in spike magnitude.
