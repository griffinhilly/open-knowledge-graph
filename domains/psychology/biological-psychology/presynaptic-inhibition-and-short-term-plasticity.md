---
id: presynaptic-inhibition-and-short-term-plasticity
title: Presynaptic Inhibition and Short-Term Synaptic Plasticity
domain: psychology
course: biological-psychology
prerequisites:
- id: synaptic-transmission-process
  type: hard
- id: ion-channels-and-neural-excitability
  type: hard
builds-toward:
- neural-integration-synaptic-plasticity
- motor-learning-cerebellar
tags:
- presynaptic
- inhibition
- short-term-plasticity
- facilitation
- depression
stage: advanced
status: draft
---

# Presynaptic Inhibition and Short-Term Synaptic Plasticity

## Core Idea
Presynaptic inhibition occurs when an inhibitory axon terminal contacts another neuron's axon terminal, reducing transmitter release by suppressing calcium influx. This provides gain control without affecting postsynaptic input resistance. Short-term plasticity—including facilitation and depression—reflects rapid changes in release probability and available vesicles over milliseconds to seconds, opposing long-term plasticity.

## How It's Best Learned
Study paired-pulse recordings showing facilitation vs depression by varying the interstimulus interval. Use voltage-clamp of presynaptic terminals to measure how GABA-B receptors reduce calcium current.

## Common Misconceptions
Presynaptic inhibition is not postsynaptic hyperpolarization; it directly reduces the probability of transmitter release. Short-term plasticity is a separate mechanism from long-term potentiation—it's transient and reverses in seconds.

## Explainer

You already know that synaptic transmission begins when an action potential invades an axon terminal, opens voltage-gated calcium channels, and triggers neurotransmitter release. You know that ion channels determine whether a neuron reaches threshold and fires. **Presynaptic inhibition** inserts a control point *before* any of that — it modulates transmission upstream of the postsynaptic cell entirely. An inhibitory axon terminal forms an **axoaxonic synapse** directly onto another neuron's terminal. When this inhibitory terminal releases GABA, it activates **GABA-B receptors** on the target terminal, which are coupled to potassium channels (increasing outward current) and to calcium channel suppression. Less calcium enters the terminal → fewer vesicles fuse → less transmitter is released.

The elegance of this mechanism lies in its selectivity. Postsynaptic inhibition — a chloride current from a GABA-A receptor on the soma or dendrite — reduces the cell's overall responsiveness to *all* its inputs simultaneously. Presynaptic inhibition can silence a single input pathway to a cell while leaving its other inputs completely unaffected. It also does not change the cell's input resistance, so the postsynaptic cell remains normally integrative. In sensory systems, this allows the nervous system to gate one modality (e.g., a particular touch receptor) without shutting down adjacent pathways — a kind of surgical quiet that broadband postsynaptic inhibition cannot achieve.

Now consider what happens during rapid repetitive firing at a single synapse. **Short-term plasticity** describes changes in synaptic strength lasting milliseconds to seconds — far shorter than the long-term potentiation (LTP) you may encounter elsewhere. **Facilitation** occurs when residual calcium from a first action potential lingers in the terminal, so the second pulse arrives into a higher calcium concentration and triggers more vesicle fusion than the first. This **paired-pulse facilitation** (the second response is larger than the first) is diagnostic: you measure it by applying two pulses at short intervals and comparing the amplitudes. Facilitation is most prominent at synapses with normally *low* release probability, where the initial response leaves room to grow.

The opposite pattern is **synaptic depression**: with rapid firing, each successive pulse triggers a smaller postsynaptic potential. The mechanism is vesicle depletion — the **readily releasable pool** of docked vesicles is consumed faster than it can be replenished from reserve stores. High-probability synapses (those that release a lot per pulse) deplete quickly and depress steeply. Far from being a limitation, depression and facilitation are computational: depression acts like a high-frequency filter, reducing the postsynaptic response to sustained low-frequency input while faithfully transmitting bursts; facilitation amplifies precisely the bursts that would otherwise be underrepresented. Together, these mechanisms allow the same synapse to perform different transformations depending on the firing pattern it receives — a dynamic computation built into the transmission machinery itself.
