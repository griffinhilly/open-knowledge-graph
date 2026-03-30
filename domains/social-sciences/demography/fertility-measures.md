---
id: fertility-measures
title: "Fertility Measures: TFR and ASFR"
domain: social-sciences
course: demography
prerequisites:
- id: crude-rates-and-specific-rates
  type: hard
- id: population-dynamics
  type: soft
builds-toward:
- fertility-transition
- population-projections
- population-momentum-demography
tags:
- fertility
- TFR
- ASFR
- replacement-level
- reproduction
stage: advanced
status: validated
---

# Fertility Measures: TFR and ASFR

## Core Idea
Age-specific fertility rates (ASFRs) measure the number of births to women in a given age group per 1,000 women in that age group, capturing how fertility varies across the reproductive lifespan. The total fertility rate (TFR) sums all ASFRs across the childbearing ages (typically 15-49), representing the average number of children a woman would bear if she experienced current age-specific rates throughout her life. Replacement-level fertility — approximately 2.1 in low-mortality populations — is the TFR at which a generation exactly replaces itself. The gross reproduction rate (GRR) and net reproduction rate (NRR) refine TFR by considering only female births and, in the case of NRR, adjusting for female mortality before and during the childbearing years.

## How It's Best Learned
Compute ASFRs from raw data (births by mother's age and female population by age), then sum to get TFR. Plotting the ASFR curve for multiple countries reveals differences in both the level and timing of fertility — where the peak falls and how concentrated or spread out childbearing is.

## Common Misconceptions
- TFR is a period measure applied to a synthetic cohort; it does not directly measure how many children any real woman will have. Tempo effects (postponement or acceleration of childbearing) can make TFR diverge substantially from completed cohort fertility.
- Replacement-level fertility is 2.1, not 2.0, because it must account for sex ratio at birth (slightly more boys) and female mortality before the end of childbearing.

## Questions

```yaml
- question: "A country's TFR drops from 2.5 to 1.6 over a decade, while completed fertility for cohorts passing through their childbearing years during the same period remains at 2.1. What best explains this discrepancy?"
  type: multiple-choice
  options:
    - "The TFR data must be incorrect — it cannot diverge this much from completed fertility"
    - "Women are postponing childbearing to later ages, creating a tempo distortion that depresses the period TFR below the cohort's actual completed fertility"
    - "Immigration of childless women inflates the denominator without adding births"
    - "Replacement-level fertility has changed due to declining mortality, making 1.6 the new replacement level"
  answer: 1
  explanation: "This is a classic tempo effect. When women delay childbearing — for example, shifting the mean age at first birth from 25 to 30 — period ASFRs at younger ages decline before ASFRs at older ages have fully compensated. The TFR, which sums current ASFRs across all ages, captures this temporary depression. Completed cohort fertility, measured after women finish childbearing, shows the actual quantum. Bongaarts and Feeney developed tempo-adjusted TFR (TFR*) to correct for this distortion."

- question: "Replacement-level fertility is exactly 2.0 children per woman because each couple needs to produce two children to replace themselves."
  type: true-false
  answer: false
  explanation: "Replacement level is approximately 2.1 in low-mortality settings, not 2.0, for two reasons: the sex ratio at birth is slightly above 1 (about 105 boys per 100 girls), so slightly more than 2 births are needed to produce one surviving daughter per woman; and some females die before completing their childbearing years. In high-mortality populations, replacement-level TFR can be 2.5 or higher because more women die before or during their reproductive years."

- question: "Explain the difference between the gross reproduction rate (GRR) and the net reproduction rate (NRR), and what an NRR of exactly 1.0 signifies."
  type: short-answer
  answer: "GRR is the TFR counting only female births — the average number of daughters a woman would bear at current age-specific fertility rates, ignoring mortality. NRR adjusts GRR for the probability of surviving to each childbearing age, giving the average number of daughters a woman will bear who survive to reproduce. An NRR of exactly 1.0 means each generation of women is exactly replacing itself — one surviving daughter per woman — indicating zero long-term natural population growth in the absence of mortality change."
  explanation: "NRR is the more meaningful measure for long-term population replacement because it accounts for mortality. A population with high fertility but high female mortality could have a high GRR but an NRR near or below 1.0. NRR connects directly to stable population theory: when NRR = 1 and age-specific rates are constant, the population will eventually reach a stationary state with zero growth."
```

## Explainer

Building on your understanding of crude and specific rates, fertility measurement adds a dimension unique to human reproduction: it is age-structured and concentrated in a specific portion of the lifespan. The **age-specific fertility rate** (ASFR) for a given age group — say, women aged 25-29 — divides the number of births to women in that age group by the number of women in that age group, typically expressed per 1,000. Plotting ASFRs across all age groups from 15 to 49 produces the **fertility schedule**, a curve that reveals both how much childbearing is occurring (the area under the curve) and when it is occurring (the shape and peak of the curve).

The **total fertility rate** (TFR) is the sum of all ASFRs (multiplied by the width of each age interval if using grouped data). It answers: "If a woman experienced today's age-specific fertility rates throughout her entire reproductive life, how many children would she have?" This is a **synthetic cohort** measure — it takes a cross-section of current behavior and applies it hypothetically to one woman's lifetime. The TFR is the most widely used fertility indicator because it is intuitive, comparable across populations, and available annually. But its synthetic nature makes it vulnerable to **tempo distortion**. When women systematically shift the timing of childbearing — delaying first births, for instance — the period TFR drops even if each woman ultimately has the same number of children. The completed fertility of actual cohorts (measured retrospectively) may tell a different story.

**Replacement-level fertility** is the TFR at which a population exactly replaces itself from one generation to the next, approximately 2.1 in low-mortality countries. The reason it exceeds 2.0 is that slightly more boys are born than girls (about 105:100), and some women die before completing childbearing. In high-mortality populations, replacement TFR can be considerably higher. This concept connects to the **net reproduction rate** (NRR), which measures how many surviving daughters each woman produces. An NRR of 1.0 is mathematically equivalent to replacement-level fertility and signals that, if current rates persist, the population will eventually stabilize (after any momentum effects work through the age structure).

The **gross reproduction rate** (GRR) counts only female births — it is the TFR restricted to daughters. The NRR further adjusts by multiplying each age-specific rate by the probability of a woman surviving to that age. The gap between GRR and NRR reflects the impact of female mortality: in a low-mortality country they are nearly identical, but in a high-mortality setting the NRR can be substantially lower than the GRR, indicating that many potential mothers die before completing their reproductive careers.
