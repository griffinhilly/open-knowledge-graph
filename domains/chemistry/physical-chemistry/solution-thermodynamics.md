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

## Explainer

When you studied pure-substance thermodynamics, every property — G, H, S, V — belonged to the whole system. In a mixture, you need to know how each component contributes to the total, and that contribution depends on what else is present. The **partial molar quantity** captures this: the partial molar Gibbs energy of component i, written (∂G/∂nᵢ) at constant T, P, and all other nⱼ, is the **chemical potential** μᵢ. It tells you how much the total Gibbs energy changes when you add an infinitesimal amount of component i to the mixture. Chemical potential governs everything — phase equilibrium requires equal μᵢ across phases, and reactions proceed in the direction that lowers total μ.

An **ideal solution** is the simplest model: every molecule interacts with its neighbors the same way regardless of identity. If ethanol and water formed an ideal solution, an ethanol molecule surrounded by water molecules would "feel" the same forces as one surrounded by other ethanol molecules. In this case, the chemical potential takes a clean logarithmic form: μᵢ = μᵢ* + RT ln(xᵢ), where xᵢ is the mole fraction and μᵢ* is the chemical potential of pure component i. This leads to Raoult's law for vapor pressures: Pᵢ = xᵢPᵢ*, and the thermodynamics of mixing are driven entirely by entropy — ΔmixH = 0 and ΔmixV = 0, with ΔmixG = RT Σ xᵢ ln(xᵢ), which is always negative because ln(xᵢ) < 0.

Real solutions deviate from this picture because molecular interactions are not symmetric. Ethanol-water, for example, shows negative deviations from Raoult's law — the vapor pressure is lower than predicted — because hydrogen bonding between ethanol and water is stronger than the average of ethanol-ethanol and water-water interactions. Other systems like acetone-carbon disulfide show positive deviations, where unlike molecules interact less favorably than like molecules. To handle this, we introduce the **activity coefficient** γᵢ, defining activity as aᵢ = γᵢxᵢ. When γᵢ = 1, the solution is ideal; γᵢ > 1 indicates positive deviations (molecules "want to escape" more than in an ideal solution), and γᵢ < 1 indicates negative deviations.

The **excess Gibbs energy** G^E = ΔmixG − ΔmixG(ideal) quantifies the total departure from ideality and is directly related to activity coefficients through ln(γᵢ) = (∂G^E/∂nᵢ)/RT. Models like the Margules equation (G^E = A·x₁·x₂ for a symmetric system) or the Wilson equation parameterize G^E as a function of composition, allowing you to predict activity coefficients, vapor-liquid equilibrium, and liquid-liquid phase separation from a small number of fitted parameters. This is the foundation of chemical engineering design: distillation columns, extraction processes, and crystallization all depend on knowing how far a real solution departs from ideality, and the framework of partial molar quantities and activity coefficients provides the rigorous language for quantifying those departures.
