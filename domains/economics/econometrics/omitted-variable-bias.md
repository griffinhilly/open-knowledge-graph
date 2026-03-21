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

## Questions

```yaml
- question: "A researcher regresses student test scores on class size, finding smaller classes improve scores significantly. A colleague argues this is biased because wealthier school districts tend to have both smaller classes and higher-scoring students. The colleague is describing:"
  type: multiple-choice
  options:
    - "Sampling error — the sample is not large enough to detect the true class-size effect"
    - "Reverse causality — higher test scores cause districts to reduce class sizes"
    - "Omitted variable bias — family wealth affects test scores and correlates with class size, biasing the coefficient"
    - "Multicollinearity — class size and wealth are too correlated to separate their effects"
  answer: 2
  explanation: "Family wealth (or socioeconomic status) affects test scores (positive effect on Y) and is positively correlated with smaller class sizes (wealthier districts have more resources per student). This fits the OVB formula exactly: a variable affecting Y that correlates with the regressor of interest, left out of the model. The class-size coefficient absorbs part of the wealth effect, biasing it. Multicollinearity is a different problem affecting standard errors, not coefficient direction."

- question: "A study omits ability from a wage regression on years of schooling. Ability has a positive effect on wages and is positively correlated with schooling. According to the OVB formula, the schooling coefficient is biased in which direction?"
  type: multiple-choice
  options:
    - "Downward — ability's positive influence inflates the education coefficient negatively"
    - "Upward — the coefficient is too large because it also captures ability's positive effect on wages"
    - "Upward — because ability negatively affects wages and negatively correlates with schooling"
    - "Not biased — correlation between ability and schooling doesn't affect the schooling coefficient"
  answer: 1
  explanation: "OVB formula: bias = (effect of omitted on Y) × (correlation of omitted with X). Ability has a positive effect on wages (+) and is positively correlated with schooling (+). Positive × positive = upward bias. The schooling coefficient is too large — it absorbs part of ability's positive wage effect. This is the canonical example from the explainer. Option D is a common misconception: correlation with X is precisely what causes bias, not just an effect on Y."

- question: "Omitted variable bias cannot be eliminated by collecting a larger sample of the same kind of data — it requires either measuring the omitted variable or using an alternative identification strategy."
  type: true-false
  answer: true
  explanation: "OVB is a structural problem, not a sampling problem. The OLS estimator in a misspecified model converges to the wrong quantity as sample size grows — it is homing in on a biased value, not fluctuating around the right one. The explainer states: 'A million observations... all omitting ability, will give you a million-observation estimate of the same biased number.' More data sharpens the wrong estimate. Fixes require changing the information set: include the omitted variable, use an instrumental variable, or exploit a suitable research design."

- question: "If an omitted variable affects the outcome Y but is uncorrelated with the included regressor X, omitting it biases the OLS coefficient on X."
  type: true-false
  answer: false
  explanation: "OVB requires both conditions: the omitted variable must affect Y AND be correlated with X. The Common Misconceptions section states: 'If the omitted variable is uncorrelated with the regressor of interest, omitting it biases the standard errors but not the coefficient.' With zero correlation to X, the omitted variable's effect on Y goes entirely into the error term, increasing its variance (and biasing standard errors), but the coefficient on X remains unbiased."

- question: "A friend argues that a very large, carefully designed survey can fix any regression problem, including omitted variable bias. How would you explain why this claim is wrong?"
  type: short-answer
  answer: "OVB is an identification problem, not a sampling problem. The estimator is converging to the wrong value as sample size grows — more observations just sharpen the wrong estimate. No amount of data can correct for a variable that belongs in the model but isn't there. Fixing OVB requires changing what information enters the model: measuring and including the omitted variable, using an instrumental variable that isolates variation in X uncorrelated with the omission, or exploiting a research design that makes the omission irrelevant."
  explanation: "This is why OVB is described as the fundamental obstacle to causal inference with observational data. Sampling problems (imprecision, noise) improve with more data. Identification problems (converging to the wrong value) do not — they require a different strategy entirely. Data quantity is orthogonal to data quality in this sense."
```

## Explainer

You already know from multiple regression that OLS estimates the effect of each regressor holding the others constant. That "holding constant" is the key: OLS purges the coefficient on X of the confounding influence of any other variable you have included in the model. **Omitted variable bias (OVB)** is what happens when a variable belongs in the model — it affects the outcome Y and correlates with your regressor of interest X — but you leave it out.

The classic setup: you want to estimate the return to education on wages. You regress log wages on years of schooling and get a large positive coefficient. But workers differ in **ability**: more able people earn higher wages regardless of education, and more able people also tend to get more schooling. If you omit ability, your schooling coefficient absorbs some of the ability effect — it is biased upward. The formula for the bias is exact: the bias on βₓ equals the coefficient ability would get in your regression (how much wages rise with ability) multiplied by the coefficient from a regression of ability on schooling (how correlated they are). Positive × positive = upward bias. This is the **OVB formula**: bias = (effect of omitted on Y) × (correlation of omitted with X).

The sign heuristic gives you the direction without computing anything. Ask two questions: (1) If the omitted variable were included, would its coefficient be positive or negative? (2) Is the omitted variable positively or negatively correlated with the included regressor? Multiply the signs. If the result is positive, the included coefficient is biased upward — it is too large. If negative, biased downward. Consider omitting crime rates from a regression of housing prices on school quality: crime reduces prices (negative effect on Y) and is negatively correlated with school quality (better schools, less crime). Negative × negative = positive bias: the school quality coefficient is inflated because it is also picking up the benign effects of low crime.

The critical implication is that OVB cannot be solved with more data of the same kind. A million observations of wages and schooling, all omitting ability, will give you a million-observation estimate of the same biased number. OVB is a structural problem — the estimate is converging to the wrong value. The fixes all involve changing the information set: measure and include the omitted variable directly, use an **instrumental variable** that isolates variation in X uncorrelated with the omitted variable, or exploit a research design (natural experiment, panel data with fixed effects) that makes omission irrelevant. This is why OVB is described as the fundamental obstacle to causal inference with observational data — it is the gap between correlation and causation, made precise.
