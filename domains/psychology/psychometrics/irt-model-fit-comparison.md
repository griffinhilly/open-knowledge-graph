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
- id: probability-density-functions
  type: soft
builds-toward:
- computerized-adaptive-testing
tags:
- model-selection
- goodness-of-fit
- likelihood-ratio
- aic-bic
stage: expert
status: validated
---

# IRT Model Comparison and Fit Evaluation

## Core Idea
Comparing IRT models requires examining fit statistics (likelihood ratio tests, AIC, BIC), item-level residuals, and practical utility. Model selection balances parsimony with empirical fit. A simpler model (Rasch) may be preferred even if more complex models (2PL, 3PL) fit better, depending on measurement goals and resources.

## Questions

```yaml
- question: "A psychometrician tests a 50-item certification exam. The 2PL fits significantly better than the Rasch model by likelihood ratio test (p < .001), but item discrimination parameters vary narrowly (range: 0.85–1.15). The test will be used for large-scale adaptive testing across multiple years and examinee populations. The most defensible model choice is:"
  type: multiple-choice
  options:
    - "Always the 2PL — a statistically significant fit difference must be respected"
    - "The 3PL — if the 2PL fits better than Rasch, the 3PL likely fits even better and should be explored"
    - "The Rasch model — the fit improvement is trivially small, and Rasch's sample-independent calibration property is valuable for adaptive testing and equating across populations"
    - "Neither — the narrow discrimination range means the items are too similar and should be revised before model selection"
  answer: 2
  explanation: "This question illustrates the core principle that model selection in IRT is not a statistical algorithm. With large samples, even trivial improvements in fit can be statistically significant. When item discriminations vary only modestly (0.85–1.15 is close to Rasch's assumption of 1.0), the practical gain from 2PL is minimal, while Rasch's unique measurement property — sample-independent item calibration — is highly valuable for adaptive testing and test equating. Option A commits the error of treating significance as equivalent to practical importance; options B and D introduce unnecessary complexity."

- question: "Why are information criteria like AIC and BIC often preferred over the likelihood ratio test alone for comparing IRT models in large psychometric samples?"
  type: multiple-choice
  options:
    - "Because AIC and BIC can compare non-nested models, whereas the LRT is restricted to nested model families"
    - "Because in large samples the LRT almost always rejects the simpler model regardless of practical significance, while AIC and BIC penalize complexity and measure whether added parameters earn their keep"
    - "Because the LRT requires normality assumptions that are violated in IRT data"
    - "Because AIC is always lower for more complex models, making it a reliable guide to model selection"
  answer: 1
  explanation: "The fundamental problem with using the LRT alone in large psychometric samples is that with thousands of examinees, even trivially small differences in fit produce significant chi-square values. AIC and BIC impose explicit penalties for complexity (AIC: 2k; BIC: k·ln(n)), asking not just 'is the complex model better?' but 'is the improvement worth the extra parameters?' BIC's heavier penalty makes it especially conservative in large samples. Option A is partially true (AIC/BIC can compare non-nested models) but not the *primary* reason for their use here; option D is wrong — lower AIC favors the model that best balances fit and parsimony, not simply the most complex one."

- question: "A model can show acceptable global fit statistics while individual items within it misfit the model's predictions badly."
  type: true-false
  answer: true
  explanation: "Global fit statistics (LRT, AIC, BIC) summarize fit across all items and examinees. A model can achieve good aggregate fit while specific items have response patterns that deviate substantially from the model's predicted item response functions. Item-level infit and outfit statistics are essential diagnostics precisely because global fit can mask local misfitting items. A test with five badly misfitting items among fifty is not trustworthy even if global statistics look acceptable."

- question: "When a likelihood ratio test shows the 3PL fits significantly better than the Rasch model, the 3PL should generally be selected for the final test."
  type: true-false
  answer: false
  explanation: "Statistical significance of the likelihood ratio test is necessary but not sufficient for model selection in IRT. The psychometrician must also weigh the practical utility of the models, the size of the fit improvement relative to added parameters (via AIC/BIC), the stability of parameter estimates, item-level fit, and the intended use of the test. The Rasch model's sample-independent calibration property may be worth the marginal fit cost — a judgment that no statistical test can make automatically."

- question: "What is the unique measurement property of the Rasch model that makes it especially valuable for large-scale or adaptive testing, and under what conditions might this property justify choosing Rasch over a 2PL that fits the data better?"
  type: short-answer
  answer: "The Rasch model's unique property is sample-independent item calibration: when Rasch assumptions hold, person ability and item difficulty are on the same scale, and item parameters estimated from one sample apply to a different sample without re-estimation. This makes Rasch ideal for adaptive testing (items from a calibrated bank can be administered to any examinee), test equating across years, and measurement across different populations. A psychometrician might choose Rasch over a better-fitting 2PL when item discriminations vary only modestly, the fit improvement is practically small, and the test requires the measurement stability that only Rasch provides."
  explanation: "The key distinction is that model selection involves a tradeoff between empirical fit and measurement utility. A model with slightly worse fit but superior theoretical properties for the test's purpose can be the right choice. This is what makes IRT model comparison a professional judgment, not a statistical procedure."
```

## Explainer

You have now studied three IRT model families: the Rasch (1PL) model, the 2PL, and the 3PL. Each adds one more parameter to account for more item-level variation—the 2PL adds discrimination (how steeply the item distinguishes low from high ability), and the 3PL adds a pseudo-guessing parameter (the probability that a very low-ability examinee gets the item right by chance). The natural question is: which model should you use? The answer requires balancing two competing pressures that should already be familiar from your study of probability and statistical inference—**fit** and **parsimony**.

The most direct statistical tool for comparing nested IRT models is the **likelihood ratio test (LRT)**. Because the Rasch model is a constrained version of the 2PL (with all discriminations fixed to 1), and the 2PL is a constrained version of the 3PL (with all guessing parameters fixed to 0), these models are nested. The LRT compares the log-likelihoods of two models: if the more complex model fits the data significantly better (chi-square test on the difference in log-likelihoods, with degrees of freedom equal to the difference in number of estimated parameters), you have evidence that the additional parameters are justified. When you studied the chi-square test, you encountered this same logic: a significant result means the simpler model's constraints are inconsistent with the data.

However, statistical significance alone is not sufficient for model selection. With large samples—common in psychometric applications—even trivially small improvements in fit can be statistically significant. This is where **information criteria** become essential. The **AIC** (Akaike Information Criterion) penalizes model complexity as 2k − 2ln(L), where k is the number of parameters and L is the maximized likelihood. The **BIC** (Bayesian Information Criterion) applies a heavier penalty, 2k·ln(n) − 2ln(L), making it more conservative against overfitting in large samples. Lower values are better for both. When a 3PL model has lower AIC than the Rasch model, the gain in fit outweighs the cost of the additional parameters by the AIC's metric; the model comparison is essentially asking whether the extra parameters are "earning their keep."

Beyond global fit, **item-level residuals** are equally important. A model can fit overall while specific items misfit badly—individual item response functions may not match the model's predicted curves. Infit and outfit statistics flag items where observed response patterns diverge from the model's expectations, either across the full ability range (outfit) or near the item's difficulty level (infit). A model that fits globally but has many misfitting items is not trustworthy for measuring those dimensions.

The final and often decisive factor is **practical utility**. The Rasch model has a unique property: when its assumptions hold, person ability and item difficulty are on the same scale, enabling sample-independent item calibration—items calibrated on one sample can be used to measure a different sample without re-estimation. This property makes Rasch models especially valuable for large-scale testing programs, adaptive testing, and test equating. If the 2PL fits slightly better than Rasch by AIC but item discriminations vary only modestly, a psychometrician might prefer Rasch for its measurement properties rather than the marginal fit gain. Model selection in IRT is not a statistical algorithm—it is a judgment that weighs empirical evidence, theoretical commitments, and the uses to which the test will be put.
