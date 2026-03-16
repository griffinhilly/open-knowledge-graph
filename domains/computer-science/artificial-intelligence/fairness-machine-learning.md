---
id: fairness-machine-learning
title: Fairness in Machine Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: ai-ethics-fairness-bias
  type: hard
builds-toward:
- bias-detection
- algorithmic-auditing
tags:
- fairness
- bias
- discrimination
stage: advanced
status: draft
---

# Fairness in Machine Learning

## Core Idea
Fairness addresses systematic bias that discriminates against protected groups. Fairness definitions include demographic parity (equal prediction rates), equalized odds (equal error rates across groups), and calibration (equal accuracy per group). Achieving fairness requires measuring bias, selecting appropriate fairness metrics, and retraining or post-processing models.

## Explainer

From AI ethics, you understand that machine learning systems can perpetuate and amplify societal biases present in their training data. Fairness in machine learning takes this concern from the conceptual level to the technical: it provides formal mathematical definitions of what "fair" means, methods to measure whether a model meets those definitions, and interventions to correct unfairness. The challenge is that fairness is not a single concept — there are multiple competing definitions, and a landmark impossibility result shows that most of them cannot be satisfied simultaneously.

**Demographic parity** (also called statistical parity) requires that the model's positive prediction rate is equal across groups — for instance, that a hiring algorithm recommends the same proportion of male and female candidates. This sounds straightforward, but it has a serious limitation: it ignores the actual qualifications of individuals. If one group genuinely has higher rates of the target outcome (e.g., a medical condition), enforcing equal prediction rates means the model must either over-predict for one group or under-predict for another, reducing accuracy for everyone. Demographic parity is blind to whether the predictions are *correct* — it only looks at rates.

**Equalized odds** addresses this by requiring that the model's error rates (both false positive and false negative rates) are equal across groups. This is a more nuanced criterion: it allows overall prediction rates to differ if the groups genuinely differ in base rates, but demands that the model makes mistakes at the same rate for each group. A related criterion, **equal opportunity**, relaxes this to require only equal true positive rates — ensuring that qualified individuals in all groups have the same chance of receiving a positive prediction. **Calibration** requires that among all individuals who receive a predicted probability of, say, 70%, approximately 70% actually have the positive outcome regardless of group membership. The Chouldechova-Kleinberg impossibility theorem proves that when base rates differ across groups, you cannot simultaneously achieve calibration, equal false positive rates, and equal false negative rates — you must choose which form of fairness matters most for your application.

Interventions to improve fairness operate at three stages. **Pre-processing** modifies the training data to remove bias before the model ever sees it — techniques include resampling, reweighting, or transforming features to remove correlations with protected attributes. **In-processing** modifies the learning algorithm itself, adding fairness constraints or regularization terms to the objective function so the model optimizes for both accuracy and fairness simultaneously. **Post-processing** adjusts the model's predictions after training, applying group-specific thresholds to equalize the desired fairness metric. Each approach involves tradeoffs: pre-processing may discard useful information, in-processing makes training more complex, and post-processing can feel like a patch rather than a fix. The choice depends on what kind of fairness is most important in context — criminal justice, lending, healthcare, and hiring each prioritize different definitions because the costs of different types of errors differ dramatically across these domains.
