---
id: mixed-factorial-designs
title: 'Mixed-Factorial Designs: Between and Within Factors'
domain: psychology
course: research-methods-psychology
prerequisites:
- id: between-subjects-design-implementation
  type: hard
- id: within-subjects-design-implementation
  type: hard
builds-toward:
- interaction-effects-and-moderation-psychology
tags:
- design
- factorial
- interaction
stage: formal-systems
status: draft
---

# Mixed-Factorial Designs: Between and Within Factors

## Core Idea
Mixed designs examine how effects of one factor (e.g., treatment condition) vary across levels of another factor (e.g., time or individual differences). They provide statistical efficiency and rich information but require understanding of interaction effects and threaten validity when between-groups differences interact with within-subject order or learning effects.

## How It's Best Learned
Sketch designs using 2×3 matrices (rows = between factor, columns = within factor) to visualize structure. Practice interpreting two-way interactions: does the effect of time differ by group? Does the effect of treatment differ by testing occasion? Use graphical displays showing both levels of complexity.

## Common Misconceptions
- Mixed designs are just two separate designs combined; proper analysis requires understanding interactions between factors.
- Order effects only affect the within factor; between-group differences can interact with order, creating factorial confounds.
- All factorial designs are equally powerful; efficiency depends on effect sizes and the relative costs of between vs. within observation.

## Questions

```yaml
- question: "A clinical trial assigns participants to treatment or placebo (between-subjects) and measures them at baseline, 6 weeks, and 12 weeks (within-subjects). The treatment group improves by 15 points from baseline to 12 weeks; the placebo group improves by 14 points. The Group × Time interaction is non-significant. What can you conclude?"
  type: multiple-choice
  options:
    - "The treatment was effective because the treatment group improved by more than the placebo group"
    - "The treatment showed no differential efficacy — both groups changed over time by nearly the same amount, with no significant difference in trajectory"
    - "The design is flawed because both groups should not improve if the treatment is working"
    - "No conclusion is possible without knowing whether the main effect of time was significant"
  answer: 1
  explanation: "The scientifically central question in a treatment × time design is whether the trajectory of change over time differs between groups — this is the Group × Time interaction. A non-significant interaction means both groups changed by approximately the same amount. The 1-point difference between 15 and 14 is not a differential treatment trajectory; it is captured by the group main effect and likely reflects noise. A significant interaction — not a significant group main effect — is the signature of differential treatment efficacy."

- question: "In a mixed-factorial design, why is the error term for testing the within-subjects factor smaller than for the between-subjects factor?"
  type: multiple-choice
  options:
    - "Because within-subjects effects are measured at more time points, providing more data"
    - "Because individual differences (person-level variance) are removed from the within-subjects error term, since each person serves as their own baseline"
    - "Because the within-subjects factor always has more levels, spreading variance across more cells"
    - "Because researchers choose the within-subjects factor to be the more reliable measurement"
  answer: 1
  explanation: "In within-subjects analysis, each participant contributes measurements at every level of the factor, so person-level variance can be partitioned out of the error term. Two people who both improve 10 points are perfectly consistent even if their baseline scores differ by 30 points — their individual baseline is subtracted out. This partitioning of individual differences is the core statistical efficiency advantage of within-subjects designs. It carries into the within-subjects portion of mixed designs, giving those effects more power than the between-subjects effects."

- question: "In a mixed-factorial treatment study, a significant main effect of the between-subjects group factor is the primary evidence that the treatment worked."
  type: true-false
  answer: false
  explanation: "A significant between-subjects main effect only tells you that one group scored higher on average across all time points. This could reflect pre-existing group differences rather than treatment-driven change. The Group × Time interaction is the primary evidence of differential treatment efficacy — it tests whether the trajectory of change over time differs between groups. Main effects alone cannot distinguish 'the treatment group was already different' from 'the treatment group changed differently over time.'"

- question: "In a treatment × time mixed design, non-parallel lines when plotting group means across time points indicate a Group × Time interaction."
  type: true-false
  answer: true
  explanation: "Plotting time on the x-axis with separate lines per group is the standard visualization of a mixed design. Parallel lines mean each group changed by the same amount across time — no interaction. Non-parallel lines (different slopes, or crossing lines) indicate the groups differed in their rate or direction of change over time — a Group × Time interaction. This graphical interpretation is one of the most direct ways to communicate whether a differential treatment trajectory exists."

- question: "What does a Group × Time interaction actually mean in a treatment study, and why is it more informative than the main effects alone?"
  type: short-answer
  answer: "A Group × Time interaction means the effect of time is different depending on which group you are in — equivalently, the effect of group differs depending on when you measure it. In a treatment study, this is the signature that one group's scores changed over time in a pattern the other group did not show. Main effects in isolation cannot capture this: the main effect of group asks whether one group scored higher overall; the main effect of time asks whether scores changed overall. Neither tells you whether the treatment produced a distinctive trajectory of change compared to control."
  explanation: "This is why the interaction is typically reported as the primary finding in treatment research. A treatment that causes both groups to improve equally produces significant main effects of time and possibly group, but a non-significant interaction — meaning no evidence the treatment specifically drove differential change. The interaction directly tests the causal claim."
```

## Explainer

You've studied between-subjects designs, where different participants are assigned to different conditions, and within-subjects designs, where the same participants experience all conditions. Each has characteristic strengths and limitations. Between-subjects designs eliminate carryover effects but require more participants and leave person-level variance in the error term, reducing power. Within-subjects designs are statistically efficient (person variance is removed) but are vulnerable to order effects, practice, and fatigue. A **mixed-factorial design** combines both in a single study: at least one factor is between-subjects and at least one factor is within-subjects, and the design asks how these factors interact.

The canonical mixed design in psychological research is the **treatment × time** design: participants are randomly assigned to treatment versus control (the between-subjects factor), then measured at multiple time points — pre-treatment, post-treatment, and follow-up (the within-subjects factor). This structure answers three questions at once: Did scores change over time (main effect of time)? Did the groups differ overall (main effect of group)? Did the trajectory of change over time differ between groups (the interaction)? The interaction is usually the scientifically central question — not "did the treatment group score higher overall?" but "did the treatment group improve more over time than the control group?" A significant group × time interaction is the signature of a differential treatment trajectory.

Reading mixed-design interactions requires visualizing them carefully. Plot time on the x-axis, the DV on the y-axis, and draw separate lines for each group. Parallel lines mean no interaction — both groups changed the same amount over time. Non-parallel lines — one group's slope steeper, or the two lines crossing — signal an interaction. The direction of non-parallelism tells you what the interaction means: if the treatment group rises steeply while the control group is flat, treatment produced gains that the control condition did not. If both groups rise initially but only the treatment group maintains gains at follow-up, the interaction is in the time × treatment trajectory and points to durability rather than acute efficacy.

A specific threat to mixed designs is the possibility that **carryover effects** from the within-subjects factor interact with between-subjects group differences. Suppose participants in the treatment group have had more exposure to the task by Time 3 and are therefore more fatigued; the control group, having received neutral activities, does not fatigue the same way. Now the decline in the treatment group at Time 3 reflects fatigue, not treatment decay — but this confound looks exactly like a Group × Time interaction. Counterbalancing and careful order-effect analysis are required to separate treatment effects from fatigue or practice that is differentially distributed across groups.

The mixed design's power advantage depends on how variance is partitioned. The within-subjects factor benefits from individual error removal — each person acts as their own baseline, so the error term for within-subjects effects and interactions is smaller. However, the between-subjects factor retains person-level variance in its error term, so between-groups effects are tested with less power than within-subjects effects, all else equal. This means mixed designs are especially well-suited to research questions where you expect large time or condition effects (detected with power by the within-subjects component) and where group effects are larger or you've sampled enough to compensate for the less efficient between-subjects error term.

