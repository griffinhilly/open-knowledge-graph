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
status: validated
---

# Linear Regression Basics

## Core Idea
Linear regression fits a line y = a + bx to paired data (xᵢ, yᵢ) by minimizing the sum of squared residuals. The slope b measures the change in y per unit change in x; the intercept a is y when x = 0. The regression line passes through (x̄, ȳ) and its slope is b = r × (s_y/s_x). Linear regression enables prediction and quantifies linear relationships, though predictions outside the data range (extrapolation) are unreliable.

## How It's Best Learned
Fit regression lines to scatterplots. Interpret slope in context. Use regression to make predictions and discuss uncertainty. Compare fitted values to observed values (residuals).

## Common Misconceptions
Thinking regression assumes causation. Using regression for severely nonlinear data. Extrapolating far beyond the data range with confidence. Confusing the fitted value with the data point.

## Questions

```yaml
- question: "A regression of study hours (x) on exam score (y) yields slope b = 5 and intercept a = 20. A student studies 15 hours. The fitted line predicts a score of 95. The student actually scores 88. What is the residual for this student?"
  type: multiple-choice
  options:
    - "95, because that is the predicted value"
    - "−7, because residual = observed − predicted = 88 − 95"
    - "7, because residual = predicted − observed = 95 − 88"
    - "0, because the regression line minimizes residuals to zero"
  answer: 1
  explanation: "A residual is defined as observed minus predicted: yᵢ − ŷᵢ = 88 − 95 = −7. A negative residual means the actual value fell below the regression line's prediction. Residuals are not zero for individual points — the regression minimizes the *sum of squared* residuals, but individual points scatter around the line. Option C has the subtraction reversed."

- question: "For a dataset with correlation r = 0.6, s_x = 5, and s_y = 20, what is the slope of the regression line of y on x?"
  type: multiple-choice
  options:
    - "0.15, because b = r × (s_x / s_y) = 0.6 × (5/20)"
    - "2.4, because b = r × (s_y / s_x) = 0.6 × (20/5)"
    - "0.6, because the slope equals the correlation coefficient"
    - "12, because b = s_y / s_x = 20/5 = 4, then scaled by r gives 0.6 × 20 = 12"
  answer: 1
  explanation: "The slope formula is b = r × (s_y / s_x). Substituting: b = 0.6 × (20/5) = 0.6 × 4 = 2.4. Option A inverts the ratio — that would be the slope of the regression of x on y. Option C confuses the slope with the correlation itself, which is only true when both variables have equal standard deviations."

- question: "A significant linear regression relationship between two variables proves that one variable causes the other."
  type: true-false
  answer: false
  explanation: "Regression (and correlation) quantify the strength and direction of linear association, not causation. A famous example: ice cream sales and drowning rates are positively correlated — both increase in summer — but ice cream does not cause drowning. A regression line fits the association but says nothing about whether x produces y. Establishing causation requires experimental design (randomization, control groups), not statistical fitting alone."

- question: "The least-squares regression line always passes through the point (x̄, ȳ), the means of x and y."
  type: true-false
  answer: true
  explanation: "This is a provable algebraic property of least-squares regression. The intercept is defined as a = ȳ − b × x̄, which ensures the line passes through (x̄, ȳ). Substituting x = x̄ gives ŷ = a + b × x̄ = (ȳ − b × x̄) + b × x̄ = ȳ. The regression line is therefore anchored at the centroid of the data and tilted by the slope. This also means the mean of the fitted values equals ȳ."

- question: "Explain why extrapolating a regression line far beyond the range of the data is unreliable, even when the line fits the data well."
  type: short-answer
  answer: "The regression line summarizes the linear relationship observed within the data range. There is no guarantee this relationship holds outside that range — the underlying process may become nonlinear, saturate, reverse direction, or be subject to different influences. A model fitted to adults' height-weight data would produce nonsensical (negative) weight predictions for very short heights, because the linear trend cannot extend indefinitely. The fit quality (R², residual size) only measures how well the line describes the data you have, not how well it describes regions you haven't observed."
  explanation: "The deeper point is that a regression line is an empirical description, not a physical law. Its validity is bounded by the scope of the data used to fit it. Extrapolation assumes the pattern continues, which is an untestable assumption that frequently fails in practice."
```

## Explainer

From the correlation coefficient, you know how to measure the *strength* and *direction* of a linear association between two variables. Linear regression goes one step further: it finds the specific line that best describes that association and uses it to make predictions. The method is called **least squares** because it chooses the line that minimizes the total squared vertical distance between each data point and the line.

The line has the form ŷ = a + bx, where ŷ (read "y-hat") is the *predicted* value of y for a given x. The slope b and intercept a are chosen to minimize Σ(yᵢ − ŷᵢ)², the sum of squared **residuals**. Why squared? Squaring makes all terms positive (so negative and positive errors don't cancel), and it penalizes large errors more than small ones. The algebra leads to a clean formula for the slope: b = r × (s_y / s_x), where r is the correlation coefficient you already know, s_y is the standard deviation of y, and s_x is the standard deviation of x. This formula shows how tightly regression connects to correlation: if r = 1, the slope is exactly s_y / s_x; if r = 0, the slope is 0 and the best prediction for y is just ȳ regardless of x.

The intercept follows from a key property of the regression line: it always passes through the point (x̄, ȳ), the means of both variables. Once you have the slope b, the intercept is a = ȳ − b × x̄. This means the regression line is anchored at the center of the data and tilted according to the correlation and spread. Interpreting the slope: b says "for every one-unit increase in x, the predicted y changes by b units." Interpreting the intercept: a is the predicted y when x = 0, which may or may not be meaningful depending on whether x = 0 is in the range of your data.

Two important limitations: regression describes association, not causation. Height and shoe size are correlated; fitting a regression doesn't mean height *causes* shoe size. Second, **extrapolation** — predicting y for an x value far outside your data range — is unreliable. The linear relationship observed in your data may not hold beyond it. A regression of height vs. weight in adults would give nonsense predictions for newborns. The regression line is a summary of the data you have, not a universal law, and the **residual** yᵢ − ŷᵢ for each point quantifies how far reality deviates from that summary.
