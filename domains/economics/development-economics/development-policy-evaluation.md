---
id: development-policy-evaluation
title: Development Policy Evaluation and Impact Assessment
domain: economics
course: development-economics
prerequisites:
- id: randomized-experiments-development-economics
  type: hard
- id: causal-inference-econometrics
  type: soft
tags:
- impact evaluation
- policy assessment
- methodology
- evidence
stage: advanced
status: draft
---

# Development Policy Evaluation and Impact Assessment

## Core Idea
Evaluating development policies requires isolating causal effects through RCTs, regression discontinuity, instrumental variables, or difference-in-differences. Each has strengths and limitations. Evidence-based development now requires rigorous evaluation, shifting policy from intuition toward empirical demonstration of what works, for whom, and at what cost.

## Explainer

From your work on randomized experiments in development economics, you know the gold standard for causal inference: randomly assign a program to some people and not others, then compare outcomes. But policy evaluation in development is broader than any single method. The core question is always the same — **what would have happened without the intervention?** — and the challenge is that we can never directly observe this counterfactual. Every evaluation method is a different strategy for constructing a credible comparison group.

**Randomized controlled trials (RCTs)** solve the comparison problem by design: random assignment ensures that treatment and control groups are statistically identical before the intervention, so any subsequent difference is caused by the program. But RCTs have real limitations. They are expensive and slow. They may not be ethical when the intervention is a basic right (you cannot randomly deny children vaccines). They measure average effects in a specific context, and what works in rural Kenya may not work in urban Bangladesh — this is the **external validity** problem. And some questions simply cannot be randomized: you cannot randomly assign countries to have different trade policies or institutional structures.

When randomization is impossible, economists turn to **quasi-experimental methods** that exploit natural variation. **Regression discontinuity** uses arbitrary cutoffs — a poverty program that serves households below a specific income threshold creates a natural experiment around that threshold, since households just above and just below are nearly identical. **Difference-in-differences** compares changes over time between a group affected by a policy and a group that was not, controlling for common trends. **Instrumental variables** use a source of variation that affects the treatment but has no direct effect on the outcome — for example, using distance to a school as an instrument for years of education. Each method requires specific assumptions, and the evaluator must argue convincingly that those assumptions hold.

The shift toward evidence-based policy has transformed development practice. Organizations like the World Bank and USAID now require impact evaluations for major programs. The key insight is not that RCTs are always best, but that **every policy claim implies a causal story**, and that story must be tested against data with an appropriate method. A well-designed quasi-experiment can be more informative than a poorly executed RCT. The evaluator's job is to match the method to the question, be transparent about assumptions, and report not just whether a program "worked" but **for whom, at what cost, and under what conditions** — because those details determine whether the program should be scaled, modified, or abandoned.
