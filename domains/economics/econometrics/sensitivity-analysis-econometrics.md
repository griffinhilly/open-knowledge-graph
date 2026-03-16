---
id: sensitivity-analysis-econometrics
title: Sensitivity Analysis and Robustness Checks
domain: economics
course: econometrics
prerequisites:
- id: specification-tests-econometrics
  type: soft
- id: bootstrap-inference-econometrics
  type: soft
tags:
- robustness
- sensitivity
- specification
stage: formal-systems
status: draft
---

# Sensitivity Analysis and Robustness Checks

## Core Idea
Sensitivity analysis examines whether estimates remain robust to alternative assumptions, functional forms, samples, or control variables. It provides evidence of how sensitive conclusions are to modeling choices.

## Explainer

Every econometric estimate you produce is conditional on dozens of choices you made along the way: which control variables to include, what functional form to assume, how to handle outliers, which sample restriction to apply, what standard error correction to use. From specification testing you know how to formally test some of those choices. But formal tests only tell you whether a specific alternative model fits the data better — they cannot tell you whether your conclusions survive the full range of reasonable modeling decisions. **Sensitivity analysis** is the practice of deliberately varying those choices and observing whether your estimates remain stable.

The most common form is **coefficient stability analysis**: estimate your key coefficient under a sequence of specifications, progressively adding or removing control variables, and examine the path of estimates and confidence intervals. If your treatment effect estimate is 0.4 with no controls, 0.38 with demographic controls, 0.35 with further economic controls, and never moves outside [0.2, 0.5] across any reasonable specification, that stability is strong evidence the result is not an artifact of a particular specification choice. Conversely, if adding a single control variable moves the estimate from 0.4 to 0.02 and removes significance, the conclusion was fragile — hanging on the exclusion of that variable — and you should investigate why. The **Oster (2019)** approach formalizes this by bounding the treatment effect under proportional selection assumptions, asking: how much selection on unobservables relative to observables would be required to drive the effect to zero?

**Sample robustness checks** ask whether the result holds for plausible subsamples: dropping extreme observations, restricting to a cleaner part of the distribution, splitting by time period or demographic group. These serve two purposes. First, they diagnose whether results are driven by a small influential subset rather than the broad pattern in the data. Second, they address external validity — does the effect hold across different subpopulations? **Functional form robustness** involves comparing linear models to log specifications, quadratic terms, or nonparametric alternatives like local linear regression, checking whether nonlinearity in the underlying relationship is distorting your estimates.

The bootstrap inference techniques you have already studied are closely connected: the bootstrap quantifies sampling variability, but sensitivity analysis quantifies **specification variability** — how much your estimate moves when you vary the model rather than the sample. Together they give a fuller picture of uncertainty than a single confidence interval. A credible empirical paper presents sensitivity analysis not as an afterthought but as a core component of the argument: the reader needs to know not just that *this particular* model produced *this estimate*, but that estimates in a defensible neighborhood of specifications consistently support the same conclusion. The failure mode to avoid is **specification searching** — running many specifications and reporting only the most favorable one, which is a form of pre-analysis dishonesty. Sensitivity analysis should be pre-committed or conducted transparently across a pre-specified grid of choices.
