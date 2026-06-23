---
id: residuals-and-goodness-of-fit
title: Residuals and Goodness of Fit (R²)
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: hard
- id: linear-regression-basics
  type: hard
- id: linear-regression-probability-and-statistics
  type: hard
tags:
- residuals
- R-squared
- goodness-of-fit
- residual-plots
- model-diagnostics
stage: formal-systems
status: validated
---

# Residuals and Goodness of Fit (R²)

## Core Idea
A residual is the difference between an observed y value and the predicted value ŷ from the regression line: eᵢ = yᵢ − ŷᵢ. Residual plots (residuals vs. fitted values or vs. predictor) reveal whether the linear model is appropriate — random scatter around zero indicates a good fit, while patterns suggest the model is misspecified. The coefficient of determination R² = r² gives the proportion of variability in y explained by the linear model, ranging from 0 (no explanatory power) to 1 (perfect linear fit).

## How It's Best Learned
Generate residual plots from regression output in software and practice recognizing patterns: funnel shapes indicate non-constant variance, curved patterns indicate nonlinearity. Connect R² to correlation: if r = 0.8, then R² = 0.64 — 64% of variation in y is explained by x.

## Common Misconceptions
- Thinking R² = 0.7 means 70% of data points are on or near the regression line.
- Treating a high R² as definitive proof the model is appropriate — always check residual plots.
- Confusing R² for simple regression (= r²) with adjusted R² from multiple regression.

## Questions

```yaml
- question: "A student calculates R² = 0.81 for a regression of exam score on study hours and concludes that '81% of the data points lie on or near the regression line.' What is wrong with this interpretation?"
  type: multiple-choice
  options:
    - "Nothing — R² = 0.81 does mean that 81% of the data points cluster near the line"
    - "She should say 81% of points lie exactly on the line, not near it"
    - "R² = 0.81 means the linear model explains 81% of the variation in exam scores, not that 81% of points are close to the line"
    - "R² measures the slope of the regression line, not the closeness of points to it"
  answer: 2
  explanation: "R² is the proportion of variance in y explained by the model: R² = 1 − SSR/SST. R² = 0.81 means 81% of the total variability in y is accounted for by the linear relationship with x. It says nothing about how many points happen to lie near the line — even with R² = 0.81, individual points can be far from the line. This is the single most common misreading of R²."

- question: "After fitting a linear regression, you plot residuals vs. fitted values and see a clear U-shaped (curved) pattern. What is the correct conclusion?"
  type: multiple-choice
  options:
    - "The regression is overfitted and should be simplified by removing predictors"
    - "There are too many outliers pulling the line off course"
    - "The variance of the residuals is non-constant (heteroscedasticity)"
    - "The linear model is misspecified — the true relationship between x and y is nonlinear"
  answer: 3
  explanation: "A curved pattern in a residual plot (smile or frown shape) is the signature of a nonlinear underlying relationship. You fit a line to something curved, so the residuals are systematically positive in the middle and negative at the ends (or vice versa). This violates the linearity assumption. A funnel shape (spreading residuals) indicates heteroscedasticity — a separate problem. Options A and B are not supported by a curved residual pattern."

- question: "A high R² value is sufficient evidence that a linear regression model is appropriate for the data."
  type: true-false
  answer: false
  explanation: "False — this is the most dangerous misconception about R². R² only measures the fraction of variance explained; it says nothing about whether the linear form is correct. A strongly curved relationship can produce a high R² while being fundamentally misspecified. A polynomial relationship, for example, can yield R² > 0.90 while having a dramatically curved residual plot revealing that a linear model is wrong. Always pair R² with a residual plot inspection."

- question: "In ordinary least squares regression, the residuals always sum to exactly zero."
  type: true-false
  answer: true
  explanation: "True. OLS chooses the regression line by minimizing the sum of squared residuals. A consequence of this optimization — specifically, that one of the normal equations forces the line to pass through the mean point (x̄, ȳ) — is that the residuals sum to exactly zero. This is not an approximation; it is an algebraic identity that holds for any OLS fit."

- question: "Explain why a pattern in a residual plot indicates a problem with the model even when R² is high."
  type: short-answer
  answer: "R² measures the fraction of total variance that the model explains, but it does not test whether the linear form is appropriate. A pattern in residuals (curved, funnel-shaped) reveals that systematic structure in the data is not being captured — the errors are not random noise but rather predictable deviations the model cannot see. A curved residual pattern means the model is systematically over- or under-predicting in different regions, violating the linearity assumption. R² can be high while the model is still wrong about the functional form."
  explanation: "The residual plot is the primary diagnostic for model appropriateness. R² is a summary statistic that collapses the fit into one number; the residual plot preserves the spatial structure of the errors. Both are needed: R² answers 'how much variance is explained?' while the residual plot answers 'is the model form valid?'"
```

## Explainer

Once you have fit a linear regression line to data, the natural question is: how well does it fit? The **residual** for each observation is the answer to that question at a single point — it is the gap between what the model predicted and what actually happened: eᵢ = yᵢ − ŷᵢ. A positive residual means the true value was above the line; negative means it was below. Crucially, residuals are signed — they don't cancel each other out by accident, but they do cancel on average: in ordinary least squares regression, the residuals always sum to zero. This is not a coincidence; the regression line was chosen precisely to minimize the sum of squared residuals, and that optimization forces the sum to be zero.

The most informative diagnostic tool is the **residual plot** — a scatterplot of residuals on the vertical axis against fitted values (or against the predictor x) on the horizontal axis. If the linear model is appropriate, this plot should look like random scatter around the horizontal line at zero. No trend, no fan shape, no curves. Any pattern in the residual plot is evidence of a model problem. A curved pattern (like a smile or frown) indicates the relationship is not linear — you fit a line to something curved. A **funnel shape** (residuals spread out more as fitted values increase) indicates **heteroscedasticity** — the variance of the errors is not constant. Both problems violate the assumptions that make regression inference valid. Reading a residual plot is more important than memorizing any formula.

The **coefficient of determination**, R², answers the question: what fraction of the total variation in y does the model account for? To build the intuition, think about two extremes. If you ignored x entirely and just predicted ȳ for every observation, your total prediction error would be the total variability in y — called the **total sum of squares** (SST). Now imagine the regression model reduces that error by explaining some of the variation. The **residual sum of squares** (SSR) is the variation the model could not explain. R² = 1 − SSR/SST: the proportion of variability the model did explain. An R² of 0.64 means 64% of the variation in y is accounted for by the linear relationship with x; the other 36% is noise the model cannot see.

For simple linear regression with one predictor, R² equals r² — the square of the correlation coefficient you already know. This means R² inherits a clean geometric meaning: if r = 0.8, there is a strong linear relationship, and R² = 0.64. If r = 0.5, the relationship is moderate, and only R² = 0.25 of the variation is explained. The squaring is important — it strips the sign from r (direction doesn't matter for explanatory power) and always gives a value between 0 and 1. However, a high R² is not sufficient evidence that a model is good. A curved relationship can still have high R² while being fundamentally misspecified. Always pair R² with a residual plot inspection: R² measures how much variation is explained; the residual plot tells you whether the explanation is valid.
