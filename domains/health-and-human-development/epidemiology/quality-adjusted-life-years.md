---
id: quality-adjusted-life-years
title: Quality-Adjusted Life Years (QALYs)
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: global-burden-of-disease
  type: soft
- id: health-systems-and-financing
  type: soft
builds-toward:
- cost-effectiveness-analysis-epidemiology
tags:
- health-economics
- preference-based-measures
- utility-assessment
stage: advanced
status: draft
---

# Quality-Adjusted Life Years (QALYs)

## Core Idea
QALYs measure health benefit by combining quantity of life (years lived) with quality of life (health-related quality of life or utility). QALY = years × utility weight, where utility reflects individual or population preferences for health states on a 0-1 scale (0 = death, 1 = perfect health). QALYs enable cost-effectiveness analysis by quantifying willingness-to-pay trade-offs. Different methods elicit utility weights (time trade-off, visual analog scale, preference-based instruments like EQ-5D), which substantially affect QALY calculations and cost-effectiveness conclusions.

## Explainer

When a health system or insurer must decide whether to fund a new treatment, it faces a fundamental comparison problem: how do you weigh a treatment that adds two years of life in perfect health against one that adds five years with significant disability? A simple "years of life" metric can't answer this. **Quality-Adjusted Life Years (QALYs)** address it by attaching a **utility weight** to each year lived — a number between 0 (equivalent to death) and 1 (perfect health) — and multiplying: QALY = years × utility. A person who lives 10 years with a utility of 0.6 (say, moderate chronic pain limiting activity) accumulates 6 QALYs. A treatment that raises that utility to 0.8 while extending life by 2 years would generate (12 × 0.8) − (10 × 0.6) = 9.6 − 6 = 3.6 incremental QALYs.

The most contested part of QALY calculation is how utility weights are derived. Three main methods are used. The **visual analog scale (VAS)** asks patients to mark their current health state on a line from 0 to 100 — quick but considered less reliable because it doesn't require trade-offs. The **time trade-off (TTO)** method asks: "How many years in your current health state would you trade for X years in perfect health?" If someone would trade 8 years in their current state for 6 years in perfect health, their utility is 6/8 = 0.75. The **standard gamble** method offers a choice between certain life in the current state versus a gamble with probability p of perfect health and (1−p) of immediate death; the utility equals the probability p at which the person is indifferent. TTO and standard gamble are preference-based and grounded in expected utility theory; VAS is not. Standardized instruments like the **EQ-5D** convert responses to pre-measured utility tariffs from population surveys, allowing consistent comparison across studies.

The QALY framework becomes powerful when combined with cost data in **cost-effectiveness analysis**. The key metric is the **incremental cost-effectiveness ratio (ICER)**: ICER = ΔCost / ΔQALY. If a new cancer drug costs $200,000 more than standard care and generates 2 more QALYs, its ICER is $100,000/QALY. Decision-makers then compare this to a **willingness-to-pay threshold** — in the UK's NICE, roughly £20,000–30,000/QALY; in the US, commonly cited as $50,000–$150,000/QALY. Treatments below the threshold are considered cost-effective; those above require special justification or negotiation.

Despite their utility, QALYs carry important limitations. Utility weights vary across populations: a patient who has adapted to disability may rate their utility higher than a healthy person imagining that state (**disability paradox**). QALYs also treat all years equally regardless of age, which raises equity concerns — a QALY gained by a child effectively counts the same as one gained at age 80. And measurement method matters: TTO, standard gamble, and EQ-5D tariffs for the same health state can differ substantially, producing different ICERs and different funding decisions. Understanding these limitations is essential for critically interpreting cost-effectiveness analyses in health policy discussions.
