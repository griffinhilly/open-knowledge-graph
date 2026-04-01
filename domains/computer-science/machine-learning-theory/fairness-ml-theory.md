---
id: fairness-ml-theory
title: Fairness in Machine Learning Theory
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: bias-complexity-tradeoff-formal
  type: hard
- id: causal-inference-ml
  type: hard
tags:
- fairness
- bias
- discrimination
- algorithmic-accountability
- ml-ethics
stage: expert
status: validated
---

# Fairness in Machine Learning Theory

## Core Idea
Fairness in machine learning addresses how to build algorithms that treat individuals equitably and do not unfairly discriminate based on sensitive attributes (race, gender, age, etc.). Fairness definitions are formalized through competing metrics: demographic parity (equal representation across groups), equalized odds (equal error rates across groups), calibration (predictions equally reliable across groups), individual fairness (similar individuals treated similarly), and causal fairness (controlling for discrimination via causal graphs). Trade-offs between fairness and accuracy, and between different fairness notions, require careful analysis. Achieving fairness requires understanding sources of bias (data bias, model bias, deployment bias) and applying pre-processing, in-processing, or post-processing mitigation techniques.

## Questions

```yaml
- question: "Demographic parity requires equal prediction rates (positive predictions) across protected groups. Why is this definition problematic?"
  type: short-answer
  answer: "Demographic parity does not account for true differences in outcomes across groups. For example, if historical data shows that one group truly has higher qualifications for jobs, enforcing demographic parity (hiring the same percentage from each group) would hire unqualified candidates from one group, unfairly disadvantaging them and violating merit-based fairness. Additionally, demographic parity is incompatible with other fairness definitions (e.g., calibration) when base rates differ across groups. Demographic parity is appropriate when the underlying outcome should be independent of group membership, but inappropriate when there are legitimate outcome differences."
  explanation: "This highlights the fundamental tension in fairness: different definitions are appropriate for different contexts. The wrong definition can cause harm: enforcing demographic parity inappropriately can hurt the groups it intends to help by lowering standards."

- question: "Equalized odds requires equal false positive and false negative rates across protected groups. How does this relate to fair misclassification?"
  type: multiple-choice
  options:
    - "Equalized odds has no relationship to false positive/negative rates"
    - "Equalized odds ensures that errors affect groups equally, so no group is systematically disadvantaged by misclassification"
    - "Equalized odds only cares about false positives, not false negatives"
    - "Equalized odds is the same as demographic parity"
  answer: 1
  explanation: "Equalized odds (also called 'equal opportunity' in some contexts) requires FPR and FNR to be equal across groups. This ensures that errors (false positives and false negatives) do not systematically disadvantage one group. For example, in hiring, false negatives (qualified candidates rejected) should occur at the same rate for each demographic group, and false positives (unqualified candidates hired) should also be equal. This makes the algorithm equally unreliable for all groups, ensuring fairness in error distribution. Unlike demographic parity, equalized odds allows different positive prediction rates if there are legitimate differences in underlying outcomes, making it more compatible with calibration."

- question: "Calibration requires that predictions are equally accurate/reliable across protected groups. In what situation would calibration conflict with equalized odds?"
  type: multiple-choice
  options:
    - "Calibration always agrees with equalized odds; they cannot conflict"
    - "When base rates (true outcome rates) differ significantly across groups, satisfying both calibration and equalized odds is mathematically impossible"
    - "Calibration and equalized odds only conflict when the model has very high accuracy"
    - "There is no mathematical conflict; disagreement is purely semantic"
  answer: 1
  explanation: "This is a fundamental impossibility result in fairness: when base rates differ (e.g., disease prevalence differs across demographics, or historical hiring rates differ), satisfying both calibration and equalized odds simultaneously is mathematically impossible. Calibration says P(Y=1|pred=1, group=A) should equal P(Y=1|pred=1, group=B), but equalized odds says FNR should be equal. These constraints are incompatible when base rates differ. Practitioners must choose which fairness definition to prioritize, understanding the implications of this choice for different groups."

- question: "What is the difference between individual fairness (similar individuals treated similarly) and group fairness (equitable treatment of demographic groups)?"
  type: true-false
  answer: true
  explanation: "Individual fairness asks: do similar individuals (in relevant attributes) receive similar predictions/treatment, regardless of protected attributes? This requires defining similarity metrics on non-protected attributes. Group fairness asks: do demographic groups receive equitable treatment on average? These are complementary: individual fairness prevents arbitrary discrimination but does not address systemic disparities; group fairness addresses systemic disparities but allows individual variation if the group average is fair. A system can satisfy one without the other: it could be individually fair yet have group disparities (if qualifications differ), or group-fair yet individually unfair (if similar individuals are treated differently). Achieving both simultaneously requires careful design and may be impossible in some settings."
```

## Explainer

Fairness in machine learning is both a technical and societal challenge: how do we build algorithms that make equitable decisions without systematically disadvantaging groups based on protected attributes (race, gender, age, etc.)? The challenge is technical because fairness is not a single well-defined concept but a collection of competing definitions, each appropriate in different contexts and mathematically incompatible with others.

**Fairness Definitions**: Practitioners have formalized multiple fairness notions:

1. **Demographic Parity**: P(pred=1 | group=A) = P(pred=1 | group=B). The positive prediction rate is equal across groups. Appropriate when outcomes should be independent of group membership. Problematic when legitimate outcome differences exist.

2. **Equalized Odds (Equal Opportunity)**: FPR and FNR are equal across groups: P(pred=1 | Y=0, group=A) = P(pred=1 | Y=0, group=B) and P(pred=0 | Y=1, group=A) = P(pred=0 | Y=1, group=B). Errors affect groups equally. Appropriate when you want equal error rates regardless of outcome distribution.

3. **Calibration**: P(Y=1 | pred=1, group=A) = P(Y=1 | pred=1, group=B). Predictions are equally reliable/well-calibrated across groups. Appropriate for decision-making where you need reliable confidence estimates.

4. **Individual Fairness**: Similar individuals (on relevant attributes) are treated similarly, regardless of group membership. Requires defining a similarity metric and ensures consistency. Appropriate when arbitrary discrimination is the concern.

5. **Causal Fairness**: Control for direct causal discrimination while allowing indirect effects. Use causal graphs to distinguish fair (due to qualifications) vs. unfair (due to bias) outcome differences. Appropriate when you want to identify and eliminate discriminatory causation.

**The Fairness-Accuracy Trade-off**: Enforcing fairness often reduces overall accuracy. For example, demographic parity might require predicting more positive outcomes for an under-represented group even if the model is less confident, raising false positive rates. This trade-off is unavoidable in many settings, and practitioners must decide which is more important: overall accuracy or fair distribution of errors/decisions.

**Incompatibility Results**: Different fairness definitions cannot be simultaneously satisfied when base rates differ. For example, with different outcome rates across groups, satisfying both demographic parity and calibration is impossible. Similarly, equalized odds and demographic parity are generally incompatible unless outcome rates are identical across groups. This impossibility means choosing a fairness definition requires understanding its implications.

**Sources of Bias**:

1. **Data Bias**: Training data reflects historical discrimination (e.g., hiring data where women were historically under-hired). The model learns to replicate this discrimination.

2. **Model Bias**: The model's capacity and structure can introduce disparities (e.g., a model optimized for overall accuracy may perform worse for under-represented groups).

3. **Deployment Bias**: How the model is used in practice can create disparities (e.g., a model is applied differently across groups, or feedback loops reinforce historical biases).

**Mitigation Approaches**:

1. **Pre-processing**: Clean and rebalance training data to remove historical bias before model training.

2. **In-processing**: Modify the learning objective to incorporate fairness constraints during training (adversarial debiasing, fair regularization, constrained optimization).

3. **Post-processing**: Adjust model predictions or thresholds to satisfy fairness constraints after training (threshold optimization per group).

4. **Causal Approaches**: Use causal graphs to identify and control for discriminatory pathways while allowing legitimate outcome differences (e.g., education level can affect hiring decisions, but race cannot).

**Theoretical Results**:
- **Fairness-Accuracy Pareto Frontier**: For any fairness definition, there is a Pareto trade-off: improving fairness generally reduces accuracy, and vice versa. The optimal point depends on application priorities.
- **Impossibility of All Fairness Notions**: No single algorithm can simultaneously satisfy all fairness definitions when constraints conflict.
- **Group vs. Individual Fairness Trade-off**: Focusing on group fairness may violate individual fairness and vice versa.

**Practical Implementation**:
- **Fairness Metrics**: Libraries like Fairlearn, AIF360 provide tools to measure and audit fairness.
- **Fairness-Accuracy Trade-off Visualization**: Plot accuracy and fairness across different thresholds to understand trade-offs.
- **Causal Fairness**: Use do-calculus and causal graphs to identify legitimate vs. discriminatory pathways.
- **Stakeholder Engagement**: Define fairness in collaboration with affected communities; fairness is not solely a technical choice but a societal values choice.

**Challenges and Open Questions**:
- Defining fairness requires value judgments; there is no purely technical answer to "what is fair?"
- Real-world distributions are complex; simplistic fairness definitions may be inappropriate.
- Gaming and unintended consequences: enforcing one fairness metric may create perverse incentives (e.g., demographic parity may incentivize hiring less-qualified candidates, ultimately hurting those groups).
- Intersectionality: fairness across multiple protected attributes (race AND gender) is more complex than single-attribute fairness.
- Temporal fairness: fairness definitions that hold at one time may not hold later if the world changes.

**Emerging Directions**:
- **Context-Aware Fairness**: Develop fairness frameworks tailored to specific domains (hiring, lending, criminal justice) with stakeholder input.
- **Fairness Over Time**: Study how to maintain fairness as distributions shift and feedback loops operate.
- **Causal Fairness at Scale**: Integrate causal inference with machine learning to automate fair decision-making.
- **Fairness in Foundations Models**: Ensure large language and vision models are fair and do not amplify historical biases.

Fairness in ML is not a solved problem but an active, multidisciplinary challenge combining machine learning, causal inference, ethics, and policy. Practitioners must recognize that technical solutions alone are insufficient; fairness requires ongoing dialogue with stakeholders and commitment to equitable outcomes.
