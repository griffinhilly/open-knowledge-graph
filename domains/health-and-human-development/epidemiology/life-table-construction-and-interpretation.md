---
id: life-table-construction-and-interpretation
title: Life Table Construction and Interpretation
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: disease-frequency-measures
  type: hard
- id: kaplan-meier-estimator
  type: soft
builds-toward:
- disability-adjusted-life-years
tags:
- life-expectancy
- survival-curves
- population-health
stage: advanced
status: draft
---

# Life Table Construction and Interpretation

## Core Idea
Life tables synthesize age-specific mortality rates into summary measures—life expectancy, survivorship curves, and years of life remaining—describing the survival experience of a population or birth cohort. They require age-specific death rates and population age structure, and allow comparison of mortality patterns across populations and time periods. Life tables enable calculation of health-adjusted life expectancy by incorporating disability or disease state. They are foundational for interpreting population health outcomes and burden-of-disease studies.

## How It's Best Learned
Construct a life table from age-specific mortality rates; calculate life expectancy at birth and at older ages; compare across populations.

## Common Misconceptions
Life tables predict individual survival outcomes. Population life expectancy improvements require changing mortality rates at specific ages.

## Explainer

You already know how to measure disease frequency — incidence rates, prevalence, and mortality rates expressed per person-time. A life table takes those age-specific mortality rates and synthesizes them into a coherent picture of how a population ages and dies. Think of it as asking a single question: if a birth cohort of 100,000 people were subject to today's age-specific mortality rates throughout their entire lives, how many would survive to each age, and how long would the average person live? The result is a compact summary of population mortality experience that allows cross-population and cross-time comparisons even when the populations have different age structures.

The construction starts from **age-specific death rates** (m_x), usually expressed as deaths per person-year in each age interval. From these rates you calculate q_x — the **probability of dying** within each age interval given survival to the start of that interval. The **survivorship column** (l_x) then tracks what fraction of the original cohort survives to each age: l_0 = 100,000 by convention; each subsequent l_x = l_{x-1} × (1 − q_{x-1}). The **person-years lived** in each interval (L_x) sums up all the time lived by the surviving cohort during that age band. Adding up all remaining person-years from age x onward gives T_x, and dividing by l_x yields **life expectancy at age x** (e_x): how many additional years someone who has already reached age x can expect to live.

The distinction between **period** and **cohort** life tables is essential for interpretation. A period life table (the most common type) applies the mortality rates observed in a single calendar year or period to a hypothetical cohort. It answers: "what would life expectancy be if current mortality rates persisted forever?" It is not a prediction for any real cohort — no actual group of people born today will face 2026 mortality rates at every age. A cohort life table follows a real birth cohort through time as actual mortality rates change, but requires waiting decades for data. Period life tables understate true cohort life expectancy when mortality is falling (which it generally is), because they embed current rates rather than the lower future rates the cohort will actually experience.

Life expectancy at birth is the most familiar summary measure, but life expectancy at age 65 is often more informative for health policy — it tells you how much survival time remains for those who have already reached old age. Because most mortality improvement in high-income countries has occurred at older ages, increases in life expectancy at 65 have been proportionally larger than increases at birth over recent decades. This matters for pension and healthcare planning. The **disability-adjusted life year (DALY)**, which this topic builds toward, extends the life table framework by weighting years lived in poor health, transforming a pure mortality instrument into a comprehensive measure of the burden of disease that can guide resource allocation across conditions with very different age distributions and severity profiles.

