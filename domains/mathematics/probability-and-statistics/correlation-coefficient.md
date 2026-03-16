---
id: correlation-coefficient
title: Correlation Coefficient
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: scatterplots-and-correlation
  type: hard
- id: measures-of-spread
  type: soft
builds-toward:
- linear-regression-basics
tags:
- correlation
- pearson
- r
- association
stage: formal-systems
status: draft
---

# Correlation Coefficient

## Core Idea
The Pearson correlation coefficient r measures linear association between two variables, ranging from -1 (perfect negative linear relationship) to +1 (perfect positive linear relationship), with 0 indicating no linear association. Defined as r = Cov(X,Y)/(σ_X × σ_Y), correlation is unitless and symmetric in X and Y. A correlation near 0 doesn't mean no relationship—it indicates no linear relationship; nonlinear associations may be strong but have correlation near 0.

## How It's Best Learned
Compute r for various datasets and compare to scatterplot. Generate data with specified correlations. Show examples where r = 0 but strong relationships exist.

## Common Misconceptions
Thinking r = 0 implies independence or no association. Confusing correlation with causation. Believing |r| > 0.5 indicates strong relationship (depends on context).

## Questions

```yaml
- question: "A researcher computes r = 0.02 between two variables and concludes there is essentially no relationship. What is the problem with this conclusion?"
  type: multiple-choice
  options:
    - "There is no problem — r = 0.02 is so close to zero that no relationship is confirmed"
    - "The sample size might be too small to compute r reliably"
    - "r near zero only rules out a linear relationship; a strong nonlinear relationship may still exist"
    - "r should always be computed as an absolute value, so 0.02 might be negative"
  answer: 2
  explanation: "r = Cov(X,Y)/(σ_X·σ_Y) measures only *linear* association. A perfect quadratic relationship (e.g., Y = X²) or a sinusoidal relationship produces r ≈ 0 even though the variables are strongly dependent. Before concluding 'no relationship,' always examine a scatterplot. r near zero is a reliable indicator of no *linear* pattern, not of no relationship at all."

- question: "A study finds r = 0.85 between ice cream sales and drowning rates across summer months. This correlation proves that eating ice cream increases the risk of drowning."
  type: true-false
  answer: false
  explanation: "Correlation does not imply causation. Both ice cream sales and drowning rates rise in summer because of a common cause: hot weather brings more people to pools and beaches. This is a classic example of a confounding variable (season/temperature) producing high correlation between two variables that have no direct causal link. High |r| indicates a strong linear association, not a causal mechanism."

- question: "Two variables have Pearson r = 0. Does this guarantee they are statistically independent? Explain."
  type: short-answer
  answer: "No. r = 0 only guarantees no linear association. Two variables can be strongly dependent in a nonlinear way (e.g., a U-shaped or circular relationship) while still having r = 0. Independence implies r = 0, but r = 0 does not imply independence."
  explanation: "Independence is a stronger condition than zero correlation. For example, if X is drawn uniformly from [-1, 1] and Y = X², then Cov(X,Y) = 0 (by symmetry), so r = 0 — yet knowing X tells you exactly what Y is. Statistical independence requires that the joint distribution factorizes: P(X,Y) = P(X)·P(Y) for all values, which is a much stricter requirement than uncorrelatedness."
```

## Explainer

When you examined scatterplots, you developed an intuitive sense for association: points that trend upward together suggest a positive relationship; points that trend in opposite directions suggest a negative one; a shapeless cloud suggests none. The **Pearson correlation coefficient r** turns that intuition into a single number. It measures how closely the data points cluster around a straight line, ranging from −1 (a perfect downward line) through 0 (no linear trend) to +1 (a perfect upward line).

The formula is r = Cov(X, Y) / (σ_X · σ_Y), where Cov(X, Y) is the covariance — roughly, how much X and Y vary together — and σ_X, σ_Y are the standard deviations of each variable. Dividing by the standard deviations standardizes the result, which is why r is unitless and always falls in [−1, 1]. You can swap X and Y without changing r (it is symmetric), and multiplying either variable by a positive constant leaves r unchanged. These properties make r a clean, interpretable summary of linear association.

The phrase **linear association** is doing heavy lifting in that definition. r only detects *straight-line* patterns. A dataset where Y = X² (a perfect parabola) has r = 0, because the parabola is symmetric: for every upward movement of Y as X goes from 0 to 1, there is an equal upward movement as X goes from −1 to 0, and these cancel. The scatterplot would show an obvious strong relationship; r would tell you nothing. This is why examining the scatterplot before and after computing r is essential — r summarizes one aspect of the relationship, not the whole picture.

The most common misuse of r is treating it as evidence of causation. Two variables can be highly correlated because one causes the other, because both are caused by a third variable, or purely by chance in a small sample. Ice cream sales and sunburn rates both spike in summer; their correlation is high, but neither causes the other. Identifying correlation is the *beginning* of causal inquiry, not the end. Establishing causation requires controlled experiments or careful causal reasoning beyond what r can provide.

Finally, what counts as a "strong" correlation depends on context. In physics experiments, r = 0.95 might be disappointing. In social science, r = 0.4 between a questionnaire score and a real-world outcome might be remarkably good. The sign of r tells you direction; the magnitude tells you how tightly the points cluster around a line; but interpreting whether that magnitude is meaningful requires knowing the domain, the sample size, and what you are trying to predict. r is a tool — its value only becomes interpretable in context.
