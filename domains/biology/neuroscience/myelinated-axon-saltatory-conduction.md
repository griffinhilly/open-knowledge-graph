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
stage: expert
status: draft
---

# Saltatory Conduction in Myelinated Axons

## Core Idea
Myelin insulation reduces capacitive loss; action potentials regenerate only at Nodes of Ranvier. Depolarization 'jumps' between nodes. ~50× faster than unmyelinated (~50 m/s).

## Questions

```yaml
- question: "A student argues: 'Myelinated axons conduct faster because myelin stimulates voltage-gated channels to open faster along the whole axon.' What is wrong with this explanation?"
  type: multiple-choice
  options:
    - "Nothing — myelin does increase channel opening rates throughout the axon"
    - "Myelin actually prevents action potentials from firing in myelinated segments; current flows passively through internodes and regenerates only at Nodes of Ranvier"
    - "The action potential fires at the same rate but has higher amplitude in myelinated axons"
    - "Myelinated axons are faster because ion channels in the internodes open more slowly, storing energy between nodes"
  answer: 1
  explanation: "Myelin electrically insulates the internode — there are virtually no voltage-gated channels there, and no action potentials fire in that region. Instead, depolarizing current from one node flows passively through the low-loss insulated internode to the next node, where it triggers a fresh action potential. The 'jumping' is passive current flow, not active channel opening. Speed comes from the near-instantaneous passive spread through insulated internodes, with the bottleneck only at node-to-node regeneration."

- question: "Multiple sclerosis demyelinates CNS axons. Which explanation best accounts for the resulting slowed or blocked nerve conduction?"
  type: multiple-choice
  options:
    - "Demyelination increases the number of Nodes of Ranvier, causing signal loss at too many regeneration points"
    - "Without myelin, axons lose their ATP supply from oligodendrocytes and action potentials fail energetically"
    - "Without myelin insulation, membrane capacitance increases and resistance decreases, so passive current decays before reaching the next node"
    - "Demyelination causes the Na⁺/K⁺ ATPase to reverse, collapsing the concentration gradients"
  answer: 2
  explanation: "Myelin's electrical role is to increase membrane resistance (reducing current leak) and decrease membrane capacitance (reducing charge needed to change voltage). When myelin is lost, current leaks out of the now-exposed internode, the capacitance load increases, and the passive depolarization decays before it reaches the next node with sufficient strength to trigger an action potential. Conduction either slows dramatically or blocks entirely — the saltatory mechanism requires intact insulation between nodes."

- question: "Saltatory conduction is more energy-efficient than continuous conduction because ion exchange (and the Na⁺/K⁺ ATPase work needed to restore gradients) occurs only at Nodes of Ranvier, which occupy less than 1% of the axon surface area."
  type: true-false
  answer: true
  explanation: "In continuous conduction, every stretch of membrane undergoes ion flux during each action potential, requiring the Na⁺/K⁺ ATPase to restore gradients across the entire surface. In saltatory conduction, the internode is insulated — no ions cross it — so ATPase work is confined to the nodes. Because nodes are tiny relative to the total axon length, the metabolic cost per action potential is dramatically lower. This efficiency is one reason vertebrates evolved myelination rather than the squid's strategy of simply using enormous-diameter axons."

- question: "Increasing axon diameter is the only evolutionary strategy available to speed up action potential conduction, which is why both myelinated vertebrate axons and the squid giant axon achieve fast conduction through large diameter."
  type: true-false
  answer: false
  explanation: "There are two distinct strategies for fast conduction: (1) increasing axon diameter, which reduces internal resistance and speeds continuous conduction — the squid uses this, reaching ~25 m/s with a ~1 mm diameter axon; and (2) myelination, which enables saltatory conduction, achieving 50–120 m/s in axons with diameters of only 1–20 µm. Vertebrates evolved the myelination strategy, achieving comparable or greater speeds at far smaller diameters and metabolic cost. The two strategies are alternatives, not equivalents."

- question: "Why does myelin increase conduction velocity? Explain in terms of the axon's cable properties."
  type: short-answer
  answer: "Myelin increases membrane resistance and decreases membrane capacitance in the internodal region. High resistance means very little depolarizing current leaks out through the internode membrane, so the current can travel farther along the axon interior without decaying. Low capacitance means less charge is needed to change the internode's voltage, so the passive current spreads quickly. The combined effect is that current originating at one node flows through the insulated internode nearly instantaneously and arrives at the next node with enough amplitude to trigger a fresh action potential. The signal jumps node-to-node (saltatory conduction) rather than engaging every patch of membrane sequentially, which is much slower."
  explanation: "The cable analogy is useful here: a bare wire in a conducting medium loses current to the surrounding fluid at every point; an insulated wire loses almost none. Myelin is the insulation. The physical consequences — increased resistance, decreased capacitance — are what make passive current spread fast and far, enabling the saltatory mechanism."
```

## Explainer

You have already seen how action potentials propagate along unmyelinated axons: depolarization at one point opens voltage-gated Na+ channels in the adjacent membrane, and the signal creeps forward in a continuous wave. This works, but it is slow — the current must charge every segment of membrane sequentially, and the axon's internal resistance bleeds current away over distance. **Myelination** solves this problem by fundamentally changing the electrical properties of the axon, and understanding why requires thinking about the axon as a cable with specific physical parameters.

**Myelin** is formed by glial cells — oligodendrocytes in the central nervous system and Schwann cells in the peripheral nervous system — that wrap tightly around the axon in concentric layers of lipid-rich membrane. These wraps act as electrical insulation, dramatically increasing the membrane resistance (making it harder for current to leak out) and decreasing the membrane capacitance (reducing the charge needed to change the voltage). Think of the difference between a bare copper wire lying in water versus one coated in rubber insulation: the insulated wire loses far less current to the surrounding fluid, allowing the signal to travel much farther before it decays. Between the myelinated segments are small gaps called **Nodes of Ranvier**, where the axon membrane is exposed and densely packed with voltage-gated Na+ channels.

In **saltatory conduction** (from the Latin *saltare*, "to jump"), depolarization at one node generates enough current to flow passively through the myelinated internode — with minimal loss — all the way to the next node, where it triggers a fresh action potential. The signal effectively "jumps" from node to node rather than propagating continuously. Because passive current flow through the insulated internodes is nearly instantaneous compared to the time required for channel gating, the bottleneck is only at the nodes. The result is conduction speeds of approximately 50–120 m/s in large myelinated axons, compared to about 1–2 m/s in unmyelinated axons of similar diameter — roughly a 50-fold increase.

This speed gain comes with remarkable energy efficiency as well. Because ion exchange (and therefore the work of the Na+/K+ ATPase to restore gradients) occurs only at the nodes — which make up less than 1% of the axon's surface area — myelinated axons use far less ATP per action potential than unmyelinated ones. The evolutionary advantage is clear: myelination allows vertebrate nervous systems to have fast, long-range signaling without requiring enormous axon diameters (the alternative strategy used by the squid giant axon). The clinical importance is equally clear — diseases that destroy myelin, such as **multiple sclerosis**, cause dramatic slowing or complete failure of nerve conduction, producing symptoms ranging from numbness to paralysis, precisely because saltatory conduction depends on intact insulation between nodes.
