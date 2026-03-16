---
id: outcome-misclassification-epi
title: Outcome Misclassification and Differential Error
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: information-bias-epidemiology
  type: hard
- id: diagnostic-sensitivity-specificity
  type: hard
builds-toward:
- missing-data-epidemiology
tags:
- measurement-error
- misclassification
- bias
- outcome-validity
stage: advanced
status: draft
---

# Outcome Misclassification and Differential Error

## Core Idea
Outcome misclassification occurs when true outcome status is incorrectly recorded. Non-differential errors typically bias effects toward the null; differential errors can bias in any direction. Sensitivity and specificity of outcome measures determine bias direction and magnitude.

## Explainer

Your prerequisites give you two essential tools for this topic: the general framework of information bias (measurement error distorts epidemiological estimates) and the sensitivity/specificity framework (which characterizes how well a diagnostic test correctly identifies true cases and non-cases). **Outcome misclassification** occurs when a study's outcome measure incorrectly assigns status — true cases are recorded as non-cases (false negatives, reflecting imperfect sensitivity) or true non-cases are recorded as cases (false positives, reflecting imperfect specificity). The critical question is whether this misclassification is **differential** (varying between exposed and unexposed groups) or **non-differential** (occurring equally across groups regardless of exposure).

**Non-differential misclassification** is the more common scenario and has a predictable, directional effect: it biases measures of association — risk ratios, odds ratios — toward the null (i.e., toward 1.0 for ratio measures). The intuition is that random misclassification "smears" the distinction between true cases and non-cases symmetrically across both groups, reducing the apparent contrast between exposed and unexposed. If a study finds a relative risk of 1.5, the true association may well be stronger — misclassification has diluted it. This has an important implication: a null or weak finding in a study using an imperfect outcome measure does not necessarily mean the true effect is null. A low-sensitivity outcome measure (many true cases missed) particularly attenuates associations when the disease is rare in both groups.

**Differential misclassification** is more dangerous because its direction is unpredictable and must be reasoned through case by case. Misclassification is differential when the probability of being misclassified depends on exposure status — meaning the false-negative or false-positive rate differs between exposed and unexposed groups. Consider a retrospective cohort study using medical records to ascertain myocardial infarction. Physicians may order and document cardiac workups more thoroughly for patients on a medication under investigation, leading to better case ascertainment in the exposed group. This inflates apparent incidence in the exposed group and biases the relative risk *away from* the null. The opposite can also occur: if exposed patients are less symptomatic due to a protective exposure, they seek care less often, their events go undiagnosed, and ascertainment is lower in the exposed group — biasing toward the null. The direction of bias follows from the mechanism of differential ascertainment, not from a general rule.

The sensitivity/specificity framework allows quantitative prediction of bias magnitude. For a given outcome sensitivity and specificity, and under non-differential misclassification, formulas exist to estimate the expected attenuation of the observed relative risk relative to the true relative risk. **Quantitative bias analysis** uses these formulas with plausible ranges of misclassification parameters to bound the likely true effect when perfect outcome measurement was impossible. In practice, the preferred solution is improving outcome validity at the design stage: using standardized case definitions, blinded outcome adjudication committees, or validated endpoint instruments that have known sensitivity and specificity. When improvement is not possible — as in studies relying on administrative claims data or self-report — quantitative bias analysis is the appropriate analytical response rather than dismissing the limitation with a footnote.
