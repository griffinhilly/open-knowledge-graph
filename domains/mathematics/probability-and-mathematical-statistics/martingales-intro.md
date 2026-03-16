---
id: martingales-intro
title: Introduction to Martingales
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conditional-expectation
  type: hard
tags:
- martingales
- stochastic-processes
- fair-game
stage: advanced
status: draft
---

# Introduction to Martingales

## Core Idea
A martingale is a sequence X_n such that E[X_{n+1}|X_1, ..., X_n] = X_n (fair game property). Supermartingales have ≤, submartingales have ≥. Martingales are central to probability theory: many limit theorems follow from martingale convergence. Examples: fair games, cumulative sums of mean-zero variables, likelihood ratios.
