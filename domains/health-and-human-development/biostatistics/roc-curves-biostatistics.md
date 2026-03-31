---
id: roc-curves-biostatistics
title: ROC Curves and AUC Analysis
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: diagnostic-test-evaluation
  type: hard
- id: logistic-regression-biostatistics
  type: soft
builds-toward:
- cox-proportional-hazards-detailed
tags:
- ROC
- AUC
- discrimination
- threshold
- sensitivity
- specificity
stage: advanced
status: validated
---

# ROC Curves and AUC Analysis

## Core Idea
A Receiver Operating Characteristic (ROC) curve plots sensitivity (true positive rate) against 1 - specificity (false positive rate) across all possible classification thresholds for a continuous diagnostic test or prediction model. Each point on the curve represents a different threshold, tracing the tradeoff between detecting true positives and generating false positives. The Area Under the ROC Curve (AUC) summarizes overall discriminative ability: AUC = 0.5 indicates no discrimination (equivalent to random guessing), AUC = 1.0 indicates perfect discrimination. AUC has a concordance interpretation — it equals the probability that a randomly chosen diseased individual has a higher test value than a randomly chosen non-diseased individual. ROC analysis separates discrimination (can the model distinguish cases from non-cases?) from calibration (are the predicted probabilities accurate?).

## Questions

```yaml
- question: "Two diagnostic models for predicting heart failure have AUCs of 0.85 and 0.72. A colleague claims the first model is always better for clinical use. What important caveat is missing?"
  type: multiple-choice
  options:
    - "AUC cannot be compared between models"
    - "AUC measures discrimination across all thresholds, but at the specific clinical threshold used in practice, the model with lower AUC might have better sensitivity or specificity"
    - "The model with higher AUC is always better at every threshold"
    - "AUC is only valid for binary outcomes, not heart failure severity"
  answer: 1
  explanation: "AUC is a summary measure that averages performance across all possible thresholds, including many that would never be used clinically. Two ROC curves can cross — Model A may be better at high-sensitivity thresholds while Model B is better at high-specificity thresholds. The model with higher overall AUC may perform worse at the exact clinical decision threshold. Partial AUC (restricted to clinically relevant regions) or threshold-specific sensitivity/specificity may be more informative for clinical decisions."

- question: "A prediction model has an AUC of 0.50. This means the model is performing worse than random chance."
  type: true-false
  answer: false
  explanation: "AUC = 0.50 means the model has no discriminative ability — it performs exactly at chance level. It cannot distinguish between cases and controls better than flipping a coin. An AUC below 0.50 would mean the model's predictions are inversely related to the outcome (it systematically assigns higher scores to non-cases), which can be corrected by reversing the prediction direction. AUC = 0.50 is the baseline of no information, not worse than chance."

- question: "A logistic regression model predicting diabetes has an AUC of 0.82 and appears well-discriminating, but a calibration plot shows it systematically overestimates risk — predicting 40% when the actual risk is 20%. Is the model's AUC still valid?"
  type: multiple-choice
  options:
    - "No — poor calibration invalidates the AUC"
    - "Yes — AUC measures discrimination (ranking), not calibration (absolute probability accuracy); the model correctly ranks high-risk above low-risk even if the absolute probabilities are wrong"
    - "The AUC should be recalculated after recalibrating the model"
    - "AUC and calibration always agree — a well-discriminating model must be well-calibrated"
  answer: 1
  explanation: "Discrimination and calibration are independent properties. A model can perfectly rank patients by risk (high AUC) while systematically overestimating or underestimating absolute probabilities (poor calibration). AUC reflects only whether the model assigns higher predicted probabilities to actual cases than to actual non-cases — the ranking. Clinical decisions based on absolute risk thresholds (e.g., 'treat if predicted risk > 10%') require both good discrimination and good calibration."

- question: "Explain the concordance interpretation of AUC and why it makes AUC intuitive as a measure of discrimination."
  type: short-answer
  answer: "AUC equals the probability that if you randomly select one diseased person and one non-diseased person, the model assigns a higher predicted probability to the diseased person. An AUC of 0.85 means that in 85% of randomly drawn case-control pairs, the model correctly identifies who has the disease. This interpretation makes AUC intuitive because it directly measures what discrimination means: the ability to rank cases above non-cases."
  explanation: "The concordance interpretation connects the geometric area under the curve to a concrete probabilistic statement about pairwise comparisons. It also explains why AUC = 0.5 is the chance baseline: random guessing would correctly rank a random pair 50% of the time. The concordance statistic (C-statistic) generalizes this concept to survival analysis, where it measures the probability that a subject who experiences the event sooner has a higher predicted risk."
```

## Explainer

From diagnostic test evaluation, you know that any test with a continuous measurement (blood glucose, tumor marker, risk score) requires a threshold to classify subjects as positive or negative. Lowering the threshold increases sensitivity (you catch more true cases) but decreases specificity (you also flag more healthy people). Raising the threshold does the opposite. The **ROC curve** displays this entire tradeoff at once by plotting sensitivity (y-axis) against 1 - specificity (x-axis) as the threshold sweeps from its minimum to maximum value.

The ROC curve always starts at (0, 0) — the highest possible threshold where everything is classified as negative (zero sensitivity, perfect specificity) — and ends at (1, 1) — the lowest possible threshold where everything is positive (perfect sensitivity, zero specificity). A perfect test has a curve that shoots straight up to (0, 1) and then across to (1, 1), hugging the upper-left corner. A useless test lies along the diagonal from (0, 0) to (1, 1), because raising sensitivity and raising the false positive rate occur at the same rate — the test contains no information.

The **AUC** collapses the entire curve into a single number. It has an elegant probabilistic interpretation: AUC equals the probability that a randomly chosen diseased subject has a higher test value than a randomly chosen non-diseased subject. An AUC of 0.90 means that 90% of all case-control pairs are correctly ordered by the model. This makes AUC a natural measure of **discrimination** — the model's ability to rank subjects by risk. Conventional benchmarks (though context-dependent) consider AUC of 0.7-0.8 as acceptable, 0.8-0.9 as excellent, and above 0.9 as outstanding.

However, AUC has limitations. It summarizes performance across all thresholds, including many that are clinically irrelevant. If you only care about high-sensitivity operating points (screening tests), the part of the ROC curve at low sensitivity is irrelevant but still contributes to the AUC. Two models with identical AUC can have very different performance at the threshold you would actually use. Furthermore, AUC measures discrimination but not **calibration** — whether the predicted probabilities are accurate. A model that assigns probability 0.8 to everyone with disease and 0.6 to everyone without has perfect discrimination (AUC = 1.0) but terrible calibration. For clinical decisions based on absolute risk thresholds, both discrimination and calibration matter, and AUC alone is insufficient.
