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

## Explainer

From your study of local search optimization, you know that methods like hill climbing can get trapped in local optima — they improve a single solution step by step but have no mechanism to escape a peak that is not the global best. **Genetic algorithms** (GAs) address this by maintaining an entire **population** of candidate solutions that evolve simultaneously, using mechanisms inspired by biological evolution: selection, crossover, and mutation. The population-based approach provides implicit parallelism — many regions of the search space are explored at once — and the recombination of solutions allows the algorithm to combine good building blocks from different candidates.

The basic cycle works as follows. Each candidate solution is encoded as a **chromosome** — often a binary string, but integer, real-valued, or tree-based representations are common depending on the problem. A **fitness function** evaluates how good each candidate is. **Selection** then chooses parents for the next generation, with higher-fitness individuals more likely to be selected. Common selection methods include tournament selection (pick the best of k random candidates) and roulette-wheel selection (probability proportional to fitness). Selected parents undergo **crossover** (recombination), where portions of two parent chromosomes are exchanged to create offspring — for example, one-point crossover swaps everything after a random position. **Mutation** then randomly perturbs a small fraction of the offspring's genes, introducing fresh genetic material. The new population replaces the old one, and the cycle repeats.

The balance between **exploitation** (refining known good solutions through selection and crossover) and **exploration** (discovering new regions through mutation and population diversity) is the central design challenge. If selection pressure is too strong, the population converges prematurely to a local optimum — all individuals become nearly identical, and crossover produces no new information. If mutation rate is too high, the search becomes essentially random. Typical configurations use moderate selection pressure, crossover rates of 0.6–0.9, and mutation rates of 0.001–0.01 per gene. **Elitism** — always preserving the best individual(s) from one generation to the next — prevents the algorithm from losing its best-known solution and generally improves convergence.

GAs are especially valuable for problems where the search space is large, discrete, multimodal, or poorly understood. Unlike gradient-based methods, they require no derivative information — only the ability to evaluate fitness. This makes them applicable to combinatorial optimization (scheduling, routing), design problems (antenna shapes, circuit layouts), and symbolic regression (evolving mathematical expressions to fit data). The tradeoff is efficiency: GAs typically require many more fitness evaluations than gradient methods on smooth problems, so they are best suited for problems where gradient information is unavailable or the landscape is rugged with many local optima. Understanding when a GA is the right tool — versus simulated annealing, gradient descent, or exhaustive search — is as important as understanding how to tune one.
