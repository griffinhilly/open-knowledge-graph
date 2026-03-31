---
id: returns-to-education
title: Returns to Education (Mincer Equation)
domain: economics
course: labor-economics
prerequisites:
- id: human-capital-theory
  type: hard
- id: ols-assumptions
  type: soft
tags:
- Mincer
- returns-to-schooling
- wage-equation
- ability-bias
- IV-estimation
stage: advanced
status: validated
---

# Returns to Education (Mincer Equation)

## Core Idea
The Mincer earnings equation — log(wage) = alpha + beta*S + gamma1*X + gamma2*X^2 + epsilon — is the foundational empirical specification in labor economics, where S is years of schooling, X is potential experience, and beta estimates the percentage return to an additional year of education. The equation fits observed earnings data remarkably well across countries, but the OLS estimate of beta (typically 8-13%) is biased by ability bias (high-ability individuals get more education AND earn more, inflating the apparent return) and selection bias. Instrumental variable approaches — using compulsory schooling laws, quarter of birth, or distance to college as instruments — generally find returns similar to or slightly above OLS estimates, suggesting that ability bias may be roughly offset by measurement error or that the local average treatment effect for compliers exceeds the average return.

## Questions

```yaml
- question: "The Mincer equation includes experience as a quadratic (X and X²) because..."
  type: multiple-choice
  options:
    - "All economic relationships are quadratic"
    - "Earnings rise with experience (positive first term) but at a decreasing rate (negative second term), consistent with declining human capital investment over the career"
    - "Including X² eliminates omitted variable bias"
    - "The logarithm of wages requires polynomial terms"
  answer: 1
  explanation: "Human capital theory predicts that earnings rise with experience because workers accumulate skills on the job, but that the rate of increase declines as workers age (the investment horizon shortens, reducing the return to further investment, and skills may depreciate). The quadratic captures this concave relationship: the positive coefficient on X gives the initial rate of earnings growth, and the negative coefficient on X² captures the flattening. Empirically, this specification fits experience-earnings profiles very well."

- question: "The OLS estimate of the return to education from the Mincer equation provides an unbiased estimate of the causal effect of education on earnings."
  type: true-false
  answer: false
  explanation: "OLS is biased primarily due to ability bias — unmeasured ability is correlated with both schooling (more able people get more education) and earnings (more able people earn more regardless of education), leading to an upward bias in the OLS return estimate. Other sources of bias include measurement error in schooling (which attenuates the estimate) and selection into schooling based on expected returns. IV methods attempt to address these biases by finding instruments that affect schooling but not earnings directly. Interestingly, IV estimates often exceed OLS estimates, possibly because measurement error bias (downward) exceeds ability bias (upward), or because the local effect for compliers exceeds the average effect."

- question: "Why are instrumental variable estimates of the return to education often interpreted as 'local average treatment effects' (LATE) rather than average treatment effects?"
  type: short-answer
  answer: "IV estimates identify the causal effect for 'compliers' — individuals whose education was actually changed by the instrument (e.g., those who attended more school because of compulsory schooling laws but would not have otherwise). This is the LATE, and it may differ from the average treatment effect (ATE) for the full population if compliers have different returns than always-takers or never-takers. Compulsory schooling compliers may have higher marginal returns (they were at the margin of dropping out) than the average person."
  explanation: "This is a critical econometric point. Angrist and Krueger's quarter-of-birth instrument identifies the return for students who stayed in school longer only because compulsory schooling laws compelled them — a specific subpopulation that may not represent the typical student. If these marginal students (who would have dropped out without the law) benefit more or less from education than the average student, the LATE differs from the ATE. This does not invalidate the IV estimate — it correctly identifies a causal effect — but it limits generalizability."
```

## Explainer

The Mincer equation is one of the most successful empirical specifications in all of economics. Jacob Mincer's 1974 formulation — modeling the log of earnings as a linear function of years of schooling and a quadratic in potential experience — fits the data so well across countries, time periods, and demographic groups that it has become the default starting point for any empirical analysis of wages. Its success comes from grounding the specification in human capital theory: the log-linear relationship between earnings and schooling arises from a model where each year of schooling raises productivity by a constant percentage, and the concave experience profile reflects declining human capital investment over the career.

The coefficient on schooling (beta) is typically interpreted as the percentage increase in earnings from one additional year of education. OLS estimates across developed countries generally fall between 8% and 13% — a remarkably high return compared to most physical investments. But interpretation of this coefficient is fraught with endogeneity concerns. The most important is ability bias: individuals with higher innate ability (cognitive ability, motivation, family advantages) tend to both acquire more education and earn more regardless of education. If ability is correlated with schooling and earnings but omitted from the regression, the schooling coefficient absorbs some of the ability effect and is biased upward.

The instrumental variables revolution in labor economics was motivated precisely by this problem. Angrist and Krueger (1991) used quarter of birth as an instrument: compulsory schooling laws mean that students born earlier in the year reach the legal dropout age at a younger grade, leading to slightly less schooling. Since quarter of birth is plausibly random (unrelated to ability), it provides exogenous variation in schooling. Their IV estimate of the return to education was about 7-8%, close to OLS. Other instruments — changes in compulsory schooling laws, distance to college, tuition policy changes — have also been exploited, with IV estimates often slightly exceeding OLS estimates.

The finding that IV estimates are similar to or above OLS estimates was initially surprising, since ability bias was expected to inflate OLS. Two explanations have been proposed. First, measurement error in self-reported years of schooling creates attenuation bias that pulls the OLS estimate downward, potentially offsetting the upward ability bias. Second, the LATE interpretation — IV identifies the effect for compliers, who in the case of compulsory schooling instruments are marginal students who would have dropped out without the law. If these students have particularly high returns to the marginal year (perhaps because dropping out carries a large stigma or because the last years of required schooling are particularly valuable), the LATE exceeds the average return.

The Mincer equation's simplicity is both its strength and its limitation. It assumes a constant percentage return per year of schooling (each year has the same proportional effect), which may not hold — the return to the 12th year (completing high school) may differ from the return to the 16th year (completing college) due to sheepskin effects (credential bonuses at degree completion). Extensions include allowing for nonlinear returns, controlling for observable ability measures, adding covariates for demographic and family background, and allowing returns to vary across the distribution of earnings. Despite these refinements, the basic Mincer specification remains the discipline's workhorse.
