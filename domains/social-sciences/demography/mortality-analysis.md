---
id: mortality-analysis
title: Mortality Analysis
domain: social-sciences
course: demography
prerequisites:
- id: life-tables-demography
  type: hard
- id: crude-rates-and-specific-rates
  type: hard
builds-toward:
- population-projections
- population-aging-demography
tags:
- mortality
- infant-mortality
- cause-of-death
- epidemiologic-transition
stage: advanced
status: validated
---

# Mortality Analysis

## Core Idea
Mortality analysis examines the patterns, trends, causes, and differentials in death across populations. Key measures include the infant mortality rate (IMR), under-five mortality rate, maternal mortality ratio, and cause-specific death rates. The epidemiologic transition describes the historical shift from infectious and parasitic diseases as leading causes of death to chronic and degenerative diseases — a shift driven by improvements in nutrition, sanitation, public health, and medical care. Mortality differentials by sex, socioeconomic status, race/ethnicity, and geography reveal the social determinants of health. Decomposition techniques allow analysts to attribute changes in life expectancy to specific age groups or causes of death.

## How It's Best Learned
Compare cause-of-death profiles and age-specific mortality curves for a low-income and a high-income country. The contrast between a mortality regime dominated by infectious disease in childhood versus one dominated by chronic disease in old age makes the epidemiologic transition concrete.

## Common Misconceptions
- Infant mortality rate is not a rate in the strict demographic sense — it is the number of deaths under age 1 per 1,000 live births in a year, using births rather than mid-year population as the denominator.
- The epidemiologic transition is not a simple one-time shift; some populations experience a "double burden" of infectious and chronic diseases simultaneously.

## Questions

```yaml
- question: "A country reports 8,000 infant deaths and 200,000 live births in a year. What is its infant mortality rate, and why is this measure technically not a 'rate' in the strict demographic sense?"
  type: multiple-choice
  options:
    - "40 per 1,000; it is technically a rate because it uses the mid-year infant population as the denominator"
    - "40 per 1,000; it is technically a ratio because the denominator (live births) is not the mid-year population at risk but rather a flow measure"
    - "4 per 1,000; the denominator should be the total population, making it a true rate"
    - "40 per 1,000; the distinction between rates and ratios is semantic and has no analytical consequence"
  answer: 1
  explanation: "IMR = 8,000 / 200,000 x 1,000 = 40 per 1,000. Strictly, a rate uses a mid-year population denominator (a stock measure); the IMR uses live births (a flow measure). This matters analytically because the births in the denominator and the deaths in the numerator do not refer to exactly the same cohort — some deaths in a calendar year are to babies born the previous year, and some babies born this year will die next year."

- question: "The epidemiologic transition describes a permanent, irreversible shift from infectious to chronic disease as the dominant cause of death."
  type: true-false
  answer: false
  explanation: "While the epidemiologic transition describes a general historical pattern, it is not necessarily permanent or irreversible. HIV/AIDS caused a reversal in several sub-Saharan African countries, with life expectancy declining substantially in the 1990s and 2000s as an infectious disease became the leading killer. Some scholars identify a 'fourth stage' of re-emerging infectious diseases and antimicrobial resistance. The transition is a useful model, not an iron law."

- question: "Explain what a cause-deleted life table shows and why it can overestimate the gain in life expectancy from eliminating a cause of death."
  type: short-answer
  answer: "A cause-deleted life table recalculates survival probabilities after removing deaths from a specific cause, showing how much life expectancy would increase if that cause were eliminated. It overestimates the actual gain because it assumes independence of causes — that eliminating one cause does not affect the probability of dying from others. In reality, causes compete: a person 'saved' from heart disease remains at risk of cancer, stroke, and other causes, and many of these share common risk factors. The gain from eliminating one cause is therefore less than the cause-deleted table suggests."
  explanation: "Competing risks are fundamental to mortality analysis. The assumption of cause independence is mathematically convenient but biologically unrealistic — most people who die of one cause had elevated risk of several others. This is why cause-deleted life tables provide an upper bound on the life expectancy gain rather than a precise estimate."
```

## Explainer

With life tables providing the framework for converting age-specific mortality into survivorship and life expectancy, mortality analysis adds the dimensions of cause, trend, and differential. The life table tells you *how much* mortality there is at each age; mortality analysis asks *why* — what kills people, how those causes have changed over time, and who is at greatest risk.

The **infant mortality rate** (IMR) is the most commonly cited single indicator of population health, calculated as deaths under age 1 per 1,000 live births. Despite its name, it is technically a ratio rather than a rate, because the denominator is a flow (births) rather than a stock (mid-year population). This technicality has practical consequences: some deaths counted in the numerator for a calendar year occurred to babies born the previous year, and some babies born this year will die in the next. Neonatal mortality (deaths in the first 28 days) and postneonatal mortality (deaths from 28 days to 1 year) have different cause profiles — neonatal deaths are dominated by congenital conditions and birth complications, while postneonatal deaths are more sensitive to nutrition, sanitation, and infectious disease.

The **epidemiologic transition**, conceptualized by Abdel Omran in 1971, describes the shift in cause-of-death patterns that accompanies development. In the first stage ("age of pestilence and famine"), infectious diseases, malnutrition, and maternal complications dominate, and life expectancy is low. In the second stage ("age of receding pandemics"), public health improvements reduce infectious mortality, and life expectancy rises. In the third stage ("age of degenerative and man-made diseases"), chronic conditions — heart disease, cancer, stroke — become the leading killers as populations age. Later scholars added a fourth stage of delayed degenerative diseases and a possible fifth stage of re-emerging infections. The model is useful but not deterministic: HIV/AIDS reversed the transition in several African countries, demonstrating that progress is contingent, not guaranteed.

**Mortality differentials** reveal how death is socially patterned. In virtually every studied population, mortality varies by sex (women live longer), socioeconomic status (higher income and education predict lower mortality), race/ethnicity (reflecting structural inequality rather than biology), and geography (urban-rural gaps, regional variation). Decomposition methods — particularly Arriaga's and Pollard's techniques — allow analysts to attribute a change in life expectancy to contributions from specific age groups and causes, answering questions like "how much of the gap in life expectancy between men and women is due to cardiovascular mortality in ages 50-69?"
