---
id: gravimetric-analysis
title: Gravimetric Analysis
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: stoichiometry-calculations
  type: hard
- id: chemical-equilibrium
  type: soft
- id: sample-preparation
  type: soft
- id: measurement-uncertainty-budgeting
  type: soft
- id: quantitative-analysis-sample-preparation
  type: soft
builds-toward:
- titrimetric-analysis-intro
tags:
- gravimetry
- precipitation
- weighing
- primary standard
- solubility product
stage: formal-systems
status: validated
---
# Gravimetric Analysis

## Core Idea
Gravimetric analysis determines the quantity of an analyte by converting it to a sparingly soluble, stoichiometrically defined precipitate that is filtered, dried or ignited, and weighed. The gravimetric factor converts the mass of precipitate to the mass of analyte using molar mass ratios. For high accuracy, precipitates must be nearly insoluble (Ksp < 10⁻⁸), free of coprecipitation, large-grained (for efficient filtration), and of known, stable composition. Thermogravimetric analysis (TGA) extends gravimetry by continuously monitoring mass changes as a function of temperature.

## How It's Best Learned
Perform a classical determination such as sulfate by precipitation as BaSO₄ or chloride as AgCl. Carefully documenting each source of uncertainty — incomplete precipitation, precipitate solubility, filter retention — makes gravimetry an ideal vehicle for understanding systematic error.

## Common Misconceptions
- Coprecipitation (carrying down impurities) can cause either positive or negative errors depending on whether the impurity is heavier or lighter than the analyte ion displaced.
- Ignition temperature must be controlled: BaSO₄ can be reduced to BaS above 700°C in a reducing flame, giving a falsely low mass.

## Questions

```yaml
- question: "A chemist precipitates chloride ions as AgCl and weighs the dried precipitate. The result implies a sulfate content 8% higher than expected from an independent analysis. Which explanation best accounts for this positive error?"
  type: multiple-choice
  options:
    - "Ksp of AgCl was too high, so excess chloride remained in solution — a negative error source, not positive"
    - "Coprecipitation — foreign ions were adsorbed onto or occluded within the AgCl crystals, adding mass beyond the analyte's contribution"
    - "The gravimetric factor was applied upside down, inflating the calculated analyte mass"
    - "The precipitate was dried at too low a temperature, retaining water"
  answer: 1
  explanation: "Coprecipitation introduces foreign mass into the precipitate, directly causing positive errors — the precipitate weighs more than pure analyte-derived compound, so the calculated analyte is too high. This typically occurs when precipitation is rapid from concentrated solution, generating many tiny crystals with high surface area that trap impurities via adsorption or occlusion. The remedy is slow precipitation from hot, dilute solution to grow larger, purer crystals. Note: the question says 'sulfate content' — this is likely a mislabeled analyte in a real scenario; the error mechanism is coprecipitation regardless."

- question: "Why is gravimetric analysis used to establish primary standards, while UV-Vis spectrophotometry requires calibration curves?"
  type: multiple-choice
  options:
    - "Gravimetric instruments are more expensive and therefore more accurate"
    - "Gravimetry is more sensitive than spectrophotometric methods at low concentrations"
    - "Gravimetry measures mass — an absolute, fundamental SI unit — requiring no comparison to external standards at measurement time; spectrophotometry measures relative absorbance, which drifts and must be calibrated"
    - "Gravimetry works on more analyte types and is therefore more versatile"
  answer: 2
  explanation: "The power of gravimetry lies in using mass as its signal. Mass is traceable directly to fundamental SI units (the kilogram) without requiring instrument calibration or reference standards at the time of measurement. An analytical balance simply weighs; it does not need to be 'taught' what a known standard looks like. Spectrophotometry measures absorbance, which is an instrument response that depends on lamp intensity, detector sensitivity, and cell path length — all of which drift and must be corrected via calibration curves using known standards. This is why gravimetry establishes the primary standards against which spectrophotometric and other methods are validated."

- question: "Gravimetric accuracy requires that the Ksp of the precipitate be very small (typically below 10⁻⁸) to ensure nearly complete precipitation of the analyte."
  type: true-false
  answer: true
  explanation: "If Ksp is too large, a measurable quantity of the analyte remains dissolved in the supernatant rather than transferring to the precipitate — producing a negative error (precipitate weighs less than expected → calculated analyte is too low). For quantitative precipitation (≥99.9% capture), Ksp must be very small. Adding excess precipitating reagent exploits the common ion effect to further suppress solubility, driving precipitation toward completion."

- question: "Coprecipitation generally causes a positive error in gravimetric analysis, making the calculated analyte mass too high."
  type: true-false
  answer: false
  explanation: "Coprecipitation can cause either positive or negative errors, depending on the nature of the contaminant. If foreign ions are simply adsorbed onto the precipitate surface (adding extra mass) or occluded within the lattice, the result is a positive error. But if the coprecipitated impurity replaces analyte ions with lighter species in the crystal structure, the precipitate may weigh less per mole of analyte than expected, producing a negative error. The direction depends on the chemical identity and mass of the contaminating species relative to the analyte ion."

- question: "Why is slow precipitation from hot, dilute solution preferred in gravimetric analysis, even though it is more time-consuming than rapid precipitation?"
  type: short-answer
  answer: "Slow precipitation from hot, dilute solution produces fewer nuclei and allows existing crystals to grow large. Large crystals have proportionally less surface area than many small ones, which reduces coprecipitation (fewer sites for impurity adsorption) and makes filtration more efficient (less loss through filter paper). The von Weimarn ratio shows that high supersaturation — from rapid mixing of concentrated solutions — nucleates a burst of tiny crystallites with enormous surface area that readily trap impurities. Heat also increases solubility temporarily, reducing supersaturation and further favoring crystal growth over nucleation."
  explanation: "In practice: after adding the precipitating reagent, the solution is digested (kept warm for 30–60 minutes) to allow small crystals to dissolve and redeposit on larger ones — Ostwald ripening. The result is a coarser, purer precipitate that filters cleanly and gives more accurate results."
```

## Explainer

Gravimetric analysis is one of the oldest and most conceptually transparent quantitative methods in chemistry. The core logic is straightforward: if you can convert your analyte into a pure, insoluble compound of known formula, then the mass of that compound tells you exactly how much analyte was in the original sample. From your study of stoichiometry, you already have the tools to make this calculation. The **gravimetric factor** is simply the ratio of the molar mass of the analyte to the molar mass of the precipitate, multiplied by appropriate stoichiometric coefficients. For example, if you precipitate sulfate as BaSO₄, the gravimetric factor for SO₄²⁻ is M(SO₄²⁻)/M(BaSO₄) = 96.06/233.39 = 0.4116. Multiply the mass of dried BaSO₄ by this factor and you have the mass of sulfate in your sample.

The beauty of gravimetric analysis is that it requires no calibration curve and no instrument calibration — the analytical balance is your detector, and mass is a fundamental, absolute measurement. This is why gravimetry is used to establish the composition of **primary standards**, the reference materials against which all other methods are ultimately calibrated. However, achieving this accuracy demands careful control of the precipitation process. From your knowledge of chemical equilibrium, you understand that a precipitate's solubility depends on the equilibrium constant Ksp. For gravimetry to work, Ksp must be extremely small (typically below 10⁻⁸) so that virtually all of the analyte is captured in the solid phase. Even then, quantitative precipitation requires adding excess reagent and often adjusting pH or temperature to suppress solubility further.

The practical challenge lies in producing a precipitate that is **pure, filterable, and of known composition**. Rapid precipitation from concentrated solutions produces tiny crystallites with enormous surface area, which trap impurities through **coprecipitation** — adsorption of foreign ions on the crystal surface or occlusion of mother liquor within the crystal lattice. The remedy is to precipitate slowly from hot, dilute solution, allowing large crystals to grow (a process guided by the von Weimarn ratio: low supersaturation favors fewer, larger crystals). After filtration, the precipitate is washed to remove adsorbed impurities, then dried or ignited to convert it to a stable weighing form. The ignition step drives off water and any volatile contaminants, but the temperature must be carefully controlled — too low and the precipitate retains moisture, too high and it may decompose or react with the crucible.

Understanding measurement uncertainty is essential to interpreting gravimetric results. Every step introduces potential error: incomplete precipitation leaves analyte in solution (negative error), coprecipitation adds foreign mass (positive error), loss of precipitate during transfer reduces the final weight, and moisture absorption during weighing inflates it. A well-executed gravimetric determination accounts for each of these by using replicate analyses, reagent blanks, and uncertainty budgets. Despite these demands, gravimetry remains the method of choice whenever absolute accuracy matters more than speed — in standardizing reference materials, verifying the composition of alloys, and in any situation where traceability to fundamental SI units (the kilogram) is required.
