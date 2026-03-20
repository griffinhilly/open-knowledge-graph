---
id: synaptic-transmission-process
title: Synaptic Transmission Process
domain: psychology
course: biological-psychology
prerequisites:
- id: action-potential-generation-and-propagation
  type: hard
- id: synaptic-vesicle-release-exocytosis
  type: soft
- id: synaptic-transmission
  type: hard
builds-toward:
- neurotransmitter-receptor-binding
tags:
- synapse
- vesicles
- exocytosis
- presynaptic
stage: advanced
status: draft
---

# Synaptic Transmission Process

## Core Idea
Synaptic transmission is a multi-step process: action potentials invade the axon terminal, opening voltage-gated Ca2+ channels; Ca2+ influx triggers synaptic vesicles to fuse with the presynaptic membrane via SNARE proteins (SNARE-mediated exocytosis); neurotransmitter molecules are released into the synaptic cleft; they diffuse across and bind postsynaptic receptors. This converts an electrical signal into a chemical one.

## How It's Best Learned
Study the complete anatomy of the synaptic terminal using electron microscopy. Watch real-time imaging of vesicle fusion and exocytosis. Measure quantal size (single vesicle events) using patch-clamp recording. Examine effects of toxins (botulinum, tetanus) that block SNARE proteins.

## Common Misconceptions
Neurotransmitter flows continuously / the synapse works like an electrical wire / vesicle release is purely deterministic / all synapses release neurotransmitter the same way.

## Explainer

You know from the action potential that neurons communicate using electrical signals — rapid reversals of membrane voltage that propagate down the axon in an all-or-nothing fashion. The fundamental problem at the synapse is that electrical signals cannot jump directly from one neuron to the next: there is a narrow fluid-filled gap — the **synaptic cleft** — between the presynaptic terminal and the postsynaptic membrane. Synaptic transmission is the solution to this engineering problem: convert the electrical signal into a chemical signal, release that chemical across the gap, and let the postsynaptic cell convert it back into an electrical signal. This chemical relay is slower and more flexible than a direct electrical connection.

The process unfolds as a precise cascade. When the action potential invades the axon terminal, it opens **voltage-gated calcium channels** (VGCCs) in the presynaptic membrane. Calcium is at very low concentration inside the neuron, so it rushes in down its electrochemical gradient. This Ca²⁺ influx is the critical trigger for everything that follows. Calcium binds to **synaptotagmin**, a calcium-sensing protein on synaptic vesicles, which initiates the final membrane fusion event. Before this, vesicles are already "docked" at the active zone and "primed" — held in a ready state by the **SNARE complex**, a set of proteins that form a molecular zipper between the vesicle membrane and the plasma membrane. Synaptotagmin's calcium binding releases the final mechanical constraint, the membranes fuse, and the vesicle's contents are released into the cleft by exocytosis.

**Quantal release** is one of the most important concepts in synaptic physiology. A quantum is the contents of a single vesicle — a fixed package of roughly a few thousand neurotransmitter molecules. Synaptic transmission is probabilistic: even when an action potential arrives, each docked vesicle has a release probability that is typically less than 1 (often 0.1–0.5 at many central synapses). This means that on any given presynaptic spike, some vesicles release and others do not. The synapse is not a wire; it is a probabilistic switch whose gain can be tuned by short-term and long-term plasticity mechanisms. This probabilistic nature gives synapses their computational flexibility.

Two well-known toxins reveal the SNARE machinery with brutal clarity. **Botulinum toxin** is a protease that cleaves SNARE proteins at peripheral motor synapses, preventing vesicle fusion entirely and causing flaccid paralysis — muscles receive no acetylcholine release signal. **Tetanus toxin** targets inhibitory interneurons in the spinal cord, cleaving different SNARE proteins and blocking inhibitory neurotransmitter release — the result is uncontrolled excitation and spastic paralysis. Both toxins demonstrate the same point: SNARE-mediated exocytosis is not optional, it is the only mechanism available for neurotransmitter release, and disrupting it abolishes synaptic transmission entirely at the affected connections.
