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
status: validated
---

# Evidence Hierarchy and Appraisal

## Core Idea
Evidence hierarchies rank study designs by strength of causal inference, with systematic reviews and randomized controlled trials at the top and expert opinion at the bottom. Critical appraisal tools assess bias risk, internal validity, precision, and applicability to synthesize evidence for public health decision-making. Study design alone does not determine evidence quality; execution and directness matter equally.

## How It's Best Learned
Use standardized appraisal tools (ROBINS-I for observational studies, Cochrane risk-of-bias tool for RCTs) on real papers. Discuss why a study's position in the hierarchy depends on design, execution, and applicability to the policy question.

## Common Misconceptions
Assuming RCTs are always better evidence than observational studies. Ignoring applicability and external validity in favor of internal validity. Rating a poorly-executed RCT higher than a well-designed observational study with greater applicability.

## Questions

```yaml
- question: "A pharmaceutical company presents a randomized controlled trial showing their drug reduces LDL cholesterol by 30% over 12 weeks in healthy male volunteers aged 25–40. A public health team also has a 20-year cohort study of 50,000 adults (men and women, all ages, with comorbidities) showing that a dietary pattern reduces cardiovascular mortality by 18%. For setting cardiovascular prevention policy in elderly women, which evidence is likely more informative?"
  type: multiple-choice
  options:
    - "The RCT, because randomization eliminates confounding and places it higher in the evidence hierarchy"
    - "The cohort study, because its population is more applicable to elderly women and its outcome (mortality) is directly clinically relevant"
    - "The RCT, because observational studies always have more confounding than randomized trials"
    - "They are equally informative, and the policy team should synthesize both with equal weight"
  answer: 1
  explanation: "This is the key distinction between hierarchy position and evidence quality. The RCT ranks higher in the hierarchy, but its internal validity advantage is irrelevant here because the trial population (healthy young men) and outcome (surrogate marker — LDL) don't answer the policy question. The cohort study has residual confounding, but its population matches the target (elderly women with comorbidities) and its outcome (mortality) is directly relevant. Applicability and outcome directness matter as much as internal validity."

- question: "A systematic review pools results from 12 RCTs on a new antibiotic. All 12 trials had inadequate blinding, industry-funded outcome assessment, and high dropout rates. What is the most accurate characterization of this systematic review's evidence quality?"
  type: multiple-choice
  options:
    - "High quality — systematic reviews always rank at the top of the evidence hierarchy regardless of included study quality"
    - "Moderate quality — the pooled sample size compensates for individual study weaknesses"
    - "Low quality — a meta-analysis of biased RCTs produces a precise but biased pooled estimate, no better than its component studies"
    - "Indeterminate — additional RCTs should be added until the bias risk averages out"
  answer: 2
  explanation: "A systematic review is only as good as its input studies. Pooling biased studies increases statistical precision (narrower confidence intervals) but does not reduce bias — it produces a precise estimate of a biased effect. This is the 'measuring a bent ruler more carefully' problem. Critical appraisal must assess each included study's risk of bias using standardized tools; the hierarchy position of the review type does not guarantee quality."

- question: "A well-designed observational cohort study with long follow-up and directly clinically relevant outcomes can provide stronger evidence for a policy decision than a poorly-executed RCT with surrogate endpoints and a highly selected population."
  type: true-false
  answer: true
  explanation: "This is the central insight: evidence hierarchy position and evidence quality are not the same thing. Hierarchy position describes ideal design advantages; actual quality depends on execution and applicability. A cohort study with large sample, long follow-up, appropriate population, and directly relevant outcomes may be far more informative than an RCT that was well-randomized but tested in the wrong population, used surrogate markers, or had high attrition."

- question: "The evidence hierarchy ranks randomized controlled trials above observational studies because RCTs usually produce more externally valid results."
  type: true-false
  answer: false
  explanation: "RCTs are ranked higher for internal validity — specifically, because randomization controls for both measured and unmeasured confounding. But RCTs often have poor external validity: highly selective eligibility criteria, artificial settings, and short follow-up can all limit applicability. Observational studies, by contrast, often capture real-world populations and long-term outcomes. The hierarchy is about causal inference, not external validity or applicability."

- question: "A public health professional receives an RCT showing a drug is effective. What three dimensions of evidence appraisal should they assess before using these results to inform policy?"
  type: short-answer
  answer: "Internal validity (was the trial conducted without bias — appropriate randomization, blinding, complete follow-up, unbiased outcome assessment?); precision (were confidence intervals narrow enough to distinguish meaningful from trivial effects?); and applicability (does the trial population, setting, dose, and outcome reflect the population and decision context for which policy is being set?)."
  explanation: "Each dimension can independently undermine otherwise impressive results. A perfectly randomized trial of a drug in young men without comorbidities provides an unbiased estimate — but an unbiased estimate of the effect in that specific population, not in elderly women with multiple medications. Evidence appraisal is ultimately asking: 'Unbiased estimate of what, in whom, and does that answer my question?'"
```

## Explainer

The evidence hierarchy is a framework for thinking about how much confidence you can place in a causal claim from a study. You already know the major epidemiologic study designs — case reports, cross-sectional surveys, cohort studies, case-control studies, and randomized controlled trials. The hierarchy arranges these by how well each design controls for **confounding**: the problem that an observed association between an exposure and an outcome might be explained by a third variable that predicts both. The core question is always: how confident can we be that this association is causal, not spurious?

At the base of the hierarchy sit case reports and expert opinion. These have high **face validity** — a physician describing a novel drug reaction in a single patient may be clinically compelling — but they carry almost no causal weight because they involve no comparison group. Moving up, observational studies (cross-sectional, case-control, cohort) add comparison groups but cannot randomize. **Cohort studies** are the strongest observational design for establishing temporal sequence (exposure precedes outcome) and can adjust statistically for measured confounders, but unmeasured confounding is always a residual threat. **Case-control studies** efficiently study rare outcomes but are vulnerable to recall bias and selection bias in choosing controls. At the apex of the traditional hierarchy sit **randomized controlled trials (RCTs)**, because randomization distributes both measured and unmeasured confounders equally across arms — the only study design that can control for what you don't know to measure.

Above individual RCTs sit **systematic reviews** and **meta-analyses**, which pool results across multiple studies to increase statistical power and assess consistency of findings. When well-conducted, they provide the most precise and reproducible estimate of an effect. But their quality depends entirely on the quality and comparability of included studies — a meta-analysis of biased RCTs produces a precise but biased pooled estimate, the statistical equivalent of measuring a bent ruler more carefully. This is why critical appraisal cannot stop at identifying a study's position in the hierarchy; it must assess each study's **risk of bias** using standardized tools like the Cochrane RoB 2 tool for RCTs and ROBINS-I for non-randomized studies.

The most important insight from evidence appraisal is that **hierarchy position and evidence quality are not the same thing**. A rigidly designed RCT with a surrogate endpoint, a highly selected trial population, and a short follow-up period may provide weaker evidence for a policy decision than a large, well-controlled cohort study with long follow-up and outcomes that matter directly to patients. The appraisal dimensions that matter most are: internal validity (was the study conducted without bias?), precision (were confidence intervals narrow enough to be clinically useful?), and **applicability** (does the study population and context match the decision being made?). A trial of a drug in young men without comorbidities tells you little about its effect in elderly women with polypharmacy — the causal estimate may be unbiased within the trial but uninformative for the policy question. Evidence appraisal is ultimately an exercise in asking: "Unbiased estimate of what, in whom, and does that answer my question?"
