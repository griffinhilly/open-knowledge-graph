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
tags:
- presynaptic
- inhibition
- short-term-plasticity
- facilitation
- depression
stage: advanced
status: validated
---

# Presynaptic Inhibition and Short-Term Synaptic Plasticity

## Core Idea
Presynaptic inhibition occurs when an inhibitory axon terminal contacts another neuron's axon terminal, reducing transmitter release by suppressing calcium influx. This provides gain control without affecting postsynaptic input resistance. Short-term plasticity—including facilitation and depression—reflects rapid changes in release probability and available vesicles over milliseconds to seconds, opposing long-term plasticity.

## How It's Best Learned
Study paired-pulse recordings showing facilitation vs depression by varying the interstimulus interval. Use voltage-clamp of presynaptic terminals to measure how GABA-B receptors reduce calcium current.

## Common Misconceptions
Presynaptic inhibition is not postsynaptic hyperpolarization; it directly reduces the probability of transmitter release. Short-term plasticity is a separate mechanism from long-term potentiation—it's transient and reverses in seconds.

## Questions

```yaml
- question: "Neuron A receives inputs from both neuron B (excitatory) and neuron C (inhibitory). The inhibitory input from C contacts the axon terminal of B directly (axoaxonic synapse), activating GABA-B receptors on B's terminal. What is the immediate consequence for neuron A?"
  type: multiple-choice
  options:
    - "Neuron A is hyperpolarized — it receives a direct inhibitory current from the axoaxonic synapse"
    - "Neuron A's input resistance decreases, making it less responsive to all inputs simultaneously"
    - "The amount of neurotransmitter released from B onto A is reduced, because GABA-B receptor activation suppresses calcium influx in B's terminal — but A's intrinsic properties are unchanged"
    - "Neuron B fires an action potential that propagates to neuron A, but the action potential is smaller in amplitude"
  answer: 2
  explanation: "This is the defining feature of presynaptic inhibition: control at the presynaptic terminal, not at the postsynaptic cell. GABA-B receptors on B's terminal are coupled to potassium channels and calcium channel suppression. Less calcium enters B's terminal → fewer vesicles fuse → less glutamate released onto A. Neuron A receives no direct inhibitory current and its input resistance is unchanged. Compare to postsynaptic inhibition via GABA-A: that would hyperpolarize A (option A) and reduce A's responsiveness to all inputs simultaneously. Presynaptic inhibition is selective — it silences only the B→A pathway, leaving all other inputs to A unaffected."

- question: "A synapse shows paired-pulse facilitation: the second postsynaptic potential is larger than the first when two stimuli are delivered 20 ms apart. What does this pattern reveal about the synapse's normal release probability?"
  type: multiple-choice
  options:
    - "The synapse has high release probability — the large second response shows robust vesicle replenishment"
    - "The synapse has low release probability — residual calcium from the first pulse adds to the second, producing a larger release because there was room to grow"
    - "The synapse is undergoing long-term potentiation, and the facilitated response reflects the early phase of LTP"
    - "The synapse's readily releasable pool is being replenished between pulses, causing the larger second response"
  answer: 1
  explanation: "Paired-pulse facilitation is diagnostic of low initial release probability. At a low-probability synapse, the first pulse releases few vesicles because calcium triggers only modest fusion. Residual calcium that remains in the terminal after the first pulse adds to the calcium influx from the second pulse, producing a higher peak calcium concentration and more vesicle fusion. Because the initial response was small (few vesicles fused), a large pool of readily-releasable vesicles remains, so the second response can be much larger. High-probability synapses show depression rather than facilitation, because most available vesicles are depleted by the first pulse."

- question: "Presynaptic inhibition reduces the responsiveness of a neuron to most of its incoming inputs simultaneously, providing global gain control."
  type: true-false
  answer: false
  explanation: "This is false — it describes postsynaptic inhibition, not presynaptic. Presynaptic inhibition acts via axoaxonic synapses on a specific input terminal, reducing transmitter release from that terminal only. The postsynaptic cell's intrinsic properties (input resistance, resting membrane potential, threshold) are unchanged, and all other inputs to the postsynaptic cell remain fully effective. This input-specific selectivity is the key advantage: it allows the nervous system to silence one pathway without broadly suppressing the downstream neuron — a surgical precision that broadband postsynaptic inhibition cannot achieve."

- question: "Synaptic depression at a high-frequency synapse reflects a malfunction in vesicle replenishment rather than a normal feature of transmission."
  type: true-false
  answer: false
  explanation: "Synaptic depression is a normal, computationally significant feature of high-probability synapses stimulated at high frequency. When each action potential releases a large fraction of the readily releasable vesicle pool, sustained activity depletes vesicles faster than they can be replenished from reserve stores. The result is a decreasing postsynaptic response with successive stimuli. Far from being a failure, this is a low-pass filter: sustained low-frequency inputs are progressively attenuated, while novel bursts stand out. Depression and facilitation together implement different frequency-dependent transformations that are built into the transmission machinery — they are computations, not errors."

- question: "Explain why presynaptic inhibition provides more surgically precise control than postsynaptic inhibition, and give a physiological context where this precision would be functionally important."
  type: short-answer
  answer: "Postsynaptic inhibition (e.g., GABA-A receptor activation on the soma or dendrites) injects inhibitory current into the postsynaptic cell, reducing its responsiveness to all inputs by hyperpolarizing it or reducing its input resistance. This is broadband — it gates everything simultaneously. Presynaptic inhibition via axoaxonic synapses targets a single input terminal: only the transmitter release from that specific terminal is reduced, leaving all other inputs to the postsynaptic cell unaffected. In sensory processing, this allows gating of one sensory modality — for example, reducing pain signals from a specific receptor during descending opioid modulation — without suppressing all other somatosensory input to the same spinal neuron."
  explanation: "A classic example occurs in the spinal cord dorsal horn. Primary afferent fibers carrying pain (Aδ and C fibers) can be presynaptically inhibited by interneurons and descending fibers, reducing their transmitter release onto projection neurons. Meanwhile, the projection neuron can still respond normally to non-pain inputs arriving via other terminals. Postsynaptic inhibition of the same projection neuron would indiscriminately block all sensory transmission. The selectivity of presynaptic inhibition makes it the preferred mechanism when modality-specific gating is needed."
```

## Explainer

You already know that synaptic transmission begins when an action potential invades an axon terminal, opens voltage-gated calcium channels, and triggers neurotransmitter release. You know that ion channels determine whether a neuron reaches threshold and fires. **Presynaptic inhibition** inserts a control point *before* any of that — it modulates transmission upstream of the postsynaptic cell entirely. An inhibitory axon terminal forms an **axoaxonic synapse** directly onto another neuron's terminal. When this inhibitory terminal releases GABA, it activates **GABA-B receptors** on the target terminal, which are coupled to potassium channels (increasing outward current) and to calcium channel suppression. Less calcium enters the terminal → fewer vesicles fuse → less transmitter is released.

The elegance of this mechanism lies in its selectivity. Postsynaptic inhibition — a chloride current from a GABA-A receptor on the soma or dendrite — reduces the cell's overall responsiveness to *all* its inputs simultaneously. Presynaptic inhibition can silence a single input pathway to a cell while leaving its other inputs completely unaffected. It also does not change the cell's input resistance, so the postsynaptic cell remains normally integrative. In sensory systems, this allows the nervous system to gate one modality (e.g., a particular touch receptor) without shutting down adjacent pathways — a kind of surgical quiet that broadband postsynaptic inhibition cannot achieve.

Now consider what happens during rapid repetitive firing at a single synapse. **Short-term plasticity** describes changes in synaptic strength lasting milliseconds to seconds — far shorter than the long-term potentiation (LTP) you may encounter elsewhere. **Facilitation** occurs when residual calcium from a first action potential lingers in the terminal, so the second pulse arrives into a higher calcium concentration and triggers more vesicle fusion than the first. This **paired-pulse facilitation** (the second response is larger than the first) is diagnostic: you measure it by applying two pulses at short intervals and comparing the amplitudes. Facilitation is most prominent at synapses with normally *low* release probability, where the initial response leaves room to grow.

The opposite pattern is **synaptic depression**: with rapid firing, each successive pulse triggers a smaller postsynaptic potential. The mechanism is vesicle depletion — the **readily releasable pool** of docked vesicles is consumed faster than it can be replenished from reserve stores. High-probability synapses (those that release a lot per pulse) deplete quickly and depress steeply. Far from being a limitation, depression and facilitation are computational: depression acts like a high-frequency filter, reducing the postsynaptic response to sustained low-frequency input while faithfully transmitting bursts; facilitation amplifies precisely the bursts that would otherwise be underrepresented. Together, these mechanisms allow the same synapse to perform different transformations depending on the firing pattern it receives — a dynamic computation built into the transmission machinery itself.
