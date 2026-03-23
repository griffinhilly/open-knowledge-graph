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
stage: formal-systems
status: validated
---

# Age-Structured Demography and Fecundity

## Core Idea
Population growth depends on age-specific survival and fecundity rates, not just total reproduction. Life tables encode these vital rates; Leslie matrix models show how populations change when different age classes have different survival and reproduction. Population growth rate (lambda) emerges from vital rates; small changes in reproductive-age survival often have larger effects than changes to pre-reproductive individuals.

## Questions

```yaml
- question: "A conservation team is managing an endangered whale population (λ = 0.95) and has limited resources. Sensitivity analysis of their Leslie matrix shows that adult survival has a sensitivity of 0.8 while juvenile fecundity has a sensitivity of 0.1. The team should prioritize:"
  type: multiple-choice
  options:
    - "Increasing juvenile fecundity, because more births directly increase population size"
    - "Protecting adult survival, because adults have the highest sensitivity value"
    - "Splitting resources equally, since both vital rates affect lambda"
    - "Improving juvenile survival, since juveniles become future adults"
  answer: 1
  explanation: "Sensitivity analysis tells you the effect on λ of a small absolute change in each vital rate. Adult survival having sensitivity 0.8 versus fecundity at 0.1 means a given improvement in adult survival improves λ eight times more than the same improvement in fecundity. For long-lived species like whales, each adult represents many future reproductive years — losing adults costs the population far more than losing an equivalent number of juveniles. This is exactly the practical application the Leslie matrix enables."

- question: "Two sea turtle populations each contain 500 individuals. Population A has 80% adults; Population B has 80% juveniles that won't reproduce for 15 years. Which population will grow faster in the near term, and why?"
  type: multiple-choice
  options:
    - "Population A, because its age structure places more individuals in reproductive classes now"
    - "Population B, because more juveniles means greater long-term reproductive potential"
    - "They will grow at the same rate, since total population size is identical"
    - "Population B, because juvenile survival rates are typically higher than adult rates"
  answer: 0
  explanation: "Population size alone does not determine growth — age structure does. Population A, dominated by reproductive adults, will produce far more offspring in the near term than Population B, whose members are years away from reproducing. The life table and Leslie matrix formalize this insight: the same 500 individuals can have very different λ values depending on how they are distributed across age classes. This is why demographic models track age structure rather than just total counts."

- question: "The dominant eigenvalue of the Leslie matrix gives the finite rate of population increase (λ), where λ > 1 indicates population growth."
  type: true-false
  answer: true
  explanation: "This is a fundamental result from matrix population models. When the Leslie matrix is repeatedly multiplied by the age-class abundance vector, the population converges to a stable age distribution and grows (or declines) at a constant rate equal to the dominant eigenvalue λ. λ > 1 means the population multiplies each time step; λ < 1 means it declines; λ = 1 means it is stationary. This eigenvalue analysis is why the Leslie matrix is so powerful — it extracts a single summary of population fate from all the age-specific vital rates."

- question: "For all species, improving juvenile survival always has a larger effect on population growth rate than improving adult survival by the same amount."
  type: true-false
  answer: false
  explanation: "This is false — the relative importance of survival at different ages depends on life history. For long-lived, slow-reproducing species (whales, tortoises, condors), adult survival typically has much higher sensitivity than juvenile survival or fecundity, because each adult represents many future reproductive years. Conversely, for short-lived, highly fecund species like insects or annual plants, early survival and fecundity may matter more. Sensitivity analysis via the Leslie matrix reveals this life-history dependency rather than giving a universal answer."

- question: "Why does sensitivity analysis of a Leslie matrix tell conservation biologists which life stage to protect, and what property of long-lived species makes adult survival particularly important?"
  type: short-answer
  answer: "Sensitivity analysis computes how much λ changes per unit change in each vital rate, identifying which rates exert the greatest leverage on population growth. For long-lived species, adult survival has high sensitivity because reproductive adults represent a large cumulative investment: each adult has already survived many years and will contribute offspring across many future time steps. Losing an adult eliminates all those future reproductive events. Improving adult survival by even a small amount therefore adds many future reproductive years to the population — an effect far larger than adding the same number of juveniles who may not survive to reproduction."
  explanation: "The key is connecting sensitivity values to the biological logic of why adult survival matters disproportionately in long-lived species. Students who understand this can predict which vital rates matter without needing to run the matrix calculation — because the underlying logic follows from life-history theory."
```

## Explainer

From your study of population age structure and life history, you know that not all individuals in a population are equivalent — they differ in age, size, and reproductive status. Age-structured demography formalizes this insight by tracking survival and reproduction as functions of age, revealing why identical-sized populations can have very different futures depending on their age composition.

The foundation of this approach is the **life table**, a schedule that records age-specific survival probability (l_x, the chance of surviving from birth to age x) and age-specific fecundity (m_x, the average number of offspring produced at age x). Together, these columns capture everything you need to project a population's trajectory. For example, a population of sea turtles where most individuals are juveniles that won't reproduce for decades will grow very differently from one dominated by reproductive adults — even if the total count is the same. The life table makes this distinction explicit.

To model how age-structured populations change over time, ecologists use the **Leslie matrix**, a square matrix where each row and column corresponds to an age class. The top row contains fecundity values (how many offspring each age class produces), and the sub-diagonal contains survival probabilities (the chance of advancing from one age class to the next). Multiplying this matrix by a vector of current age-class abundances yields the population structure one time step later. Repeated multiplication projects the population forward, and the dominant eigenvalue of the matrix gives **lambda (λ)**, the finite rate of population increase. If λ > 1, the population grows; if λ < 1, it declines.

One of the most powerful insights from this framework is **sensitivity analysis**: not all vital rates contribute equally to lambda. In long-lived species like whales or tortoises, small improvements in adult survival have a much larger effect on population growth than equivalent improvements in juvenile survival or fecundity. This is because reproductive adults represent a large cumulative investment by the population — losing them eliminates many future reproductive years. Conversely, in short-lived, highly fecund species like insects, fecundity and early survival matter more. Conservation biologists use sensitivity analysis directly: if you can only protect one life stage, the Leslie matrix tells you which intervention will have the greatest impact on population recovery.
