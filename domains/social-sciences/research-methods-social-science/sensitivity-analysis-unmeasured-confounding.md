---
id: sensitivity-analysis-unmeasured-confounding
title: 'Sensitivity Analysis: Robustness to Unmeasured Confounding'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: matching-and-weighting-causal-estimation
  type: hard
- id: covariance-between-random-variables
  type: soft
tags:
- sensitivity-analysis
- unmeasured-confounding
- robustness
stage: expert
status: validated
---

# Sensitivity Analysis: Robustness to Unmeasured Confounding

## Core Idea
All observational causal estimates depend on unverifiable assumptions about unmeasured confounders. Sensitivity analysis quantifies how large unmeasured confounding must be to overturn conclusions. This acknowledges uncertainty while assessing robustness.

## Questions

```yaml
- question: "A researcher estimates that a tutoring program raises test scores by 8 points after matching students on income, prior grades, and school quality. A reviewer asks: 'What about student motivation — more motivated students might both seek tutoring and score higher regardless?' Which response best demonstrates sensitivity analysis thinking?"
  type: multiple-choice
  options:
    - "Motivation is unmeasured, so we cannot draw any causal conclusion from this study"
    - "We estimate that an unmeasured confounder would need to roughly triple the odds of receiving tutoring while also raising baseline scores by 5 points to eliminate our result — we judge that implausibly strong"
    - "Since motivation correlates with tutoring, we should re-run the study controlling for it"
    - "The 8-point effect is large enough that motivation alone couldn't plausibly explain it away"
  answer: 1
  explanation: "Sensitivity analysis responds to the threat of unmeasured confounding not with despair or dismissal, but by quantifying the threshold: how strong would the confounder need to be to overturn the conclusion? The correct response names the specific magnitude, then argues whether confounding that large is plausible. Option A overcorrects (treating all observational evidence as worthless). Option D undercorrects (asserting robustness without quantifying it). Option C misses the point entirely — if motivation is unmeasured, you cannot 'control for it' in a future study without first measuring it."

- question: "A study reports its Rosenbaum sensitivity analysis result as Γ = 2.5. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The study's result could be explained by a confounder present in 2.5% of the sample"
    - "An unmeasured confounder would need to increase the odds of treatment assignment by a factor of 2.5 — holding all measured covariates constant — to eliminate the statistical significance of the result"
    - "The treatment effect is 2.5 times larger than any measured covariate's effect"
    - "The confidence interval spans 2.5 units on either side of the point estimate"
  answer: 1
  explanation: "Gamma parameterizes unmeasured confounding as an odds ratio for treatment assignment. Γ = 2.5 means that to explain away the result, an unmeasured confounder would need to make matched individuals 2.5 times more likely to receive treatment — after accounting for all measured covariates. Higher Γ means greater robustness: the unmeasured confounder required to nullify your result is increasingly implausible. This framing turns the question over to domain expertise: is there a plausible variable that strongly predicts both treatment and outcome but wasn't measured?"

- question: "An unmeasured variable that strongly predicts who receives treatment but has no relationship to the outcome cannot confound the estimated treatment effect, even though it is unmeasured."
  type: true-false
  answer: true
  explanation: "Confounding requires that a variable affect both treatment assignment AND the outcome. A variable that only predicts treatment creates imbalance between groups on that variable, but since it doesn't affect outcomes, it produces no bias in the estimated treatment effect. Similarly, a variable that affects outcomes but is balanced between treatment and control cannot confound either. This is not merely definitional — it has practical implications: sensitivity analysis focuses on unmeasured variables that could plausibly affect both, not just any unmeasured variable."

- question: "Conducting sensitivity analysis on an observational study's results weakens the causal claim by acknowledging that confounding might exist, effectively converting a causal finding into a correlational one."
  type: true-false
  answer: false
  explanation: "Sensitivity analysis doesn't weaken a causal claim — it makes it honest and defensible. The output remains a conditional causal claim: 'If unmeasured confounding is weaker than Γ = 2.5, the effect is causal.' This is not correlation. All observational causal inference is conditional on unverifiable assumptions; sensitivity analysis makes those conditions explicit and evaluable, which strengthens the argument rather than weakening it. Pretending the no-confounding assumption is definitely satisfied — without sensitivity analysis — is the weaker, less honest practice."

- question: "What does sensitivity analysis actually accomplish, and what is the key conceptual shift it demands from researchers?"
  type: short-answer
  answer: "Sensitivity analysis quantifies the threshold at which unmeasured confounding would overturn a conclusion — it does not eliminate or verify the no-confounding assumption. The key shift is treating causal conclusions as conditional rather than absolute: the output becomes 'IF unmeasured confounding is weaker than X, THEN the effect is real,' paired with a substantive argument about whether X is plausible. This converts a hidden, unexamined assumption into an explicit, debatable parameter."
  explanation: "Without sensitivity analysis, the no-unmeasured-confounding assumption lurks implicitly — researchers proceed as if it is satisfied without stating or defending it. With sensitivity analysis, the assumption becomes quantified: you can ask domain experts whether any plausible unmeasured variable could increase treatment odds by a factor of 3. This is a tractable question that marshals subject-matter knowledge and makes the causal argument transparent and contestable. The goal is not to fix the problem (nothing can) but to be honest about its magnitude and argue that it is insufficient to overturn your conclusion."
```

## Explainer

From your work on matching and weighting, you know that these methods balance observed covariates between treatment and control groups — essentially eliminating the influence of confounders you can measure. But matching and weighting cannot touch what you cannot see. The fundamental limitation of any observational study is the **no unmeasured confounding assumption** (also called ignorability or exchangeability): the claim that all variables that affect both treatment assignment and the outcome have been measured and controlled for. This assumption is unverifiable from the data itself. Sensitivity analysis is the discipline of reasoning carefully about how wrong this assumption can be before your conclusion falls apart.

The intuition is best grasped through an example. Suppose you estimate that a job training program raises earnings by $4,000. You have matched participants to comparable non-participants on age, education, and prior employment history. But what if motivated individuals — people with ambition not captured in your measured variables — were both more likely to enroll in the program and more likely to earn more regardless of the program? **Unmeasured confounding by motivation** could explain some or all of the estimated effect. Sensitivity analysis asks: how strong would this unmeasured confounder need to be — how much more likely are motivated people to enroll, and how much more do they earn on average — to reduce the $4,000 estimate to zero? If the answer is "implausibly strong," your conclusion is robust. If a modest, plausible amount of confounding would do it, your conclusion is fragile.

The most widely used formal framework is the **Rosenbaum sensitivity analysis** for matched studies, which parameterizes unmeasured confounding as a single value Γ (gamma): the maximum odds ratio by which an unmeasured confounder could differ between a matched pair. At Γ = 1, no unmeasured confounding exists. As Γ increases, the p-value for your treatment effect eventually crosses the significance threshold. Reporting "results remain significant at Γ = 2" tells readers that an unmeasured confounder would need to double the odds of treatment assignment — holding all measured covariates constant — to explain away the result. Your knowledge of covariance between random variables helps here: confounders do damage in proportion to how strongly they covary with both treatment assignment and the outcome. A variable that strongly predicts treatment but is unrelated to the outcome (or vice versa) cannot confound the estimate, no matter how unobserved it is.

The key conceptual shift sensitivity analysis demands is treating causal conclusions as conditional rather than absolute. The output of an observational study is not "X causes Y" but "if unmeasured confounding is smaller than a certain threshold, X causes Y." Reporting this conditional conclusion honestly, alongside substantive reasoning about whether that threshold is plausible given domain knowledge, is what distinguishes careful causal inference from naive correlation. Sensitivity analysis does not fix unmeasured confounding — nothing can — but it transforms a hidden vulnerability into an explicit, arguable claim about how fragile or robust your finding really is.
