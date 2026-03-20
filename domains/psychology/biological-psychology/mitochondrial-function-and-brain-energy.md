---
id: mitochondrial-function-and-brain-energy
title: Mitochondrial Function and Energy Supply in the Brain
domain: psychology
course: biological-psychology
prerequisites:
- id: cellular-respiration-overview
  type: soft
- id: action-potential-generation-and-propagation
  type: soft
- id: mitochondria-structure-and-function
  type: soft
- id: atp-synthesis
  type: soft
builds-toward:
- neurodegenerative-disease-pathology
- cognitive-aging-and-decline
tags:
- mitochondria
- ATP
- energy
- metabolism
- aging
stage: advanced
status: draft
---

# Mitochondrial Function and Energy Supply in the Brain

## Core Idea
Neurons are metabolically expensive due to the ATP cost of maintaining ion gradients and synaptic transmission. Mitochondria generate ATP through oxidative phosphorylation, but this process generates reactive oxygen species (ROS) that damage proteins and lipids. Mitochondrial calcium uptake during high activity can trigger apoptosis if uncontrolled. Aging and neurodegeneration involve mitochondrial dysfunction—reduced ATP production, increased ROS, and impaired calcium handling—explaining why the brain is particularly vulnerable to age-related disease.

## How It's Best Learned
Measure ATP levels and ROS production during neural activity using fluorescent indicators. Compare mitochondrial function in young vs aged neural tissue and correlate with cognitive decline.

## Explainer

Neurons are among the most metabolically demanding cells in the body, and understanding why requires connecting two things you've already studied: action potentials and ATP synthesis. Every time a neuron fires, Na⁺ rushes in and K⁺ rushes out through ion channels, temporarily destroying the resting membrane potential. Restoring those gradients is the job of the Na⁺/K⁺-ATPase pump, which must continuously push ions back against their concentration gradients. This work is not free — it consumes ATP at a rate that makes the neuron almost constantly hungry for energy, especially in highly active regions like the prefrontal cortex and hippocampus. The brain is roughly 2% of body mass but consumes around 20% of the body's total oxygen supply.

**Oxidative phosphorylation** — the process you studied in ATP synthesis — is the primary engine of neuronal energy production. Mitochondria in neurons are not static; they shuttle along axons and dendrites, clustering near synapses where demand is highest. The electron transport chain on the inner mitochondrial membrane pumps protons across into the intermembrane space, and ATP synthase harnesses the return flow to phosphorylate ADP. The structural detail that matters here is the inner membrane's high surface area via cristae — more cristae means more ETC capacity, which is why neurons in high-activity regions tend to have mitochondria with especially dense cristae. But this high throughput comes with a byproduct: **reactive oxygen species (ROS)**, leaked electrons that react with oxygen to form superoxide and hydrogen peroxide, damaging local proteins and lipids.

Mitochondria also serve as critical **calcium buffers**. During intense synaptic activity, Ca²⁺ floods into the neuron through NMDA receptors and voltage-gated channels. Mitochondria take up this excess calcium, preventing it from reaching cytotoxic concentrations. But if activity is sustained long enough, mitochondrial calcium overload opens the **mitochondrial permeability transition pore (mPTP)**, collapsing the proton gradient, releasing apoptosis-triggering factors like cytochrome c, and initiating cell death. This is the mechanism linking excitotoxicity to neurodegeneration: too much glutamate → too much Ca²⁺ → mitochondrial overload → cell death.

In aging and neurodegeneration, all three of these functions deteriorate together. Mitochondrial DNA accumulates mutations over decades because it lacks histones and sits near the ROS-producing ETC. Mutated mtDNA produces defective ETC proteins, reducing ATP output and increasing ROS leak simultaneously. This creates a vicious cycle: damaged proteins impair calcium handling, which stresses remaining mitochondria further. The brain regions with the highest metabolic demand — cortex, basal ganglia, hippocampus — are the same regions that show earliest degeneration in Alzheimer's, Parkinson's, and Huntington's disease. Mitochondrial dysfunction is not just a symptom of neurodegeneration; it is a core causal mechanism driving it.
