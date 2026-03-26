---
id: publication-bias-drawer-problem
title: Publication Bias and the File Drawer Problem
domain: psychology
course: research-methods-psychology
prerequisites:
- id: replication-and-open-science
  type: soft
- id: experimenter-bias-and-expectancy-effects
  type: soft
tags:
- bias
- publication
- meta-science
stage: formal-systems
status: validated
---
# Publication Bias and the File Drawer Problem

## Core Idea
Studies with statistically significant results are more likely to be published than null-result studies, creating systematic bias in the scientific literature. This publication bias means meta-analyses and literature reviews based on published studies substantially overestimate population effect sizes. Preregistration, open data policies, and journals publishing null results are partial remedies to improve research integrity.

## Questions

```yaml
- question: "One hundred independent research teams each test whether Supplement X improves memory. The supplement has absolutely no real effect. Each team uses α = 0.05. Approximately how many teams would you expect to find a statistically significant result?"
  type: multiple-choice
  options:
    - "Zero — if the supplement truly has no effect, properly conducted studies will always show no effect"
    - "About 5 teams, purely by chance due to the 5% false positive rate"
    - "About 50 teams, since statistical significance is roughly a coin flip"
    - "It cannot be estimated without knowing the sample sizes used"
  answer: 1
  explanation: "At α = 0.05, each study has a 5% probability of a false positive — finding a significant result even when the true effect is zero. With 100 independent studies, you expect approximately 100 × 0.05 = 5 false positives. If only those 5 get published and the other 95 null results go into file drawers, the literature appears to support a real effect with five independent replications. This is the mechanical origin of publication bias — not fraud, just the selective presentation of a predictable statistical artifact."

- question: "A meta-analysis synthesizes 20 published studies on a new therapeutic intervention and estimates a medium effect size (d = 0.50). A funnel plot shows significant asymmetry — the lower-left region (small studies with small effects) is notably absent. The most likely interpretation is:"
  type: multiple-choice
  options:
    - "The effect is definitively real; funnel asymmetry confirms that statistical power was sufficient across studies"
    - "The effect size estimate is inflated because small null-result studies were not published, biasing the meta-analytic average upward"
    - "The included studies used different methodologies, making meta-analysis inappropriate regardless of funnel shape"
    - "The heterogeneity proves the effect varies meaningfully across subpopulations"
  answer: 1
  explanation: "Funnel plot asymmetry — specifically the absence of small studies with non-significant or small effects — is the classic signature of publication bias. Small studies with null results went into file drawers; the surviving studies skew positive. The meta-analytic estimate inherits this bias, inflating the apparent effect. The true effect could be much smaller or zero. Funnel plot tests (Egger's test, trim-and-fill) can partially correct for this, but they estimate what's missing rather than directly accessing unpublished data."

- question: "A preregistered study that finds a null result is just as scientifically informative as one that finds a statistically significant effect."
  type: true-false
  answer: true
  explanation: "Null results narrow the parameter space of plausible effects — they rule out effect sizes above a certain magnitude. They are essential for accurate estimation of true population effects and prevent false beliefs from accumulating. The publication bias against null results is a structural preference of journals and authors, not a reflection of scientific value. Preregistration makes null results visible by creating a traceable record of all studies launched, independent of outcome, allowing the scientific community to see what was actually found rather than just what was published."

- question: "Publication bias can be fully corrected by conducting meta-analyses, since averaging across most available studies cancels out the individual-study bias."
  type: true-false
  answer: false
  explanation: "Meta-analyses that synthesize only published studies inherit the same publication bias — they average a biased sample. If the available studies are systematically selected for significant positive outcomes, the meta-analytic effect size estimate will be inflated. Statistical corrections like trim-and-fill or PET-PEESE can partially compensate by estimating what might be missing, but they do not recover the actual unpublished data. The bias must be addressed upstream (through preregistration, registered reports, and null-result journals) rather than corrected after the fact."

- question: "Explain how a scientific literature can systematically mislead researchers about the true magnitude of an effect even when every individual study in that literature was conducted and reported honestly."
  type: short-answer
  answer: "Selective publication creates bias at the level of the literature rather than the individual study. Each individual study may be conducted and reported with complete integrity — but if journals and authors systematically publish significant positive findings while abandoning null results, the published record is a biased sample of all research conducted. By the mathematics of false positive rates, this sample overrepresents positive outcomes even when the true effect is small or zero. Rosenthal's file drawer calculation makes this concrete: if 95 null-result studies are hidden and 5 chance-significant studies are published, the literature appears to robustly support a real effect. The distortion is systemic, not individual."
  explanation: "This is the conceptual heart of publication bias. Students who think 'each study was honest, so the literature is reliable' have missed the key insight: systemic selection bias can emerge from individually honest behavior. Understanding this explains why preregistration and registered reports are structural reforms, not just ethical norms."
```

## Explainer

From your study of replication and open science, you know that the replication crisis revealed widespread problems with the reliability of published psychological findings. Publication bias is the single most important structural explanation for why the crisis occurred. The mechanism is straightforward: journals, reviewers, and authors all favor statistically significant results. Studies that find effects get published; studies that find nothing tend to get abandoned in a file drawer or on a hard drive. Over time, the published literature accumulates a biased sample of research outcomes — a sample that systematically overrepresents positive findings.

**Rosenthal's file drawer problem** puts a precise face on the distortion. Imagine 100 research teams independently test the same hypothesis. By chance alone, approximately 5 of them will find a statistically significant result (p < .05) even if the hypothesis is false — that's what "5% false positive rate" means. If those 5 studies get published and the other 95 end up in file drawers, the literature appears to support a real effect with perfectly reasonable-looking statistics. The published record is not lying, exactly — each individual study was conducted and reported honestly — but the selective presentation of the 5 successes while hiding the 95 failures creates a systematically false impression.

The consequences compound when researchers conduct **meta-analyses** — quantitative syntheses of published studies. If the input studies are already biased toward significant positive results, the meta-analytic estimate of effect size will be inflated, sometimes dramatically. This is how findings with true population effect sizes near zero can accumulate a literature showing moderate effects. Several funnel plot methods (like Egger's test or trim-and-fill) attempt to detect and correct for this, but they are imperfect — they can only estimate what might be missing from the file drawer, not directly access it.

**Preregistration** addresses the problem at its root. By requiring researchers to publicly commit their hypotheses, sample sizes, and analysis plans before data collection, preregistration makes it possible to distinguish confirmatory hypothesis tests from exploratory analyses, and creates a traceable record of all studies launched — making it harder to simply bury null results. Registered Reports, a journal format where peer review and acceptance decisions happen before data are collected, go even further by making publication contingent on study quality rather than outcome. These reforms do not eliminate publication bias, but they substantially reduce the structural incentives that produce it, which is why open science advocates consider preregistration one of the most important methodological reforms in contemporary psychology.
