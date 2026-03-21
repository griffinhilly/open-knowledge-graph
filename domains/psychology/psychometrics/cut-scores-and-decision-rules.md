---
id: cut-scores-and-decision-rules
title: Cut Scores, Decision Rules, and Classification Accuracy
domain: psychology
course: psychometrics
prerequisites:
- id: validity-in-measurement
  type: hard
- id: effect-size-and-power
  type: soft
- id: normal-distribution
  type: soft
builds-toward:
- test-score-interpretation-frameworks
tags:
- cut-scores
- classification
- decision-making
- sensitivity-specificity
- accuracy
stage: advanced
status: draft
---

# Cut Scores, Decision Rules, and Classification Accuracy

## Core Idea
Cut scores are threshold values that divide test scores into categories (pass/fail, clinical vs. non-clinical, proficiency levels). Setting defensible cut scores requires balancing classification accuracy, consequences of false positives and false negatives, and stakeholder input. Understanding sensitivity, specificity, and positive/negative predictive values is essential for evaluating how well a cut score achieves its intended purpose.

## How It's Best Learned
Use receiver operating characteristic (ROC) curves to explore how different cut scores affect sensitivity and specificity for a diagnostic question. Consider the consequences of different types of errors (false positives vs. false negatives) in specific contexts, such as clinical diagnosis or educational certification.

## Common Misconceptions
- Assuming higher cut scores are always better; higher cuts increase specificity but lower sensitivity, potentially missing cases that need intervention.
- Ignoring the context-dependent nature of optimal cut scores; the best cut depends on the relative costs of false positives and negatives.
- Setting cut scores without reference to a criterion; cut scores should be justified by evidence of validity for the decision being made.

## Questions

```yaml
- question: "A hospital is screening for a rare but fatal infection using a blood test. The infection affects 1% of the population tested. A colleague argues you should set a high cut score to maximize accuracy (minimize total misclassifications). Why is this reasoning flawed?"
  type: multiple-choice
  options:
    - "A high cut score increases sensitivity, which is what matters most in clinical settings"
    - "Overall accuracy is dominated by the majority class, so a high cut score that misses most cases can still appear accurate"
    - "Cut scores should always be set at the mean of the distribution to ensure balance"
    - "Maximizing accuracy requires lowering the cut score when prevalence is below 50%"
  answer: 1
  explanation: "When the condition is rare (1% prevalence), a test that calls everyone negative is 99% accurate — but worthless. 'Overall accuracy' is a misleading metric when base rates are skewed, because correct negatives swamp the total. The relevant question is: what are the relative costs of missing a case (false negative) versus flagging a healthy person (false positive)? For a fatal infection, missing cases is catastrophic, so you want maximum sensitivity — a low cut score — even at the expense of many false positives who will undergo unnecessary follow-up. The cut score decision must be driven by error consequences, not aggregate accuracy."

- question: "A clinician raises the cut score on a depression screening tool from 10 to 15 points. Which of the following best describes what happens?"
  type: multiple-choice
  options:
    - "Sensitivity increases and specificity decreases"
    - "Both sensitivity and specificity increase as the test becomes more discriminating"
    - "Specificity increases and sensitivity decreases"
    - "Positive predictive value falls because more cases are missed"
  answer: 2
  explanation: "Raising the cut score means fewer people score above it, so fewer people are flagged as positive. This reduces false positives (improving specificity — fewer healthy people are incorrectly flagged) but also misses more genuine cases (reducing sensitivity — more true cases fall below the new threshold). The ROC curve makes this tradeoff explicit: every cut score occupies exactly one point on the curve, and moving the threshold always trades one type of accuracy for another. You cannot raise both simultaneously unless you improve the underlying test."

- question: "A diagnostic test with 90% sensitivity and 90% specificity will have a positive predictive value of 90% when applied to any population."
  type: true-false
  answer: false
  explanation: "Positive predictive value (PPV) depends not only on sensitivity and specificity but critically on base rate. In a high-prevalence population (e.g., 50% have the condition), a test with 90/90 sensitivity/specificity has a PPV around 90%. In a low-prevalence population (e.g., 1%), the same test has a PPV of roughly 8% — meaning 92% of positives are false alarms. This is because rare conditions produce many more opportunities for false positives than true positives, swamping the calculation. This is why screening programs in general populations often perform far worse in practice than their validation statistics suggest."

- question: "The ROC curve allows test-makers to identify the single optimal cut score that maximizes both sensitivity and specificity simultaneously."
  type: true-false
  answer: false
  explanation: "The ROC curve visualizes the *tradeoff* between sensitivity and specificity across all possible cut scores — it shows precisely that you cannot have both at once. No cut score occupies the upper-left corner (perfect sensitivity AND perfect specificity) unless the test is perfect. The ROC curve helps you see where the tradeoff lives and choose a point on it based on your context, but the choice always involves accepting more of one error type to reduce the other. The 'optimal' point on the curve does not exist until you specify the relative costs of false positives and false negatives in your particular setting."

- question: "Why does the same sensitivity and specificity produce different positive predictive values in different clinical settings?"
  type: short-answer
  answer: "PPV is determined by sensitivity, specificity, and base rate together. When a condition is rare, even a highly specific test generates many false positives relative to true positives, driving PPV down. The same test in a high-prevalence population produces far fewer false positives relative to true positives, driving PPV up."
  explanation: "Bayes' theorem governs this relationship. PPV = (sensitivity × prevalence) / [(sensitivity × prevalence) + (1 − specificity) × (1 − prevalence)]. As prevalence approaches zero, the denominator is dominated by false positives and PPV collapses regardless of how good the test is. This is why the same test used in a specialist referral clinic (high pre-test probability) produces very different clinical meaning than the same test used in a general population screen. Failing to account for base rates is one of the most common errors in clinical decision-making."
```

## Explainer

From your study of validity, you know that a test score means something only in relation to what it is supposed to measure and what decisions it is supposed to support. A cut score is the point at which that measurement gets translated into a binary action: pass or fail, clinical or non-clinical, proficient or below-proficient. Every time a number becomes a decision, a **cut score** has been applied — either explicitly or implicitly. The challenge is that the score distribution is continuous while the decisions are categorical, and no cut point is free of error.

To understand what happens at a cut score, start with the normal distribution you've already studied. Imagine you are screening for depression using a questionnaire, and you know from prior validation research that people above a certain score are much more likely to have clinical depression. If you set your cut score too low, you will flag many people who are not actually depressed — these are **false positives**. If you set it too high, you will miss people who genuinely need help — these are **false negatives**. The technical terms for the tradeoff are **sensitivity** (the probability of correctly identifying a true case — avoiding false negatives) and **specificity** (the probability of correctly clearing a non-case — avoiding false positives). Moving the cut score in one direction improves one at the expense of the other.

The **ROC curve** (receiver operating characteristic curve) is the standard tool for visualizing this tradeoff. It plots sensitivity on the y-axis against (1 - specificity) on the x-axis across every possible cut score. A perfect test would pass through the upper-left corner — 100% sensitivity and 100% specificity simultaneously. A useless test (no better than chance) would fall on the diagonal. The area under the ROC curve (AUC) summarizes overall discriminating power, independent of any particular cut score. The ROC curve lets you see not just where a test stands but where *you* should stand — which cut score to use depends on the consequences of each error type, not on any abstract notion of accuracy.

This is the key insight: the optimal cut score is always context-dependent. In a screening program for a serious but treatable condition like tuberculosis, a false negative (missing a case) is far more costly than a false positive (an unnecessary follow-up test). You should therefore set a low cut score to maximize sensitivity, even at the cost of more false positives. In a setting where a positive result triggers an invasive or stigmatizing intervention, false positives are more costly, and you should raise the threshold to protect specificity. **Positive predictive value** (the probability that someone who scores above the cut truly has the condition) and **negative predictive value** (the probability that someone below the cut truly does not) depend not only on sensitivity and specificity but also on **base rate** — how common the condition is in the population being tested. A cut score with impressive sensitivity and specificity in a high-prevalence clinical sample may have poor predictive value when applied to a low-prevalence general population. Defensible cut scores are not chosen arbitrarily or for administrative convenience — they are set after explicitly weighing the costs of different errors against the base rates in the target population.
