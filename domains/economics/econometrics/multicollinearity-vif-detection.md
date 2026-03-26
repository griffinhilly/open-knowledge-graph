---
id: multicollinearity-vif-detection
title: 'Multicollinearity: Detection Using VIF'
domain: economics
course: econometrics
prerequisites:
- id: multicollinearity
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: condition-number-of-a-matrix
  type: soft
- id: linear-independence
  type: soft
- id: variance-inflation-factor
  type: soft
- id: graphical-diagnostic-tools
  type: soft
- id: breusch-godfrey-test
  type: soft
tags:
- multicollinearity
- diagnostics
stage: advanced
status: validated
---
# Multicollinearity: Detection Using VIF

## Core Idea
The Variance Inflation Factor VIFⱼ = 1 / (1 - Rⱼ²) measures how much variance of β̂ⱼ is inflated by collinearity with other regressors. Rules of thumb: VIF > 10 indicates severe multicollinearity; values 5-10 suggest moderate concern. Correlation matrix and condition number also reveal collinearity patterns.

## Questions

```yaml
- question: "In a regression model, the VIF for variable X₃ is 25. A researcher concludes that the OLS estimate of the coefficient on X₃ is biased. Is this conclusion correct?"
  type: multiple-choice
  options:
    - "Yes — high VIF means the OLS estimator is systematically biased away from the true effect"
    - "No — multicollinearity inflates the variance of β̂₃, making it imprecise, but OLS remains unbiased; bias is not the problem"
    - "Yes — collinearity causes the coefficient to systematically underestimate the true effect of X₃"
    - "No — VIF only detects nonlinearity between predictors, not collinearity"
  answer: 1
  explanation: "This is the central misconception about multicollinearity. OLS remains unbiased under collinearity — the Gauss-Markov conditions do not require orthogonal predictors. What collinearity does is inflate the variance (standard error) of the coefficient estimate, making it imprecise and statistically unreliable. A VIF of 25 means the variance of β̂₃ is 25 times larger than it would be with no collinearity — you have a noisy estimate, not a biased one."

- question: "The auxiliary regression of predictor X₂ on all other predictors yields R² = 0.96. What is the VIF for X₂, and what does it mean?"
  type: multiple-choice
  options:
    - "VIF = 0.04; X₂ has very little collinearity because only 4% of its variation is explained by the others"
    - "VIF = 25; X₂'s coefficient variance is 25 times larger than it would be if X₂ were orthogonal to all other predictors"
    - "VIF = 0.96; X₂ is 96% collinear, which is a moderate concern"
    - "VIF = 4; there is mild multicollinearity requiring attention"
  answer: 1
  explanation: "VIF = 1/(1 − R²) = 1/(1 − 0.96) = 1/0.04 = 25. The auxiliary R² of 0.96 means 96% of X₂'s variation is explained by the other predictors — X₂ is highly redundant. OLS can barely distinguish X₂'s independent contribution, inflating its coefficient's variance 25-fold. A VIF of 25 far exceeds the common threshold of 10, indicating severe multicollinearity."

- question: "A VIF of 1 for a predictor means it is perfectly orthogonal to all other predictors in the model, so no variance inflation is occurring for that coefficient."
  type: true-false
  answer: true
  explanation: "VIF = 1/(1 − Rⱼ²). When Rⱼ² = 0, the auxiliary regression explains none of predictor j's variation — meaning the other predictors share no information with j. VIF = 1/1 = 1 corresponds to a multiplicative inflation of exactly 1 (no inflation). This is the baseline case of perfectly orthogonal design."

- question: "High VIF values are typically a critical problem requiring remediation before a regression model can be used for any purpose."
  type: true-false
  answer: false
  explanation: "Whether high VIF is a problem depends on the goal. For prediction, multicollinearity is largely benign: OLS predictions can remain accurate even with high VIFs, as long as the collinearity structure in the training data mirrors what will be seen in prediction. High VIF is a serious problem for causal interpretation, because it means individual coefficient estimates are noisy and unstable. Remediation (dropping variables, PCA, collecting more data) is necessary when you need to make causal claims about specific predictors."

- question: "Explain what the auxiliary regression underlying VIF measures and why it captures the severity of multicollinearity for a specific predictor."
  type: short-answer
  answer: "The auxiliary regression regresses predictor j on all other predictors in the model. Its R² measures how much of predictor j's variation is already 'explained' by the other predictors — in other words, how redundant j is. If R² is high, the other predictors contain most of j's information, so OLS cannot isolate j's independent effect without large variance in the estimate. VIF = 1/(1 − R²) formalizes this: as j becomes more redundant (R² → 1), VIF → ∞, reflecting the impossibility of separately identifying j's contribution. A VIF close to 1 means j adds genuinely new information."
  explanation: "The auxiliary regression is a regression within a regression — it tests whether one predictor can be predicted from the others. High predictability means low independent information, which means high variance in the main regression's coefficient for that predictor."
```

## Explainer

From your study of multicollinearity, you know the core problem: when predictors move together, OLS has trouble distinguishing their individual effects on the outcome. The coefficient estimates become unreliable — large standard errors, wild sign flips when a variable is added or removed, coefficients that are individually insignificant yet jointly significant. The **Variance Inflation Factor** gives you a precise, interpretable measure of how severe this inflation is for each predictor.

The intuition behind VIFⱼ = 1 / (1 - Rⱼ²) comes from an **auxiliary regression**: regress predictor j on all other predictors in your model. The R² from that auxiliary regression tells you how well the other predictors can "explain" predictor j — in other words, how redundant predictor j is. If Rⱼ² = 0, predictor j is orthogonal to all others, and VIF = 1 (no inflation). If Rⱼ² = 0.9, ninety percent of predictor j's variation is explained by the others, and VIF = 10 (ten times as much variance as you'd have with no collinearity). This connects directly to linear independence: a VIF approaching infinity signals that the columns of your design matrix X are nearly linearly dependent.

The **condition number** of the matrix X'X, which you've encountered, provides a complementary diagnostic. It equals the square root of the ratio of the largest to smallest eigenvalue. Large eigenvalues correspond to directions in predictor space with lots of variation; small eigenvalues correspond to near-collinear combinations. A condition number above 30 is often flagged as problematic. While VIF diagnoses collinearity for individual predictors, the condition number and **eigenvalue decomposition** reveal which combinations of predictors are nearly collinear — useful when the problem involves several predictors interacting.

The harder question is what to do about multicollinearity once detected. OLS remains unbiased — multicollinearity doesn't cause bias, only imprecision. If your goal is prediction rather than causal inference, high VIFs may be tolerable. For causal interpretation, solutions include dropping one of a pair of highly correlated variables, constructing a composite index, using principal components, or collecting more data to increase precision. The key diagnostic insight is this: if removing one variable substantially changes the coefficients on others, you're seeing collinearity in action — the model is not identifying individual effects cleanly.
