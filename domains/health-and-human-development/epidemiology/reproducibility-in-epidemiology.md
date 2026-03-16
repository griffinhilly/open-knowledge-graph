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
status: draft
---

# Reproducibility and Replication in Epidemiology

## Core Idea
Reproducibility—obtaining consistent findings across independent studies—is central to causal inference but is threatened by publication bias, p-hacking, selective reporting, and insufficient statistical power. Large randomized trials provide gold-standard evidence; observational studies with multiple analyses often produce heterogeneous or conflicting results. Meta-analyses aggregate evidence across studies but conflicting conclusions suggest publication bias, true heterogeneity, or chance. Direct replication studies test reproducibility; open science practices (preregistration, data sharing, transparent reporting) improve scientific integrity and allow detection of bias.

## How It's Best Learned
Review sets of epidemiological studies examining the same hypothesis; assess which show consistent findings, identify sources of discrepancy, evaluate study quality.

## Explainer

From your study of meta-analysis, you know how to pool estimates from multiple studies and assess heterogeneity — the degree to which studies give inconsistent results. **Reproducibility** asks the deeper question behind that heterogeneity: when two well-conducted studies examining the same question reach different conclusions, what does that mean? Is the true effect size different across populations? Or are one or both studies producing wrong answers? Reproducibility concerns are fundamentally concerns about the reliability of individual study results, which meta-analysis aggregates but cannot fully compensate for.

**Reproducibility** and **replicability** are related but distinct concepts. Reproducibility (sometimes called computational reproducibility) refers to whether the same data and analysis code, in another researcher's hands, produce the same numerical results. Replicability refers to whether a new independent study — new data, same protocol — produces results consistent with the original. Both matter, but in epidemiology the replication challenge is more fundamental: observational studies cannot be reproduced in the strict sense because exposure patterns in populations change over time, and even "identical" designs in different populations may face different effect modifiers.

The threats to replication are numerous and partially systematic. **Publication bias** — the tendency for statistically significant findings to be published and null findings to be filed away — inflates the apparent effect sizes in the literature and makes the evidence base misleadingly consistent. When you synthesize a body of evidence in meta-analysis, you are implicitly sampling from the published literature, which is a biased sample of all studies conducted. **P-hacking** compounds this: when researchers test multiple outcomes or subgroups and report only those that cross p < 0.05, they manufacture false positives without any conscious intent to deceive. **Selective reporting** — registering one primary outcome and publishing a different one — is a softer version of the same problem.

**Insufficient statistical power** is a subtler threat. Small studies with large variance can detect effects only when the estimated effect is large — which happens partly by chance. When a small, underpowered study finds a large effect and a large replication trial finds a small one, the discrepancy reflects regression to the mean: the original study's large estimate was partly noise, not signal. This is the "winner's curse" in science: initial findings are often inflated because only the largest estimates clear the significance threshold in underpowered designs. Meta-analyses dominated by small studies are particularly vulnerable to this distortion.

**Open science practices** address these threats by changing the information structure of the research process. **Pre-registration** — publicly recording the hypothesis, design, and primary outcome before data collection — prevents post-hoc reframing of exploratory analyses as confirmatory ones and makes selective reporting detectable. **Data sharing** enables other researchers to check analyses, test alternative specifications, and run independent analyses. **Transparent reporting standards** (STROBE for observational studies, CONSORT for trials) ensure that readers can evaluate study quality without relying on the authors' self-assessment. None of these practices eliminate false positives, but they make the provenance of findings auditable, which is the minimum condition for science to self-correct. Epidemiology's credibility as a discipline depends not just on any single study's quality, but on whether the accumulated body of evidence can be trusted as a representative sample of what is true.
