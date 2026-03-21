---
id: confounding-variables
title: Confounding Variables and Internal Validity
domain: psychology
course: research-methods-psychology
prerequisites:
- id: variables-in-psychology
  type: hard
- id: experimental-research-design
  type: hard
- id: correlational-research-design
  type: soft
- id: random-assignment
  type: soft
builds-toward:
- blinding-in-experiments
- validity-in-measurement
tags:
- confound
- internal-validity
- history-effect
- maturation
- selection-bias
stage: formal-systems
status: validated
---
# Confounding Variables and Internal Validity

## Core Idea
A confounding variable is any factor other than the IV that systematically differs between conditions and could explain the DV results. Internal validity refers to the degree to which a study justifies a causal inference — high internal validity means confounds have been ruled out. Common threats include selection bias (non-equivalent groups), history effects (external events during the study), maturation (natural change over time), regression to the mean, and demand characteristics. Experimental control and random assignment are the primary defenses against confounding.

## How It's Best Learned
Read descriptions of quasi-experiments (no random assignment) and identify which specific threats to internal validity apply and why they cannot be ruled out.

## Common Misconceptions
- Adding more participants does not reduce confounding — it only increases statistical power. Confounds are design problems, not sample-size problems.
- Internal and external validity are often in tension: tightly controlled experiments high on internal validity may lack real-world applicability.

## Questions

```yaml
- question: "A study finds that cities with more hospitals per capita have higher death rates. A policy student concludes hospitals are harmful and proposes reducing hospital funding. What is the most likely confounding variable?"
  type: multiple-choice
  options:
    - "City population size — larger cities have more hospitals and more deaths in raw numbers"
    - "Illness severity — sicker populations both seek hospital care and are more likely to die, making hospitals appear harmful"
    - "Hospital quality — better hospitals attract more patients who then die despite good care"
    - "Medical staff shortages — fewer doctors per patient leads to both more hospitals and higher death rates"
  answer: 1
  explanation: "Illness severity is the classic confound here: sicker populations create demand for more hospitals AND are more likely to die regardless of care quality. The pre-existing illness explains both the number of hospitals and the death rate — it is a systematic alternative explanation for both variables. This is selection bias at the population level: the comparison groups (high-hospital vs. low-hospital cities) differ in population health before any hospital effect can be measured. The causal direction is reversed from what the naive interpretation suggests."

- question: "A school tests a new reading curriculum by comparing students in the new program (Group A) to students from the previous year who used the old curriculum (Group B). Group A scores 15% higher. What is the primary threat to internal validity?"
  type: multiple-choice
  options:
    - "Regression to the mean — Group A's scores are likely to drop back toward average next year"
    - "History effects — other improvements (new teachers, school initiatives) may have occurred between the two years"
    - "Demand characteristics — Group A students knew they were in the new curriculum and tried harder"
    - "The sample was too small — adding more students would have eliminated these confounds"
  answer: 1
  explanation: "Comparing across different years means any changes between years are potential confounds. History effects capture exactly this: external events (new teachers, school-wide initiatives, demographic shifts) that occurred between the two measurement periods could explain the score difference independently of the curriculum. Option D is a key misconception: more participants increase statistical power but do not remove confounds — confounding is a design problem, not a sample-size problem."

- question: "A variable that is randomly distributed across participants in a study reduces internal validity by acting as a confound."
  type: true-false
  answer: false
  explanation: "Random variation is noise — it increases variance in the dependent variable but does not threaten internal validity. A confound requires SYSTEMATIC variation correlated with the independent variable that provides an alternative causal explanation. If a variable (say, IQ) is randomly distributed across conditions due to random assignment, it adds noise but not bias — it cannot explain why one condition outperformed another, because IQ is equally distributed in both groups."

- question: "Running a study with a larger sample size can eliminate confounding variables if the sample is large enough."
  type: true-false
  answer: false
  explanation: "Confounding is a design problem, not a sample-size problem. A confound exists when the study design allows a variable to systematically differ between conditions. No matter how many participants you add, if more motivated students are assigned to the treatment condition, motivation remains confounded with treatment. More participants give you more power to detect a confounded effect — which is arguably worse, since you become more confident in a misleading conclusion. The solution is design: random assignment, matching, or other control procedures."

- question: "Why does random assignment eliminate confounds, while statistical control (measuring and adjusting for known confounds) does not fully solve the problem?"
  type: short-answer
  answer: "Random assignment distributes all participant characteristics — both measured and unmeasured — roughly equally across conditions by chance. No variable can systematically favor one group. Statistical control, by contrast, can only adjust for confounds you have already measured and correctly modeled. Unknown confounds, confounds you didn't think to measure, and confounds with complex relationships to the outcome cannot be adequately controlled statistically. Random assignment provides blanket protection against all potential confounds; statistical control addresses only the ones you already know about."
  explanation: "This asymmetry explains why experiments with random assignment are the gold standard for causal inference, while observational studies — even with extensive statistical controls — cannot fully rule out alternative explanations. Every observational study carries the caveat 'there may be unmeasured confounds.' A randomized experiment pushes that concern aside by design. The practical implication: design is the first line of defense against confounding, and statistical analysis is a secondary tool for variables that couldn't be fully randomized."
```

## Explainer

From experimental research design, you know that the purpose of an experiment is to isolate causation — to show that changes in the independent variable (IV) caused changes in the dependent variable (DV). A **confounding variable** is anything that threatens this isolation. Precisely: a confounder is a variable that (1) systematically differs between conditions, and (2) could plausibly explain the DV results independently of the IV. Both conditions must be met. A variable that varies randomly across participants is not a confound — it is noise. A variable that varies systematically and provides an alternative causal story is the problem.

Consider a study testing whether a new tutoring program improves test scores. Students who sign up for the program are compared against those who do not. Even if program students score higher, you cannot attribute this to the program, because students who volunteer for tutoring are likely more motivated to begin with. **Selection bias** is the confound: the groups differed in motivation before the intervention started, and motivation independently predicts test performance. The difference in test scores is explained (at least partly) by pre-existing group differences, not by the program. This is what makes it a confound rather than just a coincidental correlation — it is a systematic alternative explanation.

Random assignment is the primary tool for defeating confounds because it distributes all pre-existing differences — known and unknown — roughly equally across conditions by chance. When you randomly assign participants to the tutoring program or the control group, the two groups should be equivalent in motivation, ability, family support, and every other variable you could think of (plus the ones you have not thought of). The IV manipulation becomes the only systematic difference. This is why experimental design with random assignment earns the label "high internal validity" — confounds have been neutralized by design, not just measured and controlled statistically.

The major **threats to internal validity** each represent a specific failure mode. **History effects** occur when an external event happens during the study and affects one group more than the other. **Maturation** is a problem in longitudinal designs: participants naturally change over time, and this change could be mistaken for a treatment effect. **Regression to the mean** occurs when participants are selected because they scored at an extreme, and subsequent scores naturally drift toward average regardless of any intervention. **Demand characteristics** occur when participants infer the study's hypothesis and modify their behavior accordingly. Each threat is worth naming specifically because each has a specific remedy — and recognizing the threat is the first step toward designing around it.
