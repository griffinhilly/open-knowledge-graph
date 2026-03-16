---
id: omitted-variable-bias
title: Omitted Variable Bias
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: ols-assumptions
  type: hard
- id: r-squared-and-model-fit
  type: soft
builds-toward:
- endogeneity
- instrumental-variables
- causal-inference-econometrics
tags:
- OVB
- bias
- confounding
- identification
stage: formal-systems
status: validated
---
# Omitted Variable Bias

## Core Idea
Omitted variable bias (OVB) occurs when a variable that affects y and is correlated with an included regressor is excluded from the model, causing the OLS estimator to be biased and inconsistent. The direction of bias is determined by the sign of the correlation between the omitted variable and the included regressor, multiplied by the sign of the omitted variable's effect on y. The canonical example is estimating the return to education: omitting ability biases the education coefficient upward because ability raises wages and is positively correlated with schooling. OVB is the fundamental obstacle to causal inference with observational data.

## How It's Best Learned
Derive the OVB formula algebraically, then apply the 'sign heuristic' to real examples — labor economics wage regressions are ideal for this exercise.

## Common Misconceptions
- OVB cannot be fixed by adding more data; it requires either measuring the omitted variable or using an instrumental variable strategy.
- If the omitted variable is uncorrelated with the regressor of interest, omitting it biases the standard errors but not the coefficient.

## Explainer

You already know from multiple regression that OLS estimates the effect of each regressor holding the others constant. That "holding constant" is the key: OLS purges the coefficient on X of the confounding influence of any other variable you have included in the model. **Omitted variable bias (OVB)** is what happens when a variable belongs in the model — it affects the outcome Y and correlates with your regressor of interest X — but you leave it out.

The classic setup: you want to estimate the return to education on wages. You regress log wages on years of schooling and get a large positive coefficient. But workers differ in **ability**: more able people earn higher wages regardless of education, and more able people also tend to get more schooling. If you omit ability, your schooling coefficient absorbs some of the ability effect — it is biased upward. The formula for the bias is exact: the bias on βₓ equals the coefficient ability would get in your regression (how much wages rise with ability) multiplied by the coefficient from a regression of ability on schooling (how correlated they are). Positive × positive = upward bias. This is the **OVB formula**: bias = (effect of omitted on Y) × (correlation of omitted with X).

The sign heuristic gives you the direction without computing anything. Ask two questions: (1) If the omitted variable were included, would its coefficient be positive or negative? (2) Is the omitted variable positively or negatively correlated with the included regressor? Multiply the signs. If the result is positive, the included coefficient is biased upward — it is too large. If negative, biased downward. Consider omitting crime rates from a regression of housing prices on school quality: crime reduces prices (negative effect on Y) and is negatively correlated with school quality (better schools, less crime). Negative × negative = positive bias: the school quality coefficient is inflated because it is also picking up the benign effects of low crime.

The critical implication is that OVB cannot be solved with more data of the same kind. A million observations of wages and schooling, all omitting ability, will give you a million-observation estimate of the same biased number. OVB is a structural problem — the estimate is converging to the wrong value. The fixes all involve changing the information set: measure and include the omitted variable directly, use an **instrumental variable** that isolates variation in X uncorrelated with the omitted variable, or exploit a research design (natural experiment, panel data with fixed effects) that makes omission irrelevant. This is why OVB is described as the fundamental obstacle to causal inference with observational data — it is the gap between correlation and causation, made precise.
