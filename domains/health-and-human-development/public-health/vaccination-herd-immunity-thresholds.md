---
id: vaccination-herd-immunity-thresholds
title: Vaccination Coverage and Herd Immunity Thresholds
domain: health-and-human-development
course: public-health
prerequisites:
- id: basic-reproduction-number
  type: hard
- id: herd-immunity-and-vaccination
  type: hard
builds-toward:
- vaccine-effectiveness-evaluation
- outbreak-transmission-models
tags:
- vaccination
- herd-immunity
- immunization
stage: advanced
status: draft
---

# Vaccination Coverage and Herd Immunity Thresholds

## Core Idea
The vaccination coverage needed to achieve herd immunity is determined by the basic reproduction number (R₀): vaccination threshold = 1 - (1/R₀). Diseases with high R₀ (measles R₀~15) require ~93% population vaccination; diseases with low R₀ (COVID-19 R₀~2-3) require 50-67%. When vaccination coverage falls below this threshold, disease persists in vulnerable unvaccinated populations. Above the threshold, disease cannot sustain itself even in unvaccinated groups. This principle guides vaccination program targets and explains outbreak patterns.

## How It's Best Learned
Calculate herd immunity thresholds for five different diseases with varying R₀ values. Compare to actual vaccination coverage in different countries.

## Common Misconceptions
Thinking high R₀ diseases need uniform vaccination across all populations—actual immunity patterns vary spatially and immunity requirements differ by setting.

## Questions

```yaml
- question: "Measles has R₀ ≈ 15 and polio has R₀ ≈ 5. What vaccination thresholds are required for herd immunity against each, and what does the difference reveal?"
  type: multiple-choice
  options:
    - "Measles: ~50%, Polio: ~20%; the threshold is proportional to R₀"
    - "Measles: ~93%, Polio: ~80%; more transmissible diseases require dramatically higher coverage"
    - "Measles: ~93%, Polio: ~80%; the gap is small because both are vaccine-preventable"
    - "Both require ~95% because public health programs target a uniform high standard"
  answer: 1
  explanation: "Using p = 1 − 1/R₀: measles threshold = 1 − 1/15 ≈ 93%; polio threshold = 1 − 1/5 = 80%. The formula reveals why transmissibility matters so much: a small increase in R₀ requires a dramatically larger coverage increase near the top. The gap between 80% and 93% coverage seems modest, but in large populations it represents millions of unvaccinated individuals — and for measles, those 7% unvaccinated are enough to sustain chains of transmission if clustered."

- question: "A country achieves 95% vaccination coverage against measles (R₀ ≈ 15, threshold ≈ 93%), yet a localized outbreak occurs in one region. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The vaccine has lost effectiveness due to a new measles variant that evades immunity"
    - "The 95% national average masks local clustering of unvaccinated individuals whose effective coverage falls below the threshold"
    - "Measles requires 100% coverage because the R₀ formula underestimates its true transmissibility"
    - "Herd immunity only works for diseases with R₀ below 10; measles is too transmissible to be controlled this way"
  answer: 1
  explanation: "The herd immunity threshold formula assumes uniform mixing — that immune and susceptible individuals are randomly distributed. In reality, vaccine-hesitant communities cluster geographically and socially. A community with 60% coverage against measles has a local effective R of 15 × 0.4 = 6 — well above 1, sustaining an outbreak even when the national average exceeds the threshold. Surveillance must track sub-population heterogeneity, not just national averages."

- question: "Herd immunity from vaccination primarily benefits the vaccinated individuals by reducing their risk of exposure."
  type: true-false
  answer: false
  explanation: "This gets the ethical logic backwards. Vaccinated individuals are directly protected by their own immunity — herd immunity is the additional protection that the vaccinated extend to those who cannot be vaccinated: infants too young for the vaccine series, immunocompromised individuals for whom vaccination is contraindicated, and the small fraction for whom vaccines fail to generate protective immunity. Herd immunity is not a benefit for those who chose vaccination; it is a public good created by that choice, protecting the most vulnerable members of the community."

- question: "As a disease's R₀ increases, the vaccination threshold increases proportionally — a disease with R₀ = 10 needs twice the coverage of one with R₀ = 5."
  type: true-false
  answer: false
  explanation: "The relationship is not proportional because of the formula p = 1 − 1/R₀. For R₀ = 5: threshold = 80%. For R₀ = 10: threshold = 90%. The ratio of thresholds (90/80 = 1.125) is far less than the ratio of R₀ values (10/5 = 2). The threshold converges toward 100% asymptotically as R₀ increases — doubling R₀ does not double the threshold, but it does shrink the margin for error at already high coverage levels."

- question: "Why does average national vaccination coverage above the herd immunity threshold not guarantee that no outbreaks will occur? What does this imply for surveillance?"
  type: short-answer
  answer: "The herd immunity threshold formula assumes random, uniform mixing throughout the population. When vaccination coverage is spatially or socially clustered — as it is when vaccine hesitancy concentrates in specific communities — the local effective R within unvaccinated clusters can far exceed 1 even when the national average is above the threshold. An unvaccinated community of 40% within a nationally 95%-vaccinated country can sustain transmission entirely within itself. This implies that surveillance must track sub-population coverage and identify clusters of under-vaccination, not just monitor national-average statistics."
  explanation: "The practical consequence is that outbreak investigation focuses on geographic and demographic clustering of susceptibles, not national coverage trends. Reaching the 'hard-to-reach' unvaccinated communities is disproportionately important for outbreak prevention because those communities create the local transmission networks where R > 1."
```

## Explainer

From your study of the basic reproduction number, you know that R₀ measures how many secondary infections a single case generates in a fully susceptible population. An epidemic grows when R₀ > 1 and dies out when R₀ < 1. **Herd immunity** is the state where enough of the population is immune — through vaccination or prior infection — that the *effective* reproduction number drops below 1, even though many individuals remain unprotected. The formula connecting R₀ to the vaccination threshold follows directly from this logic: if a fraction *p* of the population is immune, the effective R is R₀ × (1 − p). Setting this equal to 1 and solving gives **p = 1 − 1/R₀**. For measles, with R₀ ≈ 15, this yields a threshold of approximately 93%. For COVID-19, with original variant R₀ ≈ 2.5, the threshold is around 60%.

The reason high R₀ diseases are so demanding becomes intuitive once you think about what R₀ measures: transmission opportunity. Measles is extraordinarily contagious — airborne, viable for hours after an infected person leaves a room, infectious before symptoms appear. Each case, if unvaccinated contacts are available, generates 12–18 new cases. To stop measles from spreading, you must eliminate almost all susceptible contacts from an infected person's transmission network. At 90% vaccination coverage, the 10% who are unvaccinated are still too close together — the virus can find them. Only at 93%+ does the chain of transmission reliably break before it can sustain itself.

The threshold formula assumes uniform, random mixing — in reality, immunity is distributed unevenly across space and social networks. This is why average national coverage can exceed the threshold while outbreaks still occur. **Vaccine-hesitant communities** cluster geographically and socially, creating local pockets where effective vaccination coverage is far below the national average. In a pocket where 60% are vaccinated against measles, the local effective R is 15 × 0.4 = 6 — well above 1. The rest of the population's immunity provides no protection to that cluster because transmission stays within it. This is why surveillance must track not just population-average coverage but **sub-population heterogeneity** — the relevant unit for outbreak risk is the local transmission network, not the country.

When coverage falls below threshold, the burden falls asymmetrically on those who cannot be vaccinated: infants too young to complete the vaccine series, immunocompromised individuals for whom vaccination is contraindicated, and the small fraction for whom vaccines fail to generate immunity. Herd immunity is not a benefit that accrues to the vaccinated — it is a protection that the vaccinated extend to those who cannot protect themselves. Calculating and communicating the threshold is therefore both a technical and an ethical task: it defines the level of community participation required to protect the most vulnerable.

