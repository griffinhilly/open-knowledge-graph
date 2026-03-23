---
id: population-stochasticity-and-extinction
title: Population Stochasticity and Extinction Risk
domain: biology
course: ecology-and-evolution
prerequisites:
- id: effective-population-size
  type: hard
- id: genetic-drift-in-small-populations
  type: hard
builds-toward:
- population-viability-analysis
- conservation-genetics-and-population-recovery
tags:
- stochasticity
- extinction
- small-populations
- risk
stage: formal-systems
status: validated
---

# Population Stochasticity and Extinction Risk

## Core Idea
Small populations are vulnerable to extinction from demographic stochasticity (random birth/death variation), environmental stochasticity, and genetic stochasticity (drift and inbreeding). The extinction vortex describes how small size leads to inbreeding depression and fitness loss, further reducing size. Extinction risk increases nonlinearly as population size decreases. Management must maintain populations above minimum viable sizes to buffer against stochastic events.

## Questions

```yaml
- question: "A population of 20 individuals has a birth rate that exactly equals its death rate — on average, the population is stable. Is this population safe from extinction?"
  type: multiple-choice
  options:
    - "Yes — if births equal deaths on average, the population will remain stable indefinitely"
    - "No — even with balanced average rates, demographic stochasticity can produce enough random variance in a small population to drive it extinct"
    - "Yes — extinction only occurs when death rate exceeds birth rate"
    - "No — but only because inbreeding will eventually reduce fertility"
  answer: 1
  explanation: "Demographic stochasticity is the key insight here. In a population of millions, random variation averages out and the actual rate tracks the expected rate closely. But in a population of 20, chance alone can produce a bad year: maybe 15 deaths and only 5 births — not because conditions worsened, but simply because coin flips come up tails. The expected value (equal birth and death rates) would sustain a large population indefinitely, but variance around that expectation is lethal at small sizes. This is why a stable average is not sufficient to ensure persistence in small populations."

- question: "What is the extinction vortex, and why is it called a 'vortex'?"
  type: multiple-choice
  options:
    - "A rapid environmental catastrophe (flood, fire) that eliminates a small population in a single event"
    - "A positive feedback loop in which small population size causes inbreeding depression, which reduces fitness and shrinks the population further, intensifying inbreeding"
    - "The mathematical spiral shape of a population's size trajectory when plotted over time before extinction"
    - "The geographic phenomenon where habitat fragmentation pulls populations downward toward local extinction"
  answer: 1
  explanation: "The 'vortex' refers to a self-reinforcing feedback loop. Small populations experience unavoidable inbreeding (few mates available), which exposes deleterious recessive alleles and causes inbreeding depression — reduced survival and fertility. This further reduces population size, which intensifies inbreeding, which causes more fitness loss, which shrinks the population again. Each turn of the vortex accelerates the next, making it progressively harder to escape without outside intervention such as genetic rescue (introduction of individuals from other populations). The metaphor captures the downward spiral aspect: unlike simple linear decline, the vortex actively accelerates toward extinction."

- question: "If a population's average birth rate exceeds its average death rate, demographic stochasticity cannot cause it to go extinct."
  type: true-false
  answer: false
  explanation: "False. Even when the average growth rate is positive, demographic stochasticity — random variation in individual birth and death events — can drive a small population to zero. In a population of 10–50 individuals, a run of bad luck (more deaths than births in several consecutive years, or a skewed sex ratio by chance) can eliminate the population entirely before the positive average rate can rescue it. This is mathematically analogous to gambler's ruin: even a gambler who wins slightly more often than they lose can go broke if their bankroll is small enough. Positive average growth only guarantees persistence in the limit of large population size."

- question: "Extinction risk increases nonlinearly as population size decreases — cutting a population in half more than doubles its extinction risk."
  type: true-false
  answer: true
  explanation: "True. At large population sizes, all three forms of stochasticity (demographic, environmental, genetic) have negligible effects — the law of large numbers keeps actual rates close to expected rates, and the population can buffer environmental shocks. As size drops below a threshold, each of these risks begins to matter, and they interact: a population weakened by inbreeding depression is more vulnerable to a bad winter; a genetically impoverished population has less adaptive potential to respond. Below minimum viable population thresholds, multiple stochastic processes act simultaneously and reinforce each other, making extinction risk rise far faster than a linear model would predict."

- question: "Why do conservation biologists emphasize maintaining populations *above* a minimum viable size rather than simply maximizing total numbers? What makes the threshold concept important?"
  type: short-answer
  answer: "Below a threshold population size, stochastic processes — demographic chance events, environmental fluctuations, and genetic deterioration through inbreeding — dominate over the deterministic factors (birth rate, habitat quality) that would otherwise sustain the population. Above the threshold, random bad years can be weathered because the population has enough individuals that variance averages out and inbreeding is rare. Below it, the same random events can eliminate the population, and the extinction vortex can take hold. The threshold concept matters because it means small increases in a critically small population provide disproportionately large reductions in extinction risk — there is a nonlinear relationship between size and safety, not a linear one."
  explanation: "Minimum viable population (MVP) estimates — typically calculated for a 95% probability of persistence over 100 years — give managers concrete targets. The threshold concept also explains why connecting habitat fragments (via corridors) and conducting genetic rescue matter even when total numbers seem adequate: an isolated population of 100 may face greater extinction risk than a connected metapopulation of 25+25+25+25 because connectivity allows demographic and genetic rescue across subpopulations."
```

## Explainer

From your study of effective population size and genetic drift in small populations, you know that smaller populations experience stronger random fluctuations in allele frequencies and lose genetic variation faster. Population stochasticity extends this insight beyond genetics to the full range of random processes that threaten small populations with extinction. The core message is sobering: once a population becomes small enough, randomness alone can kill it, even if the average birth and death rates would sustain a larger population indefinitely.

**Demographic stochasticity** is random variation in individual birth and death events. In a population of millions, the law of large numbers ensures that the actual birth rate closely matches the expected rate. But in a population of twenty, random chance might produce fifteen deaths and only five births in a given year — not because conditions worsened, but simply because coin flips sometimes come up tails. Imagine flipping a fair coin twenty times: you might easily get twelve heads and eight tails, a 60/40 split that would be negligible in a thousand flips but devastating in a tiny population. **Environmental stochasticity** adds another layer: random fluctuations in weather, food supply, disease, or predator pressure that affect all individuals simultaneously. A single bad winter can wipe out a population that was otherwise viable. **Catastrophes** — floods, fires, epidemics — are extreme environmental events that can eliminate populations in one stroke.

**Genetic stochasticity** completes the picture. Small populations lose alleles through drift, reducing adaptive potential. Inbreeding becomes unavoidable when few mates are available, exposing deleterious recessive alleles and causing **inbreeding depression** — reduced survival and fertility. This is where the **extinction vortex** takes hold: a small population suffers inbreeding depression, which reduces fitness, which shrinks the population further, which intensifies inbreeding, which reduces fitness more. Each turn of the vortex accelerates the next, creating a positive feedback loop that is extremely difficult to escape without outside intervention.

The practical consequence is that extinction risk increases **nonlinearly** as population size drops. A population of 10,000 might face negligible stochastic risk; a population of 500 faces moderate risk; a population of 50 faces severe risk from all three forms of stochasticity acting simultaneously. Conservation biologists use **minimum viable population** (MVP) estimates — the smallest population size with a high probability of persisting for a given time horizon — to set management targets. Strategies like genetic rescue (introducing individuals from other populations to restore genetic diversity), habitat corridors (connecting isolated fragments), and captive breeding all aim to push populations above the threshold where stochastic processes dominate, giving deterministic factors like birth rates and habitat quality a chance to sustain the population.
