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
stage: abstract-reasoning
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

## Explainer

Your training in inferential statistics gave you the mathematical framework for p-values and significance thresholds. Now consider what happens when that framework meets the real incentive structure of academic publishing. A single study with p < .05 is publishable — interesting, novel, confirms a theory. A replication attempt that fails to find the same effect is not interesting to most journals — it goes in the file drawer. The result of thousands of researchers making thousands of independent decisions about what to submit, and thousands of editors making thousands of decisions about what to accept, is a published literature that is systematically skewed toward positive results. This is **publication bias**, and it corrupts the knowledge base even when every individual researcher is acting honestly.

The 2015 Reproducibility Project (Open Science Collaboration) made the scale of the problem concrete: a team of researchers attempted to replicate 100 studies from top psychology journals and found that only about 36-39% produced statistically significant results matching the original. Average effect sizes in the replications were roughly half those in the originals. This is the **replication crisis**. Understanding *why* this happened requires connecting two concepts from your inferential statistics training. First, **underpowered studies** — designed with samples too small to reliably detect realistic effect sizes — produce high false-negative rates, but when they do find effects, those effects are likely overestimates (the "winner's curse": only the largest-by-chance results clear the significance threshold in small samples). Second, **p-hacking** — also called "researcher degrees of freedom" — exploits the fact that researchers make many analytic decisions (when to stop collecting data, which covariates to include, how to handle outliers) that each slightly affect the p-value. When these decisions are made while looking at the data and are reported selectively, p < .05 becomes much easier to achieve than it should be.

The **Open Science movement** addresses these structural problems with a set of reforms that change what gets recorded before the data are collected and what gets shared afterward. **Preregistration** requires researchers to specify their hypotheses, sample size, primary outcomes, and analysis plan in a time-stamped public record before collecting data. This eliminates the most serious form of p-hacking, because deviations from the plan are visible. A stronger variant, the **registered report**, gets the preregistered design peer-reviewed and accepted for publication *before* data collection, with the journal committing to publish the results regardless of outcome. This directly attacks publication bias by decoupling the publication decision from whether the results are positive. **Open data** and **open materials** sharing allow independent researchers to verify analyses and attempt methodologically faithful replications without having to reconstruct everything from scratch.

It would be a mistake to interpret the replication crisis as evidence that psychological science is worthless or that individual findings cannot be trusted. The more precise lesson is that single studies — especially small ones in competitive research areas — should be treated as preliminary evidence, not established facts. **Meta-analysis**, which quantitatively synthesizes effect sizes across many studies using weighting procedures that account for sample size, provides more stable estimates than any individual study. The replication crisis has, ultimately, been productive: it has produced a generation of methodologically sophisticated researchers, a more skeptical reading culture, and a set of institutional reforms that, when adopted, genuinely increase the credibility of published findings.
