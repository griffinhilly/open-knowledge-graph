---
id: life-tables-demography
title: Life Tables
domain: social-sciences
course: demography
prerequisites:
- id: crude-rates-and-specific-rates
  type: hard
- id: probability-density-functions
  type: soft
builds-toward:
- mortality-analysis
- population-projections
- stable-population-theory
tags:
- life-table
- survivorship
- life-expectancy
- actuarial
stage: advanced
status: validated
---

# Life Tables

## Core Idea
A life table traces the mortality experience of a cohort — real or synthetic — from birth (or any starting age) to extinction, converting age-specific death rates into a comprehensive model of survivorship. Its columns include the probability of dying in each age interval (qx), the number surviving to each age (lx), person-years lived (Lx), cumulative person-years remaining (Tx), and life expectancy at each age (ex). Period life tables use current age-specific mortality rates applied to a hypothetical cohort; cohort life tables follow an actual birth cohort through time. Life tables are the central analytic tool in demography, actuarial science, and epidemiology, transforming a set of age-specific rates into interpretable summary measures like life expectancy at birth.

## How It's Best Learned
Build a complete abridged life table by hand from age-specific death rates for a real country. Working through each column — converting rates to probabilities, computing survivors, person-years, and finally life expectancy — makes the logic transparent. Then compare your table to one from a country with very different mortality patterns.

## Common Misconceptions
- Life expectancy at birth does not mean most people die at that age — it is an average heavily influenced by infant and child mortality. In populations with high child mortality, most adults who survive childhood live well beyond the life expectancy at birth.
- Period life tables describe a hypothetical cohort experiencing current mortality rates for its entire life; they do not predict how long anyone actually born today will live, since mortality rates will change.

## Questions

```yaml
- question: "A country has a life expectancy at birth of 55 years but a life expectancy at age 5 of 65 years. What explains this apparent paradox?"
  type: multiple-choice
  options:
    - "The data are inconsistent — life expectancy should always decrease with age"
    - "High infant and child mortality pulls down the average at birth; those who survive early childhood face much lower mortality and can expect to live considerably longer"
    - "Life expectancy at age 5 is calculated differently and is not comparable to life expectancy at birth"
    - "Immigration of healthy adults artificially inflates life expectancy at older ages"
  answer: 1
  explanation: "Life expectancy at birth is an average across all members of the hypothetical cohort, including those who die in infancy and childhood. When early-life mortality is high, it drags the average down substantially. Conditional on surviving to age 5, the remaining life expectancy (e5) can be considerably higher than e0 because the high-risk early years have been survived. This is why historical populations with e0 of 35-40 years still had many people living into their 60s and 70s."

- question: "A period life table predicts how long people born in a given year will actually live."
  type: true-false
  answer: false
  explanation: "A period life table applies the age-specific mortality rates observed in a single year (or period) to a hypothetical cohort, showing what would happen if those rates persisted unchanged for a lifetime. Since mortality rates typically improve over time, period life expectancy at birth usually underestimates how long newborns will actually live. Cohort life tables, which follow a real birth cohort and use the actual mortality rates they experience at each age, provide a better (but retrospective) measure of true longevity."

- question: "Describe the relationship between qx (probability of dying), lx (survivors), and ex (life expectancy) in a life table, and explain why ex can increase from one age to the next in some populations."
  type: short-answer
  answer: "qx is the probability of dying in the interval starting at age x; it converts age-specific death rates into probabilities. lx tracks how many of the original cohort (typically 100,000) survive to exact age x — each lx is derived by applying the previous age's qx to the previous lx. ex is the average remaining years of life for those who reach age x, computed from cumulative person-years lived (Tx) divided by survivors (lx). ex can increase from birth to age 1 or 5 in populations with high infant/child mortality because surviving the dangerous early years removes a major source of mortality, increasing the conditional expectation of remaining life."
  explanation: "The mathematical structure of the life table makes this counterintuitive result inevitable when early-age mortality is high. The key insight is that ex is conditional on survival to age x — it asks 'given that you made it this far, how much longer can you expect to live?' When the hazard of dying is concentrated in early life, making it past that gauntlet substantially improves your outlook."
```

## Explainer

You already know how to compute age-specific death rates — deaths in an age group divided by the mid-year population in that group. The life table takes a full set of these rates and transforms them into a model of how a cohort lives and dies across the entire age range. It is, in essence, a bookkeeping device that converts observed mortality rates into the survival experience of a population.

The construction proceeds through a series of linked columns. Start with **nMx**, the age-specific death rate for the interval from age x to x+n. Convert this to **nqx**, the probability of dying in that interval, using a formula that accounts for the distribution of deaths within the interval. Apply nqx to the number of survivors at the start of the interval (**lx**, starting from a conventional radix of 100,000 at birth) to get the number dying (**ndx**) and the number surviving to the next age (**lx+n**). Compute person-years lived in the interval (**nLx**) by accounting for when within the interval deaths occur. Sum person-years from age x onward to get **Tx**. Finally, divide Tx by lx to get **ex**, life expectancy at age x — the average number of years remaining for someone who has survived to exact age x.

The most commonly cited output is **e0**, life expectancy at birth. But e0 can be profoundly misleading if interpreted as "the age at which most people die." In historical populations where infant mortality was 200-300 per 1,000, e0 might be 35 years, yet a person who survived to age 20 might expect to live to 55 or 60. The life table makes this transparent: **e5** or **e20** shows the conditional expectation of remaining life for those who survived the dangerous early years. In populations with concentrated early-age mortality, ex actually *increases* from birth to age 1 or 5 — a result that surprises students but follows directly from the mathematics.

A critical distinction separates **period** and **cohort** life tables. A period life table takes the age-specific mortality rates observed in a single calendar year and applies them to a hypothetical cohort, as if those rates would persist unchanged forever. A cohort life table follows an actual birth cohort through time, using the mortality rates they really experienced at each age. Period tables are available immediately; cohort tables can only be completed after the last member of the cohort has died. Since mortality generally improves over time, period life expectancy at birth typically *underestimates* how long people born that year will actually live — a systematic bias that matters for pension planning and policy projections.
