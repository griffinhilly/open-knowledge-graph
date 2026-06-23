---
id: ampa-receptors-trafficking
title: 'AMPA Receptors: Structure, Trafficking, and Function'
domain: biology
course: neuroscience
prerequisites:
- id: ligand-gated-ion-channels
  type: hard
- id: long-term-potentiation
  type: hard
builds-toward:
- spike-timing-dependent-plasticity
tags:
- ampa
- ampar
- trafficking
- plasticity
stage: expert
status: validated
---

# AMPA Receptors: Structure, Trafficking, and Function

## Core Idea
AMPA receptors are tetrameric ionotropic glutamate receptors mediating fast excitatory transmission. Trafficking to and from postsynaptic membranes is a major plasticity mechanism: increasing AMPAR number strengthens synapses; removal weakens them. Subunit composition (GluA2 flip/flop) determines kinetics and calcium permeability.

## How It's Best Learned
Measure whole-cell AMPA currents using voltage clamp. Use immunofluorescence to quantify AMPAR localization during plasticity.

## Common Misconceptions
AMPA receptors are constitutively present—their numbers are dynamically regulated. All AMPA receptors are identical—subunit composition matters.

## Questions

```yaml
- question: "After strong stimulation that induces LTP at a synapse, synaptic strength increases over the following minutes. At the molecular level, this increased strength is primarily expressed by:"
  type: multiple-choice
  options:
    - "Increased glutamate release from the presynaptic terminal"
    - "More NMDA receptors inserted at the postsynaptic membrane"
    - "Increased number of AMPA receptors at the postsynaptic density through exocytosis and lateral diffusion from extrasynaptic pools"
    - "New AMPA receptors synthesized from scratch via upregulated gene expression"
  answer: 2
  explanation: "The expression of LTP is primarily postsynaptic and works by rapidly delivering existing AMPA receptors to the synapse surface, not by synthesizing new ones. CaMKII phosphorylates GluA1 subunits, promoting exocytosis of intracellular AMPAR vesicles and lateral diffusion of extrasynaptic receptors into the postsynaptic density. This can happen within minutes of LTP induction — far too fast for new gene expression. More AMPARs at the synapse means more ion channels open per glutamate release event, producing a larger excitatory postsynaptic potential. This is why AMPAR trafficking is called the expression mechanism of LTP."

- question: "A neuron with AMPA receptors lacking the GluA2 subunit would be expected to show which property?"
  type: multiple-choice
  options:
    - "Smaller currents per channel opening, because GluA2 enhances ion conductance"
    - "Calcium-permeable AMPA channels, potentially contributing directly to plasticity signaling"
    - "Complete loss of AMPAR function, since GluA2 is required for channel assembly"
    - "Resistance to internalization during LTD, since GluA2 is required for endocytosis"
  answer: 1
  explanation: "GluA2 contains a unique edited arginine residue in the channel pore that blocks calcium permeation. When GluA2 is present (as in most mature synapses), AMPARs are calcium-impermeable and have linear current-voltage relationships. Without GluA2, the channel becomes calcium-permeable — and calcium is the critical second messenger that triggers CaMKII activation and downstream plasticity signaling. GluA2-lacking receptors are therefore more than just ion channels; they are signaling entry points. This is why the ratio of GluA2-containing to GluA2-lacking receptors at a synapse affects both the strength and the plasticity potential of that synapse."

- question: "NMDA receptors are the primary expression mechanism of LTP because their activation directly produces the increased synaptic strength observed after potentiation."
  type: true-false
  answer: false
  explanation: "NMDA receptors detect the conditions for plasticity — they are the coincidence detectors that require simultaneous pre- and postsynaptic activity to open and allow calcium influx. But they are not the expression mechanism. The increased synaptic strength is expressed by having more AMPA receptors at the postsynaptic membrane. NMDA receptor activation triggers the signaling cascades (CaMKII phosphorylation, etc.) that drive AMPAR delivery — but it is the additional AMPARs that produce the stronger response to subsequent glutamate release. NMDA receptors remain roughly constant; AMPA receptor number changes."

- question: "Synaptic strength can be rapidly modulated by shuffling existing AMPA receptors to or from the postsynaptic membrane, without requiring synthesis of new receptor proteins."
  type: true-false
  answer: true
  explanation: "This is the key insight about AMPAR trafficking as a plasticity mechanism. Neurons maintain intracellular pools of AMPARs in endosomal compartments and on extrasynaptic regions of the dendritic membrane. During LTP, these existing receptors are delivered to the postsynaptic density via exocytosis and lateral diffusion within minutes. During LTD, surface receptors are removed via endocytosis and stored or degraded. Because the cell does not need to wait for new transcription or translation, trafficking-based plasticity can occur on timescales of seconds to minutes — fast enough to encode memory-relevant changes in synaptic strength."

- question: "Why is AMPA receptor trafficking described as the 'expression mechanism' of synaptic plasticity, and what distinct role do NMDA receptors play in this process?"
  type: short-answer
  answer: "AMPA receptor trafficking is the expression mechanism because it is the physical change that makes a synapse stronger or weaker: more AMPARs at the synapse surface means larger excitatory postsynaptic currents in response to glutamate; fewer means smaller currents. The synapse's strength is literally set by AMPAR number. NMDA receptors play the complementary role of detection: they are coincidence detectors that open only when both glutamate is present (presynaptic activity) and the postsynaptic membrane is depolarized (postsynaptic activity). The resulting calcium influx activates CaMKII and other kinases that phosphorylate GluA1, triggering AMPAR delivery. NMDA receptors sense the signal for change; AMPA receptor trafficking executes the change."
  explanation: "The separation of detection (NMDA) from expression (AMPA) has important functional implications. It means that the same NMDA receptor mechanism can produce either LTP or LTD depending on the magnitude of calcium influx and the downstream cascades activated — high calcium activates kinases and drives AMPAR insertion (LTP), while low calcium activates phosphatases and drives AMPAR removal (LTD). This gives the synapse a graded, bidirectional plasticity mechanism controlled by a single calcium signal of varying amplitude."
```

## Explainer

You already understand that ligand-gated ion channels open in response to neurotransmitter binding and that long-term potentiation strengthens synapses. AMPA receptors sit at the intersection of these two concepts: they are the ligand-gated channels responsible for most fast excitatory transmission in the brain, and changes in their number at the synapse are one of the primary ways LTP and LTD are physically expressed.

**AMPA receptors** (AMPARs) are tetramers — four protein subunits assembled into a functional channel. The subunits are called GluA1 through GluA4, and which combination assembles matters enormously. The critical subunit is **GluA2**: when it is present (which is most of the time in mature neurons), the channel is impermeable to calcium and has linear current-voltage properties. When GluA2 is absent, the channel becomes calcium-permeable — and calcium, as you know from studying LTP, is the key intracellular signal that triggers synaptic strengthening. So the subunit composition of an AMPA receptor determines not just how much current it passes, but whether it can directly contribute to plasticity signaling.

The real power of AMPA receptors as a plasticity mechanism lies in **trafficking** — the regulated insertion and removal of receptors from the postsynaptic membrane. Think of the synapse like a dock: the strength of the signal depends on how many receptors are waiting at the surface to catch glutamate when it arrives. During LTP, intracellular pools of AMPARs are rapidly delivered to the postsynaptic density through exocytosis and lateral diffusion along the membrane. During LTD, receptors are internalized via endocytosis — pulled back inside the cell. This means the synapse can change its sensitivity to glutamate in minutes without building new receptors from scratch, simply by reshuffling the ones it already has.

The molecular details of trafficking connect directly to the signaling cascades you studied in LTP. When NMDA receptors detect coincident pre- and postsynaptic activity and allow calcium influx, that calcium activates CaMKII, which phosphorylates GluA1 subunits and promotes their delivery to the synapse. Conversely, low-level calcium signals activate phosphatases that dephosphorylate GluA1 and trigger receptor internalization — the basis of LTD. This is why AMPA receptor trafficking is often called the "expression mechanism" of synaptic plasticity: NMDA receptors detect the conditions for change, but AMPA receptors are what actually changes. The synapse gets stronger or weaker because it has more or fewer AMPARs at the surface, and the molecular machinery controlling this trafficking is exquisitely sensitive to the pattern of neural activity.
