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
status: draft
---

# Assumption Violations and Statistical Test Robustness

## Core Idea
Statistical tests rest on assumptions (normality, homogeneity of variance, independence of observations) that, when violated, can compromise validity of conclusions. Robust methods are relatively insensitive to assumption violations; when assumptions are severely violated, alternative tests or data transformations are appropriate. Documenting assumption checking and justifying analytical choices strengthens research reporting.

## Explainer

From inferential statistics, you know that procedures like the t-test and ANOVA produce p-values by comparing an observed test statistic against a theoretical sampling distribution. That theoretical distribution — the one that tells you how likely your result would be under the null hypothesis — was derived under specific mathematical conditions. These conditions are the **assumptions** of the test. When the assumptions hold, the p-value means what it says. When they are violated, the sampling distribution you are comparing against may be wrong, and the p-value can mislead.

The three core assumptions for most parametric tests are **normality** (the outcome variable, or the residuals from the model, follow a normal distribution within groups), **homogeneity of variance** (the spread of scores is similar across the groups being compared), and **independence of observations** (each data point is unrelated to others — one person's score does not predict another's). Of these, independence is by far the most serious. Violating independence — for example, by collecting multiple responses from the same person and treating them as independent — can inflate your false-positive rate dramatically, because clustered observations carry far less information than truly independent ones. Normality and homogeneity violations are more forgiving, especially with larger samples.

This is where **robustness** becomes important. A test is robust to a given assumption if its Type I error rate (false positive rate) and power stay close to their nominal values even when that assumption is violated. The t-test and ANOVA are reasonably robust to non-normality when sample sizes are large (invoking the central limit theorem) and groups are roughly equal in size. However, both are more sensitive to **heteroscedasticity** (unequal variances), especially when group sizes differ. When variances are unequal and group sizes are unbalanced, the standard F-test can produce p-values that are substantially wrong. Welch's correction for the t-test and its ANOVA analog directly address this by adjusting the degrees of freedom.

When violations are severe, two general strategies exist: **non-parametric alternatives** that make fewer distributional assumptions (Wilcoxon rank-sum instead of t-test, Kruskal-Wallis instead of one-way ANOVA), or **data transformations** that pull the distribution closer to normality before applying parametric tests. Common transformations include log transforms for positive-skewed data (e.g., reaction times, income), square-root transforms for count data, and arcsine transforms for proportions. Neither strategy is universally superior — non-parametric tests lose power when the distributional assumptions of parametric tests are actually met, and transformations can make results harder to interpret. The practical skill is diagnosing which assumptions matter most for your specific design and data, checking them using residual plots and diagnostic statistics rather than relying on significance tests of the assumptions themselves (which are often underpowered for the violations that matter), and documenting your choices transparently so readers can evaluate your analytic decisions.
