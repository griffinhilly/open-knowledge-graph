---
id: long-term-depression-ltd-synaptic-weakening
title: 'Long-Term Depression (LTD): Synaptic Weakening'
domain: psychology
course: biological-psychology
prerequisites:
- id: synaptic-transmission-neurotransmitter-release
  type: hard
- id: long-term-potentiation-ltp-memory-encoding
  type: soft
- id: long-term-depression
  type: hard
- id: ion-channels-and-neural-excitability
  type: hard
- id: calcium-signaling-neurons
  type: hard
builds-toward:
- memory-consolidation-systems
- learning-and-experience-dependent-plasticity
tags:
- plasticity
- learning
- synaptic-weakening
stage: formal-systems
status: validated
---

# Long-Term Depression (LTD): Synaptic Weakening

## Core Idea
Long-term depression is an activity-dependent decrease in synaptic strength that complements LTP. Low-frequency stimulation or postsynaptic activation alone (without strong presynaptic input) triggers modest calcium elevation through NMDA receptors, activating phosphatases that remove AMPA receptors. LTD is essential for circuit refinement, prevention of runaway excitation, and forgetting of irrelevant information.

## Questions

```yaml
- question: "A researcher applies low-frequency stimulation to a synapse and observes long-lasting synaptic weakening. Which chain of events best explains this LTD?"
  type: multiple-choice
  options:
    - "Low stimulation reduces NMDA receptor number at the membrane, preventing calcium entry and weakening the synapse"
    - "Low-frequency stimulation produces a modest calcium rise through NMDA receptors, activating phosphatases that remove AMPA receptors from the synapse"
    - "Low stimulation activates a separate class of metabotropic receptors unrelated to LTP, triggering an independent weakening cascade"
    - "Reduced presynaptic activity permanently decreases neurotransmitter release, preventing sufficient postsynaptic activation"
  answer: 1
  explanation: "LTD at most excitatory synapses involves NMDA receptor-mediated calcium entry — the same receptors involved in LTP. The key is calcium quantity: low-frequency stimulation produces only a modest calcium rise, which preferentially activates phosphatases (calcineurin, PP1) rather than kinases. Phosphatases dephosphorylate AMPA receptors, triggering their internalization from the synapse membrane. With fewer AMPA receptors present, subsequent stimulation elicits a weaker postsynaptic response. The mechanism is postsynaptic, not presynaptic."

- question: "Why would a nervous system capable only of LTP (synaptic strengthening) but never LTD eventually become dysfunctional?"
  type: multiple-choice
  options:
    - "Because LTP requires LTD to reset NMDA receptors between uses, so LTP itself would eventually fail"
    - "Because without LTD, all synapses would eventually saturate at maximum strength, eliminating the network's capacity to encode new distinctions between experiences"
    - "Because LTP is metabolically expensive and LTD provides the energy recovery needed to sustain further strengthening"
    - "Because LTD prevents excessive action potential firing that would otherwise cause seizures in all circuits"
  answer: 1
  explanation: "If synapses could only be strengthened, every synapse would eventually approach its maximum possible strength (maximum AMPA receptor density). At saturation, the network loses its dynamic range — it can no longer distinguish strong signals from weak ones, or encode new memories differentially. LTD provides the complementary 'write-down' operation that allows the system to weaken synaptic traces that are irrelevant or incorrect. This bidirectionality is what makes the system capable of storing a large number of distinguishable memories rather than a single maximally-activated state."

- question: "The difference between LTP and LTD at the same synapse is primarily determined by the amount of calcium entering the postsynaptic cell, not by activation of different receptor types."
  type: true-false
  answer: true
  explanation: "Both LTP and LTD are initiated through NMDA receptor activation and calcium influx. The calcium threshold model explains the bidirectionality: high-frequency stimulation drives large calcium spikes, which preferentially activate kinases (like CaMKII) that insert AMPA receptors (LTP). Low-frequency stimulation produces modest calcium rises that preferentially activate phosphatases that remove AMPA receptors (LTD). Same receptor, same ion, opposite outcomes — the difference is the calcium concentration and which downstream effectors that concentration recruits."

- question: "LTD always involves a decrease in presynaptic neurotransmitter release, which then reduces postsynaptic receptor activation."
  type: true-false
  answer: false
  explanation: "Canonical NMDA-dependent LTD is a postsynaptic phenomenon: the presynaptic terminal continues releasing the same amount of neurotransmitter, but the postsynaptic response weakens because AMPA receptors are internalized from the synapse membrane. Fewer AMPA receptors means less depolarization for the same glutamate release. There are forms of presynaptic plasticity that alter neurotransmitter release, but the defining mechanism of NMDA-dependent LTD is postsynaptic AMPA receptor removal driven by modest calcium influx."

- question: "Explain the calcium threshold model of synaptic plasticity and how it accounts for both LTP and LTD at the same synapse."
  type: short-answer
  answer: "The calcium threshold model proposes that the direction of synaptic change depends on the magnitude of calcium entry through NMDA receptors. High-frequency stimulation drives large calcium spikes that activate kinases (like CaMKII), which phosphorylate AMPA receptors and recruit additional ones to the synapse — producing LTP. Low-frequency stimulation produces only a modest calcium rise that preferentially activates phosphatases (calcineurin, PP1), which dephosphorylate AMPA receptors and trigger their internalization — producing LTD. Both outcomes use the same NMDA receptors and the same calcium ion; the calcium concentration determines which effector proteins are recruited and therefore whether the synapse strengthens or weakens."
  explanation: "The elegance of the calcium threshold model is that it explains bidirectional plasticity without requiring two entirely separate molecular pathways. The system is essentially a calcium sensor with two competing downstream signals: kinases win at high calcium, phosphatases win at low calcium. This makes the synapse sensitive to the pattern of activity — how often and how synchronously it is stimulated — rather than just whether it is stimulated at all. It is also the reason that timing matters so much for synaptic plasticity: the calcium concentration depends on how synchronized pre- and postsynaptic activity are."
```

## Explainer

You already understand LTP — the synaptic strengthening that encodes memories through NMDA receptor activation, calcium influx, and AMPA receptor insertion. LTD is the mirror process: it *weakens* synapses. The key to understanding both is not which molecules are recruited, but *how much* calcium enters the postsynaptic cell. The same NMDA receptors are involved, but the outcome depends on the calcium concentration they produce.

The **calcium threshold model** captures this elegantly. High-frequency presynaptic stimulation drives large calcium spikes, which activate kinases (like CaMKII) that insert more AMPA receptors into the synapse — that's LTP. But low-frequency stimulation, or postsynaptic activation that occurs without synchronized strong presynaptic input, produces only a modest calcium rise. This lower calcium level preferentially activates **phosphatases** (like protein phosphatase 1 and calcineurin) rather than kinases. Phosphatases do the opposite of kinases: they remove phosphate groups from AMPA receptors, triggering their **internalization** — the receptors are removed from the synapse membrane and stored inside the cell. With fewer AMPA receptors at the synapse, the postsynaptic response to subsequent stimulation is weaker. The synapse has been depressed.

The biological logic of LTD becomes clear when you consider what would happen without it. If LTP only ever strengthened synapses, the system would saturate — every synapse would max out, and the network would lose its capacity to encode new distinctions. LTD provides the complementary "write-down" operation. It is especially prominent in the cerebellum, where it underlies motor learning: when a climbing fiber (error signal) co-activates a cerebellar Purkinje cell alongside a weak parallel fiber input, that parallel fiber synapse is depressed. This is how the cerebellum adjusts motor programs — repeatedly activating unhelpful pathways weakens them while correct pathways are strengthened.

At the systems level, LTD contributes to **synaptic homeostasis** and **circuit refinement** during development. During sleep, for instance, widespread synaptic downscaling (a form of global LTD) is thought to prevent network saturation and consolidate the most important memories by weakening weaker synaptic traces. The result is a nervous system that is not simply an accumulation of reinforced pathways, but a dynamically sculpted network that can forget irrelevant detail while preserving meaningful signal.
