---
id: helmholtz-gibbs-free-energy
title: 'Helmholtz and Gibbs Free Energy: Maximum Work'
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: legendre-transformations-thermodynamics
  type: hard
- id: second-law-thermodynamics-entropy
  type: hard
builds-toward:
- chemical-equilibrium-reaction-analysis
tags:
- helmholtz
- gibbs
- free-energy
- available-work
- spontaneity
stage: advanced
status: draft
---

# Helmholtz and Gibbs Free Energy: Maximum Work

## Core Idea
Helmholtz free energy A = U - TS represents maximum useful work for systems at constant T and V; Gibbs free energy G = H - TS for constant T and P. Both decrease for spontaneous processes; equilibrium occurs at minimum G or A. Negative ΔG indicates spontaneous reaction; ΔG° = -RT ln(K_p) relates standard state free energy to the equilibrium constant.

## Explainer

You already know from the second law and entropy that spontaneous processes increase total entropy (system plus surroundings), and from Legendre transformations that you can recast thermodynamic relations by switching independent variables. The free energies bring both ideas together in a remarkably practical form: they tell you whether a process will happen spontaneously **without** explicitly tracking the entropy of the surroundings.

The argument is as follows. For a system at constant temperature in contact with a heat reservoir, the Clausius inequality gives dS_total = dS_system + dS_surroundings ≥ 0. The surroundings exchange heat reversibly, so dS_surroundings = −dQ_system/T. Substituting and rearranging: dU − T·dS ≤ 0 at constant T and V (no boundary work). Define **Helmholtz free energy** A = U − TS. Then dA ≤ 0 at constant T and V — the Helmholtz free energy can only decrease or stay constant. It reaches its minimum at equilibrium. A is also equal to the maximum work a system can do in an isothermal, constant-volume process: W_max = −ΔA. The "free" energy is literally the energy free to do work after entropy costs are paid to the environment.

Most engineering systems operate at constant temperature and pressure, not constant volume. For these, the relevant potential is **Gibbs free energy** G = H − TS = U + PV − TS. By the same argument, dG ≤ 0 at constant T and P — G is minimized at equilibrium. This is why G is the central quantity in chemistry and chemical engineering: reactions in open vessels at atmospheric pressure happen at constant T and P. ΔG < 0 means spontaneous; ΔG > 0 means the reverse reaction is spontaneous; ΔG = 0 means equilibrium.

The quantitative link to equilibrium constants comes from the standard-state relation **ΔG° = −RT ln(K_p)**. The standard free energy change ΔG° measures the free energy difference when all reactants and products are at standard conditions (1 bar, 298 K). K_p is the equilibrium constant in terms of partial pressures. If ΔG° is large and negative, K_p ≫ 1 — products are strongly favored at equilibrium. If ΔG° is large and positive, K_p ≪ 1 — reactants dominate. A system not at equilibrium has ΔG = ΔG° + RT ln(Q), where Q is the reaction quotient; the system moves spontaneously in whichever direction reduces G until Q = K_p and ΔG = 0. This framework transforms the second law from a qualitative principle ("entropy increases") into a quantitative engineering tool for predicting reaction extents, phase boundaries, and material stability.
