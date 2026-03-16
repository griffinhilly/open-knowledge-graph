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

## Explainer

From your study of epidemiologic study designs, you know that controlling for confounding is one of the central challenges of observational research. A case-control study addresses confounding by selecting controls from the same population as cases; a cohort study addresses it by measuring confounders prospectively and adjusting statistically. The **case-crossover design** takes an entirely different approach: instead of selecting different people as controls, it uses each case as their own control. The key insight is that if a person's risk of some acute outcome (a car crash, a heart attack, an asthma exacerbation) varies over time in response to transient exposures, then you can estimate the exposure's effect by comparing what the person was exposed to immediately before the outcome to what they were exposed to during a comparable "control" period when no event occurred.

Consider the classic application: studying whether driving while talking on a cell phone increases crash risk. You recruit people who have just had a car crash. For each person, you ask: were they using a phone in the 10 minutes before the crash (the **hazard window**)? You then ask about their phone use during a reference period — say, the same 10-minute interval on the previous day. Because you are comparing the same person to themselves, all time-invariant characteristics — their driving experience, risk tolerance, visual acuity, vehicle type, regular routes — are automatically held constant. You never need to measure them, because they cannot differ between the hazard and control windows for the same person. This is the design's core strength and the direct solution to confounding by stable personal characteristics that was your prerequisite concern.

The design has specific scope conditions that are important to understand. It is appropriate only when both the exposure and the outcome are **transient** — the exposure should turn on and off (not be chronic), and the outcome should be acute (a discrete event, not a slowly accumulating disease state). Chronic exposures like smoking cannot be studied this way because there is no meaningful variation between the hazard window and reference period. Similarly, outcomes with long latency cannot be studied this way because the causal window is unknown. The case-crossover design is also susceptible to **time-trend bias**: if the background rate of the exposure is changing over time (cell phone use has increased steadily), then comparing last week to this week may confuse a secular trend with a causal effect. Choosing reference periods carefully — often symmetrically before and after the event, or using the same time-of-week in prior weeks — mitigates this. Despite these constraints, the case-crossover design has proven remarkably powerful for studying acute environmental triggers (air pollution and respiratory events), behavioral exposures (physical exertion and cardiac events), and pharmacological exposures (drug initiation and adverse events), precisely because it eliminates the vast space of stable individual confounders that plague conventional between-person designs.
