---
id: population-attributable-risk-and-impact
title: Population Attributable Risk and Disease Burden Estimation
domain: health-and-human-development
course: public-health
prerequisites:
- id: relative-risk-calculation
  type: hard
- id: disease-frequency-measures
  type: hard
builds-toward:
- burden-of-disease-and-comparative-health-assessment
- policy-analysis-and-health-impact-evaluation
tags:
- epidemiology
- burden-of-disease
- risk-metrics
stage: advanced
status: draft
---

# Population Attributable Risk and Disease Burden Estimation

## Core Idea
Population attributable risk (PAR) combines the strength of association between a risk factor and disease with the prevalence of that factor to estimate the disease burden potentially preventable by eliminating the exposure. PAR differs from relative risk (individual-level) and is essential for prioritizing public health resources. A weak risk factor with high prevalence may have greater PAR than a strong risk factor affecting few people.

## How It's Best Learned
Calculate PAR for multiple risk factors in the same disease (e.g., smoking, obesity, physical inactivity for cardiovascular disease) to compare their relative contributions to disease burden.

## Common Misconceptions
- Relative risk directly predicts population impact; high relative risk for rare exposures has minimal PAR.
- PAR assumes elimination of exposure is feasible; in practice, PAR estimates represent upper bounds on preventable disease.

## Questions

```yaml
- question: "A genetic variant multiplies lung cancer risk 50-fold (RR = 50) but is carried by only 0.2% of the population. A smoking-cessation campaign targets a risk factor with RR = 3 that affects 30% of the population. Using PAR% = p(RR−1) / [p(RR−1) + 1], which intervention would prevent more cancer cases?"
  type: multiple-choice
  options:
    - "Genetic screening — the 50-fold relative risk clearly dominates"
    - "The smoking-cessation campaign — high prevalence means smoking's PAR far exceeds the genetic variant's"
    - "They are equal because PAR is determined solely by relative risk"
    - "Genetic screening — rare, severe risk factors always take priority in public health"
  answer: 1
  explanation: "Genetic variant: PAR ≈ 0.002 × 49 / (0.002 × 49 + 1) ≈ 9%. Smoking: PAR ≈ 0.30 × 2 / (0.30 × 2 + 1) ≈ 37.5%. Despite the dramatically higher relative risk, the genetic variant's tiny prevalence limits its population impact. Smoking's moderate risk applied to a large population prevents far more cases in absolute terms. This is the core lesson: PAR depends on both RR and prevalence, and high RR alone does not determine population impact."

- question: "A study reports smoking PAR for cardiovascular disease = 35%, physical inactivity PAR = 25%, and hypertension PAR = 20%. A student concludes that eliminating all three risk factors would prevent 80% of cardiovascular cases. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "PAR values can sum above 100%, making the calculation technically valid"
    - "Risk factors co-occur and their effects overlap, so individual PARs cannot simply be added"
    - "PAR measures individual risk, not population burden, so it cannot be summed across groups"
    - "The student forgot to weight each PAR by the intervention's effectiveness"
  answer: 1
  explanation: "PARs for different risk factors in the same disease do not add linearly because the same patient may simultaneously be a smoker, physically inactive, and hypertensive. That patient appears in all three PAR estimates. Summing them double- or triple-counts overlapping cases. The actual preventable burden from eliminating all three is bounded by 100% and is less than the arithmetic sum of individual PARs. PARs are best used for *ranking* risk factors' relative contributions, not for summing."

- question: "A risk factor with a very high relative risk (e.g., RR = 100) always has a larger population attributable risk than a risk factor with a moderate relative risk (e.g., RR = 5)."
  type: true-false
  answer: false
  explanation: "This is exactly the misconception PAR is designed to correct. PAR depends on both relative risk AND exposure prevalence. A risk factor with RR = 100 but prevalence 0.01% has a tiny PAR — almost no one is exposed, so eliminating it prevents almost no cases. A risk factor with RR = 5 affecting 40% of the population has a large PAR — the moderate individual risk is multiplied across a huge exposed group. Prevalence and relative risk together determine population impact."

- question: "Population attributable risk represents an upper bound on preventable disease burden, not a prediction of what any specific intervention will actually achieve."
  type: true-false
  answer: true
  explanation: "PAR assumes complete elimination of the exposure — a theoretical ideal. Real-world interventions rarely achieve 100% reduction in a risk factor across an entire population. Smoking rates, dietary patterns, and physical activity are shaped by environment, culture, economics, and psychology, and change slowly and incompletely in response to policy. PAR therefore sets a ceiling on what is theoretically preventable, not a forecast of any particular intervention's outcome. Its power is comparative: ranking which risk factors offer the greatest return on intervention investment."

- question: "Explain why two risk factors with very different relative risks might have similar population attributable risks."
  type: short-answer
  answer: "PAR depends on both the relative risk (strength of the association) and the prevalence of the exposure in the population. A high-RR risk factor that is very rare contributes little to overall disease burden because few people are exposed. A moderate-RR risk factor that is very common contributes substantially because that modest individual risk is multiplied across a large proportion of the population. When the lower-RR factor has sufficiently higher prevalence, its PAR can equal or exceed that of the rarer but stronger risk factor."
  explanation: "The formula PAR% = p(RR−1) / [p(RR−1) + 1] makes this explicit: the numerator involves both p and (RR−1). A small p × large (RR−1) can equal a large p × small (RR−1). This is why public health interventions targeting common, moderately-sized risks often prevent more disease than targeting rare, large risks."
```

## Explainer

You already know how to calculate **relative risk (RR)** from cohort data: it measures the strength of association between an exposure and a disease at the individual level. An exposed person is RR times more likely to develop disease than an unexposed person. **Population attributable risk (PAR)** asks a different — and for policy purposes more important — question: if we eliminated this exposure from the entire population, how much disease would disappear?

The formula reveals why high RR doesn't automatically translate to high PAR. PAR depends on two things: the strength of association (RR) and the **prevalence of exposure** in the population. The formula is: PAR% = p(RR − 1) / [p(RR − 1) + 1], where p is the prevalence of exposure in the general population. Consider two risk factors for lung cancer: smoking (RR ~15–25, prevalence ~15% in many countries) and a hypothetical rare genetic variant (RR = 50, prevalence 0.5%). The genetic variant has a dramatically higher relative risk, but its PAR is tiny because almost nobody carries it. Smoking's PAR is enormous because the risk is high and the exposure is widespread. The practical implication: targeting common, moderately-sized risks often prevents more disease than targeting rare, large risks.

The logic of PAR becomes clearest when comparing multiple risk factors for the same disease. Suppose you're analyzing preventable cardiovascular disease and compute PAR for smoking (35%), physical inactivity (25%), hypertension (20%), and obesity (20%). These percentages don't sum to 100% — they can overlap because risk factors co-occur and their joint effects are not simply additive. But ranking them by PAR tells public health planners where intervention resources will have the greatest expected return. A smoking intervention with a PAR of 35% theoretically prevents more cardiovascular deaths than a hypertension intervention with PAR of 20%, holding intervention effectiveness constant.

Two important limitations temper the use of PAR in practice. First, PAR rests on the causal assumption embedded in the RR estimate — if confounding inflates the apparent association, PAR is correspondingly overstated. Second, "eliminating the exposure" is a theoretical construct. People don't stop smoking simply because policy says so; dietary and physical activity patterns are shaped by environment, culture, and economics. PAR therefore represents an **upper bound** on what is preventable, not a prediction of what any specific intervention will achieve. Its value is comparative — ranking risk factors against each other — rather than absolute prediction of impact. This is why PAR is described as translating epidemiological evidence into the language of public health priority-setting.
