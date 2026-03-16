---
id: force-of-infection
title: Force of Infection
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: basic-reproduction-number
  type: hard
- id: sir-compartmental-model
  type: hard
- id: disease-frequency-measures
  type: soft
builds-toward:
- age-structured-epidemiological-models
tags:
- transmission-rate
- contact-patterns
- age-specific-risk
stage: advanced
status: draft
---

# Force of Infection

## Core Idea
The force of infection (λ) is the per-capita rate at which susceptible individuals become infected, connecting population-level disease frequency to individual infection risk. It integrates contact patterns, pathogen transmissibility, and current pathogen prevalence in the population. Estimating force of infection from serological surveys and longitudinal incidence data reveals age-specific transmission patterns and enables comparison across populations and time periods. Force of infection underpins age-structured transmission models and guides vaccination strategy.

## How It's Best Learned
Estimate force of infection from age-prevalence or age-incidence curves; compare estimates across populations with different transmission intensities.

## Common Misconceptions
Force of infection is the same as the transmission probability for a single contact. It is population-specific and time-dependent.

## Explainer

From your work on the SIR compartmental model, you know how epidemic dynamics play out at the population level: susceptibles (S) become infected (I) at a rate that depends on how many infected individuals are present, then recover (R) and gain immunity. The basic reproduction number R₀ tells you whether an outbreak will grow (R₀ > 1) or fade (R₀ < 1) in a fully susceptible population. But R₀ is a summary statistic that collapses many individual-level processes into a single number. The **force of infection** (λ) unpacks one of those processes: it is the per-capita *rate* at which susceptible individuals become infected, measured at a specific moment in time.

Formally, λ is a hazard rate — not a probability but a rate. If a susceptible person faces force of infection λ at time t, then over a small interval Δt, their probability of becoming infected is approximately λΔt. In the classic SIR model with homogeneous mixing, λ = βI/N, where β is the transmission coefficient (combining contact rate and per-contact transmission probability) and I/N is the current prevalence of infection. Notice that λ is not fixed — it rises and falls as the epidemic progresses. When few people are infected, λ is low; at the epidemic peak, λ is highest; as the epidemic burns through susceptibles, λ falls again. This is why incidence curves have the characteristic shape you studied: they follow the trajectory of λ across time.

The real power of the force of infection concept emerges in **age-structured epidemiology**. For many infectious diseases — measles, varicella, mumps before vaccination — the age distribution of past infection (measured by seropositivity in cross-sectional surveys) follows a characteristic pattern: near-zero at birth (maternal antibodies wane), rising steeply through childhood, and reaching near-saturation in adults. By fitting a **catalytic model** to age-seroprevalence data, you can estimate the force of infection at different ages. The model says: a susceptible person aged a has been exposed to force of infection λ continuously since birth; the probability of remaining seronegative at age a is e^(-λa). The rate at which the seroprevalence curve rises with age is λ. This approach reveals not just average transmission intensity but who is most at risk — typically young children with high household and daycare contact rates — and directly guides vaccination program design by identifying the ages where immunization will most efficiently interrupt transmission.

Estimating λ requires distinguishing it precisely from related quantities. The force of infection is not the per-contact transmission probability (call it q), which describes biology at the level of a single exposure. It is not the attack rate, which is cumulative risk over an entire epidemic or outbreak period. It is not R₀, which is a threshold parameter at the epidemic's start in a fully susceptible population. λ is the *instantaneous* per-capita infection hazard facing a susceptible individual right now, in the current population with its current level of immunity and current pathogen prevalence. Estimating it from serological data requires a catalytic model; estimating it from incidence data requires dividing new cases per unit time by the susceptible person-time at risk. Getting these denominators right — knowing how many people were truly susceptible and for how long — is the technical core of the calculation, and errors here (miscounting susceptibles, misclassifying immune individuals) are the main sources of bias in force of infection estimates.
