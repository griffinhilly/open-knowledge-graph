---
id: case-crossover-design
title: Case-Crossover Design
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: confounding-epidemiology
  type: soft
builds-toward:
- exposure-measurement-error-epi
tags:
- study-design
- acute-exposures
- within-subject-comparison
stage: advanced
status: draft
---

# Case-Crossover Design

## Core Idea
Case-crossover design studies acute exposures and acute outcomes. Each case serves as their own control by comparing exposure status in the period just before the outcome to exposure status in a reference period. This within-person comparison automatically adjusts for time-invariant confounders.

## Questions

```yaml
- question: "A researcher studies whether cell phone use immediately before a car crash increases crash risk. For each crash victim, they compare phone use in the 10 minutes before the crash to phone use during the same 10-minute window the previous day. What type of confounding does this design automatically eliminate?"
  type: multiple-choice
  options:
    - "Time-varying confounders only, such as traffic density that changes by the hour"
    - "All forms of confounding, including secular trends in cell phone adoption"
    - "Time-invariant personal characteristics like driving skill, risk tolerance, and visual acuity"
    - "Confounders that affect only the control period, not the hazard window"
  answer: 2
  explanation: "Because the same person serves as their own control, all stable personal characteristics — driving experience, personality, vehicle type, usual routes — are held constant by design. They cannot differ between the hazard window and the reference window for the same person. However, time-trend bias (e.g., cell phone use rising steadily over time) is NOT automatically eliminated; it requires careful choice of reference periods."

- question: "A researcher wants to study whether long-term low-level air pollution exposure increases the risk of developing type 2 diabetes, which accumulates over years. Is a case-crossover design appropriate?"
  type: multiple-choice
  options:
    - "Yes — air pollution is an environmental exposure, which is exactly what case-crossover designs study"
    - "Yes — as long as the hazard window is extended to cover the relevant exposure period"
    - "No — the exposure is not transient (it is chronic), and the outcome has a long latency, violating both design requirements"
    - "No — case-crossover designs can only be used for cardiovascular events, not metabolic diseases"
  answer: 2
  explanation: "Case-crossover design requires both a transient (intermittent) exposure and an acute outcome with a short, identifiable causal window. Chronic exposure like long-term air pollution cannot be captured by comparing a brief hazard window to a brief reference period — the exposure is essentially the same in both windows. Outcomes with long latency (years) also lack a meaningful 'just before the outcome' comparison point. The design is suited to acute triggers of acute events, not cumulative exposures and slowly developing diseases."

- question: "In a case-crossover design, the comparison group consists of a separate set of healthy individuals matched to the cases on demographic characteristics."
  type: true-false
  answer: false
  explanation: "This describes a conventional case-control design. In a case-crossover design, there is no separate comparison group — each case is compared to themselves at a different time. The hazard window (just before the event) is compared to one or more reference windows (the same person at other times when no event occurred). This within-person design is precisely what eliminates time-invariant confounders."

- question: "A case-crossover study comparing exposures on the day of a heart attack to exposures one week earlier is susceptible to time-trend bias if the prevalence of the exposure is changing over calendar time."
  type: true-false
  answer: true
  explanation: "If exposure prevalence is trending upward (or downward) over time, then comparing 'today' (hazard window) to 'last week' (reference window) will systematically differ in exposure rate for reasons unrelated to the event itself — the secular trend creates an artificial difference. Symmetric reference periods (comparing times equidistant before and after the event) or multiple reference windows from prior weeks are strategies used to mitigate this bias."

- question: "Why does the case-crossover design automatically control for time-invariant confounders, and what is the essential condition the exposure must meet for this design to be valid?"
  type: short-answer
  answer: "Time-invariant confounders (stable characteristics like genetics, personality, or occupational history) are held constant because the same person appears in both the hazard and control windows — they cannot differ between windows for the same individual. For validity, the exposure must be transient (it turns on and off), so there is meaningful variation between the hazard period and a reference period. Chronic or stable exposures cannot be studied this way because there is nothing to compare — exposure would be the same in both windows."
  explanation: "This is the design's defining strength and its defining limitation simultaneously. The within-person comparison is powerful precisely because it never needs to measure stable confounders — but it only works when the exposure is the kind of thing that varies day-to-day or hour-to-hour. Applications like air pollution spikes and asthma attacks, physical exertion and cardiac events, or drug initiation and adverse events all share this transient structure."
```

## Explainer

From your study of epidemiologic study designs, you know that controlling for confounding is one of the central challenges of observational research. A case-control study addresses confounding by selecting controls from the same population as cases; a cohort study addresses it by measuring confounders prospectively and adjusting statistically. The **case-crossover design** takes an entirely different approach: instead of selecting different people as controls, it uses each case as their own control. The key insight is that if a person's risk of some acute outcome (a car crash, a heart attack, an asthma exacerbation) varies over time in response to transient exposures, then you can estimate the exposure's effect by comparing what the person was exposed to immediately before the outcome to what they were exposed to during a comparable "control" period when no event occurred.

Consider the classic application: studying whether driving while talking on a cell phone increases crash risk. You recruit people who have just had a car crash. For each person, you ask: were they using a phone in the 10 minutes before the crash (the **hazard window**)? You then ask about their phone use during a reference period — say, the same 10-minute interval on the previous day. Because you are comparing the same person to themselves, all time-invariant characteristics — their driving experience, risk tolerance, visual acuity, vehicle type, regular routes — are automatically held constant. You never need to measure them, because they cannot differ between the hazard and control windows for the same person. This is the design's core strength and the direct solution to confounding by stable personal characteristics that was your prerequisite concern.

The design has specific scope conditions that are important to understand. It is appropriate only when both the exposure and the outcome are **transient** — the exposure should turn on and off (not be chronic), and the outcome should be acute (a discrete event, not a slowly accumulating disease state). Chronic exposures like smoking cannot be studied this way because there is no meaningful variation between the hazard window and reference period. Similarly, outcomes with long latency cannot be studied this way because the causal window is unknown. The case-crossover design is also susceptible to **time-trend bias**: if the background rate of the exposure is changing over time (cell phone use has increased steadily), then comparing last week to this week may confuse a secular trend with a causal effect. Choosing reference periods carefully — often symmetrically before and after the event, or using the same time-of-week in prior weeks — mitigates this. Despite these constraints, the case-crossover design has proven remarkably powerful for studying acute environmental triggers (air pollution and respiratory events), behavioral exposures (physical exertion and cardiac events), and pharmacological exposures (drug initiation and adverse events), precisely because it eliminates the vast space of stable individual confounders that plague conventional between-person designs.
