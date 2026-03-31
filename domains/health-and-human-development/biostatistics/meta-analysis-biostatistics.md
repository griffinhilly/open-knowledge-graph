---
id: meta-analysis-biostatistics
title: Meta-Analysis in Biostatistics
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: study-design-biostatistics
  type: hard
- id: power-and-sample-size
  type: soft
- id: multiple-testing-corrections
  type: soft
builds-toward:
- network-meta-analysis
tags:
- meta-analysis
- systematic-review
- heterogeneity
- fixed-effect
- random-effects
- forest-plot
- publication-bias
stage: expert
status: validated
---

# Meta-Analysis in Biostatistics

## Core Idea
Meta-analysis statistically combines the results of multiple independent studies addressing the same research question to produce a single, more precise summary estimate. It weights each study inversely proportional to its variance (larger, more precise studies get more weight) and produces a pooled effect size with a narrower confidence interval than any individual study. The critical choice is between a fixed-effect model (assumes all studies estimate the same true effect) and a random-effects model (assumes study-specific true effects drawn from a distribution, with between-study heterogeneity). The I-squared statistic quantifies the proportion of total variability due to heterogeneity rather than sampling error. Meta-analyses are threatened by publication bias (studies with positive results are more likely to be published) and require systematic review methodology to identify all relevant studies, not just the convenient ones.

## Questions

```yaml
- question: "A meta-analysis of 15 trials testing a drug for hypertension reports I² = 85%. What does this indicate and what are the implications?"
  type: multiple-choice
  options:
    - "85% of studies support the drug — it is highly effective"
    - "85% of the observed variability in effect sizes is due to genuine heterogeneity between studies rather than sampling error, suggesting the true effect likely varies across study populations or conditions"
    - "The meta-analysis has 85% statistical power"
    - "85% of patients in the studies experienced a benefit"
  answer: 1
  explanation: "I² = 85% indicates substantial between-study heterogeneity — the studies are not estimating the same quantity. This does not mean the meta-analysis is invalid, but it means the pooled estimate represents an average across genuinely different effects. The critical follow-up is to investigate why effects vary: are certain patient populations, drug doses, or outcome definitions driving the heterogeneity? A random-effects model is appropriate here, and subgroup analyses or meta-regression should explore sources of heterogeneity."

- question: "A funnel plot for a meta-analysis shows asymmetry, with small studies predominantly reporting large positive effects. What does this suggest?"
  type: multiple-choice
  options:
    - "Small studies are more rigorous and therefore find larger effects"
    - "Publication bias — small studies with null or negative results were likely conducted but not published, leaving an asymmetric distribution of reported effects"
    - "The treatment is more effective in small studies"
    - "The meta-analysis included too many studies"
  answer: 1
  explanation: "A symmetric funnel plot is expected when published studies represent all conducted studies: small studies scatter widely around the pooled estimate, and large studies cluster tightly. Asymmetry — particularly an absence of small studies with small or negative effects — suggests publication bias: those studies were conducted but their results were not published because they were not statistically significant or were perceived as uninteresting. Statistical tests (Egger's test, Begg's test) and trim-and-fill methods can assess and partially adjust for this bias."

- question: "A fixed-effect meta-analysis assumes all studies share a single true effect size, while a random-effects model assumes study-specific true effects drawn from a distribution. When there is substantial heterogeneity, the fixed-effect model gives too much weight to large studies."
  type: true-false
  answer: true
  explanation: "Under the fixed-effect model, weights are inversely proportional to within-study variance only. Large studies have small variance and dominate the pooled estimate. Under the random-effects model, weights include an additional between-study variance component, which equalizes weights across studies — even large studies carry non-trivial between-study uncertainty. When heterogeneity is substantial, the random-effects model gives relatively more weight to smaller studies than the fixed-effect model, and the confidence interval is wider, properly reflecting the uncertainty about the true distribution of effects."

- question: "Explain why a meta-analysis that pools only published studies, without a systematic search for unpublished data, may produce a biased summary effect."
  type: short-answer
  answer: "Studies with statistically significant or positive results are more likely to be published, submitted, and accepted. If a meta-analysis includes only published studies, it oversamples positive results and undersamples null or negative results. The pooled estimate is therefore biased toward larger effects than the true average across all conducted studies. This publication bias can make an ineffective treatment appear effective or make a modestly effective treatment appear highly effective."
  explanation: "This is why rigorous meta-analyses use systematic review methodology: searching multiple databases, registries of clinical trials (ClinicalTrials.gov), grey literature (conference abstracts, dissertations), and contacting study authors for unpublished data. Pre-registration of systematic review protocols (PROSPERO) further protects against selective reporting of meta-analytic results."
```

## Explainer

Individual studies are often too small to detect clinically important effects with adequate power. Meta-analysis addresses this by combining results across studies, effectively increasing the sample size and producing more precise estimates. But it is not simply adding up patients — each study is treated as the unit of analysis, and its result is weighted by its precision (inversely proportional to the variance of its effect estimate). A study of 10,000 patients gets more weight than a study of 50 patients because its estimate is more precise.

The fundamental distinction is between **fixed-effect** and **random-effects** models. A fixed-effect model assumes every study estimates the same true underlying effect — differences between observed effect sizes are due entirely to sampling variation. A random-effects model assumes that each study has its own true effect size, drawn from a distribution of effects, and the meta-analytic goal is to estimate the mean of that distribution. The choice matters: when heterogeneity is present, the fixed-effect confidence interval is too narrow (it ignores between-study variability), and the random-effects model is more appropriate. The **I-squared statistic** quantifies heterogeneity — the proportion of total variability attributable to true differences between studies rather than chance. Values above 50% are conventionally considered substantial heterogeneity.

**Forest plots** are the visual workhorse of meta-analysis. Each horizontal line represents one study: the point estimate and its confidence interval. The diamond at the bottom represents the pooled estimate, with its width showing the pooled confidence interval. Studies with wider confidence intervals (less precise) have less influence on the diamond. When the lines are scattered widely and the diamond's confidence interval is narrow, you have high precision but high heterogeneity — and the single pooled number may be misleading as a summary.

The most serious threat to meta-analysis validity is **publication bias**. If studies with non-significant results are less likely to be published, the meta-analysis systematically overestimates the effect. Funnel plots (plotting study precision against effect size) provide a visual diagnostic: an asymmetric funnel, with small studies missing on the null side, suggests bias. Statistical corrections (trim-and-fill, selection models) can partially adjust for this, but the best protection is a comprehensive systematic review that searches for unpublished data. The distinction between meta-analysis (the statistical method) and systematic review (the comprehensive literature search methodology) is important — meta-analysis without systematic review is a quantitative synthesis of a biased sample.
