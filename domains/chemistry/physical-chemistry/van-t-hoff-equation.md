---
id: van-t-hoff-equation
title: "The van't Hoff Equation: Temperature Dependence of Equilibrium"
domain: chemistry
course: physical-chemistry
prerequisites:
- id: statistical-thermodynamics-applications
  type: hard
builds-toward: []
tags:
- van-t-Hoff
- equilibrium-constant
- temperature-dependence
- Le-Chatelier
- enthalpy-of-reaction
- thermodynamic-equilibrium
stage: formal-systems
status: validated
---

# The van't Hoff Equation: Temperature Dependence of Equilibrium

## Core Idea
The van't Hoff equation d(ln K)/dT = Delta_H_std/(R*T^2) quantifies how the equilibrium constant K changes with temperature, providing the quantitative foundation for Le Chatelier's principle. For an endothermic reaction (Delta_H > 0), K increases with temperature; for exothermic (Delta_H < 0), K decreases. The integrated form ln(K2/K1) = -(Delta_H/R)(1/T2 - 1/T1) assumes Delta_H is approximately constant over the temperature range and enables prediction of K at any temperature from a single measured value. A van't Hoff plot of ln K vs 1/T yields a straight line with slope -Delta_H/R when enthalpy is temperature-independent; curvature indicates significant Delta_Cp, requiring the Kirchhoff equation correction. This relationship connects macroscopic equilibrium measurements directly to molecular-level energetics.

## How It's Best Learned
Collect or look up equilibrium constant data for a reaction at multiple temperatures (e.g., the dissociation of N2O4 or the solubility of a sparingly soluble salt). Construct the van't Hoff plot, extract Delta_H from the slope, and verify consistency with calorimetric measurements.

## Common Misconceptions
- Assuming Delta_H is always temperature-independent; for reactions with large Delta_Cp (heat capacity changes), the van't Hoff plot curves and the simple two-point integrated form becomes inaccurate.
- Confusing the van't Hoff equation with the Arrhenius equation; the former relates K (equilibrium) to temperature while the latter relates k (rate constant) to temperature -- they have similar mathematical forms but describe fundamentally different quantities.

## Questions

```yaml
- question: "A reaction is exothermic with ΔH° = –50 kJ/mol. A chemist increases the temperature of the system at equilibrium. According to the van't Hoff equation, what happens to K?"
  type: multiple-choice
  options:
    - "K increases, because higher temperature always drives reactions forward"
    - "K decreases, because higher temperature favors the endothermic (reverse) direction, shifting equilibrium toward reactants"
    - "K stays constant, because K is a thermodynamic quantity independent of temperature"
    - "K increases, because exothermic reactions release more heat at higher temperatures"
  answer: 1
  explanation: "For an exothermic reaction (ΔH° < 0), d(ln K)/dT < 0 — K decreases as temperature rises. Higher temperature favors the endothermic (reverse) direction. This is the quantitative foundation of Le Chatelier's principle: adding heat shifts an exothermic equilibrium toward reactants. Option A reflects the common misconception that temperature always drives forward reactions; in fact, temperature drives equilibrium toward the endothermic direction."

- question: "Using the integrated van't Hoff equation, a researcher finds K₂/K₁ > 1 when T₂ > T₁. What can they conclude about the reaction?"
  type: multiple-choice
  options:
    - "The reaction is exothermic, because K increased with temperature"
    - "The reaction is endothermic, because K increased with temperature"
    - "The reaction has ΔH° = 0, because K always increases with temperature"
    - "The reaction is spontaneous, because K > 1 indicates products are favored"
  answer: 1
  explanation: "From the integrated form ln(K₂/K₁) = –(ΔH°/R)(1/T₂ – 1/T₁): if T₂ > T₁, then (1/T₂ – 1/T₁) is negative. For ln(K₂/K₁) to be positive (K increasing), we need ΔH° > 0 — the reaction must be endothermic. Endothermic reactions have K that increases with temperature because higher temperature provides energy to drive the thermodynamically uphill forward reaction."

- question: "A van't Hoff plot of ln K vs 1/T is curved rather than linear. This indicates that the reaction's enthalpy of reaction is zero."
  type: true-false
  answer: false
  explanation: "Curvature in a van't Hoff plot indicates that ΔH° is not constant over the temperature range — not that it is zero. Curvature arises when the heat capacities of products and reactants differ significantly (large ΔCp), so ΔH° itself changes with temperature. A zero ΔH° would produce a horizontal line (slope = 0), not a curved one. Significant curvature signals that the Kirchhoff equation correction is needed."

- question: "The van't Hoff equation and the Arrhenius equation look similar mathematically because they describe the same physical phenomenon."
  type: true-false
  answer: false
  explanation: "They look similar (both have RT in the denominator) but describe fundamentally different quantities. Van't Hoff governs K, the equilibrium constant — a thermodynamic quantity telling you where equilibrium lies. Arrhenius governs k, the rate constant — a kinetic quantity telling you how fast a reaction proceeds. A reaction can have large K (thermodynamically favorable) but tiny k (kinetically slow), or vice versa. These are completely independent."

- question: "Why does the van't Hoff equation contain ΔH° rather than ΔG°, even though ΔG° directly determines K?"
  type: short-answer
  answer: "ΔG° = ΔH° – TΔS°, so ΔG° already contains temperature explicitly. When you differentiate ΔG°/T with respect to T (via the Gibbs-Helmholtz equation), the TΔS° term cancels, leaving only ΔH°/T². This is why ΔH° — not ΔG° — controls how K changes with temperature. ΔG° tells you the equilibrium position at one temperature; ΔH° tells you how that position shifts as temperature changes."
  explanation: "This is a mathematically elegant result: the temperature sensitivity of K depends only on the reaction enthalpy, not the full Gibbs energy. It means you can predict K at any temperature using only calorimetric data (ΔH°), without needing the entropy contribution at every temperature."
```

## Explainer

From statistical thermodynamics, you know that the equilibrium constant K is related to the standard Gibbs energy change by ΔG° = −RT ln K. This relationship tells you *where* equilibrium lies at a given temperature, but it does not tell you what happens when you change the temperature. The **van't Hoff equation** fills that gap. By differentiating the Gibbs-temperature relationship with respect to T and applying the Gibbs-Helmholtz equation, you arrive at d(ln K)/dT = ΔH°/(RT²). This elegant result says that the rate at which the equilibrium constant changes with temperature depends on the enthalpy of reaction — and nothing else (assuming ΔH° is roughly constant).

The intuition is thermodynamic. For an **endothermic reaction** (ΔH° > 0), the products are energetically uphill. Raising the temperature provides more thermal energy to climb that hill, so the equilibrium shifts toward products — K increases. For an **exothermic reaction** (ΔH° < 0), the products are energetically downhill, and raising the temperature makes the reverse (endothermic) direction more favorable — K decreases. This is exactly Le Chatelier's principle, but now you have a quantitative equation rather than a qualitative rule. You can calculate *how much* K changes for a given temperature change, not just the direction.

The **integrated form** ln(K₂/K₁) = −(ΔH°/R)(1/T₂ − 1/T₁) is what you will use most often in practice. Given K at one temperature and the enthalpy of reaction, you can predict K at any other temperature. The key assumption is that ΔH° does not change significantly over the temperature range — a reasonable approximation for modest intervals but one that breaks down over hundreds of degrees. When you plot ln K versus 1/T (a **van't Hoff plot**), a straight line confirms that ΔH° is effectively constant, and the slope equals −ΔH°/R. Curvature in the plot signals that the heat capacities of products and reactants differ appreciably, requiring the Kirchhoff equation to account for how ΔH° itself varies with temperature.

A common source of confusion is the superficial resemblance to the **Arrhenius equation**, ln k = −Eₐ/(RT) + constant, which looks almost identical. But these equations describe fundamentally different quantities: van't Hoff governs K (the equilibrium constant — a thermodynamic quantity reflecting the ratio of product to reactant concentrations at equilibrium), while Arrhenius governs k (the rate constant — a kinetic quantity reflecting how fast a reaction proceeds). A reaction can have a large K (thermodynamically favorable) but a tiny k (kinetically slow), or vice versa. The van't Hoff equation tells you nothing about reaction speed; it tells you only about the final balance between forward and reverse reactions once the system has had time to reach equilibrium.
