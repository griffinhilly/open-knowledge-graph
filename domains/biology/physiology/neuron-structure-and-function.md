---
id: neuron-structure-and-function
title: Neuron Structure and Function
domain: biology
course: physiology
prerequisites:
- id: eukaryotic-cells
  type: hard
- id: cell-membrane-structure
  type: hard
builds-toward:
- action-potential
- synaptic-transmission
- nervous-system-overview
tags:
- neuron
- dendrites
- axon
- myelin
- nervous system
stage: advanced
status: validated
---

# Neuron Structure and Function

## Core Idea
Neurons are electrically excitable cells specialized for rapid signal transmission. A typical neuron consists of a cell body (soma) containing the nucleus and organelles, dendrites that receive and integrate incoming signals, and an axon that conducts electrical signals away from the soma to synaptic terminals. Many axons are wrapped in myelin sheaths produced by Schwann cells (PNS) or oligodendrocytes (CNS), which insulate the axon and enable saltatory conduction at nodes of Ranvier — dramatically increasing signal speed. The axon hillock, where the axon emerges from the soma, is the site where incoming signals summate and action potentials are initiated if threshold is reached.

## How It's Best Learned
Draw a labeled neuron from memory, identifying soma, dendrites, axon hillock, axon, myelin sheath, nodes of Ranvier, and axon terminals. Compare myelinated vs. unmyelinated conduction velocity and correlate with the biological importance of speed: fast motor commands and pain reflexes require myelination, while slowly conducted pain uses unmyelinated C fibers.

## Common Misconceptions
- Neurons are not the only cells in the nervous system; glial cells (astrocytes, oligodendrocytes, microglia, Schwann cells) outnumber neurons and actively regulate the neural environment.
- Not all neurons have the classic soma-dendrite-axon shape; sensory neurons (pseudounipolar) and many interneurons differ substantially in morphology.

## Questions

```yaml
- question: "At which location on a neuron is the action potential typically initiated?"
  type: multiple-choice
  options: ["At the tips of the dendrites, where signals are received", "At the soma, where the nucleus integrates information", "At the axon hillock, where the axon emerges from the soma", "At the axon terminal, just before the synapse"]
  answer: 2
  explanation: "The axon hillock has the highest density of voltage-gated sodium channels and the lowest threshold for firing. Incoming signals from dendrites and the soma summate at the axon hillock; if the combined depolarization reaches threshold, an action potential is triggered there and propagates down the axon."

- question: "Myelin sheaths wrap the axon in a continuous, unbroken insulating layer along its entire length."
  type: true-false
  answer: false
  explanation: "Myelin wraps the axon in segments, with small gaps called nodes of Ranvier left exposed between each segment. These gaps are essential: voltage-gated sodium channels are concentrated at the nodes, and the action potential 'jumps' from node to node (saltatory conduction). A completely unbroken myelin sheath would actually prevent propagation."

- question: "How does myelination increase the speed of action potential propagation along an axon?"
  type: short-answer
  answer: "Myelin electrically insulates the axon between nodes of Ranvier, preventing ion leakage and forcing the action potential to 'jump' from one node to the next (saltatory conduction) rather than propagating continuously along the entire membrane. This is much faster because the electrical signal spreads passively and rapidly through the insulated segments, and regeneration only needs to occur at the widely spaced nodes."
  explanation: "Unmyelinated axons depolarize every patch of membrane in sequence, which is slow and metabolically expensive. Saltatory conduction reduces both the time and energy cost of propagation. This is why demyelinating diseases like multiple sclerosis — where myelin is damaged — cause profound deficits in motor and sensory function."
```

## Explainer

You already know from cell biology that neurons are eukaryotic cells with all the standard organelles. What makes neurons unique is their extreme specialization for receiving, integrating, and transmitting electrical signals — and the remarkable anatomical shape that serves this function.

The soma (cell body) is the metabolic hub. It contains the nucleus, ribosomes, and most organelles, and it is responsible for producing the proteins the neuron needs. Branching off the soma are dendrites — thin, tree-like processes that receive incoming signals from other neurons or sensory receptors. The dendritic tree can be vast; some neurons in the brain receive thousands of inputs across their dendrites simultaneously. All of these signals — some excitatory, some inhibitory — converge on the soma and ultimately on the axon hillock.

The axon hillock is a critical chokepoint. It is where the axon emerges from the soma, and it has the highest density of voltage-gated sodium channels anywhere on the neuron. This means it has the lowest threshold for firing an action potential. Think of it as the neuron's "decision point": if the integrated input arriving from dendrites and the soma is strong enough to depolarize the axon hillock to threshold, the neuron fires. Below threshold, it stays silent.

The axon carries the action potential away from the soma toward synaptic terminals, where the signal is passed on to the next cell. Many axons are wrapped in a myelin sheath — a multilayer lipid coating produced by glial cells (Schwann cells in the peripheral nervous system, oligodendrocytes in the central nervous system). Myelin insulates the axon, but it is not continuous: small gaps called nodes of Ranvier are left exposed at regular intervals. The action potential essentially jumps from node to node — saltatory conduction — which is dramatically faster than propagating continuously through unmyelinated membrane. Fast, precise movements and quick reflexes depend on myelination.

It is worth noting that neurons are not the whole story in the nervous system. Glial cells — including astrocytes, oligodendrocytes, microglia (CNS), and Schwann cells (PNS) — actually outnumber neurons and actively regulate the neural environment: maintaining ion concentrations, providing structural support, pruning synapses, and responding to injury. The stereotype of neurons as the only "real" cells in the brain is a significant oversimplification.
