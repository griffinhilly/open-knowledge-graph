---
id: competing-risks-analysis-biostatistics
title: Competing Risks Analysis
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: cox-proportional-hazards-detailed
  type: hard
- id: survival-analysis-kaplan-meier
  type: hard
builds-toward:
- joint-longitudinal-survival-models
tags:
- competing-risks
- cumulative-incidence
- Fine-Gray
- cause-specific-hazard
- subdistribution
stage: expert
status: validated
---

# Competing Risks Analysis

## Core Idea
Competing risks arise when subjects can experience more than one type of event, and the occurrence of one event precludes the others — a patient may die from cardiac causes, cancer, or other causes, but can only die once. Standard Kaplan-Meier and Cox methods treat competing events as censored observations, which overestimates the probability of the event of interest because it assumes censored subjects could still experience it. Two complementary approaches exist: cause-specific hazard models (separate Cox models for each event type, treating competing events as censored) and the Fine-Gray subdistribution hazard model (which directly models the cumulative incidence function, keeping subjects who experience competing events in the risk set). These approaches answer different questions and can lead to different conclusions.

## Questions

```yaml
- question: "In a study of cardiac mortality among elderly patients, deaths from cancer are treated as censored in a standard Kaplan-Meier analysis. Why does this overestimate cardiac mortality risk?"
  type: multiple-choice
  options:
    - "Cancer deaths reduce the sample size, widening confidence intervals"
    - "Censoring cancer deaths implies those patients could still die from cardiac causes, but they cannot — they are already dead. The KM estimator overestimates the cumulative probability of cardiac death by assuming censored subjects remain at risk"
    - "Cancer deaths should be combined with cardiac deaths as a single outcome"
    - "The KM estimator underestimates cardiac mortality when competing risks are present"
  answer: 1
  explanation: "The KM estimator assumes that censored subjects have the same future risk as those remaining — an assumption violated by competing risks. A patient who died of cancer is removed from the risk set as if they were merely lost to follow-up and could still have a cardiac event. The cumulative incidence function (CIF), which properly accounts for competing risks, will always be lower than or equal to the KM complement (1 - KM) because it recognizes that some subjects will experience competing events instead."

- question: "A cause-specific hazard model and a Fine-Gray subdistribution model can give contradictory results for the same exposure-outcome relationship. This occurs because they answer fundamentally different questions."
  type: true-false
  answer: true
  explanation: "The cause-specific hazard asks: among those currently alive (event-free), what is the instantaneous rate of the event of interest? The subdistribution hazard asks: what is the rate of the event of interest in a hypothetical world where subjects who experienced competing events remain in the risk set? A treatment that reduces cardiac death but increases cancer death might show a reduced cause-specific cardiac hazard but an unchanged subdistribution hazard (because fewer cardiac deaths are offset by the subjects remaining at risk longer due to increased cancer deaths). The cause-specific model is better for understanding etiology; the Fine-Gray model is better for prediction and clinical decision-making about overall risk."

- question: "Explain why the cumulative incidence function (CIF) must sum across all event types to a value less than or equal to 1, and why this constraint distinguishes it from the Kaplan-Meier complement."
  type: short-answer
  answer: "The CIF for each event type represents the probability of experiencing that specific event by time t, given that competing events are possible. Since a subject can only experience one event, the CIFs across all event types sum to the total probability of experiencing any event — which cannot exceed 1. The KM complement (1 - S(t)) computed separately for each event type treats competing events as censored and can exceed the true probability because it imagines a world without competing risks. The CIFs properly partition the total failure probability among event types."
  explanation: "At any time t, CIF_cardiac(t) + CIF_cancer(t) + CIF_other(t) = total failure probability ≤ 1. Each individual CIF is bounded above by the total failure probability. The KM complement for cardiac death, computed by censoring cancer and other deaths, estimates the probability of cardiac death in a hypothetical world where competing events do not exist — a quantity that may be of scientific interest but does not correspond to what patients actually experience."
```

## Explainer

Standard survival analysis assumes a single event type and treats everything else as censoring. This works when censoring is truly non-informative — when a subject lost to follow-up has the same future risk as those remaining. But when a patient dies of cancer, they do not have the same future cardiac risk as a living patient. Cancer death is not non-informative censoring — it is a **competing risk** that permanently removes the patient from the possibility of experiencing the cardiac event. Treating it as censoring violates the independence assumption and inflates the estimated probability of the event of interest.

The **cumulative incidence function** (CIF) directly estimates the probability of experiencing a specific event type by time t, properly accounting for the fact that some subjects will be claimed by competing events first. Unlike the KM complement (1 - S(t)), which imagines a world without competing risks, the CIF represents the actual probability in the real world where multiple event types coexist. The CIF for cardiac death will always be less than or equal to the KM complement because it acknowledges that some subjects who would have eventually died of cardiac causes will instead die of cancer first.

Two regression frameworks address competing risks. The **cause-specific hazard model** fits a separate Cox model for each event type, treating competing events as censored observations. It estimates the instantaneous rate of each event among subjects still alive — the "etiological" quantity that tells you about the direct biological effect of a covariate on a specific cause of death. The **Fine-Gray subdistribution hazard model** takes a different approach: when a subject experiences a competing event, they remain in the risk set for the event of interest with zero probability of experiencing it. This produces a hazard that directly links to the cumulative incidence function, making it natural for prediction — if you want to estimate the 5-year probability of cardiac death for a patient with specific characteristics, the Fine-Gray model gives you that directly.

These two approaches can disagree. Consider a treatment that reduces cardiac death but increases cancer death. The cause-specific cardiac hazard will show a protective effect (lower cardiac death rate among the living). But the Fine-Gray subdistribution hazard may show no effect or even an adverse effect because the patients saved from cardiac death now live longer and accumulate more cancer deaths, altering the cumulative incidence. Neither approach is "correct" — they answer different questions. Most methodologists recommend reporting both, using the cause-specific model for understanding mechanisms and the Fine-Gray model for clinical prediction.
