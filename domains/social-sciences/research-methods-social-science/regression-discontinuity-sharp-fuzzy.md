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

## Questions

```yaml
- question: "A city gives housing vouchers to all families scoring below 50 on a needs index. A researcher compares outcomes for families scoring 48–52 and finds they are similar on all observable characteristics. She estimates a 15% improvement in children's educational outcomes from the voucher. What can she validly conclude?"
  type: multiple-choice
  options:
    - "Housing vouchers cause a 15% improvement in educational outcomes on average across all eligible families"
    - "Housing vouchers cause a 15% improvement in outcomes for families near the needs-index cutoff of 50"
    - "Housing vouchers cause a 15% improvement for the most disadvantaged families who scored well below 40"
    - "The voucher program is cost-effective and should be expanded to all low-income families based on this evidence"
  answer: 1
  explanation: "RDD is inherently a *local* estimator — it identifies the treatment effect for units near the threshold, not for the full distribution of treated units. Families near the cutoff of 50 may respond to housing vouchers very differently from families scoring 20 or 30, who face much more severe deprivation and may have different constraints. The 15% finding cannot be extrapolated to these populations. Options A, C, and D all commit the error of generalizing beyond the local window the design supports."

- question: "In a fuzzy RDD, the threshold for treatment eligibility is used as an instrumental variable. What property of the threshold makes it a valid instrument for treatment receipt?"
  type: multiple-choice
  options:
    - "It perfectly determines treatment receipt, eliminating any measurement error in the assignment process"
    - "It creates a discontinuous jump in treatment *probability* at the threshold while having no direct effect on the outcome except through treatment"
    - "It ensures that all individuals on both sides of the threshold have identical observable characteristics"
    - "It eliminates all selection bias by removing variation in the running variable near the cutoff"
  answer: 1
  explanation: "A valid instrument must (1) affect treatment receipt (relevance) and (2) affect the outcome only through treatment, not directly (exclusion restriction). The threshold satisfies both: crossing it makes treatment more likely (relevance), and being just above vs. just below the threshold has no direct causal effect on the outcome — it only matters insofar as it affects whether someone receives treatment. This is analogous to a standard IV design, with the discontinuity serving as the exogenous variation that assigns treatment."

- question: "In a sharp RDD, if students can retake an exam until they cross the admission threshold, the design's validity is preserved as long as the discontinuity in outcomes is still visible at the cutoff."
  type: true-false
  answer: false
  explanation: "Manipulation of the running variable — gaming the cutoff — destroys the key assumption that units just above and below the threshold are comparable. Students who retake tests until they barely cross the cutoff are systematically different from those who didn't: they had more motivation, more resources (tutoring, test-prep), or more information about the threshold. The discontinuity in outcomes may remain visible, but it now reflects these pre-existing differences as well as the treatment effect, making causal inference invalid."

- question: "In a regression discontinuity design, a researcher should check whether observable pre-treatment covariates also jump discontinuously at the threshold; such a jump would undermine the causal interpretation of the outcome discontinuity."
  type: true-false
  answer: true
  explanation: "Pre-treatment covariate smoothness is a key validity check in RDD. If the treatment is truly as-good-as-random at the threshold, units just above and below should be similar on everything except treatment receipt — including characteristics measured before treatment assignment. A jump in baseline covariates at the threshold signals that the groups differ systematically (perhaps due to manipulation or a policy change that coincides with the cutoff), and the outcome jump can no longer be attributed solely to treatment."

- question: "Why is the treatment effect estimated by RDD described as 'local,' and what does this imply for generalizing findings to policy contexts beyond the threshold?"
  type: short-answer
  answer: "RDD identifies the average treatment effect only for units near the cutoff — those whose treatment status is most directly influenced by the threshold rule. Units far from the cutoff may differ systematically in characteristics that moderate treatment response. A scholarship effect estimated at a score cutoff of 70 cannot be assumed to apply to students scoring 50 (who face greater disadvantage) or 90 (who face fewer barriers). Generalization requires either theoretical arguments that the threshold population is representative or additional evidence from other designs."
  explanation: "The locality of RDD is both its strength and its limitation. Its strength is credibility: near the threshold, assignment is as-if random, so causal inference is clean. Its limitation is external validity: the people near the threshold are often marginal cases — just barely eligible or ineligible — and may not be the primary target population for the policy. Policymakers should understand they are learning about the effect on the margin, not the average."
```

## Explainer

From your study of natural experiments and identification strategies, you know the core challenge: we want to compare treated and untreated units who are otherwise identical, but treatment is rarely assigned randomly in the real world. Natural experiments exploit situations where assignment is "as-if" random due to features of the institutional environment. **Regression discontinuity design (RDD)** is one of the most compelling natural experiments — and it works by exploiting a threshold rule that determines treatment.

The intuition is simple. Suppose a scholarship program admits students who score 70 or above on an exam and rejects everyone below. Students who score 69 and 71 are nearly identical in ability, motivation, and background — they're separated by a single point that may reflect measurement noise as much as true ability. Yet one group gets the scholarship and the other doesn't. RDD treats this cutoff as a locally randomized experiment: right around the threshold, the treated (71+) and control (69−) groups are comparable, and any difference in outcomes is plausibly caused by the treatment. This is a **sharp RDD**: everyone above the cutoff receives treatment, everyone below does not, producing a step-function in treatment probability at the threshold.

The **running variable** is the variable that determines treatment assignment — in this case, exam score. The key identifying assumption is **continuity**: in the absence of treatment, the outcome would change smoothly across the threshold. We check this by plotting the outcome against the running variable on both sides of the cutoff — if the relationship is smooth everywhere except at the threshold, and there is a visible jump exactly at the cutoff, that jump is our estimate of the **local average treatment effect (LATE)** at the threshold. "Local" is crucial: RDD only identifies the treatment effect for units near the cutoff, not for all units. Whether this generalizes depends on your research question.

**Fuzzy RDD** applies when the threshold doesn't perfectly determine treatment — it only makes treatment more likely. Maybe some students below the cutoff get the scholarship through an appeal process; some above it decline it. Now treatment probability jumps at the cutoff but doesn't jump from 0 to 1. Fuzzy RDD estimates the treatment effect using the threshold as an **instrumental variable**: the discontinuity in treatment probability instruments for actual treatment receipt, recovering a LATE for "compliers" (those whose treatment status actually changed at the threshold). Two key threats to validity that you always check: **manipulation** (did people game the running variable to land just above the cutoff?) — tested by examining whether the density of the running variable is smooth at the threshold (McCrary test) — and **covariate smoothness** (do observable pre-treatment characteristics jump at the threshold? If so, the as-good-as-random assumption is violated).
