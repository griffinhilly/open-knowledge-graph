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
status: draft
---

# Myelin Structure and Myelination

## Core Idea
Myelin is a lipid-rich insulating sheath wrapping axons in multiple layers, dramatically increasing conduction velocity through saltatory conduction at nodes of Ranvier. One Schwann cell myelinates a single internode in the PNS; oligodendrocytes myelinate segments of multiple axons in the CNS. Myelination is activity-dependent throughout life.

## How It's Best Learned
Calculate conduction velocity using cable equation parameters with and without myelin. Examine electron microscopy showing myelin lamellae.

## Common Misconceptions
Myelin completely isolates axons—it only insulates at nodes. Myelination is fixed after development—it's dynamic and regulates circuit speed.

## Explainer

You already know that glial cells are non-neuronal partners in the nervous system and that neurons transmit signals along axons as electrical impulses. Myelin is where these two concepts converge: glial cells wrap axons in insulation that transforms how electrical signals travel, solving a fundamental engineering problem of the nervous system.

The problem is speed. An unmyelinated axon conducts action potentials by sequentially depolarizing each adjacent patch of membrane — like a row of dominoes falling one after another. This works, but it is slow (about 0.5–2 m/s for thin unmyelinated fibers) and metabolically expensive, because every patch of membrane that depolarizes requires Na⁺/K⁺-ATPase activity to restore ion gradients afterward. To conduct faster without myelin, axons must be thicker — the giant axon of the squid reaches 1 mm in diameter to achieve about 25 m/s. Vertebrate nervous systems found a different solution: **myelination**, which achieves 100+ m/s in axons just a few micrometers across.

**Myelin** is formed when a glial cell wraps its membrane around an axon multiple times, creating a tight spiral of lipid bilayers — sometimes 100 or more layers thick. In the peripheral nervous system, each **Schwann cell** wraps a single segment (called an **internode**) of one axon. In the central nervous system, a single **oligodendrocyte** extends multiple processes, each myelinating a segment on a different axon — one oligodendrocyte can service 30–60 internodes across many axons. Between adjacent myelinated segments are small gaps called **nodes of Ranvier** where the axon membrane is exposed and packed with voltage-gated Na⁺ channels. The myelin acts as an electrical insulator: current entering at one node cannot leak out through the myelinated internode, so it flows rapidly down the axon interior to the next node, where it triggers a new action potential. This jumping pattern — **saltatory conduction** — is both faster and more energy-efficient, because ions only cross the membrane at nodes rather than along the entire axon length.

A critical insight from recent research is that myelination is not a fixed developmental event — it is **activity-dependent** and continues throughout life. Neurons that fire more frequently can signal to oligodendrocyte precursor cells, promoting new myelin formation or adjustments to existing myelin thickness and internode length. This **adaptive myelination** fine-tunes conduction velocity to synchronize signals across circuits that need precise timing, such as auditory processing pathways. It also means that learning and experience physically reshape the brain's white matter. Demyelinating diseases like multiple sclerosis illustrate what happens when this insulation fails: action potentials slow, become unreliable, or block entirely, producing the varied neurological symptoms — vision loss, weakness, coordination problems — that depend on which axon tracts lose their myelin.
