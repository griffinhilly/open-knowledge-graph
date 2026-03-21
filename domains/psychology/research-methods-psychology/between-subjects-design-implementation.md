---
id: between-subjects-design-implementation
title: Between-Subjects Design Implementation and Assignment
domain: psychology
course: research-methods-psychology
prerequisites:
- id: control-and-experimental-groups
  type: soft
builds-toward:
- within-subjects-design-implementation
- mixed-factorial-designs
- internal-validity-and-threats
tags:
- design
- experimental
- assignment
stage: formal-systems
status: draft
---

# Between-Subjects Design Implementation and Assignment

## Core Idea
Between-subjects designs assign different participants to different experimental conditions, allowing comparison of independent groups on outcome measures. This design requires random assignment to minimize selection bias and ensures differences between groups reflect experimental effects rather than pre-existing individual differences. However, it requires more participants than within-subjects designs due to higher error variance.

## How It's Best Learned
Implement random assignment using computerized randomizers, random number tables, or block randomization. Examine baseline equivalence by comparing groups on demographic variables and pretest measures using t-tests or chi-square tests (non-significant differences support successful randomization). Discuss efficiency trade-offs: more conditions require more participants but avoid practice effects.

## Common Misconceptions
- Matching participants on variables improves random assignment; true random assignment is superior because it controls for all variables simultaneously.
- You can verify successful randomization after seeing data; randomization must be completed before data collection regardless of subsequent group equivalence.
- Between-subjects designs are weaker than within-subjects designs; they provide strong internal validity when properly randomized.

## Questions

```yaml
- question: "A researcher studies the effect of sleep deprivation on memory. She matches participants into pairs based on their baseline memory scores, then assigns one member of each pair to the sleep-deprived condition and the other to the control. A colleague argues they should use simple random assignment instead. Why is the colleague correct?"
  type: multiple-choice
  options:
    - "Matching on baseline memory automatically improves statistical power beyond what randomization can achieve"
    - "Random assignment controls for all confounding variables simultaneously — including ones the researcher hasn't measured — while matching only controls for the variables explicitly matched on"
    - "Matching is only valid in within-subjects designs; between-subjects designs prohibit it"
    - "The colleague is wrong; matching is always superior to random assignment for controlling confounds"
  answer: 1
  explanation: "Matching controls for variables you know about and think to measure (here, baseline memory). But it leaves uncontrolled all the other variables that differ between participants — motivation, sleep history, health, personality, etc. Random assignment, by the law of large numbers, equates groups on ALL variables simultaneously, including those the researcher hasn't thought to measure. This is the unique power of randomization: it turns a designed experiment into a causal inference engine."

- question: "Why do between-subjects designs typically require more participants than within-subjects designs to achieve the same statistical power?"
  type: multiple-choice
  options:
    - "Between-subjects designs use less efficient statistical tests that require larger samples"
    - "Between-subjects designs require a separate control group, which doubles the required sample size"
    - "Individual differences between participants add error variance to group comparisons, making it harder to detect real treatment effects without a larger sample"
    - "Between-subjects designs measure each participant only once, which always reduces reliability"
  answer: 2
  explanation: "In a between-subjects design, the groups differ not only because of the treatment but also because people differ from one another in baseline performance, personality, and countless other variables. This between-person variability is part of the error variance in the statistical test, making real treatment effects harder to distinguish from noise. Within-subjects designs eliminate this source of variance by having each participant serve as their own control. The solution in between-subjects designs is a larger sample, which dilutes individual differences."

- question: "Random assignment to conditions in a between-subjects experiment controls for confounding variables even when those variables were not measured or anticipated by the researcher."
  type: true-false
  answer: true
  explanation: "This is the central advantage of random assignment. Because participants are assigned to conditions by chance, any variable that might correlate with the outcome — measured or unmeasured, anticipated or not — is equally likely to end up distributed across both groups. Over a large sample, this ensures group equivalence on all characteristics simultaneously. This is why true experiments (with random assignment) permit causal inference in a way that observational studies and quasi-experiments cannot."

- question: "Between-subjects designs are inherently weaker than within-subjects designs in terms of internal validity when both are properly conducted."
  type: true-false
  answer: false
  explanation: "Internal validity — the degree to which observed differences can be attributed to the independent variable — is determined primarily by random assignment, not by design type. A properly randomized between-subjects design has strong internal validity. Within-subjects designs have different threats (carryover effects, practice effects, order effects) that can compromise internal validity in their own way. The tradeoff is in statistical power and sample size, not in internal validity. Neither design is inherently superior on that dimension."

- question: "Explain why random assignment is considered more powerful than matching participants on key variables, even when matching is done carefully on variables known to correlate with the outcome."
  type: short-answer
  answer: "Matching controls only for the variables the researcher explicitly identifies and measures. But countless unmeasured variables — motivation, personality, genetics, health, mood — also affect outcomes. Random assignment, because it assigns by chance, equates groups on ALL such variables simultaneously through probability, including ones the researcher hasn't thought to measure or couldn't measure. Matching also risks creating inadvertent systematic differences on unmatched variables. Random assignment is therefore a more comprehensive and assumption-free method of achieving group equivalence."
  explanation: "The intuition is that matching is a targeted tool (it fixes specific known problems) while randomization is a universal tool (it addresses all problems at once, known and unknown). In practice, researchers sometimes combine them — using stratified randomization to ensure balance on the most important variables while relying on probability to handle the rest."
```

## Explainer

From your prerequisite on control and experimental groups, you understand the basic logic: you manipulate the independent variable, hold everything else constant, and compare outcomes. The **between-subjects design** implements that logic by assigning different participants to each condition — one group receives the treatment, another does not, and you compare the groups on the outcome measure. The fundamental challenge is ensuring the groups are comparable *before* the manipulation, so that any difference in outcomes afterward can be attributed to the treatment and not to pre-existing differences between people.

**Random assignment** is the gold-standard solution. If you randomly assign 100 participants to two groups of 50, probability theory ensures the groups will be equivalent, on average, on *all* characteristics simultaneously — not just the ones you thought to measure, but also personality, motivation, mood, and any other variable that could confound the result. This is the unique power of randomization: it doesn't require you to enumerate every possible confound. It controls for them all at once, including the ones you haven't thought of. This is precisely what makes a study a true experiment rather than a quasi-experiment or observational study.

Implementing random assignment well matters in practice. Simple coin-flip randomization works but can produce accidentally lopsided groups in smaller samples. **Block randomization** guarantees equal group sizes as the study progresses: participants are assigned in fixed-size blocks (e.g., every four participants, two go to each condition), preventing gradual drift. When a key variable is known to correlate strongly with the outcome, **stratified randomization** — randomizing separately within subgroups (e.g., by sex, diagnostic status) — ensures those subgroups are balanced across conditions.

The cost of the between-subjects design is statistical power. Because different people are in different conditions, between-person variability in baseline performance adds noise to the group comparison — the groups differ both because of the treatment and because people are different from one another. This **error variance** makes real treatment effects harder to detect. The standard solution is a larger sample, which dilutes the impact of individual differences. This is the explicit trade-off: between-subjects designs avoid carryover effects and order effects (problems that plague within-subjects designs) at the cost of needing more participants to achieve equivalent sensitivity. Knowing this trade-off allows you to make it deliberately rather than by accident.
