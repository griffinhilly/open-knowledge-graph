---
id: dose-response-relationships
title: Dose-Response Analysis and Exposure-Outcome Curves
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: measures-of-association
  type: hard
- id: multivariable-regression-epi
  type: hard
builds-toward:
- exposure-measurement-error-epi
tags:
- dose-response
- exposure-response
- effect-estimation
- causality-criteria
stage: advanced
status: draft
---

# Dose-Response Analysis and Exposure-Outcome Curves

## Core Idea
Dose-response relationships examine how the magnitude of exposure affects the magnitude of effect. Evidence of a dose-response strengthens causal inference because the relationship follows expected biologic gradients. Analysis may use linear, polynomial, or spline regression to characterize the functional form.

## Explainer

From your study of measures of association, you know that epidemiology routinely compares binary exposure groups — exposed vs. unexposed — using risk ratios, odds ratios, or rate ratios. Dose-response analysis extends this framework: instead of asking "does the exposure cause the outcome?", it asks "does more exposure cause more of the outcome?" This quantitative dimension is one of the most powerful tools for strengthening causal inference because it goes beyond mere association to test whether the relationship follows the gradient that a causal mechanism would predict.

The reasoning connects directly to Bradford Hill's **biological gradient criterion** — one of the considerations used to evaluate whether an observed association is likely causal. If smoking causes lung cancer, we expect heavy smokers to have higher risk than moderate smokers, who in turn have higher risk than light smokers. If every additional pack-year of exposure increases risk in a roughly consistent way, this pattern is much harder to explain by confounding alone, because a confounder would have to track exposure quantity precisely across the entire distribution. Dose-response evidence therefore shifts the evidentiary bar: a step-wise gradient from low to medium to high exposure, each with increasing risk, is more compelling than a single exposed/unexposed comparison even when the odds ratio is numerically similar.

Characterizing the **functional form** of the dose-response curve requires more than just comparing three exposure categories. From your background in multivariable regression, you know that linear regression assumes a constant increment of effect per unit increase in exposure. This is sometimes appropriate but often wrong. A **threshold model** posits no effect below a certain dose and a sharp increase above it (relevant for toxicants). A **supralinear** model posits that the first small doses carry disproportionate risk per unit. An **inverted-U** may apply where moderate doses are beneficial but high doses are harmful (as with some nutrients). **Restricted cubic splines** — piecewise polynomial functions fitted through knot points across the exposure distribution — are a flexible approach that lets the data determine the curve shape without imposing a functional form. The resulting curve can be plotted with confidence intervals to show where the association is well-estimated and where uncertainty is high.

A common pitfall is assuming that a dose-response relationship is sufficient to establish causation. **Reverse causation** can produce apparent gradients — sicker people may drink less alcohol, creating the illusion that more alcohol is protective. **Exposure measurement error** can attenuate dose-response relationships or even create artifactual U-shapes when misclassification is differential across the distribution. And **confounding by indication** can create gradients when higher doses are given to higher-risk patients. Interpreting a dose-response curve therefore requires the same rigor you apply to any measure of association: examine the study design, consider plausible confounders, and assess whether the gradient is biologically coherent given what is known about the mechanism.
