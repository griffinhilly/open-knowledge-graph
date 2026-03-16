---
id: seir-model-latency
title: SEIR Models Incorporating Latent Periods
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: sir-compartmental-model
  type: hard
tags:
- seir-model
- latent-period
- compartmental-models
- incubation-period
stage: advanced
status: draft
---

# SEIR Models Incorporating Latent Periods

## Core Idea
The SEIR model extends SIR by adding an Exposed (latent) compartment, representing individuals who are infected but not yet infectious. The latent period (1/σ) is the mean duration from infection to infectiousness. SEIR models more accurately represent diseases with substantial latent periods (e.g., tuberculosis, COVID-19) and affect predictions of epidemic dynamics compared to simpler SIR models.

## Explainer

In the SIR model you already know, individuals move directly from Susceptible to Infectious upon exposure — there is no delay. This is a good approximation for diseases where the latent period (time from infection to becoming infectious) is short relative to the generation interval. But for many important pathogens — measles, COVID-19, Ebola, tuberculosis — there is a meaningful gap between the moment of infection and the moment the infected person can transmit. The **SEIR model** inserts a new compartment, **E (Exposed)**, to capture this delay.

The four compartments now represent distinct biological states. **Susceptible (S)** individuals have no immunity. **Exposed (E)** individuals are infected — the pathogen is replicating inside them — but they are not yet producing enough virus or bacterial load to transmit. **Infectious (I)** individuals can transmit. **Removed (R)** individuals are recovered and immune (or dead). The flow is: S → E → I → R. The rate of leaving E is σ (sigma), so the average **latent period** is 1/σ days. The rate of leaving I is γ, so the average **infectious period** is 1/γ days.

The governing differential equations become:
dS/dt = −βSI/N
dE/dt = βSI/N − σE
dI/dt = σE − γI
dR/dt = γI

Notice that β, the transmission rate, still depends on S and I — not S and E, because exposed individuals are not yet infectious. The basic reproduction number R₀ = β/γ is unchanged from SIR: adding the latent period does not change how many people one infectious person ultimately infects, only when.

What the latent period does change is **epidemic timing and speed**. The epidemic curve is stretched out: the initial exponential growth phase is slower because new infections flow through E before becoming infectious, introducing a delay in the feedback loop. The peak occurs later and is slightly lower than a corresponding SIR epidemic with the same R₀. For early warning systems, this matters: there is an unavoidable lag between the start of transmission and the first observed cases, because cases are not visible until they are infectious (and then tested). The size of this lag is approximately 1/σ — knowing the latent period helps you estimate how far ahead of the current case count the epidemic actually is.

The practical importance of SEIR is disease-specific. For influenza, where the latent period is short (~1–2 days), the SIR model is often adequate. For COVID-19, where the latent period averages ~5 days and presymptomatic transmission occurs during the E→I transition, SEIR more accurately captures both the delayed growth and the critical role of asymptomatic or presymptomatic spread. For tuberculosis, the latent period can be years — a feature that requires SEIR extensions that allow reactivation from the E compartment. SEIR is thus not a single model but a family of parameterizable structures; the latent period is one of the most consequential parameters for matching model dynamics to real outbreak data.
