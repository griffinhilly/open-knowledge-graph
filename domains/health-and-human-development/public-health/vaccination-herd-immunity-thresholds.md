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
stage: abstract-reasoning
status: draft
---

# Vaccination Coverage and Herd Immunity Thresholds

## Core Idea
The vaccination coverage needed to achieve herd immunity is determined by the basic reproduction number (R₀): vaccination threshold = 1 - (1/R₀). Diseases with high R₀ (measles R₀~15) require ~93% population vaccination; diseases with low R₀ (COVID-19 R₀~2-3) require 50-67%. When vaccination coverage falls below this threshold, disease persists in vulnerable unvaccinated populations. Above the threshold, disease cannot sustain itself even in unvaccinated groups. This principle guides vaccination program targets and explains outbreak patterns.

## How It's Best Learned
Calculate herd immunity thresholds for five different diseases with varying R₀ values. Compare to actual vaccination coverage in different countries.

## Common Misconceptions
Thinking high R₀ diseases need uniform vaccination across all populations—actual immunity patterns vary spatially and immunity requirements differ by setting.

## Explainer

From your study of the basic reproduction number, you know that R₀ measures how many secondary infections a single case generates in a fully susceptible population. An epidemic grows when R₀ > 1 and dies out when R₀ < 1. **Herd immunity** is the state where enough of the population is immune — through vaccination or prior infection — that the *effective* reproduction number drops below 1, even though many individuals remain unprotected. The formula connecting R₀ to the vaccination threshold follows directly from this logic: if a fraction *p* of the population is immune, the effective R is R₀ × (1 − p). Setting this equal to 1 and solving gives **p = 1 − 1/R₀**. For measles, with R₀ ≈ 15, this yields a threshold of approximately 93%. For COVID-19, with original variant R₀ ≈ 2.5, the threshold is around 60%.

The reason high R₀ diseases are so demanding becomes intuitive once you think about what R₀ measures: transmission opportunity. Measles is extraordinarily contagious — airborne, viable for hours after an infected person leaves a room, infectious before symptoms appear. Each case, if unvaccinated contacts are available, generates 12–18 new cases. To stop measles from spreading, you must eliminate almost all susceptible contacts from an infected person's transmission network. At 90% vaccination coverage, the 10% who are unvaccinated are still too close together — the virus can find them. Only at 93%+ does the chain of transmission reliably break before it can sustain itself.

The threshold formula assumes uniform, random mixing — in reality, immunity is distributed unevenly across space and social networks. This is why average national coverage can exceed the threshold while outbreaks still occur. **Vaccine-hesitant communities** cluster geographically and socially, creating local pockets where effective vaccination coverage is far below the national average. In a pocket where 60% are vaccinated against measles, the local effective R is 15 × 0.4 = 6 — well above 1. The rest of the population's immunity provides no protection to that cluster because transmission stays within it. This is why surveillance must track not just population-average coverage but **sub-population heterogeneity** — the relevant unit for outbreak risk is the local transmission network, not the country.

When coverage falls below threshold, the burden falls asymmetrically on those who cannot be vaccinated: infants too young to complete the vaccine series, immunocompromised individuals for whom vaccination is contraindicated, and the small fraction for whom vaccines fail to generate immunity. Herd immunity is not a benefit that accrues to the vaccinated — it is a protection that the vaccinated extend to those who cannot protect themselves. Calculating and communicating the threshold is therefore both a technical and an ethical task: it defines the level of community participation required to protect the most vulnerable.

