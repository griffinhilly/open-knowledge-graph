---
id: quasi-experimental-non-randomized-designs
title: Quasi-Experimental Designs and Non-Randomized Comparisons
domain: psychology
course: research-methods-psychology
prerequisites:
- id: research-design-selection-and-matching
  type: hard
- id: true-experimental-randomized-designs
  type: soft
builds-toward:
- internal-validity-confounds-and-control
tags:
- quasi-experimental
- causal-inference-approximate
- non-equivalent-groups
stage: abstract-reasoning
status: draft
---

# Quasi-Experimental Designs and Non-Randomized Comparisons

## Core Idea
Quasi-experiments use non-equivalent control groups, interrupted time-series, or matched pairs to approximate causal inference when randomization is impossible or unethical. They sacrifice randomization's power to eliminate confounds but remain valuable when true experiments are infeasible. Statistical control and design logic partially compensate for lack of random assignment.

## How It's Best Learned
Compare a randomized and quasi-experimental study on similar questions. Identify the specific quasi-experimental design (e.g., interrupted time-series, regression discontinuity) and discuss threats it faces. Practice designing a quasi-experiment when randomization is ruled out.

## Common Misconceptions
- Quasi-experiments are weak science; - Matching groups before treatment equals randomization; - Quasi-experiments cannot contribute to causal inference; - All threats to internal validity are equally severe in quasi-experiments.

## Explainer

From your study of true experimental designs, you know that random assignment is the gold standard for causal inference — it equates groups on all confounds, known and unknown, before the treatment begins. But many of the most important causal questions in psychology cannot be answered with randomized experiments. You cannot randomly assign people to poverty, to childhood trauma, to being a member of a stigmatized group, or to receiving a mandatory policy intervention. **Quasi-experimental designs** are the toolkit researchers use when randomization is impossible, impractical, or unethical — not as a concession to poor science, but as a deliberate strategy for extracting causal signal from non-random data.

The most common quasi-experimental approach is the **non-equivalent control group design**: two groups are compared, one receiving treatment and one not, but group membership was not randomly determined. The critical question is always: were the groups similar enough before the treatment that post-treatment differences are attributable to the treatment rather than pre-existing differences? This is where selection bias becomes the central threat. Matching on observed characteristics (age, gender, prior test scores) reduces this threat but does not eliminate it — groups may differ on unmeasured variables that are correlated with both group membership and the outcome. This is why matched groups are not equivalent to randomly assigned groups: matching controls only what you can measure.

The **interrupted time-series design** is a more powerful quasi-experimental approach when longitudinal data exist. Rather than comparing two groups at one time point, it tracks a single group's trajectory before and after an intervention and asks: did the trend change at the moment of the intervention in ways inconsistent with the pre-existing trajectory? A new traffic safety law takes effect at a specific date — if traffic fatalities had been on a steady trend for years and then show an abrupt change at the law's implementation, the design provides compelling (though not definitive) causal evidence. The design's strength comes from using the group's own pre-intervention trend as the control condition.

The **regression discontinuity design** exploits sharp assignment cutoffs: applicants above a test score threshold receive a scholarship; those below do not. The key insight is that people just above and just below the threshold are essentially equivalent in ability and motivation — the cutoff creates local randomization near the threshold. Comparing outcomes for these near-threshold groups provides a credible causal estimate of the scholarship's effect. This design is highly regarded in economics and policy evaluation precisely because the assignment rule is known, measurable, and sharp. The quality of any quasi-experimental inference ultimately depends on the plausibility of the argument that the comparison group represents what the treatment group would have looked like without treatment — a claim that requires both design logic and empirical checks, not just an assumption.
