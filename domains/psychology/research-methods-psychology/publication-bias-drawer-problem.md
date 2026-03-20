---
id: publication-bias-drawer-problem
title: Publication Bias and the File Drawer Problem
domain: psychology
course: research-methods-psychology
prerequisites:
- id: replication-and-open-science
  type: soft
tags:
- bias
- publication
- meta-science
stage: formal-systems
status: draft
---

# Publication Bias and the File Drawer Problem

## Core Idea
Studies with statistically significant results are more likely to be published than null-result studies, creating systematic bias in the scientific literature. This publication bias means meta-analyses and literature reviews based on published studies substantially overestimate population effect sizes. Preregistration, open data policies, and journals publishing null results are partial remedies to improve research integrity.

## Explainer

From your study of replication and open science, you know that the replication crisis revealed widespread problems with the reliability of published psychological findings. Publication bias is the single most important structural explanation for why the crisis occurred. The mechanism is straightforward: journals, reviewers, and authors all favor statistically significant results. Studies that find effects get published; studies that find nothing tend to get abandoned in a file drawer or on a hard drive. Over time, the published literature accumulates a biased sample of research outcomes — a sample that systematically overrepresents positive findings.

**Rosenthal's file drawer problem** puts a precise face on the distortion. Imagine 100 research teams independently test the same hypothesis. By chance alone, approximately 5 of them will find a statistically significant result (p < .05) even if the hypothesis is false — that's what "5% false positive rate" means. If those 5 studies get published and the other 95 end up in file drawers, the literature appears to support a real effect with perfectly reasonable-looking statistics. The published record is not lying, exactly — each individual study was conducted and reported honestly — but the selective presentation of the 5 successes while hiding the 95 failures creates a systematically false impression.

The consequences compound when researchers conduct **meta-analyses** — quantitative syntheses of published studies. If the input studies are already biased toward significant positive results, the meta-analytic estimate of effect size will be inflated, sometimes dramatically. This is how findings with true population effect sizes near zero can accumulate a literature showing moderate effects. Several funnel plot methods (like Egger's test or trim-and-fill) attempt to detect and correct for this, but they are imperfect — they can only estimate what might be missing from the file drawer, not directly access it.

**Preregistration** addresses the problem at its root. By requiring researchers to publicly commit their hypotheses, sample sizes, and analysis plans before data collection, preregistration makes it possible to distinguish confirmatory hypothesis tests from exploratory analyses, and creates a traceable record of all studies launched — making it harder to simply bury null results. Registered Reports, a journal format where peer review and acceptance decisions happen before data are collected, go even further by making publication contingent on study quality rather than outcome. These reforms do not eliminate publication bias, but they substantially reduce the structural incentives that produce it, which is why open science advocates consider preregistration one of the most important methodological reforms in contemporary psychology.
