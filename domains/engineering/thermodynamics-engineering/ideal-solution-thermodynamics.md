---
id: ideal-solution-thermodynamics
title: Ideal and Non-ideal Solution Behavior
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: partial-molar-properties-solutions
  type: hard
- id: chemical-equilibrium-reaction-analysis
  type: soft
builds-toward:
- gibbs-phase-rule-multicomponent
tags:
- ideal-solution
- raoults-law
- activity-coefficient
- non-ideal
- mixing
stage: formal-systems
status: draft
---

# Ideal and Non-ideal Solution Behavior

## Core Idea
Ideal solutions follow Raoult's law and require no heat of mixing. Real solutions exhibit deviations quantified by activity coefficients γᵢ; fugacity f̄ᵢ = γᵢ xᵢ fᵢ replaces partial pressure. Common models (Wilson, NRTL, UNIQUAC) predict liquid-liquid and vapor-liquid equilibrium based on component interactions, critical for distillation and extraction design.

## Questions

```yaml
- question: "An engineer attempts to purify ethanol from a water-ethanol mixture through repeated distillation. After many stages, the distillate stabilizes at 95.6 mol% ethanol and cannot be made purer regardless of how many additional stages are added. Why?"
  type: multiple-choice
  options:
    - "A minimum-boiling azeotrope exists at this composition: the vapor and liquid phases have identical compositions, so distillation produces no further enrichment — the driving force for separation disappears"
    - "Ethanol and water form an ideal solution at high ethanol concentrations, so Raoult's law applies exactly and there is no vapor pressure difference to exploit"
    - "The boiling point of the mixture rises to match pure water's boiling point at this composition, halting further distillation"
    - "The activity coefficients approach zero at high ethanol concentrations, eliminating the fugacity difference between phases"
  answer: 0
  explanation: "The ethanol-water system shows positive deviation from Raoult's law — A-B (ethanol-water) interactions are weaker than A-A and B-B interactions, so the mixture has higher vapor pressure than Raoult's law predicts. This positive deviation creates a maximum in the total vapor pressure curve, which corresponds to a minimum-boiling azeotrope at 95.6 mol% ethanol, 78.1°C at 1 atm. At the azeotrope, vapor and liquid compositions are identical; evaporating the liquid produces vapor of the same composition. No amount of additional distillation stages can move past this composition. Absolute (100%) ethanol requires a different process such as molecular sieves or azeotropic distillation with a third component."

- question: "Two liquid species A and B have weaker A-B intermolecular interactions than either A-A or B-B interactions. What does this imply for their solution behavior?"
  type: multiple-choice
  options:
    - "Positive deviation from Raoult's law (γᵢ > 1): molecules 'prefer' like neighbors and escape into the vapor more readily than Raoult's law predicts, raising vapor pressure above the ideal prediction"
    - "Negative deviation from Raoult's law (γᵢ < 1): weaker cross-interactions mean the mixture is less stable, so vapor pressure is lower than ideal"
    - "Ideal solution behavior (γᵢ = 1): differences in intermolecular forces only matter for the enthalpy of mixing, not for vapor pressure"
    - "A maximum-boiling azeotrope: weaker cross-interactions cause the mixture to boil at a higher temperature than either pure component"
  answer: 0
  explanation: "When A-B interactions are weaker than A-A or B-B, each molecule is less 'held' by its neighbors in solution than it would be in the pure liquid. Molecules escape into the vapor more easily, raising the partial pressure of each component above the xᵢPᵢˢᵃᵗ prediction of Raoult's law. Activity coefficients γᵢ > 1 quantify this excess tendency to vaporize. The ethanol-acetone system is a classic example. Negative deviation (option B) results from the opposite: unusually strong cross-interactions (e.g., hydrogen bonding between unlike molecules) that make the liquid more stable and reduce vapor pressure below Raoult's law."

- question: "For an ideal solution, the activity coefficient γᵢ equals 1 for all components, and the enthalpy of mixing is zero."
  type: true-false
  answer: true
  explanation: "An ideal solution is defined by the condition that all intermolecular interactions are equal (A-A = B-B = A-B). This means mixing is a purely entropic process: ΔH_mix = 0 and ΔV_mix = 0. With no energetic preference for any neighbor, the tendency of each component to vaporize is proportional only to its mole fraction, giving pᵢ = xᵢPᵢˢᵃᵗ (Raoult's law) and γᵢ = 1. Activity coefficients are 1 for all compositions and all components simultaneously. Ideal behavior is a reasonable approximation for chemically very similar species, such as benzene-toluene or isotopic mixtures."

- question: "A maximum-boiling azeotrope, such as the HCl-water system, arises from positive deviation from Raoult's law."
  type: true-false
  answer: false
  explanation: "Maximum-boiling azeotropes arise from negative deviation (γᵢ < 1), caused by unusually strong cross-species interactions. Stronger A-B attraction relative to A-A and B-B holds molecules in the liquid phase more tightly, reducing vapor pressure below the Raoult's law prediction. The vapor pressure curve shows a minimum at the azeotrope composition, corresponding to a maximum in boiling point — the mixture is hardest to vaporize at that composition. Positive deviation creates a vapor pressure maximum (minimum-boiling azeotrope). The HCl-water system has strong HCl-H₂O hydrogen bonding interactions, producing negative deviation and a maximum-boiling azeotrope at ~20% HCl."

- question: "Why is an azeotrope a fundamental limitation for distillation engineers, and what does its existence reveal about the thermodynamics of the liquid mixture?"
  type: short-answer
  answer: "Distillation relies on the vapor phase being richer in the more volatile component than the liquid phase — this composition difference is what each stage exploits. At an azeotrope, the vapor and liquid have identical compositions: K_i = yᵢ/xᵢ = 1 for all components. Evaporating the liquid produces vapor of the same composition, so no separation occurs regardless of the number of stages or reflux ratio. This is a thermodynamic limit, not an engineering one. The azeotrope's existence reveals that activity coefficients are non-unity: the liquid mixture has strong molecular interactions (positive or negative deviation) that cause the total vapor pressure curve to have a local extremum. At that extremum, the Gibbs-Duhem equation constrains the partial pressures to converge to equal compositions in both phases."
  explanation: "Engineers bypass azeotropes by pressure-swing distillation (azeotrope composition shifts with pressure if the components' vapor pressures have different pressure dependencies), extractive distillation (adding a third solvent that breaks the azeotrope), or entirely different separation technologies. The ethanol-water azeotrope is why fuel-grade ethanol (denatured, ~96%) is cheap but absolute ethanol is expensive."
```

## Explainer

From partial molar properties, you know that the chemical potential of component i in a mixture is μᵢ = μᵢ° + RT ln(aᵢ), where aᵢ is the **activity** — a dimensionless measure of how "active" the component is compared to a reference state. The key question is how activity relates to composition. The answer depends on whether the solution is ideal.

An **ideal solution** is one where every molecule experiences the same intermolecular forces regardless of its neighbors. This means mixing is purely entropic — there is no enthalpy of mixing (ΔH_mix = 0) and the volume doesn't change on mixing (ΔV_mix = 0). Under these conditions, **Raoult's law** holds: the partial pressure of component i above the solution equals its mole fraction times its pure-component saturation pressure, pᵢ = xᵢ Pᵢˢᵃᵗ. Activity coefficients γᵢ are all equal to 1. Ideal behavior is a reasonable approximation for mixtures of chemically similar species (e.g., benzene + toluene, or isotopes), but most engineering systems deviate significantly.

Real solutions have **non-unity activity coefficients**. If molecules of different species repel each other more than like molecules do (weaker cross-interactions), the vapor pressure exceeds the Raoult's law prediction — a **positive deviation** (γᵢ > 1). The liquid molecules prefer to escape into the vapor. If cross-interactions are stronger than like-interactions (e.g., hydrogen bonding between different species), vapor pressures fall below Raoult's law — **negative deviation** (γᵢ < 1). The activity coefficient captures this departure: the fugacity in the liquid phase is f̄ᵢ = γᵢ xᵢ fᵢ, where fᵢ is the pure-component fugacity.

The engineering consequences are large. **Azeotropes** occur when the vapor and liquid compositions become equal — no further separation is possible by simple distillation. For a positive-deviation binary mixture, the total vapor pressure has a maximum above what Raoult's law predicts; at that composition, the mixture boils at a temperature lower than either pure component (**minimum-boiling azeotrope**). The ethanol-water system at 95.6 mol% ethanol (78.1°C at 1 atm) is the canonical example — this is why absolute alcohol cannot be made by distillation alone. Negative-deviation systems form **maximum-boiling azeotropes** (the HCl-water azeotrope at 20.2% HCl, 108.6°C). Activity coefficient models like Wilson, NRTL, and UNIQUAC fit experimental phase equilibrium data and extrapolate to other conditions, making them the workhorses of distillation design software.
