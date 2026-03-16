---
id: sodium-potassium-atpase
title: 'The Na+/K+-ATPase: Maintaining Ion Gradients'
domain: biology
course: neuroscience
prerequisites:
- id: active-transport
  type: hard
- id: neuronal-compartments
  type: soft
- id: atp-hydrolysis-and-free-energy
  type: hard
builds-toward:
- resting-membrane-potential
- nernst-equation
tags:
- ion-transport
- energy-metabolism
- homeostasis
stage: advanced
status: draft
---

# The Na+/K+-ATPase: Maintaining Ion Gradients

## Core Idea
The Na+/K+-ATPase pumps three Na+ ions out and two K+ ions into the cell using ATP hydrolysis, maintaining the steep concentration gradients essential for neuronal excitability. Although the pump generates a small electrogenic (outward) current, its primary role is establishing chemical driving forces that ion channels subsequently exploit for electrical signaling.

## Explainer

You already understand that active transport moves molecules against their concentration gradient using energy, and that ATP hydrolysis releases free energy that can power cellular work. The **Na⁺/K⁺-ATPase** (also called the sodium-potassium pump) is the single most important active transporter in neurons — and arguably in all animal cells. It consumes roughly 20–40% of the brain's total energy budget, and without it, neurons would lose their ability to fire within minutes.

The pump is a transmembrane protein that operates through a repeating conformational cycle. In its inward-facing state, it binds three Na⁺ ions from the cytoplasm. ATP then binds and is hydrolyzed, transferring a phosphate group to the pump itself — this **phosphorylation** triggers a conformational change that opens the pump to the extracellular side and releases the three Na⁺ ions outside the cell. In this outward-facing, phosphorylated state, the pump binds two K⁺ ions from the extracellular fluid. Dephosphorylation then triggers the reverse conformational change, returning the pump to its inward-facing state and releasing the two K⁺ ions into the cytoplasm. One complete cycle: 3 Na⁺ out, 2 K⁺ in, 1 ATP consumed. Each pump completes this cycle roughly 100–300 times per second.

The asymmetry of the pump — three positive charges out for every two in — means it generates a small net outward current, making the inside of the cell slightly more negative. This is the **electrogenic** contribution of the pump, but it accounts for only about −3 to −5 mV of the resting potential. The pump's far more important role is maintaining the **concentration gradients** themselves: high Na⁺ outside (~145 mM) and low inside (~15 mM); high K⁺ inside (~140 mM) and low outside (~5 mM). These gradients are the stored energy that ion channels exploit. When a voltage-gated Na⁺ channel opens during an action potential, Na⁺ rushes inward down the concentration gradient the pump established — the pump did the work of pushing Na⁺ uphill in advance, and the channel lets it flow back downhill to generate the electrical signal.

Think of the Na⁺/K⁺-ATPase as a battery charger. Ion channels are like the devices that drain the battery — each action potential lets a small amount of Na⁺ in and K⁺ out, slightly dissipating the gradients. The pump continuously recharges the system by restoring those gradients. A single action potential moves only a tiny fraction of the total ions (the concentration change is negligible), so a neuron can fire thousands of times before the gradients degrade noticeably even if the pump were suddenly stopped. But over the long term, the pump is essential — block it with the cardiac glycoside **ouabain**, and within minutes the ion gradients collapse, the resting potential depolarizes, and the neuron can no longer generate action potentials. The Na⁺/K⁺-ATPase thus provides the thermodynamic foundation upon which all electrical signaling in the nervous system is built.
