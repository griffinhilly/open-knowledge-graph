---
id: rasch-model
title: 'Rasch Model: One-Parameter Item Response Theory'
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: probability-and-statistics
  type: hard
- id: exponential-functions-and-graphs
  type: hard
builds-toward:
- irt-model-fit-comparison
tags:
- rasch-model
- 1pl
- item-response-theory
- interval-scale
stage: advanced
status: draft
---

# Rasch Model: One-Parameter Item Response Theory

## Core Idea
The Rasch model is the simplest item response theory model, assuming item difficulty is the sole item parameter, with equal discrimination across items. It produces interval-scale scores and has desirable statistical properties. The model is most useful when sample size is limited or when simplicity is valued over model complexity.

## How It's Best Learned
Fit Rasch models to real assessment data using software (Winsteps, RUMM). Examine goodness-of-fit statistics and compare Rasch item parameters with classical item difficulty indices.

## Common Misconceptions
Perfect Rasch model fit guarantees good measurement or validity. Even perfect fit doesn't ensure the test measures the intended construct. The unidimensionality requirement is critical but sometimes overstated regarding what it means for practical application.

## Questions

```yaml
- question: "Under the Rasch model, what makes the total raw score a 'sufficient statistic' for ability estimation?"
  type: multiple-choice
  options:
    - "All items are scored on the same scale, so they contribute equally to the total"
    - "Because all item characteristic curves have the same slope, the number correct contains all the information about ability — which specific items were answered correctly adds nothing"
    - "The raw score is sufficient because the Rasch model assumes all items are equally difficult"
    - "Raw scores are sufficient in all IRT models, not just the Rasch model"
  answer: 1
  explanation: "Sufficient statistic means knowing the total raw score is enough — you don't need to know *which* items the person got right. This property holds uniquely in the Rasch (1PL) model because all ICCs have the same slope (discrimination). When discriminations differ (2PL model), getting a hard item right carries different information than getting an easy item right, so the raw score alone is no longer sufficient. This sufficiency property is what underpins Rasch's 'specific objectivity.'"

- question: "A researcher finds perfect fit of a test to the Rasch model. They conclude the test is valid and measures what it claims to measure. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — perfect model fit proves construct validity"
    - "Perfect fit only means the items have equal discrimination; it says nothing about whether the construct being measured is the intended one"
    - "Rasch fit statistics cannot reach perfection, so the premise is impossible"
    - "The conclusion would be correct if sample size is large enough"
  answer: 1
  explanation: "Rasch model fit indicates that items behave consistently with the model's assumptions (equal discrimination, unidimensionality). It says nothing about whether the measured trait is the one you *intended* to measure. A perfectly fitting Rasch scale could measure something entirely different from the claimed construct — validity is a separate, substantive judgment requiring content analysis, criterion validity studies, and domain expertise. Fit statistics diagnose statistical behavior, not meaning."

- question: "The Rasch model produces interval-scale ability estimates because it converts raw scores into logit units."
  type: true-false
  answer: true
  explanation: "Raw test scores are ordinal — going from 0 to 1 correct may represent a larger ability jump than going from 9 to 10, depending on item placement. Rasch converts scores to log-odds (logit) units via the model's logistic function, which places persons and items on a common interval scale. A one-logit difference in ability means the same increase in probability of success regardless of where you are on the scale. This interval property allows arithmetic operations (means, differences, regressions) that are inappropriate for raw scores."

- question: "Under the Rasch model, item difficulty estimates obtained from one sample are meaningless for describing those items' behavior in a different sample."
  type: true-false
  answer: false
  explanation: "This is precisely what the Rasch model's 'specific objectivity' refutes. When data fit the model, item difficulty estimates are sample-independent — they can be calibrated on one group and applied to another (after equating the scales). This is analogous to physical measurement: a ruler calibrated in one laboratory gives the same measurement elsewhere. Under CTT or 2PL IRT, item parameters are more sample-dependent because the discrimination parameter conflates item properties with the ability range of the sample."

- question: "What is 'specific objectivity' in the Rasch model and why does it make Rasch measurement resemble physical measurement more than classical test scores do?"
  type: short-answer
  answer: "Specific objectivity means that person ability estimates do not depend on which particular items were administered, and item difficulty estimates do not depend on which particular sample was tested — as long as the data fit the model. This mirrors physical measurement: you can measure a person's weight with different calibrated scales and get the same result. Classical raw scores lack this property because they are sensitive to item selection (an easy test inflates scores) and sample characteristics (item statistics shift with sample ability). Rasch's logit scale creates a stable metric that allows comparisons across test forms and samples."
  explanation: "The physical measurement analogy is important: Rasch saw his model as achieving in psychology what rulers and thermometers achieve in physics — a context-independent unit of measurement. Whether this ideal is achievable with psychological constructs (which are far less clearly defined than length or temperature) is debated, but it sets the aspirational standard that distinguishes measurement from mere ordering."
```

## Explainer

From your study of item response functions, you know that an **item characteristic curve** (ICC) maps person ability onto the probability of a correct response — an S-shaped curve that rises from near zero at the left (low ability) to near one at the right (high ability). Different IRT models differ in how many parameters they use to describe each item's ICC. The Rasch model, also called the **1-parameter logistic (1PL)** model, makes a radical simplifying claim: every item's ICC has exactly the same slope. The only thing that varies across items is where the curve is centered on the ability scale — how hard the item is. Easy items have their curve shifted left (most people of average ability get them right); hard items shift right.

This might seem overly restrictive, but the simplicity buys something important. When all ICCs have the same slope, a person's total raw score is a **sufficient statistic** for their ability estimate — you don't need any more information about which specific items they got right or wrong, only how many. This is a unique and mathematically remarkable property. It also means that under the Rasch model, item difficulty estimates do not depend on the particular sample of people you used to calibrate them, and person ability estimates do not depend on the particular set of items administered. This property is called **specific objectivity**, and it is what makes Rasch measurement feel more like physical measurement: you can measure a person's weight with different scales and get the same result, as long as the scales are calibrated on the same metric.

The interval-scale property follows from the log-odds transformation at the heart of the model. Raw scores on a classical test are ordinal — going from 0 to 1 correct might be a bigger ability jump than going from 9 to 10 correct, depending on item placement, but the raw score treats all increments as equal. Rasch converts raw scores to **logit** estimates (log-odds units) that are interval-scale: a one-logit difference in ability means the same increase in probability of success regardless of where on the scale you are. This matters for research that computes means, differences, and regression coefficients — arithmetic operations that assume interval measurement.

The model's limitation is the stringency of its assumptions. All items must discriminate equally well between people just above and just below the item's threshold — an assumption that real items frequently violate. Items also must show no **differential item functioning**: they should be equally fair across demographic subgroups (gender, ethnicity, language background) after controlling for ability. When data don't fit the Rasch model, researchers face a choice: remove misfitting items (sacrificing content) or move to a more flexible 2PL or 3PL model (sacrificing the specific-objectivity property). Neither option is free. Rasch fit statistics — infit and outfit mean-square statistics — diagnose which items are behaving inconsistently with the model, but fit statistics alone cannot tell you whether the violation is serious enough to invalidate the measurement for your purpose. That judgment requires content knowledge about what each item is measuring and why it might behave unexpectedly.
