---
id: irt-model-fit-comparison
title: IRT Model Comparison and Fit Evaluation
domain: psychology
course: psychometrics
prerequisites:
- id: rasch-model
  type: hard
- id: two-parameter-logistic-model
  type: hard
- id: three-parameter-logistic-model
  type: hard
- id: chi-square-test
  type: soft
- id: probability-distributions
  type: soft
builds-toward:
- computerized-adaptive-testing
tags:
- model-selection
- goodness-of-fit
- likelihood-ratio
- aic-bic
stage: advanced
status: draft
---

# IRT Model Comparison and Fit Evaluation

## Core Idea
Comparing IRT models requires examining fit statistics (likelihood ratio tests, AIC, BIC), item-level residuals, and practical utility. Model selection balances parsimony with empirical fit. A simpler model (Rasch) may be preferred even if more complex models (2PL, 3PL) fit better, depending on measurement goals and resources.

## Explainer

You have now studied three IRT model families: the Rasch (1PL) model, the 2PL, and the 3PL. Each adds one more parameter to account for more item-level variation—the 2PL adds discrimination (how steeply the item distinguishes low from high ability), and the 3PL adds a pseudo-guessing parameter (the probability that a very low-ability examinee gets the item right by chance). The natural question is: which model should you use? The answer requires balancing two competing pressures that should already be familiar from your study of probability and statistical inference—**fit** and **parsimony**.

The most direct statistical tool for comparing nested IRT models is the **likelihood ratio test (LRT)**. Because the Rasch model is a constrained version of the 2PL (with all discriminations fixed to 1), and the 2PL is a constrained version of the 3PL (with all guessing parameters fixed to 0), these models are nested. The LRT compares the log-likelihoods of two models: if the more complex model fits the data significantly better (chi-square test on the difference in log-likelihoods, with degrees of freedom equal to the difference in number of estimated parameters), you have evidence that the additional parameters are justified. When you studied the chi-square test, you encountered this same logic: a significant result means the simpler model's constraints are inconsistent with the data.

However, statistical significance alone is not sufficient for model selection. With large samples—common in psychometric applications—even trivially small improvements in fit can be statistically significant. This is where **information criteria** become essential. The **AIC** (Akaike Information Criterion) penalizes model complexity as 2k − 2ln(L), where k is the number of parameters and L is the maximized likelihood. The **BIC** (Bayesian Information Criterion) applies a heavier penalty, 2k·ln(n) − 2ln(L), making it more conservative against overfitting in large samples. Lower values are better for both. When a 3PL model has lower AIC than the Rasch model, the gain in fit outweighs the cost of the additional parameters by the AIC's metric; the model comparison is essentially asking whether the extra parameters are "earning their keep."

Beyond global fit, **item-level residuals** are equally important. A model can fit overall while specific items misfit badly—individual item response functions may not match the model's predicted curves. Infit and outfit statistics flag items where observed response patterns diverge from the model's expectations, either across the full ability range (outfit) or near the item's difficulty level (infit). A model that fits globally but has many misfitting items is not trustworthy for measuring those dimensions.

The final and often decisive factor is **practical utility**. The Rasch model has a unique property: when its assumptions hold, person ability and item difficulty are on the same scale, enabling sample-independent item calibration—items calibrated on one sample can be used to measure a different sample without re-estimation. This property makes Rasch models especially valuable for large-scale testing programs, adaptive testing, and test equating. If the 2PL fits slightly better than Rasch by AIC but item discriminations vary only modestly, a psychometrician might prefer Rasch for its measurement properties rather than the marginal fit gain. Model selection in IRT is not a statistical algorithm—it is a judgment that weighs empirical evidence, theoretical commitments, and the uses to which the test will be put.
