---
id: reproducibility-in-epidemiology
title: Reproducibility and Replication in Epidemiology
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: meta-analysis-methods
  type: hard
tags:
- causal-inference
- study-quality
- open-science
stage: advanced
status: validated
---

# Reproducibility and Replication in Epidemiology

## Core Idea
Reproducibility—obtaining consistent findings across independent studies—is central to causal inference but is threatened by publication bias, p-hacking, selective reporting, and insufficient statistical power. Large randomized trials provide gold-standard evidence; observational studies with multiple analyses often produce heterogeneous or conflicting results. Meta-analyses aggregate evidence across studies but conflicting conclusions suggest publication bias, true heterogeneity, or chance. Direct replication studies test reproducibility; open science practices (preregistration, data sharing, transparent reporting) improve scientific integrity and allow detection of bias.

## How It's Best Learned
Review sets of epidemiological studies examining the same hypothesis; assess which show consistent findings, identify sources of discrepancy, evaluate study quality.

## Questions

```yaml
- question: "A researcher conducts a meta-analysis pooling 20 observational studies on whether a dietary factor causes cancer. The pooled estimate is statistically significant with very low heterogeneity. A colleague concludes this is strong evidence for a causal relationship. Which concern most directly challenges this conclusion?"
  type: multiple-choice
  options:
    - "Low heterogeneity confirms a true underlying effect, making this a reliable causal inference"
    - "Publication bias may mean the 20 published studies are a biased sample — null and negative results were never published, producing artificial consistency"
    - "Observational studies are ineligible for meta-analysis; only randomized trials can be pooled"
    - "Twenty studies is too few for a valid meta-analysis regardless of heterogeneity"
  answer: 1
  explanation: "Low heterogeneity does not rule out publication bias — it can actually result from it. If only studies finding a significant effect in the same direction were published, the meta-analysis pools a biased, homogeneous sample that overstates the true effect. A rigorous meta-analyst would check for publication bias using funnel plots or Egger's test, and would note that observational evidence — even when pooled — is not sufficient for causal inference without triangulation."

- question: "An initial small study (n=50) reports a large protective effect of a novel supplement (OR=0.5, p=0.04). A large replication trial (n=2,000) finds a small non-significant effect (OR=0.92, p=0.3). Which explanation best captures the 'winner's curse' phenomenon?"
  type: multiple-choice
  options:
    - "The replication trial was underpowered and missed a real protective effect"
    - "The original study used a biased population that responded unusually well to the supplement"
    - "Small underpowered studies can only achieve statistical significance when the effect estimate is inflated by chance; the original's large estimate was partly noise crossing the significance threshold"
    - "The replication trial's null result reflects regression to a different population mean unrelated to study power"
  answer: 2
  explanation: "The winner's curse in science occurs because underpowered studies only detect effects when the estimated effect size is large enough to cross the significance threshold — which happens partly by chance (random noise pushing the estimate up). The original study's OR=0.5 was likely inflated. The larger trial provides a more precise estimate near the true effect size. This systematic inflation of initial findings — not bias in the replication — is what the winner's curse describes."

- question: "Pre-registration of a study's primary outcome and analysis plan before data collection is a key open science practice that makes selective reporting detectable."
  type: true-false
  answer: true
  explanation: "Pre-registration publicly records the hypothesis, study design, and primary outcome before data is collected. This prevents researchers from post-hoc reframing exploratory analyses as confirmatory findings, and makes selective reporting detectable: reviewers can compare the registered protocol against what was actually reported. It changes the information structure of the research process without eliminating false positives — but makes the provenance of findings auditable."

- question: "A meta-analysis that finds consistent results across many studies with low heterogeneity is necessarily unaffected by publication bias."
  type: true-false
  answer: false
  explanation: "Publication bias can produce artificial consistency. If only studies finding a significant effect in the same direction get published, a meta-analysis would pool a biased, homogeneous set, yielding low heterogeneity and a 'consistent' significant result that overstates the true effect. True consistency of results is a positive sign, but it must be distinguished from consistency produced by systematic suppression of null results. Funnel plot asymmetry and registration-based methods can help detect this."

- question: "Why does the 'winner's curse' cause initial study findings to systematically overestimate effect sizes, and what study design feature makes this problem worse?"
  type: short-answer
  answer: "Small, underpowered studies can only achieve statistical significance when their estimated effect size is large enough — which happens partly by chance (sampling variation pushing the estimate up). Only studies whose estimates clear the significance threshold tend to get published, so the published literature is a biased sample skewed toward inflated findings. Smaller sample sizes make the winner's curse worse: with lower power and higher variance, the bar for detection requires a larger (and more likely chance-inflated) estimate. The winner's curse therefore predicts that initial findings from small studies will be followed by smaller, more modest estimates in larger replications."
  explanation: "This is distinct from fraud or p-hacking — the winner's curse is a statistical inevitability when significance-based publication filters operate on underpowered studies. Meta-analyses dominated by small studies are particularly vulnerable because they amplify the bias of each constituent study rather than correcting for it."
```

## Explainer

From your study of meta-analysis, you know how to pool estimates from multiple studies and assess heterogeneity — the degree to which studies give inconsistent results. **Reproducibility** asks the deeper question behind that heterogeneity: when two well-conducted studies examining the same question reach different conclusions, what does that mean? Is the true effect size different across populations? Or are one or both studies producing wrong answers? Reproducibility concerns are fundamentally concerns about the reliability of individual study results, which meta-analysis aggregates but cannot fully compensate for.

**Reproducibility** and **replicability** are related but distinct concepts. Reproducibility (sometimes called computational reproducibility) refers to whether the same data and analysis code, in another researcher's hands, produce the same numerical results. Replicability refers to whether a new independent study — new data, same protocol — produces results consistent with the original. Both matter, but in epidemiology the replication challenge is more fundamental: observational studies cannot be reproduced in the strict sense because exposure patterns in populations change over time, and even "identical" designs in different populations may face different effect modifiers.

The threats to replication are numerous and partially systematic. **Publication bias** — the tendency for statistically significant findings to be published and null findings to be filed away — inflates the apparent effect sizes in the literature and makes the evidence base misleadingly consistent. When you synthesize a body of evidence in meta-analysis, you are implicitly sampling from the published literature, which is a biased sample of all studies conducted. **P-hacking** compounds this: when researchers test multiple outcomes or subgroups and report only those that cross p < 0.05, they manufacture false positives without any conscious intent to deceive. **Selective reporting** — registering one primary outcome and publishing a different one — is a softer version of the same problem.

**Insufficient statistical power** is a subtler threat. Small studies with large variance can detect effects only when the estimated effect is large — which happens partly by chance. When a small, underpowered study finds a large effect and a large replication trial finds a small one, the discrepancy reflects regression to the mean: the original study's large estimate was partly noise, not signal. This is the "winner's curse" in science: initial findings are often inflated because only the largest estimates clear the significance threshold in underpowered designs. Meta-analyses dominated by small studies are particularly vulnerable to this distortion.

**Open science practices** address these threats by changing the information structure of the research process. **Pre-registration** — publicly recording the hypothesis, design, and primary outcome before data collection — prevents post-hoc reframing of exploratory analyses as confirmatory ones and makes selective reporting detectable. **Data sharing** enables other researchers to check analyses, test alternative specifications, and run independent analyses. **Transparent reporting standards** (STROBE for observational studies, CONSORT for trials) ensure that readers can evaluate study quality without relying on the authors' self-assessment. None of these practices eliminate false positives, but they make the provenance of findings auditable, which is the minimum condition for science to self-correct. Epidemiology's credibility as a discipline depends not just on any single study's quality, but on whether the accumulated body of evidence can be trusted as a representative sample of what is true.
