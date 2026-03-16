---
id: nad-nadh-structure-and-function
title: 'NAD+ and NADH: Structure and Redox Chemistry'
domain: biology
course: biochemistry
prerequisites:
- id: enzyme-cofactors-and-coenzymes
  type: hard
- id: organic-chemistry-intro
  type: soft
- id: carbonyl-chemistry-intro
  type: soft
- id: oxidation-numbers
  type: soft
- id: oxidation-reduction-basics
  type: soft
- id: oxidation-reduction-reactions
  type: soft
- id: redox-chemistry-intro
  type: soft
builds-toward:
- glycolysis
- citric-acid-cycle-mechanism
- fatty-acid-oxidation-beta-oxidation
tags:
- cofactors
- redox
- NAD+
- NADH
stage: advanced
status: draft
---

# NAD+ and NADH: Structure and Redox Chemistry

## Core Idea
NAD+ is the major electron carrier in catabolic pathways, accepting hydride ions (H⁻) from substrates and being reduced to NADH. The NAD+/NADH ratio determines the direction of equilibrium in NAD+-dependent reactions and reflects cellular energy status. High NADH/NAD+ indicates a reduced state and metabolic energy; low NADH/NAD+ indicates oxidative stress.

## Explainer

You already know that coenzymes are small organic molecules that assist enzymes by carrying chemical groups between reactions. **NAD⁺** (nicotinamide adenine dinucleotide) is arguably the most important coenzyme in all of metabolism, because it serves as the cell's primary electron shuttle — picking up high-energy electrons from fuel molecules during catabolism and delivering them to the electron transport chain for ATP production.

Structurally, NAD⁺ consists of two nucleotides joined through their phosphate groups. One nucleotide contains adenine (which you recognize from ATP), and the other contains **nicotinamide**, a derivative of vitamin B₃ (niacin). The nicotinamide ring is where the chemistry happens. In its oxidized form (NAD⁺), the ring carries a positive charge and can accept a **hydride ion** (H⁻) — essentially a hydrogen atom with an extra electron. This is not just a single electron transfer; the hydride brings two electrons at once, reducing NAD⁺ to **NADH**. A second hydrogen from the substrate is released as H⁺ into solution. The reaction can be written as: Substrate-H₂ + NAD⁺ → Substrate + NADH + H⁺. From your redox chemistry background, you can see this is an oxidation of the substrate coupled to a reduction of NAD⁺.

What makes this system so powerful is that NADH is a concentrated packet of reducing power. The two electrons it carries are at a high energy level, and when NADH later donates them to Complex I of the electron transport chain, that energy is released in controlled steps to pump protons and ultimately drive ATP synthesis. Think of NAD⁺ as an empty electron taxi and NADH as a loaded one — the loaded taxi delivers its passengers (electrons) to the electron transport chain, gets emptied back to NAD⁺, and returns to pick up more electrons from metabolic reactions.

The **NAD⁺/NADH ratio** acts as a metabolic thermostat for the cell. When NADH accumulates faster than the electron transport chain can oxidize it, the ratio drops, and NAD⁺-dependent reactions in glycolysis and the citric acid cycle slow down because they need NAD⁺ as a substrate. Conversely, when the cell is actively consuming ATP and the electron transport chain is running fast, NADH is rapidly reoxidized to NAD⁺, keeping catabolic pathways flowing. This ratio therefore links the rate of fuel oxidation directly to the cell's energy demand — an elegant feedback mechanism that prevents the cell from burning fuel it does not need.
