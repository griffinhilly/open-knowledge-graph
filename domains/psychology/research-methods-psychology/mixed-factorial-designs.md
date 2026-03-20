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

## Explainer

You've studied between-subjects designs, where different participants are assigned to different conditions, and within-subjects designs, where the same participants experience all conditions. Each has characteristic strengths and limitations. Between-subjects designs eliminate carryover effects but require more participants and leave person-level variance in the error term, reducing power. Within-subjects designs are statistically efficient (person variance is removed) but are vulnerable to order effects, practice, and fatigue. A **mixed-factorial design** combines both in a single study: at least one factor is between-subjects and at least one factor is within-subjects, and the design asks how these factors interact.

The canonical mixed design in psychological research is the **treatment × time** design: participants are randomly assigned to treatment versus control (the between-subjects factor), then measured at multiple time points — pre-treatment, post-treatment, and follow-up (the within-subjects factor). This structure answers three questions at once: Did scores change over time (main effect of time)? Did the groups differ overall (main effect of group)? Did the trajectory of change over time differ between groups (the interaction)? The interaction is usually the scientifically central question — not "did the treatment group score higher overall?" but "did the treatment group improve more over time than the control group?" A significant group × time interaction is the signature of a differential treatment trajectory.

Reading mixed-design interactions requires visualizing them carefully. Plot time on the x-axis, the DV on the y-axis, and draw separate lines for each group. Parallel lines mean no interaction — both groups changed the same amount over time. Non-parallel lines — one group's slope steeper, or the two lines crossing — signal an interaction. The direction of non-parallelism tells you what the interaction means: if the treatment group rises steeply while the control group is flat, treatment produced gains that the control condition did not. If both groups rise initially but only the treatment group maintains gains at follow-up, the interaction is in the time × treatment trajectory and points to durability rather than acute efficacy.

A specific threat to mixed designs is the possibility that **carryover effects** from the within-subjects factor interact with between-subjects group differences. Suppose participants in the treatment group have had more exposure to the task by Time 3 and are therefore more fatigued; the control group, having received neutral activities, does not fatigue the same way. Now the decline in the treatment group at Time 3 reflects fatigue, not treatment decay — but this confound looks exactly like a Group × Time interaction. Counterbalancing and careful order-effect analysis are required to separate treatment effects from fatigue or practice that is differentially distributed across groups.

The mixed design's power advantage depends on how variance is partitioned. The within-subjects factor benefits from individual error removal — each person acts as their own baseline, so the error term for within-subjects effects and interactions is smaller. However, the between-subjects factor retains person-level variance in its error term, so between-groups effects are tested with less power than within-subjects effects, all else equal. This means mixed designs are especially well-suited to research questions where you expect large time or condition effects (detected with power by the within-subjects component) and where group effects are larger or you've sampled enough to compensate for the less efficient between-subjects error term.

