---
id: cost-utility-analysis
title: 'Cost-Utility Analysis: QALYs and DALYs'
domain: health-and-human-development
course: health-economics
prerequisites:
- id: cost-effectiveness-analysis
  type: hard
- id: cost-effectiveness-analysis-health-econ
  type: hard
builds-toward:
- health-technology-assessment
- willingness-to-pay-health
- burden-of-disease
tags:
- CUA
- QALY
- DALY
- utility
- health-state-valuation
- EQ-5D
stage: advanced
status: validated
---

# Cost-Utility Analysis: QALYs and DALYs

## Core Idea
Cost-utility analysis (CUA) is a specialized form of cost-effectiveness analysis that measures health outcomes in quality-adjusted life-years (QALYs), combining length of life and quality of life into a single metric. One QALY equals one year lived in perfect health; a year lived with a disability or chronic condition is weighted by a utility value between 0 (death) and 1 (perfect health). QALYs enable comparison across diseases and interventions — a cancer drug that extends life by 2 years at utility 0.6 produces 1.2 QALYs, comparable to a joint replacement that improves quality from 0.5 to 0.9 for 3 years (1.2 QALYs). DALYs (disability-adjusted life-years) invert the metric: they measure years of healthy life lost to disease. Both metrics operationalize the intuition that extending a miserable life is worth less than extending a good one, enabling resource allocation that accounts for quality, not just quantity.

## Questions

```yaml
- question: "A cancer treatment extends life by 3 years with a health utility of 0.4 (severe side effects). An alternative treatment extends life by 2 years with a utility of 0.8 (mild side effects). Which produces more QALYs?"
  type: multiple-choice
  options:
    - "The first treatment: 3 × 0.4 = 1.2 QALYs"
    - "The second treatment: 2 × 0.8 = 1.6 QALYs"
    - "They are equal because one trades quantity for quality"
    - "QALYs cannot be calculated without knowing the cost"
  answer: 1
  explanation: "QALYs multiply years by utility: 3 × 0.4 = 1.2 vs. 2 × 0.8 = 1.6. The shorter-lived treatment with better quality produces more QALYs. This illustrates the core value of the QALY metric — it captures the intuition that quality matters, not just duration. A patient might rationally prefer 2 good years to 3 miserable ones, and the QALY framework formalizes this preference. Of course, individual patients may value quality and quantity differently, which is one limitation of using population-average utilities."

- question: "Health utilities used in QALY calculations are typically elicited from the general public rather than from patients actually living with the condition. Why?"
  type: short-answer
  answer: "The general public perspective is used because QALYs inform societal resource allocation decisions — the question is how much society should invest in treating a condition, and society (through taxes or insurance) is paying. Patients who have adapted to their condition often rate their quality of life higher than the general public would predict (disability paradox or hedonic adaptation), which would reduce the apparent benefit of treating the condition and bias allocation away from conditions that people adapt to well. Using public preferences ensures the values reflect societal willingness to pay rather than patient adaptation."
  explanation: "This is controversial. Patient advocates argue that actual patients' valuations are more authentic, while health economists argue that using adapted patient values would systematically undervalue interventions for conditions that patients learn to live with. The choice of whose values to use is fundamentally a normative question about whose perspective should drive resource allocation."

- question: "DALYs and QALYs are conceptual inverses: QALYs measure health gained, DALYs measure health lost. A disease that causes 1,000 DALYs in a population is equivalent to losing 1,000 years of perfect health."
  type: true-false
  answer: true
  explanation: "DALYs = Years of Life Lost (YLL) from premature mortality + Years Lived with Disability (YLD) weighted by disability severity. They measure the burden of disease — the gap between the current health of a population and the ideal of living to old age in perfect health. QALYs measure the health gained from an intervention. A treatment that prevents 1,000 DALYs is equivalent to producing 1,000 QALYs (approximately — the two metrics use slightly different disability weights and reference points, but the conceptual relationship holds)."
```

## Explainer

Standard cost-effectiveness analysis can compare interventions for the same disease (two blood pressure drugs measured in mmHg reduction), but it cannot compare across diseases — how do you weigh a mmHg of blood pressure against a percentage of cancer recurrence? **QALYs** solve this by creating a common currency for health outcomes that combines quantity and quality of life into a single number.

The **QALY** is calculated by multiplying time in a health state by the **utility weight** of that state. Utility weights range from 1 (perfect health) to 0 (death), with some states valued below 0 (worse than death — e.g., severe, unremitting pain). A year of perfect health = 1 QALY. A year at utility 0.7 (moderate arthritis) = 0.7 QALYs. Five years at utility 0.5 = 2.5 QALYs. Utilities are measured using standardized instruments: the **EQ-5D** questionnaire (five dimensions: mobility, self-care, usual activities, pain/discomfort, anxiety/depression, each with 3-5 levels) is the most widely used, with country-specific value sets translating EQ-5D profiles into utility weights.

**DALYs** approach the same problem from the opposite direction — measuring health lost rather than health gained. One DALY represents one lost year of healthy life. DALYs have two components: **Years of Life Lost** (YLL) from premature death (comparing actual age at death to a standard life expectancy) and **Years Lived with Disability** (YLD), weighted by disability severity (ranging from 0 for no disability to 1 for death-equivalent disability). The Global Burden of Disease Study, coordinated by the Institute for Health Metrics and Evaluation, uses DALYs to quantify the health impact of every disease in every country — providing the data foundation for global health priority-setting.

Both metrics have limitations. QALYs assume that a QALY is a QALY regardless of who receives it — one QALY for a 20-year-old is valued the same as one for an 80-year-old, and one QALY for a wealthy person equals one for a poor person. This ignores equity concerns that many societies consider important (some argue QALYs should be weighted by severity or social disadvantage). The utility weights themselves are debatable — they vary by country, elicitation method, and respondent population. And the fundamental assumption that quality and quantity trade off linearly (two years at 0.5 = one year at 1.0) may not match individual preferences. Despite these limitations, QALYs remain the standard outcome measure for health technology assessment worldwide because no better alternative has emerged for cross-disease comparison.
