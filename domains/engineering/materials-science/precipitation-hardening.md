---
id: precipitation-hardening
title: Precipitation Hardening
domain: engineering
course: materials-science
prerequisites:
- id: strengthening-mechanisms
  type: hard
- id: phase-diagrams-binary
  type: hard
builds-toward:
- materials-selection-design
tags:
- age-hardening
- nucleation-and-growth
- coherent-precipitates
- overaging
- guinier-preston-zones
stage: formal-systems
status: draft
---

# Precipitation Hardening

## Core Idea
Precipitation hardening (age hardening) strengthens an alloy by dispersing fine second-phase particles throughout the matrix, forcing dislocations to either cut through or bow around them. The process requires three steps: solution treatment (dissolving the solute into a single-phase solid solution at high temperature), quenching (rapidly cooling to trap the solute in a supersaturated state), and aging (holding at an intermediate temperature to allow controlled precipitation). During aging, precipitates evolve through a sequence — from coherent Guinier-Preston (GP) zones that share the matrix lattice, to semi-coherent intermediate precipitates, to incoherent equilibrium precipitates. Peak hardness occurs at an optimal aging time when precipitates are large enough to strongly impede dislocations but still coherent or semi-coherent with the matrix. Beyond this point, overaging occurs: precipitates coarsen (Ostwald ripening), lose coherency, and the spacing between them increases, reducing their effectiveness as barriers. The Al-Cu system is the classic example, but precipitation hardening is used extensively in nickel superalloys, maraging steels, and titanium alloys.

## How It's Best Learned
Plot hardness versus aging time at a fixed temperature to see the characteristic rise-to-peak-then-decline curve. Use a phase diagram with a solvus line to identify the temperature windows for solution treatment and aging. Examine TEM micrographs showing GP zones, intermediate precipitates, and coarsened equilibrium particles to connect microstructure to mechanical response at each aging stage.

## Common Misconceptions
- Precipitation hardening is not instantaneous after quenching — the supersaturated solution must be aged at a controlled temperature for the precipitates to form and reach optimal size.
- Overaging does not mean the material is ruined; it simply means the precipitates have grown past the peak-hardness configuration. The material can often be re-solution-treated and re-aged.
- Larger precipitates are not stronger obstacles — peak strength corresponds to fine, closely spaced precipitates that force dislocations to interact with many particles simultaneously.

## Explainer

From strengthening mechanisms, you know that strength in metals comes from making dislocation motion difficult. The more barriers a dislocation encounters — grain boundaries, solute atoms, other dislocations, or second-phase particles — the higher the stress required to push it through the lattice. **Precipitation hardening** exploits phase diagrams to generate a dense, tunable dispersion of very fine particles inside the crystal, creating the most potent obstacle array achievable in metallic systems.

The starting point is a phase diagram with a **solvus** line — a curved boundary that separates a single-phase solid solution (at high temperature) from a two-phase field (at lower temperature). In the Al-Cu system, above the solvus a copper-rich solid solution in aluminum is stable; below it, a second phase (the θ phase, CuAl₂) is thermodynamically favored. The three-step process uses this geometry directly. First, **solution treatment**: heat well above the solvus to dissolve all copper into a homogeneous FCC aluminum matrix. Second, **quench**: cool rapidly enough that copper atoms are frozen in place — they cannot diffuse to form the equilibrium θ phase, so the alloy is now a **supersaturated solid solution** out of equilibrium but temporarily stable. Third, **aging**: hold at an intermediate temperature. Here, with moderate thermal energy, copper atoms begin to cluster and precipitate. But the sequence of precipitates they form is not the equilibrium θ phase — not at first.

The early precipitates are **Guinier-Preston (GP) zones**: thin, plate-like clusters of copper atoms, just a few atomic layers thick, that remain coherent with the aluminum matrix (their lattice planes are continuous with the surrounding matrix). This coherency creates local strain fields around each zone, and it is these strain fields — not the zones themselves — that impede dislocations by forcing them to cut through mismatched lattice regions. As aging continues, GP zones grow into larger, semi-coherent intermediate precipitates (θ'' and θ'), which are even more effective obstacles. Peak hardness typically occurs at this semi-coherent stage: precipitates are large enough to create strong strain fields but still closely enough spaced that dislocations encounter many of them before traveling far.

Beyond peak hardness, **overaging** occurs. The intermediate precipitates grow into the incoherent equilibrium θ phase via Ostwald ripening — larger particles grow at the expense of smaller ones, because the smaller particles have higher surface energy. The equilibrium precipitates have no coherency strain field, so they are weaker obstacles. Worse, as the total number of particles decreases and average spacing increases, the **Orowan mechanism** becomes relevant: instead of cutting through particles, dislocations bow around them and bypass, leaving dislocation loops. The critical stress for Orowan bowing decreases as particle spacing increases. The result is a declining hardness curve with continued aging time. The engineering lesson is that aging time and temperature are variables to be optimized, not just minimized — there is a specific "peak aged" condition that maximizes strength.
