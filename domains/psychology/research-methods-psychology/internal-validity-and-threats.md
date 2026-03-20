---
id: internal-validity-and-threats
title: Internal Validity and Threats to Causal Inference
domain: psychology
course: research-methods-psychology
prerequisites:
- id: experimental-research-design
  type: hard
- id: confounding-variables
  type: soft
builds-toward:
- construct-validity-and-measurement
- external-validity-generalization
tags:
- validity
- causality
- confounds
stage: formal-systems
status: draft
---

# Internal Validity and Threats to Causal Inference

## Core Idea
Internal validity is the degree to which you can confidently conclude that changes in the dependent variable are caused by the independent variable rather than other factors. Major threats include history, maturation, testing effects, instrumentation, selection bias, and regression to the mean. Experimental designs with random assignment provide strongest internal validity; quasi-experimental and observational designs require systematic threat identification and control.

## How It's Best Learned
For each potential threat (history, maturation, testing, instrumentation, selection, regression, interactions), identify how your design eliminates or controls it. Compare internal validity across designs: true experiment > quasi-experiment > correlational study. Read published critiques of studies to see how researchers address alternative explanations.

## Common Misconceptions
- A study has either good or poor internal validity; it's more nuanced—specific threats are present or absent, and your design strength addresses them differentially.
- Random assignment eliminates all threats to internal validity; it controls selection bias and interactions but not history, maturation, or testing effects.
- Controlling variables by holding them constant strengthens internal validity; this reduces confounding but may compromise external validity by restricting generalizability.

## Explainer

From your study of experimental research design, you know that the defining feature of a true experiment is random assignment — and you know it's important. Internal validity explains why. **Internal validity** is the degree to which you can make a confident causal claim: did the independent variable actually cause the change in the dependent variable, or could something else explain it? Every threat to internal validity is a plausible alternative explanation that, if present, undermines the causal conclusion. You can think of threats as rival hypotheses competing with your treatment explanation.

The major threats identified by Campbell and Stanley fall into recognizable categories. **History** refers to events that occur during a study — between pretest and posttest — that might cause change independent of the treatment. If a stress-reduction intervention runs during final exams week, the observed changes in stress could reflect the exam period ending, not the treatment. **Maturation** refers to natural developmental or biological changes over time: participants grow older, get tired, get better on their own. A learning intervention with children over a school year competes with the maturation of reading skills. **Testing effects** occur when taking the pretest itself changes performance on the posttest — practice effects, sensitization, or learning the measure. **Instrumentation** occurs when the measurement tool or the raters change over the course of the study, creating apparent change that is really a measurement artifact.

**Selection bias** and **regression to the mean** are particularly important in quasi-experimental designs. Selection bias arises when comparison groups differ on relevant characteristics before the study begins — the groups were not equivalent to start with, so any difference at the end could reflect pre-existing differences rather than the treatment. Regression to the mean is a statistical phenomenon: if you select participants because they scored extremely high or low on a pretest, their posttest scores will tend to drift back toward the population mean regardless of any intervention, because extreme scores partly reflect measurement error. Treating this drift as a treatment effect is a classic error in studies targeting "at-risk" populations.

**Random assignment** is the most powerful safeguard against these threats because it distributes all known and unknown confounds equally across conditions on average — including ones the researcher never thought to measure. But it doesn't eliminate every threat. A long study with random assignment still faces history and maturation; a study using pretests faces testing effects. The value of understanding specific threats is that it guides design choices: adding a no-treatment control group addresses history and maturation; using a posttest-only design eliminates testing effects; using masked raters addresses instrumentation drift. Strong experimental design is the systematic removal of alternative explanations before data collection begins.
