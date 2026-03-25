---
id: fairness-machine-learning
title: Fairness in Machine Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: ai-ethics-fairness-bias
  type: hard
tags:
- fairness
- bias
- discrimination
stage: advanced
status: validated
---

# Fairness in Machine Learning

## Core Idea
Fairness addresses systematic bias that discriminates against protected groups. Fairness definitions include demographic parity (equal prediction rates), equalized odds (equal error rates across groups), and calibration (equal accuracy per group). Achieving fairness requires measuring bias, selecting appropriate fairness metrics, and retraining or post-processing models.

## Questions

```yaml
- question: "A recidivism prediction model is well-calibrated across racial groups — among defendants who receive a 70% risk score, roughly 70% actually reoffend, regardless of race. However, the model's false positive rate is higher for Black defendants than for White defendants. Which of the following is true?"
  type: multiple-choice
  options:
    - "The model satisfies both calibration and equalized odds"
    - "The model satisfies calibration but violates equalized odds"
    - "The model violates calibration because error rates differ across groups"
    - "The model must be retrained — both calibration and equalized odds can always be satisfied simultaneously"
  answer: 1
  explanation: "Calibration requires that predicted probabilities correspond to actual outcome rates, regardless of group — this is satisfied here. Equalized odds requires that both false positive and false negative rates are equal across groups — the unequal false positive rates mean this is violated. Importantly, option D is wrong: the Chouldechova-Kleinberg impossibility theorem proves that when base rates differ across groups, you cannot simultaneously satisfy calibration and equal error rates. This is the real-world tension exposed in the 2016 ProPublica/Northpointe COMPAS debate."

- question: "Why does demographic parity have a fundamental limitation as a fairness criterion for a medical diagnosis model?"
  type: multiple-choice
  options:
    - "Demographic parity is too computationally expensive to enforce for medical models"
    - "It requires equal positive prediction rates across groups, which would force the model to either over-predict for low-prevalence groups or under-predict for high-prevalence groups"
    - "Medical models are exempt from fairness requirements under HIPAA regulations"
    - "Demographic parity only measures false positives, ignoring the impact of false negatives on patient care"
  answer: 1
  explanation: "If disease rates genuinely differ between groups (e.g., a condition is more prevalent in older adults), enforcing equal positive prediction rates forces the model to make incorrect predictions for someone. Either it over-predicts for the low-prevalence group (unnecessary interventions) or under-predicts for the high-prevalence group (missed diagnoses). Demographic parity ignores whether predictions are *correct* — it only measures rates. A model can satisfy demographic parity while being less accurate for both groups than a model that ignores group membership entirely."

- question: "A machine learning model that satisfies demographic parity necessarily also satisfies equalized odds."
  type: true-false
  answer: false
  explanation: "Demographic parity requires equal positive prediction rates across groups. Equalized odds requires equal true positive *and* false positive rates (i.e., the model makes correct and incorrect predictions at the same rates for each group). These are distinct definitions. A model can have equal prediction rates while having very different error structures — for example, one group's positives could all be true positives while another group's include many false positives. Satisfying one definition says nothing about the other."

- question: "When base rates of the target outcome differ between groups, it is mathematically impossible to simultaneously achieve calibration, equal false positive rates, and equal false negative rates."
  type: true-false
  answer: true
  explanation: "This is the Chouldechova-Kleinberg impossibility theorem. If Group A has a higher base rate of the positive outcome than Group B, then a calibrated classifier will necessarily assign higher predicted probabilities to Group A members, which means equalizing error rates while maintaining calibration is mathematically impossible. One of the three properties must be sacrificed. This is not a failure of engineering — it is a mathematical constraint, which is why the choice of fairness metric must be a normative decision, not a technical one."

- question: "Why must the choice of fairness metric depend on the application context rather than being defined universally for all machine learning systems?"
  type: short-answer
  answer: "Different applications assign different costs to different types of errors. In criminal justice, a false positive (wrongly predicting reoffending) restricts an innocent person's liberty — making equal false positive rates a priority. In medical screening, a false negative (missing a disease) may be fatal — making equal true positive rates (equal opportunity) more important. In lending, calibration may be legally required to prevent redlining. Because the Chouldechova-Kleinberg impossibility theorem shows these definitions cannot all be satisfied at once when base rates differ, the choice of which fairness property to prioritize is an ethical judgment about which type of error is more harmful — a question that cannot be answered by mathematics alone."
  explanation: "This is the central practical lesson of fairness in ML: there is no 'default' fairness criterion. Each definition encodes a value judgment about what counts as fair, and different stakeholders in different domains may reasonably disagree. Pre-processing, in-processing, and post-processing interventions all optimize for whichever metric the designer selects. A system that appears 'fair' by one definition may appear systematically discriminatory by another — which is why transparency about which fairness metric was chosen, and why, is essential."
```

## Explainer

From AI ethics, you understand that machine learning systems can perpetuate and amplify societal biases present in their training data. Fairness in machine learning takes this concern from the conceptual level to the technical: it provides formal mathematical definitions of what "fair" means, methods to measure whether a model meets those definitions, and interventions to correct unfairness. The challenge is that fairness is not a single concept — there are multiple competing definitions, and a landmark impossibility result shows that most of them cannot be satisfied simultaneously.

**Demographic parity** (also called statistical parity) requires that the model's positive prediction rate is equal across groups — for instance, that a hiring algorithm recommends the same proportion of male and female candidates. This sounds straightforward, but it has a serious limitation: it ignores the actual qualifications of individuals. If one group genuinely has higher rates of the target outcome (e.g., a medical condition), enforcing equal prediction rates means the model must either over-predict for one group or under-predict for another, reducing accuracy for everyone. Demographic parity is blind to whether the predictions are *correct* — it only looks at rates.

**Equalized odds** addresses this by requiring that the model's error rates (both false positive and false negative rates) are equal across groups. This is a more nuanced criterion: it allows overall prediction rates to differ if the groups genuinely differ in base rates, but demands that the model makes mistakes at the same rate for each group. A related criterion, **equal opportunity**, relaxes this to require only equal true positive rates — ensuring that qualified individuals in all groups have the same chance of receiving a positive prediction. **Calibration** requires that among all individuals who receive a predicted probability of, say, 70%, approximately 70% actually have the positive outcome regardless of group membership. The Chouldechova-Kleinberg impossibility theorem proves that when base rates differ across groups, you cannot simultaneously achieve calibration, equal false positive rates, and equal false negative rates — you must choose which form of fairness matters most for your application.

Interventions to improve fairness operate at three stages. **Pre-processing** modifies the training data to remove bias before the model ever sees it — techniques include resampling, reweighting, or transforming features to remove correlations with protected attributes. **In-processing** modifies the learning algorithm itself, adding fairness constraints or regularization terms to the objective function so the model optimizes for both accuracy and fairness simultaneously. **Post-processing** adjusts the model's predictions after training, applying group-specific thresholds to equalize the desired fairness metric. Each approach involves tradeoffs: pre-processing may discard useful information, in-processing makes training more complex, and post-processing can feel like a patch rather than a fix. The choice depends on what kind of fairness is most important in context — criminal justice, lending, healthcare, and hiring each prioritize different definitions because the costs of different types of errors differ dramatically across these domains.
