---
id: meta-analysis-methods
title: Meta-Analysis Methods and Heterogeneity Assessment
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: measures-of-association
  type: hard
- id: biostatistics-in-public-health
  type: soft
tags:
- meta-analysis
- systematic-review
- fixed-effects
- random-effects
- heterogeneity
stage: advanced
status: draft
---

# Meta-Analysis Methods and Heterogeneity Assessment

## Core Idea
Meta-analysis combines effect estimates from multiple studies to derive an overall estimate. Fixed-effects models assume a single true effect; random-effects models assume effects vary across studies. Heterogeneity (I² statistic, Q-test) quantifies variation among study effects. Meta-analysis increases statistical power and generalizability but requires careful attention to publication bias and quality assessment.

## Explainer

You already know how to calculate measures of association — risk ratios, odds ratios, mean differences — from individual studies, and you understand confidence intervals as expressions of statistical uncertainty. Meta-analysis starts from the observation that each individual study is a noisy estimate of some underlying truth, and that mathematically combining estimates from many studies should yield a more precise and more reliable summary estimate. The key word is "should" — the validity of the combination depends entirely on whether the studies are measuring the same thing.

The mechanics of a meta-analysis begin with a **systematic review**: a pre-specified, comprehensive search for all studies that meet defined eligibility criteria, followed by data extraction and quality assessment. Only once you have identified and characterized the eligible studies does the statistical pooling begin. Each study contributes a point estimate (say, an odds ratio) and a standard error. The standard meta-analytic approach weights each study's estimate by the inverse of its variance — studies with larger samples and tighter confidence intervals get more weight, because they carry more information. The weighted average is the pooled estimate, displayed visually in a **forest plot**: a figure where each study appears as a horizontal line (the confidence interval) with a box (whose area represents its weight), and the overall pooled estimate appears as a diamond at the bottom.

The critical statistical question is whether the studies' true effects are the same or vary. The **Q-test** assesses whether the variation among study estimates exceeds what we would expect from sampling error alone. The **I² statistic** quantifies what proportion of total variation is due to between-study heterogeneity rather than chance: I² near 0% means most variation is noise; I² above 50–75% signals substantial heterogeneity. Under a **fixed-effects model**, we assume all studies estimate the same underlying true effect, and we only need to deal with within-study sampling error. Under a **random-effects model** (more common in epidemiology), we assume there is a distribution of true effects across studies — perhaps because different populations, doses, or measurement methods produce genuinely different effects — and we estimate the mean of that distribution along with its variance (τ²). Random-effects models produce wider confidence intervals than fixed-effects models, appropriately reflecting greater uncertainty.

A major threat to meta-analytic conclusions is **publication bias**: studies with statistically significant results are more likely to be published than null studies, so the literature represents a biased sample of all conducted research. A **funnel plot** can visually detect this: if the true effect is estimated without bias, study estimates should scatter symmetrically around the summary estimate, with smaller studies showing more scatter. Asymmetry in the funnel plot suggests missing studies, typically in the region of small, null results. Statistical tests (Egger's test, Begg's test) can formalize this assessment, though they have limited power with few studies. A well-conducted meta-analysis treats all these issues explicitly, making transparent what assumptions drive the conclusions and where fragility lies — which is why understanding methodology matters as much as reading the headline pooled estimate.
