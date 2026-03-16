---
id: myelinated-axon-saltatory-conduction
title: Saltatory Conduction in Myelinated Axons
domain: biology
course: neuroscience
prerequisites:
- id: unmyelinated-axon-conduction
  type: hard
- id: neuron-structure-and-function
  type: hard
builds-toward:
- hodgkin-huxley-model
tags:
- conduction-velocity
- myelin
stage: advanced
status: draft
---

# Saltatory Conduction in Myelinated Axons

## Core Idea
Myelin insulation reduces capacitive loss; action potentials regenerate only at Nodes of Ranvier. Depolarization 'jumps' between nodes. ~50× faster than unmyelinated (~50 m/s).

## Explainer

You have already seen how action potentials propagate along unmyelinated axons: depolarization at one point opens voltage-gated Na+ channels in the adjacent membrane, and the signal creeps forward in a continuous wave. This works, but it is slow — the current must charge every segment of membrane sequentially, and the axon's internal resistance bleeds current away over distance. **Myelination** solves this problem by fundamentally changing the electrical properties of the axon, and understanding why requires thinking about the axon as a cable with specific physical parameters.

**Myelin** is formed by glial cells — oligodendrocytes in the central nervous system and Schwann cells in the peripheral nervous system — that wrap tightly around the axon in concentric layers of lipid-rich membrane. These wraps act as electrical insulation, dramatically increasing the membrane resistance (making it harder for current to leak out) and decreasing the membrane capacitance (reducing the charge needed to change the voltage). Think of the difference between a bare copper wire lying in water versus one coated in rubber insulation: the insulated wire loses far less current to the surrounding fluid, allowing the signal to travel much farther before it decays. Between the myelinated segments are small gaps called **Nodes of Ranvier**, where the axon membrane is exposed and densely packed with voltage-gated Na+ channels.

In **saltatory conduction** (from the Latin *saltare*, "to jump"), depolarization at one node generates enough current to flow passively through the myelinated internode — with minimal loss — all the way to the next node, where it triggers a fresh action potential. The signal effectively "jumps" from node to node rather than propagating continuously. Because passive current flow through the insulated internodes is nearly instantaneous compared to the time required for channel gating, the bottleneck is only at the nodes. The result is conduction speeds of approximately 50–120 m/s in large myelinated axons, compared to about 1–2 m/s in unmyelinated axons of similar diameter — roughly a 50-fold increase.

This speed gain comes with remarkable energy efficiency as well. Because ion exchange (and therefore the work of the Na+/K+ ATPase to restore gradients) occurs only at the nodes — which make up less than 1% of the axon's surface area — myelinated axons use far less ATP per action potential than unmyelinated ones. The evolutionary advantage is clear: myelination allows vertebrate nervous systems to have fast, long-range signaling without requiring enormous axon diameters (the alternative strategy used by the squid giant axon). The clinical importance is equally clear — diseases that destroy myelin, such as **multiple sclerosis**, cause dramatic slowing or complete failure of nerve conduction, producing symptoms ranging from numbness to paralysis, precisely because saltatory conduction depends on intact insulation between nodes.
