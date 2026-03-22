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

## Questions

```yaml
- question: "A regression of annual salary (y) on years of education (x) yields ŷ = 20,000 + 3,500x. A student concludes: 'Getting one more year of education causes your salary to increase by $3,500.' What is wrong with this interpretation?"
  type: multiple-choice
  options:
    - "The intercept $20,000 is implausibly low, which invalidates the slope interpretation"
    - "The slope represents a predictive association, not causation — lurking variables like field of study or ability could explain the relationship"
    - "The interpretation is only valid for people with exactly average education levels"
    - "The interpretation is correct as long as the R² value is sufficiently high"
  answer: 1
  explanation: "Regression describes the average difference in y associated with a one-unit difference in x in the observed data — an associative relationship. It cannot establish that changing x produces the change in y. Students with more education may earn more for many reasons besides education itself (family background, field of study, innate ability). A high R² confirms the line fits well; it says nothing about causation. Causal claims require experimental design where x is randomly assigned."

- question: "A researcher fits a regression line to data on tree heights (y) and trunk diameter (x) for trees between 5 and 80 cm in diameter. She then uses the line to predict the height of a tree with a 200 cm diameter. Why is this prediction unreliable?"
  type: multiple-choice
  options:
    - "Regression equations cannot be evaluated at values larger than the sample mean"
    - "The linear relationship may not hold beyond the observed range — the line has no obligation to track data where it hasn't been observed"
    - "The slope b₁ changes its value outside the observed data range"
    - "Predictions are unreliable whenever the x-value is more than one standard deviation from the mean"
  answer: 1
  explanation: "Extrapolation uses the regression line to predict y for x values outside the observed data range. The fitted line summarizes the linear trend within that range; there is no guarantee the relationship stays linear (or even monotone) beyond it. Very large trees may follow different growth patterns. The regression equation doesn't change — our confidence that it describes reality outside the observed range is gone. The line has been stretched beyond where it was calibrated."

- question: "The regression line ŷ = b₀ + b₁x always passes through the point (x̄, ȳ) — the sample means of both variables."
  type: true-false
  answer: true
  explanation: "This is a direct consequence of the least-squares conditions. Setting the partial derivatives of the sum of squared residuals to zero forces the line to pass through the centroid (x̄, ȳ). This fact also explains why b₀ = ȳ − b₁x̄: the intercept is derived from the requirement that the line hits the balance point of the data. You can verify this for any regression line you fit."

- question: "To predict x from y, you can simply rearrange the regression equation ŷ = b₀ + b₁x algebraically to solve for x."
  type: true-false
  answer: false
  explanation: "The regression of y on x and the regression of x on y are different lines that minimize different quantities. The 'y on x' regression minimizes vertical (squared) distances from points to the line; the 'x on y' regression minimizes horizontal distances. Algebraically rearranging the first line gives slope 1/b₁, but this is NOT the least-squares line for predicting x from y. The two regressions only coincide when r = ±1 (a perfect linear relationship). This is one of the most persistent misconceptions in regression analysis."

- question: "Why does the slope of a regression line represent a predictive rather than causal relationship, and what would be required to justify a causal interpretation?"
  type: short-answer
  answer: "The slope b₁ describes the average difference in y associated with a one-unit difference in x in the observed data. Because many other variables (lurking variables) might cause both x and y to vary together, we cannot conclude that changing x produces the observed change in y. To justify a causal interpretation, we would need experimental evidence: randomly assigning different values of x to subjects so that lurking variables cannot systematically differ between groups, isolating x as the only thing that differs."
  explanation: "This distinction is fundamental to statistical reasoning. Regression is a powerful descriptive and predictive tool, but it operates on observational data where confounders are common. The jump from 'associated with' to 'causes' requires ruling out alternative explanations — which observational regression alone cannot do. Recognizing this boundary is one of the most practically important skills in applied statistics."
```

## Explainer

From the correlation coefficient r, you know how to measure the strength and direction of a linear association between two variables. But r just gives a single number between −1 and 1 — it doesn't tell you *how much* y changes for a one-unit change in x, and it doesn't give you a formula for prediction. **Simple linear regression** takes the next step: it finds the specific line ŷ = b₀ + b₁x that best fits the data, where "best" is precisely defined as minimizing the total squared vertical distance between each observed point and the line.

The criterion is **least squares**: minimize Σ(yᵢ − ŷᵢ)², where yᵢ is the observed value and ŷᵢ = b₀ + b₁xᵢ is the predicted value. Each difference yᵢ − ŷᵢ is called a **residual** — the amount by which the line misses the actual point. Squaring residuals before summing means large misses are penalized heavily; it also makes the optimization tractable. Taking derivatives and setting them to zero gives closed-form formulas: b₁ = r · (sᵧ/sₓ) and b₀ = ȳ − b₁x̄. Notice how b₁ inherits its sign and direction from r, then scales it by the ratio of standard deviations to convert from correlation units to actual slope units. The fact that the line passes through (x̄, ȳ) — the "balance point" of the data — is a direct consequence of the least-squares conditions.

Interpreting the slope b₁ requires care. It says: on average, when x increases by 1 unit, the predicted y changes by b₁ units. This is a **predictive** or **associative** statement, not a causal one. If b₁ = 2.3 in a regression of exam scores on hours studied, it means students who study 1 hour more than average tend to score 2.3 points higher — it does not mean studying an extra hour *causes* exactly 2.3 more points. Lurking variables (ability, prior knowledge, motivation) could explain the association. The y-intercept b₀ is the predicted y when x = 0, which is only meaningful if x = 0 is plausible given the data range.

The correlation coefficient r has a second role in regression: r² (the **coefficient of determination**) tells you what proportion of the total variability in y is explained by the linear relationship with x. If r = 0.8, then r² = 0.64, meaning 64% of the variation in y is accounted for by knowing x. The remaining 36% is unexplained — attributable to other variables, measurement error, or nonlinearity. **Extrapolation** — using the regression line to predict y for x values outside the observed data range — is unreliable because the linear relationship may not hold beyond the observed region; the line has no obligation to track the data where we haven't looked.
