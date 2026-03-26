---
id: attributable-risk-calculation
title: Attributable Risk and Population Attributable Fraction
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: relative-risk-calculation
  type: hard
- id: odds-ratio-interpretation
  type: soft
builds-toward:
- number-needed-to-treat
tags:
- attributable-risk
- public-health-impact
- prevention
stage: expert
status: validated
---

# Attributable Risk and Population Attributable Fraction

## Core Idea
Attributable risk (AR) quantifies the absolute excess risk due to exposure: AR = Risk(Exposed) – Risk(Unexposed). Population attributable fraction (PAF) indicates what proportion of disease in the population results from exposure, accounting for both the RR and the prevalence of exposure. AR and PAF are essential for setting public health priorities.

## Questions

```yaml
- question: "Two occupational exposures each have a relative risk of 4 for a certain cancer. Exposure A affects 3% of the population; Exposure B affects 45% of the population. Which has the larger population attributable fraction?"
  type: multiple-choice
  options:
    - "Exposure A, because its rarity makes it a more specific and potent cause"
    - "They are equal, because PAF depends only on the relative risk"
    - "Exposure B, because PAF depends on both the relative risk and the prevalence of exposure in the population"
    - "Cannot be determined without knowing the absolute incidence of cancer"
  answer: 2
  explanation: "PAF = Pe(RR − 1) / [1 + Pe(RR − 1)]. With RR = 4 (so RR − 1 = 3): Exposure A gives PAF ≈ 0.03 × 3 / (1 + 0.03 × 3) = 0.083 (8.3%). Exposure B gives PAF ≈ 0.45 × 3 / (1 + 0.45 × 3) = 0.574 (57.4%). The same individual risk ratio produces vastly different population impact depending on how common the exposure is. Eliminating a common exposure with moderate RR prevents far more cases than eliminating a rare exposure with the same RR. This is the core insight that distinguishes public health priorities from individual clinical risk."

- question: "Among exposed workers, 18% develop a disease over 10 years. Among unexposed workers, 6% develop the same disease. What is the attributable risk?"
  type: multiple-choice
  options:
    - "3 (the relative risk, calculated as 18/6)"
    - "12% (the absolute excess risk: 18% − 6%)"
    - "6% (the background risk in unexposed workers)"
    - "67% (the attributable fraction among the exposed)"
  answer: 1
  explanation: "Attributable risk = Risk(Exposed) − Risk(Unexposed) = 18% − 6% = 12%. This is the absolute excess risk — the additional disease that would not occur if the exposure were eliminated among exposed workers. Option A gives the relative risk (RR = 3), which tells us the exposure multiplies risk by 3, but says nothing about the absolute magnitude. Option D gives the attributable fraction (AR/Risk_Exposed = 12/18 = 67%), a different measure. The distinction between AR (absolute excess) and RR (multiplicative ratio) is the fundamental conceptual test of this topic."

- question: "Attributable risk (risk difference) and relative risk both measure excess disease due to an exposure, so a higher RR usually implies a higher attributable risk."
  type: true-false
  answer: false
  explanation: "AR and RR measure different things and can diverge completely. Two exposures with the same RR can have very different ARs depending on the baseline risk. If baseline risk is 1% and RR = 5, AR = 4%. If baseline risk is 30% and RR = 5, AR = 120% — impossible since risk is bounded, so consider RR = 2: baseline 1% → AR = 1%; baseline 40% → AR = 40%. Conversely, a moderate RR with a high baseline produces a larger AR than a high RR with a low baseline. AR depends on the absolute magnitudes of both risks, not just their ratio."

- question: "A moderately risky exposure (RR = 2) that affects 60% of the population can have a higher population attributable fraction than a highly risky exposure (RR = 10) that affects 1% of the population."
  type: true-false
  answer: true
  explanation: "Using PAF = Pe(RR − 1) / [1 + Pe(RR − 1)]: For RR = 2, Pe = 0.60: PAF = 0.60 × 1 / (1 + 0.60 × 1) = 0.375 (37.5%). For RR = 10, Pe = 0.01: PAF = 0.01 × 9 / (1 + 0.01 × 9) = 0.082 (8.2%). The common, moderately risky exposure has nearly 5× higher PAF. This is why public health campaigns target smoking, physical inactivity, and poor diet — high prevalence exposures with moderate-to-high RR — rather than rare toxic exposures with very high RR but negligible prevalence."

- question: "Explain why public health officials should use population attributable fraction rather than relative risk alone when deciding which exposures to prioritize for population-level interventions."
  type: short-answer
  answer: "Relative risk tells you how much more likely an individual exposed person is to get disease compared to an unexposed person — it's an individual-level measure. PAF tells you what proportion of all cases in the entire population are attributable to a given exposure, factoring in how common that exposure is. A rare exposure with high RR affects few people; eliminating it prevents few cases. A common exposure with moderate RR affects many people; eliminating it prevents many cases. PAF integrates both the magnitude of the individual risk increase and the prevalence of exposure, giving the true potential impact of a population-wide intervention."
  explanation: "The practical consequence is significant: policymakers who prioritize by RR alone will direct resources toward rare, high-ratio exposures that contribute little to total disease burden. PAF-based prioritization directs resources toward exposures where intervention would prevent the most actual cases — which often means focusing on widespread lifestyle and environmental factors rather than rare industrial toxins, even if the latter have higher individual RRs."
```

## Explainer

You already know from relative risk (RR) that it answers the question: "How many times more likely is disease in the exposed group compared to the unexposed?" But RR, powerful as it is, tells you nothing about the actual burden of disease attributable to that exposure, nor about the potential impact of eliminating it. **Attributable risk (AR)** — also called the **risk difference** — closes this gap by subtracting: AR = Risk(Exposed) − Risk(Unexposed). If exposed workers have a 10% five-year risk of lung disease and unexposed workers have a 2% risk, AR = 8%. That 8% represents the absolute excess disease that would not occur if the exposure were eliminated — the directly preventable fraction among those who were exposed.

Consider two exposures with the same RR of 5 but very different baseline risks. Exposure A raises risk from 1% to 5% (AR = 4%). Exposure B raises risk from 20% to 100% (AR = 80%). The RR is identical, but exposure B is responsible for a vastly greater number of cases per 100 exposed people. This is why AR, not RR, is the correct metric for estimating clinical or policy impact: it tells you the absolute number of cases that an intervention could prevent per unit of exposed population.

The **population attributable fraction (PAF)** takes this logic to the population level, asking: "What proportion of all disease cases in the entire population — exposed and unexposed combined — are attributable to this exposure?" The formula is PAF = Pe(RR − 1) / [1 + Pe(RR − 1)], where Pe is the prevalence of exposure in the population. Alternatively, PAF = (Risk_population − Risk_unexposed) / Risk_population. The PAF depends on both the strength of the association (RR) and how common the exposure is. A moderately risky exposure that affects 60% of the population (e.g., physical inactivity) can have a larger PAF than a highly risky exposure that affects 1% (e.g., a rare occupational toxin), even though the individual risk ratio for the rare exposure is much higher.

This is the core insight for public health prioritization: **high PAF exposures are the ones where population-wide interventions yield the greatest disease reduction**. Smoking cessation campaigns, physical activity programs, and dietary interventions target exposures with both substantial RR and high prevalence, resulting in large PAF values. When setting policy, comparing PAFs across exposures — not just RRs — allows health authorities to allocate resources where elimination or reduction of exposure would prevent the most disease at the population level.
