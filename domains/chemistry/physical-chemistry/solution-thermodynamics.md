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
stage: expert
status: validated
---

# Solution Thermodynamics: Partial Molar Quantities and Activity

## Core Idea
In mixtures, the thermodynamic properties of each component depend on composition, and partial molar quantities capture this dependence. The partial molar Gibbs energy is the chemical potential: mu_i = (dG/dn_i)_{T,P,n_j}, which governs phase equilibria and reaction direction. Ideal solutions obey Raoult's law (mu_i = mu_i* + RT*ln(x_i)), but real solutions deviate, requiring activity coefficients gamma_i such that a_i = gamma_i * x_i. The thermodynamics of mixing -- Delta_mix G, H, S, and V -- distinguish ideal behavior (Delta_mix H = 0, Delta_mix V = 0) from non-ideal behavior where excess functions G^E, H^E, S^E quantify the departure from ideality. Models like Margules, van Laar, and Wilson equations parameterize G^E as a function of composition and are essential for chemical engineering applications including distillation design and liquid-liquid equilibrium prediction.

## How It's Best Learned
Measure or analyze vapor pressure data for a binary liquid mixture (e.g., ethanol-water), compute activity coefficients from Raoult's law deviations, and plot G^E vs composition. Connecting positive deviations to unfavorable interactions and negative deviations to favorable ones gives physical intuition for the mathematical formalism.

## Common Misconceptions
- Confusing mole fraction with activity; activity equals mole fraction only in ideal solutions -- real solutions can have activity coefficients far from unity, especially at dilute or concentrated extremes.
- Thinking Delta_mix G < 0 means the solution is ideal; all spontaneous mixing has Delta_mix G < 0, but ideal mixing additionally requires Delta_mix H = 0.

## Questions

```yaml
- question: "A chemist measures the vapor pressure of component A above a binary liquid mixture and finds it is 35% higher than Raoult's law predicts (P_A > x_A · P_A*). Which statement correctly interprets this result?"
  type: multiple-choice
  options:
    - "The mole fraction x_A was calculated incorrectly; higher vapor pressure simply means more A is present"
    - "The activity coefficient γ_A > 1, indicating A-B molecular interactions are less favorable than A-A interactions, so A molecules escape the liquid more readily"
    - "The chemical potential of A in the mixture is lower than in pure liquid A, consistent with strong A-B attractions"
    - "This measurement is impossible; Raoult's law holds exactly for all binary mixtures"
  answer: 1
  explanation: "A vapor pressure above the Raoult's law prediction is a positive deviation, quantified by activity coefficient γ_A > 1 (since P_A = γ_A x_A P_A*). It means A-B interactions are weaker than the average of A-A and B-B interactions — A molecules 'want to escape' the solution more than they would in an ideal mixture. Option C describes the opposite situation (negative deviation, γ < 1), which would result from unusually strong A-B attractions. This misconception — thinking stronger interactions always raise vapor pressure — is common."

- question: "For an ideal solution formed by mixing two liquids at constant T and P, which thermodynamic statement is always true?"
  type: multiple-choice
  options:
    - "The enthalpy of mixing is negative because forming unlike-molecule pairs releases energy"
    - "The entropy of mixing is zero because the molecules are indistinguishable in an ideal solution"
    - "The Gibbs energy of mixing is negative, driven entirely by the entropy of mixing since ΔmixH = 0"
    - "The volume of the mixture is greater than the sum of pure component volumes"
  answer: 2
  explanation: "In an ideal solution, by definition ΔmixH = 0 (unlike-molecule interactions are identical to like-molecule interactions) and ΔmixV = 0. Therefore ΔmixG = −TΔmixS, which is always negative because mixing increases entropy (ΔmixS = −R Σ xi ln xi > 0 since ln xi < 0 for all xi < 1). Option A describes non-ideal behavior with negative deviations from Raoult's law. Option B reverses the truth — entropy of mixing is always positive (non-zero) even in ideal solutions."

- question: "If the Gibbs energy of mixing (ΔmixG) is negative for two liquids, the solution should be behaving ideally."
  type: true-false
  answer: false
  explanation: "All spontaneous mixing produces ΔmixG < 0 — this is simply the criterion for the mixing process to occur spontaneously. It says nothing about whether behavior is ideal or not. Ideal mixing additionally requires ΔmixH = 0 and ΔmixV = 0. A strongly non-ideal solution (e.g., acetone-chloroform with large negative excess Gibbs energy) still has ΔmixG < 0. The excess Gibbs energy G^E = ΔmixG − ΔmixG(ideal) is the quantity that captures deviation from ideality; G^E = 0 characterizes ideal solutions, not simply ΔmixG < 0."

- question: "An activity coefficient γ_i = 0.6 means that component i behaves thermodynamically as if its concentration in the mixture is less than its actual mole fraction."
  type: true-false
  answer: true
  explanation: "Activity is defined as a_i = γ_i · x_i, so γ_i = 0.6 means a_i = 0.6 x_i — the component's 'effective thermodynamic concentration' is 40% lower than its actual mole fraction. This represents a negative deviation from Raoult's law: A-B interactions are stronger than average, so molecules are less prone to escape into the vapor phase. Chemical potential, vapor pressure, and all thermodynamic equilibria depend on activity, not mole fraction, so in real solutions γ ≠ 1 changes equilibrium predictions significantly."

- question: "Explain why activity coefficients can deviate substantially from 1 in real solutions, and describe the molecular-level interpretation of γ > 1 versus γ < 1."
  type: short-answer
  answer: "Activity coefficients deviate from 1 when unlike-molecule (A-B) interactions differ from the average of like-molecule (A-A and B-B) interactions. In an ideal solution, all molecular interactions are equivalent, so the thermodynamic tendency to escape the solution depends only on mole fraction. In real solutions, if A-B interactions are weaker than the A-A/B-B average (e.g., mixing polar and nonpolar molecules), A molecules escape more readily than predicted — giving γ_A > 1 (positive deviation from Raoult's law). If A-B interactions are stronger (e.g., hydrogen bonding between unlike species), molecules are held in solution more strongly than in the pure liquid, giving γ_A < 1 (negative deviation). The magnitude of γ reflects how different the real mixture is from the ideal case."
  explanation: "This molecular-level picture connects directly to excess enthalpy: positive deviations correspond to ΔmixH > 0 (energy cost to mixing), while negative deviations correspond to ΔmixH < 0 (energy released on mixing). The excess Gibbs energy G^E parameterizes this departure and is the foundation of engineering models like Margules and Wilson equations used in distillation design."
```

## Explainer

When you studied pure-substance thermodynamics, every property — G, H, S, V — belonged to the whole system. In a mixture, you need to know how each component contributes to the total, and that contribution depends on what else is present. The **partial molar quantity** captures this: the partial molar Gibbs energy of component i, written (∂G/∂nᵢ) at constant T, P, and all other nⱼ, is the **chemical potential** μᵢ. It tells you how much the total Gibbs energy changes when you add an infinitesimal amount of component i to the mixture. Chemical potential governs everything — phase equilibrium requires equal μᵢ across phases, and reactions proceed in the direction that lowers total μ.

An **ideal solution** is the simplest model: every molecule interacts with its neighbors the same way regardless of identity. If ethanol and water formed an ideal solution, an ethanol molecule surrounded by water molecules would "feel" the same forces as one surrounded by other ethanol molecules. In this case, the chemical potential takes a clean logarithmic form: μᵢ = μᵢ* + RT ln(xᵢ), where xᵢ is the mole fraction and μᵢ* is the chemical potential of pure component i. This leads to Raoult's law for vapor pressures: Pᵢ = xᵢPᵢ*, and the thermodynamics of mixing are driven entirely by entropy — ΔmixH = 0 and ΔmixV = 0, with ΔmixG = RT Σ xᵢ ln(xᵢ), which is always negative because ln(xᵢ) < 0.

Real solutions deviate from this picture because molecular interactions are not symmetric. Ethanol-water, for example, shows negative deviations from Raoult's law — the vapor pressure is lower than predicted — because hydrogen bonding between ethanol and water is stronger than the average of ethanol-ethanol and water-water interactions. Other systems like acetone-carbon disulfide show positive deviations, where unlike molecules interact less favorably than like molecules. To handle this, we introduce the **activity coefficient** γᵢ, defining activity as aᵢ = γᵢxᵢ. When γᵢ = 1, the solution is ideal; γᵢ > 1 indicates positive deviations (molecules "want to escape" more than in an ideal solution), and γᵢ < 1 indicates negative deviations.

The **excess Gibbs energy** G^E = ΔmixG − ΔmixG(ideal) quantifies the total departure from ideality and is directly related to activity coefficients through ln(γᵢ) = (∂G^E/∂nᵢ)/RT. Models like the Margules equation (G^E = A·x₁·x₂ for a symmetric system) or the Wilson equation parameterize G^E as a function of composition, allowing you to predict activity coefficients, vapor-liquid equilibrium, and liquid-liquid phase separation from a small number of fitted parameters. This is the foundation of chemical engineering design: distillation columns, extraction processes, and crystallization all depend on knowing how far a real solution departs from ideality, and the framework of partial molar quantities and activity coefficients provides the rigorous language for quantifying those departures.
