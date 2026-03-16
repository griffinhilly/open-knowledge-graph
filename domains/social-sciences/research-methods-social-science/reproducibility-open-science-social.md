---
id: reproducibility-open-science-social
title: Reproducibility and Open Science in Social Research
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-advanced
  type: soft
tags:
- reproducibility
- replication
- pre-registration
- open-data
- transparency
stage: advanced
status: draft
---

# Reproducibility and Open Science in Social Research

## Core Idea
Examines reproducibility and replicability challenges in social science, covering p-hacking, the replication crisis, and solutions including pre-registration, open data, code sharing, and transparent reporting. Addresses tensions between exploratory and confirmatory research.

## How It's Best Learned
Pre-register a study hypothesis and analysis plan, practice reproducible data management and scripting, analyze meta-science evidence on replication rates, discuss incentive structures in publishing.

## Common Misconceptions
- Reproducibility means perfect replication
- Pre-registration limits exploratory discovery
- Open science requires sharing identifying information

## Explainer

From your research design work, you know that a study's internal validity depends on following a rigorous protocol from hypothesis to analysis. **Reproducibility** and **replicability** capture two related but distinct standards for scientific quality. A study is *reproducible* if someone using the same data and the same code reaches the same results — a purely computational standard. It is *replicable* if an independent team using different data and the same method obtains the same effect — a deeper epistemic standard about whether the finding generalizes. The **replication crisis** that shook psychology and social science beginning around 2011 revealed that many prominent findings failed the replication standard: when independent labs tried to reproduce canonical experiments, they often got much smaller effects or none at all.

The primary culprit is a cluster of practices that collectively go by the name **researcher degrees of freedom** — the many small, apparently reasonable decisions researchers make after data collection that, when made strategically (often unconsciously), inflate false-positive rates. **p-hacking** refers to running multiple analyses and reporting only those that cross the p < .05 threshold. **HARKing** (Hypothesizing After Results are Known) means presenting a post-hoc explanation as if it were a prior prediction. Optional stopping — continuing to collect data until significance is achieved — is another form. None of these feel like fraud because each individual choice seems defensible; but collectively they break the probabilistic logic that makes p-values meaningful. A p-value of .04 promises a 4% false-positive rate only if a single pre-specified test is run; if twenty versions of the analysis were tried, the actual false-positive rate is far higher.

The primary reform is **pre-registration**: publicly depositing a study's hypotheses, design, and analysis plan before data collection begins, typically on a platform like OSF (Open Science Framework) or AsPredicted. Pre-registration doesn't prevent exploratory analysis — it *labels* it as exploratory, distinguishing it from confirmatory tests where the p-value logic applies. A related reform is **registered reports**, a publication format where journals accept a study based on its design and analysis plan before seeing results, eliminating publication bias (the tendency to publish only significant findings). Together, these practices separate confirmatory from exploratory research rather than prohibiting either.

**Open data** and **code sharing** address reproducibility directly: when raw data and analysis scripts are publicly archived, other researchers can verify the computational chain from data to reported statistics. This has revealed numerous errors in published papers and enabled large-scale data aggregation. The concern about sharing identifying information is real for sensitive data (health records, responses about illegal behavior), but de-identification, access-controlled repositories, and synthetic data generation can address most cases without requiring abandonment of openness. The broader shift these reforms represent is from a culture of *trust in credentials* (the expert ran the study, so accept the result) toward a culture of *trust in transparency* (show me the protocol and data so the community can check).
