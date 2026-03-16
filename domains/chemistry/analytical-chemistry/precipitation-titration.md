---
id: precipitation-titration
title: Precipitation Titrations (Argentometric Methods)
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: titrimetric-analysis-intro
  type: hard
- id: chemical-equilibrium
  type: soft
tags:
- argentometry
- Mohr method
- Volhard method
- Fajans method
- Ksp
- halide
stage: advanced
status: validated
---

# Precipitation Titrations (Argentometric Methods)

## Core Idea
Precipitation titrations exploit sparingly soluble salt formation; argentometric methods using AgNO₃ as titrant are the most common application, determining halide ions (Cl⁻, Br⁻, I⁻, SCN⁻). Three classical endpoint techniques exist: the Mohr method (chromate indicator, direct titration of Cl⁻ at neutral pH), the Volhard method (thiocyanate back-titration in acidic solution, suitable for all halides), and the Fajans method (adsorption indicators such as fluorescein that change color upon adsorption to the precipitate surface). Selectivity depends on differences in Ksp values among silver halides.

## How It's Best Learned
Determine chloride in seawater or a pharmaceutical tablet by both Mohr and Volhard methods, then compare precision. Constructing a theoretical pCl titration curve and identifying the equivalence point sharpness for different Ksp values reinforces quantitative treatment.

## Common Misconceptions
- The Mohr method requires neutral pH: acidic conditions dissolve Ag₂CrO₄ (false endpoint), and basic conditions precipitate Ag₂O.
- In the Volhard method, AgCl must be filtered before back-titrating with thiocyanate to prevent conversion of AgCl to AgSCN.

## Explainer

From your study of titrimetric analysis, you understand that a titration works when a reagent reacts with an analyte in a known stoichiometric ratio and the endpoint can be detected reliably. Precipitation titrations apply this principle to reactions that produce an insoluble solid — the most important being the reaction of silver nitrate (AgNO₃) with halide ions to form insoluble silver halides. When you add Ag⁺ to a solution containing Cl⁻, the sparingly soluble salt AgCl precipitates out until all the chloride is consumed. The stoichiometry is a clean 1:1 ratio, and the equilibrium is governed by the **solubility product constant (Ksp)** you studied in chemical equilibrium.

The sharpness of the endpoint depends directly on the Ksp. A smaller Ksp means the precipitation reaction goes more completely to completion, producing a steeper change in ion concentration at the equivalence point. AgI (Ksp ≈ 10⁻¹⁶) gives a sharper endpoint than AgCl (Ksp ≈ 10⁻¹⁰), which in turn is sharper than AgBrO₃. You can visualize this by plotting **pAg** (the negative log of silver ion concentration) versus volume of titrant added — the curve looks just like a pH titration curve, with a steep inflection at the equivalence point. The steeper that inflection, the easier it is to detect the endpoint and the more precise the determination.

The three classical endpoint detection methods each solve the detection problem differently. The **Mohr method** adds a small amount of chromate (CrO₄²⁻) indicator to the analyte solution. Throughout the titration, AgCl precipitates preferentially because it is less soluble than Ag₂CrO₄. Only after essentially all the chloride is consumed does the silver concentration rise enough to exceed the Ksp of Ag₂CrO₄, forming a visible brick-red precipitate that signals the endpoint. The method requires neutral pH because acid dissolves the chromate indicator precipitate and base precipitates silver as Ag₂O. The **Volhard method** takes a back-titration approach: add excess Ag⁺ to the sample, then titrate the unreacted silver with thiocyanate (SCN⁻) using ferric ion as an indicator. When excess SCN⁻ appears, it forms the blood-red FeSCN²⁺ complex. Because this works in acidic solution, it succeeds where Mohr cannot. The **Fajans method** uses adsorption indicators (like fluorescein) that change color when they adsorb onto the precipitate surface — a fundamentally different detection mechanism based on surface chemistry rather than bulk precipitation.

The practical importance of precipitation titrations extends well beyond the teaching lab. Chloride determination by argentometric methods is a standard analysis in water treatment, food science (salt content), and clinical chemistry (electrolyte analysis). Understanding which method to choose — Mohr for direct titration in neutral solution, Volhard for acidic conditions or indirect determination of anions that form soluble silver salts, Fajans for dilute solutions where the precipitate surface area is large — connects the underlying chemistry of solubility equilibria to real analytical decision-making.
