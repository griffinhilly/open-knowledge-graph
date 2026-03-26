---
id: postsynaptic-currents-epsc-ipsc
title: 'Postsynaptic Currents: EPSCs and IPSCs'
domain: biology
course: neuroscience
prerequisites:
- id: ionotropic-vs-metabotropic-receptors
  type: hard
- id: action-potential-depolarization-repolarization
  type: soft
builds-toward:
- long-term-potentiation
tags:
- currents
- synaptic-transmission
stage: formal-systems
status: validated
---

# Postsynaptic Currents: EPSCs and IPSCs

## Core Idea
EPSCs: Na+/Ca2+ inward current through glutamate receptors, depolarizes. IPSCs: Cl− inward through GABA_A, hyperpolarizes. Sum determines firing.

## Questions

```yaml
- question: "An inhibitory interneuron synapses directly onto the soma of a pyramidal neuron, while another inhibitory synapse is located on a distal dendrite. All else being equal, which inhibitory synapse is more effective at suppressing neuronal firing, and why?"
  type: multiple-choice
  options:
    - "The distal dendritic synapse, because it intercepts excitatory inputs arriving from the dendritic tree before they summate"
    - "The somatic synapse, because it can shunt excitatory currents arriving from the entire dendritic tree before they reach the axon initial segment"
    - "Both synapses are equally effective, since inhibitory current magnitude depends only on chloride conductance"
    - "The somatic synapse, because the soma contains a higher density of GABA_A receptors than dendrites"
  answer: 1
  explanation: "Location matters enormously for inhibitory efficacy. An IPSC on the soma or axon initial segment is positioned to veto excitatory inputs arriving from the entire dendritic arbor — all those EPSCs must pass through the soma to reach the axon hillock, and the somatic IPSC provides a low-resistance shunt at exactly that bottleneck. A distal dendritic IPSC only affects inputs arriving from that dendritic branch. Shunting inhibition — where the increased conductance diverts excitatory current to the chloride reversal potential — is often more important than hyperpolarization per se, especially when the chloride equilibrium potential is near resting potential."

- question: "A single EPSC at one synapse typically produces only a 0.5–1 mV depolarization at the soma. What does this imply about how a neuron decides to fire an action potential?"
  type: multiple-choice
  options:
    - "Neurons rarely fire because individual EPSCs are too small to matter; firing only occurs during intense sensory stimulation"
    - "The neuron must summate many EPSCs — either from multiple near-simultaneous synapses (spatial summation) or repeated firing from the same synapse (temporal summation) — to reach threshold"
    - "A single EPSC is sufficient if it arrives at the axon hillock directly rather than through dendrites"
    - "Neurons compensate by increasing channel density at the synapse to amplify individual EPSCs"
  answer: 1
  explanation: "A single EPSC produces a tiny EPSP (~0.5–1 mV) because each synaptic event opens only a small number of channels. Reaching the ~15 mV depolarization needed for an action potential requires summation. Spatial summation occurs when multiple synapses fire at nearly the same time — their EPSPs add at the soma. Temporal summation occurs when the same synapse fires repeatedly before the membrane potential has recovered — each successive EPSP adds to the last. This summation requirement means the neuron effectively computes a weighted average over its inputs, which is why individual neurons can function as computational units that integrate information from hundreds of sources."

- question: "Inhibitory postsynaptic currents can suppress neuronal firing even without measurably hyperpolarizing the membrane potential, through shunting inhibition."
  type: true-false
  answer: true
  explanation: "Shunting inhibition occurs when GABA_A receptor opening increases chloride conductance, pulling the membrane potential toward the chloride reversal potential (~−75 mV). If the cell is already near rest (−70 mV), this may produce only a few mV of hyperpolarization — imperceptible in many recordings. But the key effect is the increase in membrane conductance: by providing a low-resistance pathway to −75 mV, the shunt 'diverts' excitatory currents that would otherwise depolarize the membrane. Nearby EPSCs lose much of their effectiveness because the increased conductance dissipates their current before it can raise membrane voltage. This is particularly powerful when inhibitory synapses are near the axon initial segment."

- question: "In mature adult neurons, GABA_A receptor activation generally produces inhibition by driving the membrane potential toward a hyperpolarized chloride reversal potential."
  type: true-false
  answer: false
  explanation: "This is only true for mature neurons. In immature developing neurons (and in some adult neurons), the chloride transporter NKCC1 predominates over KCC2, maintaining high intracellular chloride concentrations. As a result, the chloride reversal potential is more depolarized than the resting potential, and GABA_A activation causes chloride to flow OUT of the cell — producing depolarization rather than hyperpolarization. GABA is therefore excitatory early in development. This developmental switch (from KCC2 maturation progressively shifting the chloride equilibrium) is why neonatal seizures can be paradoxically worsened by benzodiazepines that potentiate GABA_A, an important clinical consideration."

- question: "Why does the TIMING of an IPSC relative to incoming EPSCs matter for whether excitation succeeds in triggering an action potential? Explain with reference to the neuron's integration process."
  type: short-answer
  answer: "The neuron integrates currents at each moment in time. An IPSC that arrives during or just before a volley of EPSCs can shunt or cancel those excitatory currents — the chloride conductance is elevated exactly when the excitatory current is trying to raise membrane voltage, so the two largely cancel. But an IPSC that arrives too early (before the EPSCs) or too late (after the neuron has already depolarized toward threshold) has minimal effect on whether the action potential occurs. Neural circuits exploit this temporal precision: inhibitory interneurons with millisecond-accurate timing can gate specific windows of excitability, allowing the brain to select which excitatory inputs produce output and which are suppressed."
  explanation: "This timing sensitivity makes neural computation highly dynamic. The same set of excitatory inputs can produce very different outputs depending on whether and when inhibitory signals arrive. Feedforward inhibition — where an input activates both excitatory and inhibitory cells, with the inhibitory cells delaying excitation of the target — implements a coincidence detection window: only inputs arriving within the narrow window before inhibition closes off excitability will drive firing. This is a key mechanism for temporal coding and pattern selectivity in neural circuits."
```

## Explainer

You already understand the distinction between ionotropic and metabotropic receptors and know how action potentials involve depolarization and repolarization. **Postsynaptic currents** are the electrical events that ionotropic receptors produce when neurotransmitter binds — they are the fundamental units of fast synaptic communication, and understanding them is essential for grasping how neurons integrate information from thousands of inputs to decide whether to fire.

An **excitatory postsynaptic current** (EPSC) occurs when glutamate binds to ionotropic glutamate receptors (AMPA and NMDA types), opening channels that are permeable to Na⁺ and, in the case of NMDA receptors, Ca²⁺. Because the electrochemical driving force pushes these cations inward at resting membrane potential, the net effect is an inward current — positive charges flowing into the cell. This inward current produces a small, transient depolarization called an excitatory postsynaptic potential (EPSP). A single EPSC from one synapse is far too small to bring the neuron to threshold on its own — typically only 0.5–1 mV at the soma. The neuron must summate many EPSCs, either from multiple synapses firing near-simultaneously (**spatial summation**) or from the same synapse firing repeatedly (**temporal summation**), to reach the ~15 mV depolarization needed to trigger an action potential.

An **inhibitory postsynaptic current** (IPSC) works in the opposite direction. When GABA binds to GABA_A receptors, channels open that are selectively permeable to Cl⁻ ions. In most adult neurons, the chloride equilibrium potential is near or slightly negative to the resting potential, so Cl⁻ flows inward, producing an outward current (in electrical convention, negative charge moving in is equivalent to positive charge moving out). This drives the membrane potential toward the chloride reversal potential, which is typically around −75 mV — further from threshold. Even when the IPSC does not noticeably hyperpolarize the cell, it increases the membrane's conductance, effectively **shunting** nearby excitatory currents by providing a low-resistance path to the chloride equilibrium potential. This shunting inhibition is particularly powerful when inhibitory synapses are located on the soma or axon initial segment, where they can veto excitatory inputs arriving from the entire dendritic tree.

The neuron's firing decision emerges from the continuous, moment-by-moment balance between EPSCs and IPSCs. At any given instant, a cortical neuron might be receiving hundreds of excitatory and inhibitory inputs. The net postsynaptic current — the algebraic sum of all EPSCs and IPSCs — determines whether the membrane potential at the axon hillock crosses threshold. This is not a simple addition: the timing, location, and conductance of each input all matter. An IPSC arriving a few milliseconds before a volley of EPSCs can cancel the excitation entirely, while the same IPSC arriving too late has no effect. This dynamic integration of opposing currents is how neural circuits implement computation — selecting which signals pass through and which are suppressed, shaping the temporal precision of neural coding with millisecond accuracy.
