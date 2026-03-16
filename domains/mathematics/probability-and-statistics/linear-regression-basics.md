---
id: linear-regression-basics
title: Linear Regression Basics
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: correlation-coefficient
  type: hard
builds-toward:
- residuals-and-goodness-of-fit
tags:
- regression
- least-squares
- prediction
- slope-intercept
stage: formal-systems
status: draft
---

# Linear Regression Basics

## Core Idea
Linear regression fits a line y = a + bx to paired data (xᵢ, yᵢ) by minimizing the sum of squared residuals. The slope b measures the change in y per unit change in x; the intercept a is y when x = 0. The regression line passes through (x̄, ȳ) and its slope is b = r × (s_y/s_x). Linear regression enables prediction and quantifies linear relationships, though predictions outside the data range (extrapolation) are unreliable.

## How It's Best Learned
Fit regression lines to scatterplots. Interpret slope in context. Use regression to make predictions and discuss uncertainty. Compare fitted values to observed values (residuals).

## Common Misconceptions
Thinking regression assumes causation. Using regression for severely nonlinear data. Extrapolating far beyond the data range with confidence. Confusing the fitted value with the data point.

## Explainer

From the correlation coefficient, you know how to measure the *strength* and *direction* of a linear association between two variables. Linear regression goes one step further: it finds the specific line that best describes that association and uses it to make predictions. The method is called **least squares** because it chooses the line that minimizes the total squared vertical distance between each data point and the line.

The line has the form ŷ = a + bx, where ŷ (read "y-hat") is the *predicted* value of y for a given x. The slope b and intercept a are chosen to minimize Σ(yᵢ − ŷᵢ)², the sum of squared **residuals**. Why squared? Squaring makes all terms positive (so negative and positive errors don't cancel), and it penalizes large errors more than small ones. The algebra leads to a clean formula for the slope: b = r × (s_y / s_x), where r is the correlation coefficient you already know, s_y is the standard deviation of y, and s_x is the standard deviation of x. This formula shows how tightly regression connects to correlation: if r = 1, the slope is exactly s_y / s_x; if r = 0, the slope is 0 and the best prediction for y is just ȳ regardless of x.

The intercept follows from a key property of the regression line: it always passes through the point (x̄, ȳ), the means of both variables. Once you have the slope b, the intercept is a = ȳ − b × x̄. This means the regression line is anchored at the center of the data and tilted according to the correlation and spread. Interpreting the slope: b says "for every one-unit increase in x, the predicted y changes by b units." Interpreting the intercept: a is the predicted y when x = 0, which may or may not be meaningful depending on whether x = 0 is in the range of your data.

Two important limitations: regression describes association, not causation. Height and shoe size are correlated; fitting a regression doesn't mean height *causes* shoe size. Second, **extrapolation** — predicting y for an x value far outside your data range — is unreliable. The linear relationship observed in your data may not hold beyond it. A regression of height vs. weight in adults would give nonsense predictions for newborns. The regression line is a summary of the data you have, not a universal law, and the **residual** yᵢ − ŷᵢ for each point quantifies how far reality deviates from that summary.
