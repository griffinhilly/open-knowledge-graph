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
status: validated
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

## Questions

```yaml
- question: "A researcher tests whether a mindfulness program reduces student anxiety. All participants complete the 8-week program during finals season. Anxiety is measured before (high-stress exam period) and after (summer break). Students show significantly lower post-program anxiety. What is the main threat to internal validity?"
  type: multiple-choice
  options:
    - "Regression to the mean — anxious students naturally return to baseline"
    - "Selection bias — the students who enrolled chose to be there"
    - "History or maturation — the exam season ending could explain the anxiety decrease, not the program"
    - "Instrumentation — the anxiety measure may not be valid"
  answer: 2
  explanation: "This is a textbook history/maturation confound. The pre-post change coincides with moving from finals week (high-stress) to summer (low-stress). Any improvement in anxiety could be caused by this external event (history) or natural recovery once the stressor passes (maturation), not the mindfulness program. There is no control group experiencing the same time period without the treatment, so we cannot distinguish the treatment effect from the passage of time."

- question: "A study targets struggling readers (bottom 10% on a pretest), implements a reading intervention, and finds their posttest scores improved significantly. A skeptic says this may not reflect a real treatment effect. Why?"
  type: multiple-choice
  options:
    - "Struggling readers cannot improve regardless of intervention, making the gains suspicious"
    - "Regression to the mean: extreme low scorers tend to score closer to the population average on a second test regardless of any treatment, because extreme scores partly reflect measurement error"
    - "Selection bias: the students chose to participate, making them unrepresentative"
    - "The study lacks random assignment, so no conclusions are possible"
  answer: 1
  explanation: "Regression to the mean is the key threat here. When participants are selected because they scored extremely low on a pretest, their true scores are near the floor, but their measured scores include downward measurement error. On a second measurement, that error is less likely to be extreme and downward, so scores tend to drift upward toward the group mean — regardless of any intervention. Studies targeting 'at-risk' populations without a parallel control group systematically overestimate treatment effects for this reason."

- question: "Adding a no-treatment control group to a study helps rule out history and maturation as alternative explanations for observed changes in the treatment group."
  type: true-false
  answer: true
  explanation: "A control group experiencing the same time period, environment, and measurement procedures as the treatment group but not receiving the treatment controls for history (both groups face the same external events) and maturation (both groups age and develop at the same rate). If the treatment group improves more than the control group, the difference is less likely to be explained by history or maturation alone. This is why the pre-post-with-control design is fundamentally stronger than a simple pre-post design."

- question: "Random assignment to conditions eliminates all major threats to internal validity, making additional experimental controls unnecessary."
  type: true-false
  answer: false
  explanation: "Random assignment is powerful but limited: it controls selection bias by distributing known and unknown confounds equally across conditions at the start. It does not eliminate history (external events can affect both groups differentially if they are tested at different times), maturation (both groups mature, but differential maturation remains if groups experience the study differently), or testing effects (all participants who take a pretest are affected by it). Random assignment is necessary but not sufficient for ruling out all threats to internal validity."

- question: "What is the key function of a control group in an experiment, framed in terms of threats to internal validity rather than statistical power?"
  type: short-answer
  answer: "The control group serves as a comparison condition that experiences all the same potential confounds as the treatment group — the same passage of time (history and maturation), the same measurement procedures (testing and instrumentation effects) — but without the treatment. Any change observed in both groups can be attributed to these shared alternative explanations. Only the difference between groups can plausibly be attributed to the treatment. Without a control group, you cannot separate the treatment effect from the confounds; the control group is the systematic elimination of rival hypotheses."
  explanation: "Framing the control group in terms of threats reveals its deeper purpose: it is not just a statistical baseline but a structural defense against alternative explanations. Every major threat to internal validity is a rival hypothesis — the control group is what allows you to rule out those rivals. This is why quasi-experimental designs that lack equivalent control groups require much more careful threat-by-threat analysis to support causal conclusions."
```

## Explainer

From your study of experimental research design, you know that the defining feature of a true experiment is random assignment — and you know it's important. Internal validity explains why. **Internal validity** is the degree to which you can make a confident causal claim: did the independent variable actually cause the change in the dependent variable, or could something else explain it? Every threat to internal validity is a plausible alternative explanation that, if present, undermines the causal conclusion. You can think of threats as rival hypotheses competing with your treatment explanation.

The major threats identified by Campbell and Stanley fall into recognizable categories. **History** refers to events that occur during a study — between pretest and posttest — that might cause change independent of the treatment. If a stress-reduction intervention runs during final exams week, the observed changes in stress could reflect the exam period ending, not the treatment. **Maturation** refers to natural developmental or biological changes over time: participants grow older, get tired, get better on their own. A learning intervention with children over a school year competes with the maturation of reading skills. **Testing effects** occur when taking the pretest itself changes performance on the posttest — practice effects, sensitization, or learning the measure. **Instrumentation** occurs when the measurement tool or the raters change over the course of the study, creating apparent change that is really a measurement artifact.

**Selection bias** and **regression to the mean** are particularly important in quasi-experimental designs. Selection bias arises when comparison groups differ on relevant characteristics before the study begins — the groups were not equivalent to start with, so any difference at the end could reflect pre-existing differences rather than the treatment. Regression to the mean is a statistical phenomenon: if you select participants because they scored extremely high or low on a pretest, their posttest scores will tend to drift back toward the population mean regardless of any intervention, because extreme scores partly reflect measurement error. Treating this drift as a treatment effect is a classic error in studies targeting "at-risk" populations.

**Random assignment** is the most powerful safeguard against these threats because it distributes all known and unknown confounds equally across conditions on average — including ones the researcher never thought to measure. But it doesn't eliminate every threat. A long study with random assignment still faces history and maturation; a study using pretests faces testing effects. The value of understanding specific threats is that it guides design choices: adding a no-treatment control group addresses history and maturation; using a posttest-only design eliminates testing effects; using masked raters addresses instrumentation drift. Strong experimental design is the systematic removal of alternative explanations before data collection begins.
