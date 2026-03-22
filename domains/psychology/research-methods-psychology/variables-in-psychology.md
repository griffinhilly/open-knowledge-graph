---
id: variables-in-psychology
title: 'Variables: Independent, Dependent, and Confounding'
domain: psychology
course: research-methods-psychology
prerequisites:
- id: operational-definitions
  type: hard
- id: research-hypothesis-formation
  type: hard
builds-toward:
- experimental-research-design
- correlational-research-design
- confounding-variables
tags:
- IV
- DV
- confound
- variables
- experimental-control
stage: formal-systems
status: validated
---

# Variables: Independent, Dependent, and Confounding

## Core Idea
The independent variable (IV) is what the researcher manipulates or uses to group participants; the dependent variable (DV) is what is measured as the outcome. Confounding variables are extraneous factors that vary with the IV and can provide alternative explanations for changes in the DV. Identifying and controlling confounds is essential for establishing causal relationships. Well-designed studies isolate the IV's effect by holding other variables constant or randomizing them.

## How It's Best Learned
Given a study description, practice labeling the IV, DV, and any potential confounds. Then redesign the study to control for identified confounds.

## Common Misconceptions
- A correlation between two variables does not make one the IV and the other the DV — those roles are defined by the research design, not the data.
- Controlling a confound doesn't mean eliminating it; it means ensuring it doesn't systematically differ across conditions.

## Questions

```yaml
- question: "A study tests whether caffeine improves memory by giving one group 200mg of caffeine and a control group a placebo, then measuring scores on a word-recall test. What is the dependent variable?"
  type: multiple-choice
  options: ["Caffeine dose (200mg vs. placebo)", "Word-recall test scores", "The participants themselves", "The amount of sleep participants got the night before"]
  answer: 1
  explanation: "The dependent variable is what is measured as the outcome — word-recall scores. Caffeine dose is the independent variable (what is manipulated). Amount of sleep is a potential confounding variable. The DV is always the outcome you are measuring to see whether the IV had an effect."

- question: "In an observational study that finds a correlation between screen time and attention difficulties in children, screen time is the independent variable."
  type: true-false
  answer: false
  explanation: "In an observational (non-experimental) study, neither variable is manipulated — both are simply measured. The labels 'independent variable' and 'dependent variable' are defined by research design, not by correlation. Calling screen time the IV implies it was assigned or manipulated, which it was not. In correlational studies, researchers use terms like 'predictor' and 'outcome' to avoid implying causation."

- question: "A researcher studying the effect of exercise on mood fails to account for the fact that participants who exercise more also tend to sleep more. What threat does this represent, and how could it be addressed?"
  type: short-answer
  answer: "Sleep is a confounding variable — it co-varies with exercise (the IV) and independently affects mood (the DV), making it impossible to attribute mood changes solely to exercise. It could be addressed by measuring and statistically adjusting for sleep, or by holding sleep constant across conditions."
  explanation: "Confounds are threats to internal validity because they provide alternative explanations for the IV-DV relationship. Good experimental design either holds confounds constant, randomizes them across groups, or measures and statistically controls them."
```

## Explainer

Every empirical study in psychology involves at least three conceptual roles for variables, and keeping them straight is the difference between a study that answers its question and one that cannot. You have already practiced writing operational definitions — precise, measurable specifications of abstract concepts. Now those definitions get sorted into roles: what is being manipulated, what is being measured, and what might be contaminating the relationship between them.

The independent variable (IV) is what the researcher controls or assigns. In a true experiment, participants are randomly assigned to different levels of the IV — perhaps 0mg, 100mg, or 200mg of caffeine. The IV is the cause you are testing. The dependent variable (DV) is the outcome you measure — the word-recall score, the reaction time, the self-reported mood rating. It is "dependent" because its value is expected to depend on the IV. A clean way to remember the relationship: the DV depends on the IV.

Confounding variables are where studies go wrong. A confound is any variable that (1) varies systematically with the IV and (2) independently influences the DV. If your high-caffeine participants also happen to have slept more than your control group, sleep is confounded with caffeine — and any improvement in recall could be due to sleep, caffeine, or both. You cannot tell. Experimental control means either holding confounds constant across conditions or randomizing participants so that confounds are equally distributed across groups. Randomization is the gold standard precisely because it controls for every confound simultaneously, even ones you have not thought of.

A common error is treating the IV/DV distinction as a property of the variables themselves rather than of the research design. In a correlational study, you simply measure two variables and observe their relationship — neither is assigned or manipulated, so neither is technically an "independent variable." Calling one the IV would imply a causal claim the design cannot support. Researchers in non-experimental work instead use "predictor" and "outcome" — the same conceptual relationship, but without the causal implication. This distinction is not pedantic; it is the difference between a valid inference and an overreach.
