---
id: microbial-growth-kinetics-and-population-dynamics
title: Microbial Growth Kinetics and Population Dynamics
domain: biology
course: microbiology
prerequisites:
- id: bacterial-growth-and-reproduction
  type: hard
- id: exponential-growth-and-decay
  type: hard
builds-toward:
- microbial-ecology-biogeochemical-cycling
- fermentation-pathways-and-end-products
tags:
- growth-kinetics
- population-dynamics
- doubling-time
- growth-phases
stage: formal-systems
status: draft
---

# Microbial Growth Kinetics and Population Dynamics

## Core Idea
Microbial populations exhibit four distinct growth phases: lag phase (adaptation to new conditions, minimal growth), exponential/log phase (constant doubling rate), stationary phase (growth halts due to nutrient limitation or waste accumulation), and death phase (cell lysis and loss of viability). Doubling time varies with temperature, nutrient availability, and pH; faster-growing competitors eventually dominate batch cultures. Population dynamics follow logistic growth models with carrying capacity determined by limiting resources.

## Explainer

From your study of bacterial growth and reproduction, you know that bacteria reproduce by binary fission — one cell becomes two, two become four, four become eight. And from your mathematics prerequisite on exponential growth, you know that this kind of constant-rate doubling produces a characteristic J-shaped curve when plotted over time. **Microbial growth kinetics** applies these principles quantitatively, describing how bacterial populations change in size and why their growth inevitably slows and stops. The central equation is deceptively simple: N(t) = N₀ × 2^(t/g), where N₀ is the starting population, g is the **generation time** (doubling time), and t is elapsed time. Under ideal conditions, *E. coli* doubles every 20 minutes — starting from a single cell, that produces over a billion cells in just 10 hours.

But real bacterial cultures never sustain exponential growth indefinitely, and the **growth curve** tells the full story. When bacteria are inoculated into fresh medium, they first enter a **lag phase** during which cell numbers barely change. The cells are not dormant — they are actively synthesizing the enzymes, ribosomes, and transport proteins needed to exploit the new nutrient environment. The length of the lag phase depends on how different the new conditions are from the old: transfer *E. coli* from glucose to glucose and the lag is minutes; transfer it from glucose to lactose and it must first induce the *lac* operon, extending the lag to an hour or more. Once the necessary machinery is in place, the culture enters **exponential (log) phase**, where cells divide at a constant maximum rate and growth is truly exponential. On a semilogarithmic plot (log of cell number versus time), this phase appears as a straight line whose slope gives the **specific growth rate** (μ), related to doubling time by g = ln(2)/μ.

Exponential growth cannot last because the environment is finite. As nutrients deplete and waste products (acids, alcohols, oxidized compounds) accumulate, the growth rate decelerates and the culture enters **stationary phase** — a dynamic equilibrium where the rate of new cell division roughly equals the rate of cell death. The population has reached the environment's **carrying capacity**, a concept you may recognize from logistic growth models in mathematics. During stationary phase, bacteria activate stress-response programs (the sigma factor RpoS regulon in *E. coli*), shrink in size, thicken their cell walls, and begin degrading nonessential cellular components to scavenge amino acids and energy. Some species form endospores. Eventually, as resources are fully exhausted and toxic byproducts accumulate beyond tolerance, the culture enters the **death phase**, where cells lyse and viable counts decline exponentially — though a subset of persister cells may survive for extended periods.

These growth dynamics have direct practical consequences. In clinical microbiology, understanding growth phases explains why antibiotic susceptibility tests require standardized inoculum densities in log phase — stationary phase cells are physiologically different and often more resistant. In industrial fermentation, the goal is typically to maximize the time a culture spends in the productive growth phase while controlling the transition to stationary phase. The **Monod equation**, μ = μ_max × [S]/(K_s + [S]), describes how the specific growth rate depends on the concentration of the limiting substrate [S], where K_s is the substrate concentration at half-maximal growth rate. This equation — structurally identical to Michaelis-Menten enzyme kinetics — is the quantitative foundation for designing continuous culture systems (chemostats) and predicting competitive outcomes when multiple species vie for the same limiting nutrient.
