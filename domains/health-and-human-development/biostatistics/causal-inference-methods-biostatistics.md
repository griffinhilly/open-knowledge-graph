---
id: causal-inference-methods-biostatistics
title: Causal Inference Methods in Biostatistics
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: study-design-biostatistics
  type: hard
- id: logistic-regression-biostatistics
  type: hard
- id: cox-proportional-hazards-detailed
  type: soft
builds-toward:
- propensity-score-methods-biostatistics
- instrumental-variables-biostatistics
- difference-in-differences-biostatistics
tags:
- causal-inference
- counterfactual
- potential-outcomes
- confounding
- DAG
- SUTVA
stage: expert
status: validated
---

# Causal Inference Methods in Biostatistics

## Core Idea
Causal inference in biostatistics formalizes the question "does X cause Y?" using the potential outcomes framework (Rubin causal model): each subject has a potential outcome under treatment Y(1) and under control Y(0), but only one is observed — the fundamental problem of causal inference. The average treatment effect (ATE) is E[Y(1) - Y(0)]. In randomized trials, randomization ensures that observed treatment groups estimate potential outcomes without bias. In observational studies, confounding (common causes of treatment and outcome) prevents direct causal interpretation. Causal inference methods — propensity scores, instrumental variables, difference-in-differences, regression discontinuity — each address confounding under different assumptions. Directed acyclic graphs (DAGs) provide a visual language for encoding causal assumptions and identifying what must be adjusted for to estimate causal effects.

## Questions

```yaml
- question: "The fundamental problem of causal inference states that we can never observe both potential outcomes for the same individual. Why does randomization solve this problem at the population level even though it cannot solve it at the individual level?"
  type: multiple-choice
  options:
    - "Randomization ensures every individual is observed under both conditions"
    - "Randomization ensures that the treatment and control groups are, on average, exchangeable — the treated group's observed outcomes estimate Y(1) for the population, and the control group's observed outcomes estimate Y(0), because assignment is independent of potential outcomes"
    - "Randomization eliminates all confounders including those that cannot be measured"
    - "Both B and C"
  answer: 3
  explanation: "Both B and C are correct and describe the same mechanism from different angles. Randomization makes treatment assignment independent of all subject characteristics (measured and unmeasured), ensuring exchangeability — the treated group is a random sample of the population's Y(1) values and the control group is a random sample of Y(0) values. This solves the problem at the group level (we can estimate E[Y(1)] and E[Y(0)] separately) even though each individual is only observed under one condition."

- question: "A directed acyclic graph (DAG) shows that Socioeconomic Status (SES) causes both Exercise (treatment) and Heart Disease (outcome). A researcher adjusts for SES in a regression. According to the DAG, is this sufficient to identify the causal effect of Exercise on Heart Disease?"
  type: multiple-choice
  options:
    - "Yes, if SES is the only confounder — adjusting for it blocks the backdoor path from Exercise to Heart Disease through SES"
    - "No — adjusting for confounders is never sufficient in observational data"
    - "Yes, but only if Exercise is randomized"
    - "No — you should also adjust for all variables in the dataset"
  answer: 0
  explanation: "The backdoor criterion from DAG theory states that the causal effect is identified if all backdoor paths (non-causal paths from treatment to outcome) are blocked by conditioning on a sufficient set of variables. If SES is the only confounder, adjusting for it blocks the only backdoor path Exercise ← SES → Heart Disease, and the remaining association is causal. DAGs make the no-unmeasured-confounders assumption explicit and help determine the minimum sufficient adjustment set — adjusting for everything is actually harmful if it includes colliders or mediators."

- question: "Adjusting for a collider (a variable caused by both treatment and outcome) in a regression introduces bias rather than removing it."
  type: true-false
  answer: true
  explanation: "A collider is a variable that is caused by both the treatment and the outcome (or by causes of each). Conditioning on a collider opens a spurious path between treatment and outcome that was not present before adjustment. This is called collider bias or Berkson's bias. For example, if both Exercise and Heart Disease independently affect Hospital Admission (a collider), conditioning on hospitalization creates a spurious negative association between exercise and heart disease among hospitalized patients. DAGs reveal this: a path Treatment → Collider ← Outcome is blocked by default but opened by conditioning on the collider."

- question: "Explain the SUTVA (Stable Unit Treatment Value Assumption) and give a biostatistical example of when it would be violated."
  type: short-answer
  answer: "SUTVA requires that (1) each subject's potential outcome depends only on their own treatment, not on other subjects' treatments (no interference), and (2) there is only one version of each treatment level (no hidden variations). It is violated in vaccination studies: an unvaccinated person's probability of infection depends on how many of their contacts are vaccinated (herd immunity), so one person's treatment assignment affects another person's outcome. It is also violated if the 'same' drug is administered at different doses, by different routes, or with different compliance levels across study sites."
  explanation: "SUTVA violations are common in infectious disease, cluster-randomized trials, and social network studies. When interference is present, the potential outcomes notation Y_i(1) and Y_i(0) is insufficient — the potential outcome depends on the full treatment vector of all subjects, not just the individual's assignment. Methods for handling interference include cluster-randomized designs and interference-aware estimands."
```

## Explainer

The goal of causal inference is to determine whether a treatment or exposure causes a change in an outcome — not merely whether the two are associated. From your study of study design, you know that randomized experiments provide the strongest evidence for causation. The potential outcomes framework explains why: each subject has two potential outcomes, Y(1) under treatment and Y(0) under control. The causal effect for that individual is Y(1) - Y(0). The "fundamental problem of causal inference" is that we observe only one of these — a person either receives the treatment or does not, never both simultaneously.

Randomization solves this at the population level by ensuring that the group of treated subjects is a representative sample of the population's Y(1) values, and the control group samples Y(0). The difference in group means estimates the **Average Treatment Effect** (ATE): E[Y(1)] - E[Y(0)]. This works because random assignment makes treatment independent of all patient characteristics — measured and unmeasured — eliminating confounding.

In observational studies, treatment is not randomly assigned — patients who receive a treatment may differ systematically from those who do not. **Confounders** (variables that cause both treatment and outcome) create spurious associations. **Directed acyclic graphs** (DAGs) provide a rigorous visual language for representing causal relationships and identifying what must be controlled for. The **backdoor criterion** states that the causal effect of X on Y is identified if you condition on a set of variables that blocks all backdoor paths (non-causal paths from X to Y through confounders). DAGs also reveal what you should not condition on: **colliders** (variables caused by both treatment and outcome), which introduce bias when conditioned upon, and **mediators** (variables on the causal path from treatment to outcome), which absorb the very effect you are trying to estimate.

The various causal inference methods — propensity scores, instrumental variables, difference-in-differences, regression discontinuity — each address confounding under different assumptions about which variables are observed and how treatment assignment works. No method eliminates the need for assumptions; each makes different untestable assumptions transparent. Propensity scores assume no unmeasured confounders. Instrumental variables assume the existence of a variable that affects treatment but not outcome directly. Difference-in-differences assumes parallel trends. The choice of method depends on the data structure and the plausibility of its specific assumptions.
