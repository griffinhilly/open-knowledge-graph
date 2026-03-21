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

## Questions

```yaml
- question: "A new antidepressant is associated with a doubled risk of type 2 diabetes in a large insurance claims cohort compared to non-users of antidepressants. Which methodological threat most plausibly explains this finding even if the drug has no real effect?"
  type: multiple-choice
  options:
    - "Immortal time bias — the period before first prescription is misclassified as exposed"
    - "Confounding by indication — depression itself increases diabetes risk, and depressed patients are more likely to receive the drug"
    - "Disproportionality inflation — the database is too large to detect true null associations"
    - "Channeling bias — the drug is preferentially prescribed to younger, healthier patients"
  answer: 1
  explanation: "Confounding by indication is the central threat in pharmacoepidemiology: the disease being treated is itself a risk factor for the outcome, making the drug appear harmful even if it is not. Depression independently raises diabetes risk via metabolic and behavioral mechanisms. The comparison group (non-users) is systematically different from drug users in a way that predicts the outcome. An active comparator design — comparing the drug to another antidepressant rather than to non-users — is the standard methodological fix."

- question: "A spontaneous reporting analysis finds that Drug X has a proportional reporting ratio (PRR) of 8.5 for a specific cardiac arrhythmia, far exceeding the threshold used for signal detection. What does this finding establish?"
  type: multiple-choice
  options:
    - "Drug X causally increases the risk of this arrhythmia in the general population"
    - "Drug X should be immediately withdrawn from the market"
    - "The drug-event pair is reported more often than expected by chance, warranting further investigation"
    - "The absolute risk of arrhythmia in Drug X users is 8.5 times higher than in non-users"
  answer: 2
  explanation: "Disproportionality analysis in spontaneous reporting detects statistical signals — drug-event pairs reported more often than chance would predict — but cannot establish causation. The database has no denominator (you don't know how many patients took the drug without incident), voluntary reporting biases the sample, and confounding is uncontrolled. A strong PRR is a hypothesis-generator that triggers regulatory investigation, not a causal verdict. Interpreting it as a relative risk (option D) confuses signal strength with incidence ratio."

- question: "Spontaneous adverse event reporting systems (like FDA's FAERS) cannot calculate true incidence rates of adverse drug reactions."
  type: true-false
  answer: true
  explanation: "Spontaneous reporting systems lack a denominator: they record the number of adverse event reports filed, but not the number of people who took the drug without incident. Without knowing the total exposure, you cannot compute incidence (events per exposed person-time). This is a fundamental structural limitation, not a data-quality problem. It is why disproportionality analyses compare reporting rates within the database rather than computing absolute risks."

- question: "In a large pharmacoepidemiology database study, a very high odds ratio (e.g., OR = 15) provides stronger evidence of causation than a modest odds ratio (e.g., OR = 1.5) because statistical association implies causation at sufficient magnitude."
  type: true-false
  answer: false
  explanation: "In large administrative databases, statistical association is almost guaranteed to be achievable for any drug-outcome pair if you search long enough — the challenge is not detecting association but distinguishing true causal effects from confounding, selection bias, and multiple comparisons. The Bradford Hill criterion of 'strength of association' does play a role in causal assessment, but it cannot substitute for ruling out confounding. A very large association could still be entirely explained by confounding by indication. The discipline's goal is causal inference under observational constraints, not effect-size maximization."

- question: "Why does confounding by indication pose a particular challenge in pharmacoepidemiology, and how does an active comparator design address it?"
  type: short-answer
  answer: "Confounding by indication occurs because the disease for which a drug is prescribed is itself often a risk factor for the outcomes being studied — so sicker patients receive certain drugs, making the drug appear harmful even if it is neutral or protective. Simply comparing drug users to non-users conflates drug effect with disease effect. An active comparator design addresses this by comparing the drug of interest to another drug prescribed for the same indication — so both groups have the same underlying disease. This balances the confounding variable (disease severity) across exposure groups, isolating the drug's effect more cleanly."
  explanation: "This is the defining methodological challenge of pharmacoepidemiology because the very purpose of a drug (treating a disease) makes non-users a systematically invalid comparison group. Active comparator designs have become standard practice in the field because they eliminate the most severe form of indication confounding, though they do not solve all confounding problems — residual confounding from drug selection within the same indication class can remain."
```

## Explainer

From your study of epidemiologic study designs, you know the core toolkit: randomized controlled trials eliminate confounding through random assignment; cohort studies follow exposed and unexposed groups forward through time to measure incidence; case-control studies work backward from outcomes to compare exposure histories. Clinical trials using this toolkit are the gold standard for establishing drug efficacy before regulatory approval. But they have a structural limitation that becomes apparent once a drug enters widespread use. Trials enroll carefully selected patients (often younger, without comorbidities, taking few other medications) for months to a few years, and are powered to detect primary efficacy endpoints — not rare adverse events. A drug then used by millions of patients for decades, across populations with multiple co-medications and chronic conditions, creates an entirely different observational context. **Pharmacoepidemiology** is the discipline that applies epidemiologic methods to study what drugs actually do in those real-world populations, at real scale, over real time.

The first systematic activity is **post-market surveillance** — detecting safety signals after a drug enters widespread use. The oldest method is **spontaneous reporting**: healthcare providers and patients voluntarily report suspected adverse drug reactions to regulatory agencies (the FDA's FAERS database in the US, Yellow Card in the UK). The resulting database contains millions of individual case safety reports, but with fundamental limitations: reporting is voluntary and inconsistent, so dramatic acute events are over-represented while chronic or subtle effects are under-reported, and there is no denominator — you know how many adverse event reports were filed, but not how many people took the drug without incident. Despite these limitations, spontaneous reporting is a powerful hypothesis-generator. **Disproportionality analysis** uses statistics like the **proportional reporting ratio (PRR)** to identify drug-event pairs reported more often than you would expect by chance, given how often the drug and the event each appear separately in the database. A strong disproportionality signal triggers regulatory investigation but does not itself establish causation.

To move from signal to evidence, pharmacoepidemiologists use the study designs from your prerequisite applied to large administrative databases: insurance claims, electronic health records, pharmacy dispensing data. A **cohort study** in claims data follows everyone who initiated Drug A versus a comparable drug for the same indication, using **propensity score matching** to balance baseline covariates and reduce confounding, then compares rates of hospitalization or serious adverse events over years of follow-up. A **nested case-control study** identifies all patients who experienced a rare outcome (drug-induced liver failure, anaphylaxis) within a cohort and compares their recent drug exposures to matched controls. These designs face specific validity threats that standard epidemiologic training must be extended to address: **confounding by indication** (sicker patients receive certain drugs, making the drug appear harmful even if it is not), **immortal time bias** (misclassifying the period between cohort entry and first prescription as unexposed time), and **channeling bias** (new drugs are often prescribed to different risk subgroups than old drugs). Recognizing and methodologically addressing these biases — through active comparator designs, restriction, or time-varying exposure analysis — is the technical heart of the field.

Establishing causality from observational data requires structured judgment. The **Bradford Hill criteria** — originally developed for the smoking-lung cancer relationship — provide prompts for evaluating a body of evidence: Does exposure precede outcome (**temporality**)? Does more drug produce more risk (**dose-response**)? Does the association replicate across studies and populations (**consistency**)? Is there a plausible biological mechanism (**biological plausibility**)? Is the effect large enough to be implausible as confounding (**strength of association**)? These criteria do not produce a checklist with a binary answer; they are structured ways of weighing a body of evidence. In pharmacoepidemiology, temporality and biological plausibility are often most decisive — because statistical association in large databases is almost guaranteed to be achievable for any drug-outcome pair if you search long enough. The discipline's goal is not to detect association but to distinguish true causal drug effects from the background noise of confounding, selection bias, and multiple comparisons.
