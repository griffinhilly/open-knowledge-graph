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
stage: expert
status: validated
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

## Questions

```yaml
- question: "A researcher runs 20 different statistical analyses on their dataset — varying covariates, exclusion criteria, and outcome measures — and reports only the analysis that yields p = .03. Why is this problematic?"
  type: multiple-choice
  options:
    - "Running more than one analysis on the same dataset always inflates effect sizes"
    - "A p-value is only valid if a single pre-specified test is run; with 20 analyses, the probability of at least one false positive by chance far exceeds 5%, so p = .03 no longer carries its nominal meaning"
    - "Reporting a single result from multiple analyses violates open data requirements"
    - "The p-value is only problematic if the researcher was consciously trying to get a significant result"
  answer: 1
  explanation: "The probabilistic logic of p-values assumes that a single pre-specified test is run. A p-value of .03 promises a 3% false-positive rate — but only if you ran that test once. If you tried 20 versions and reported the best result, the actual probability of getting at least one false positive is much higher (for independent tests, roughly 1 − 0.97²⁰ ≈ 46%). This is p-hacking: not necessarily intentional fraud, but the cumulative effect of 'researcher degrees of freedom' — small, defensible-seeming decisions after data collection that collectively break the statistical logic being invoked."

- question: "What does pre-registration primarily accomplish in scientific research?"
  type: multiple-choice
  options:
    - "It prevents researchers from conducting any exploratory analyses on their data"
    - "It separates confirmatory tests (where p-value logic applies) from exploratory analyses (which are labeled as such), eliminating the ambiguity that researcher degrees of freedom exploit"
    - "It guarantees that pre-registered studies will replicate because the design was publicly committed in advance"
    - "It eliminates publication bias by requiring all pre-registered studies to be published regardless of results"
  answer: 1
  explanation: "Pre-registration doesn't prohibit exploratory analysis — it labels it. By depositing hypotheses, design, and analysis plan before data collection, researchers create a clear distinction: confirmatory tests follow the pre-specified plan and p-values carry their nominal meaning; anything beyond that is labeled exploratory and not treated as confirmatory evidence. This eliminates the loophole that researcher degrees of freedom exploit, which is the post-hoc selection of analyses that happened to be significant. Registered reports extend this further by having journals accept based on design before results are known."

- question: "A study is reproducible (same data + same code → same statistical results) but fails to replicate (independent team, new data → much smaller effect). These two outcomes are compatible."
  type: true-false
  answer: true
  explanation: "Reproducibility and replicability are distinct standards. Reproducibility is a computational standard: given the same inputs, the analysis pipeline produces the same outputs. A study can be perfectly reproducible — every number checks out — and still fail to replicate, meaning the effect was real in that one dataset but doesn't generalize to new data and different samples. Replicability is the deeper epistemic standard: does the effect exist in the world, or was it specific to sampling variability, context, or researcher degrees of freedom in the original study? The replication crisis revealed many high-profile findings that were reproducible but not replicable."

- question: "Pre-registration prohibits researchers from conducting exploratory data analysis; once a study is pre-registered, researchers must report only the pre-specified analyses."
  type: true-false
  answer: false
  explanation: "This is a common misconception that discourages pre-registration. Pre-registration does not prohibit exploration — it distinguishes exploration from confirmation. Researchers can still run any analyses they like; the constraint is on labeling: only analyses specified in advance can be reported as confirmatory tests. Everything else is labeled exploratory, with appropriate caveats that the findings require replication. This distinction is the entire point: exploratory findings are valuable and generate hypotheses; confirmatory tests evaluate those hypotheses. Pre-registration restores that distinction without sacrificing either."

- question: "Why did the replication crisis emerge primarily from practices that most researchers did not consider fraudulent, and what does this reveal about the relationship between individual decisions and systemic research quality?"
  type: short-answer
  answer: "The replication crisis arose from 'researcher degrees of freedom' — the many small, apparently reasonable decisions made after data collection (which covariates to include, which outliers to exclude, when to stop collecting data, which outcome measure to report). Each decision seems defensible in isolation, but when made strategically — even unconsciously — they collectively inflate false-positive rates far above the nominal 5%. No individual felt they were fabricating results; they were exercising normal scientific judgment. The systemic problem is that incentive structures (publish or perish, journals favoring significant novel results) pushed these decisions in one direction repeatedly."
  explanation: "This reveals that research quality is not just a matter of individual integrity — it's a property of systems and incentive structures. When the reward structure consistently favors significant, novel, clean results, many small individually defensible decisions cumulatively produce a literature biased toward false positives. Open science reforms (pre-registration, registered reports, open data) work by changing the system's incentive structure rather than assuming individual virtue will be sufficient. The lesson is that structural solutions are needed alongside — not instead of — individual commitment to rigor."
```

## Explainer

From your research design work, you know that a study's internal validity depends on following a rigorous protocol from hypothesis to analysis. **Reproducibility** and **replicability** capture two related but distinct standards for scientific quality. A study is *reproducible* if someone using the same data and the same code reaches the same results — a purely computational standard. It is *replicable* if an independent team using different data and the same method obtains the same effect — a deeper epistemic standard about whether the finding generalizes. The **replication crisis** that shook psychology and social science beginning around 2011 revealed that many prominent findings failed the replication standard: when independent labs tried to reproduce canonical experiments, they often got much smaller effects or none at all.

The primary culprit is a cluster of practices that collectively go by the name **researcher degrees of freedom** — the many small, apparently reasonable decisions researchers make after data collection that, when made strategically (often unconsciously), inflate false-positive rates. **p-hacking** refers to running multiple analyses and reporting only those that cross the p < .05 threshold. **HARKing** (Hypothesizing After Results are Known) means presenting a post-hoc explanation as if it were a prior prediction. Optional stopping — continuing to collect data until significance is achieved — is another form. None of these feel like fraud because each individual choice seems defensible; but collectively they break the probabilistic logic that makes p-values meaningful. A p-value of .04 promises a 4% false-positive rate only if a single pre-specified test is run; if twenty versions of the analysis were tried, the actual false-positive rate is far higher.

The primary reform is **pre-registration**: publicly depositing a study's hypotheses, design, and analysis plan before data collection begins, typically on a platform like OSF (Open Science Framework) or AsPredicted. Pre-registration doesn't prevent exploratory analysis — it *labels* it as exploratory, distinguishing it from confirmatory tests where the p-value logic applies. A related reform is **registered reports**, a publication format where journals accept a study based on its design and analysis plan before seeing results, eliminating publication bias (the tendency to publish only significant findings). Together, these practices separate confirmatory from exploratory research rather than prohibiting either.

**Open data** and **code sharing** address reproducibility directly: when raw data and analysis scripts are publicly archived, other researchers can verify the computational chain from data to reported statistics. This has revealed numerous errors in published papers and enabled large-scale data aggregation. The concern about sharing identifying information is real for sensitive data (health records, responses about illegal behavior), but de-identification, access-controlled repositories, and synthetic data generation can address most cases without requiring abandonment of openness. The broader shift these reforms represent is from a culture of *trust in credentials* (the expert ran the study, so accept the result) toward a culture of *trust in transparency* (show me the protocol and data so the community can check).
