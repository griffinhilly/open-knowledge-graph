---
id: effect-size-and-power
title: Effect Size and Statistical Power
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
- id: type-i-and-type-ii-errors
  type: soft
- id: hypothesis-testing-fundamentals
  type: soft
- id: measures-of-spread
  type: soft
- id: normal-distribution-intro
  type: soft
builds-toward:
- replication-and-open-science
tags:
- effect-size
- Cohen-d
- power
- sample-size
- type-II-error
stage: formal-systems
status: validated
---

# Effect Size and Statistical Power

## Core Idea
Effect size quantifies the practical magnitude of a relationship or difference, independent of sample size. Cohen's d measures standardized mean differences; r measures correlation magnitude. Statistical power is the probability that a study will detect a true effect when one exists — it increases with larger samples, larger effect sizes, and higher significance thresholds. Low-powered studies produce many false negatives and, paradoxically, inflate effect sizes when they do detect effects. Power analysis before data collection is standard practice for well-designed research.

## How It's Best Learned
Given a Cohen's d of .50 and α = .05, use a power table or calculator to find the sample size needed for 80% power. Discuss what happens to false-positive rates when many underpowered studies are conducted.

## Common Misconceptions
- A non-significant result from an underpowered study does not mean there is no effect — it may simply mean the study couldn't detect one.
- Effect sizes are comparable across studies; p-values are not, because they depend on sample size.

## Questions

```yaml
- question: "A study with n = 10,000 finds p = .03 for a difference between two groups. What additional information is most important for evaluating this finding?"
  type: multiple-choice
  options: ["The exact alpha level used", "The effect size (e.g., Cohen's d), because statistical significance does not indicate practical importance", "Whether the result was replicated, since large samples are unusual", "The standard deviation of each group, since p-values don't account for spread"]
  answer: 1
  explanation: "With very large samples, even trivially small differences become statistically significant. A p-value of .03 tells you the result is unlikely under the null, but says nothing about whether the difference is large enough to matter. Effect size (like Cohen's d) standardizes the difference by the spread of scores, making it interpretable regardless of sample size."

- question: "A study fails to find a statistically significant result (p > .05). This means the researchers have demonstrated that no true effect exists."
  type: true-false
  answer: false
  explanation: "A non-significant result from an underpowered study is not evidence of no effect — it may simply mean the study was too small to detect a real but modest effect. 'Absence of evidence is not evidence of absence.' To support a null finding, you need a well-powered study or a Bayesian analysis that quantifies evidence for the null hypothesis."

- question: "Why do underpowered studies that happen to achieve statistical significance tend to overestimate the true effect size?"
  type: short-answer
  answer: "In a low-powered study, only samples that produce an unusually large observed effect will clear the significance threshold. The estimates that get published are therefore a biased, lucky subset — those that happened to overestimate the true effect. This 'winner's curse' means effect sizes from underpowered studies shrink when better-powered replications are run."
  explanation: "This is a statistical consequence of sampling variability combined with a significance filter. The threshold for publication (p < .05) selects for samples at the tail of the sampling distribution, which are precisely the samples that overestimate the effect. Pre-registration and pre-specified power analyses help mitigate this bias."
```

## Explainer

Suppose a study finds that a new therapy reduces anxiety scores by 2 points on a 100-point scale, and this result is statistically significant (p = .01). Should you prescribe the therapy? The p-value tells you the result is unlikely to be a fluke, but it says nothing about whether a 2-point reduction is clinically meaningful. This is the gap that effect size fills.

Effect size measures the *magnitude* of a difference or relationship, independent of how many participants were tested. Cohen's d is the most common measure for comparing two means: it expresses the difference in units of the pooled standard deviation. A d of 0.2 is conventionally small, 0.5 medium, and 0.8 large — though these benchmarks are rough guides, not universal standards. What matters is whether the effect is large enough to be practically important in context. Effect sizes, unlike p-values, are comparable across studies even when sample sizes differ, which makes them the currency of meta-analysis.

Statistical power is the flip side of the same coin. Power is the probability that a study will detect a real effect — that it will return p < .05 when a true effect of a given size exists. Power increases with three things: larger sample sizes (more data = more sensitivity), larger true effect sizes (bigger signals are easier to detect), and more lenient significance thresholds (though raising alpha risks more false positives). The conventional target is 80% power, meaning a 1-in-5 chance of missing a real effect. Most psychological studies prior to the 2010s were severely underpowered, with power estimates often below 50%.

Low power has a pernicious side effect beyond just producing false negatives. When an underpowered study does reach significance, it is often because that particular sample happened to overestimate the true effect. This is the "winner's curse": the effect sizes that survive the significance filter are the lucky, inflated ones. This is why large effects from small studies shrink in replication — the original estimate was atypically large, not representative. Pre-registering a power analysis before data collection constrains researcher degrees of freedom and ensures the study is genuinely equipped to answer its research question.

The practical upshot: always report effect sizes alongside p-values. When reading research, ask whether the study was adequately powered, and treat a non-significant result from a small study as uninformative rather than as evidence of no effect. The replication crisis in psychology was driven in large part by the combination of underpowered designs, flexible analysis practices, and publication bias toward significant results — understanding power and effect size is the foundation for reading that literature critically.
