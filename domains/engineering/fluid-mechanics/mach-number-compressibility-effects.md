---
id: mach-number-compressibility-effects
title: Mach Number and Compressibility Effects on Flow Properties
domain: engineering
course: fluid-mechanics
prerequisites:
- id: compressible-flow-basics
  type: hard
- id: dimensional-analysis-and-similarity
  type: soft
builds-toward:
- normal-shock-pressure-temperature-relations
tags:
- mach-number
- compressibility
- speed-of-sound
stage: advanced
status: draft
---

# Mach Number and Compressibility Effects on Flow Properties

## Core Idea
The Mach number, M = V/a (velocity over speed of sound), determines whether compressibility effects dominate. For M < 0.3, density changes are typically negligible and incompressible analysis is adequate. For M > 0.3, pressure, temperature, and density variations become significant and compressible flow equations must be used. Understanding Mach number regime determines whether to use simplified or full compressible analysis.

## Explainer

From your compressible flow prerequisites, you know that sound is a pressure wave propagating at speed a = √(γRT) through the fluid. The **Mach number** M = V/a is not just a speed ratio — it is the ratio of how fast the flow moves information by convection to how fast acoustic signals can propagate. This ratio governs the entire character of compressible flow.

When M is small (say, 0.1), a slight perturbation — a bump on a wall, a change in pressure — sends acoustic signals outward in all directions much faster than the fluid is moving. These signals can reach upstream, adjusting the flow well before fluid arrives at the obstacle. The flow effectively "knows" what's coming. Density changes caused by even strong pressure variations remain under a few percent (compressibility scales roughly as M²/2 for isentropic flow), so treating the fluid as incompressible introduces negligible error. Once M exceeds about 0.3, the density change exceeds ~5% and errors in the pressure, temperature, and velocity fields begin to compound. For M > 1, the situation changes qualitatively: the flow is moving faster than sound, so acoustic signals cannot propagate upstream at all. A supersonic flow has no advance warning of an obstacle; the adjustment must happen abruptly through a **shock wave**.

The Mach number delineates four practical flow regimes. **Subsonic** (M < 1): smooth, wave-free adjustment everywhere; incompressible approximation good below M ≈ 0.3. **Transonic** (M ≈ 0.8–1.2): a mix of subsonic and supersonic regions coexist, often with embedded shocks; this is aerodynamically complex and the regime where most commercial aircraft operate. **Supersonic** (M > 1): shocks form at leading edges and at any geometric change; pressure, temperature, and density jump discontinuously across shocks. **Hypersonic** (M > 5): extreme temperature rise across shocks drives chemical dissociation and ionization of the gas, requiring thermochemistry beyond perfect-gas assumptions.

The practical decision rule follows from this: before applying any flow analysis, compute or estimate the Mach number and classify the flow. Below M ≈ 0.3, Bernoulli and incompressible continuity are excellent tools. Above that threshold, density is a variable — it couples with pressure and temperature through the equation of state, requiring the full isentropic flow relations, normal shock tables, or oblique shock analysis depending on geometry. The M = 0.3 cutoff is a guideline, not a cliff: for high-precision work (compressor blade aerodynamics, transonic wind tunnel corrections), even M ≈ 0.2 demands compressibility corrections.
