---
id: true-experimental-randomized-designs
title: True Experimental Design and Randomization
domain: psychology
course: research-methods-psychology
prerequisites:
- id: research-design-selection-and-matching
  type: hard
builds-toward:
- internal-validity-confounds-and-control
- statistical-power-and-effect-size-determination
tags:
- experimental-design
- randomization
- causal-inference
stage: abstract-reasoning
status: draft
---

# True Experimental Design and Randomization

## Core Idea
True experiments have three defining features: manipulation of an independent variable, random assignment to conditions, and measurement of the dependent variable. Random assignment ensures groups are equivalent before manipulation, allowing causal inference because confounding variables are equally distributed across conditions. The logic is probabilistic, not deterministic.

## How It's Best Learned
Design a true experiment from scratch, specifying the IV, DV, random assignment procedure, and control/treatment groups. Review examples showing how randomization protects against confounds. Compare randomized vs. non-randomized studies on the same topic.

## Common Misconceptions
- Random assignment requires truly 'random' coin flips; - Randomization guarantees groups are identical; - All psychology research can be ethically randomized; - Randomization eliminates the need for statistical testing.

## Explainer

Research design selection, your prerequisite, introduced the landscape of strategies for establishing causal relationships. The core challenge is always confounding: when you observe that A is associated with B, a third variable C might be causing both, making it look like A causes B when it does not. The **true experiment** solves this problem more decisively than any other design, and its mechanism is **random assignment** — not random sampling of participants from a population, but random *allocation* of participants to conditions.

The three defining features form a logical unit. **Manipulation** means the researcher actively controls which level of the independent variable each participant receives — a treatment or placebo, a high or low stimulus, an intervention or standard care. Without manipulation, you are observing what naturally exists rather than creating a controlled contrast. **Random assignment** means that which condition a participant enters is determined by a chance procedure — not by participant preference, researcher judgment, or any systematic factor. **Measurement** of the dependent variable then captures outcomes in both conditions, and any difference is attributed to the manipulation.

Random assignment's power comes from probability theory. Before the manipulation begins, the groups are equivalent in expectation across *all* variables — not just the ones you measured and controlled for, but every possible confound, including variables you didn't think to measure and variables you don't even know exist. Participant intelligence, socioeconomic background, prior experience, personality, and thousands of other factors are distributed approximately equally across conditions by chance. Any subsequent difference in outcomes can therefore be attributed to the manipulation itself. This is why experiments, and only experiments, straightforwardly support **causal inference**: you know the groups were comparable before the treatment; differences after treatment must be due to the treatment.

The critical nuance is that randomization is probabilistic, not a guarantee. With small samples, random allocation will leave some imbalance between conditions — this is why statistical testing remains necessary even in randomized experiments. The test does not check whether the manipulation worked; it checks whether the observed difference between conditions is larger than what chance variation alone would produce. A second important limit is ethical: you cannot randomly assign people to childhood poverty, trauma exposure, childhood abuse, or many other variables of psychological interest. These constraints force quasi-experimental and observational designs, which approximate experimental logic through matching, regression adjustment, or natural experiments. Understanding the true experiment is essential precisely because it defines the gold standard against which every other design's limitations are measured.
