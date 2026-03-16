---
id: meta-analysis-systematic-review
title: Meta-Analysis and Systematic Review
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-advanced
  type: hard
- id: probability-and-statistics
  type: hard
- id: expected-value-and-variance
  type: soft
- id: confidence-intervals-framework
  type: soft
builds-toward:
- meta-regression-heterogeneity
- publication-bias-correction
tags:
- synthesis
- evidence
- meta-analysis
- systematic
stage: advanced
status: draft
---

# Meta-Analysis and Systematic Review

## Core Idea
Meta-analysis synthesizes results across multiple studies, combining effect sizes to estimate pooled effects and variation across studies. Systematic review follows transparent protocols to identify all relevant studies, assess quality, and extract data, mitigating publication bias and cherry-picking. Meta-analyses are increasingly central to policy: they provide high-level evidence when individual studies are inconsistent or small. Challenges include heterogeneity (why do effects differ?), comparability (do studies measure the same construct?), and quality variation.

## Explainer

Any single study is limited — by its sample, its context, its measurement choices, and its inevitable noise. Statistical logic tells you that estimates from small samples are imprecise: confidence intervals are wide, and results can reverse by chance. Meta-analysis and systematic review are the scientific response to this problem. Rather than waiting for one definitive study, they aggregate evidence across many studies to produce estimates that are more precise and more generalizable.

The conceptual foundation is straightforward. Imagine ten studies each estimating the effect of a job training program on earnings. Each has its own sample size, its own effect size estimate, and its own standard error. A **meta-analysis** takes these ten effect sizes, weights each by its precision (typically the inverse of its variance), and computes a weighted average. The result — a **pooled effect size** — is more precise than any individual estimate because it draws on more data. The confidence interval around the pooled estimate is correspondingly narrower. You can think of this as a variance-reduction procedure: more observations, more signal, less noise. The same logic that makes larger samples better applies here, treating studies as units of observation.

The harder problem is **heterogeneity**: why do effect sizes differ across studies? Some variation is just sampling noise — you expect estimates to scatter even if all studies are measuring the same true effect. But some variation reflects genuine differences in context, population, treatment intensity, or outcome measurement. The **I² statistic** quantifies what proportion of variation across studies is real heterogeneity rather than sampling error. High I² signals that you should not simply average — you need to understand why effects differ, which requires **meta-regression** to examine whether study-level characteristics (year, sample demographics, treatment dosage) moderate the effect size.

**Systematic review** is the procedural infrastructure underlying good meta-analysis. A systematic review specifies in advance — ideally in a registered protocol — the inclusion criteria, databases to search, quality assessment procedure, and statistical approach. This pre-registration prevents the cherry-picking that plagues narrative reviews, where authors cite only the studies that support their prior view. **Publication bias** is the systematic problem that positive results are more likely to be published than null results, meaning the published literature is a biased sample of all conducted research. Meta-analyses combat this by searching gray literature, unpublished theses, and conference proceedings, and by using statistical tests (funnel plot asymmetry, Egger's test) to detect whether small positive studies are overrepresented in the evidence base. The quality of a meta-analysis ultimately depends on the quality of the studies it synthesizes — and on the rigor of the review process that assembled them.
