---
id: life-table-methods
title: Life Table Methods and Population Survival
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: person-time-follow-up-studies
  type: hard
- id: incidence-density-rates
  type: hard
builds-toward:
  - standardized-rate-calculation
tags:
- survival-analysis
- population-rates
- life-expectancy
stage: advanced
status: draft
---
# Life Table Methods and Population Survival

## Core Idea
Life table methods summarize age-specific mortality rates to estimate population survival, life expectancy, and probability of surviving to specific ages. Life tables organize person-time and events by age group, allowing stratified survival comparisons between populations.

## Explainer

From your study of person-time and incidence density rates, you know how to express mortality as a rate: deaths divided by the total person-time at risk in an interval. A **life table** organizes these rates by age group into a single coherent framework that answers a different question: not "how many died per year of observation?" but "what is the probability that a person born today survives to age 70?" These questions are related but require a different calculation structure.

The life table begins with a hypothetical **cohort** — typically 100,000 persons — entering age 0. At each age interval (often 0–1, 1–5, 5–10, then five-year bands), you apply the observed age-specific mortality rate (the **m_x** column) from your population to estimate the probability of dying in that interval (**q_x**). From q_x you derive the number surviving into each interval (**l_x**), the number dying in each interval (**d_x**), and the person-time lived within each interval (**L_x**). Summing all remaining L_x values from a given age upward gives the total future person-time for the surviving cohort — and dividing by l_x yields **life expectancy at age x** (e_x), the expected additional years of life for someone who has survived to that age.

There are two variants. A **period life table** applies the mortality rates observed in a single time period (say, 2020) to a hypothetical cohort. It does not describe any real cohort's experience; it is a snapshot of current mortality conditions and asks: "If mortality rates stay as they are today, how long would a newborn be expected to live?" A **cohort life table** follows an actual birth cohort from birth to extinction, using the rates they actually experienced over their lifetimes. Period tables are far more common in public health because real cohorts take a century to complete; but period tables underestimate life expectancy in improving-mortality environments because they apply today's high elderly mortality rates to people who will actually experience the lower rates of decades hence.

The practical power of life tables is in **comparing survival across populations or subgroups**. You can apply separate mortality rates for men versus women, smokers versus nonsmokers, or different countries to generate parallel l_x columns and compare survival curves — the proportion of the original cohort still alive at each age. The area under the survival curve is life expectancy. Comparing these areas or specific survival probabilities (probability of surviving to age 65) makes the mortality difference concrete and interpretable in a way that comparing raw rates does not.

Life tables are the historical foundation of survival analysis in both demography and clinical epidemiology. The Kaplan-Meier estimator you may encounter in clinical research is essentially a life table adapted for censored data — individuals who leave the study before experiencing the outcome. The conceptual structure is identical: track a cohort through time, estimate survival at each event time, and multiply conditional survival probabilities together to get the overall survival curve. Understanding life tables gives you the intuition to read and critically evaluate any survival curve you encounter in the epidemiological literature.
