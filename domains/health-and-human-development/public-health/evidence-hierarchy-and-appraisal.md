---
id: evidence-hierarchy-and-appraisal
title: Evidence Hierarchy and Appraisal
domain: health-and-human-development
course: public-health
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: biostatistics-in-public-health
  type: hard
tags:
- evidence-synthesis
- study-quality
- bias-assessment
- systematic-review
stage: advanced
status: draft
---

# Evidence Hierarchy and Appraisal

## Core Idea
Evidence hierarchies rank study designs by strength of causal inference, with systematic reviews and randomized controlled trials at the top and expert opinion at the bottom. Critical appraisal tools assess bias risk, internal validity, precision, and applicability to synthesize evidence for public health decision-making. Study design alone does not determine evidence quality; execution and directness matter equally.

## How It's Best Learned
Use standardized appraisal tools (ROBINS-I for observational studies, Cochrane risk-of-bias tool for RCTs) on real papers. Discuss why a study's position in the hierarchy depends on design, execution, and applicability to the policy question.

## Common Misconceptions
Assuming RCTs are always better evidence than observational studies. Ignoring applicability and external validity in favor of internal validity. Rating a poorly-executed RCT higher than a well-designed observational study with greater applicability.

## Explainer

The evidence hierarchy is a framework for thinking about how much confidence you can place in a causal claim from a study. You already know the major epidemiologic study designs — case reports, cross-sectional surveys, cohort studies, case-control studies, and randomized controlled trials. The hierarchy arranges these by how well each design controls for **confounding**: the problem that an observed association between an exposure and an outcome might be explained by a third variable that predicts both. The core question is always: how confident can we be that this association is causal, not spurious?

At the base of the hierarchy sit case reports and expert opinion. These have high **face validity** — a physician describing a novel drug reaction in a single patient may be clinically compelling — but they carry almost no causal weight because they involve no comparison group. Moving up, observational studies (cross-sectional, case-control, cohort) add comparison groups but cannot randomize. **Cohort studies** are the strongest observational design for establishing temporal sequence (exposure precedes outcome) and can adjust statistically for measured confounders, but unmeasured confounding is always a residual threat. **Case-control studies** efficiently study rare outcomes but are vulnerable to recall bias and selection bias in choosing controls. At the apex of the traditional hierarchy sit **randomized controlled trials (RCTs)**, because randomization distributes both measured and unmeasured confounders equally across arms — the only study design that can control for what you don't know to measure.

Above individual RCTs sit **systematic reviews** and **meta-analyses**, which pool results across multiple studies to increase statistical power and assess consistency of findings. When well-conducted, they provide the most precise and reproducible estimate of an effect. But their quality depends entirely on the quality and comparability of included studies — a meta-analysis of biased RCTs produces a precise but biased pooled estimate, the statistical equivalent of measuring a bent ruler more carefully. This is why critical appraisal cannot stop at identifying a study's position in the hierarchy; it must assess each study's **risk of bias** using standardized tools like the Cochrane RoB 2 tool for RCTs and ROBINS-I for non-randomized studies.

The most important insight from evidence appraisal is that **hierarchy position and evidence quality are not the same thing**. A rigidly designed RCT with a surrogate endpoint, a highly selected trial population, and a short follow-up period may provide weaker evidence for a policy decision than a large, well-controlled cohort study with long follow-up and outcomes that matter directly to patients. The appraisal dimensions that matter most are: internal validity (was the study conducted without bias?), precision (were confidence intervals narrow enough to be clinically useful?), and **applicability** (does the study population and context match the decision being made?). A trial of a drug in young men without comorbidities tells you little about its effect in elderly women with polypharmacy — the causal estimate may be unbiased within the trial but uninformative for the policy question. Evidence appraisal is ultimately an exercise in asking: "Unbiased estimate of what, in whom, and does that answer my question?"
