---
id: internal-validity-threats-experimental-control
title: Internal Validity and Threats to Experimental Control
domain: psychology
course: research-methods-psychology
prerequisites:
- id: confounding-variables
  type: hard
- id: experimental-research-design
  type: hard
- id: variables-in-psychology
  type: soft
builds-toward:
- external-validity-generalizability-populations
- ecological-validity-naturalistic-settings
tags:
- validity
- experimental-design
- causal-inference
- threats
stage: formal-systems
status: draft
---

# Internal Validity and Threats to Experimental Control

## Core Idea
Internal validity refers to the degree to which a study can demonstrate a true causal relationship between an independent and dependent variable, free from confounding influences. Threats to internal validity include history, maturation, testing, instrumentation, regression to the mean, and selection bias. Understanding these specific threats enables researchers to design controls that eliminate plausible alternative explanations for observed effects. Strong internal validity is essential for causal claims, though it may require trade-offs with ecological authenticity.

## How It's Best Learned
Study classic examples where internal validity is compromised (e.g., the Hawthorne effect, practice effects from pre-testing). Analyze published experiments to identify which validity threats were addressed and which remain.

## Common Misconceptions
Internal validity means the study is well-designed overall (actually, it specifically means causal conclusions are justified). A study with perfect internal validity automatically has high external validity (actually, gains in control often reduce generalizability).

## Questions

```yaml
- question: "A researcher tests a new reading intervention by enrolling only students who scored in the bottom 10% on a reading assessment. After 6 weeks of intervention, their average score rises significantly. Which threat to internal validity is the most plausible alternative explanation?"
  type: multiple-choice
  options:
    - "History — a news event changed reading habits during the study"
    - "Instrumentation — the scoring rubric changed between assessments"
    - "Regression to the mean — extreme scorers tend to move toward average on retest regardless of intervention"
    - "Selection bias — the groups differed at baseline"
  answer: 2
  explanation: "Regression to the mean is the most plausible threat here. Students selected precisely because they scored at an extreme (the bottom 10%) are partly selected for measurement error that pushed them to that extreme. On retest, their scores will tend to move toward the population mean regardless of any intervention. Without a control group of equally low-scoring students who received no intervention, the researcher cannot distinguish genuine treatment effects from this statistical artifact."

- question: "A study with highly controlled laboratory conditions finds a large, statistically significant effect of a new therapy on anxiety. A critic notes the study has excellent internal validity. What should NOT be concluded from this?"
  type: multiple-choice
  options:
    - "The study provides evidence for a causal link between the therapy and anxiety reduction"
    - "The observed effect is unlikely to be explained by maturation or testing effects"
    - "The findings will generalize well to anxious people in real clinical settings"
    - "Random assignment was probably used to control for selection bias"
  answer: 2
  explanation: "Internal validity is specifically about whether the causal inference within the study is justified — not whether findings generalize. High internal validity often requires tight laboratory control that reduces ecological authenticity: artificial settings, homogeneous samples, carefully screened participants. These controls that strengthen internal validity are precisely what can limit external validity (generalizability to real populations and contexts). The two are frequently in tension."

- question: "A study can have high internal validity but low external validity."
  type: true-false
  answer: true
  explanation: "This is a fundamental and often-overlooked distinction. Internal validity asks: was the causal inference within this study justified? External validity asks: do these findings generalize to other people, settings, and times? Highly controlled laboratory experiments often maximize internal validity by eliminating confounds, but the artificial conditions — screened participants, controlled environments, experimenter observation — reduce how well the findings transfer to messy real-world contexts."

- question: "Random assignment to conditions eliminates all threats to internal validity in an experiment."
  type: true-false
  answer: false
  explanation: "Random assignment is the most powerful tool for addressing selection bias — it distributes known and unknown individual differences equally across conditions at baseline. But it does not eliminate every threat. History (an external event affecting both groups differently), testing effects (sensitization from the pretest), and instrumentation (changes in measurement procedures between assessments) can still operate even with random assignment. Each threat requires its own design solution."

- question: "What does it mean for a study to have high internal validity, and why might achieving it require trade-offs?"
  type: short-answer
  answer: "High internal validity means the study provides strong evidence that the independent variable caused the observed change in the dependent variable — all plausible alternative explanations have been ruled out. Achieving it typically requires tight experimental control: random assignment, standardized procedures, control groups, and laboratory settings. These controls often introduce trade-offs with external validity: the more artificial and controlled the setting, the less it may resemble the real-world contexts to which we want to generalize."
  explanation: "Internal validity is specific: it is about causal inference, not general study quality. A well-designed study can still have low internal validity if its design fails to rule out key alternative explanations. And a study can have high internal validity while being narrow in applicability. The skill is diagnosing which threats are plausible in a given design and evaluating whether the study's controls actually address them."
```

## Explainer

From your study of experimental research design, you know that the logic of experimentation is to manipulate one variable while holding everything else constant, then attribute any resulting change in the outcome to the manipulation. **Internal validity** is the formal name for the degree to which that inference is justified — whether the observed change in the dependent variable was truly caused by the independent variable and nothing else. Every threat to internal validity is a specific alternative explanation: a plausible reason why the outcome might have changed even if the manipulation had no effect.

The most important threats to learn, and the ones you will encounter in published research, are: **history** (an external event occurred during the study that could explain the outcome — a news story breaks while you're measuring attitudes, or a school fire drill interrupts your experiment); **maturation** (participants naturally change over time regardless of your intervention — children get older, people get tired, a condition resolves spontaneously); **testing effects** (taking the pretest sensitizes participants to the topic or teaches them the answers, so gains on the posttest reflect learning from the test itself rather than the intervention); and **instrumentation** (the measurement procedure changes between assessments — observers recalibrate their rating standards, a scale loses calibration, or the same rater becomes more lenient over time).

Two more threats require particular attention because they are less intuitively obvious. **Regression to the mean** occurs because participants selected for extreme scores — the most depressed patients, the lowest-performing students — are partly selected for measurement error that pushed them to that extreme. On retest, their scores move toward the population mean regardless of any intervention. If you enroll only the highest-scorers on a pre-test and see lower scores afterward, regression may explain it entirely. **Selection bias** occurs when the groups being compared differ systematically before the manipulation begins — in a pretest-posttest design without random assignment, the treatment group may have been more motivated to begin with.

Controlled experiments address these threats primarily through **random assignment**, which distributes all known and unknown individual differences equally across conditions at baseline. But random assignment does not eliminate every threat — history, testing effects, and instrumentation can still operate. Each threat has corresponding design solutions: control groups to absorb history and maturation effects, Solomon four-group designs to separate testing effects from treatment effects, inter-rater reliability checks and standardized protocols to address instrumentation. The important skill is not memorizing the list of threats but diagnosing which ones are plausible in a specific study and evaluating whether the design actually rules them out.
