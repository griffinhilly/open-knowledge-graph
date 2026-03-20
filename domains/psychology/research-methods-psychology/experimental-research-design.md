---
id: experimental-research-design
title: Experimental Research Design
domain: psychology
course: research-methods-psychology
prerequisites:
- id: variables-in-psychology
  type: hard
- id: research-hypothesis-formation
  type: hard
- id: psychological-research-ethics
  type: soft
- id: hypothesis-testing-fundamentals
  type: soft
builds-toward:
- control-and-experimental-groups
- random-assignment
- confounding-variables
- blinding-in-experiments
tags:
- experiment
- causation
- manipulation
- control
- between-subjects
stage: formal-systems
status: validated
---

# Experimental Research Design

## Core Idea
True experiments are the only design that can establish causal relationships because researchers actively manipulate the independent variable and randomly assign participants to conditions. The key elements are: (1) manipulation of the IV, (2) measurement of the DV, (3) control of extraneous variables, and (4) random assignment. Experiments can be between-subjects (different participants in each condition) or within-subjects (same participants in all conditions), each with distinct advantages and trade-offs.

## How It's Best Learned
Design a simple experiment from start to finish: write a hypothesis, specify the IV and DV operationally, describe the control condition, and explain the random assignment procedure.

## Common Misconceptions
- Random assignment (allocating participants to conditions) is not the same as random sampling (selecting who participates).
- A laboratory experiment is not automatically more valid than a field experiment — the setting must match the research question.

## Questions

```yaml
- question: "A researcher wants to determine whether a new tutoring program causes higher test scores. She recruits 60 students and lets them choose whether to join the tutoring group or the control group. What is the primary problem with this design?"
  type: multiple-choice
  options: ["The sample size is too small to detect an effect", "Self-selection means the groups may differ in motivation before the program starts, confounding the results", "The researcher should have used a within-subjects design instead", "Field experiments cannot establish causation"]
  answer: 1
  explanation: "Allowing participants to self-select into conditions destroys the logic of a true experiment. Students who volunteer for tutoring may already be more motivated or academically engaged than those who opt out. Any score difference at the end cannot be attributed to the tutoring program alone — it may reflect pre-existing differences. Random assignment prevents this by ensuring that motivation, ability, and all other individual differences are distributed evenly across groups by chance."

- question: "Random assignment and random sampling are two names for the same procedure in experimental research."
  type: true-false
  answer: false
  explanation: "Random sampling refers to how you select participants from the population to include in your study — it determines external validity (generalizability). Random assignment refers to how you allocate participants who are already in your study to experimental conditions — it determines internal validity (ability to infer causation). A study can have one without the other: a convenience sample (no random sampling) that is randomly assigned to conditions can still establish causation within that sample, just with limited generalizability."

- question: "What is the difference between a between-subjects and a within-subjects experimental design, and give one advantage of each?"
  type: short-answer
  answer: "Between-subjects: different participants are in each condition. Advantage: no carryover effects — participants cannot be influenced by exposure to other conditions. Within-subjects: the same participants experience all conditions. Advantage: each participant serves as their own control, eliminating individual-difference variability and requiring fewer total participants."
  explanation: "The choice between designs involves a trade-off. Between-subjects designs require more participants (separate groups for each condition) but avoid order effects, practice effects, and demand characteristics that arise when the same person completes multiple conditions. Within-subjects designs are statistically more powerful for detecting effects because individual differences are removed from the error term, but they require counterbalancing to control for carryover effects."
```

## Explainer

You have already learned what variables are in psychological research and how hypotheses are formed. The experimental design is the structure that lets you test whether one variable actually *causes* changes in another — not just whether they tend to occur together. This distinction between causation and correlation is the central reason experiments exist. Observational studies can detect patterns; only experiments can, under the right conditions, establish that one thing makes another thing happen.

The logic of a true experiment rests on random assignment. If you take a group of participants and randomly allocate them to conditions, then on average, every characteristic that might influence the outcome — prior knowledge, motivation, age, personality — will be distributed evenly across your groups. Any systematic difference you observe at the end is therefore attributable to the one thing that differed between groups: the manipulation you introduced. Without random assignment, this logic breaks down. A convenience sample that self-selects into groups carries all its pre-existing differences into the comparison, making it impossible to isolate the effect of your intervention.

The four elements of a true experiment work together: (1) You manipulate the independent variable (IV) — the presumed cause. (2) You measure the dependent variable (DV) — the presumed effect. (3) You control extraneous variables that could otherwise explain your results. (4) You randomly assign participants to conditions. Remove any one of these and you weaken your ability to draw causal conclusions. A study that manipulates an IV and measures a DV but lacks random assignment is a quasi-experiment — useful, but with greater ambiguity about causation.

The choice between between-subjects and within-subjects designs is a practical trade-off. Between-subjects designs give each participant only one condition, so there is no risk that experiencing one condition influences behavior in another (carryover or practice effects). Within-subjects designs use the same participants across conditions, which dramatically reduces the number of participants you need and removes all individual-difference variability from the comparison — a major statistical advantage. The cost is managing order effects through counterbalancing (varying the sequence of conditions across participants).

One important misconception: laboratory experiments do not automatically have more validity than field experiments. Laboratory settings offer control — you can hold constant many variables that vary in the real world — but that control can come at the cost of ecological validity: the degree to which your findings generalize to natural settings. If you are studying whether noise affects test performance, a lab study gives you clean control over noise levels but may produce a situation so artificial that participants behave differently than they would in a real exam. Matching the setting to the research question is what determines validity, not the setting itself.
