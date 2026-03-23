---
id: measures-of-association
title: Measures of Association and Impact
domain: health-and-human-development
course: public-health
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: disease-frequency-measures
  type: hard
builds-toward:
- biostatistics-in-public-health
- chronic-disease-epidemiology
- disease-prevention-levels
tags:
- relative-risk
- odds-ratio
- attributable-risk
- causation
- epidemiology
stage: expert
status: validated
---

# Measures of Association and Impact

## Core Idea
The relative risk (risk ratio) compares incidence between exposed and unexposed groups, conveying how much more likely exposure makes an outcome. The odds ratio approximates the risk ratio for rare diseases and is the native output of logistic regression. Attributable risk (risk difference) quantifies the absolute excess burden due to exposure, which matters more for policy prioritization than relative measures alone. Population attributable fraction estimates how much disease would be eliminated if an exposure were removed from the population entirely, combining the size of the exposed group with the strength of association.

## How It's Best Learned
Practice computing RR, OR, AR, and PAF from 2×2 contingency tables. Then interpret a set of real epidemiologic findings where RR and AR tell conflicting 'importance' stories—this crystallizes why both perspectives are necessary.

## Common Misconceptions
- A large relative risk does not mean the exposure causes many cases if baseline risk is very low; absolute risk difference matters for public health impact.
- An OR > 1 does not mean the exposure is causal; it means disease is more common among the exposed, which could reflect bias or confounding.
- PAF depends on both how common the exposure is and how strong the association is; a weak association in a highly prevalent exposure can have high PAF.

## Questions

```yaml
- question: "A study finds smokers have a relative risk (RR) of 15 for lung cancer, while sedentary adults have an RR of 1.3 for type 2 diabetes. Which factor could make diabetes prevention the higher public health priority despite the smaller RR?"
  type: multiple-choice
  options: ["The diabetes study used a larger sample size", "Sedentary behavior is far more prevalent, giving it a much higher population attributable fraction", "An RR below 2 is not statistically meaningful", "The odds ratio for sedentary behavior corrects for confounding in ways RR cannot"]
  answer: 1
  explanation: "Population attributable fraction (PAF) depends on both the strength of association (RR) and the prevalence of the exposure. If 60% of the population is sedentary, even an RR of 1.3 can account for a huge share of all diabetes cases. A lung cancer RR of 15 is dramatic, but if few people smoke, fewer total cases are attributable. This is why absolute and population-level measures must accompany relative risk when setting priorities."

- question: "A relative risk of 8.0 always indicates a greater public health burden than a relative risk of 1.4."
  type: true-false
  answer: false
  explanation: "Relative risk captures how much more likely an outcome is in the exposed group compared to the unexposed — it does not account for how common the exposure is or how frequent the baseline outcome is. An RR of 8.0 on an exposure affecting 0.1% of the population may cause far fewer total cases than an RR of 1.4 applied to an exposure affecting 70% of the population. Public health impact requires examining attributable risk and population attributable fraction alongside relative measures."

- question: "In a case-control study of a rare disease, why is the odds ratio (OR) preferred over the relative risk (RR)?"
  type: short-answer
  answer: "Case-control studies select participants based on disease status, not exposure, so true population incidence rates cannot be directly calculated. The OR can be computed from the resulting 2×2 table and approximates the RR closely when the disease is rare."
  explanation: "Relative risk requires incidence data from defined exposed and unexposed populations followed over time — a cohort design. In a case-control study, researchers work backward from disease outcomes to past exposures, so the proportion of 'exposed' among cases and controls does not reflect true population incidence. The OR — calculated as (exposed cases × unexposed controls) ÷ (unexposed cases × exposed controls) — avoids this problem and is a valid approximation of RR under the rare disease assumption."
```

## Explainer

When you studied disease frequency measures, you learned to quantify how common a condition is using incidence rates and prevalence. Measures of association take the next step: comparing those frequencies between groups to determine whether an exposure is linked to an outcome, and how strongly.

The **relative risk** (RR), also called the risk ratio, is the most direct measure. Divide the incidence rate in the exposed group by the incidence rate in the unexposed group. An RR of 4 means exposed individuals develop the outcome four times as often. An RR of 1 means no difference. The RR is most naturally computed from cohort studies, where you follow exposed and unexposed groups forward in time and compare outcomes.

The **odds ratio** (OR) answers a similar question but is calculated differently — as the ratio of the odds of disease in the exposed group to the odds in the unexposed group. The OR is the native measure in case-control studies and logistic regression, because those designs do not yield incidence rates directly. When the disease is rare (roughly under 10% prevalence), the OR closely approximates the RR. For common outcomes, the OR exaggerates the association and should not be interpreted as though it were an RR.

Both RR and OR tell you about *relative* differences between groups, but they say nothing about absolute burden. This is where **attributable risk** (AR) enters. The risk difference — incidence in exposed minus incidence in unexposed — tells you how much extra disease the exposure adds per person at risk. An exposure might have an RR of 10, but if baseline incidence is 1 in a million, the AR is only 9 in a million — still extremely rare. Conversely, a modest RR applied to a very common exposure can produce a large AR.

Finally, the **population attributable fraction** (PAF) asks: if this exposure were entirely eliminated from the population, what fraction of all cases would disappear? PAF incorporates both the strength of the association and the prevalence of the exposure. A moderate association with a very common exposure can have a higher PAF than a dramatic association with a rare one. This is why addressing ubiquitous risk factors like physical inactivity or high dietary sodium often prevents more total disease than addressing rarer but biologically potent exposures. Knowing when to emphasize relative versus absolute versus population-level measures is the core practical skill this topic develops.
