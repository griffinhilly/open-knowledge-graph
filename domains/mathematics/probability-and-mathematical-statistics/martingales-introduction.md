---
id: martingales-introduction
title: Introduction to Martingales
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conditional-expectation
  type: hard
- id: markov-chains
  type: soft
tags:
- martingales
- stochastic-processes
- probability
stage: abstract-reasoning
status: draft
---

# Introduction to Martingales

## Core Idea
A sequence {Mₙ} is a martingale if E[Mₙ₊₁ | ℱₙ] = Mₙ almost surely, where ℱₙ is the sigma-algebra of information up to time n. Martingales have zero expected change given current information—they are 'fair games.' The optional stopping theorem, martingale convergence theorem, and inequalities (Doob, Markov) are powerful tools for analyzing random processes.
