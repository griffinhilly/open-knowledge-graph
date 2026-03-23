---
id: vaccine-effectiveness-evaluation
title: Vaccine Effectiveness Evaluation
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: herd-immunity-and-vaccination
  type: hard
- id: relative-risk-calculation
  type: soft
- id: antibody-structure-and-function
  type: soft
- id: adaptive-immune-response-kinetics
  type: soft
tags:
- vaccine-studies
- immunization-programs
- disease-prevention
stage: expert
status: validated
---

# Vaccine Effectiveness Evaluation

## Core Idea
Vaccine effectiveness (VE) measures the proportional reduction in disease risk among vaccinated compared to unvaccinated populations under real-world field conditions—distinct from efficacy measured in randomized trials. VE is estimated using cohort and case-control designs and must account for vaccination coverage variations, waning immunity over time, and evolving population immunity. Time-stratified VE analysis reveals seasonal and temporal patterns. Modern efficient designs (screening method, test-negative) are increasingly used for evaluating influenza and other seasonal vaccines.

## How It's Best Learned
Calculate vaccine effectiveness from published cohort and case-control studies; implement test-negative design using flu surveillance data.

## Common Misconceptions
Vaccine effectiveness estimates are universally applicable across all populations and time periods. Efficacy measured in trials equals effectiveness in the field.

## Questions

```yaml
- question: "A vaccine showed 95% efficacy in a phase III RCT among adults aged 18–65 during controlled trial conditions. Six months after rollout among elderly populations, field studies estimate 60% effectiveness. Which explanation best accounts for this gap?"
  type: multiple-choice
  options:
    - "The field studies are unreliable — effectiveness estimates are inherently less accurate than RCT efficacy"
    - "The gap is a statistical artifact because elderly populations are too small to yield precise estimates"
    - "Vaccine effectiveness differs from efficacy due to real-world factors: different population (elderly, more comorbidities), waning immunity over time, and possible strain evolution"
    - "The trial overestimated efficacy because it used the test-negative design"
  answer: 2
  explanation: "Efficacy and effectiveness measure different things. Trial efficacy is measured under ideal, controlled conditions in a selected population. Real-world effectiveness reflects what the vaccine actually does in heterogeneous populations, with different immune backgrounds, waning immunity over months, and evolving circulating strains. None of these forces should make the estimates identical. The gap between 95% and 60% is not a measurement failure — it is the exact signal that vaccine surveillance programs exist to detect. Options A and B misidentify a real biological phenomenon as a statistical problem. Option D confuses study design (the test-negative design is used for field studies, not RCTs)."

- question: "Why does the test-negative design effectively reduce healthy vaccinee bias in influenza vaccine effectiveness studies?"
  type: multiple-choice
  options:
    - "It randomizes patients between vaccinated and unvaccinated groups"
    - "Both test-positive cases and test-negative controls sought care for flu-like illness, so health-seeking behavior is balanced between groups — the key confounder is controlled by design"
    - "It excludes elderly patients, who are disproportionately targeted for vaccination"
    - "It measures antibody titers directly, bypassing the need to compare vaccinated and unvaccinated individuals"
  answer: 1
  explanation: "Healthy vaccinee bias arises because healthier, more health-conscious people are more likely to get vaccinated AND more likely to seek care — making vaccinated people look better than the vaccine actually makes them. The test-negative design controls this by enrolling only patients who already came to care with flu-like illness. Both test-positive cases and test-negative controls are care-seekers, so care-seeking behavior is similar in both groups. Vaccination status is then compared within this care-seeking population, removing the confounding effect of differential care-seeking. This is an elegant observational design solution that does not require randomization."

- question: "A cohort study following vaccinated and unvaccinated individuals may overestimate vaccine effectiveness if healthier, more health-conscious individuals are more likely to seek vaccination."
  type: true-false
  answer: true
  explanation: "This is the healthy vaccinee bias. If vaccinated people are systematically healthier than unvaccinated people (due to health-consciousness, access, or physician recommendation patterns), then even a vaccine with no efficacy would appear to protect them — their lower disease rates would partly reflect pre-existing health differences. Controlling for measured confounders (age, sex, comorbidities) helps, but unmeasured health-consciousness or health-seeking behavior is hard to fully adjust for. This is one reason observational VE estimates require careful interpretation."

- question: "Vaccine effectiveness against influenza is approximately constant throughout a season because the immune response is fully established before the flu season begins."
  type: true-false
  answer: false
  explanation: "VE against influenza wanes measurably within a single season. Vaccine-induced antibody titers decline over time, and circulating influenza strains may drift away from vaccine strains as the season progresses. Studies consistently show higher VE in the weeks immediately following vaccination than later in the season. This is why time-stratified VE analysis is important — it estimates effectiveness in windows defined by time since vaccination, capturing the waning pattern. For COVID-19, the waning was even more dramatic, driving booster dose recommendations. VE is not a fixed number but a function of time since vaccination, among other variables."

- question: "Why should vaccine effectiveness be understood as a function of multiple variables rather than as a single fixed number, and what are the key variables it depends on?"
  type: short-answer
  answer: "VE is not a stable property of a vaccine but varies with: (1) the pathogen strain — a vaccine calibrated against one variant may be less effective against a drifted strain; (2) the target population — age, immune history, comorbidities, and prior infection all affect immune response; (3) time since vaccination — immunity wanes, so early post-vaccination VE may be 90% while VE six months later could be 50%; and (4) the clinical endpoint — VE against any infection is typically lower than VE against symptomatic disease, which is lower than VE against hospitalization or death. A single headline number (e.g., '95% effective') is a snapshot at a specific time, in a specific trial population, against a specific strain, measuring a specific outcome. Treating it as a universal constant leads to both overconfidence and unjustified dismissal of vaccines as protection wanes."
```

## Explainer

From your work on epidemiologic study designs, you know that randomized controlled trials (RCTs) are the gold standard for estimating causal effects. When a vaccine is tested in a phase III RCT — randomized assignment, blinded outcome assessment, controlled conditions — the result is **vaccine efficacy (VE_trial)**: the proportional reduction in disease incidence in vaccinated versus placebo recipients under ideal trial conditions. This number tells you what the vaccine can do. **Vaccine effectiveness (VE_field)** is different: it measures what the vaccine actually does in real-world populations, where vaccination is not randomized, conditions vary, strains drift, and immunity wanes. The gap between efficacy and effectiveness can be substantial and is the central focus of post-licensure vaccine surveillance.

The formula is the same regardless of study design: VE = 1 − RR (or 1 − OR when using case-control designs). If vaccinated individuals have 40% the disease risk of unvaccinated, VE = 1 − 0.40 = 60%. In a **cohort study**, you follow vaccinated and unvaccinated individuals and compare incidence rates — giving you a relative risk directly. In a **case-control study**, you compare vaccination status among cases and controls, yielding an odds ratio that approximates relative risk when disease is rare. Both designs require careful attention to confounding: vaccination status in real populations is not random. The **healthy vaccinee bias** — where healthier, more health-conscious people are more likely to get vaccinated — inflates VE estimates. Conversely, the **frailty bias** — where high-risk individuals are preferentially targeted for vaccination — deflates estimates. Uncontrolled confounders can make a marginally effective vaccine look excellent or an effective vaccine look useless.

The **test-negative design** is an elegant solution developed originally for influenza VE studies. Cases are patients who present to healthcare with flu-like illness and test positive for influenza; controls are patients with the same presentation who test negative. Because both groups sought care for similar symptoms, care-seeking behavior (a major confounder) is balanced between them. Vaccination status is then compared. The test-negative design removes the healthy-vaccinee bias almost entirely and is now the dominant design for rapid seasonal influenza effectiveness evaluation, requiring only routine surveillance data and no separate enrollment.

**Waning immunity** and **strain mismatch** are the two forces that make VE a moving target rather than a fixed property. Effectiveness against influenza declines measurably within a single season as vaccine-induced antibody titers fall and circulating strains evolve away from vaccine strains. For COVID-19, early VE estimates against severe disease exceeded 90% and fell substantially over 6–12 months. **Time-stratified VE analysis** — estimating effectiveness in strata defined by time since vaccination — captures this waning and informs booster timing decisions. Understanding that VE is not a single number but a function of pathogen, population, time, and endpoint (infection vs. symptomatic disease vs. hospitalization vs. death) is the key conceptual advance that separates sophisticated vaccine surveillance from naive headline-reading.
