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
- synaptic-strength-plasticity
tags:
- ampa
- ampar
- trafficking
- plasticity
stage: advanced
status: draft
---

# AMPA Receptors: Structure, Trafficking, and Function

## Core Idea
AMPA receptors are tetrameric ionotropic glutamate receptors mediating fast excitatory transmission. Trafficking to and from postsynaptic membranes is a major plasticity mechanism: increasing AMPAR number strengthens synapses; removal weakens them. Subunit composition (GluA2 flip/flop) determines kinetics and calcium permeability.

## How It's Best Learned
Measure whole-cell AMPA currents using voltage clamp. Use immunofluorescence to quantify AMPAR localization during plasticity.

## Common Misconceptions
AMPA receptors are constitutively present—their numbers are dynamically regulated. All AMPA receptors are identical—subunit composition matters.

## Explainer

You already understand that ligand-gated ion channels open in response to neurotransmitter binding and that long-term potentiation strengthens synapses. AMPA receptors sit at the intersection of these two concepts: they are the ligand-gated channels responsible for most fast excitatory transmission in the brain, and changes in their number at the synapse are one of the primary ways LTP and LTD are physically expressed.

**AMPA receptors** (AMPARs) are tetramers — four protein subunits assembled into a functional channel. The subunits are called GluA1 through GluA4, and which combination assembles matters enormously. The critical subunit is **GluA2**: when it is present (which is most of the time in mature neurons), the channel is impermeable to calcium and has linear current-voltage properties. When GluA2 is absent, the channel becomes calcium-permeable — and calcium, as you know from studying LTP, is the key intracellular signal that triggers synaptic strengthening. So the subunit composition of an AMPA receptor determines not just how much current it passes, but whether it can directly contribute to plasticity signaling.

The real power of AMPA receptors as a plasticity mechanism lies in **trafficking** — the regulated insertion and removal of receptors from the postsynaptic membrane. Think of the synapse like a dock: the strength of the signal depends on how many receptors are waiting at the surface to catch glutamate when it arrives. During LTP, intracellular pools of AMPARs are rapidly delivered to the postsynaptic density through exocytosis and lateral diffusion along the membrane. During LTD, receptors are internalized via endocytosis — pulled back inside the cell. This means the synapse can change its sensitivity to glutamate in minutes without building new receptors from scratch, simply by reshuffling the ones it already has.

The molecular details of trafficking connect directly to the signaling cascades you studied in LTP. When NMDA receptors detect coincident pre- and postsynaptic activity and allow calcium influx, that calcium activates CaMKII, which phosphorylates GluA1 subunits and promotes their delivery to the synapse. Conversely, low-level calcium signals activate phosphatases that dephosphorylate GluA1 and trigger receptor internalization — the basis of LTD. This is why AMPA receptor trafficking is often called the "expression mechanism" of synaptic plasticity: NMDA receptors detect the conditions for change, but AMPA receptors are what actually changes. The synapse gets stronger or weaker because it has more or fewer AMPARs at the surface, and the molecular machinery controlling this trafficking is exquisitely sensitive to the pattern of neural activity.
