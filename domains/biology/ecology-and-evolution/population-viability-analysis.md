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
- id: probability-density-functions
  type: hard
- id: age-structured-demographics-and-fecundity
  type: soft
- id: density-dependence-mechanisms
  type: soft
- id: effective-population-size-ne-estimation
  type: soft
- id: population-bottleneck-drift-inbreeding
  type: soft
- id: population-stochasticity-and-extinction
  type: soft
builds-toward:
- extinction-vortex-populations
tags:
- pva
- viability
- predictive-modeling
- extinction-risk
stage: formal-systems
status: validated
---

# Population Viability Analysis and Predictive Modeling

## Core Idea
Population Viability Analysis (PVA) uses demographic and genetic data to predict extinction risk and evaluate conservation strategies. Models incorporate stochastic environmental variation, demographic stochasticity, and genetic effects. PVA identifies minimum viable population sizes and critical management interventions needed to ensure long-term species persistence.

## Questions

```yaml
- question: "A PVA model for a population of 25 condors finds a 40% probability of extinction within 50 years, even though average birth rates exceed death rates. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The model contains an error — positive average growth rates preclude extinction by definition"
    - "Demographic stochasticity — in small populations, random variation in individual outcomes can drive extinction despite favorable averages"
    - "The model is too pessimistic because it omits density-dependent population recovery"
    - "Environmental stochasticity is the only relevant factor; individual-level randomness is negligible at any population size"
  answer: 1
  explanation: "In small populations, demographic stochasticity (randomness in whether individual animals survive or reproduce) dominates. With only 25 birds, a run of bad luck — several females failing to breed, a disease killing a few individuals — can drive the population extinct even when average rates favor growth. In a population of 25,000, individual coin flips average out; in a population of 25, they don't. Option A is the key misconception: average growth rate > 1 does not guarantee persistence in stochastic small-population models."

- question: "The primary output of a Population Viability Analysis is best described as:"
  type: multiple-choice
  options:
    - "A single predicted population size at a specified future date"
    - "The minimum viable population size for the species under current conditions"
    - "A probability of extinction over a specified time horizon, estimated from many stochastic simulations"
    - "The carrying capacity of the habitat given current resource levels"
  answer: 2
  explanation: "PVA runs hundreds or thousands of stochastic simulations incorporating random variation in survival, reproduction, and environmental conditions. The output is a probability — for example, '35% chance of extinction within 100 years under current conditions.' This framing is powerful because it lets managers compare scenarios quantitatively: adding individuals, protecting habitat, or assuming catastrophes each change the extinction probability curve. A single deterministic prediction (option A) would hide exactly the uncertainty that makes PVA valuable."

- question: "A population with an average birth rate exceeding its death rate can seldom go extinct within 100 years, even if it is small."
  type: true-false
  answer: false
  explanation: "This ignores stochasticity. In small populations, demographic stochasticity — the randomness inherent in individual survival and reproduction events — can drive extinction even when average rates favor growth. If only 10 individuals remain and several consecutive bad years occur, the population may hit zero before average rates can rescue it. PVA models quantify this risk precisely by running thousands of stochastic trials, not by extrapolating the average growth rate."

- question: "PVA is more valuable for comparing the extinction probabilities of different management scenarios than for predicting exact extinction dates."
  type: true-false
  answer: true
  explanation: "PVA cannot predict when extinction will occur with precision — its probabilistic estimates depend on data quality and model assumptions. Its real power is comparative: 'translocation of 10 individuals every 5 years reduces the 100-year extinction probability from 35% to 12%.' This makes trade-offs between management options explicit and quantitative. The absolute predictions carry wide uncertainty, but the relative ordering of scenarios is more reliable — which is exactly what conservation managers need to prioritize interventions."

- question: "Why does demographic stochasticity pose a greater extinction risk to a population of 20 individuals than to a population of 20,000, even if both have identical average birth and death rates?"
  type: short-answer
  answer: "Demographic stochasticity refers to randomness in individual-level outcomes — each animal independently has a probability of surviving or reproducing in a given year. In a large population, these individual coin flips average out to the mean rate: random variation in one individual's fate has negligible effect on the whole population trajectory. In a population of 20, individual outcomes dominate — if 3 of 20 breeding females happen to fail this year by chance, that is a 15% reduction in reproduction, potentially catastrophic. The law of large numbers protects large populations from demographic stochasticity but offers no protection to small ones."
  explanation: "This is why minimum viable population estimates typically run into the hundreds to thousands: below a critical size, stochastic extinction overwhelms even favorable average growth rates. Genetic deterioration (inbreeding, loss of heterozygosity) compounds the problem — small populations simultaneously face stochastic extinction risk and genetic erosion, a dynamic called the extinction vortex."
```

## Explainer

You have studied population growth models — exponential and logistic equations that predict how populations change over time given birth and death rates. You also understand age structure and life history, which reveal that not all individuals contribute equally to population growth. And from probability theory, you know how to describe random variation with distributions. **Population Viability Analysis** brings all three together in a single question: given what we know about a species' demography and the uncertainty in its environment, what is the probability that this population will go extinct within a specified time frame?

The core of a PVA is a **stochastic simulation**. Rather than predicting a single deterministic trajectory, the model runs hundreds or thousands of simulations, each incorporating random variation. **Demographic stochasticity** captures the randomness inherent in small populations — whether a particular female breeds this year, how many of her offspring survive. In a population of 10,000, these individual-level coin flips average out. In a population of 20, a run of bad luck can drive the group to extinction even if average birth rates exceed death rates. **Environmental stochasticity** adds year-to-year variation in conditions — droughts, disease outbreaks, harsh winters — that affect the entire population simultaneously. The model draws these random events from probability distributions calibrated to real data, then tracks the population forward through time.

The output is not a single prediction but a **probability of extinction** — for example, "there is a 35% chance this population will go extinct within 100 years under current conditions." This framing is powerful for conservation decision-making because it lets managers compare scenarios: What if we add 10 individuals from another population every five years? What if we protect an additional 500 hectares of habitat? What if a catastrophic flood occurs once per decade? Each scenario produces a different extinction probability curve, making trade-offs between interventions explicit and quantitative.

A key concept emerging from PVA is the **minimum viable population (MVP)** — the smallest population size that has a high probability (often defined as 95%) of persisting for a long period (often 100 years). MVP estimates are not fixed numbers; they depend on the species' life history, the degree of environmental variation, and whether genetic deterioration from inbreeding is included in the model. PVA is not a crystal ball — its predictions are only as good as the demographic data fed into it, and real populations face threats that models may not anticipate. But as a structured way to integrate what we know, quantify uncertainty, and compare management options, it remains one of conservation biology's most important analytical tools.
