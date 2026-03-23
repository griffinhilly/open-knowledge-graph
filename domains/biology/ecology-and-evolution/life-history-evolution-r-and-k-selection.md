---
id: life-history-evolution-r-and-k-selection
title: 'Life History Evolution: r-Selection and K-Selection'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: life-history-strategies
  type: hard
- id: population-growth-models
  type: soft
builds-toward:
- age-structured-demographics-and-fecundity
- population-regulation
tags:
- life-history
- r-k-selection
- evolution
- strategy
stage: formal-systems
status: draft
---

# Life History Evolution: r-Selection and K-Selection

## Core Idea
Life history traits evolve under selection and vary with environmental conditions. In unstable or resource-rich environments, r-selected species maximize growth rate through early maturation, high fecundity, and short lifespans. In stable or resource-limited environments, K-selected species maximize competitive ability through late maturation, low fecundity, and long lifespans. Most species lie on a continuum between these extremes.

## Questions

```yaml
- question: "A volcanic eruption destroys a forest and creates a large expanse of bare substrate with abundant sunlight and nutrients. Which type of species would you expect to colonize successfully first?"
  type: multiple-choice
  options:
    - "K-selected species, because their large body size gives them a competitive advantage for claiming territory"
    - "r-selected species, because they reproduce rapidly and can exploit an uncrowded, resource-rich environment before competition intensifies"
    - "K-selected species, because their long lifespans allow them to persist until conditions fully stabilize"
    - "r-selected species, because they invest heavily in parental care, maximizing each offspring's survival in uncertain conditions"
  answer: 1
  explanation: "After disturbance, the environment is well below carrying capacity — resources are abundant and competition is minimal. This is exactly the environment r-selection favors. r-selected species reproduce quickly, produce many offspring with minimal investment, and colonize rapidly before the space fills. Note that option D gets the logic backwards: r-selected species invest little in each offspring, not a lot. The strategy succeeds because producing many cheap offspring captures temporary abundance — most die, but enough survive to exploit it."

- question: "Which scenario best illustrates a K-selected life history strategy?"
  type: multiple-choice
  options:
    - "A mosquito that lays hundreds of eggs in standing water and completes its life cycle in under two weeks"
    - "A weed that begins flowering within weeks of germination and releases thousands of airborne seeds"
    - "An elephant that gestates for nearly two years, produces a single calf, and provides parental care for over a decade"
    - "A bacterium that divides every 20 minutes under favorable nutrient conditions"
  answer: 2
  explanation: "The elephant exemplifies K-selection: late maturity, single offspring, extended parental investment, long lifespan, and low reproductive rate. This strategy succeeds in environments near carrying capacity where resources are scarce and competition is intense — each offspring must be well-equipped to compete. The other options all exemplify r-selection: high reproductive rate, many small offspring with minimal parental investment, short generation times. K-selection is not about being large or sophisticated generally, but about allocating reproductive effort toward fewer, more competitive offspring."

- question: "r-selected species are evolutionarily inferior to K-selected species because they invest less in each offspring and have shorter lifespans."
  type: true-false
  answer: false
  explanation: "Neither strategy is inherently superior — each is optimal for a specific environmental regime. r-selection is favored when populations are frequently knocked below carrying capacity, where rapid reproduction captures temporary resource abundance. K-selection is favored when populations are near carrying capacity and competition for limiting resources determines fitness. Dandelions are not inferior to elephants; they are optimally adapted to unstable, frequently disturbed environments. Applying the label inferior imports a value judgment that natural selection does not make."

- question: "The letters r and K in r/K selection theory are taken directly from the parameters of the logistic population growth equation."
  type: true-false
  answer: true
  explanation: "This is not coincidental — it is the theoretical foundation of the framework. In the logistic equation, r is the intrinsic rate of increase and K is the carrying capacity. r-selection describes selection that maximizes r when populations are well below K; K-selection describes selection for competitive traits that succeed when populations are near K. The naming directly embeds the population dynamic context that drives the selective pressures, connecting evolutionary life history theory to population ecology."

- question: "Why does the optimal life history strategy depend on environmental conditions rather than being universally fixed? Use the r/K framework to explain."
  type: short-answer
  answer: "In uncrowded environments (population well below K), fast reproduction captures abundant resources before competitors arrive — favoring r-selected traits like early maturation and high fecundity. In crowded environments near K, resources are scarce and every offspring slot is contested, so investing heavily in competitive ability per offspring wins over producing more offspring that cannot compete. Neither strategy is inherently better; fitness depends entirely on which environmental regime the organism faces."
  explanation: "This context-dependence is the central insight of life history theory: evolution does not optimize life histories in the abstract but in relation to specific ecological conditions. The r/K framework makes this explicit by tying selective pressures to the population's position relative to K. Modern life history theory extends this logic further to predict optimal clutch size, age at maturity, and senescence schedules from specific mortality schedules and resource competition parameters, but the core intuition that environment determines what strategy wins remains foundational."
```

## Explainer

From your study of life history strategies, you know that organisms face fundamental trade-offs in how they allocate energy — between growth and reproduction, between many offspring and few, between current reproduction and future survival. The r/K selection framework explains *why* different environments favor different solutions to these trade-offs, connecting the population growth models you already understand to the selective pressures that shape life history evolution.

The names come directly from the logistic growth equation: **r** is the intrinsic rate of increase and **K** is the carrying capacity. In environments where populations are frequently knocked below carrying capacity — by disturbances, seasonal die-offs, or colonization of new habitat — selection favors traits that maximize r. These **r-selected** species reproduce early, produce many small offspring with minimal parental investment, and grow rapidly. Think of dandelions scattering thousands of seeds, or bacteria dividing every twenty minutes. The strategy works because in an uncrowded environment, the lineage that reproduces fastest captures the most resources. Most offspring die, but enough survive to exploit the temporary abundance.

In contrast, environments where populations remain near carrying capacity favor a different strategy. Here, resources are limiting and competition is intense. **K-selected** species invest heavily in each offspring — producing fewer young but providing parental care, larger body size, or better competitive ability. Elephants, with their two-year gestation, single calves, and decades of parental investment, exemplify this end of the continuum. When the environment is full, producing more offspring does not help if none can compete for the scarce resources; instead, the advantage goes to individuals whose offspring are well-equipped to survive in a crowded world.

Most organisms do not sit at either extreme but fall along a continuum, and the same species may shift strategies in different environments or life stages. A forest tree is K-selected relative to a weed, but r-selected relative to a whale. Modern ecology has moved beyond strict r/K dichotomy toward more nuanced life history theory — including demographic models that predict optimal clutch size, age at maturity, and senescence patterns from specific mortality schedules. Still, the r/K framework remains valuable as an intuitive bridge between population dynamics and natural selection: it shows that the "best" life history depends entirely on whether the environment rewards fast reproduction or competitive endurance.
