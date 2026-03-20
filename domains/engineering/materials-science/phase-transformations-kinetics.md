---
id: phase-transformations-kinetics
title: Kinetics of Solid-State Phase Transformations
domain: engineering
course: materials-science
prerequisites:
- id: binary-phase-diagrams
  type: hard
- id: diffusion-mechanisms-materials
  type: hard
builds-toward:
- heat-treatment-steels
tags:
- phase-transformations
- kinetics
- nucleation-growth
- ttc-curves
stage: advanced
status: draft
---

# Kinetics of Solid-State Phase Transformations

## Core Idea
Phase transformations proceed from metastable states toward equilibrium through nucleation (formation of new phase) and growth (expansion of new phase), with both processes being temperature-dependent and often diffusion-controlled. Time-temperature-transformation (TTT) curves quantify transformation kinetics and show how cooling rate affects final microstructure. Rapid cooling can suppress equilibrium transformations, producing non-equilibrium phases like martensite, enabling strength enhancement through heat treatment.

## Explainer

Your prerequisite on binary phase diagrams tells you what phase is thermodynamically stable at a given composition and temperature — but not how fast you get there. Kinetics is the study of transformation rates, and it reveals something crucial: a material can persist indefinitely in a thermodynamically unstable (metastable) state if the transformation pathway is too slow. This gap between equilibrium prediction and actual behavior is what heat treatment exploits.

Every solid-state phase transformation proceeds in two steps: **nucleation** and **growth**. Nucleation is the formation of a small embryo of the new phase within the parent phase. This requires energy for two competing reasons: creating the new phase lowers the bulk free energy (favorable), but creating a new interface costs surface energy (unfavorable). The result is an energy barrier that only embryos above a **critical radius** can overcome — smaller ones dissolve back into the matrix, larger ones grow. At temperatures just below the equilibrium transformation temperature, the driving force for transformation is small (little free energy difference) and the barrier is high, so nucleation is slow. At temperatures much lower, diffusion is sluggish and atoms cannot rearrange quickly enough. In between is the **nose** of the TTT curve — the temperature of maximum transformation rate.

**TTT curves** (time-temperature-transformation diagrams) map the time required to start and complete a phase transformation as a function of temperature. For steel held isothermally below the eutectoid temperature, the TTT diagram shows a C-shaped curve: slow transformation near the eutectoid (little driving force), fastest transformation at intermediate temperature (nose), and slow again at low temperatures (limited diffusion). If you cool steel fast enough to pass to the left of the nose — never giving the austenite time to transform — you suppress the diffusion-controlled transformation entirely. The austenite becomes supersaturated and transforms instead by **martensite**: a diffusionless, shear transformation where carbon atoms are trapped in a body-centered tetragonal structure under enormous lattice strain. This is why quenched steel is extremely hard — the trapped carbon distorts the lattice and blocks dislocation motion — but also brittle.

The practical recipe for steel heat treatment follows directly: austenitize to dissolve carbon uniformly, quench rapidly past the TTT nose to form martensite, then **temper** at a moderate temperature to allow some carbon to precipitate as fine carbides, reducing hardness but greatly improving toughness. The final microstructure — and thus mechanical properties — is entirely determined by the cooling rate relative to the TTT curve. Slow cooling gives soft pearlite (layered ferrite + cementite), intermediate cooling gives bainite, rapid cooling gives martensite. This ability to tune microstructure and properties through controlled cooling is the foundation of all ferrous metallurgy, and it is only possible because kinetics allows materials to be trapped in non-equilibrium states.
