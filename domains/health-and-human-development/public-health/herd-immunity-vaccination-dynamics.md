---
id: herd-immunity-vaccination-dynamics
title: Herd Immunity and Vaccination Dynamics
domain: health-and-human-development
course: public-health
prerequisites:
- id: basic-reproduction-number
  type: hard
- id: outbreak-transmission-models
  type: hard
builds-toward:
- vaccine-effectiveness-evaluation
tags:
- vaccination
- immunity
- transmission
- coverage-threshold
- r0
stage: advanced
status: draft
---

# Herd Immunity and Vaccination Dynamics

## Core Idea
Herd immunity occurs when sufficient population immunity prevents pathogen transmission, protecting unvaccinated individuals. The vaccination coverage needed to interrupt transmission depends on a pathogen's basic reproduction number (R₀); higher R₀ pathogens require higher vaccination coverage. Understanding herd immunity dynamics guides vaccine distribution strategies, coverage targets, and interpretation of outbreaks in vaccinated populations.

## How It's Best Learned
Use mathematical models to calculate vaccination coverage needed for herd immunity at different R₀ values. Compare actual vaccination coverage in countries to predicted thresholds for different diseases.

## Common Misconceptions
Herd immunity means zero transmission rather than prevention of sustained transmission. Herd immunity threshold is universal across populations rather than depending on R₀. Confusing herd immunity with individual protection from vaccination.

## Explainer

From your study of the basic reproduction number and transmission models, you know that R₀ describes how many people one infectious individual infects in a fully susceptible population. R₀ is the theoretical ceiling — what happens when everyone is susceptible. In reality, some fraction of the population is already immune (from prior infection or vaccination), and those immune individuals cannot transmit the pathogen onward. The **effective reproduction number** (Rₑ) at any moment equals R₀ multiplied by the fraction of the population that is still susceptible: Rₑ = R₀ × (1 − p), where p is the proportion immune. For a disease to spread, Rₑ must exceed 1. For transmission chains to die out on their own, Rₑ must fall below 1.

Setting Rₑ < 1 and solving gives the **herd immunity threshold**: p_c = 1 − (1/R₀). For a pathogen with R₀ = 2, you need 50% immune. For R₀ = 5, you need 80%. For measles, which has one of the highest known R₀ values (12–18 in unvaccinated populations), the threshold is 92–95% — explaining why measles outbreaks recur in communities where vaccination coverage dips even slightly. For polio (R₀ ≈ 5–7), the threshold of 80–85% has proven achievable through sustained vaccination campaigns, enabling eradication in most of the world. This mathematical relationship is why a new pathogen's R₀ estimate — often one of the first epidemiological questions asked during an outbreak — has immediate policy implications: it directly determines the vaccination coverage needed to interrupt transmission.

The public health value of herd immunity extends beyond protecting vaccinated individuals. Those who **cannot** be vaccinated — newborns too young to receive certain vaccines, immunocompromised individuals whose immune systems cannot mount a protective response, and people with specific contraindications — depend entirely on herd immunity for protection. This **indirect protection** is the mechanism behind the ethical argument for vaccination as a social responsibility: your immunity extends a protective umbrella over your most vulnerable community members. When coverage falls below threshold (through vaccine hesitancy, supply disruptions, or access failures), outbreaks disproportionately harm precisely these high-risk groups.

A critical nuance is that the herd immunity threshold assumes **uniform random mixing** across the population — a simplification that rarely holds. People mix preferentially within households, schools, neighborhoods, and social networks. When unvaccinated individuals cluster together (as often happens in communities where vaccine hesitancy is culturally concentrated), local susceptible density can exceed the critical level even when overall population coverage meets the threshold. This is why measles outbreaks can occur in highly vaccinated countries: aggregate national coverage of 93% masks local pockets of 60–70% coverage that are large enough to sustain transmission chains. Understanding herd immunity requires thinking not just about the average but about the spatial and social distribution of immunity — and why equity in vaccination coverage is an epidemiological necessity, not merely a social aspiration.


