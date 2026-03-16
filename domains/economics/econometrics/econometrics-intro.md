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

## Explainer

From your work with scatterplots and correlation, you can compute how strongly two variables move together. Econometrics asks the harder question: does one cause the other? The frustrating answer is that a correlation coefficient tells you nothing about this. Two variables can correlate strongly for three entirely different reasons: X causes Y, Y causes X, or some third variable Z causes both. Econometrics is the discipline that developed tools to tell these apart when you cannot run a controlled experiment — which, in economics, is almost always.

The reason causation is so hard to establish in economics is that economic variables are **jointly determined**. Prices and quantities are determined simultaneously by supply and demand — they both respond to the same underlying market conditions. If you observe a scatterplot of ice cream prices and quantities sold, you see a positive correlation (both high in summer, both low in winter) that reflects demand shifts, not a supply curve. Running a simple regression of quantity on price would give you a garbage estimate of the demand elasticity. The problem is **simultaneity**: both variables are "on the right-hand side" of the real data-generating process, even if they appear on different sides of your regression equation.

**Endogeneity** is the general term for the problem that arises when a right-hand-side variable in your regression is correlated with the error term. It has three main sources. **Omitted variable bias** occurs when a variable affects Y and is correlated with X but is not in your model — its effect bleeds into the coefficient on X. For example, if you regress wages on education without controlling for family background, the education coefficient absorbs some of the family-background effect, overstating education's causal impact. **Reverse causation** occurs when Y causes X: more police might appear in high-crime areas because crime drives police deployment, making a positive correlation between police presence and crime completely uninformative about whether police reduce crime. **Measurement error** in X also creates attenuation bias.

The goal of econometric identification is to find variation in X that is (approximately) as good as random — variation that is plausibly unrelated to the error term. This might come from a **natural experiment**, where some feature of history or policy creates quasi-random assignment. It might come from an **instrumental variable** that shifts X but affects Y only through X. It might come from a **regression discontinuity** where a policy cutoff creates a sharp threshold. Each of these strategies is essentially arguing: "here is a source of variation that behaves like random assignment even though we didn't control it." The statistical technique follows from the identification strategy, not the other way around.

Your supply-and-demand intuition is exactly the right frame. Every empirical question in economics is ultimately a question about which mechanism is operating — supply shifting, demand shifting, or both simultaneously. Writing down the correct economic model first tells you what variation you need to observe, what variables belong in the regression, and what confounders to worry about. A regression that violates the underlying economic model will produce coefficients that cannot be given a causal interpretation no matter how sophisticated the estimation technique. The economic model and the statistical tool must fit each other.
