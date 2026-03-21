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

## Questions

```yaml
- question: "An action potential arrives at a presynaptic terminal, but no neurotransmitter is detected in the cleft. Which explanation is most consistent with normal synaptic physiology?"
  type: multiple-choice
  options:
    - "The SNARE proteins are permanently fused and cannot open"
    - "The release probability of individual vesicles is less than 1, so it is possible for no vesicles to fuse on a given spike"
    - "Calcium channels must have been permanently closed due to repolarization"
    - "The synaptic cleft is too wide for neurotransmitter to diffuse across"
  answer: 1
  explanation: "Synaptic vesicle release is probabilistic — each docked vesicle has a release probability typically between 0.1 and 0.5 at many central synapses. On any given action potential, it is entirely possible that no vesicle happens to fuse. This is not a failure; it is the normal statistical nature of quantal release. Option A is wrong because SNARE proteins are not 'permanently fused' — they zip and unzip during each fusion event. Option C is wrong because calcium channels open normally during an action potential and then close during repolarization; this is expected and does not prevent transmission. Option D is wrong because the synaptic cleft (~20 nm) is easily traversed by diffusion."

- question: "Botulinum toxin causes flaccid paralysis while tetanus toxin causes spastic paralysis. Both toxins cleave SNARE proteins. What best explains the opposite clinical outcomes?"
  type: multiple-choice
  options:
    - "They cleave different SNARE proteins at different synapses: botulinum at excitatory motor synapses, tetanus at inhibitory spinal interneurons"
    - "Botulinum blocks calcium channels; tetanus blocks potassium channels"
    - "Tetanus toxin works presynaptically; botulinum toxin works postsynaptically"
    - "Botulinum cleaves the vesicle membrane; tetanus cleaves the postsynaptic receptor"
  answer: 0
  explanation: "Both toxins are SNARE-cleaving proteases, but they target different synaptic populations. Botulinum toxin acts at neuromuscular junctions (peripheral motor synapses), blocking acetylcholine release and preventing muscle activation — hence flaccid paralysis. Tetanus toxin is transported retrogradely into the spinal cord, where it cleaves SNARE proteins in inhibitory interneurons, blocking glycine/GABA release. Without inhibitory input, motor neurons fire uncontrollably — hence spastic paralysis. The lesson: the same molecular mechanism (SNARE cleavage) produces opposite clinical effects depending on which synapses are targeted."

- question: "Synaptic transmission is called 'quantal' because each vesicle releases a fixed, all-or-nothing packet of neurotransmitter."
  type: true-false
  answer: true
  explanation: "This is correct. A 'quantum' of neurotransmitter is the fixed package of molecules contained in a single synaptic vesicle — typically thousands of molecules. The quantal nature of release was demonstrated by del Castillo and Katz using miniature end-plate potentials (mEPPs), tiny spontaneous potentials that are integer multiples of a basic unit. The key insight is that release is granular, not continuous: you get 0, 1, 2, or more vesicles releasing, each contributing one quantum to the postsynaptic response."

- question: "A stronger (larger-amplitude) action potential will cause more neurotransmitter to be released from the presynaptic terminal."
  type: true-false
  answer: false
  explanation: "Action potentials are all-or-nothing events — a larger stimulus does not produce a larger action potential. The amplitude of the action potential at the terminal does not vary with stimulus intensity. What varies is the firing rate (how many APs per second) and, through other modulatory mechanisms, the release probability. The amount of neurotransmitter released per AP is determined by the local calcium influx, the number of docked vesicles, and their release probability — none of which depend on the AP amplitude itself. This is a critical distinction between graded potentials and action potentials."

- question: "Why is calcium influx — rather than the action potential voltage change itself — the direct trigger for synaptic vesicle fusion?"
  type: short-answer
  answer: "Calcium serves as a chemical second messenger that couples the electrical event (membrane depolarization) to the mechanical event (vesicle fusion). The SNARE machinery is already assembled and primed; what holds it back is a calcium-sensitive clamp. When Ca²⁺ enters through voltage-gated channels and binds synaptotagmin on the vesicle, it releases this constraint and allows the SNARE complex to complete membrane fusion. Voltage alone cannot do this — it only opens the Ca²⁺ channels that deliver the trigger."
  explanation: "This two-step design (voltage → Ca²⁺ → fusion) allows the synapse to be regulated at multiple levels. Release probability can be tuned by changing local calcium concentration (e.g., with drugs that block or enhance Ca²⁺ channels), by changing the distance between channels and vesicles, or by modifying synaptotagmin's calcium sensitivity. If voltage directly triggered fusion, the synapse would lose this flexibility and would be non-modulatable."
```

## Explainer

You know from the action potential that neurons communicate using electrical signals — rapid reversals of membrane voltage that propagate down the axon in an all-or-nothing fashion. The fundamental problem at the synapse is that electrical signals cannot jump directly from one neuron to the next: there is a narrow fluid-filled gap — the **synaptic cleft** — between the presynaptic terminal and the postsynaptic membrane. Synaptic transmission is the solution to this engineering problem: convert the electrical signal into a chemical signal, release that chemical across the gap, and let the postsynaptic cell convert it back into an electrical signal. This chemical relay is slower and more flexible than a direct electrical connection.

The process unfolds as a precise cascade. When the action potential invades the axon terminal, it opens **voltage-gated calcium channels** (VGCCs) in the presynaptic membrane. Calcium is at very low concentration inside the neuron, so it rushes in down its electrochemical gradient. This Ca²⁺ influx is the critical trigger for everything that follows. Calcium binds to **synaptotagmin**, a calcium-sensing protein on synaptic vesicles, which initiates the final membrane fusion event. Before this, vesicles are already "docked" at the active zone and "primed" — held in a ready state by the **SNARE complex**, a set of proteins that form a molecular zipper between the vesicle membrane and the plasma membrane. Synaptotagmin's calcium binding releases the final mechanical constraint, the membranes fuse, and the vesicle's contents are released into the cleft by exocytosis.

**Quantal release** is one of the most important concepts in synaptic physiology. A quantum is the contents of a single vesicle — a fixed package of roughly a few thousand neurotransmitter molecules. Synaptic transmission is probabilistic: even when an action potential arrives, each docked vesicle has a release probability that is typically less than 1 (often 0.1–0.5 at many central synapses). This means that on any given presynaptic spike, some vesicles release and others do not. The synapse is not a wire; it is a probabilistic switch whose gain can be tuned by short-term and long-term plasticity mechanisms. This probabilistic nature gives synapses their computational flexibility.

Two well-known toxins reveal the SNARE machinery with brutal clarity. **Botulinum toxin** is a protease that cleaves SNARE proteins at peripheral motor synapses, preventing vesicle fusion entirely and causing flaccid paralysis — muscles receive no acetylcholine release signal. **Tetanus toxin** targets inhibitory interneurons in the spinal cord, cleaving different SNARE proteins and blocking inhibitory neurotransmitter release — the result is uncontrolled excitation and spastic paralysis. Both toxins demonstrate the same point: SNARE-mediated exocytosis is not optional, it is the only mechanism available for neurotransmitter release, and disrupting it abolishes synaptic transmission entirely at the affected connections.
