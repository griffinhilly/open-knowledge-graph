---
id: analysis-plan-preregistration-commitment
title: Analysis Planning and Preregistration of Hypotheses
domain: psychology
course: research-methods-psychology
prerequisites:
- id: psychological-research-ethics
  type: soft
- id: research-question-formulation-specificity
  type: soft
builds-toward:
- publication-bias-drawer-problem
tags:
- integrity
- transparency
- preregistration
stage: abstract-reasoning
status: draft
---

# Analysis Planning and Preregistration of Hypotheses

## Core Idea
Preregistration involves publicly specifying hypotheses, variables, design, and analytical approach before data collection, creating accountability and distinguishing confirmatory hypothesis tests from exploratory post-hoc analyses. Preregistration reduces researcher degrees of freedom (p-hacking) while enabling transparent exploration properly labeled as such. This practice improves reproducibility and protects against selective reporting.

## Questions

```yaml
- question: "A researcher collects data, then tries 20 different combinations of exclusion criteria, covariates, and outcome measures until finding p < 0.05. This is problematic primarily because:"
  type: multiple-choice
  options:
    - "Using multiple analysis methods is always a violation of APA ethical guidelines"
    - "The p-value's meaning as a false positive rate assumes the analysis was prespecified; selecting the best result from many alternatives inflates the true false positive rate far above 5%"
    - "The study should have collected more data before running any analyses"
    - "Researchers must use identical methods to those used in prior studies on the same topic"
  answer: 1
  explanation: "The p < 0.05 threshold is meaningful only when the test was specified in advance. When a researcher searches through analytic space and reports the most favorable result, the probability of obtaining p < 0.05 by chance is far higher than 5% — the nominal error rate collapses. This is the structural problem (researcher degrees of freedom / p-hacking) that preregistration addresses, regardless of whether the researcher did it intentionally."

- question: "A preregistered study finds a statistically significant relationship that was not included in the analysis plan. The correct course of action is:"
  type: multiple-choice
  options:
    - "Report it as a confirmed finding since it was statistically significant"
    - "Discard the finding entirely since it wasn't preregistered"
    - "Report it as exploratory or hypothesis-generating, noting it requires a future confirmatory study"
    - "Add it to the preregistration retroactively before publishing to maintain transparency"
  answer: 2
  explanation: "Preregistration does not prohibit exploration — it requires that exploration be labeled as such. An unexpected finding is genuinely interesting and worth reporting, but it counts as a hypothesis to be confirmed, not as established knowledge. Only a future study that preregisters this finding as its primary hypothesis can provide confirmatory evidence. Discarding it entirely would waste valuable information; calling it confirmed would repeat the original problem."

- question: "Preregistration prevents researchers from conducting any analyses beyond what was specified in the preregistration document."
  type: true-false
  answer: false
  explanation: "This is a common misunderstanding. Preregistration does NOT prohibit exploratory analyses — it requires that they be clearly distinguished from confirmatory ones. Curiosity and hypothesis generation are essential to science; the problem was never exploration itself, but presenting exploratory findings as confirmatory hypothesis tests with their associated error-rate interpretations. A preregistered study can and should report unexpected findings, clearly labeled as exploratory."

- question: "A researcher who unconsciously p-hacks — making analytic choices without realizing they are being influenced by how those choices affect results — is still inflating the false positive rate."
  type: true-false
  answer: true
  explanation: "Researcher degrees of freedom inflate false positive rates whether or not the researcher is aware of the bias. The problem is structural, not motivational. Analytic choices like 'this outlier looks like a data entry error' or 'this covariate improves model fit' often seem locally justified, but when they are consistently made in the direction of better results, the cumulative effect is the same as deliberate p-hacking. This is why structural solutions like preregistration are more effective than appeals to researcher conscientiousness."

- question: "Why does preregistration make a p-value more interpretable, even when the data and statistical methods are identical to an unregistered study?"
  type: short-answer
  answer: "The p-value's interpretation as a false positive rate (e.g., 5% chance of rejecting a true null at alpha = 0.05) holds only when the analysis was specified before seeing the data. Preregistration creates a timestamped record verifying this commitment. Without preregistration, a reported p < 0.05 may be the best result from dozens of analytic alternatives, in which case the actual false positive rate is far higher than 5%. Preregistration restores the statistical guarantee by ensuring the test was a genuine prospective prediction, not retrospective pattern-matching."
  explanation: "This is the mathematical heart of why preregistration matters. The frequentist guarantee — 'if the null is true, we'll reject it only 5% of the time' — applies to a single prespecified test. When researchers perform many tests and report the most favorable, the math breaks down. Preregistration doesn't change the data or the methods; it changes whether the reported p-value means what it claims to mean."
```

## Explainer

Your background in research ethics and research question formulation establishes what good research is supposed to be: a transparent test of a specific prediction. Preregistration is the mechanism that enforces that standard at the moment it is most vulnerable — when the researcher sits down with data and has countless small decisions to make.

The core problem is **researcher degrees of freedom**: the large number of legitimate-looking analytic choices that face a researcher after data are collected. Which participants to exclude? Which covariates to include? Which of several outcome measures to report as primary? Should you transform that skewed variable? When should you stop collecting data? Each choice seems defensible in isolation. But when every choice is made after observing how it affects the results — consciously or not — the researcher is no longer testing a hypothesis. They are searching the data for a pattern and then reporting it as if it were predicted. This process, known as **p-hacking**, inflates false positive rates far above the nominal 5% level. The replication crisis in psychology was in large part a consequence of widespread, often unconscious, researcher degrees of freedom.

**Preregistration** closes this loophole by requiring researchers to commit publicly — before data collection — to their hypotheses, primary variables, sample size, exclusion criteria, and analysis plan. The commitment is filed on a registry such as OSF (Open Science Framework), timestamped, and retrievable. When a paper is later published, readers and reviewers can inspect what was predicted in advance. Analyses that match the preregistered plan are **confirmatory**: they constitute a genuine hypothesis test with interpretable error rates. Analyses that deviate from or go beyond the plan are **exploratory**: they generate hypotheses for future study but do not confirm them.

The key clarification is that preregistration does not prohibit exploration — it requires that exploration be *labeled* as such. Curiosity and hypothesis generation are essential to science; the problem was never exploration itself, but presenting exploratory findings as confirmatory. A preregistered study that finds something unexpected in an unplanned analysis has discovered something interesting and worth pursuing — but that finding requires its own confirmatory test before it counts as established knowledge.
