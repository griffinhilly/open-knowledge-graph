---
id: age-structured-demographics-and-fecundity
title: Age-Structured Demography and Fecundity
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-age-structure-life-history
  type: hard
- id: population-growth-models
  type: soft
builds-toward:
- source-sink-population-models
- population-viability-analysis
tags:
- demography
- age-structure
- population
- fecundity
stage: advanced
status: draft
---

# Age-Structured Demography and Fecundity

## Core Idea
Population growth depends on age-specific survival and fecundity rates, not just total reproduction. Life tables encode these vital rates; Leslie matrix models show how populations change when different age classes have different survival and reproduction. Population growth rate (lambda) emerges from vital rates; small changes in reproductive-age survival often have larger effects than changes to pre-reproductive individuals.

## Explainer

From your study of population age structure and life history, you know that not all individuals in a population are equivalent — they differ in age, size, and reproductive status. Age-structured demography formalizes this insight by tracking survival and reproduction as functions of age, revealing why identical-sized populations can have very different futures depending on their age composition.

The foundation of this approach is the **life table**, a schedule that records age-specific survival probability (l_x, the chance of surviving from birth to age x) and age-specific fecundity (m_x, the average number of offspring produced at age x). Together, these columns capture everything you need to project a population's trajectory. For example, a population of sea turtles where most individuals are juveniles that won't reproduce for decades will grow very differently from one dominated by reproductive adults — even if the total count is the same. The life table makes this distinction explicit.

To model how age-structured populations change over time, ecologists use the **Leslie matrix**, a square matrix where each row and column corresponds to an age class. The top row contains fecundity values (how many offspring each age class produces), and the sub-diagonal contains survival probabilities (the chance of advancing from one age class to the next). Multiplying this matrix by a vector of current age-class abundances yields the population structure one time step later. Repeated multiplication projects the population forward, and the dominant eigenvalue of the matrix gives **lambda (λ)**, the finite rate of population increase. If λ > 1, the population grows; if λ < 1, it declines.

One of the most powerful insights from this framework is **sensitivity analysis**: not all vital rates contribute equally to lambda. In long-lived species like whales or tortoises, small improvements in adult survival have a much larger effect on population growth than equivalent improvements in juvenile survival or fecundity. This is because reproductive adults represent a large cumulative investment by the population — losing them eliminates many future reproductive years. Conversely, in short-lived, highly fecund species like insects, fecundity and early survival matter more. Conservation biologists use sensitivity analysis directly: if you can only protect one life stage, the Leslie matrix tells you which intervention will have the greatest impact on population recovery.
