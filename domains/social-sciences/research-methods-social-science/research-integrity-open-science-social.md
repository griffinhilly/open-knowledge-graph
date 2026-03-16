---
id: research-integrity-open-science-social
title: 'Research Integrity and Open Science: Transparency and Reproducibility'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-ethics-human-subjects
  type: soft
tags:
- research-integrity
- open-science
- reproducibility
- preregistration
stage: advanced
status: draft
---

# Research Integrity and Open Science: Transparency and Reproducibility

## Core Idea
Research integrity requires transparency about methods, data, and decisions. Open science practices—preregistration, data sharing, code availability—reduce researcher degrees of freedom and enable replication. Social science faces a reproducibility challenge; transparency improves reliability.

## Explainer

Your prerequisite introduced research ethics in the context of human subjects — the rules that protect participants from harm. This topic addresses a different dimension of integrity: not participant harm but the reliability of scientific knowledge itself. The social sciences experienced what is now called the **replication crisis**: a series of high-profile failures when influential findings could not be reproduced by independent researchers. A 2015 project attempted to replicate 100 psychology studies and found that only about 36–39% produced significant results in the same direction. This is not primarily a story about fraud — it is a story about structural features of the research process that systematically inflate false-positive findings.

The key concept is **researcher degrees of freedom** — the many legitimate-seeming choices a researcher makes during data collection, processing, and analysis that can, consciously or not, be steered toward significant results. When to stop collecting data, which participants to exclude, which covariates to include, which of several plausible dependent variable operationalizations to use — each choice creates a fork. With enough forks, a researcher can almost always find a path to p < .05 even in the absence of a real effect. This is sometimes called **p-hacking** when intentional, but the same outcome arises from unconscious motivated reasoning. The research literature accumulates false positives because journals preferentially publish significant results (**publication bias**), so the non-significant replications that never get submitted are invisible.

**Preregistration** is the primary structural solution. Before collecting data, a researcher publicly registers their hypotheses, sample size, exclusion criteria, and analysis plan in a time-stamped repository (such as AsPredicted or OSF). This creates a clean separation between confirmatory analysis (testing the pre-specified hypothesis) and exploratory analysis (discovering patterns not anticipated in advance). Both are legitimate, but they have different inferential status: an exploratory finding requires replication before it is treated as confirmed. Preregistration does not eliminate researcher flexibility — it makes it transparent, allowing readers to evaluate which choices were made in advance versus post-hoc.

**Open data and open code** address the complementary problem of reproducibility. When data and analysis scripts are published alongside findings, other researchers can reproduce the exact results, catch errors, and run alternative analyses. This standard — increasingly required by journals and funders — represents a shift from "trust the author" to "verify the analysis." The infrastructure for this (GitHub, OSF, Zenodo) now makes sharing cheap; the main barriers are cultural and incentive-based. A researcher who shares imperfect data faces scrutiny they might avoid by not sharing; changing these incentives requires field-level norm change, not just individual virtue. Understanding these structural dynamics is what distinguishes integrity as a systems problem from integrity as a personal ethics problem.
