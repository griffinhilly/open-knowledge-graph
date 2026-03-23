---
id: species-interactions
title: 'Species Interactions: Competition, Predation, Mutualism, and Parasitism'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: community-ecology-intro
  type: hard
- id: natural-selection
  type: soft
- id: coevolution
  type: soft
- id: predator-prey-dynamics
  type: soft
builds-toward:
- keystone-species
- ecological-succession
- trophic-levels-and-food-webs
tags:
- competition
- predation
- mutualism
- parasitism
- commensalism
stage: formal-systems
status: validated
---
# Species Interactions: Competition, Predation, Mutualism, and Parasitism

## Core Idea
Species interact in ways classified by their effects on each participant: competition (−/−) reduces fitness of both; predation and parasitism (+/−) benefit one and harm the other; mutualism (+/+) benefits both; commensalism (+/0) benefits one with no effect on the other. Competitive exclusion (Gause's principle) states that two species competing for identical resources cannot coexist indefinitely. Resource partitioning and character displacement allow ecologically similar species to coexist by specializing on different niches.

## How It's Best Learned
Use Lotka-Volterra competition equations to predict competitive exclusion vs. coexistence outcomes based on interspecific and intraspecific competition coefficients. Study empirical examples of character displacement (e.g., Darwin's finch beak size) as evidence for competition structuring communities.

## Common Misconceptions
- Mutualism is not always obligate — many mutualistic associations are facultative and context-dependent.
- Competitive exclusion is a theoretical limit; in practice, environmental heterogeneity and disturbance prevent it in many systems.
- Parasites are not always detrimental at the community level — parasitism can regulate dominant competitors and maintain biodiversity.

## Questions

```yaml
- question: "Two bird species feed on the same insects in the same forest. Over evolutionary time, one species specializes on canopy insects while the other specializes on forest-floor insects. This pattern is best explained by:"
  type: multiple-choice
  options: ["Competitive exclusion driving one species to local extinction", "Resource partitioning reducing niche overlap and enabling coexistence", "Mutualistic coevolution between the two bird species", "Predator-prey dynamics separating their foraging zones"]
  answer: 1
  explanation: "Resource partitioning is the division of a shared resource along some axis (space, time, prey size, etc.) that reduces competitive overlap and allows ecologically similar species to coexist. This is distinct from competitive exclusion (where one species is eliminated) and mutualism (where both species benefit from the interaction)."

- question: "Parasitism always harms the host population and is therefore always detrimental to ecosystem biodiversity."
  type: true-false
  answer: false
  explanation: "Parasites can maintain biodiversity by preferentially infecting dominant competitor species, preventing competitive exclusion and freeing resources for subordinate species. Parasitism that regulates the most abundant host can act as a stabilizing force in communities, increasing species diversity rather than decreasing it."

- question: "What is Gause's competitive exclusion principle, and why does it not strictly apply in most real ecosystems?"
  type: short-answer
  answer: "Gause's principle states that two species competing for identical resources in a constant, homogeneous environment cannot coexist indefinitely — one will exclude the other. It does not strictly apply in real ecosystems because environmental heterogeneity, disturbance, and niche partitioning prevent any species from fully and permanently out-competing another."
  explanation: "The principle assumes constant, identical environments where competitive advantages are fixed. Real environments vary in space and time, creating shifting competitive landscapes where different species have advantages under different conditions. This allows many species with overlapping niches to coexist through mechanisms like the storage effect, frequency-dependent selection, and spatial refuges."
```

## Explainer

Communities are not just collections of species — they are networks of interactions that shape population sizes, evolutionary trajectories, and ecosystem structure. Building on what you know about natural selection and population dynamics, this topic classifies species interactions by their fitness consequences and explores how they structure ecological communities.

The standard classification uses a two-symbol notation for each interacting species: (+) if the interaction increases fitness, (−) if it decreases it, and (0) if it has no effect. Competition (−/−) reduces both species' fitness through shared resource depletion or interference. Predation and parasitism (+/−) benefit one organism and harm the other. Mutualism (+/+) benefits both partners. Commensalism (+/0) benefits one species with no measurable effect on the other. These categories are useful but simplified — the sign of an interaction can shift with environmental context, population density, and evolutionary history.

Competition is particularly important for community structure. Gause's competitive exclusion principle predicts that two species competing for completely identical resources cannot coexist indefinitely in a stable, uniform environment — one will have even a slight advantage and drive the other to local extinction. In practice, complete niche overlap is rare. Resource partitioning — the division of resources along some dimension — reduces overlap and enables coexistence. A striking evolutionary outcome is character displacement: when two ecologically similar species co-occur, selection favors individuals that differ more from the competitor, gradually pushing the species' niches further apart. Darwin's finches in the Galápagos show this pattern in beak morphology, with species that co-occur on islands showing greater beak divergence than those found in isolation.

Predation and parasitism drive coevolutionary arms races: prey evolve defenses (camouflage, toxins, warning coloration), while predators evolve counter-adaptations (better detection, venom, cooperative hunting). An important community-level insight is that predators and parasites are not simply negative forces — they can be biodiversity engineers. By preferentially targeting dominant competitor species, they free resources for subordinate species that would otherwise be excluded. Remove a keystone predator and communities often simplify dramatically, as seen with the reintroduction of wolves to Yellowstone.

Mutualism is often presented as straightforward cooperation, but the evolutionary logic is subtler. A mutualistic interaction is maintained because each partner currently gains more from the interaction than it costs. When that cost-benefit balance shifts — for example, if one partner becomes so common that the other can get the benefit without reciprocating — the mutualism can degrade into commensalism or even parasitism. Many mutualisms are therefore conditional and facultative rather than obligate partnerships, and understanding them requires thinking about the economics of cooperation under varying ecological conditions.
