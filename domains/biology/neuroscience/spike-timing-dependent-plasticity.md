---
id: spike-timing-dependent-plasticity
title: Spike-Timing-Dependent Plasticity
domain: biology
course: neuroscience
prerequisites:
- id: long-term-potentiation
  type: hard
- id: long-term-depression
  type: hard
- id: nmda-receptor-structure
  type: hard
builds-toward:
- hebbian-learning
- circuit-development
- learning-memory
tags:
- stdp
- spike-timing
- causality
stage: expert
status: validated
---

# Spike-Timing-Dependent Plasticity

## Core Idea
Spike-timing-dependent plasticity is Hebbian learning where timing of presynaptic and postsynaptic spikes determines synaptic change: presynaptic firing before postsynaptic (causal, positive Δt) causes LTP; reverse timing causes LTD. The learning window spans tens of milliseconds and reflects NMDA receptor-mediated calcium signaling.

## How It's Best Learned
Use voltage clamp with precise spike pairings. Plot plasticity magnitude vs. spike timing.

## Common Misconceptions
STDP always follows one rule—rules vary across synapses. All synapses use STDP—it's one of several plasticity mechanisms.

## Questions

```yaml
- question: "A postsynaptic neuron fires an action potential, and then 15 milliseconds later the presynaptic neuron fires. According to the STDP rule, what happens to this synapse?"
  type: multiple-choice
  options:
    - "The synapse is strengthened (LTP), because both neurons fired within the plasticity window"
    - "The synapse is weakened (LTD), because the presynaptic input arrived after the postsynaptic spike and cannot have caused it"
    - "No change occurs, because 15 milliseconds is outside the plasticity window"
    - "The synapse is strengthened (LTP), because the postsynaptic neuron fired first and set up the NMDA receptor for coincidence detection"
  answer: 1
  explanation: "STDP is directional — the temporal order of pre- and postsynaptic firing, not just their proximity, determines the outcome. When post fires before pre, the presynaptic input arrived too late to have contributed to the postsynaptic spike, so the connection is weakened (LTD). This 'reverse' timing signals that the synapse is not contributing causally to the postsynaptic neuron's behavior. LTP only occurs when pre fires first (within ~20ms), which is consistent with a causal role: the presynaptic neuron may have helped trigger the postsynaptic spike."

- question: "How does the NMDA receptor produce LTP when pre fires before post, but LTD when post fires before pre — given that the same receptor is involved in both cases?"
  type: multiple-choice
  options:
    - "Different NMDA receptor subtypes are activated depending on which neuron fires first"
    - "Pre-before-post timing produces a large, fast calcium influx that activates kinases; post-before-pre produces a weaker, slower calcium signal that activates phosphatases instead"
    - "Post-before-pre timing causes NMDA receptors to conduct potassium instead of calcium, activating a different signaling pathway"
    - "The NMDA receptor is only activated when pre fires first; reverse timing does not open NMDA receptors at all"
  answer: 1
  explanation: "The same receptor produces opposite outcomes because calcium signal amplitude and kinetics differ based on timing. Pre-before-post: glutamate arrives first, binds NMDA; then the postsynaptic depolarization (arriving milliseconds later) expels the Mg²⁺ block while strong voltage is present, producing a large, fast calcium influx. This high [Ca²⁺] activates CaMKII and other kinases → AMPA receptor insertion → LTP. Post-before-pre: postsynaptic depolarization has already faded when glutamate arrives, so NMDA opens under weak depolarization → smaller, slower calcium signal. This low [Ca²⁺] preferentially activates phosphatases like calcineurin → AMPA receptor removal → LTD."

- question: "In STDP, the amplitude and kinetics of calcium influx through NMDA receptors are the key signal that determines whether a synapse undergoes LTP or LTD."
  type: true-false
  answer: true
  explanation: "This is the central mechanistic insight of STDP. The same NMDA receptor can drive either LTP or LTD depending on the calcium signal it produces. Large, fast calcium transients (produced by pre-before-post timing with strong postsynaptic depolarization) activate high-affinity kinases like CaMKII, driving AMPA receptor insertion and LTP. Small, slow calcium transients (produced by poor timing coincidence) preferentially activate calcineurin and other phosphatases, driving AMPA receptor internalization and LTD. The calcium amplitude and time course act as a biochemical switch between the two outcomes."

- question: "STDP follows a universal rule across most synapse types: pre-before-post timing generally causes LTP, and post-before-pre timing generally causes LTD."
  type: true-false
  answer: false
  explanation: "The 'classic' asymmetric STDP rule describes the most common pattern at excitatory cortical and hippocampal synapses, but it is not universal. Inhibitory synapses can show inverted rules. Some synapses show symmetric plasticity windows where timing direction doesn't matter. Others show different time constants or threshold requirements. STDP rules are tuned to the computational needs of specific circuits, meaning the brain uses multiple plasticity mechanisms rather than a single universal rule. The diversity reflects the fact that different neural circuits need to learn different things — causal sequences, coincidences, or other temporal patterns."

- question: "Explain how NMDA receptor biophysics implement a spike-timing-based learning rule. Why does the order of pre- and postsynaptic spikes determine whether a synapse is strengthened or weakened?"
  type: short-answer
  answer: "NMDA receptors require two simultaneous conditions to open: glutamate binding (signaling presynaptic activity) and postsynaptic depolarization (expelling the Mg²⁺ block). When pre fires before post, glutamate is present when the backpropagating postsynaptic action potential arrives, producing strong coincidence detection and a large calcium influx. This drives LTP. When post fires before pre, the postsynaptic depolarization has already decayed before glutamate arrives, so the Mg²⁺ block is only partially relieved, producing a weak calcium signal that drives LTD instead."
  explanation: "The NMDA receptor's voltage-dependent Mg²⁺ block is the physical implementation of a temporal coincidence detector. It acts like an AND gate: calcium only flows well when both 'pre spike' (glutamate) and 'post spike' (depolarization) occur together. The temporal asymmetry — LTP for pre-first, LTD for post-first — emerges from the kinetics: postsynaptic depolarization decays over milliseconds, so by the time delayed presynaptic input arrives in the post-before-pre case, the depolarization signal has weakened. The calcium signal's amplitude and time course then route through different intracellular pathways (kinases vs. phosphatases), producing the asymmetric plasticity rule."
```

## Explainer

You already know that LTP strengthens synapses and LTD weakens them, and that NMDA receptors act as coincidence detectors requiring both glutamate binding and postsynaptic depolarization to open. **Spike-timing-dependent plasticity (STDP)** adds a crucial dimension to this picture: it is not just *whether* two neurons are active together that matters, but *the precise order and timing* of their firing. This transforms Hebb's vague "fire together, wire together" principle into a quantitative rule with a direction.

The core STDP rule is elegant. If the **presynaptic neuron fires first** and the **postsynaptic neuron fires shortly after** (within roughly 10–20 milliseconds), the synapse is strengthened — this is LTP. The logic is causal: the presynaptic cell may have *caused* the postsynaptic cell to fire, so the connection is reinforced. If the order is reversed — postsynaptic fires first, then presynaptic — the synapse is weakened via LTD. Here, the presynaptic input arrived too late to have contributed to the postsynaptic spike, so it is pruned. The magnitude of the change depends on the **time interval (Δt)**: the closer together the spikes, the larger the effect; at intervals beyond about 40–50 milliseconds, the plasticity window closes and no change occurs.

The mechanism relies directly on the NMDA receptor properties you studied. When the presynaptic spike arrives first, it releases glutamate that binds NMDA receptors. The postsynaptic spike, arriving milliseconds later, provides the depolarization needed to expel the Mg²⁺ block from the NMDA channel. The result is a large, fast calcium influx that activates **CaMKII** and other kinases, driving AMPA receptor insertion and LTP. When the timing is reversed, the postsynaptic depolarization has already faded by the time glutamate arrives, so NMDA receptors open under weaker depolarization conditions. The resulting modest, slow calcium signal preferentially activates **phosphatases** (like calcineurin) rather than kinases, triggering AMPA receptor internalization and LTD. The same receptor, responding to the same two signals, produces opposite outcomes depending purely on temporal order — calcium amplitude and kinetics are the switch.

STDP has profound computational implications. It means that synapses automatically detect and reinforce **causal relationships** in neural activity: inputs that reliably predict a neuron's firing get strengthened, while inputs that consistently arrive too late get weakened. This is exactly the kind of learning rule needed for the brain to extract temporal structure from sensory experience — to learn that one sound predicts another, that a visual motion pattern implies a trajectory, or that a sequence of muscle activations produces a coordinated movement. However, STDP is not a universal law. Different synapse types and brain regions show variations: some inhibitory synapses have inverted STDP rules (reversed timing produces LTP), and some synapses show symmetric windows where timing order does not matter. The "classic" STDP curve — asymmetric, with LTP for pre-before-post and LTD for post-before-pre — is the most common pattern at excitatory cortical and hippocampal synapses, but the brain uses multiple plasticity rules tuned to the computational needs of each circuit.
