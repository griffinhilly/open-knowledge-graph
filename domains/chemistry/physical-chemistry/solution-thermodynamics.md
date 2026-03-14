---
id: solution-thermodynamics
title: 'Solution Thermodynamics: Partial Molar Quantities and Activity'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: statistical-thermodynamics-applications
  type: hard
builds-toward: []
tags:
- partial-molar-quantities
- mixing-thermodynamics
- activity-coefficients
- excess-functions
- ideal-solutions
- chemical-potential
stage: advanced
status: draft
---

# Solution Thermodynamics: Partial Molar Quantities and Activity

## Core Idea
In mixtures, the thermodynamic properties of each component depend on composition, and partial molar quantities capture this dependence. The partial molar Gibbs energy is the chemical potential: mu_i = (dG/dn_i)_{T,P,n_j}, which governs phase equilibria and reaction direction. Ideal solutions obey Raoult's law (mu_i = mu_i* + RT*ln(x_i)), but real solutions deviate, requiring activity coefficients gamma_i such that a_i = gamma_i * x_i. The thermodynamics of mixing -- Delta_mix G, H, S, and V -- distinguish ideal behavior (Delta_mix H = 0, Delta_mix V = 0) from non-ideal behavior where excess functions G^E, H^E, S^E quantify the departure from ideality. Models like Margules, van Laar, and Wilson equations parameterize G^E as a function of composition and are essential for chemical engineering applications including distillation design and liquid-liquid equilibrium prediction.

## How It's Best Learned
Measure or analyze vapor pressure data for a binary liquid mixture (e.g., ethanol-water), compute activity coefficients from Raoult's law deviations, and plot G^E vs composition. Connecting positive deviations to unfavorable interactions and negative deviations to favorable ones gives physical intuition for the mathematical formalism.

## Common Misconceptions
- Confusing mole fraction with activity; activity equals mole fraction only in ideal solutions -- real solutions can have activity coefficients far from unity, especially at dilute or concentrated extremes.
- Thinking Delta_mix G < 0 means the solution is ideal; all spontaneous mixing has Delta_mix G < 0, but ideal mixing additionally requires Delta_mix H = 0.
