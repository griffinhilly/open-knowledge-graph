---
id: econometrics-intro
title: Introduction to Econometrics
domain: economics
course: econometrics
prerequisites:
- id: sample-vs-population
  type: hard
- id: scatterplots-and-correlation
  type: hard
- id: supply-and-demand-basics
  type: soft
builds-toward:
- bivariate-regression
- causal-inference-econometrics
tags:
- foundations
- empirical-methods
- data
stage: formal-systems
status: validated
---

# Introduction to Econometrics

## Core Idea
Econometrics applies statistical methods to economic data in order to test hypotheses, estimate relationships, and forecast outcomes. Unlike pure statistics, econometrics is preoccupied with identification: isolating causal effects from observational data where experiments are often impossible. The core challenge is that economic variables are jointly determined — prices and quantities move together, making causation difficult to establish. The discipline develops tools to handle endogeneity, selection, and omitted variables.

## How It's Best Learned
Start by reading empirical economics papers before mastering all the math — seeing what questions the tools answer motivates the technical investment. Practice distinguishing descriptive from causal claims in everyday economic reporting.

## Common Misconceptions
- Correlation in regression output does not imply causation; econometrics exists precisely because causation is hard to establish.
- Econometrics is not just applied statistics — the economic model guiding variable selection is as important as the estimation technique.

## Questions

```yaml
- question: "A researcher observes that cities with more police officers have higher crime rates, and concludes that policing causes crime. What is the most likely econometric problem?"
  type: multiple-choice
  options:
    - "Omitted variable bias — a third variable causes both police presence and crime independently"
    - "Reverse causation — high crime rates cause governments to deploy more police"
    - "Measurement error — crime statistics are underreported in cities with more police"
    - "Simultaneity bias — both police and crime are driven by city population size"
  answer: 1
  explanation: "This is reverse causation: police are deployed in response to crime, so crime drives police presence, not the other way around. A simple regression of crime on police conflates causal direction. Omitted variable bias would require a third variable causing both independently (option A is plausible but secondary here). The key diagnostic question is always: does X cause Y, Y cause X, or both — and the deployment pattern strongly suggests Y → X."

- question: "A student regresses quantity demanded on price using market data collected over time. The positive correlation she observes means the demand curve slopes upward."
  type: multiple-choice
  options:
    - "True — if quantity increases with price in the data, the demand curve must be upward-sloping"
    - "False — the positive correlation reflects simultaneous demand shifts, not movement along the demand curve; it estimates neither slope"
    - "False — the student should use a logarithmic regression, which would reveal the true negative slope"
    - "True — market data averages across supply and demand movements, giving an unbiased estimate of the demand slope"
  answer: 1
  explanation: "Market data reflects equilibrium price-quantity pairs shaped by both supply and demand shifts simultaneously. Summer ice cream data shows high prices and high quantities — both driven by demand, not a supply curve. Running a regression on these points estimates neither the demand slope nor the supply slope; it estimates the path of equilibrium points across shifting curves. This is the simultaneity problem: the variables are jointly determined, and simple regression cannot disentangle the causal structure."

- question: "Omitted variable bias occurs whenever a variable that affects the outcome Y is left out of the regression model."
  type: true-false
  answer: false
  explanation: "Omitted variable bias requires the omitted variable to be correlated with BOTH the included regressor X and the outcome Y. If it correlates with Y but not X, it increases the error variance but doesn't bias the coefficient on X. Only when both conditions hold does the omitted variable's effect 'bleed into' the X coefficient. This distinction is critical: not every missing control creates bias — only those correlated with the regressors you're already including."

- question: "Econometrics is best understood as statistics applied to economic data, with the same goals and methods as other applied statistics."
  type: true-false
  answer: false
  explanation: "Econometrics differs from general applied statistics in its preoccupation with causal identification from observational data. Economic variables are jointly determined — prices and quantities respond to the same underlying forces — so correlation analysis cannot establish causal effects. Econometrics develops specific tools (instrumental variables, natural experiments, regression discontinuity) to find variation that is as-good-as-random, enabling causal inference where experiments are typically impossible. The economic model driving variable selection is as important as the estimation technique."

- question: "What does it mean for an econometric strategy to 'identify' a causal effect, and why is identification the central challenge of the discipline?"
  type: short-answer
  answer: "Identification means finding a source of variation in the regressor X that is plausibly unrelated to the error term — variation that behaves as-if-randomly assigned, even though it wasn't. This matters because economic variables are jointly determined: prices, wages, and quantities all respond to the same underlying forces, making endogeneity the default rather than the exception. Without a valid identification strategy, regression coefficients measure correlations, not causal effects. Identification strategies include natural experiments, instrumental variables, and regression discontinuity designs."
  explanation: "The core challenge is that in observational data, people and firms make choices that reflect their unobservable characteristics — ability, ambition, risk tolerance. These unobservables correlate with both the treatment (education, job training) and the outcome (wages), biasing naive estimates. Identification is the art of finding variation that is genuinely exogenous: variation in X that happened 'by accident,' unrelated to anything else affecting Y."
```

## Explainer

From your work with scatterplots and correlation, you can compute how strongly two variables move together. Econometrics asks the harder question: does one cause the other? The frustrating answer is that a correlation coefficient tells you nothing about this. Two variables can correlate strongly for three entirely different reasons: X causes Y, Y causes X, or some third variable Z causes both. Econometrics is the discipline that developed tools to tell these apart when you cannot run a controlled experiment — which, in economics, is almost always.

The reason causation is so hard to establish in economics is that economic variables are **jointly determined**. Prices and quantities are determined simultaneously by supply and demand — they both respond to the same underlying market conditions. If you observe a scatterplot of ice cream prices and quantities sold, you see a positive correlation (both high in summer, both low in winter) that reflects demand shifts, not a supply curve. Running a simple regression of quantity on price would give you a garbage estimate of the demand elasticity. The problem is **simultaneity**: both variables are "on the right-hand side" of the real data-generating process, even if they appear on different sides of your regression equation.

**Endogeneity** is the general term for the problem that arises when a right-hand-side variable in your regression is correlated with the error term. It has three main sources. **Omitted variable bias** occurs when a variable affects Y and is correlated with X but is not in your model — its effect bleeds into the coefficient on X. For example, if you regress wages on education without controlling for family background, the education coefficient absorbs some of the family-background effect, overstating education's causal impact. **Reverse causation** occurs when Y causes X: more police might appear in high-crime areas because crime drives police deployment, making a positive correlation between police presence and crime completely uninformative about whether police reduce crime. **Measurement error** in X also creates attenuation bias.

The goal of econometric identification is to find variation in X that is (approximately) as good as random — variation that is plausibly unrelated to the error term. This might come from a **natural experiment**, where some feature of history or policy creates quasi-random assignment. It might come from an **instrumental variable** that shifts X but affects Y only through X. It might come from a **regression discontinuity** where a policy cutoff creates a sharp threshold. Each of these strategies is essentially arguing: "here is a source of variation that behaves like random assignment even though we didn't control it." The statistical technique follows from the identification strategy, not the other way around.

Your supply-and-demand intuition is exactly the right frame. Every empirical question in economics is ultimately a question about which mechanism is operating — supply shifting, demand shifting, or both simultaneously. Writing down the correct economic model first tells you what variation you need to observe, what variables belong in the regression, and what confounders to worry about. A regression that violates the underlying economic model will produce coefficients that cannot be given a causal interpretation no matter how sophisticated the estimation technique. The economic model and the statistical tool must fit each other.
