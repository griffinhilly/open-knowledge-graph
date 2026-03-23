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
builds-toward: []
tags:
- transmission-rate
- contact-patterns
- age-specific-risk
stage: expert
status: draft
---
# Force of Infection

## Core Idea
The force of infection (λ) is the per-capita rate at which susceptible individuals become infected, connecting population-level disease frequency to individual infection risk. It integrates contact patterns, pathogen transmissibility, and current pathogen prevalence in the population. Estimating force of infection from serological surveys and longitudinal incidence data reveals age-specific transmission patterns and enables comparison across populations and time periods. Force of infection underpins age-structured transmission models and guides vaccination strategy.

## How It's Best Learned
Estimate force of infection from age-prevalence or age-incidence curves; compare estimates across populations with different transmission intensities.

## Common Misconceptions
Force of infection is the same as the transmission probability for a single contact. It is population-specific and time-dependent.

## Questions

```yaml
- question: "A disease has a per-contact transmission probability of 0.30 and a contact rate of 5 contacts per day with infectious individuals. A researcher claims the force of infection is therefore 0.30. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "The force of infection equals R₀ divided by the infectious period, not the per-contact probability"
    - "Force of infection is not the per-contact transmission probability; it integrates contact rate, per-contact probability, and current prevalence of infection in the population"
    - "The force of infection must be dimensionless, so it cannot equal a probability"
    - "The per-contact probability of 0.30 should first be converted to an odds ratio"
  answer: 1
  explanation: "In the standard SIR model, force of infection λ = β × I/N, where β combines the contact rate and per-contact transmission probability, and I/N is the current prevalence. The per-contact probability (q = 0.30) is only one component. Even with the same per-contact probability, λ will be high when many people are currently infected (high I/N) and low when few are (e.g., late in the epidemic or with high vaccine coverage). The researcher has confused a fixed biological parameter (q) with a population-level, time-varying rate (λ)."

- question: "A cross-sectional seroprevalence survey finds that antibody positivity to a childhood virus rises steeply between ages 1–5 and plateaus near 95% by age 8. What does this pattern most directly reveal about the force of infection?"
  type: multiple-choice
  options:
    - "The force of infection increases with age — older children are at higher risk than younger ones"
    - "The force of infection is high in early childhood, concentrating most transmission among young children"
    - "The attack rate is 95%, implying this is a highly lethal infection"
    - "The virus was introduced into the population approximately 8 years ago"
  answer: 1
  explanation: "Under a catalytic model with constant force of infection λ, the proportion susceptible at age a is e^(-λa) — an exponential decay. A steep rise in seroprevalence during ages 1–5 means the probability of remaining susceptible falls quickly in those years, which requires a high λ in that age range. Near-complete seropositivity by age 8 means almost all susceptibles have been infected by then. This pattern is characteristic of diseases transmitted mainly in daycare and school settings (measles, varicella before vaccination), where young children have high contact rates. The pattern directly informs the optimal age for vaccination."

- question: "The force of infection λ remains constant throughout the course of an epidemic in the classic SIR model."
  type: true-false
  answer: false
  explanation: "In the SIR model, λ = βI/N. As the epidemic progresses, I — the number of currently infectious individuals — rises to a peak and then falls as infected individuals recover. λ therefore rises from near zero (early epidemic, few infectious individuals), peaks at the epidemic peak, and declines as the pool of susceptibles is depleted and infectious individuals recover. This dynamic trajectory of λ over time is precisely what produces the characteristic bell-shaped incidence curve. A constant λ would produce an exponential rise in cases with no natural peak."

- question: "The force of infection can be estimated from age-seroprevalence data using the catalytic model, in which the probability of remaining susceptible at age a is approximately e^(−λa) under a constant force of infection."
  type: true-false
  answer: true
  explanation: "The catalytic model treats infection as a continuous hazard process: a susceptible person faces a constant rate λ of becoming infected per unit time. Survival analysis gives the probability of escaping infection to age a as e^(-λa). Equivalently, the expected proportion seropositive at age a is 1 − e^(-λa). Fitting this curve to observed seroprevalence data by age yields a maximum-likelihood estimate of λ. The rate at which the seroprevalence curve rises with age directly reflects the force of infection. This approach is widely used for estimating pre-vaccination transmission intensity of measles, rubella, and other childhood infections."

- question: "Explain the distinction between force of infection (λ), per-contact transmission probability (q), and the basic reproduction number (R₀), and why correctly distinguishing them matters for vaccine program design."
  type: short-answer
  answer: "Per-contact transmission probability (q) is a biological parameter: the chance of transmission given a single contact between an infectious and a susceptible individual. Force of infection (λ) is a population-level hazard rate: the instantaneous per-capita rate at which susceptibles become infected, which depends on q, the contact rate, and current disease prevalence. R₀ is a threshold parameter at epidemic start in a fully susceptible population: the average number of secondary cases from one case. For vaccine design, λ matters most: because λ varies by age (reflecting age-specific contact rates), age-seroprevalence curves reveal which age groups face the highest infection hazard and therefore benefit most from vaccination — guiding decisions about target age, booster timing, and coverage needed for herd immunity."
  explanation: "Confusing these quantities leads to policy errors. Using q (per-contact risk) as a proxy for λ ignores how prevalence and contact patterns shift the actual infection rate. Using R₀ alone obscures age structure entirely. Estimating λ from serological data is the empirically grounded approach that directly measures who is getting infected and at what rate — the input the vaccine program actually needs."
```

## Explainer

From your work on the SIR compartmental model, you know how epidemic dynamics play out at the population level: susceptibles (S) become infected (I) at a rate that depends on how many infected individuals are present, then recover (R) and gain immunity. The basic reproduction number R₀ tells you whether an outbreak will grow (R₀ > 1) or fade (R₀ < 1) in a fully susceptible population. But R₀ is a summary statistic that collapses many individual-level processes into a single number. The **force of infection** (λ) unpacks one of those processes: it is the per-capita *rate* at which susceptible individuals become infected, measured at a specific moment in time.

Formally, λ is a hazard rate — not a probability but a rate. If a susceptible person faces force of infection λ at time t, then over a small interval Δt, their probability of becoming infected is approximately λΔt. In the classic SIR model with homogeneous mixing, λ = βI/N, where β is the transmission coefficient (combining contact rate and per-contact transmission probability) and I/N is the current prevalence of infection. Notice that λ is not fixed — it rises and falls as the epidemic progresses. When few people are infected, λ is low; at the epidemic peak, λ is highest; as the epidemic burns through susceptibles, λ falls again. This is why incidence curves have the characteristic shape you studied: they follow the trajectory of λ across time.

The real power of the force of infection concept emerges in **age-structured epidemiology**. For many infectious diseases — measles, varicella, mumps before vaccination — the age distribution of past infection (measured by seropositivity in cross-sectional surveys) follows a characteristic pattern: near-zero at birth (maternal antibodies wane), rising steeply through childhood, and reaching near-saturation in adults. By fitting a **catalytic model** to age-seroprevalence data, you can estimate the force of infection at different ages. The model says: a susceptible person aged a has been exposed to force of infection λ continuously since birth; the probability of remaining seronegative at age a is e^(-λa). The rate at which the seroprevalence curve rises with age is λ. This approach reveals not just average transmission intensity but who is most at risk — typically young children with high household and daycare contact rates — and directly guides vaccination program design by identifying the ages where immunization will most efficiently interrupt transmission.

Estimating λ requires distinguishing it precisely from related quantities. The force of infection is not the per-contact transmission probability (call it q), which describes biology at the level of a single exposure. It is not the attack rate, which is cumulative risk over an entire epidemic or outbreak period. It is not R₀, which is a threshold parameter at the epidemic's start in a fully susceptible population. λ is the *instantaneous* per-capita infection hazard facing a susceptible individual right now, in the current population with its current level of immunity and current pathogen prevalence. Estimating it from serological data requires a catalytic model; estimating it from incidence data requires dividing new cases per unit time by the susceptible person-time at risk. Getting these denominators right — knowing how many people were truly susceptible and for how long — is the technical core of the calculation, and errors here (miscounting susceptibles, misclassifying immune individuals) are the main sources of bias in force of infection estimates.
