---
id: neural-integration-synaptic-plasticity
title: Neural Integration and Synaptic Plasticity
domain: biology
course: physiology
prerequisites:
- id: synaptic-transmission
  type: hard
- id: long-term-potentiation
  type: hard
builds-toward:
- motor-control-spinal-coordination
- sensory-neural-coding-perception
- hypothalamic-neuroendocrine-integration
tags:
- synaptic
- plasticity
- learning
- memory
- integration
stage: formal-systems
status: draft
---

# Neural Integration and Synaptic Plasticity

## Core Idea
Neurons integrate signals from many synapses through spatial and temporal summation to decide whether to fire. Synaptic plasticity—the ability of synapses to strengthen or weaken—underlies learning and memory. Both pre- and post-synaptic mechanisms contribute to changes in synaptic efficacy over time and are essential for nervous system adaptation.

## How It's Best Learned
Compare AMPA and NMDA receptor roles in LTP. Use a simple circuit model to trace how multiple inputs summate. Examine how calcium influx triggers molecular cascades that strengthen synapses.

## Common Misconceptions
Assuming all synapses strengthen equally with use—different neurons exhibit different plasticity rules. Thinking LTP is purely postsynaptic when presynaptic factors (transmitter release) also change.

## Questions

```yaml
- question: "A postsynaptic neuron receives simultaneous weak stimulation from 200 excitatory synapses, each producing a sub-threshold EPSP. The combined depolarization reaches threshold and the neuron fires. This is an example of:"
  type: multiple-choice
  options:
    - "Temporal summation — multiple EPSPs from rapid successive firing of a single synapse"
    - "Spatial summation — simultaneous EPSPs from multiple synapses add together at the axon hillock"
    - "LTP — co-activation of many synapses permanently strengthens their connections"
    - "Lateral inhibition — inactive neighboring synapses suppress the effects of active ones"
  answer: 1
  explanation: "Spatial summation occurs when EPSPs from different anatomical locations (different synapses) arrive simultaneously and their depolarizations add together at the axon hillock. Each individual contribution is sub-threshold, but the combined effect crosses threshold. Temporal summation is distinct: a single synapse fires rapidly enough that EPSPs arrive before the previous one decays — summation in time rather than space. LTP (option C) is a persistent change in synaptic strength resulting from sustained co-activation; the question describes a single firing event, not a long-term structural change."

- question: "Why does LTP specifically require coincident presynaptic and postsynaptic activity, rather than being triggered by either one alone?"
  type: multiple-choice
  options:
    - "Because AMPA receptors only open when both glutamate binds and the membrane is simultaneously depolarized"
    - "Because the NMDA receptor requires both glutamate binding AND relief of Mg²⁺ block by postsynaptic depolarization before calcium can enter and trigger LTP"
    - "Because presynaptic activity releases BDNF that must combine with postsynaptic calcium to initiate LTP"
    - "Because temporal summation is required to accumulate enough calcium for LTP induction"
  answer: 1
  explanation: "The NMDA receptor functions as a coincidence detector — a molecular AND gate. It requires TWO simultaneous conditions: (1) glutamate binding from the presynaptic terminal, AND (2) sufficient postsynaptic depolarization to displace the Mg²⁺ ion blocking the channel. Only when both conditions are met does calcium enter and trigger the CaMKII-mediated cascade that inserts more AMPA receptors and strengthens the synapse. Either condition alone is insufficient: glutamate without depolarization leaves the Mg²⁺ block intact; depolarization without glutamate leaves the channel closed. This coincidence requirement implements Hebb's rule ('neurons that fire together wire together') at the molecular level."

- question: "Long-term potentiation (LTP) is a purely postsynaptic phenomenon — changes in synaptic strength during LTP involve only the postsynaptic cell's receptor number and conductance."
  type: true-false
  answer: false
  explanation: "LTP involves both postsynaptic and presynaptic changes. Postsynaptically, CaMKII activation inserts additional AMPA receptors into the synapse and enhances their conductance. But presynaptic changes also occur: retrograde signaling molecules (including endocannabinoids and nitric oxide) travel from the postsynaptic cell back to the presynaptic terminal, increasing neurotransmitter release probability. Changes in vesicle pool size and release mechanisms have been documented. Both sides of the synapse contribute to enhanced transmission in LTP, which is why studies manipulating only postsynaptic factors underestimate the full magnitude of potentiation."

- question: "According to Hebb's rule, a synapse is strengthened whenever the presynaptic neuron fires, regardless of what the postsynaptic neuron is doing at that moment."
  type: true-false
  answer: false
  explanation: "Hebb's rule specifically requires coincident activity: 'neurons that fire together wire together.' A synapse is strengthened only when the presynaptic neuron fires AND the postsynaptic neuron is simultaneously sufficiently depolarized. If the presynaptic neuron fires when the postsynaptic cell is inactive, the NMDA receptor remains Mg²⁺-blocked and no calcium influx occurs — LTP does not result. In fact, weak presynaptic stimulation without sufficient postsynaptic depolarization can produce long-term depression (LTD) instead. The coincidence requirement ensures that only correlated activity produces synaptic strengthening, allowing neural circuits to encode associations rather than indiscriminately potentiating all active synapses."

- question: "Explain why the NMDA receptor has been called a 'coincidence detector' and why this property is essential for associative learning."
  type: short-answer
  answer: "The NMDA receptor acts as a coincidence detector because it requires two simultaneous conditions to open and pass calcium: (1) glutamate binding from the presynaptic neuron, indicating presynaptic activity, and (2) sufficient postsynaptic depolarization to displace the Mg²⁺ blocking the channel, indicating the postsynaptic cell is also active. Only when both neurons are simultaneously active does calcium enter and trigger LTP. This is essential for associative learning because it allows synapses to detect and record co-occurrence: if two inputs reliably fire together, both conditions are met repeatedly, the connection strengthens, and the brain encodes the association. Random, uncorrelated activity leaves the Mg²⁺ block in place and produces no lasting change."
  explanation: "The coincidence detection property implements Hebb's rule at the molecular level and is thought to underlie how the brain forms associations between stimuli, learns cause-and-effect relationships, and stores memories. Without it, all activity would strengthen all synapses indiscriminately — there would be no mechanism to selectively encode which inputs are meaningfully correlated versus which co-activated by chance."
```

## Explainer

From your study of synaptic transmission and long-term potentiation, you understand that neurons communicate through chemical synapses and that repeated activation can strengthen these connections. Neural integration and synaptic plasticity are the principles that explain how the nervous system turns this basic signaling machinery into computation, learning, and memory.

**Neural integration** is how a single neuron decides whether to fire. A typical neuron in the central nervous system receives thousands of synaptic inputs — some excitatory (producing EPSPs that depolarize the membrane) and some inhibitory (producing IPSPs that hyperpolarize it). The neuron's membrane acts as a leaky integrator: it sums these inputs in two ways. **Spatial summation** occurs when EPSPs from different synapses arrive simultaneously and their depolarizations add together at the axon hillock. **Temporal summation** occurs when a single synapse fires rapidly enough that each EPSP arrives before the previous one has fully decayed. If the combined depolarization at the axon hillock reaches threshold, the neuron fires an action potential. If not, the signal dies. This all-or-none decision is the fundamental computation of the nervous system, and the balance of excitation and inhibition determines what information gets transmitted and what gets filtered out.

**Synaptic plasticity** adds a time dimension to this integration. Rather than having fixed synaptic weights, neurons adjust connection strength based on experience. **Long-term potentiation (LTP)** at glutamatergic synapses is the best-studied example. At resting conditions, AMPA receptors carry the bulk of excitatory current while NMDA receptors remain blocked by magnesium ions. When a synapse is strongly activated — enough to substantially depolarize the postsynaptic membrane — the magnesium block is relieved, NMDA receptors open, and calcium floods into the dendritic spine. This calcium influx activates CaMKII and other kinases that insert additional AMPA receptors into the postsynaptic membrane and enhance their conductance, making the synapse more responsive to future stimulation. The beauty of this mechanism is that it requires *coincidence*: the presynaptic neuron must release glutamate at the same time the postsynaptic neuron is sufficiently depolarized. This coincidence detection is the molecular basis of **Hebb's rule** — "neurons that fire together wire together."

Plasticity is not a one-way street. **Long-term depression (LTD)** weakens synapses that are activated without sufficient postsynaptic depolarization, typically through low-frequency stimulation that produces modest calcium influx activating phosphatases instead of kinases. The balance between LTP and LTD allows neural circuits to continuously recalibrate: frequently co-activated pathways strengthen while unused connections weaken, sharpening the network's representation of relevant information. Presynaptic plasticity further modulates these circuits — changes in neurotransmitter release probability, vesicle pool size, and retrograde signaling (such as endocannabinoids) all adjust synaptic gain. Together, integration and plasticity explain how the same neural hardware can learn a new language, adapt to injury, form associations between a sound and a reward, and forget information that is no longer relevant.
