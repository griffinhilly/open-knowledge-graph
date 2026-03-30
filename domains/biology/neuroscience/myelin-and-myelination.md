---
id: myelin-and-myelination
title: Myelin Structure and Myelination
domain: biology
course: neuroscience
prerequisites:
- id: glial-cells-structure-function
  type: hard
- id: neuron-structure-and-function
  type: hard
builds-toward:
- saltatory-conduction
- cable-theory-axonal-conduction
tags:
- myelin
- myelination
- conduction-velocity
stage: advanced
status: validated
---

# Myelin Structure and Myelination

## Core Idea
Myelin is a lipid-rich insulating sheath wrapping axons in multiple layers, dramatically increasing conduction velocity through saltatory conduction at nodes of Ranvier. One Schwann cell myelinates a single internode in the PNS; oligodendrocytes myelinate segments of multiple axons in the CNS. Myelination is activity-dependent throughout life.

## How It's Best Learned
Calculate conduction velocity using cable equation parameters with and without myelin. Examine electron microscopy showing myelin lamellae.

## Common Misconceptions
Myelin completely isolates axons—it only insulates at nodes. Myelination is fixed after development—it's dynamic and regulates circuit speed.

## Questions

```yaml
- question: "A patient with multiple sclerosis has lost myelin from optic nerve axons. Which aspect of action potential propagation is most directly disrupted?"
  type: multiple-choice
  options:
    - "The generation of action potentials at the axon hillock is blocked"
    - "Saltatory conduction fails — current leaks through the demyelinated internode rather than jumping to the next node"
    - "Neurotransmitter release at the synapse is impaired because signals arrive with the wrong frequency"
    - "The resting membrane potential of the axon collapses, preventing repolarization"
  answer: 1
  explanation: "Myelin functions by insulating the axon between nodes of Ranvier, forcing current to flow longitudinally through the axon interior to the next node rather than leaking across the membrane. When myelin is destroyed, current leaks out along the demyelinated segment, reducing or blocking the signal at the next node. This disrupts saltatory conduction — the jumping pattern that makes myelinated conduction fast and efficient. The action potential slows, becomes unreliable, or fails entirely, depending on the severity of demyelination."

- question: "How does myelination by oligodendrocytes in the CNS differ from Schwann cell myelination in the PNS?"
  type: multiple-choice
  options:
    - "Oligodendrocytes myelinate a single axon completely, while Schwann cells only myelinate one segment"
    - "Schwann cells myelinate multiple axons simultaneously; oligodendrocytes myelinate only one axon at a time"
    - "A single oligodendrocyte can myelinate segments of multiple different axons; each Schwann cell myelinates one internode on one axon"
    - "There is no functional difference — the distinction is purely anatomical"
  answer: 2
  explanation: "In the PNS, each Schwann cell wraps around a single internode (segment) of a single axon. In the CNS, a single oligodendrocyte extends multiple processes and can myelinate internodes on 30–60 different axons simultaneously. This architectural difference has clinical implications: oligodendrocyte loss in CNS diseases like multiple sclerosis can simultaneously disrupt conduction in many axons, while PNS demyelinating conditions (like Guillain-Barré syndrome) affect individual Schwann cells but cannot have the same multi-axon impact from a single cell's loss."

- question: "Saltatory conduction is more energy-efficient than continuous conduction along an unmyelinated axon because ions only cross the membrane at nodes of Ranvier rather than along the entire axon length."
  type: true-false
  answer: true
  explanation: "Each patch of membrane that undergoes an action potential requires Na⁺/K⁺-ATPase activity afterward to restore ion gradients — this is metabolically expensive. In unmyelinated axons, every patch of membrane along the entire axon length depolarizes sequentially. In myelinated axons, the membrane is only breached at widely spaced nodes, so only those small regions require ion pumping. This dramatically reduces metabolic cost while increasing speed. The CNS contains enormous numbers of axons, making energy efficiency a critical design constraint."

- question: "Myelination is a fixed developmental process — once axons are myelinated in early life, the myelin sheath thickness and internode length remain unchanged in adult nervous systems."
  type: true-false
  answer: false
  explanation: "This is a major misconception corrected by recent research. Myelination is activity-dependent and continues throughout life. Neurons that fire more frequently can signal to oligodendrocyte precursor cells to promote new myelin formation or modify existing myelin properties (thickness, internode length). This adaptive myelination fine-tunes conduction velocity to synchronize signals across circuits requiring precise timing. It also means that learning and experience physically reshape white matter — skills acquired in adulthood involve measurable changes in myelin structure."

- question: "Why does myelination increase conduction velocity without requiring a larger axon diameter, and what physical mechanism achieves this?"
  type: short-answer
  answer: "Unmyelinated axons conduct by sequentially depolarizing every adjacent patch of membrane — like dominoes falling one at a time. Increasing conduction speed in unmyelinated axons requires a larger axon diameter (which reduces internal resistance), but this has physical limits. Myelination bypasses this constraint through saltatory conduction: the myelin sheath insulates the axon membrane between nodes of Ranvier, preventing current from leaking out. When an action potential fires at one node, the current flows rapidly down the low-resistance axon interior to the next node (skipping the insulated internode), where it triggers a new action potential. This jumping pattern is faster because the signal travels as a passive electrical current through cytoplasm rather than slowly regenerating through each membrane patch, and it works even in thin axons because the insulation eliminates the leakage that would otherwise require larger diameter."
  explanation: "This is why vertebrates can have fast-conducting nerve fibers just a few micrometers across, while the squid must use a 1mm-diameter giant axon to achieve comparable speeds without myelin."
```

## Explainer

You already know that glial cells are non-neuronal partners in the nervous system and that neurons transmit signals along axons as electrical impulses. Myelin is where these two concepts converge: glial cells wrap axons in insulation that transforms how electrical signals travel, solving a fundamental engineering problem of the nervous system.

The problem is speed. An unmyelinated axon conducts action potentials by sequentially depolarizing each adjacent patch of membrane — like a row of dominoes falling one after another. This works, but it is slow (about 0.5–2 m/s for thin unmyelinated fibers) and metabolically expensive, because every patch of membrane that depolarizes requires Na⁺/K⁺-ATPase activity to restore ion gradients afterward. To conduct faster without myelin, axons must be thicker — the giant axon of the squid reaches 1 mm in diameter to achieve about 25 m/s. Vertebrate nervous systems found a different solution: **myelination**, which achieves 100+ m/s in axons just a few micrometers across.

**Myelin** is formed when a glial cell wraps its membrane around an axon multiple times, creating a tight spiral of lipid bilayers — sometimes 100 or more layers thick. In the peripheral nervous system, each **Schwann cell** wraps a single segment (called an **internode**) of one axon. In the central nervous system, a single **oligodendrocyte** extends multiple processes, each myelinating a segment on a different axon — one oligodendrocyte can service 30–60 internodes across many axons. Between adjacent myelinated segments are small gaps called **nodes of Ranvier** where the axon membrane is exposed and packed with voltage-gated Na⁺ channels. The myelin acts as an electrical insulator: current entering at one node cannot leak out through the myelinated internode, so it flows rapidly down the axon interior to the next node, where it triggers a new action potential. This jumping pattern — **saltatory conduction** — is both faster and more energy-efficient, because ions only cross the membrane at nodes rather than along the entire axon length.

A critical insight from recent research is that myelination is not a fixed developmental event — it is **activity-dependent** and continues throughout life. Neurons that fire more frequently can signal to oligodendrocyte precursor cells, promoting new myelin formation or adjustments to existing myelin thickness and internode length. This **adaptive myelination** fine-tunes conduction velocity to synchronize signals across circuits that need precise timing, such as auditory processing pathways. It also means that learning and experience physically reshape the brain's white matter. Demyelinating diseases like multiple sclerosis illustrate what happens when this insulation fails: action potentials slow, become unreliable, or block entirely, producing the varied neurological symptoms — vision loss, weakness, coordination problems — that depend on which axon tracts lose their myelin.
