---
id: assumption-violations-robustness
title: Assumption Violations and Statistical Test Robustness
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
builds-toward:
- multiple-comparisons-and-corrections
tags:
- statistics
- assumptions
- robustness
stage: formal-systems
status: validated
---

# Assumption Violations and Statistical Test Robustness

## Core Idea
Statistical tests rest on assumptions (normality, homogeneity of variance, independence of observations) that, when violated, can compromise validity of conclusions. Robust methods are relatively insensitive to assumption violations; when assumptions are severely violated, alternative tests or data transformations are appropriate. Documenting assumption checking and justifying analytical choices strengthens research reporting.

## Questions

```yaml
- question: "A researcher measures anxiety in 50 participants, asks the same 50 participants to complete a stress task, then measures anxiety again. She treats all 100 anxiety scores as 100 independent observations in a t-test. What is the primary statistical problem?"
  type: multiple-choice
  options:
    - "The sample size of 50 is too small to use a t-test"
    - "Two measurements from the same person are correlated, so observations are not independent — the effective sample size is much smaller than 100"
    - "Anxiety scores are likely non-normal, which invalidates the t-test"
    - "She should have used an ANOVA rather than a t-test for this design"
  answer: 1
  explanation: "Independence is violated: two scores from the same person will be correlated (anxious people tend to be anxious on both occasions). When correlated observations are treated as independent, the standard error is underestimated, artificially inflating the t-statistic and the false positive rate. Treating 50 paired observations as 100 independent ones can dramatically inflate Type I error. Non-normality (option C) is generally a lesser concern, especially with larger N. Option D (ANOVA) is not the issue — the independence violation is the same regardless of which test is used."

- question: "A t-test is described as 'robust to non-normality.' What does this most precisely mean?"
  type: multiple-choice
  options:
    - "The p-value is identical whether or not the normality assumption holds"
    - "The test can be applied to any data distribution without any loss of power"
    - "The Type I error rate stays close to the nominal alpha level even when normality is violated, especially with larger samples"
    - "Non-normality only matters for t-tests when sample sizes are very small"
  answer: 2
  explanation: "Robustness means the test's operating characteristics — primarily its Type I error rate — remain close to their intended values despite assumption violations. It does NOT mean p-values are unchanged (option A) or that there is no cost to power (option B). The Central Limit Theorem explains why robustness to non-normality improves with larger samples: sampling distributions of means become approximately normal regardless of the underlying distribution. Option D overstates the case — robustness applies broadly with moderate to large equal-sized groups, not just very small samples."

- question: "A statistical test that is robust to an assumption violation produces the same p-value as it would if that assumption were perfectly satisfied."
  type: true-false
  answer: false
  explanation: "Robustness means the Type I error rate (and ideally power) stays close to nominal despite the violation — not that p-values are numerically identical under both conditions. The p-value itself may differ when assumptions are violated; what robustness guarantees is that the false positive rate remains approximately controlled at the alpha level. Confusing 'robust' with 'unaffected' leads to the mistaken belief that robustness makes assumption checking irrelevant."

- question: "With sufficiently large and roughly equal group sizes, the independent-samples t-test remains approximately valid even when the normality assumption is violated."
  type: true-false
  answer: true
  explanation: "The Central Limit Theorem ensures that sampling distributions of means approach normality as sample size increases, regardless of the shape of the underlying distribution. For the t-test, this means the test statistic follows approximately the expected distribution even with non-normal data, provided group sizes are reasonably large (often cited as n ≥ 30 per group as a rough heuristic) and roughly equal. This is why normality violations are generally more forgiving than independence violations — the latter have no such CLT rescue."

- question: "Why is violating the independence assumption generally considered more serious than violating the normality assumption for parametric tests like the t-test?"
  type: short-answer
  answer: "Independence violations inflate the false positive rate in ways the Central Limit Theorem cannot fix, because clustered observations carry less information than truly independent ones — the effective sample size may be far smaller than the nominal N."
  explanation: "When observations are correlated (e.g., multiple responses from the same person, students within classrooms), the standard error is computed as if observations were independent, which underestimates true sampling variability. The resulting t-statistic is inflated, and the p-value is too small. This can make truly null results appear significant at rates far exceeding the nominal alpha. Normality violations, by contrast, are largely rescued by the Central Limit Theorem as N grows — the sampling distribution of means normalizes regardless of the population shape. There is no analogous rescue for non-independence; the structural problem remains no matter how large N becomes."
```

## Explainer

From inferential statistics, you know that procedures like the t-test and ANOVA produce p-values by comparing an observed test statistic against a theoretical sampling distribution. That theoretical distribution — the one that tells you how likely your result would be under the null hypothesis — was derived under specific mathematical conditions. These conditions are the **assumptions** of the test. When the assumptions hold, the p-value means what it says. When they are violated, the sampling distribution you are comparing against may be wrong, and the p-value can mislead.

The three core assumptions for most parametric tests are **normality** (the outcome variable, or the residuals from the model, follow a normal distribution within groups), **homogeneity of variance** (the spread of scores is similar across the groups being compared), and **independence of observations** (each data point is unrelated to others — one person's score does not predict another's). Of these, independence is by far the most serious. Violating independence — for example, by collecting multiple responses from the same person and treating them as independent — can inflate your false-positive rate dramatically, because clustered observations carry far less information than truly independent ones. Normality and homogeneity violations are more forgiving, especially with larger samples.

This is where **robustness** becomes important. A test is robust to a given assumption if its Type I error rate (false positive rate) and power stay close to their nominal values even when that assumption is violated. The t-test and ANOVA are reasonably robust to non-normality when sample sizes are large (invoking the central limit theorem) and groups are roughly equal in size. However, both are more sensitive to **heteroscedasticity** (unequal variances), especially when group sizes differ. When variances are unequal and group sizes are unbalanced, the standard F-test can produce p-values that are substantially wrong. Welch's correction for the t-test and its ANOVA analog directly address this by adjusting the degrees of freedom.

When violations are severe, two general strategies exist: **non-parametric alternatives** that make fewer distributional assumptions (Wilcoxon rank-sum instead of t-test, Kruskal-Wallis instead of one-way ANOVA), or **data transformations** that pull the distribution closer to normality before applying parametric tests. Common transformations include log transforms for positive-skewed data (e.g., reaction times, income), square-root transforms for count data, and arcsine transforms for proportions. Neither strategy is universally superior — non-parametric tests lose power when the distributional assumptions of parametric tests are actually met, and transformations can make results harder to interpret. The practical skill is diagnosing which assumptions matter most for your specific design and data, checking them using residual plots and diagnostic statistics rather than relying on significance tests of the assumptions themselves (which are often underpowered for the violations that matter), and documenting your choices transparently so readers can evaluate your analytic decisions.
