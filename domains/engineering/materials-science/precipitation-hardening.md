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
