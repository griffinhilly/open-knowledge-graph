---
id: log-rank-test
title: Log-Rank Test for Survival Comparison
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: survival-analysis-kaplan-meier
  type: hard
- id: hypothesis-testing-fundamentals
  type: hard
builds-toward:
- cox-proportional-hazards-detailed
tags:
- log-rank
- survival
- hypothesis-test
- chi-squared
stage: advanced
status: validated
---

# Log-Rank Test for Survival Comparison

## Core Idea
The log-rank test is a nonparametric hypothesis test that compares the survival distributions of two or more groups. At each observed event time, it compares the number of events in each group to the number expected under the null hypothesis that the survival curves are identical. The test statistic sums these observed-minus-expected differences across all event times and follows an approximate chi-squared distribution under the null. The log-rank test gives equal weight to all time points and is most powerful when the hazard ratio between groups is approximately constant over time (proportional hazards). When survival curves cross, the log-rank test may fail to detect a difference even when the groups clearly differ.

## Questions

```yaml
- question: "Two Kaplan-Meier survival curves for treatments A and B cross at 12 months — Treatment A is better early but Treatment B is better late. A log-rank test yields p = 0.42. A colleague concludes the treatments are equivalent. What is the problem?"
  type: multiple-choice
  options:
    - "The log-rank test lacks power to detect any difference — a larger sample is needed"
    - "The log-rank test averages the difference over time; when curves cross, the early advantage and late advantage cancel out, masking a real difference"
    - "The p-value of 0.42 definitively proves equivalence"
    - "The log-rank test only works for three or more groups"
  answer: 1
  explanation: "The log-rank test is designed to detect a consistent difference in survival (proportional hazards). When curves cross, one treatment is better early and the other better late — the positive and negative differences cancel, producing a small test statistic even though the treatments behave very differently. Alternative tests like the Wilcoxon (Breslow) test weight early events more heavily, or time-dependent analyses can explicitly model the crossing. A non-significant log-rank test with crossing curves does not mean equivalence — it means the test was inappropriate for that pattern."

- question: "The log-rank test compares observed to expected events at each event time. Under the null hypothesis, how are expected events computed?"
  type: multiple-choice
  options:
    - "Expected events equal the total events divided equally among groups"
    - "Expected events for each group are proportional to the number at risk in that group at each event time"
    - "Expected events are computed from a parametric survival distribution fitted to the combined data"
    - "Expected events are the historical rates from previous studies"
  answer: 1
  explanation: "Under the null hypothesis of identical survival, the probability of an event in any group is proportional to that group's share of the risk set. If 60 of 100 subjects at risk at time t are in Group A, and 3 events occur at that time, the expected number of events in Group A is 3 × (60/100) = 1.8. This is computed at every event time, and the observed-minus-expected differences are summed to form the test statistic. The approach is analogous to the Mantel-Haenszel method for combining 2×2 tables across strata."

- question: "The log-rank test requires the proportional hazards assumption — that the ratio of hazard rates between groups remains constant over time."
  type: true-false
  answer: true
  explanation: "The log-rank test is most powerful under proportional hazards because it gives equal weight to all event times. When the hazard ratio is constant, the cumulative difference between observed and expected events grows consistently over time, maximizing the test statistic. If hazards cross (one group has higher early hazard, the other higher late hazard), the contributions at different times cancel, reducing power. The log-rank test is valid under non-proportional hazards (the Type I error rate is still controlled), but it may fail to detect real differences — it is a question of power, not validity."

- question: "Explain what the log-rank test statistic measures and why it follows a chi-squared distribution."
  type: short-answer
  answer: "The test statistic sums the squared differences between observed and expected events in each group, divided by the variance of the expected events, across all event times. Under the null hypothesis that survival is identical across groups, the observed-minus-expected differences at each event time are approximately independent with known variance (from the hypergeometric distribution). By the central limit theorem, the sum of many such standardized differences converges to a chi-squared distribution with degrees of freedom equal to the number of groups minus one."
  explanation: "The construction is analogous to a Pearson chi-squared test applied repeatedly at each event time and summed. With two groups, the test statistic has 1 degree of freedom. With k groups, it has k-1 degrees of freedom. The hypergeometric distribution at each event time reflects the fact that the allocation of events to groups, given the total events and the risk set sizes, follows this distribution under the null."
```

## Explainer

The Kaplan-Meier estimator describes the survival experience of a single group, but the clinical question is usually comparative: is Treatment A better than Treatment B? Simply eyeballing two KM curves is not sufficient because apparent differences may be due to chance, especially with small samples or heavy censoring. The **log-rank test** provides a formal statistical framework for this comparison.

The test works by examining what happens at every observed event time across the combined sample. At each event time t_i, you know how many subjects are at risk in each group and how many events occurred. Under the null hypothesis that the groups have identical survival distributions, the expected number of events in each group is proportional to its share of the risk set at that moment. If Group A has 40 of 80 subjects at risk when 2 events occur, the expected number of events in Group A is 2 × (40/80) = 1. If both events actually occurred in Group A, the observed-minus-expected contribution at that time point is 2 - 1 = 1, suggesting Group A is doing worse than expected.

The test statistic sums these observed-minus-expected contributions across all event times and standardizes by the variance. Under the null hypothesis, the statistic follows a chi-squared distribution with k-1 degrees of freedom (where k is the number of groups). A large test statistic indicates that the observed event pattern deviates systematically from what equal survival would predict. The p-value then tells you how unlikely such a deviation would be under the null.

The log-rank test has an important limitation: it gives equal weight to all event times, making it most powerful when the **hazard ratio** (the ratio of instantaneous event rates) is constant over time — the proportional hazards assumption. When survival curves cross — one treatment is better early but the other is better late — the positive and negative contributions cancel, and the log-rank test may return a non-significant result despite a clear qualitative difference. In these situations, alternatives like weighted log-rank tests (which emphasize early or late differences) or tests designed for crossing hazards (e.g., the max-combo test) are more appropriate. The proportional hazards assumption is also foundational for the Cox regression model, which extends this framework to adjust for covariates.
