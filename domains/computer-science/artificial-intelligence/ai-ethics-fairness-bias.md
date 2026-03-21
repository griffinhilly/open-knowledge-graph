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

## Questions

```yaml
- question: "A loan approval algorithm achieves demographic parity: it approves 40% of applicants from every racial group. However, Group A has a 5% historical default rate and Group B has a 25% default rate. Which statement best describes the fairness situation?"
  type: multiple-choice
  options:
    - "The algorithm is fair because it treats every group identically at the point of decision"
    - "The algorithm satisfies demographic parity but likely violates calibration — among those approved, group B members are far more likely to default"
    - "The algorithm satisfies equalized odds because approval rates are equal across groups"
    - "The algorithm has no bias because it does not use race as an input feature"
  answer: 1
  explanation: "Demographic parity and calibration are in tension here. Calibration requires that among all people given a given risk score, the actual outcome rate matches the score — regardless of group. If Group B's true default rate is 25% but they're approved at the same rate as Group A (5% default rate), the model's scores cannot simultaneously be well-calibrated for both groups. Option A is the common misconception that equal treatment equals fairness. Option C confuses demographic parity with equalized odds. Option D ignores proxy discrimination — features correlated with race can produce disparate impact even without explicit race inputs."

- question: "Why can't an AI classifier simultaneously satisfy demographic parity, equalized odds, and calibration in most real-world settings?"
  type: multiple-choice
  options:
    - "Because current computing power is insufficient to optimize all three objectives simultaneously"
    - "Because these metrics require perfectly balanced training data, which rarely exists"
    - "Because when base rates differ between groups, satisfying one definition mathematically precludes satisfying the others"
    - "Because fairness metrics apply to individuals rather than groups, making group-level metrics inherently contradictory"
  answer: 2
  explanation: "This is Choquet's impossibility result (and related theorems). When two groups have different base rates for the outcome — say, different historical default rates — you cannot equalize approval rates (demographic parity), equalize true and false positive rates (equalized odds), AND have scores mean the same thing across groups (calibration) simultaneously. The math forces a trade-off. This is not a data problem or a computational problem; it is a logical consequence of group base rate differences."

- question: "Once an AI system has been deployed with fairness constraints, ongoing monitoring is unnecessary because the fairness properties established at training time persist."
  type: true-false
  answer: false
  explanation: "Distribution shift — changes in the data-generating process over time — can introduce new forms of bias even in systems that were fair at deployment. The population served may change, economic conditions may shift, and correlations between features and outcomes may evolve. Responsible AI practice requires continuous monitoring for disparate impact, not just a one-time audit at training. The EU AI Act and other regulatory frameworks are beginning to codify ongoing monitoring requirements for this reason."

- question: "Choosing which fairness definition (demographic parity, equalized odds, calibration, etc.) to optimize for is ultimately an ethical and political decision, not a purely technical one."
  type: true-false
  answer: true
  explanation: "Because fairness definitions are mathematically incompatible in general, prioritizing one requires a value judgment about whose interests matter more and what kind of errors are more acceptable. Demographic parity emphasizes equal treatment at the decision point. Equalized odds emphasizes equal accuracy across groups. Calibration emphasizes that scores mean the same thing for everyone. Which to prioritize depends on the stakes, the domain (criminal justice vs. loan approval vs. medical screening), and contested social values about equity — not on algorithm design alone."

- question: "Explain why fairness definitions like demographic parity and equalized odds are in tension with each other, and what this means for AI practitioners who want to build 'fair' systems."
  type: short-answer
  answer: "When two groups have different base rates for the predicted outcome (e.g., different actual default rates), equalizing the positive prediction rate across groups (demographic parity) forces the model to approve higher-risk members of one group and reject lower-risk members of another — producing different error rates. Equalized odds demands equal error rates, which then requires different approval rates, violating parity. Calibration requires that the same score means the same risk for both groups, which clashes with forced approval-rate equality. Practitioners must explicitly choose which definition to prioritize based on the context and accept that the choice involves an ethical trade-off, not a technical solution."
  explanation: "This impossibility result means 'build a fair AI' is not a well-posed engineering objective. Practitioners must ask: what kind of fairness, for whom, measured how? Ignoring this leads to false confidence — a system optimized for one metric may be deeply unfair by another equally defensible metric. Making the trade-off explicit and accountable is itself part of responsible AI practice."
```

## Explainer

When you build a classifier or recommendation system, you are encoding decisions that affect people — who gets a loan, who sees a job posting, who is flagged for additional screening. **Algorithmic bias** arises when these decisions systematically disadvantage groups defined by protected attributes like race, gender, age, or disability. The sources are rarely malicious intent. More often, bias enters through training data that reflects historical inequities (a hiring model trained on past decisions inherits past discrimination), through label definitions that embed contested value judgments (what counts as "creditworthy" depends on who defined the threshold), or through feature selection that serves as a proxy for protected attributes (zip code can proxy for race in many contexts).

The challenge deepens when you try to define **fairness** mathematically. Several competing definitions exist, and they are provably incompatible in most real-world settings. **Demographic parity** requires that the positive prediction rate be equal across groups — the same fraction of men and women should be approved for loans. **Equalized odds** requires that the true positive rate and false positive rate be equal across groups — the model should be equally accurate for everyone. **Calibration** requires that among all people given a 70% risk score, 70% actually default, regardless of group. Choquet's impossibility result shows that except in trivial cases, you cannot satisfy all three simultaneously. This means every fairness intervention involves a tradeoff, and choosing which definition to prioritize is an ethical and political decision, not a purely technical one.

Mitigation strategies operate at three stages. **Pre-processing** methods modify the training data — resampling to balance group representation, relabeling potentially biased labels, or learning fair representations that remove protected information while preserving predictive signal. **In-processing** methods add fairness constraints directly to the learning algorithm, such as penalizing disparate impact in the loss function or enforcing equalized odds as a constraint during optimization. **Post-processing** methods adjust the model's outputs after training, for example by choosing different classification thresholds for different groups to equalize false positive rates. Each approach has strengths and limitations: pre-processing is model-agnostic but may discard useful information; in-processing gives the tightest integration but requires modifying the training pipeline; post-processing is easy to implement but can feel like a patch rather than a fix.

Beyond technical mitigation, responsible AI practice requires institutional structures: **bias audits** that measure disparate impact before deployment, transparency mechanisms that allow affected individuals to understand and contest decisions, ongoing monitoring for distribution shift that can introduce new biases over time, and diverse teams whose varied perspectives catch blind spots that homogeneous groups miss. Regulatory frameworks like the EU AI Act are beginning to codify these requirements into law. The core lesson is that fairness is not a box to check once — it is a continuous process of measurement, deliberation, and adjustment that requires both technical skill and ethical reasoning.
