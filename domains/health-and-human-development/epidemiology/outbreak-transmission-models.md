---
id: outbreak-transmission-models
title: Mathematical Models of Disease Transmission
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: sir-compartmental-model
  type: hard
- id: seir-model-latency
  type: hard
- id: basic-reproduction-number
  type: hard
tags:
- mathematical-models
- transmission-dynamics
- compartmental-models
stage: expert
status: draft
---

# Mathematical Models of Disease Transmission

## Core Idea
Compartmental models (SIR, SEIR, SIRD) describe disease transmission by tracking individuals in disease states using differential equations to model transitions. Models predict epidemic trajectories, estimate R0, and evaluate intervention effects. Fitting models to observed data allows inference about unobserved transmission dynamics.

## Questions

```yaml
- question: "In an SIR model, the epidemic peak (maximum number of infectious individuals) occurs at which condition?"
  type: multiple-choice
  options:
    - "When the entire susceptible population has been infected"
    - "When the exposed (E) compartment reaches its maximum"
    - "When the fraction of susceptibles S/N equals 1/R₀, so that each case infects exactly one other"
    - "When the recovery rate γ equals the transmission rate β"
  answer: 2
  explanation: "The infectious compartment grows when dI/dt = βSI/N − γI > 0, i.e., when βS/N > γ, or S/N > γ/β = 1/R₀. The peak occurs when dI/dt = 0, which is exactly when S/N = 1/R₀. At that point, each infectious individual infects exactly one other on average — the turning point of the epidemic. After this, S has been depleted below the threshold and the epidemic declines. Option D confuses the condition γ = β (which would mean R₀ = 1, the epidemic threshold) with the peak condition."

- question: "An SIR model has R₀ = 3. A student argues: 'Since R₀ > 1, the epidemic will keep growing until everyone is infected.' What does the model actually predict?"
  type: multiple-choice
  options:
    - "The student is correct — R₀ > 1 guarantees the entire population will eventually be infected"
    - "The epidemic grows initially but peaks and declines once S/N falls to 1/R₀ ≈ 33%, leaving roughly 67% susceptible uninfected"
    - "The epidemic peaks when S/N = 33% but then oscillates indefinitely without ending"
    - "The epidemic declines immediately because the herd immunity threshold has already been reached"
  answer: 1
  explanation: "R₀ > 1 means the epidemic grows initially, but not indefinitely. As infections spread, the susceptible pool S is depleted. When S/N falls to 1/R₀ = 1/3, each case generates exactly one new case — the peak. After the peak, S continues to fall below 1/R₀ and the epidemic declines. The final attack rate (fraction ever infected) is less than 1 — for R₀ = 3, roughly 94% will be infected before the epidemic ends, but this comes from solving the final size equation, not from 'everyone gets it.' The student's intuition confuses 'epidemic grows when R₀ > 1' with 'everyone gets infected.'"

- question: "In an SIR model, an epidemic can peak and decline without any external intervention, even when R₀ > 1."
  type: true-false
  answer: true
  explanation: "The epidemic's own dynamics create the decline: as infections accumulate, susceptibles are converted to recovered individuals, depleting the pool available for new transmission. Once S/N < 1/R₀, the effective reproduction number Rₜ = R₀ × (S/N) falls below 1, and the infectious class begins to shrink. No intervention is needed — the epidemic is self-limiting. This is why all historical epidemics eventually ended even without vaccines or effective treatments."

- question: "Adding an exposed (E) compartment to create an SEIR model increases the epidemic peak size compared to the equivalent SIR model, because more individuals are 'loaded' in the pre-infectious stage before the peak."
  type: true-false
  answer: false
  explanation: "The E compartment (latent period) actually delays and flattens the epidemic curve — it reduces the peak height and shifts it later in time. Individuals in E are infected but not yet infectious, so they slow the rate at which the infectious class I grows. The total attack rate (final epidemic size) is similar, but the peak is lower and later. This is why diseases with longer incubation periods (like COVID-19) tend to produce slower-building, more prolonged outbreaks than diseases with very short latent periods."

- question: "Explain why the transmission term βSI/N in the SIR model causes epidemics to be self-limiting, even without any interventions."
  type: short-answer
  answer: "The term βSI/N is the rate of new infections. It is proportional to S (the number of susceptibles). As the epidemic spreads, individuals move from S to I to R, permanently depleting S. As S shrinks, the product βSI/N decreases — fewer susceptibles means fewer new infections per unit time, even if the number infectious I is still large. Eventually S/N falls below 1/R₀, meaning each infectious case generates fewer than one new case, and the epidemic declines. The epidemic consumes the very fuel (susceptibles) that sustains it."
  explanation: "This self-limiting property is one of the most important insights from compartmental models. It explains why epidemic curves are bell-shaped rather than growing without bound. It also gives rise to the herd immunity threshold: if enough of the population is immune before an outbreak, S/N is already below 1/R₀ at the start, and the epidemic cannot grow at all."
```

## Explainer

You already know the SIR and SEIR frameworks as conceptual tools for partitioning a population into disease states. Now the task is to see how those boxes and arrows translate into differential equations that generate quantitative predictions. The SIR model has three rates: β (transmission rate — how quickly susceptibles become infected per infectious contact), γ (recovery rate — the inverse of the average infectious period), and N (population size). The equations are: dS/dt = −βSI/N, dI/dt = βSI/N − γI, dR/dt = γI. Notice that the term βSI/N is the "engine" of the outbreak — it is the product of transmission rate, the fraction susceptible, and the number infectious. As S depletes, this term shrinks, which is why outbreaks eventually peak and decline even without intervention.

The **basic reproduction number** R₀ = β/γ emerges naturally from this structure. R₀ is the expected number of secondary cases generated by one infectious individual in a fully susceptible population. When R₀ > 1, dI/dt is initially positive — the epidemic grows. When R₀ < 1, the infectious class declines immediately — the pathogen cannot sustain transmission. The epidemic peak occurs when S/N = 1/R₀, the point where each case on average infects exactly one other. The herd immunity threshold (1 − 1/R₀) tells you what fraction of the population must be immune to prevent growth — it is derived directly from the condition that R₀ × (fraction susceptible) < 1.

The **SEIR model** adds an exposed (E) compartment to capture the **latent period** — the window between infection and infectiousness. For diseases like COVID-19, influenza, or measles, individuals spend days in E before entering I. Adding E slows the epidemic curve, reduces the peak, and delays it in time. SIRD extends the model by separating deaths (D) from recovered individuals, enabling estimates of infection fatality rates. More complex variants add age structure, spatial heterogeneity, vaccination compartments, waning immunity, or multiple transmission routes. Each addition increases realism but also multiplies parameters, requiring more data to identify.

**Fitting models to outbreak data** is how the parameters are estimated in practice. When an epidemic begins, you observe reported cases over time, but the true infection curve is broader and earlier — many infections are undetected, and reporting lags behind infection. By fitting the SIR or SEIR differential equations to the observed curve (using least-squares or maximum likelihood), you can estimate β, γ, and the fraction of infections that are reported. Crucially, this fitting allows you to **infer unobserved dynamics** — the total attack rate, when the peak truly occurred, and how many infections have already happened. Early in an outbreak, model-based estimates of R₀ and the effective reproductive number Rₜ (R₀ adjusted for current susceptibility and interventions) guide decisions about when and how aggressively to intervene. The skill of translating compartmental diagrams into differential equations, fitting them to noisy data, and reading out policy-relevant parameters is the core quantitative contribution of mathematical epidemiology.
