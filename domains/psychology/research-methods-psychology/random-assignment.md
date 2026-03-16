---
id: random-assignment
title: Random Assignment
domain: psychology
course: research-methods-psychology
prerequisites:
- id: control-and-experimental-groups
  type: hard
- id: sampling-in-psychology
  type: soft
builds-toward:
- confounding-variables
- inferential-statistics-psychology
tags:
- random-assignment
- confound-control
- equivalence
- internal-validity
stage: abstract-reasoning
status: validated
---

# Random Assignment

## Core Idea
Random assignment allocates participants to experimental conditions by chance, ensuring that pre-existing differences between individuals are distributed evenly across groups on average. This is what makes experiments capable of supporting causal conclusions — any differences in outcomes can be attributed to the IV rather than pre-existing group differences. Random assignment does not guarantee groups are identical; it only ensures no systematic bias in assignment. With small samples, chance imbalances can still occur.

## How It's Best Learned
Simulate random assignment of 20 participants to two groups (using a random number table) and check whether the groups are balanced on a key characteristic. Repeat the simulation multiple times to see variability.

## Common Misconceptions
- Random assignment is not the same as random sampling — a study can have one, both, or neither.
- Random assignment does not eliminate all confounds; only systematic ones are controlled. Chance imbalances remain possible.

## Explainer

You understand the structure of an experiment: a control group establishes the baseline, an experimental group receives the treatment, and any difference in outcomes is attributed to the independent variable. But this logical chain has a hidden assumption — that the two groups were equivalent *before* the study began. If the groups were different at the start, any outcome difference might reflect that initial difference rather than the treatment. Random assignment is the mechanism that creates pre-treatment equivalence, and understanding precisely why it works explains why experiments occupy a privileged position in causal inference.

The threat that random assignment defeats is the **confounding variable**: a pre-existing participant characteristic that could independently affect the outcome. Imagine testing whether a new therapy reduces anxiety. If you let participants choose their group, motivated, help-seeking individuals would likely self-select into treatment. Any improvement might reflect their motivation and self-selection, not the therapy. Random assignment breaks the connection between participant characteristics and group membership. When assignment is determined by a coin flip or random number generator, every personal characteristic — motivation, baseline severity, personality, prior treatment history — is equally likely to end up in either group. No characteristic can systematically concentrate in one condition.

This is what makes experiments qualitatively different from correlational designs for establishing causation. A correlation between two variables might be explained by a third variable causing both. But when participants are randomly assigned to conditions, no third variable can *systematically* account for a group difference — it was distributed randomly between groups. The causal logic follows cleanly: the groups were equivalent before treatment; they were treated identically except for the independent variable; one group shows better outcomes. The treatment caused the improvement. This inference is unavailable in correlational research regardless of sample size or statistical sophistication.

One distinction deserves emphasis: **random assignment** and **random sampling** are independent. Random sampling controls who enters your study from the population and affects external validity — how far your findings generalize. Random assignment controls who goes into which condition and affects internal validity — whether you can conclude causation. A lab study can randomly assign university students (random assignment without random sampling); a national survey can sample randomly without assigning anyone to conditions (random sampling without random assignment). Both are valuable; they solve different problems. Only random assignment enables causal conclusions.
