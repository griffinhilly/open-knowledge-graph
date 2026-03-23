---
id: nested-case-control-studies
title: Nested Case-Control and Case-Cohort Studies
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: person-time-follow-up-studies
  type: hard
builds-toward:
- exposure-measurement-error-epi
tags:
- study-design
- efficiency
- cohort-substudies
stage: expert
status: validated
---

# Nested Case-Control and Case-Cohort Studies

## Core Idea
Nested case-control and case-cohort designs select subcohorts from a parent cohort to measure expensive exposures, reducing cost while maintaining prospective strength. Both preserve person-time denominators and allow calculation of relative risk.

## Questions

```yaml
- question: "A cohort of 50,000 people is being followed for cancer outcomes. The key exposure is a stored plasma biomarker that costs $200 to assay. Why would a nested case-control design be preferred over assaying all 50,000 participants?"
  type: multiple-choice
  options:
    - "Because nested case-control studies are retrospective and avoid recall bias"
    - "Because you only need to assay cases and a small sample of controls matched at each case's risk set, preserving prospective strength at a fraction of the cost"
    - "Because nested designs allow you to calculate odds ratios, which are more informative than rate ratios"
    - "Because the full cohort's person-time denominator is unknown and must be estimated from the sample"
  answer: 1
  explanation: "The key advantage is efficiency without sacrificing the prospective structure. By sampling controls from risk sets at the moment of each case's diagnosis, you measure the expensive exposure only in cases plus their matched controls — a tiny fraction of 50,000. Crucially, this preserves the forward-looking (prospective) nature of the parent cohort, eliminating recall bias. Option A is wrong: nested case-control is still prospective. Option C is wrong: the odds ratio from incidence density sampling estimates the *rate ratio* — a strength, not a limitation. Option D is wrong: the parent cohort's person-time is still known."

- question: "A study team wants to investigate five different outcomes (cancer, cardiovascular disease, diabetes, neurological disease, and mortality) in the same cohort. They need to measure a costly biomarker for each outcome's controls. Which design is most efficient?"
  type: multiple-choice
  options:
    - "Five separate nested case-control studies, each with its own matched risk sets"
    - "A case-cohort design, because the same subcohort serves as the reference population for all five outcomes"
    - "A traditional case-control study, because it does not require a parent cohort"
    - "A nested case-control study using one large risk set for all cases regardless of outcome type"
  answer: 1
  explanation: "The case-cohort design's critical advantage over nested case-control is that a single subcohort, sampled once at baseline, serves as the comparison group for every outcome analyzed — you measure the expensive biomarker in the subcohort once and reuse it across all five outcome analyses. Nested case-control designs match controls separately to each case at each case's risk set time; with five outcomes, this requires five separate matching exercises and potentially five different control pools. The case-cohort is the preferred design precisely in multi-outcome settings."

- question: "In a nested case-control study using incidence density sampling, controls are randomly selected from the risk set at the moment each case is diagnosed — meaning they are people who were still under follow-up and had not yet had the outcome at that moment."
  type: true-false
  answer: true
  explanation: "This is the defining feature of incidence density sampling. At each case's event time, the risk set consists of all cohort members who remain at risk (under follow-up, outcome-free) at that exact moment. Selecting controls from this risk set has a critical consequence: because controls represent the person-time at risk when each case arose, the resulting odds ratio directly estimates the incidence rate ratio — without the rare-disease approximation required by traditional case-control studies."

- question: "A traditional case-control study and a nested case-control study using incidence density sampling both produce odds ratios that directly estimate the incidence rate ratio, so their analytic advantages are equivalent."
  type: true-false
  answer: false
  explanation: "This is false. A traditional case-control study's odds ratio approximates the relative risk only under the rare-disease assumption — if the outcome is common, the odds ratio diverges from the risk ratio and rate ratio. A nested case-control with incidence density sampling, by contrast, produces an odds ratio that *directly* estimates the incidence rate ratio regardless of outcome frequency, because the sampling procedure mimics how person-time generates cases in the full cohort. This is a genuine analytic advantage of the nested design, not just a terminology difference."

- question: "Why does incidence density sampling in a nested case-control study allow the odds ratio to directly estimate the incidence rate ratio, without requiring the rare-disease assumption?"
  type: short-answer
  answer: "Because controls are sampled from the risk set at each case's event time, they represent the distribution of exposure in the person-time at risk when each case arose. This mirrors the way the rate ratio in the full cohort compares the rate of the outcome in exposed versus unexposed person-time. The sampling procedure essentially reconstructs the exposure distribution in the person-time denominator, so the resulting odds ratio is mathematically equivalent to the rate ratio — not an approximation of it."
  explanation: "In a traditional case-control study, controls represent disease-free survivors at the end of follow-up, which estimates the exposure distribution in the population at a single time point (approximating risk denominators, not person-time denominators). Incidence density sampling ties controls to the specific person-time when each case occurred, directly modeling the rate comparison. This distinction matters in practice because the rate ratio is the natural parameter of interest in cohort studies, and nested designs recover it exactly rather than approximately."
```

## Explainer

From your study of epidemiologic study designs and person-time follow-up studies, you know the basic tradeoffs: a full cohort study follows everyone from enrollment to outcome, giving you exposure data on all participants and precise estimates of incidence rates — but it is expensive when the exposure measurement is costly (a genetic assay, a stored biomarker, an expensive laboratory panel). A traditional case-control study is efficient — you only measure exposure in cases and selected controls — but it is retrospective and vulnerable to recall bias and selection bias. Nested case-control and case-cohort designs occupy a powerful middle ground: they extract efficiency savings from the case-control logic while retaining the prospective structure of a cohort.

In a **nested case-control study**, you begin with a defined parent cohort with baseline information collected at enrollment. As follow-up proceeds and cases (people who develop the outcome) emerge, you define **risk sets**: at the moment each case is diagnosed, the risk set consists of all cohort members who are still under follow-up and haven't yet had the outcome — they were "at risk" of being the case at that moment. You then randomly sample a small number of **controls** from the risk set for each case, and measure the expensive exposure only in the cases plus their matched controls. This sampling procedure is called **incidence density sampling**. Because controls are sampled from the risk set at the time of the case, the odds ratio from the nested case-control directly estimates the **rate ratio** (incidence rate ratio) — without the approximation assumptions required by traditional case-control studies. This is a major advantage: you recover the interpretive strength of a rate-based cohort analysis at a fraction of the cost.

The **case-cohort design** solves the same efficiency problem differently. Rather than matching controls to each case individually, you define a **subcohort** — a random sample of the full cohort selected at baseline — and measure the expensive exposure in everyone in the subcohort plus all cases (whether or not they are in the subcohort). The subcohort serves as the reference population for all cases throughout the study period, regardless of when they occur. This means a case-cohort design can support multiple outcomes analyzed against the same subcohort, making it highly efficient for studies with several endpoints. The analysis uses modified survival analysis methods (Prentice weighting) to account for the fact that subcohort members are sampled with known probability. The case-cohort design produces **hazard ratios** rather than odds ratios, and the subcohort members who later become cases contribute to both the case group and the subcohort, requiring care in the statistical analysis.

Both designs preserve the prospective exposure-before-outcome ordering that eliminates recall bias. Both allow you to calculate absolute risks and rates, not just odds ratios, because the parent cohort's person-time denominator is known. The key tradeoff between them is this: nested case-control designs are more statistically efficient when you have a single outcome and want to match on time-varying confounders, while case-cohort designs are more efficient when you want to study multiple outcomes against the same control pool. In either case, you are buying analytic power at a fraction of the cost of measuring the expensive exposure in the full cohort — which is why these designs are standard in large biobank studies where genetic or biomarker assays are the bottleneck.
