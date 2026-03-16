---
id: ai-ethics-fairness-bias
title: AI Ethics, Fairness, and Bias
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: soft
tags:
- ethics
- fairness
- bias-mitigation
stage: advanced
status: draft
---

# AI Ethics, Fairness, and Bias

## Core Idea
AI systems inherit biases from data, labels, and design, causing harms along protected attributes. Fairness definitions (demographic parity, equalized odds) conflict; no universal metric exists. Mitigation: dataset balancing, fairness constraints, debiasing. Regulatory frameworks are emerging.

## How It's Best Learned
Audit a classifier for demographic bias, implement fairness constraints, and measure fairness-accuracy tradeoffs.

## Common Misconceptions
Bias cannot be eliminated, only understood and mitigated. Fairness requires explicit measurement and involves trade-offs.

## Explainer

When you build a classifier or recommendation system, you are encoding decisions that affect people — who gets a loan, who sees a job posting, who is flagged for additional screening. **Algorithmic bias** arises when these decisions systematically disadvantage groups defined by protected attributes like race, gender, age, or disability. The sources are rarely malicious intent. More often, bias enters through training data that reflects historical inequities (a hiring model trained on past decisions inherits past discrimination), through label definitions that embed contested value judgments (what counts as "creditworthy" depends on who defined the threshold), or through feature selection that serves as a proxy for protected attributes (zip code can proxy for race in many contexts).

The challenge deepens when you try to define **fairness** mathematically. Several competing definitions exist, and they are provably incompatible in most real-world settings. **Demographic parity** requires that the positive prediction rate be equal across groups — the same fraction of men and women should be approved for loans. **Equalized odds** requires that the true positive rate and false positive rate be equal across groups — the model should be equally accurate for everyone. **Calibration** requires that among all people given a 70% risk score, 70% actually default, regardless of group. Choquet's impossibility result shows that except in trivial cases, you cannot satisfy all three simultaneously. This means every fairness intervention involves a tradeoff, and choosing which definition to prioritize is an ethical and political decision, not a purely technical one.

Mitigation strategies operate at three stages. **Pre-processing** methods modify the training data — resampling to balance group representation, relabeling potentially biased labels, or learning fair representations that remove protected information while preserving predictive signal. **In-processing** methods add fairness constraints directly to the learning algorithm, such as penalizing disparate impact in the loss function or enforcing equalized odds as a constraint during optimization. **Post-processing** methods adjust the model's outputs after training, for example by choosing different classification thresholds for different groups to equalize false positive rates. Each approach has strengths and limitations: pre-processing is model-agnostic but may discard useful information; in-processing gives the tightest integration but requires modifying the training pipeline; post-processing is easy to implement but can feel like a patch rather than a fix.

Beyond technical mitigation, responsible AI practice requires institutional structures: **bias audits** that measure disparate impact before deployment, transparency mechanisms that allow affected individuals to understand and contest decisions, ongoing monitoring for distribution shift that can introduce new biases over time, and diverse teams whose varied perspectives catch blind spots that homogeneous groups miss. Regulatory frameworks like the EU AI Act are beginning to codify these requirements into law. The core lesson is that fairness is not a box to check once — it is a continuous process of measurement, deliberation, and adjustment that requires both technical skill and ethical reasoning.
