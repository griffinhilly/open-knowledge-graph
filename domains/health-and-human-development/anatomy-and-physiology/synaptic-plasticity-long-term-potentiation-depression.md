---
id: synaptic-plasticity-long-term-potentiation-depression
title: 'Synaptic Plasticity: Long-Term Potentiation and Depression'
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: synaptic-transmission-neurotransmitter-dynamics
  type: hard
- id: neural-anatomy-and-organization
  type: hard
builds-toward:
- memory-consolidation
tags:
- synaptic-plasticity
- LTP
- LTD
stage: formal-systems
status: validated
---

# Synaptic Plasticity: Long-Term Potentiation and Depression

## Core Idea
Synaptic strength changes through activity-dependent plasticity: long-term potentiation (LTP) strengthens synapses when postsynaptic stimulation enables NMDA-mediated Ca²⁺ influx, activating kinases that phosphorylate and insert AMPA receptors. Long-term depression (LTD) weakens synapses through opposite mechanisms. The pattern and timing of pre- and postsynaptic activity determines whether potentiation or depression occurs, encoding stimulus relationships and enabling learning.

## Questions

```yaml
- question: "A researcher blocks all AMPA receptors in a postsynaptic neuron and then delivers high-frequency presynaptic stimulation. What happens to LTP induction?"
  type: multiple-choice
  options:
    - "LTP occurs normally because NMDA receptors can detect presynaptic activity independently"
    - "LTP is blocked because AMPA-mediated depolarization is required to relieve the Mg²⁺ block on NMDA receptors"
    - "LTP is enhanced because there is no competition for AMPA receptor insertion sites"
    - "LTP is replaced by LTD because the postsynaptic membrane stays hyperpolarized"
  answer: 1
  explanation: "The NMDA receptor is a coincidence detector: it requires both glutamate binding AND postsynaptic depolarization to open. The Mg²⁺ block is only relieved when the postsynaptic membrane is already depolarized — normally achieved by AMPA receptor activation. With AMPA receptors blocked, the membrane stays near resting potential, the Mg²⁺ block persists, Ca²⁺ cannot enter through NMDA receptors, and LTP cannot be induced. Option A is the classic misconception — as if the NMDA receptor responds to presynaptic activity alone."

- question: "After LTP is established at a synapse, NMDA receptor antagonists are applied. What effect does this have on the potentiated synaptic response?"
  type: multiple-choice
  options:
    - "The potentiated response decays back to baseline because NMDA receptors are required to maintain LTP"
    - "The potentiated response is preserved because LTP expression depends on inserted AMPA receptors, not ongoing NMDA activity"
    - "The potentiated response is enhanced because NMDA blockade prevents any further LTD"
    - "The potentiated response fluctuates unpredictably without NMDA receptor input"
  answer: 1
  explanation: "LTP induction requires NMDA-mediated Ca²⁺ influx to activate kinases and insert AMPA receptors. But LTP expression — the maintained increase in synaptic strength — depends on the extra AMPA receptors now in the membrane, not on continued NMDA activity. Blocking NMDA receptors after LTP is established does not remove the AMPA receptors, so the potentiated response persists. Induction and expression are mechanistically distinct."

- question: "The NMDA receptor acts as a molecular coincidence detector because it requires both presynaptic glutamate release and postsynaptic membrane depolarization to open."
  type: true-false
  answer: true
  explanation: "This is the defining property of the NMDA receptor that enables associative learning. At resting potential, a Mg²⁺ ion physically blocks the channel even when glutamate is bound. The block is only relieved when the postsynaptic membrane is already depolarized (typically by AMPA receptor activation). Both conditions must be met simultaneously — 'coincidence detection' — and it is this requirement that makes the NMDA receptor the molecular substrate for Hebbian learning: only synapses whose presynaptic activity correlates with postsynaptic firing get strengthened."

- question: "Long-term depression (LTD) uses a completely different receptor and ion channel than LTP, which is why weak stimulation produces the opposite outcome."
  type: true-false
  answer: false
  explanation: "LTD and LTP both depend on the NMDA receptor and Ca²⁺ influx — the same receptor and the same ion. What differs is the amplitude and kinetics of the Ca²⁺ signal. High-frequency or coincident stimulation produces a large, rapid Ca²⁺ rise that activates kinases (particularly CaMKII), leading to AMPA receptor phosphorylation and insertion (LTP). Weak or asynchronous stimulation produces a smaller, slower Ca²⁺ signal that preferentially activates phosphatases, leading to AMPA receptor dephosphorylation and internalization (LTD). Same receptor, same ion, opposite outcomes — determined by the pattern of activity."

- question: "Why does the direction of synaptic change — potentiation versus depression — depend on the pattern of Ca²⁺ influx rather than simply on whether Ca²⁺ enters the postsynaptic cell?"
  type: short-answer
  answer: "The amplitude and kinetics of Ca²⁺ influx determine which downstream enzymes are activated. A large, rapid Ca²⁺ rise (from high-frequency or coincident stimulation) preferentially activates kinases like CaMKII, which phosphorylate and insert AMPA receptors, potentiating the synapse. A small, slow Ca²⁺ rise (from weak or asynchronous stimulation) preferentially activates phosphatases, which dephosphorylate and internalize AMPA receptors, depressing the synapse. The threshold and kinetics differ for the two enzyme classes, making the Ca²⁺ signal a graded switch."
  explanation: "This is the key insight: Ca²⁺ is not just an on/off signal but a graded, temporally-patterned signal. Kinases have a higher activation threshold than phosphatases, so only the large Ca²⁺ signal triggers potentiation. The same molecular machinery reads the quantitative properties of Ca²⁺ entry and routes the outcome in opposite directions — a single ion species acting as a bidirectional plasticity switch depending on how it enters."
```

## Explainer

From your study of synaptic transmission, you know that a synapse communicates by releasing neurotransmitter into a cleft, where it binds receptors on the postsynaptic membrane and alters ion conductance. **Synaptic plasticity** is the capacity of that communication to be strengthened or weakened based on recent activity — a mechanism that lets neural circuits change in response to experience. The key principle is that synaptic strength is not fixed hardware; it is continuously adjustable software written by patterns of neural activity.

**Long-term potentiation (LTP)** is triggered by high-frequency or coincident pre- and postsynaptic activity, and its mechanism hinges on a molecular coincidence detector: the **NMDA receptor**. Like AMPA receptors, NMDA receptors are glutamate-gated ion channels, but with a critical difference: at resting membrane potentials, a magnesium ion physically blocks the channel even when glutamate is bound. The Mg²⁺ block is only relieved when the postsynaptic membrane is already depolarized — which happens when AMPA receptors nearby are already activated. This means the NMDA receptor opens only when glutamate arrives *and* the postsynaptic cell is already active — it detects the coincidence of pre- and postsynaptic firing. When both conditions are met, Ca²⁺ flows through the NMDA channel, activating protein kinases (particularly CaMKII) that phosphorylate existing AMPA receptors and trigger insertion of additional AMPA receptors into the postsynaptic membrane. More AMPA receptors means a larger response to the same presynaptic signal — the synapse is potentiated. This potentiation can last hours, days, or permanently.

**Long-term depression (LTD)** is the mirror process. Weak or asynchronous stimulation produces modest Ca²⁺ influx through NMDA receptors — lower amplitude, slower time course than LTP-triggering stimulation. This low-level Ca²⁺ signal preferentially activates phosphatases rather than kinases, which dephosphorylate AMPA receptors and trigger their internalization (removal from the membrane). The synapse becomes weaker. The same receptor, the same ion, the same channel — but amplitude and timing determine whether the outcome is potentiation or depression.

This timing-dependence has a precise formulation called **spike-timing-dependent plasticity (STDP)**: if the presynaptic neuron fires just before the postsynaptic neuron (pre then post), LTP results; if the order reverses (post then pre), LTD results. The logic is causal: a synapse strengthens when its activity appears to have caused the postsynaptic response, and weakens when it fired too late to have been the cause. This elegantly instantiates the Hebbian maxim that "neurons that fire together wire together" — and its corollary, neurons that fire out of phase weaken their connection. The asymmetric timing window, typically tens of milliseconds, is the biological implementation of associative learning at the cellular scale.

The link to memory consolidation — your builds-toward topic — lies in the hippocampus, where LTP is the most studied and best-documented example. The formation of new explicit memories depends on hippocampal synaptic strengthening driven by these same NMDA/AMPA mechanisms. Blocking NMDA receptors in the hippocampus impairs new memory formation without affecting retrieval of old memories, demonstrating that LTP is not just a laboratory curiosity but the actual cellular substrate of learning.
