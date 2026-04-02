---
id: action-potential-generation-and-propagation
title: Action Potential Generation and Propagation
domain: psychology
course: biological-psychology
prerequisites:
- id: membrane-potential-and-ion-dynamics
  type: hard
- id: voltage-gated-sodium-channels
  type: soft
- id: action-potential-depolarization-repolarization
  type: hard
- id: ion-channels-selectivity
  type: hard
- id: myelin-and-myelination
  type: hard
builds-toward:
- synaptic-transmission-process
tags:
- action-potential
- conduction
- spikes
- excitability
stage: advanced
status: validated
---

# Action Potential Generation and Propagation

## Core Idea
Action potentials are rapid, stereotyped changes in membrane potential caused by sequential opening and closing of voltage-gated Na+ and K+ channels. Depolarization past threshold triggers Na+ influx (depolarizing phase), which is terminated by Na+ channel inactivation and K+ channel opening (repolarizing phase). This regenerative process propagates along the axon as each region's depolarization opens nearby channels, with saltatory conduction in myelinated axons allowing much faster propagation.

## How It's Best Learned
Study voltage-clamp recordings showing isolated Na+ and K+ currents. Simulate the Hodgkin-Huxley model to understand gating variable dynamics. Measure conduction velocity differences between unmyelinated and myelinated axons. Observe threshold phenomena and all-or-none firing.

## Common Misconceptions
Voltage "travels" along axon like water in a pipe / an action potential is electrical current flowing down the axon / conduction is instantaneous / repolarization is passive.

## Questions

```yaml
- question: "During an action potential, what causes depolarization to spread to adjacent regions of the axon?"
  type: multiple-choice
  options:
    - "Electrical current flows down the axon from the initial segment, like current through a wire"
    - "Local circuit currents from the depolarized patch flow laterally to adjacent membrane, depolarizing it past threshold"
    - "The sodium-potassium pump actively transports positive charge to neighboring membrane regions"
    - "Voltage-gated channels open simultaneously along the entire axon length in response to the initial stimulus"
  answer: 1
  explanation: "The action potential is not a current flowing down the axon like water in a pipe — it is regenerated at each point. When one membrane patch depolarizes, positive charge flows laterally inside the axon to the adjacent resting membrane (local circuit currents). This small current depolarizes the neighboring patch past threshold, triggering its own Na⁺ channel cascade. The wave moves by sequential regeneration, not transmission. Option A is the classic misconception."

- question: "A toxin permanently blocks voltage-gated Na⁺ channel inactivation — channels can open normally but cannot transition to the inactivated state. What is the most likely effect on a neuron exposed to this toxin?"
  type: multiple-choice
  options:
    - "Neurons fire more rapidly, since more sodium influx means a stronger signal"
    - "Action potentials propagate faster because Na⁺ channels remain open longer at each site"
    - "The neuron becomes stuck in a prolonged depolarized state and cannot generate further action potentials"
    - "Repolarization is faster because K⁺ channels overcompensate for the stuck Na⁺ channels"
  answer: 2
  explanation: "Na⁺ channel inactivation is what terminates the depolarizing phase and establishes the absolute refractory period. Without inactivation, Na⁺ channels remain open indefinitely, keeping the membrane depolarized near +40 mV. The neuron cannot repolarize, cannot re-activate its voltage-gated channels, and is locked in a state that prevents any subsequent action potential. This is the mechanism by which several neurotoxins (e.g., batrachotoxin) cause persistent depolarization and nerve failure."

- question: "An action potential's amplitude decreases progressively as it travels further from the site of initiation, eventually fading out — similar to how a ripple in water weakens with distance."
  type: true-false
  answer: false
  explanation: "This describes a decremental (graded) potential, not an action potential. The action potential is all-or-none and is regenerated de novo at each point along the axon by the opening of fresh voltage-gated Na⁺ channels. Each regeneration event produces a full-amplitude spike, so the signal maintains its size across the entire axon length. The refractory period behind the advancing wave prevents it from reversing direction, but amplitude does not decay with distance."

- question: "The absolute refractory period — during which no stimulus can trigger another action potential — is what ensures that action potentials propagate in only one direction along an axon."
  type: true-false
  answer: true
  explanation: "After a patch of membrane fires, its Na⁺ channels enter the inactivated state and remain so for 1–2 ms (the absolute refractory period). The region that just fired therefore cannot re-fire even if the advancing depolarization wave loops back to it. This means the depolarization can only trigger the next, not-yet-fired patch in the forward direction — enforcing unidirectional conduction. Without the refractory period, signals could travel in both directions or create re-entrant loops."

- question: "Explain why myelin dramatically increases conduction velocity rather than simply allowing the action potential to decay, as passive electrical signals do."
  type: short-answer
  answer: "Myelin insulates the axon segments between nodes of Ranvier, dramatically reducing ion leakage and membrane capacitance along those segments. When an action potential fires at one node, the resulting local circuit current spreads with minimal attenuation along the myelinated internodal segment and reaches the next node of Ranvier with enough strength to depolarize it past threshold. The action potential effectively 'jumps' from node to node (saltatory conduction) rather than being regenerated at every point. Each saltatory jump covers far more distance per regeneration event than unmyelinated propagation, producing conduction velocities up to 100 m/s — compared to ~1 m/s in small unmyelinated fibers."
  explanation: "The key is that myelin does not just speed up propagation — it changes its mechanism from continuous to saltatory. In unmyelinated fibers, every patch of membrane must be depolarized past threshold to regenerate the signal, which is slow. In myelinated fibers, the insulation makes the internodal membrane electrically 'invisible,' so current jumps directly between nodes where the voltage-gated channels are concentrated. This is why demyelinating diseases (multiple sclerosis, Guillain-Barré) cause dramatic slowing or failure of conduction — they eliminate the saltatory mechanism."
```

## Explainer

From your study of membrane potential and ion dynamics, you know that a neuron at rest maintains a charge difference across its membrane — roughly −70 mV inside relative to outside — sustained by the sodium-potassium pump and the selective permeability of leak channels. The **action potential** begins when local depolarization (from synaptic input or an electrode) nudges the membrane potential toward the threshold, typically around −55 mV. At threshold, **voltage-gated sodium channels** snap open. This is the pivotal moment: sodium ions, driven by both concentration gradient and electrical attraction, flood into the cell. Their entry further depolarizes the membrane, opening more Na⁺ channels in a positive feedback loop — the rapid, self-amplifying inrush of sodium that drives the membrane potential to approximately +40 mV in less than a millisecond. This is the **all-or-nothing** principle: below threshold, nothing happens; at or above threshold, the full spike fires.

The spike cannot last indefinitely. Two mechanisms terminate it. First, voltage-gated Na⁺ channels undergo **inactivation** — a conformational change distinct from simple closure that blocks the channel even while it is still "open." This inactivation gate closes within a millisecond of channel opening, halting further sodium influx. Second, **voltage-gated potassium channels** open more slowly than Na⁺ channels but are also triggered by depolarization. Potassium ions, driven out by both concentration gradient and the now-positive interior charge, exit the cell, repolarizing the membrane back toward the resting potential. Because K⁺ channels close slowly and the sodium pump continues working, the membrane briefly **hyperpolarizes** below resting potential (the **undershoot** or afterhyperpolarization) before equilibrating back to −70 mV. The period during which the Na⁺ channels remain inactivated is the **absolute refractory period** — no stimulus, however strong, can fire another action potential. This ensures the signal propagates in one direction only.

Propagation works not by current flowing down the axon like water in a pipe, but by **local circuit currents**. When one patch of membrane depolarizes, positive charge flows laterally inside the axon to the adjacent resting membrane. This small local current depolarizes the neighboring patch past threshold, triggering its own Na⁺ channel cascade. That patch then depolarizes the next one, and so on — a chain reaction of sequential Na⁺ channel activations moving down the axon. The action potential does not travel; it is *regenerated* at each point. The already-fired patch behind the wave cannot re-fire because its Na⁺ channels are still inactivated, so the wave moves in only one direction.

In **myelinated axons**, this mechanism is dramatically accelerated by **saltatory conduction**. Myelin sheaths wrap tightly around axon segments between the nodes of Ranvier, electrically insulating those segments so that ion channels there are sparse and local current leakage is minimized. The depolarizing current generated at one node of Ranvier therefore spreads far along the axon — rather than decrementing over millimeters — and reaches the next node with enough strength to depolarize it past threshold. The action potential effectively "jumps" from node to node (saltatory, from the Latin for jump), covering far more distance per regeneration event. This produces conduction velocities up to 100 meters per second in large myelinated axons, compared to roughly 1 m/s in small unmyelinated fibers — the same mechanism that allows the nervous system to coordinate rapid, precisely timed movements across the full length of the body.
