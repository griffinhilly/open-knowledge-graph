---
id: count-data-regression-models
title: 'Count Data Regression: Poisson and Negative Binomial Models'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: logistic-regression-binary-categorical
  type: hard
- id: poisson-distribution
  type: hard
- id: probability-distributions
  type: hard
- id: probability-mass-functions
  type: soft
tags:
- count-data
- poisson
- negative-binomial
- overdispersion
stage: expert
status: validated
---

# Count Data Regression: Poisson and Negative Binomial Models

## Core Idea
Count outcomes like protest events or arrests are often overdispersed—more variable than Poisson assumes. Negative binomial regression accommodates overdispersion. Zero-inflated models address excess zeros. Proper model selection improves inference and prevents bias.

## Questions

```yaml
- question: "A researcher models the number of political protests per country per year using Poisson regression. Diagnostics reveal the variance is 18 times the mean. What is the most likely consequence of ignoring this?"
  type: multiple-choice
  options:
    - "Predicted counts will occasionally be negative"
    - "The model will automatically compensate by widening confidence intervals"
    - "Standard errors will be underestimated, making predictors appear statistically significant when they may not be"
    - "The log-link function will produce biased coefficient estimates"
  answer: 2
  explanation: "Overdispersion means the Poisson model is misspecified — it assumes variance equals the mean, but the actual variance is far larger. When this constraint is violated, Poisson underestimates standard errors. Underestimated SEs produce inflated z-statistics and artificially small p-values, leading researchers to declare spurious significance. Negative binomial regression adds a dispersion parameter that absorbs the extra-Poisson variation, producing correctly estimated standard errors and reliable inference."

- question: "What is the defining characteristic of overdispersion in count data?"
  type: multiple-choice
  options:
    - "The outcome variable contains a large number of zero values"
    - "The variance of the count variable substantially exceeds its mean"
    - "The count distribution is negatively skewed"
    - "The mean of the count variable exceeds its variance"
  answer: 1
  explanation: "Poisson regression's core constraint is mean = variance. Overdispersion is specifically defined as variance > mean — the data is more variable than the Poisson distribution can accommodate. This arises from clustering, contagion processes, or unobserved heterogeneity across units. Excess zeros (option A) are a related but distinct problem handled by zero-inflated models; they don't define overdispersion on their own. Underdispersion (mean > variance) exists but is rare in social science count data."

- question: "Negative binomial regression is generally preferred over Poisson regression when overdispersion tests indicate that the variance of the count outcome significantly exceeds the mean."
  type: true-false
  answer: true
  explanation: "This is the primary model selection criterion for count data. Negative binomial adds a dispersion parameter (sometimes called α) to the Poisson model — conceptually, each observation gets its own underlying rate drawn from a gamma distribution, and the mixture produces the negative binomial. When overdispersion is present, this extra parameter absorbs the excess variation and produces correctly calibrated standard errors. In practice, social science count data is almost always overdispersed, making negative binomial the default preference unless a test confirms Poisson adequacy."

- question: "Zero-inflated count models are appropriate whenever the count outcome variable contains any zero values."
  type: true-false
  answer: false
  explanation: "Zero-inflated models are specifically for EXCESS zeros — more zeros than Poisson or negative binomial would predict given the estimated rate. Many genuine count processes produce zeros naturally (a country might have zero protests in a quiet year), and standard Poisson or negative binomial handles these fine. Zero-inflated models are appropriate when two distinct data-generating processes are at work: one that determines whether any events can occur at all (a structural zero mechanism) and one that determines how many occur when they do. Diagnostic tools like rootograms and the Vuong test help distinguish excess zeros from ordinary count variation."

- question: "Why does fitting a Poisson model to overdispersed count data produce unreliable hypothesis tests, and what does negative binomial regression do differently to address this problem?"
  type: short-answer
  answer: "Poisson constrains variance to equal the mean. When actual variance exceeds this, the model underestimates standard errors — inflating test statistics and producing false significance. Negative binomial adds a dispersion parameter that lets variance exceed the mean by an estimated amount, absorbing the extra variation and producing correctly sized standard errors."
  explanation: "The core issue is model misspecification: Poisson's mean-variance constraint is a strong assumption that count data routinely violates. When the assumption fails, the model's uncertainty estimates are wrong — not just imprecise, but systematically too small. This makes the problem invisible to the researcher: estimates look precise and significant, but the precision is an artifact of the wrong model. Negative binomial's dispersion parameter is estimated from the data and adjusts the variance-mean relationship accordingly. AIC/BIC comparison and likelihood ratio tests comparing Poisson vs. negative binomial are standard diagnostic steps before reporting results."
```

## Explainer

You already know that ordinary linear regression assumes a continuous, normally distributed outcome. But many social science outcomes are **counts** — the number of protests in a country in a year, arrests per month, bills introduced in a legislative session, or war casualties in a conflict. Counts are non-negative integers, and their distribution tends to be highly skewed: many observations near zero, a long tail of large values. Fitting OLS to count data can produce nonsensical predictions (negative counts, fractional events) and incorrect standard errors. The solution is a family of regression models built specifically for count data.

The starting point is **Poisson regression**. The Poisson distribution — which you've studied — has one defining property: its mean equals its variance. Poisson regression models the log of the expected count as a linear function of predictors, which guarantees non-negative predictions and has a natural interpretation: coefficients are log-incident rate ratios, and exponentiated coefficients are multiplicative effects on the expected count. If a coefficient is 0.5, e^0.5 ≈ 1.65, meaning a one-unit increase in that predictor multiplies the expected count by 1.65.

The critical limitation of Poisson is its mean-equals-variance constraint. Real count data is almost always **overdispersed** — the variance exceeds the mean, often dramatically. This happens when outcomes are clustered (protests cluster in time and space), when unobserved heterogeneity exists across units, or when events follow a contagion process. If you force Poisson on overdispersed data, the model is misspecified: standard errors are underestimated, test statistics are inflated, and you will declare spurious significance. **Negative binomial regression** relaxes the constraint by adding a dispersion parameter that captures extra-Poisson variation. Think of it as a Poisson model where each observation has its own underlying rate drawn from a gamma distribution — the resulting mixture is the negative binomial. In practice, negative binomial fits are nearly always preferred when overdispersion tests flag a problem.

A further complication is **excess zeros** — outcomes where the count is zero far more often than Poisson or negative binomial predicts. This arises when two distinct processes generate the data: one process determines whether any events occur at all (a logistic-type "always-zero" mechanism), and a second process governs how many occur when they do (a count mechanism). **Zero-inflated Poisson** and **zero-inflated negative binomial** models estimate both processes simultaneously. Model selection between these options typically uses the Vuong test, AIC/BIC comparison, and rootograms (graphical comparison of observed vs. predicted count frequencies) to diagnose where the plain Poisson fails.
