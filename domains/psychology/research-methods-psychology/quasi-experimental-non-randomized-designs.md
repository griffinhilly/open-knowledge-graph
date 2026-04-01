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
- id: quasi-experimental-designs-nonequivalent-groups
  type: soft
builds-toward:
- internal-validity-confounds-and-control
tags:
- quasi-experimental
- causal-inference-approximate
- non-equivalent-groups
stage: formal-systems
status: validated
---
# Quasi-Experimental Designs and Non-Randomized Comparisons

## Core Idea
Quasi-experiments use non-equivalent control groups, interrupted time-series, or matched pairs to approximate causal inference when randomization is impossible or unethical. They sacrifice randomization's power to eliminate confounds but remain valuable when true experiments are infeasible. Statistical control and design logic partially compensate for lack of random assignment.

## How It's Best Learned
Compare a randomized and quasi-experimental study on similar questions. Identify the specific quasi-experimental design (e.g., interrupted time-series, regression discontinuity) and discuss threats it faces. Practice designing a quasi-experiment when randomization is ruled out.

## Common Misconceptions
- Quasi-experiments are weak science; - Matching groups before treatment equals randomization; - Quasi-experiments cannot contribute to causal inference; - All threats to internal validity are equally severe in quasi-experiments.

## Questions

```yaml
- question: "A researcher matches 200 people who voluntarily enrolled in a job training program to 200 unemployed individuals on age, education level, and prior work history. After matching, she compares employment outcomes. What threat to causal inference persists despite the matching?"
  type: multiple-choice
  options:
    - "Unmeasured variables correlated with both program self-selection and employment outcomes may differ between groups"
    - "The matched sample is too small to draw meaningful conclusions about employment effects"
    - "Matching on too many variables inflates the probability of a Type I error"
    - "No threats remain — matching eliminates all pre-existing group differences, just like randomization"
  answer: 0
  explanation: "Matching controls only what you can measure and choose to match on. People who voluntarily enroll in job training may also be more motivated, have stronger social networks, or differ in dozens of other ways that predict employment but were never measured. These unmeasured confounds remain as selection bias even after matching. This is the core difference from random assignment, which equates groups on all confounds — known and unknown — simultaneously. Option D is the classic misconception this topic is designed to correct."

- question: "A university awards merit scholarships to applicants who score 1200 or above on an entrance exam and denies them to those who score below 1200. A researcher compares the graduation rates of students who scored 1199 versus 1201. Why does this comparison yield a credible causal estimate?"
  type: multiple-choice
  options:
    - "Students just above and just below the cutoff are essentially equivalent in ability, approximating local random assignment"
    - "The test score is randomly distributed across all applicants, making the cutoff effectively random"
    - "The scholarship was randomly assigned within each score group, creating true experimental conditions"
    - "All university applicants are similar enough that any cutoff comparison is internally valid"
  answer: 0
  explanation: "This is the regression discontinuity design's key insight: applicants who score 1199 vs. 1201 differ by essentially nothing in ability or preparation — the 2-point difference is within measurement noise. Yet one group received the scholarship and the other did not. Because the assignment rule is known, sharp, and based on a continuous variable, the near-threshold comparison mimics random assignment locally. This design is highly credible precisely because the arbitrary discontinuity creates a natural experiment, not because scores are randomly distributed or because all applicants are similar."

- question: "In an interrupted time-series design, a group's own pre-intervention trend serves as the control condition."
  type: true-false
  answer: true
  explanation: "This is the defining feature of the interrupted time-series design and the source of its strength. Rather than comparing a treated group to a separate (potentially non-equivalent) control group, the design tracks the same group's trajectory over many time points before the intervention and asks: did something change at the intervention point beyond what the pre-existing trend would predict? The group's own history is the counterfactual. This is why the design is more informative than a simple pre-post comparison with no control."

- question: "Quasi-experimental designs cannot contribute meaningfully to causal inference — mainly true randomized experiments can establish causation."
  type: true-false
  answer: false
  explanation: "This is the most damaging misconception about quasi-experimental methods. Well-designed quasi-experiments — particularly regression discontinuity and interrupted time-series designs — can provide highly credible causal evidence. Many of the most important causal questions (effects of policies, early childhood poverty, educational interventions) cannot be studied with randomized experiments for ethical or practical reasons. Quasi-experiments are not a concession to weak science; they are a principled toolkit for extracting causal signal when randomization is impossible. The quality of inference depends on the plausibility of the design argument, not on whether randomization occurred."

- question: "Why is matching participants on observable characteristics not equivalent to random assignment, even when matching is done carefully on many variables?"
  type: short-answer
  answer: "Matching controls only variables that were measured and selected for matching. Random assignment equates groups on all confounds simultaneously — including variables the researcher never thought to measure or cannot measure. Matched groups can still differ systematically on unmeasured characteristics correlated with both group membership and the outcome, which is the definition of selection bias. Since researchers can only match on what they observe, unobserved confounds remain as threats to causal inference. Random assignment solves this problem by making group membership probabilistically independent of all background characteristics, observed or not."
  explanation: "This distinction is the central reason quasi-experiments have lower internal validity than true experiments. The residual threat from unobserved confounds is why quasi-experimental studies typically require stronger design logic, empirical checks (e.g., parallel pre-trends), and theoretical arguments to be convincing about causal claims. The insight that 'matching controls only what you measure' is the key to understanding the limits of quasi-experimental inference."
```

## Explainer

From your study of true experimental designs, you know that random assignment is the gold standard for causal inference — it equates groups on all confounds, known and unknown, before the treatment begins. But many of the most important causal questions in psychology cannot be answered with randomized experiments. You cannot randomly assign people to poverty, to childhood trauma, to being a member of a stigmatized group, or to receiving a mandatory policy intervention. **Quasi-experimental designs** are the toolkit researchers use when randomization is impossible, impractical, or unethical — not as a concession to poor science, but as a deliberate strategy for extracting causal signal from non-random data.

The most common quasi-experimental approach is the **non-equivalent control group design**: two groups are compared, one receiving treatment and one not, but group membership was not randomly determined. The critical question is always: were the groups similar enough before the treatment that post-treatment differences are attributable to the treatment rather than pre-existing differences? This is where selection bias becomes the central threat. Matching on observed characteristics (age, gender, prior test scores) reduces this threat but does not eliminate it — groups may differ on unmeasured variables that are correlated with both group membership and the outcome. This is why matched groups are not equivalent to randomly assigned groups: matching controls only what you can measure.

The **interrupted time-series design** is a more powerful quasi-experimental approach when longitudinal data exist. Rather than comparing two groups at one time point, it tracks a single group's trajectory before and after an intervention and asks: did the trend change at the moment of the intervention in ways inconsistent with the pre-existing trajectory? A new traffic safety law takes effect at a specific date — if traffic fatalities had been on a steady trend for years and then show an abrupt change at the law's implementation, the design provides compelling (though not definitive) causal evidence. The design's strength comes from using the group's own pre-intervention trend as the control condition.

The **regression discontinuity design** exploits sharp assignment cutoffs: applicants above a test score threshold receive a scholarship; those below do not. The key insight is that people just above and just below the threshold are essentially equivalent in ability and motivation — the cutoff creates local randomization near the threshold. Comparing outcomes for these near-threshold groups provides a credible causal estimate of the scholarship's effect. This design is highly regarded in economics and policy evaluation precisely because the assignment rule is known, measurable, and sharp. The quality of any quasi-experimental inference ultimately depends on the plausibility of the argument that the comparison group represents what the treatment group would have looked like without treatment — a claim that requires both design logic and empirical checks, not just an assumption.
