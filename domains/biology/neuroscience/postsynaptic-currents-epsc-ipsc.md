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
stage: advanced
status: draft
---

# Postsynaptic Currents: EPSCs and IPSCs

## Core Idea
EPSCs: Na+/Ca2+ inward current through glutamate receptors, depolarizes. IPSCs: Cl− inward through GABA_A, hyperpolarizes. Sum determines firing.

## Explainer

You already understand the distinction between ionotropic and metabotropic receptors and know how action potentials involve depolarization and repolarization. **Postsynaptic currents** are the electrical events that ionotropic receptors produce when neurotransmitter binds — they are the fundamental units of fast synaptic communication, and understanding them is essential for grasping how neurons integrate information from thousands of inputs to decide whether to fire.

An **excitatory postsynaptic current** (EPSC) occurs when glutamate binds to ionotropic glutamate receptors (AMPA and NMDA types), opening channels that are permeable to Na⁺ and, in the case of NMDA receptors, Ca²⁺. Because the electrochemical driving force pushes these cations inward at resting membrane potential, the net effect is an inward current — positive charges flowing into the cell. This inward current produces a small, transient depolarization called an excitatory postsynaptic potential (EPSP). A single EPSC from one synapse is far too small to bring the neuron to threshold on its own — typically only 0.5–1 mV at the soma. The neuron must summate many EPSCs, either from multiple synapses firing near-simultaneously (**spatial summation**) or from the same synapse firing repeatedly (**temporal summation**), to reach the ~15 mV depolarization needed to trigger an action potential.

An **inhibitory postsynaptic current** (IPSC) works in the opposite direction. When GABA binds to GABA_A receptors, channels open that are selectively permeable to Cl⁻ ions. In most adult neurons, the chloride equilibrium potential is near or slightly negative to the resting potential, so Cl⁻ flows inward, producing an outward current (in electrical convention, negative charge moving in is equivalent to positive charge moving out). This drives the membrane potential toward the chloride reversal potential, which is typically around −75 mV — further from threshold. Even when the IPSC does not noticeably hyperpolarize the cell, it increases the membrane's conductance, effectively **shunting** nearby excitatory currents by providing a low-resistance path to the chloride equilibrium potential. This shunting inhibition is particularly powerful when inhibitory synapses are located on the soma or axon initial segment, where they can veto excitatory inputs arriving from the entire dendritic tree.

The neuron's firing decision emerges from the continuous, moment-by-moment balance between EPSCs and IPSCs. At any given instant, a cortical neuron might be receiving hundreds of excitatory and inhibitory inputs. The net postsynaptic current — the algebraic sum of all EPSCs and IPSCs — determines whether the membrane potential at the axon hillock crosses threshold. This is not a simple addition: the timing, location, and conductance of each input all matter. An IPSC arriving a few milliseconds before a volley of EPSCs can cancel the excitation entirely, while the same IPSC arriving too late has no effect. This dynamic integration of opposing currents is how neural circuits implement computation — selecting which signals pass through and which are suppressed, shaping the temporal precision of neural coding with millisecond accuracy.
