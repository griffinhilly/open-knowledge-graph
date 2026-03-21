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
stage: formal-systems
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

## Questions

```yaml
- question: "A researcher randomly assigns 40 university students to a treatment or control group, then measures anxiety after a 6-week therapy program. After the study, she finds the treatment group had significantly lower anxiety. She also notes she did not use random sampling from any population. Which conclusion is most justified?"
  type: multiple-choice
  options:
    - "Neither causation nor generalization — without random sampling, the study is invalid"
    - "Causation within this sample, but limited generalization to the broader population"
    - "Broad generalization to all adults, because the finding was statistically significant"
    - "Causation only if the two groups happened to be identical on all pre-existing characteristics"
  answer: 1
  explanation: "Random assignment enables causal inference (the treatment likely caused the anxiety reduction) by eliminating systematic confounds. Without random sampling, generalizability is limited — the finding may not extend beyond university students or this particular population. But the absence of random sampling does not invalidate the causal conclusion within the study. Random assignment controls internal validity; random sampling controls external validity. They are independent, and a study can have one without the other."

- question: "After random assignment, a researcher checks her two groups and finds that, by chance, the treatment group has slightly higher baseline anxiety than the control group. What does this reveal about random assignment?"
  type: multiple-choice
  options:
    - "The random assignment was done incorrectly and must be redone"
    - "Random assignment guarantees perfect group equivalence, so this finding indicates a procedural error"
    - "Random assignment prevents systematic bias but does not guarantee identical groups — chance imbalances are still possible, especially with small samples"
    - "This imbalance is impossible if true randomization was used"
  answer: 2
  explanation: "Random assignment ensures that no characteristic systematically concentrates in one condition — assignment is determined by chance, not by any property of the participant. But chance itself can produce imbalances, particularly with small samples. In a study of 40 participants, a few unlucky assignments could leave one group slightly higher on a variable. This is not an error; it is the expected variability of random processes. Random assignment controls systematic bias, not sampling error. Large samples reduce but never eliminate this possibility."

- question: "A study that uses random assignment but not random sampling can still support causal conclusions about the effect of the independent variable."
  type: true-false
  answer: true
  explanation: "Causal inference depends on internal validity, which random assignment provides by distributing pre-existing differences evenly across groups. External validity (generalizability) depends on how the sample was selected — random sampling improves it, but its absence does not undermine causation. A laboratory study using convenience sampling with random assignment can validly conclude that the treatment caused the observed difference within that study, even if generalization to other populations requires caution."

- question: "Random assignment eliminates all confounding variables, ensuring that any group difference in outcomes must be caused by the independent variable."
  type: true-false
  answer: false
  explanation: "Random assignment eliminates systematic confounds — pre-existing characteristics that would otherwise concentrate in one group due to how participants were selected or self-selected. But it cannot eliminate chance imbalances on specific variables, and it does not control for procedural confounds introduced during the study (e.g., experimenter expectancy effects). The correct claim is that random assignment eliminates *systematic* bias in group composition, which is what enables causal inference on average and across replications."

- question: "Why does random assignment enable causal conclusions in a way that correlational research cannot, regardless of how large the correlational sample is?"
  type: short-answer
  answer: "In correlational research, any observed association between X and Y might be explained by a third variable Z that causes both — a confound. Increasing sample size cannot rule out this explanation; it only provides more precise estimates of the association. Random assignment breaks the connection between participant characteristics and group membership: because assignment is determined by chance, no participant characteristic can systematically differ between groups. Before the manipulation, groups are equivalent on average on all variables (measured and unmeasured). Any post-treatment difference therefore cannot be explained by pre-existing group differences, leaving the treatment as the only systematic explanation."
  explanation: "This is the logical structure that gives experiments their privileged status for causal inference. The logic is: (1) groups were equivalent before treatment by design, (2) groups were treated identically except for the IV, (3) one group shows better outcomes — therefore the IV caused the difference. Step 1 is only guaranteed by random assignment. No statistical technique applied to correlational data can fully replicate this guarantee, because unmeasured confounds always remain possible."
```

## Explainer

You understand the structure of an experiment: a control group establishes the baseline, an experimental group receives the treatment, and any difference in outcomes is attributed to the independent variable. But this logical chain has a hidden assumption — that the two groups were equivalent *before* the study began. If the groups were different at the start, any outcome difference might reflect that initial difference rather than the treatment. Random assignment is the mechanism that creates pre-treatment equivalence, and understanding precisely why it works explains why experiments occupy a privileged position in causal inference.

The threat that random assignment defeats is the **confounding variable**: a pre-existing participant characteristic that could independently affect the outcome. Imagine testing whether a new therapy reduces anxiety. If you let participants choose their group, motivated, help-seeking individuals would likely self-select into treatment. Any improvement might reflect their motivation and self-selection, not the therapy. Random assignment breaks the connection between participant characteristics and group membership. When assignment is determined by a coin flip or random number generator, every personal characteristic — motivation, baseline severity, personality, prior treatment history — is equally likely to end up in either group. No characteristic can systematically concentrate in one condition.

This is what makes experiments qualitatively different from correlational designs for establishing causation. A correlation between two variables might be explained by a third variable causing both. But when participants are randomly assigned to conditions, no third variable can *systematically* account for a group difference — it was distributed randomly between groups. The causal logic follows cleanly: the groups were equivalent before treatment; they were treated identically except for the independent variable; one group shows better outcomes. The treatment caused the improvement. This inference is unavailable in correlational research regardless of sample size or statistical sophistication.

One distinction deserves emphasis: **random assignment** and **random sampling** are independent. Random sampling controls who enters your study from the population and affects external validity — how far your findings generalize. Random assignment controls who goes into which condition and affects internal validity — whether you can conclude causation. A lab study can randomly assign university students (random assignment without random sampling); a national survey can sample randomly without assigning anyone to conditions (random sampling without random assignment). Both are valuable; they solve different problems. Only random assignment enables causal conclusions.
