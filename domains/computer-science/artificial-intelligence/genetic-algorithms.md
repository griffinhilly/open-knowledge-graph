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
