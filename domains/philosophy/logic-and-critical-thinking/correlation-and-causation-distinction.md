---
id: correlation-and-causation-distinction
title: Correlation and Causation Distinction
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: statistical-reasoning-basics
  type: hard
builds-toward:
- fallacy-detection-in-reasoning
- argument-evaluation-holistic
tags:
- causation
- correlation
- causal-reasoning
stage: abstract-reasoning
status: draft
---

# Correlation and Causation Distinction

## Core Idea
Two variables can be correlated (move together) without one causing the other. Confounding variables, reverse causation, or coincidence can explain correlations. Valid causal reasoning requires ruling out alternative explanations. Example: ice cream sales and drowning deaths correlate because both increase in summer, not because ice cream causes drowning.

## Common Misconceptions
Any strong correlation suggests causation (spurious correlations are common). Temporal order proves causation (even if X precedes Y, Z might cause both). Controlling for one variable proves there is no confounding (multiple confounders might still be at work). Correlation of zero means no relationship (nonlinear relationships produce zero linear correlation).

## Explainer

From statistical reasoning, you know that **correlation** measures the degree to which two variables move together — when one goes up, does the other tend to go up (positive correlation) or down (negative correlation)? Correlation is a purely statistical relationship between observed values. **Causation** is a different kind of claim: it says that changes in one variable *produce* changes in another, not merely that they co-vary. Understanding why these come apart is one of the most practically important skills in reasoning from data.

The classic illustration: ice cream sales and drowning deaths correlate strongly across months of the year. Both rise in summer, both fall in winter. Does eating ice cream cause drowning? Obviously not. The real explanation is a **confounding variable** — summer. Hot weather causes both more ice cream consumption and more swimming (which leads to more drowning). The correlation is genuine; the causal inference is wrong. A **confounder** is any third variable that independently influences both of the variables you're studying, creating a spurious association between them. Confounders are pervasive: wealth correlates with health, but socioeconomic status influences both; shoe size correlates with reading ability in children, but both are caused by age.

**Reverse causation** is another explanation for correlation that has nothing to do with the causal direction you assumed. Hospitals are full of sick people — is going to hospitals causing sickness? No: the sickness came first and caused the hospital visit. People with more police in their neighborhoods often have higher crime rates — does policing cause crime? Often the reverse: more crime attracts more police. Without an experiment or careful causal reasoning, observational data can't tell you which direction causation runs.

To establish causation rigorously, you need to rule out confounders and reverse causation. The gold standard is a **randomized controlled experiment**: you randomly assign subjects to treatment and control groups, eliminating systematic differences that could confound results. When randomization is impossible — in economics, epidemiology, history — researchers use **natural experiments**, **instrumental variables**, **difference-in-differences**, and other quasi-experimental designs that try to approximate random assignment. The point of all these methods is the same: isolate the effect of X on Y by holding everything else constant.

A useful mental habit: whenever you see a correlation reported in the media or a policy claim, ask three questions. (1) Could a confounding variable explain the pattern? (2) Could causation run in the opposite direction? (3) Could this be pure coincidence in a large dataset (spurious correlation)? The bar for claiming causation is much higher than the bar for observing correlation, and most real-world reasoning — in health, education, economics, and policy — fails to clear it.
