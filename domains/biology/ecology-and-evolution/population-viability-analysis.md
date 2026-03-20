---
id: population-viability-analysis
title: Population Viability Analysis and Predictive Modeling
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-age-structure-life-history
  type: hard
- id: population-growth-models
  type: hard
- id: probability-distributions-theory
  type: hard
builds-toward:
- extinction-vortex-populations
tags:
- pva
- viability
- predictive-modeling
- extinction-risk
stage: advanced
status: draft
---

# Population Viability Analysis and Predictive Modeling

## Core Idea
Population Viability Analysis (PVA) uses demographic and genetic data to predict extinction risk and evaluate conservation strategies. Models incorporate stochastic environmental variation, demographic stochasticity, and genetic effects. PVA identifies minimum viable population sizes and critical management interventions needed to ensure long-term species persistence.

## Explainer

You have studied population growth models — exponential and logistic equations that predict how populations change over time given birth and death rates. You also understand age structure and life history, which reveal that not all individuals contribute equally to population growth. And from probability theory, you know how to describe random variation with distributions. **Population Viability Analysis** brings all three together in a single question: given what we know about a species' demography and the uncertainty in its environment, what is the probability that this population will go extinct within a specified time frame?

The core of a PVA is a **stochastic simulation**. Rather than predicting a single deterministic trajectory, the model runs hundreds or thousands of simulations, each incorporating random variation. **Demographic stochasticity** captures the randomness inherent in small populations — whether a particular female breeds this year, how many of her offspring survive. In a population of 10,000, these individual-level coin flips average out. In a population of 20, a run of bad luck can drive the group to extinction even if average birth rates exceed death rates. **Environmental stochasticity** adds year-to-year variation in conditions — droughts, disease outbreaks, harsh winters — that affect the entire population simultaneously. The model draws these random events from probability distributions calibrated to real data, then tracks the population forward through time.

The output is not a single prediction but a **probability of extinction** — for example, "there is a 35% chance this population will go extinct within 100 years under current conditions." This framing is powerful for conservation decision-making because it lets managers compare scenarios: What if we add 10 individuals from another population every five years? What if we protect an additional 500 hectares of habitat? What if a catastrophic flood occurs once per decade? Each scenario produces a different extinction probability curve, making trade-offs between interventions explicit and quantitative.

A key concept emerging from PVA is the **minimum viable population (MVP)** — the smallest population size that has a high probability (often defined as 95%) of persisting for a long period (often 100 years). MVP estimates are not fixed numbers; they depend on the species' life history, the degree of environmental variation, and whether genetic deterioration from inbreeding is included in the model. PVA is not a crystal ball — its predictions are only as good as the demographic data fed into it, and real populations face threats that models may not anticipate. But as a structured way to integrate what we know, quantify uncertainty, and compare management options, it remains one of conservation biology's most important analytical tools.
