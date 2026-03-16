---
id: linear-regression-probability-and-statistics
title: Simple Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: correlation-coefficient
  type: hard
- id: slope-concept
  type: soft
- id: writing-linear-equations
  type: soft
builds-toward:
- residuals-and-goodness-of-fit
tags:
- linear-regression
- least-squares
- slope
- intercept
- prediction
stage: formal-systems
status: validated
---
# Simple Linear Regression

## Core Idea
Simple linear regression fits a line ŷ = b₀ + b₁x to data by minimizing the sum of squared residuals (least squares). The slope b₁ = r · (sᵧ/sₓ) and intercept b₀ = ȳ − b₁x̄ are uniquely determined by the data. The regression line always passes through (x̄, ȳ). The slope represents the predicted change in y per one-unit increase in x, and predictions should only be made within the observed range of x (avoiding extrapolation).

## How It's Best Learned
Use real datasets: predict college GPA from SAT scores, or fuel efficiency from car weight. Have students interpret slope in context ('for each additional 100 lbs, fuel efficiency decreases by 0.5 mpg'). Explicitly warn against extrapolation with vivid examples of absurd predictions outside the data range.

## Common Misconceptions
- Switching predictor and response variables changes the regression line — y on x ≠ x on y.
- Interpreting the y-intercept as meaningful when x = 0 is outside the data range.
- Using regression for prediction when the relationship is clearly nonlinear.

## Explainer

From the correlation coefficient r, you know how to measure the strength and direction of a linear association between two variables. But r just gives a single number between −1 and 1 — it doesn't tell you *how much* y changes for a one-unit change in x, and it doesn't give you a formula for prediction. **Simple linear regression** takes the next step: it finds the specific line ŷ = b₀ + b₁x that best fits the data, where "best" is precisely defined as minimizing the total squared vertical distance between each observed point and the line.

The criterion is **least squares**: minimize Σ(yᵢ − ŷᵢ)², where yᵢ is the observed value and ŷᵢ = b₀ + b₁xᵢ is the predicted value. Each difference yᵢ − ŷᵢ is called a **residual** — the amount by which the line misses the actual point. Squaring residuals before summing means large misses are penalized heavily; it also makes the optimization tractable. Taking derivatives and setting them to zero gives closed-form formulas: b₁ = r · (sᵧ/sₓ) and b₀ = ȳ − b₁x̄. Notice how b₁ inherits its sign and direction from r, then scales it by the ratio of standard deviations to convert from correlation units to actual slope units. The fact that the line passes through (x̄, ȳ) — the "balance point" of the data — is a direct consequence of the least-squares conditions.

Interpreting the slope b₁ requires care. It says: on average, when x increases by 1 unit, the predicted y changes by b₁ units. This is a **predictive** or **associative** statement, not a causal one. If b₁ = 2.3 in a regression of exam scores on hours studied, it means students who study 1 hour more than average tend to score 2.3 points higher — it does not mean studying an extra hour *causes* exactly 2.3 more points. Lurking variables (ability, prior knowledge, motivation) could explain the association. The y-intercept b₀ is the predicted y when x = 0, which is only meaningful if x = 0 is plausible given the data range.

The correlation coefficient r has a second role in regression: r² (the **coefficient of determination**) tells you what proportion of the total variability in y is explained by the linear relationship with x. If r = 0.8, then r² = 0.64, meaning 64% of the variation in y is accounted for by knowing x. The remaining 36% is unexplained — attributable to other variables, measurement error, or nonlinearity. **Extrapolation** — using the regression line to predict y for x values outside the observed data range — is unreliable because the linear relationship may not hold beyond the observed region; the line has no obligation to track the data where we haven't looked.
