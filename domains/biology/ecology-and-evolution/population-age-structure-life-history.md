---
id: population-age-structure-life-history
title: Population Age Structure and Life History
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-ecology-intro
  type: hard
- id: population-growth-models
  type: hard
- id: life-history-strategies
  type: soft
builds-toward:
- population-viability-analysis
- conservation-genetics-effective-size
tags:
- age-structure
- life-history
- reproductive-value
stage: advanced
status: draft
---

# Population Age Structure and Life History

## Core Idea
A population's age structure—the proportion of individuals in each age class—determines its growth rate and future trajectory. Populations with more reproductive-age individuals grow faster than those dominated by post-reproductive individuals. Life history traits (age at reproduction, clutch size, lifespan) evolve under selection and vary widely across species, creating a spectrum from r-selected to K-selected strategies.

## Explainer

Population growth models like exponential and logistic growth treat all individuals as identical — every organism has the same probability of reproducing and dying. But real populations are structured: a population of 1,000 deer with 800 fawns and 200 adults will behave very differently from one with 200 fawns and 800 prime-age adults, even though both total 1,000. **Age structure** captures this by dividing the population into age classes and tracking age-specific survival and fertility rates. The tool for visualizing this is the **age pyramid** (or population pyramid): a bar chart where each horizontal bar represents an age class, and the width represents the number of individuals in that class.

The shape of the pyramid tells you where the population is headed. A broad-based pyramid (many juveniles, few old individuals) signals rapid growth — there is a large cohort about to enter reproductive age. A column-shaped pyramid indicates a stable population with roughly equal recruitment and mortality across age classes. An inverted or top-heavy pyramid, with more old individuals than young, signals decline. Critically, age structure creates **population momentum**: even if a rapidly growing population instantly drops its birth rate to replacement level, it will continue growing for decades as its large young cohorts move through reproductive ages. This is why human demographic projections extend 50+ years into the future — today's age structure constrains tomorrow's population size regardless of policy changes.

**Life history theory** asks why organisms differ so dramatically in their age-specific schedules of reproduction and survival. An oak tree produces millions of acorns over centuries; a salmon pours all its energy into a single massive spawning event and dies. These are not random — they are evolved strategies shaped by the ecological pressures you've encountered in population ecology. The classic framework organizes life histories along an **r-K continuum**: r-selected species (high fecundity, small offspring, little parental care, short lifespan) thrive in unpredictable or disturbed environments where rapid reproduction fills empty habitat; K-selected species (low fecundity, large offspring, extensive parental care, long lifespan) dominate stable environments where competition is intense and survival to adulthood matters more than sheer reproductive output.

The r-K framework is a useful heuristic but modern life history theory recognizes it as an oversimplification. Trade-offs are the deeper principle: energy allocated to reproduction cannot also be allocated to growth or survival, and natural selection optimizes the allocation schedule for the organism's specific environment. **Reproductive value** — the expected future reproductive contribution of an individual at a given age — quantifies this: young adults in a long-lived species have high reproductive value because they have many breeding seasons ahead, while the same age class in a short-lived species may already be near the end. Conservation biologists use age-structured models (Leslie matrices) to identify which age class most influences population growth rate, because protecting that class yields the greatest demographic return — often, for large mammals and sea turtles, it is adult survival rather than juvenile recruitment that matters most.
