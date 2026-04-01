---
id: meta-analysis-systematic-review
title: Meta-Analysis and Systematic Review
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-advanced
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
status: validated
---

# Meta-Analysis and Systematic Review

## Core Idea
Meta-analysis synthesizes results across multiple studies, combining effect sizes to estimate pooled effects and variation across studies. Systematic review follows transparent protocols to identify all relevant studies, assess quality, and extract data, mitigating publication bias and cherry-picking. Meta-analyses are increasingly central to policy: they provide high-level evidence when individual studies are inconsistent or small. Challenges include heterogeneity (why do effects differ?), comparability (do studies measure the same construct?), and quality variation.

## Questions

```yaml
- question: "A meta-analysis of ten studies on a job training program finds a pooled effect size of d = 0.45 with I² = 82%. What is the most appropriate interpretation?"
  type: multiple-choice
  options:
    - "The program reliably increases earnings by 0.45 standard deviations across all contexts"
    - "The high I² indicates that most variation across studies reflects real contextual differences, so the single pooled estimate may be misleading — meta-regression is needed to understand why effects differ"
    - "The meta-analysis is invalid because the studies produced inconsistent results"
    - "The pooled estimate should be fully trusted because averaging across more studies always reduces error"
  answer: 1
  explanation: "I² measures what proportion of cross-study variation is real heterogeneity rather than sampling noise. An I² of 82% means most variation is genuine — the studies are not all measuring the same effect in the same population. Simply reporting a pooled average obscures this: the 'true' effect size likely varies by context, population, treatment intensity, or outcome measure. Meta-regression, examining whether study-level moderators predict effect size differences, is the appropriate next step. Option A overstates certainty; option C mistakes heterogeneity for invalidity; option D misapplies the precision logic."

- question: "Why does meta-analysis weight studies by the inverse of their variance rather than giving each study equal weight?"
  type: multiple-choice
  options:
    - "Larger studies are more recent and use better methods, so they deserve more weight"
    - "Inverse-variance weighting ensures that studies with smaller standard errors — which are more precise estimates — contribute more to the pooled effect size"
    - "Studies with low variance are rare, so weighting by inverse variance increases the number of qualifying studies"
    - "Equal weighting would overcount null results, introducing publication bias into the pooled estimate"
  answer: 1
  explanation: "Inverse-variance weighting is a precision-weighting scheme: studies with smaller standard errors (narrower confidence intervals, more precise estimates) are given more weight because they contain more information about the true effect. A study with n=5,000 has a much smaller standard error than one with n=50, so it should pull the pooled estimate toward its result more strongly. Option A conflates sample size with methodological quality — large studies can be methodologically weak. Option D confuses inverse-variance weighting with a bias correction."

- question: "A meta-analysis that includes more studies is generally more reliable than one with fewer studies, because pooling more evidence brings the estimate closer to the true effect."
  type: true-false
  answer: false
  explanation: "More studies improve precision only when they are estimating the same underlying effect under comparable conditions. When studies are highly heterogeneous (measuring different constructs, populations, or treatments), pooling more of them can distort rather than clarify the estimate. Additionally, if the additional studies are drawn from a biased literature (e.g., all published positive findings), adding them amplifies publication bias rather than correcting it. Quality and comparability of studies matter as much as quantity."

- question: "Publication bias can cause a meta-analysis to overestimate effect sizes, because studies finding significant positive results are more likely to be published than null or negative results."
  type: true-false
  answer: true
  explanation: "Publication bias means the published literature is a non-random sample of all conducted studies — positive results get published; null results often do not. When a meta-analysis draws only from published studies, the pooled effect size is systematically inflated. Systematic reviews combat this by searching gray literature, unpublished dissertations, and conference proceedings, and by using statistical tools (funnel plot asymmetry, Egger's test, trim-and-fill methods) to detect and correct for the underrepresentation of null results."

- question: "Explain what the I² statistic measures and why a high I² value changes what you should conclude from a meta-analysis."
  type: short-answer
  answer: "I² measures the proportion of total variance across studies that reflects true heterogeneity — real differences in effect sizes — rather than sampling error. A low I² (e.g., 20%) suggests most cross-study variation is noise and a pooled average is a reasonable summary. A high I² (e.g., 80%) means most variation is genuine: the studies are not all measuring the same effect, so averaging them produces a number that may not accurately represent any specific context. High I² is a signal to investigate moderators via meta-regression — to understand which study-level factors (population, dosage, outcome measure) explain why effects differ."
  explanation: "The key shift with high I² is moving from 'what is the average effect?' to 'under what conditions is the effect large or small?' A pooled estimate with high heterogeneity is like averaging temperatures in Alaska and Florida — the number exists but doesn't describe either place well. Meta-regression replaces the average with a conditional relationship: effect as a function of moderating variables."
```

## Explainer

Any single study is limited — by its sample, its context, its measurement choices, and its inevitable noise. Statistical logic tells you that estimates from small samples are imprecise: confidence intervals are wide, and results can reverse by chance. Meta-analysis and systematic review are the scientific response to this problem. Rather than waiting for one definitive study, they aggregate evidence across many studies to produce estimates that are more precise and more generalizable.

The conceptual foundation is straightforward. Imagine ten studies each estimating the effect of a job training program on earnings. Each has its own sample size, its own effect size estimate, and its own standard error. A **meta-analysis** takes these ten effect sizes, weights each by its precision (typically the inverse of its variance), and computes a weighted average. The result — a **pooled effect size** — is more precise than any individual estimate because it draws on more data. The confidence interval around the pooled estimate is correspondingly narrower. You can think of this as a variance-reduction procedure: more observations, more signal, less noise. The same logic that makes larger samples better applies here, treating studies as units of observation.

The harder problem is **heterogeneity**: why do effect sizes differ across studies? Some variation is just sampling noise — you expect estimates to scatter even if all studies are measuring the same true effect. But some variation reflects genuine differences in context, population, treatment intensity, or outcome measurement. The **I² statistic** quantifies what proportion of variation across studies is real heterogeneity rather than sampling error. High I² signals that you should not simply average — you need to understand why effects differ, which requires **meta-regression** to examine whether study-level characteristics (year, sample demographics, treatment dosage) moderate the effect size.

**Systematic review** is the procedural infrastructure underlying good meta-analysis. A systematic review specifies in advance — ideally in a registered protocol — the inclusion criteria, databases to search, quality assessment procedure, and statistical approach. This pre-registration prevents the cherry-picking that plagues narrative reviews, where authors cite only the studies that support their prior view. **Publication bias** is the systematic problem that positive results are more likely to be published than null results, meaning the published literature is a biased sample of all conducted research. Meta-analyses combat this by searching gray literature, unpublished theses, and conference proceedings, and by using statistical tests (funnel plot asymmetry, Egger's test) to detect whether small positive studies are overrepresented in the evidence base. The quality of a meta-analysis ultimately depends on the quality of the studies it synthesizes — and on the rigor of the review process that assembled them.
