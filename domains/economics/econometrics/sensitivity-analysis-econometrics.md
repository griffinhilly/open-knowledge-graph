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
status: validated
---

# Sensitivity Analysis and Robustness Checks

## Core Idea
Sensitivity analysis examines whether estimates remain robust to alternative assumptions, functional forms, samples, or control variables. It provides evidence of how sensitive conclusions are to modeling choices.

## Questions

```yaml
- question: "A researcher estimates a job training program's effect on earnings: no controls gives +$2,000; with demographic controls +$1,900; with economic controls +$1,800; with all controls +$1,750. What does this pattern indicate about the result?"
  type: multiple-choice
  options:
    - "The estimate is fragile — each additional control reduces it, revealing severe omitted variable bias"
    - "The estimate is robust — it moves within a small, consistent range across plausible specifications, supporting the conclusion"
    - "The researcher should report only the no-controls estimate since it shows the largest, most significant effect"
    - "Adding controls always mechanically reduces estimates; no conclusion about robustness can be drawn"
  answer: 1
  explanation: "A 'stable path' of estimates across reasonable specifications is the evidence sensitivity analysis is designed to produce. Moving from $2,000 to $1,750 across four specifications — all in the same direction, never near zero — is strong evidence the result doesn't depend on any single modeling choice. A fragile result would be one that crosses zero or changes sign with a minor adjustment. Option A misreads the pattern: a small, consistent decline with additional controls suggests mild selection bias that controls are correctly adjusting for, not fragility."

- question: "After completing her analysis, a researcher runs 40 different model specifications and reports only the 3 that show statistically significant results. What is this practice called, and why is it problematic?"
  type: multiple-choice
  options:
    - "Robustness checking — reporting the most significant results demonstrates the estimates hold up"
    - "Specification searching — it inflates false discovery rates and misrepresents the true evidential weight of the results"
    - "Sensitivity analysis — systematically varying specifications and selecting the clearest is exactly the point"
    - "Bootstrap inference — randomly sampling from 40 specifications approximates a bootstrap distribution"
  answer: 1
  explanation: "Running many specifications and reporting only the significant ones is specification searching (sometimes called 'p-hacking'). With 40 specifications, you would expect roughly 2 to show p < 0.05 by chance even under the null. Selectively reporting those 3 creates the appearance of evidence that doesn't exist. Sensitivity analysis is the *opposite*: it requires reporting all results across a pre-specified or transparent grid of choices, including those that do not support the hypothesis. The distinction between searching and analysis is transparency and pre-commitment."

- question: "Sensitivity analysis and bootstrap inference both measure the same dimension of uncertainty in an econometric estimate."
  type: true-false
  answer: false
  explanation: "They measure fundamentally different dimensions. Bootstrap inference quantifies sampling variability — how much estimates would vary if you drew a different sample from the same population. Sensitivity analysis quantifies specification variability — how much estimates move when you change modeling choices (controls, functional form, sample restrictions) while keeping the same data. A result can be robust to sampling noise (tight bootstrap CIs) but fragile to specification changes, or vice versa. A credible empirical paper needs both."

- question: "An estimate that changes dramatically when a single control variable is added or removed provides weaker causal evidence than one that remains stable across many plausible specifications."
  type: true-false
  answer: true
  explanation: "If a treatment effect estimate swings from economically significant to near-zero upon inclusion of one variable, the conclusion was 'hanging on' the exclusion of that variable. This suggests either strong confounding — the omitted variable was capturing much of the true variation — or model instability. Stable estimates across a range of reasonable specifications mean the conclusion does not depend on any particular modeling choice, which is what we want from credible causal inference."

- question: "What is the key difference between sensitivity analysis and formal specification testing (e.g., Hausman tests, RESET tests), and why does sensitivity analysis provide information those tests cannot?"
  type: short-answer
  answer: "Formal specification tests compare a base model to one specific alternative — they answer 'is this particular alternative model statistically distinguishable from mine?' They produce a binary pass/fail for that one comparison. Sensitivity analysis instead varies a *range* of modeling choices (different control sets, functional forms, sample restrictions) and tracks the path of estimates across that space. It answers 'does my conclusion hold across the neighborhood of reasonable models?' Formal tests cannot evaluate the full space of plausible specifications; sensitivity analysis can show whether any specification within that space would overturn the conclusion."
  explanation: "The additional value is that sensitivity analysis guards against a specific failure mode: a researcher who passes all formal tests but happened to choose the one specification where results are strongest. Formal tests would not detect this. Sensitivity analysis, done transparently across a pre-committed grid, makes that cherry-picking impossible — the full path of estimates is disclosed."
```

## Explainer

Every econometric estimate you produce is conditional on dozens of choices you made along the way: which control variables to include, what functional form to assume, how to handle outliers, which sample restriction to apply, what standard error correction to use. From specification testing you know how to formally test some of those choices. But formal tests only tell you whether a specific alternative model fits the data better — they cannot tell you whether your conclusions survive the full range of reasonable modeling decisions. **Sensitivity analysis** is the practice of deliberately varying those choices and observing whether your estimates remain stable.

The most common form is **coefficient stability analysis**: estimate your key coefficient under a sequence of specifications, progressively adding or removing control variables, and examine the path of estimates and confidence intervals. If your treatment effect estimate is 0.4 with no controls, 0.38 with demographic controls, 0.35 with further economic controls, and never moves outside [0.2, 0.5] across any reasonable specification, that stability is strong evidence the result is not an artifact of a particular specification choice. Conversely, if adding a single control variable moves the estimate from 0.4 to 0.02 and removes significance, the conclusion was fragile — hanging on the exclusion of that variable — and you should investigate why. The **Oster (2019)** approach formalizes this by bounding the treatment effect under proportional selection assumptions, asking: how much selection on unobservables relative to observables would be required to drive the effect to zero?

**Sample robustness checks** ask whether the result holds for plausible subsamples: dropping extreme observations, restricting to a cleaner part of the distribution, splitting by time period or demographic group. These serve two purposes. First, they diagnose whether results are driven by a small influential subset rather than the broad pattern in the data. Second, they address external validity — does the effect hold across different subpopulations? **Functional form robustness** involves comparing linear models to log specifications, quadratic terms, or nonparametric alternatives like local linear regression, checking whether nonlinearity in the underlying relationship is distorting your estimates.

The bootstrap inference techniques you have already studied are closely connected: the bootstrap quantifies sampling variability, but sensitivity analysis quantifies **specification variability** — how much your estimate moves when you vary the model rather than the sample. Together they give a fuller picture of uncertainty than a single confidence interval. A credible empirical paper presents sensitivity analysis not as an afterthought but as a core component of the argument: the reader needs to know not just that *this particular* model produced *this estimate*, but that estimates in a defensible neighborhood of specifications consistently support the same conclusion. The failure mode to avoid is **specification searching** — running many specifications and reporting only the most favorable one, which is a form of pre-analysis dishonesty. Sensitivity analysis should be pre-committed or conducted transparently across a pre-specified grid of choices.
