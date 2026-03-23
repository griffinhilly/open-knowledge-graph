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
stage: formal-systems
status: validated
---

# True Experimental Design and Randomization

## Core Idea
True experiments have three defining features: manipulation of an independent variable, random assignment to conditions, and measurement of the dependent variable. Random assignment ensures groups are equivalent before manipulation, allowing causal inference because confounding variables are equally distributed across conditions. The logic is probabilistic, not deterministic.

## How It's Best Learned
Design a true experiment from scratch, specifying the IV, DV, random assignment procedure, and control/treatment groups. Review examples showing how randomization protects against confounds. Compare randomized vs. non-randomized studies on the same topic.

## Common Misconceptions
- Random assignment requires truly 'random' coin flips; - Randomization guarantees groups are identical; - All psychology research can be ethically randomized; - Randomization eliminates the need for statistical testing.

## Questions

```yaml
- question: "A researcher randomly assigns 80 participants to a meditation condition or a control condition to test whether meditation reduces anxiety. A critic notes she never measured participants' prior meditation experience. Is this a valid concern?"
  type: multiple-choice
  options:
    - "Yes — without measuring prior experience, it could confound the results and invalidate the study"
    - "No — random assignment distributes prior experience approximately equally across conditions, so it is controlled for even without being measured"
    - "Yes — any unmeasured variable is a fatal flaw in a true experiment"
    - "No — prior experience is irrelevant because both groups still received the same instructions"
  answer: 1
  explanation: "This is the key insight of randomization. Because participants were randomly assigned, prior meditation experience — along with every other variable, measured or not — is distributed approximately equally across conditions by chance. The critic's concern would be valid in a non-randomized study, but random assignment controls for all confounds simultaneously, including variables the researcher never thought to measure."

- question: "What is the critical distinction between 'random sampling' and 'random assignment'?"
  type: multiple-choice
  options:
    - "Random sampling determines which condition participants enter; random assignment determines who is recruited for the study"
    - "Random sampling selects who participates in the study from a population; random assignment determines which condition participants are placed into"
    - "They are equivalent procedures applied at different stages of analysis"
    - "Random assignment is used in observational studies; random sampling is used in true experiments"
  answer: 1
  explanation: "Random sampling (drawing a representative sample from a population) is about external validity — generalizing results to the broader population. Random assignment (allocating participants to conditions by chance) is about internal validity — ensuring groups are equivalent before manipulation so that differences in outcomes can be attributed to the treatment. A study can have one without the other."

- question: "Randomization in a true experiment guarantees that the experimental and control groups are identical on all variables before the treatment begins."
  type: true-false
  answer: false
  explanation: "Randomization ensures group equivalence in expectation — on average, across many replications. With any finite sample, chance variation will leave some imbalance between groups. This is especially true with small samples, which is why statistical testing is still necessary even in randomized experiments: the test checks whether the observed difference between conditions exceeds what random variation alone would produce."

- question: "Only true experiments with random assignment can straightforwardly support causal inference, because only randomization ensures that groups were equivalent before the treatment was administered."
  type: true-false
  answer: true
  explanation: "In a randomized experiment, the groups are equivalent in expectation across all variables — including unmeasured ones — before manipulation begins. Any subsequent difference in outcomes can therefore be attributed to the treatment. Non-randomized designs (quasi-experiments, observational studies) must use matching, regression adjustment, or other techniques to approximate this equivalence, but they can never be certain they've controlled for all confounds."

- question: "Why does random assignment allow causal inference in ways that non-randomized designs cannot, even when those designs carefully measure and statistically control for many known confounding variables?"
  type: short-answer
  answer: "Random assignment controls for all confounders simultaneously — including unmeasured and unknown ones — by distributing them equally across conditions by chance. Non-randomized designs can only control for confounders the researcher identifies and measures. There may always be additional unmeasured variables driving the observed association, so non-randomized designs cannot rule out alternative explanations in the way a randomized experiment can."
  explanation: "This is the gold-standard logic of the true experiment. No matter how carefully a non-randomized study measures and adjusts for confounds, a critic can always point to an unmeasured variable that might explain the result. Random assignment eliminates this objection: before treatment, the groups were equivalent by design — not by assumption or measurement."
```

## Explainer

Research design selection, your prerequisite, introduced the landscape of strategies for establishing causal relationships. The core challenge is always confounding: when you observe that A is associated with B, a third variable C might be causing both, making it look like A causes B when it does not. The **true experiment** solves this problem more decisively than any other design, and its mechanism is **random assignment** — not random sampling of participants from a population, but random *allocation* of participants to conditions.

The three defining features form a logical unit. **Manipulation** means the researcher actively controls which level of the independent variable each participant receives — a treatment or placebo, a high or low stimulus, an intervention or standard care. Without manipulation, you are observing what naturally exists rather than creating a controlled contrast. **Random assignment** means that which condition a participant enters is determined by a chance procedure — not by participant preference, researcher judgment, or any systematic factor. **Measurement** of the dependent variable then captures outcomes in both conditions, and any difference is attributed to the manipulation.

Random assignment's power comes from probability theory. Before the manipulation begins, the groups are equivalent in expectation across *all* variables — not just the ones you measured and controlled for, but every possible confound, including variables you didn't think to measure and variables you don't even know exist. Participant intelligence, socioeconomic background, prior experience, personality, and thousands of other factors are distributed approximately equally across conditions by chance. Any subsequent difference in outcomes can therefore be attributed to the manipulation itself. This is why experiments, and only experiments, straightforwardly support **causal inference**: you know the groups were comparable before the treatment; differences after treatment must be due to the treatment.

The critical nuance is that randomization is probabilistic, not a guarantee. With small samples, random allocation will leave some imbalance between conditions — this is why statistical testing remains necessary even in randomized experiments. The test does not check whether the manipulation worked; it checks whether the observed difference between conditions is larger than what chance variation alone would produce. A second important limit is ethical: you cannot randomly assign people to childhood poverty, trauma exposure, childhood abuse, or many other variables of psychological interest. These constraints force quasi-experimental and observational designs, which approximate experimental logic through matching, regression adjustment, or natural experiments. Understanding the true experiment is essential precisely because it defines the gold standard against which every other design's limitations are measured.
