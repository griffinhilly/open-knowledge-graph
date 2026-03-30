---
id: population-projections
title: Population Projections
domain: social-sciences
course: demography
prerequisites:
- id: life-tables-demography
  type: hard
- id: fertility-measures
  type: hard
- id: migration-theory-demography
  type: soft
builds-toward:
- stable-population-theory
- population-and-environment
tags:
- projection
- cohort-component
- scenarios
- UN-projections
stage: advanced
status: validated
---

# Population Projections

## Core Idea
Population projections calculate future population size, age structure, and composition by applying assumed future rates of fertility, mortality, and migration to a current population. The cohort-component method — the standard approach — advances each age-sex group forward in time by applying age-specific survival rates, adds newborns using age-specific fertility rates, and adjusts for net migration. Projections are not predictions; they are conditional statements — "if fertility, mortality, and migration follow these assumed paths, then the population will be X." The UN produces projections under multiple variants (low, medium, high, constant-fertility) to bracket uncertainty. Projection accuracy depends critically on assumptions about future fertility, which is the most uncertain and consequential component.

## How It's Best Learned
Build a simplified cohort-component projection by hand: start with a population distributed across 5-year age groups, apply survival ratios and fertility rates for one projection interval (5 years), and observe how the age structure transforms. Then vary the fertility assumption and see how dramatically the projected population diverges after just a few intervals.

## Common Misconceptions
- Population projections are not forecasts or predictions — they are scenarios conditional on explicit assumptions. The UN's "medium variant" is widely treated as a forecast, but it is the midpoint of a range, not a best guess about what will happen.
- Long-range projections (50+ years) are inherently uncertain, especially regarding fertility. Small differences in TFR assumptions compound dramatically over decades, producing enormous divergence between high and low variants.

## Questions

```yaml
- question: "Two population projections differ only in their fertility assumption: one uses a TFR of 2.1 and the other uses 1.6. After 50 years, the populations differ by billions. What explains this extreme sensitivity?"
  type: multiple-choice
  options:
    - "The projection models are mathematically unstable and produce unreliable results over long time horizons"
    - "Compounding: each generation born under different fertility assumptions produces a differently-sized next generation, and the difference grows exponentially over multiple generations"
    - "The TFR difference of 0.5 is unusually large; smaller differences would produce negligible divergence"
    - "Mortality and migration assumptions cancel out the fertility difference, so the divergence must be due to a modeling error"
  answer: 1
  explanation: "A TFR of 2.1 produces replacement-level growth (roughly stable population), while 1.6 produces each generation 24% smaller than the last. Over 50 years (roughly two generations), the smaller generation produces an even smaller next generation, and the gap compounds. A 0.5 TFR difference is not unusual — the gap between the UN's high and medium variants is often this magnitude — yet it produces fundamentally different population futures. This is why long-range projections must be understood as scenarios, not forecasts."

- question: "The UN's medium-variant population projection represents the most likely future population path."
  type: true-false
  answer: false
  explanation: "The medium variant is the central scenario in a range of projections, not a probability-weighted best estimate. It assumes fertility will converge toward replacement level in most countries, but this assumption could prove too high (if below-replacement fertility persists or deepens) or too low (if fertility rebounds in low-fertility countries). The UN uses probabilistic methods to generate prediction intervals, but the medium variant itself is not a 'most likely' forecast — it is the middle of a distribution of possible outcomes."

- question: "Describe the cohort-component method and explain why fertility assumptions matter more than mortality assumptions for long-range projections."
  type: short-answer
  answer: "The cohort-component method starts with the current population disaggregated by age and sex. For each projection interval, it: (1) applies age-specific survival rates to advance each cohort to the next age group, (2) applies age-specific fertility rates to women of childbearing age to generate new births, and (3) adds or subtracts net migrants by age and sex. Fertility assumptions matter more for long-range projections because they determine how many new people enter the population, and each cohort of newborns generates the next generation. Small fertility differences compound across generations. Mortality assumptions matter less because most of the variation in mortality improvement affects life expectancy at older ages, which changes population size less than differences in the number of births."
  explanation: "This asymmetry is counterintuitive — students often expect mortality to matter more. But adding 10 years of life expectancy at age 70 adds person-years without adding new births. Changing TFR by 0.5 children per woman changes the entire future population because each generation's size determines the next generation's size. The compounding effect of fertility differences is the single most important fact about long-range population projections."
```

## Explainer

From life tables and fertility measures, you have the tools to describe current mortality and fertility patterns. Population projections extend those tools into the future by asking: if current or assumed future rates persist, what will the population look like in 10, 50, or 100 years? The answer is computed through the **cohort-component method**, which is essentially a bookkeeping exercise applied to the demographic balancing equation, disaggregated by age and sex.

Start with the current population arranged in 5-year age-sex groups (e.g., males 0-4, males 5-9, ... , females 0-4, females 5-9, ...). To advance one 5-year interval: apply **age-specific survival ratios** (derived from the projected life table) to move each cohort forward — the males aged 0-4 become the males aged 5-9, reduced by mortality. Apply **age-specific fertility rates** to women in the childbearing ages to compute the number of births, split by sex using the assumed sex ratio at birth, and survive these newborns through the first age interval to produce the 0-4 age group. Add **net migrants** by age and sex. Repeat for each interval. The output is a complete age-sex distribution at each future time point.

The method is mechanically straightforward, but the difficulty lies entirely in the **assumptions**. Three components must be projected: future mortality (how fast will life expectancy improve?), future fertility (will TFR remain below replacement, rise, or fall further?), and future migration (how large and age-distributed will net flows be?). Of these, **fertility is by far the most consequential and the most uncertain**. A difference of 0.5 in TFR — say, 1.6 versus 2.1 — seems small but compounds across generations. Under 2.1, each generation roughly replaces itself; under 1.6, each generation is about 24% smaller than the last. Over 50 years (two generations), this produces dramatically different populations. Mortality improvements, while important for quality of life, typically add years at older ages and have a much smaller effect on total population size.

The United Nations Population Division produces the most widely cited global projections, updated biennially. They publish multiple **variants**: the medium variant assumes fertility converges toward replacement in most countries; the high variant assumes it converges 0.5 children higher; the low variant, 0.5 children lower. The constant-fertility variant shows what happens if current rates persist unchanged. These variants bracket a wide range of possible futures. The medium variant is commonly treated in media and policy as a forecast, but it is more accurately understood as the central scenario in a range of plausible outcomes. Probabilistic projections, which assign probability distributions to future fertility and mortality, offer a more honest representation of uncertainty — the 95% prediction interval for world population in 2100 spans roughly 9 to 12 billion, a range of 3 billion people.
