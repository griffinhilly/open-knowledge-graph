---
id: publication-bias-detection
title: Publication Bias and Reporting Bias
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: meta-analysis-methods
  type: hard
- id: sensitivity-analysis-epidemiology
  type: soft
tags:
- publication-bias
- selective-reporting
- meta-analysis-bias
stage: advanced
status: draft
---

# Publication Bias and Reporting Bias

## Core Idea
Publication bias occurs when studies with significant positive results are more likely to be published than null results, biasing synthesized evidence toward inflated effects. Funnel plots, Egger regression, and trim-and-fill methods assess asymmetry suggesting publication bias. Reporting bias similarly distorts meta-analytic results.

## Explainer

From your study of meta-analysis methods, you know that a meta-analysis pools effect estimates from multiple studies to produce a more precise summary estimate. The validity of that summary estimate rests on an assumption that is rarely stated explicitly: that the studies you pooled are a representative sample of *all* studies that were ever conducted on the question. Publication bias directly violates this assumption. The problem, sometimes called the **file drawer problem**, is that studies with null or negative results are systematically less likely to be submitted, accepted, or published than studies with positive results. This means the literature is a biased sample of the evidence — and a meta-analysis of a biased sample produces a biased estimate.

The canonical diagnostic tool is the **funnel plot**, which plots each study's effect estimate on the x-axis against a measure of its precision (typically standard error or sample size) on the y-axis. Large, precise studies cluster near the top with narrow confidence intervals and should be close to the true effect. Small studies have wide confidence intervals and should scatter broadly but symmetrically around the true effect. If there is no publication bias, the plot should look like an inverted funnel — symmetric around the true effect. **Asymmetry** in the funnel, especially a gap in the lower-left quadrant (small studies with small or negative effects that are missing), suggests that the small null or negative studies were never published. Importantly, funnel asymmetry can also arise from genuine heterogeneity, quality differences, or chance — the funnel plot is a tool for raising questions, not providing definitive answers.

To quantify funnel plot asymmetry more formally, **Egger's regression** regresses the standardized effect estimate on its standard error; a non-zero intercept indicates asymmetry. The **trim-and-fill method** goes further: it iteratively removes asymmetric outlier studies on one side of the funnel (the "trim" step), estimates the true center, then imputes hypothetical missing studies on the other side (the "fill" step), producing an adjusted pooled estimate that accounts for the estimated missing evidence. If the trim-and-fill estimate is substantially different from the original meta-analytic estimate, this is a red flag that the pooled effect may be inflated.

**Reporting bias** is a distinct but related problem — it occurs not at the level of the whole study but at the outcome level. A single trial may be published, but only the statistically significant outcomes may be reported, while non-significant secondary outcomes are buried or omitted. Comparing registered trial protocols (in ClinicalTrials.gov or WHO ICTRP) against published reports reveals this pattern. The **ORBIT framework** and systematic methods for detecting selective outcome reporting are part of the Cochrane risk-of-bias toolkit. Together, publication bias and reporting bias represent two of the most serious threats to the validity of evidence synthesis, because unlike random error, they introduce systematic inflation of effects that grows rather than shrinks as more small studies are pooled.
