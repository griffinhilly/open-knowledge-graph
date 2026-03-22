---
id: replication-and-open-science
title: Replication and the Open Science Movement
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
- id: effect-size-and-power
  type: soft
- id: validity-in-measurement
  type: soft
- id: scientific-method-psychology
  type: soft
tags:
- replication
- replication-crisis
- open-science
- preregistration
- publication-bias
stage: formal-systems
status: validated
---

# Replication and the Open Science Movement

## Core Idea
Replication — repeating a study to see if findings hold — is foundational to science, yet psychology's 'replication crisis' revealed that many published findings fail to replicate reliably. Contributing factors include publication bias (journals favoring positive results), p-hacking (testing many analyses until p < .05), and low statistical power. The Open Science movement responds with preregistration (registering hypotheses before data collection), open data sharing, and registered reports. Meta-analysis — quantitatively synthesizing many studies — provides more reliable effect estimates than any single study.

## How It's Best Learned
Read the Reproducibility Project (OSC, 2015) summary and identify what percentage of studies replicated. Discuss what structural incentives in academia contribute to the problem and which reforms address each incentive.

## Common Misconceptions
- A failure to replicate does not always mean the original finding was wrong — differences in samples, contexts, or operationalizations can produce genuine moderating effects.
- Preregistration does not prevent exploratory analyses; it distinguishes confirmatory from exploratory analyses so readers can calibrate their confidence accordingly.

## Questions

```yaml
- question: "A researcher runs 20 different analyses on their dataset, finds one with p = .03, and reports it as their primary finding without mentioning the other 19. The most accurate description of this practice is:"
  type: multiple-choice
  options:
    - "Scientific fraud, because the researcher deliberately hid negative results"
    - "P-hacking, because researcher degrees of freedom inflated the false-positive rate beyond the nominal 5%"
    - "Acceptable exploratory analysis, since the finding is still statistically significant"
    - "Publication bias, because the journal only accepts positive results"
  answer: 1
  explanation: "This is p-hacking (researcher degrees of freedom): making many analytic decisions while looking at the data systematically inflates the chance of finding p < .05 by chance. It's distinct from fraud — the researcher may not even be aware they're doing it. Publication bias refers to journal-level filtering, not researcher-level analysis choices. A finding produced this way cannot be interpreted at face value as a 5% false-positive rate."

- question: "A researcher preregisters their study and then collects data. After looking at the results, they notice an interesting pattern not in their original plan. What does preregistration allow them to do?"
  type: multiple-choice
  options:
    - "Nothing — preregistration legally prohibits any unplanned analyses"
    - "Run the exploratory analysis but label it as exploratory, so readers can calibrate their confidence"
    - "Discard the preregistered hypotheses if the exploratory finding is more interesting"
    - "Publish the exploratory finding as confirmatory since it came from the same dataset"
  answer: 1
  explanation: "Preregistration distinguishes confirmatory from exploratory analyses — it does not eliminate exploratory work. Researchers can and should report unexpected patterns, but labeling them as exploratory signals to readers that these findings require independent replication before being treated as established. Presenting exploratory findings as confirmatory is exactly what preregistration is designed to prevent."

- question: "A replication study fails to reproduce the original finding. This proves the original study's results were false."
  type: true-false
  answer: false
  explanation: "Failure to replicate does not automatically mean the original was wrong. Differences in sample characteristics, cultural context, operationalizations of variables, or time period can produce genuine moderating effects — the original finding may be real but context-dependent. Replication failures are important evidence that demands explanation, but the correct response is to investigate why, not to conclude the original was fabricated or simply wrong."

- question: "Publication bias can distort a scientific literature even when every individual researcher behaves honestly and no data manipulation occurs."
  type: true-false
  answer: true
  explanation: "Publication bias is a systemic, structural phenomenon. When journals preferentially accept positive results and researchers preferentially submit them, the published record ends up skewed — not because anyone cheated, but because thousands of honest individual decisions collectively filter out negative and null findings. The result is a literature that overstates effect sizes and effect prevalence. This is why the Open Science movement focuses on structural reforms (registered reports, preregistration) rather than just policing individual conduct."

- question: "Why do small, underpowered studies that achieve statistical significance tend to overestimate effect sizes — a phenomenon sometimes called the 'winner's curse'?"
  type: short-answer
  answer: "In an underpowered study, only the largest-by-chance results will clear the significance threshold. If the true effect is small and the sample is small, most runs of the study will produce non-significant results. The rare runs that do achieve significance are those where sampling error happened to inflate the estimated effect. This means the subset of underpowered studies that get published (because they're significant) are selected for having inflated estimates — creating a systematic overestimation in the published literature."
  explanation: "This is why average effect sizes in the Reproducibility Project replications were roughly half those in the originals. The originals were often underpowered, and the published results were filtered for significance, selecting for overestimates. Larger, well-powered replications regress toward the true (smaller) effect size. The winner's curse is a direct consequence of combining publication bias with low power."
```

## Explainer

Your training in inferential statistics gave you the mathematical framework for p-values and significance thresholds. Now consider what happens when that framework meets the real incentive structure of academic publishing. A single study with p < .05 is publishable — interesting, novel, confirms a theory. A replication attempt that fails to find the same effect is not interesting to most journals — it goes in the file drawer. The result of thousands of researchers making thousands of independent decisions about what to submit, and thousands of editors making thousands of decisions about what to accept, is a published literature that is systematically skewed toward positive results. This is **publication bias**, and it corrupts the knowledge base even when every individual researcher is acting honestly.

The 2015 Reproducibility Project (Open Science Collaboration) made the scale of the problem concrete: a team of researchers attempted to replicate 100 studies from top psychology journals and found that only about 36-39% produced statistically significant results matching the original. Average effect sizes in the replications were roughly half those in the originals. This is the **replication crisis**. Understanding *why* this happened requires connecting two concepts from your inferential statistics training. First, **underpowered studies** — designed with samples too small to reliably detect realistic effect sizes — produce high false-negative rates, but when they do find effects, those effects are likely overestimates (the "winner's curse": only the largest-by-chance results clear the significance threshold in small samples). Second, **p-hacking** — also called "researcher degrees of freedom" — exploits the fact that researchers make many analytic decisions (when to stop collecting data, which covariates to include, how to handle outliers) that each slightly affect the p-value. When these decisions are made while looking at the data and are reported selectively, p < .05 becomes much easier to achieve than it should be.

The **Open Science movement** addresses these structural problems with a set of reforms that change what gets recorded before the data are collected and what gets shared afterward. **Preregistration** requires researchers to specify their hypotheses, sample size, primary outcomes, and analysis plan in a time-stamped public record before collecting data. This eliminates the most serious form of p-hacking, because deviations from the plan are visible. A stronger variant, the **registered report**, gets the preregistered design peer-reviewed and accepted for publication *before* data collection, with the journal committing to publish the results regardless of outcome. This directly attacks publication bias by decoupling the publication decision from whether the results are positive. **Open data** and **open materials** sharing allow independent researchers to verify analyses and attempt methodologically faithful replications without having to reconstruct everything from scratch.

It would be a mistake to interpret the replication crisis as evidence that psychological science is worthless or that individual findings cannot be trusted. The more precise lesson is that single studies — especially small ones in competitive research areas — should be treated as preliminary evidence, not established facts. **Meta-analysis**, which quantitatively synthesizes effect sizes across many studies using weighting procedures that account for sample size, provides more stable estimates than any individual study. The replication crisis has, ultimately, been productive: it has produced a generation of methodologically sophisticated researchers, a more skeptical reading culture, and a set of institutional reforms that, when adopted, genuinely increase the credibility of published findings.
