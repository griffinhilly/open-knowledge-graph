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
status: draft
---

# NMDA Receptors: Structure and Properties

## Core Idea
NMDA receptors require both glutamate binding AND postsynaptic depolarization (to relieve Mg2+ block) to open. This voltage-dependent gating makes NMDARs coincidence detectors critical for Hebbian learning. NMDARs pass large amounts of calcium, triggering plasticity. Excessive activation causes excitotoxicity.

## How It's Best Learned
Measure NMDAR current across different holding potentials. Model Mg2+ block using Boltzmann kinetics.

## Common Misconceptions
NMDA receptors are fast like AMPA receptors—NMDARs have slower kinetics. All glutamate receptors are identical—NMDARs pass more Ca2+ than AMPARs.

## Explainer

You already know that ligand-gated ion channels open when a neurotransmitter binds them, allowing ions to flow across the membrane. NMDA receptors follow this basic principle — they are glutamate-gated ion channels — but they add a critical twist that makes them unlike any other channel in the nervous system. To understand why NMDARs are considered the molecular foundation of learning, you need to grasp what makes their gating mechanism special.

Most ligand-gated channels have a simple rule: bind the transmitter, open the pore. **NMDA receptors require two conditions to be met simultaneously**. First, glutamate (plus the co-agonist glycine or D-serine) must be bound to the receptor. Second, the postsynaptic membrane must be sufficiently depolarized. The reason for this dual requirement is a **magnesium block**: at resting membrane potential (around −65 mV), a Mg²⁺ ion sits in the channel pore, physically blocking ion flow even when glutamate is bound. Only when the membrane depolarizes — typically because nearby AMPA receptors have already been activated by the same glutamate release — does the Mg²⁺ ion get expelled by electrostatic repulsion, allowing current to flow through the NMDA channel. This means the NMDAR opens only when presynaptic activity (glutamate release) and postsynaptic activity (depolarization) occur at the same time.

This **coincidence detection** property is what makes NMDARs the biological implementation of Hebb's rule — "neurons that fire together, wire together." When a presynaptic neuron releases glutamate while the postsynaptic neuron is already depolarized, NMDARs open and allow a flood of **calcium ions** (Ca²⁺) into the postsynaptic cell. NMDA receptors are highly permeable to calcium compared to AMPA receptors, and this calcium influx is the critical trigger for synaptic plasticity. The calcium activates intracellular signaling cascades — including CaMKII, calcineurin, and various protein kinases — that lead to lasting changes in synaptic strength, the molecular basis of long-term potentiation and long-term depression.

Structurally, NMDA receptors are **heterotetramers**, typically composed of two obligatory GluN1 subunits and two GluN2 subunits (GluN2A, 2B, 2C, or 2D). The GluN1 subunits bind the co-agonist glycine, while GluN2 subunits bind glutamate. The subunit composition determines the receptor's kinetics, Mg²⁺ sensitivity, and calcium permeability — GluN2B-containing receptors, for instance, have slower kinetics and are particularly important during development. The channel has notably slow kinetics compared to AMPA receptors: it opens slowly, stays open longer, and thus provides a prolonged window for calcium entry. This slow timecourse also means that NMDARs contribute relatively little to the fast excitatory postsynaptic potential but are essential for the integrative and plasticity functions of the synapse. The flip side of calcium entry is **excitotoxicity**: excessive NMDAR activation during stroke or seizures floods neurons with calcium, triggering cell death pathways — a reminder that the same mechanism underlying learning can become destructive when uncontrolled.
