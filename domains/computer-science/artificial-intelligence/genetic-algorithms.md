---
id: genetic-algorithms
title: Genetic Algorithms
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: local-search-optimization
  type: soft
tags:
- evolutionary-algorithms
- optimization
- population-based
stage: advanced
status: draft
---

# Genetic Algorithms

## Core Idea
Genetic algorithms maintain a population of candidate solutions and apply crossover and mutation operators to simulate evolution. Fitness-proportionate selection ensures better solutions are more likely to reproduce; a balance between parent selection and genetic variation is essential to avoid premature convergence. Genetic algorithms are population-based methods suitable for discrete and continuous optimization with minimal problem structure required.

## How It's Best Learned
Implement a genetic algorithm for a symbolic regression or function optimization problem, experimenting with population size, crossover, and mutation rates to understand their effects.

## Questions

```yaml
- question: "A genetic algorithm is run for 100 generations on a combinatorial optimization problem. By generation 50, all individuals in the population are nearly identical and the best fitness value has not improved in 30 generations. What has most likely caused this?"
  type: multiple-choice
  options:
    - "The fitness function is poorly designed and does not distinguish good solutions from bad ones"
    - "Selection pressure was too strong, causing premature convergence — the population lost diversity before exploring the search space adequately"
    - "The mutation rate was too high, continuously destroying good solutions"
    - "The crossover rate was too low, preventing offspring from inheriting useful traits"
  answer: 1
  explanation: "When all individuals become nearly identical, the population has converged — diversity is gone. Crossover between identical individuals produces no new information, and without diversity there is no way to escape the local optimum. This premature convergence is the signature failure mode of overly aggressive selection, where high-fitness individuals reproduce so dominantly that the population rapidly homogenizes. Option C (high mutation) would cause the opposite problem — fitness values would be erratic rather than stagnant. The fix involves reducing selection pressure, reintroducing diversity through higher mutation or migration, or using diversity-preserving mechanisms like niching."

- question: "Why are genetic algorithms well-suited for optimization problems where the landscape has many local optima, while gradient-based methods struggle?"
  type: multiple-choice
  options:
    - "Genetic algorithms can compute gradients by comparing fitness values of adjacent solutions, giving them better directional information"
    - "Genetic algorithms maintain a population exploring multiple regions simultaneously, and crossover can jump across valleys between local optima rather than being trapped by local gradient descent"
    - "Genetic algorithms always converge to the global optimum, whereas gradient methods can only find local optima"
    - "Genetic algorithms work faster because they evaluate fewer candidate solutions per iteration"
  answer: 1
  explanation: "Gradient methods follow the gradient downhill (or uphill for maximization) from a single point — once they reach a local optimum, they stop. A GA's population explores many points concurrently, and crossover can recombine partial solutions from different peaks, potentially creating offspring that 'jump' across the valley between local optima. Note that option C is wrong: GAs are not guaranteed to find the global optimum — they are heuristics with no such guarantee. Option D is also wrong: GAs typically require far more fitness evaluations than gradient methods on smooth problems, making them less efficient when gradients are available."

- question: "Maintaining high population diversity in a genetic algorithm helps prevent premature convergence by ensuring multiple distinct regions of the search space are explored simultaneously."
  type: true-false
  answer: true
  explanation: "This is the core reason population-based search outperforms single-point methods on multimodal landscapes. Each individual in the population represents a different candidate solution in a different region of the search space. When crossover combines two diverse individuals, the offspring may land in a new region not yet explored by either parent. If the population converges to near-identical individuals, crossover becomes ineffective (copies crossed with copies produce copies), and only mutation provides any exploration — which at low mutation rates is very slow."

- question: "A higher mutation rate always improves genetic algorithm performance by continuously introducing new genetic material and preventing stagnation."
  type: true-false
  answer: false
  explanation: "Mutation rate controls the exploration-exploitation tradeoff. A very low rate means the algorithm relies almost entirely on recombining existing material — useful for exploiting discovered structure, but slow to explore new regions. A very high rate means good solutions are constantly disrupted before they can be selected and propagated — the search degenerates toward random sampling. Typical effective mutation rates are 0.001–0.01 per gene. The right rate depends on chromosome length, fitness landscape ruggedness, and population size. 'More mutation is always better' is a common misconception."

- question: "Explain the tension between exploitation and exploration in genetic algorithms, and describe how crossover and mutation each contribute to this balance."
  type: short-answer
  answer: "Exploitation means refining and building on solutions already known to be good — converging toward the best-discovered region. Exploration means searching new, unvisited regions — diversifying the population. Too much exploitation leads to premature convergence on a local optimum; too much exploration wastes evaluations on random regions and never refines good solutions. Crossover primarily drives exploitation: it recombines high-fitness parents to create offspring that inherit their good building blocks, concentrating search near already-promising regions. Mutation primarily drives exploration: by randomly flipping genes, it creates occasional novel individuals that extend the search into areas the population has not yet visited. The interplay between these two operators — controlled by crossover and mutation rates, along with selection pressure — determines whether the algorithm effectively navigates the tradeoff."
  explanation: "Recognizing the exploitation-exploration tradeoff is the central insight for using and tuning GAs effectively. It explains why neither 'always crossover' nor 'always mutate' is sufficient — and why elitism (preserving the best individual) helps exploitation without sacrificing the balance, since it guarantees the best-found solution is never discarded."
```

## Explainer

From your study of local search optimization, you know that methods like hill climbing can get trapped in local optima — they improve a single solution step by step but have no mechanism to escape a peak that is not the global best. **Genetic algorithms** (GAs) address this by maintaining an entire **population** of candidate solutions that evolve simultaneously, using mechanisms inspired by biological evolution: selection, crossover, and mutation. The population-based approach provides implicit parallelism — many regions of the search space are explored at once — and the recombination of solutions allows the algorithm to combine good building blocks from different candidates.

The basic cycle works as follows. Each candidate solution is encoded as a **chromosome** — often a binary string, but integer, real-valued, or tree-based representations are common depending on the problem. A **fitness function** evaluates how good each candidate is. **Selection** then chooses parents for the next generation, with higher-fitness individuals more likely to be selected. Common selection methods include tournament selection (pick the best of k random candidates) and roulette-wheel selection (probability proportional to fitness). Selected parents undergo **crossover** (recombination), where portions of two parent chromosomes are exchanged to create offspring — for example, one-point crossover swaps everything after a random position. **Mutation** then randomly perturbs a small fraction of the offspring's genes, introducing fresh genetic material. The new population replaces the old one, and the cycle repeats.

The balance between **exploitation** (refining known good solutions through selection and crossover) and **exploration** (discovering new regions through mutation and population diversity) is the central design challenge. If selection pressure is too strong, the population converges prematurely to a local optimum — all individuals become nearly identical, and crossover produces no new information. If mutation rate is too high, the search becomes essentially random. Typical configurations use moderate selection pressure, crossover rates of 0.6–0.9, and mutation rates of 0.001–0.01 per gene. **Elitism** — always preserving the best individual(s) from one generation to the next — prevents the algorithm from losing its best-known solution and generally improves convergence.

GAs are especially valuable for problems where the search space is large, discrete, multimodal, or poorly understood. Unlike gradient-based methods, they require no derivative information — only the ability to evaluate fitness. This makes them applicable to combinatorial optimization (scheduling, routing), design problems (antenna shapes, circuit layouts), and symbolic regression (evolving mathematical expressions to fit data). The tradeoff is efficiency: GAs typically require many more fitness evaluations than gradient methods on smooth problems, so they are best suited for problems where gradient information is unavailable or the landscape is rugged with many local optima. Understanding when a GA is the right tool — versus simulated annealing, gradient descent, or exhaustive search — is as important as understanding how to tune one.
