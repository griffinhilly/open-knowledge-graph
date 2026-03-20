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
status: draft
---

# Action Potential Generation and Propagation

## Core Idea
Action potentials are rapid, stereotyped changes in membrane potential caused by sequential opening and closing of voltage-gated Na+ and K+ channels. Depolarization past threshold triggers Na+ influx (depolarizing phase), which is terminated by Na+ channel inactivation and K+ channel opening (repolarizing phase). This regenerative process propagates along the axon as each region's depolarization opens nearby channels, with saltatory conduction in myelinated axons allowing much faster propagation.

## How It's Best Learned
Study voltage-clamp recordings showing isolated Na+ and K+ currents. Simulate the Hodgkin-Huxley model to understand gating variable dynamics. Measure conduction velocity differences between unmyelinated and myelinated axons. Observe threshold phenomena and all-or-none firing.

## Common Misconceptions
Voltage "travels" along axon like water in a pipe / an action potential is electrical current flowing down the axon / conduction is instantaneous / repolarization is passive.

## Explainer

From your study of membrane potential and ion dynamics, you know that a neuron at rest maintains a charge difference across its membrane — roughly −70 mV inside relative to outside — sustained by the sodium-potassium pump and the selective permeability of leak channels. The **action potential** begins when local depolarization (from synaptic input or an electrode) nudges the membrane potential toward the threshold, typically around −55 mV. At threshold, **voltage-gated sodium channels** snap open. This is the pivotal moment: sodium ions, driven by both concentration gradient and electrical attraction, flood into the cell. Their entry further depolarizes the membrane, opening more Na⁺ channels in a positive feedback loop — the rapid, self-amplifying inrush of sodium that drives the membrane potential to approximately +40 mV in less than a millisecond. This is the **all-or-nothing** principle: below threshold, nothing happens; at or above threshold, the full spike fires.

The spike cannot last indefinitely. Two mechanisms terminate it. First, voltage-gated Na⁺ channels undergo **inactivation** — a conformational change distinct from simple closure that blocks the channel even while it is still "open." This inactivation gate closes within a millisecond of channel opening, halting further sodium influx. Second, **voltage-gated potassium channels** open more slowly than Na⁺ channels but are also triggered by depolarization. Potassium ions, driven out by both concentration gradient and the now-positive interior charge, exit the cell, repolarizing the membrane back toward the resting potential. Because K⁺ channels close slowly and the sodium pump continues working, the membrane briefly **hyperpolarizes** below resting potential (the **undershoot** or afterhyperpolarization) before equilibrating back to −70 mV. The period during which the Na⁺ channels remain inactivated is the **absolute refractory period** — no stimulus, however strong, can fire another action potential. This ensures the signal propagates in one direction only.

Propagation works not by current flowing down the axon like water in a pipe, but by **local circuit currents**. When one patch of membrane depolarizes, positive charge flows laterally inside the axon to the adjacent resting membrane. This small local current depolarizes the neighboring patch past threshold, triggering its own Na⁺ channel cascade. That patch then depolarizes the next one, and so on — a chain reaction of sequential Na⁺ channel activations moving down the axon. The action potential does not travel; it is *regenerated* at each point. The already-fired patch behind the wave cannot re-fire because its Na⁺ channels are still inactivated, so the wave moves in only one direction.

In **myelinated axons**, this mechanism is dramatically accelerated by **saltatory conduction**. Myelin sheaths wrap tightly around axon segments between the nodes of Ranvier, electrically insulating those segments so that ion channels there are sparse and local current leakage is minimized. The depolarizing current generated at one node of Ranvier therefore spreads far along the axon — rather than decrementing over millimeters — and reaches the next node with enough strength to depolarize it past threshold. The action potential effectively "jumps" from node to node (saltatory, from the Latin for jump), covering far more distance per regeneration event. This produces conduction velocities up to 100 meters per second in large myelinated axons, compared to roughly 1 m/s in small unmyelinated fibers — the same mechanism that allows the nervous system to coordinate rapid, precisely timed movements across the full length of the body.
