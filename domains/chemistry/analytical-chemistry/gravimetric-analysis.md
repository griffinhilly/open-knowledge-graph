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
builds-toward:
- titrimetric-analysis-intro
tags:
- gravimetry
- precipitation
- weighing
- primary standard
- solubility product
stage: advanced
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

## Explainer

Gravimetric analysis is one of the oldest and most conceptually transparent quantitative methods in chemistry. The core logic is straightforward: if you can convert your analyte into a pure, insoluble compound of known formula, then the mass of that compound tells you exactly how much analyte was in the original sample. From your study of stoichiometry, you already have the tools to make this calculation. The **gravimetric factor** is simply the ratio of the molar mass of the analyte to the molar mass of the precipitate, multiplied by appropriate stoichiometric coefficients. For example, if you precipitate sulfate as BaSO₄, the gravimetric factor for SO₄²⁻ is M(SO₄²⁻)/M(BaSO₄) = 96.06/233.39 = 0.4116. Multiply the mass of dried BaSO₄ by this factor and you have the mass of sulfate in your sample.

The beauty of gravimetric analysis is that it requires no calibration curve and no instrument calibration — the analytical balance is your detector, and mass is a fundamental, absolute measurement. This is why gravimetry is used to establish the composition of **primary standards**, the reference materials against which all other methods are ultimately calibrated. However, achieving this accuracy demands careful control of the precipitation process. From your knowledge of chemical equilibrium, you understand that a precipitate's solubility depends on the equilibrium constant Ksp. For gravimetry to work, Ksp must be extremely small (typically below 10⁻⁸) so that virtually all of the analyte is captured in the solid phase. Even then, quantitative precipitation requires adding excess reagent and often adjusting pH or temperature to suppress solubility further.

The practical challenge lies in producing a precipitate that is **pure, filterable, and of known composition**. Rapid precipitation from concentrated solutions produces tiny crystallites with enormous surface area, which trap impurities through **coprecipitation** — adsorption of foreign ions on the crystal surface or occlusion of mother liquor within the crystal lattice. The remedy is to precipitate slowly from hot, dilute solution, allowing large crystals to grow (a process guided by the von Weimarn ratio: low supersaturation favors fewer, larger crystals). After filtration, the precipitate is washed to remove adsorbed impurities, then dried or ignited to convert it to a stable weighing form. The ignition step drives off water and any volatile contaminants, but the temperature must be carefully controlled — too low and the precipitate retains moisture, too high and it may decompose or react with the crucible.

Understanding measurement uncertainty is essential to interpreting gravimetric results. Every step introduces potential error: incomplete precipitation leaves analyte in solution (negative error), coprecipitation adds foreign mass (positive error), loss of precipitate during transfer reduces the final weight, and moisture absorption during weighing inflates it. A well-executed gravimetric determination accounts for each of these by using replicate analyses, reagent blanks, and uncertainty budgets. Despite these demands, gravimetry remains the method of choice whenever absolute accuracy matters more than speed — in standardizing reference materials, verifying the composition of alloys, and in any situation where traceability to fundamental SI units (the kilogram) is required.
