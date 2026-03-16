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

## Explainer

From your study of validity, you know that a test score means something only in relation to what it is supposed to measure and what decisions it is supposed to support. A cut score is the point at which that measurement gets translated into a binary action: pass or fail, clinical or non-clinical, proficient or below-proficient. Every time a number becomes a decision, a **cut score** has been applied — either explicitly or implicitly. The challenge is that the score distribution is continuous while the decisions are categorical, and no cut point is free of error.

To understand what happens at a cut score, start with the normal distribution you've already studied. Imagine you are screening for depression using a questionnaire, and you know from prior validation research that people above a certain score are much more likely to have clinical depression. If you set your cut score too low, you will flag many people who are not actually depressed — these are **false positives**. If you set it too high, you will miss people who genuinely need help — these are **false negatives**. The technical terms for the tradeoff are **sensitivity** (the probability of correctly identifying a true case — avoiding false negatives) and **specificity** (the probability of correctly clearing a non-case — avoiding false positives). Moving the cut score in one direction improves one at the expense of the other.

The **ROC curve** (receiver operating characteristic curve) is the standard tool for visualizing this tradeoff. It plots sensitivity on the y-axis against (1 - specificity) on the x-axis across every possible cut score. A perfect test would pass through the upper-left corner — 100% sensitivity and 100% specificity simultaneously. A useless test (no better than chance) would fall on the diagonal. The area under the ROC curve (AUC) summarizes overall discriminating power, independent of any particular cut score. The ROC curve lets you see not just where a test stands but where *you* should stand — which cut score to use depends on the consequences of each error type, not on any abstract notion of accuracy.

This is the key insight: the optimal cut score is always context-dependent. In a screening program for a serious but treatable condition like tuberculosis, a false negative (missing a case) is far more costly than a false positive (an unnecessary follow-up test). You should therefore set a low cut score to maximize sensitivity, even at the cost of more false positives. In a setting where a positive result triggers an invasive or stigmatizing intervention, false positives are more costly, and you should raise the threshold to protect specificity. **Positive predictive value** (the probability that someone who scores above the cut truly has the condition) and **negative predictive value** (the probability that someone below the cut truly does not) depend not only on sensitivity and specificity but also on **base rate** — how common the condition is in the population being tested. A cut score with impressive sensitivity and specificity in a high-prevalence clinical sample may have poor predictive value when applied to a low-prevalence general population. Defensible cut scores are not chosen arbitrarily or for administrative convenience — they are set after explicitly weighing the costs of different errors against the base rates in the target population.
