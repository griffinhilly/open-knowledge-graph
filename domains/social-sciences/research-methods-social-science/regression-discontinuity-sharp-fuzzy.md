---
id: regression-discontinuity-sharp-fuzzy
title: 'Regression Discontinuity: Sharp and Fuzzy Designs'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: natural-experiments-identification-strategy
  type: hard
- id: functions-domain-codomain-range
  type: soft
tags:
- regression-discontinuity
- rdd
- threshold
stage: advanced
status: draft
---

# Regression Discontinuity: Sharp and Fuzzy Designs

## Core Idea
Regression discontinuity designs exploit threshold rules in policy or eligibility. When treatment changes discontinuously at a cutoff (sharp RDD) or is affected by a running variable (fuzzy RDD), the discontinuity estimates local treatment effects. RDD requires no assumption about unconfoundedness away from the threshold.

## Explainer

From your study of natural experiments and identification strategies, you know the core challenge: we want to compare treated and untreated units who are otherwise identical, but treatment is rarely assigned randomly in the real world. Natural experiments exploit situations where assignment is "as-if" random due to features of the institutional environment. **Regression discontinuity design (RDD)** is one of the most compelling natural experiments — and it works by exploiting a threshold rule that determines treatment.

The intuition is simple. Suppose a scholarship program admits students who score 70 or above on an exam and rejects everyone below. Students who score 69 and 71 are nearly identical in ability, motivation, and background — they're separated by a single point that may reflect measurement noise as much as true ability. Yet one group gets the scholarship and the other doesn't. RDD treats this cutoff as a locally randomized experiment: right around the threshold, the treated (71+) and control (69−) groups are comparable, and any difference in outcomes is plausibly caused by the treatment. This is a **sharp RDD**: everyone above the cutoff receives treatment, everyone below does not, producing a step-function in treatment probability at the threshold.

The **running variable** is the variable that determines treatment assignment — in this case, exam score. The key identifying assumption is **continuity**: in the absence of treatment, the outcome would change smoothly across the threshold. We check this by plotting the outcome against the running variable on both sides of the cutoff — if the relationship is smooth everywhere except at the threshold, and there is a visible jump exactly at the cutoff, that jump is our estimate of the **local average treatment effect (LATE)** at the threshold. "Local" is crucial: RDD only identifies the treatment effect for units near the cutoff, not for all units. Whether this generalizes depends on your research question.

**Fuzzy RDD** applies when the threshold doesn't perfectly determine treatment — it only makes treatment more likely. Maybe some students below the cutoff get the scholarship through an appeal process; some above it decline it. Now treatment probability jumps at the cutoff but doesn't jump from 0 to 1. Fuzzy RDD estimates the treatment effect using the threshold as an **instrumental variable**: the discontinuity in treatment probability instruments for actual treatment receipt, recovering a LATE for "compliers" (those whose treatment status actually changed at the threshold). Two key threats to validity that you always check: **manipulation** (did people game the running variable to land just above the cutoff?) — tested by examining whether the density of the running variable is smooth at the threshold (McCrary test) — and **covariate smoothness** (do observable pre-treatment characteristics jump at the threshold? If so, the as-good-as-random assumption is violated).
