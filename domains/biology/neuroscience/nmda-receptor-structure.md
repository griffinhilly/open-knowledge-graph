---
id: nmda-receptor-structure
title: 'NMDA Receptors: Structure and Properties'
domain: biology
course: neuroscience
prerequisites:
- id: nmda-receptor-calcium
  type: hard
- id: ligand-gated-ion-channels
  type: hard
- id: resting-membrane-potential
  type: soft
builds-toward:
- long-term-potentiation
- spike-timing-dependent-plasticity
tags:
- nmdar
- nmda
- calcium
- voltage-dependent
stage: advanced
status: validated
---

# NMDA Receptors: Structure and Properties

## Core Idea
NMDA receptors require both glutamate binding AND postsynaptic depolarization (to relieve Mg2+ block) to open. This voltage-dependent gating makes NMDARs coincidence detectors critical for Hebbian learning. NMDARs pass large amounts of calcium, triggering plasticity. Excessive activation causes excitotoxicity.

## How It's Best Learned
Measure NMDAR current across different holding potentials. Model Mg2+ block using Boltzmann kinetics.

## Common Misconceptions
NMDA receptors are fast like AMPA receptors—NMDARs have slower kinetics. All glutamate receptors are identical—NMDARs pass more Ca2+ than AMPARs.

## Questions

```yaml
- question: "A presynaptic neuron fires weakly, releasing a small amount of glutamate onto a postsynaptic cell that is near its resting membrane potential (around −65 mV). What happens to NMDA receptor current at that synapse?"
  type: multiple-choice
  options:
    - "NMDA receptors open fully because glutamate is the only requirement for gating"
    - "NMDA receptors open partially, passing a small calcium current proportional to the amount of glutamate"
    - "NMDA receptors remain blocked by Mg²⁺ and pass little or no current, even though glutamate is bound"
    - "NMDA receptors open but pass only sodium, not calcium, at resting potential"
  answer: 2
  explanation: "At resting potential (−65 mV), a Mg²⁺ ion sits in the NMDA receptor channel pore and blocks ion flow even when glutamate is bound. Glutamate binding alone is necessary but not sufficient — the postsynaptic membrane must also be depolarized to expel the Mg²⁺ block by electrostatic repulsion. Weak presynaptic activity produces little AMPA-mediated depolarization, so the Mg²⁺ block persists and NMDAR current is minimal. This is the mechanistic basis of the coincidence detection property."

- question: "Why does NMDA receptor opening require postsynaptic depolarization in addition to glutamate binding?"
  type: multiple-choice
  options:
    - "Glutamate binds to both GluN1 and GluN2 subunits, and GluN2 only changes conformation when the membrane is depolarized"
    - "A Mg²⁺ ion physically blocks the open pore at resting membrane potential; depolarization electrostatically expels it, allowing ion flow"
    - "Depolarization causes conformational changes in the channel that increase its affinity for glutamate"
    - "NMDA receptors require voltage-gated calcium channels to open first, which then depolarize the membrane to activate the NMDAR"
  answer: 1
  explanation: "The Mg²⁺ block is the mechanism. At resting potential, a divalent Mg²⁺ ion sits in the channel pore, blocking it despite glutamate being bound. When the membrane depolarizes — typically because nearby AMPA receptors have been activated — the reduced electronegativity inside the cell no longer holds the Mg²⁺ in the pore, and it is expelled. Now, with both glutamate bound AND the pore unblocked, current (including Ca²⁺) flows through the NMDAR. This voltage-dependent gating by a blocking ion is unusual among ligand-gated channels and is what makes NMDARs coincidence detectors."

- question: "NMDA receptor opening requires simultaneous glutamate binding and postsynaptic membrane depolarization, making the receptor sensitive to the correlation between pre- and postsynaptic activity."
  type: true-false
  answer: true
  explanation: "This is the core property of NMDARs. The glutamate requirement reflects presynaptic activity; the depolarization requirement reflects postsynaptic activity (typically driven by prior AMPA receptor activation). Both conditions must be met simultaneously for the channel to open. This coincidence detection is the molecular implementation of Hebb's rule — the NMDAR opens only when pre- and postsynaptic neurons are both active at the same time, triggering the calcium influx that drives synaptic plasticity."

- question: "NMDA receptors open faster than AMPA receptors and produce larger, more rapid excitatory currents in response to glutamate."
  type: true-false
  answer: false
  explanation: "This is the opposite of reality. NMDARs have notably slow kinetics compared to AMPA receptors — they open slowly and remain open longer. AMPA receptors generate the fast component of the excitatory postsynaptic potential. NMDARs contribute little to fast signaling but provide the slow, sustained calcium entry that triggers plasticity. The slow timecourse of NMDAR activation is part of why they serve an integrative function rather than a fast signal-relay function."

- question: "Explain why the Mg²⁺ block makes NMDA receptors act as coincidence detectors, and why this property matters for learning."
  type: short-answer
  answer: "The Mg²⁺ ion blocks the NMDAR pore at resting membrane potential. Glutamate binding alone (presynaptic signal) is insufficient to open it. The membrane must also be depolarized (postsynaptic signal), which happens when nearby AMPA receptors have been activated by strong or repeated stimulation. Thus the NMDAR only opens when presynaptic activity (glutamate release) and postsynaptic activity (depolarization) occur simultaneously. This coincidence condition means NMDARs detect correlated activity between two neurons — the exact condition Hebb's rule specifies for strengthening synaptic connections. When NMDARs do open, the resulting Ca²⁺ influx triggers the signaling cascades that long-term potentiation."
  explanation: "The Mg²⁺ block is the physical implementation of logical AND: both conditions (glutamate AND depolarization) must be true simultaneously for the channel to open. This is why NMDARs are called coincidence detectors and why disrupting NMDAR function impairs learning and memory — without coincidence detection, the synapse cannot distinguish correlated from uncorrelated activity and cannot selectively strengthen the right connections."
```

## Explainer

You already know that ligand-gated ion channels open when a neurotransmitter binds them, allowing ions to flow across the membrane. NMDA receptors follow this basic principle — they are glutamate-gated ion channels — but they add a critical twist that makes them unlike any other channel in the nervous system. To understand why NMDARs are considered the molecular foundation of learning, you need to grasp what makes their gating mechanism special.

Most ligand-gated channels have a simple rule: bind the transmitter, open the pore. **NMDA receptors require two conditions to be met simultaneously**. First, glutamate (plus the co-agonist glycine or D-serine) must be bound to the receptor. Second, the postsynaptic membrane must be sufficiently depolarized. The reason for this dual requirement is a **magnesium block**: at resting membrane potential (around −65 mV), a Mg²⁺ ion sits in the channel pore, physically blocking ion flow even when glutamate is bound. Only when the membrane depolarizes — typically because nearby AMPA receptors have already been activated by the same glutamate release — does the Mg²⁺ ion get expelled by electrostatic repulsion, allowing current to flow through the NMDA channel. This means the NMDAR opens only when presynaptic activity (glutamate release) and postsynaptic activity (depolarization) occur at the same time.

This **coincidence detection** property is what makes NMDARs the biological implementation of Hebb's rule — "neurons that fire together, wire together." When a presynaptic neuron releases glutamate while the postsynaptic neuron is already depolarized, NMDARs open and allow a flood of **calcium ions** (Ca²⁺) into the postsynaptic cell. NMDA receptors are highly permeable to calcium compared to AMPA receptors, and this calcium influx is the critical trigger for synaptic plasticity. The calcium activates intracellular signaling cascades — including CaMKII, calcineurin, and various protein kinases — that lead to lasting changes in synaptic strength, the molecular basis of long-term potentiation and long-term depression.

Structurally, NMDA receptors are **heterotetramers**, typically composed of two obligatory GluN1 subunits and two GluN2 subunits (GluN2A, 2B, 2C, or 2D). The GluN1 subunits bind the co-agonist glycine, while GluN2 subunits bind glutamate. The subunit composition determines the receptor's kinetics, Mg²⁺ sensitivity, and calcium permeability — GluN2B-containing receptors, for instance, have slower kinetics and are particularly important during development. The channel has notably slow kinetics compared to AMPA receptors: it opens slowly, stays open longer, and thus provides a prolonged window for calcium entry. This slow timecourse also means that NMDARs contribute relatively little to the fast excitatory postsynaptic potential but are essential for the integrative and plasticity functions of the synapse. The flip side of calcium entry is **excitotoxicity**: excessive NMDAR activation during stroke or seizures floods neurons with calcium, triggering cell death pathways — a reminder that the same mechanism underlying learning can become destructive when uncontrolled.
