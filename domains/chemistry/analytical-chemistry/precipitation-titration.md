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
stage: formal-systems
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

## Questions

```yaml
- question: "You need to determine the chloride concentration in a strongly acidic industrial waste sample. Which argentometric method is most appropriate, and why?"
  type: multiple-choice
  options:
    - "Mohr method, because chromate indicator gives the clearest color change for chloride"
    - "Fajans method, because adsorption indicators are completely unaffected by solution pH"
    - "Volhard method, because it uses a back-titration in acidic solution, where the Mohr method's chromate indicator would decompose or fail to precipitate correctly"
    - "All three methods are equally applicable; pH does not affect argentometric titrations"
  answer: 2
  explanation: "The Mohr method requires neutral pH (approximately 6.5–10). In acidic solution, chromate exists as dichromate (CrO₄²⁻ is protonated to give HCrO₄⁻/Cr₂O₇²⁻), which has a different Ksp relationship with Ag⁺ — making the endpoint unreliable. In basic conditions, Ag⁺ precipitates as Ag₂O before the endpoint. The Volhard method avoids this: it is performed in acidic solution (0.1–0.5 M HNO₃), where the ferric thiocyanate indicator is stable and the excess silver can be properly back-titrated. This pH constraint is one of the most important practical considerations in method selection."

- question: "Two argentometric titrations are performed — one determining iodide (AgI, Ksp ≈ 10⁻¹⁶) and one determining chloride (AgCl, Ksp ≈ 10⁻¹⁰). At the equivalence point, what difference should be expected?"
  type: multiple-choice
  options:
    - "The AgCl titration will have a sharper equivalence point because chloride is more commonly determined by this method"
    - "Both titrations will have identical equivalence point sharpness because both reactions have 1:1 stoichiometry with Ag⁺"
    - "The AgI titration will have a sharper equivalence point because the smaller Ksp produces a steeper change in Ag⁺ concentration at the equivalence point"
    - "The AgI titration will have a broader equivalence point because iodide binds more tightly and slows the precipitation kinetics"
  answer: 2
  explanation: "Ksp directly determines endpoint sharpness. A smaller Ksp means the precipitation equilibrium lies further toward complete reaction — as the last analyte ions are consumed, the free Ag⁺ concentration spikes steeply over a tiny volume range. Plotting pAg versus volume of titrant, the inflection at the equivalence point is much steeper for AgI than for AgCl. This is why iodide determinations can achieve better precision than chloride determinations by argentometry, all else equal. The 1:1 stoichiometry is the same in both cases — the difference is entirely in the thermodynamics of precipitation."

- question: "In the Mohr method, the chromate indicator precipitates as Ag₂CrO₄ only after virtually all the chloride has been consumed, because AgCl has a lower Ksp than Ag₂CrO₄."
  type: true-false
  answer: true
  explanation: "This sequential precipitation is the entire mechanism of the Mohr endpoint. AgCl (Ksp ≈ 10⁻¹⁰) precipitates preferentially over Ag₂CrO₄ (Ksp ≈ 10⁻¹²·⁵ for the 2:1 stoichiometry, but with the concentration of chromate used in practice, the effective Ksp comparison favors AgCl first). Throughout the titration, Ag⁺ is consumed by the more soluble halide. Only after the halide is essentially exhausted does [Ag⁺] rise high enough to exceed the ion product for Ag₂CrO₄, producing the brick-red precipitate that signals the endpoint. The relative Ksp values are what guarantee correct sequencing."

- question: "In the Volhard back-titration, after adding excess AgNO₃ to a chloride sample, you can immediately back-titrate the excess with thiocyanate without any additional treatment."
  type: true-false
  answer: false
  explanation: "This is the classic Volhard method mistake. AgCl must be filtered off (or the precipitate must be coated with nitrobenzene) before the back-titration with thiocyanate. If AgCl is present when thiocyanate is added, the following reaction occurs: AgCl(s) + SCN⁻ → AgSCN(s) + Cl⁻. Since AgSCN (Ksp ≈ 10⁻¹²) is less soluble than AgCl (Ksp ≈ 10⁻¹⁰), the thiocyanate converts AgCl into AgSCN, consuming additional titrant beyond the excess Ag⁺. This produces a falsely high result for the excess silver and therefore a falsely low result for the original chloride concentration."

- question: "Explain how the Ksp of a silver salt determines the sharpness of the equivalence point in a precipitation titration, and what practical consequence this has for analytical precision."
  type: short-answer
  answer: "Ksp sets how completely the precipitation reaction proceeds at the equivalence point. A smaller Ksp means the reaction goes more completely to completion as the analyte is consumed — at the equivalence point, the small remaining analyte concentration forces a steep, large change in the silver ion concentration over a tiny added volume. This steep inflection in the pAg titration curve makes the endpoint sharp and easy to detect reliably. A larger Ksp means the transition is gradual, spread over a larger volume range, making precise endpoint detection more difficult. Consequently, analytes forming less soluble silver salts (e.g., iodide vs. chloride) yield inherently more precise argentometric determinations."
  explanation: "This question connects the equilibrium chemistry (Ksp) to the practical analytical outcome (endpoint sharpness and precision). The same principle applies throughout titrimetric analysis: the completeness of the reaction at the equivalence point determines how sharp the endpoint is, which determines how precisely the analyst can identify it. Understanding Ksp not just as a solubility concept but as a predictor of analytical performance is the key insight that makes precipitation titrations a coherent topic rather than a collection of disconnected methods."
```

## Explainer

From your study of titrimetric analysis, you understand that a titration works when a reagent reacts with an analyte in a known stoichiometric ratio and the endpoint can be detected reliably. Precipitation titrations apply this principle to reactions that produce an insoluble solid — the most important being the reaction of silver nitrate (AgNO₃) with halide ions to form insoluble silver halides. When you add Ag⁺ to a solution containing Cl⁻, the sparingly soluble salt AgCl precipitates out until all the chloride is consumed. The stoichiometry is a clean 1:1 ratio, and the equilibrium is governed by the **solubility product constant (Ksp)** you studied in chemical equilibrium.

The sharpness of the endpoint depends directly on the Ksp. A smaller Ksp means the precipitation reaction goes more completely to completion, producing a steeper change in ion concentration at the equivalence point. AgI (Ksp ≈ 10⁻¹⁶) gives a sharper endpoint than AgCl (Ksp ≈ 10⁻¹⁰), which in turn is sharper than AgBrO₃. You can visualize this by plotting **pAg** (the negative log of silver ion concentration) versus volume of titrant added — the curve looks just like a pH titration curve, with a steep inflection at the equivalence point. The steeper that inflection, the easier it is to detect the endpoint and the more precise the determination.

The three classical endpoint detection methods each solve the detection problem differently. The **Mohr method** adds a small amount of chromate (CrO₄²⁻) indicator to the analyte solution. Throughout the titration, AgCl precipitates preferentially because it is less soluble than Ag₂CrO₄. Only after essentially all the chloride is consumed does the silver concentration rise enough to exceed the Ksp of Ag₂CrO₄, forming a visible brick-red precipitate that signals the endpoint. The method requires neutral pH because acid dissolves the chromate indicator precipitate and base precipitates silver as Ag₂O. The **Volhard method** takes a back-titration approach: add excess Ag⁺ to the sample, then titrate the unreacted silver with thiocyanate (SCN⁻) using ferric ion as an indicator. When excess SCN⁻ appears, it forms the blood-red FeSCN²⁺ complex. Because this works in acidic solution, it succeeds where Mohr cannot. The **Fajans method** uses adsorption indicators (like fluorescein) that change color when they adsorb onto the precipitate surface — a fundamentally different detection mechanism based on surface chemistry rather than bulk precipitation.

The practical importance of precipitation titrations extends well beyond the teaching lab. Chloride determination by argentometric methods is a standard analysis in water treatment, food science (salt content), and clinical chemistry (electrolyte analysis). Understanding which method to choose — Mohr for direct titration in neutral solution, Volhard for acidic conditions or indirect determination of anions that form soluble silver salts, Fajans for dilute solutions where the precipitate surface area is large — connects the underlying chemistry of solubility equilibria to real analytical decision-making.
