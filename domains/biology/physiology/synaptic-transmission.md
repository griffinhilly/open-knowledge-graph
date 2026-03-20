---
id: synaptic-transmission
title: Synaptic Transmission
domain: biology
course: physiology
prerequisites:
- id: action-potential
  type: hard
- id: cell-signaling-intro
  type: hard
- id: organic-chemistry-intro
  type: soft
builds-toward:
- neuromuscular-junction
- nervous-system-overview
tags:
- synapse
- neurotransmitter
- chemical synapse
- receptor
- EPSP
- IPSP
stage: advanced
status: validated
---

# Synaptic Transmission

## Core Idea
Synaptic transmission converts an electrical signal in a presynaptic neuron into a chemical signal that crosses the synaptic cleft and is reconverted to electrical or biochemical signals in the postsynaptic cell. When an action potential reaches an axon terminal, voltage-gated Ca²⁺ channels open and Ca²⁺ influx triggers exocytosis of neurotransmitter-loaded vesicles. Neurotransmitters diffuse across the ~20 nm cleft and bind to postsynaptic receptors: ionotropic receptors open ion channels directly (fast, milliseconds), while metabotropic receptors activate G-protein cascades (slow, seconds to minutes). The signal is terminated by reuptake into the presynaptic terminal, enzymatic degradation, or diffusion away from the cleft.

## How It's Best Learned
Trace the seven-step sequence: AP arrives → Ca²⁺ enters → vesicles dock and fuse → neurotransmitter released → binds receptor → postsynaptic current flows → signal terminated. Compare an excitatory synapse (glutamate → AMPA receptor → Na⁺ influx → depolarization → EPSP) vs. an inhibitory synapse (GABA → GABA-A receptor → Cl⁻ influx → hyperpolarization → IPSP). Explain how spatial and temporal summation at the axon hillock determines whether an action potential fires.

## Common Misconceptions
- The chemical step at the synapse is not simply a relay — it introduces gain control, modulation, and plasticity that pure electrical transmission cannot provide.
- Inhibitory synapses do not silence the postsynaptic cell passively; they actively hyperpolarize it, requiring stronger excitatory input to reach threshold.
- One neurotransmitter can be excitatory or inhibitory depending on the receptor it binds — GABA is inhibitory at GABA-A but can be excitatory in early development.

## Questions

```yaml
- question: "What is the direct role of Ca²⁺ influx at the axon terminal when an action potential arrives?"
  type: multiple-choice
  options: ["It opens Na⁺ channels to depolarize the postsynaptic cell", "It triggers exocytosis of neurotransmitter-filled vesicles", "It hyperpolarizes the axon terminal to reset it for the next signal", "It binds to postsynaptic receptors to generate an EPSP"]
  answer: 1
  explanation: "Voltage-gated Ca²⁺ channels open when the action potential reaches the terminal, and the resulting Ca²⁺ influx is the direct trigger for vesicle docking and fusion (exocytosis), releasing neurotransmitter into the synaptic cleft. Ca²⁺ does not itself cross the cleft or bind postsynaptic receptors — it acts inside the presynaptic terminal as the coupling signal between electrical arrival and chemical release."

- question: "An inhibitory postsynaptic potential (IPSP) is produced when the postsynaptic neuron stops receiving electrical input and goes passive."
  type: true-false
  answer: false
  explanation: "An IPSP is an active process: inhibitory neurotransmitters (like GABA binding GABA-A receptors) open Cl⁻ channels, causing chloride to flow into the cell, actively hyperpolarizing the membrane potential further from threshold. The neuron does not simply go passive — it is pushed away from firing. This distinction matters clinically: drugs that enhance GABA-A activity (like benzodiazepines) actively suppress neural firing rather than just reducing excitation."

- question: "How can the same neurotransmitter produce excitatory effects at some synapses and inhibitory effects at others?"
  type: short-answer
  answer: "The effect depends on which receptor the neurotransmitter binds, not on the neurotransmitter itself. Different receptor types open different ion channels: if the channel conducts Na⁺ (inward), the membrane depolarizes (excitatory); if it conducts Cl⁻ or K⁺ (outward), the membrane hyperpolarizes (inhibitory). GABA is typically inhibitory, but in early development when Cl⁻ gradients are reversed, GABA-A activation causes Cl⁻ to flow outward, producing depolarization instead."
  explanation: "This is a fundamental principle: a chemical signal's effect is determined by the receiver, not the signal itself. The receptor defines what ion channel opens or what G-protein cascade activates. This gives the nervous system enormous flexibility — the same neurotransmitter released from different neurons can have opposite effects in different target cells or developmental stages."
```

## Explainer

Synaptic transmission is the mechanism by which a neuron converts the electrical signal of an action potential into a chemical message, sends that message across a tiny gap, and allows the receiving cell to convert it back into an electrical or biochemical response. You already understand action potentials — the rapid, all-or-none depolarization that travels down an axon. The synapse is what happens at the end.

When the action potential reaches the axon terminal, it depolarizes voltage-gated Ca²⁺ channels in the terminal membrane, causing Ca²⁺ to rush in from the extracellular space. This calcium influx is the coupling event: it triggers vesicles — tiny membrane-bound packages filled with neurotransmitter molecules — to dock with the terminal membrane and fuse with it, dumping their contents into the synaptic cleft. The cleft is only about 20 nanometers wide, so diffusion across it is nearly instantaneous.

On the other side, neurotransmitter molecules bind to postsynaptic receptors. The outcome depends entirely on the receptor type. Ionotropic receptors (like AMPA for glutamate, or GABA-A for GABA) are ion channels directly — binding the neurotransmitter opens the channel in milliseconds. Metabotropic receptors (like many dopamine receptors) instead activate G-proteins, which then launch slower but longer-lasting intracellular cascades. The ion that flows determines the effect: Na⁺ influx depolarizes (EPSP, excitatory); Cl⁻ influx hyperpolarizes (IPSP, inhibitory). Whether a neurotransmitter is excitatory or inhibitory is determined by the receptor it binds, not its own chemistry — the same GABA molecule can be inhibitory in an adult brain and excitatory in a fetal brain because the Cl⁻ gradient reverses during development.

A critical misconception to discard is the idea that the synapse is just a relay station. Chemical synapses introduce gain control: a single action potential can release more or fewer vesicles depending on recent activity (synaptic facilitation and depression). They introduce modulation: third-party inputs can strengthen or weaken a synapse (the basis of learning and memory, via long-term potentiation). And they enable computation: the postsynaptic neuron integrates hundreds of EPSPs and IPSPs arriving at different times (temporal summation) and different locations (spatial summation), and only fires a new action potential if the net depolarization at the axon hillock reaches threshold.

Signal termination is the final piece. If neurotransmitters stayed in the cleft indefinitely, the postsynaptic cell would never stop firing. Three mechanisms clear the cleft: reuptake transporters pull neurotransmitter back into the presynaptic terminal (the mechanism targeted by SSRIs, which block serotonin reuptake); enzymatic degradation breaks the neurotransmitter down in the cleft (acetylcholinesterase does this for acetylcholine); and simple diffusion dilutes what remains. Each mechanism has different kinetics and can be pharmacologically targeted — which is why understanding synaptic transmission is foundational to neuropharmacology.
