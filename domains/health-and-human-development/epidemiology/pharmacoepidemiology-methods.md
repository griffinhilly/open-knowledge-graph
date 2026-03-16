---
id: pharmacoepidemiology-methods
title: 'Pharmacoepidemiology: Drug Safety and Adverse Event Surveillance'
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
tags:
- pharmacoepidemiology
- drug-safety
- adverse-events
- spontaneous-reporting
- surveillance
stage: advanced
status: draft
---

# Pharmacoepidemiology: Drug Safety and Adverse Event Surveillance

## Core Idea
Pharmacoepidemiology applies epidemiologic methods to study medication effects in large populations, including adverse events missed in clinical trials. Surveillance systems (spontaneous reporting, claims data, electronic health records) detect safety signals post-approval. Causality assessment uses epidemiologic criteria (temporal relationship, dose-response, consistency) to distinguish true drug effects from confounding or bias.

## Explainer

From your study of epidemiologic study designs, you know the core toolkit: randomized controlled trials eliminate confounding through random assignment; cohort studies follow exposed and unexposed groups forward through time to measure incidence; case-control studies work backward from outcomes to compare exposure histories. Clinical trials using this toolkit are the gold standard for establishing drug efficacy before regulatory approval. But they have a structural limitation that becomes apparent once a drug enters widespread use. Trials enroll carefully selected patients (often younger, without comorbidities, taking few other medications) for months to a few years, and are powered to detect primary efficacy endpoints — not rare adverse events. A drug then used by millions of patients for decades, across populations with multiple co-medications and chronic conditions, creates an entirely different observational context. **Pharmacoepidemiology** is the discipline that applies epidemiologic methods to study what drugs actually do in those real-world populations, at real scale, over real time.

The first systematic activity is **post-market surveillance** — detecting safety signals after a drug enters widespread use. The oldest method is **spontaneous reporting**: healthcare providers and patients voluntarily report suspected adverse drug reactions to regulatory agencies (the FDA's FAERS database in the US, Yellow Card in the UK). The resulting database contains millions of individual case safety reports, but with fundamental limitations: reporting is voluntary and inconsistent, so dramatic acute events are over-represented while chronic or subtle effects are under-reported, and there is no denominator — you know how many adverse event reports were filed, but not how many people took the drug without incident. Despite these limitations, spontaneous reporting is a powerful hypothesis-generator. **Disproportionality analysis** uses statistics like the **proportional reporting ratio (PRR)** to identify drug-event pairs reported more often than you would expect by chance, given how often the drug and the event each appear separately in the database. A strong disproportionality signal triggers regulatory investigation but does not itself establish causation.

To move from signal to evidence, pharmacoepidemiologists use the study designs from your prerequisite applied to large administrative databases: insurance claims, electronic health records, pharmacy dispensing data. A **cohort study** in claims data follows everyone who initiated Drug A versus a comparable drug for the same indication, using **propensity score matching** to balance baseline covariates and reduce confounding, then compares rates of hospitalization or serious adverse events over years of follow-up. A **nested case-control study** identifies all patients who experienced a rare outcome (drug-induced liver failure, anaphylaxis) within a cohort and compares their recent drug exposures to matched controls. These designs face specific validity threats that standard epidemiologic training must be extended to address: **confounding by indication** (sicker patients receive certain drugs, making the drug appear harmful even if it is not), **immortal time bias** (misclassifying the period between cohort entry and first prescription as unexposed time), and **channeling bias** (new drugs are often prescribed to different risk subgroups than old drugs). Recognizing and methodologically addressing these biases — through active comparator designs, restriction, or time-varying exposure analysis — is the technical heart of the field.

Establishing causality from observational data requires structured judgment. The **Bradford Hill criteria** — originally developed for the smoking-lung cancer relationship — provide prompts for evaluating a body of evidence: Does exposure precede outcome (**temporality**)? Does more drug produce more risk (**dose-response**)? Does the association replicate across studies and populations (**consistency**)? Is there a plausible biological mechanism (**biological plausibility**)? Is the effect large enough to be implausible as confounding (**strength of association**)? These criteria do not produce a checklist with a binary answer; they are structured ways of weighing a body of evidence. In pharmacoepidemiology, temporality and biological plausibility are often most decisive — because statistical association in large databases is almost guaranteed to be achievable for any drug-outcome pair if you search long enough. The discipline's goal is not to detect association but to distinguish true causal drug effects from the background noise of confounding, selection bias, and multiple comparisons.
