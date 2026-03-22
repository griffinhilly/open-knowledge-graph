---
id: scatterplots-and-correlation
title: Scatterplots and Correlation
domain: mathematics
course: probability-and-statistics
prerequisites: []
builds-toward:
- correlation-coefficient
- linear-regression-basics
tags:
- scatterplot
- bivariate-data
- association
stage: formal-systems
status: draft
---

# Scatterplots and Correlation

## Core Idea
A scatterplot displays paired observations (x, y) as points on a coordinate plane. Scatterplots reveal the nature of association between two variables: linear or nonlinear, positive or negative, strong or weak, with or without outliers. Visual patterns in scatterplots motivate quantitative measures of association (like correlation) and suggest appropriate modeling approaches. Scatterplots are the first step in bivariate analysis.

## How It's Best Learned
Plot various datasets (positive, negative, no correlation; linear and nonlinear) and describe visual patterns. Add regression lines to understand prediction.

## Common Misconceptions
Thinking correlation is present just because points follow any pattern (nonlinear associations aren't linear). Assuming scatterplots reveal causation.

## Explainer

A **scatterplot** is the most fundamental tool for exploring the relationship between two quantitative variables. Each observation contributes one point: its x-coordinate is the value of one variable, its y-coordinate the value of the other. The resulting cloud of points reveals patterns that no single number can capture — the direction of the association (positive or negative), its form (linear or curved), its strength (tight clustering or loose spread), and the presence of outliers or clusters. Looking at the scatterplot before computing any summary statistic is not optional; it is the essential first step in bivariate analysis.

Three features describe the pattern in a scatterplot. **Direction**: a positive association means that as x increases, y tends to increase (points slope upward from left to right); a negative association means y tends to decrease as x increases (points slope downward). **Form**: the pattern may be approximately linear (following a straight line), curved (quadratic, exponential, logarithmic), or have no discernible form. **Strength**: strong associations show points clustered tightly around the underlying pattern; weak associations show a loose, dispersed cloud. A strong positive linear association looks like a narrow band of points ascending from left to right; a weak association looks like a diffuse oval.

The **correlation coefficient** r quantifies only the linear component of the association. It ranges from −1 (perfect negative linear) to +1 (perfect positive linear), with 0 indicating no linear relationship. But r = 0 does not mean "no relationship" — it means "no linear relationship." A perfect U-shaped curve has r ≈ 0 because the upward and downward linear tendencies cancel. This is precisely why the scatterplot matters: it reveals nonlinear structure that r completely misses. Anscombe's Quartet — four datasets with nearly identical means, variances, and correlation coefficients but wildly different scatterplots — is the canonical demonstration that summary statistics alone can be deeply misleading.

A strong association in a scatterplot does **not** establish causation. Ice cream sales and drowning rates are strongly positively correlated, but ice cream does not cause drowning — both are driven by summer temperatures, a confounding variable. Establishing causation requires experimental design (randomized controlled trials), not just observed correlation. The mantra "correlation does not imply causation" is not merely a slogan — it reflects a fundamental logical gap between observing that two variables move together and concluding that one drives the other. Scatterplots reveal association; determining its cause requires additional evidence and careful study design.

## Questions

```yaml
- question: "A researcher plots hours of TV watched per day (x) against exam scores (y) for 100 students. The scatterplot shows a clear U-shaped curve — low scorers watch very little TV, moderate viewers score highest, and heavy viewers score lowest. The correlation coefficient r ≈ 0. What is the correct conclusion?"
  type: multiple-choice
  options:
    - "There is no association between TV watching and exam scores"
    - "The data is too noisy to detect any pattern"
    - "There is a strong nonlinear association, but r ≈ 0 because correlation measures only linear association"
    - "The scatterplot must be incorrect if r ≈ 0 but a pattern appears"
  answer: 2
  explanation: "The correlation coefficient r measures the strength of LINEAR association only. A U-shaped curve is a strong association — it's just nonlinear. Because the positive and negative linear components cancel out, r ≈ 0 even though the scatterplot reveals a clear pattern. This is why looking at the scatterplot first is essential: r alone can completely miss a strong nonlinear relationship. The scatterplot is not wrong — it is correctly showing what r cannot capture."

- question: "Which of the following can a scatterplot reliably tell you about two variables?"
  type: multiple-choice
  options:
    - "Whether one variable causes changes in the other"
    - "The direction, form, and strength of the association between the variables"
    - "The true population relationship, as opposed to the sample relationship"
    - "Whether the observed association would hold in a different context or population"
  answer: 1
  explanation: "Scatterplots reveal the nature of the observed association: whether it's positive or negative (direction), whether it's linear or curved (form), and whether points cluster tightly or loosely around the pattern (strength). They also reveal outliers. What scatterplots cannot establish is causation — an association between two variables might be driven by a third variable, or be coincidental. Causation requires experimental or quasi-experimental methods, not just observing covariation."

- question: "A strong positive association visible in a scatterplot means that increases in x cause increases in y."
  type: true-false
  answer: false
  explanation: "Correlation is not causation. A strong association in a scatterplot indicates the two variables move together, but not why. There may be a hidden confounding variable that drives both; causation might run in the opposite direction; or the association might be spurious. For example, ice cream sales and drowning rates are strongly positively correlated (both peak in summer), but ice cream doesn't cause drowning — temperature confounds both. Causation requires additional evidence beyond observed correlation."

- question: "A scatterplot can reveal a strong relationship between two variables even when the linear correlation coefficient r is close to zero."
  type: true-false
  answer: true
  explanation: "Yes — r only measures linear association. If the true relationship is curved (quadratic, sinusoidal, etc.), r can be near zero while the scatterplot clearly shows a systematic, strong pattern. This is precisely why examining a scatterplot is the first step in bivariate analysis: it shows the full picture, while r summarizes only the linear component. Relying solely on r without looking at the plot can lead to badly mistaken conclusions about the data."

- question: "Explain why examining a scatterplot before computing a correlation coefficient is important, not just a formality."
  type: short-answer
  answer: "The correlation coefficient r summarizes only the strength and direction of linear association. A scatterplot reveals whether the relationship is actually linear, whether there are outliers that might distort r, and whether a nonlinear pattern exists that r would miss entirely. Without the scatterplot, you might compute r ≈ 0 and conclude 'no association' when there's a strong curved relationship, or r ≈ 0.8 driven entirely by a single outlier in an otherwise flat cloud. The scatterplot is the raw visual evidence; r is a summary statistic that makes sense only after confirming the relationship is approximately linear."
  explanation: "The principle is: visualize before you summarize. Summary statistics compress information and can mislead — Anscombe's Quartet shows four datasets with nearly identical means, variances, and correlation coefficients that look completely different when plotted. Scatterplots protect against this by showing the actual shape, outliers, and form of the relationship that r cannot distinguish."
```
