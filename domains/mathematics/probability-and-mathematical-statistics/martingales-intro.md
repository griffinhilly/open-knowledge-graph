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

## Explainer

You know that conditional expectation E[X | Y] is the best prediction of a random variable X given information Y. A **martingale** is a stochastic process — a sequence of random variables indexed by time — where the best prediction of tomorrow's value, given everything you know today, is exactly today's value. Formally, {X_n} is a martingale with respect to a sequence of information sets ("filtrations") F_n if E[X_{n+1} | F_n] = X_n. Nothing more, nothing less: on average, the process goes nowhere.

The intuition is a fair gambling game. Suppose you are betting at a fair casino: your fortune at time n is X_n. Because each bet is fair, your expected fortune tomorrow, conditional on knowing your fortune history, is exactly your current fortune. The martingale condition says there is no drift — no systematic upward or downward tendency once you condition on what has happened. Contrast this with a **supermartingale** (E[X_{n+1} | F_n] ≤ X_n), which models an unfavorable game where your expected fortune decreases, and a **submartingale** (E[X_{n+1} | F_n] ≥ X_n), which models a favorable game where it increases. Every supermartingale is a "losing game" in expectation, every submartingale a "winning game."

Simple examples build the intuition. If ξ_1, ξ_2, ... are independent mean-zero random variables, then the partial sums X_n = ξ_1 + ··· + ξ_n form a martingale. Each new step has mean zero, so the expected future value is always the current value. A random walk where each step is ±1 with probability ½ is the simplest case. **Likelihood ratios** provide a more sophisticated example: in hypothesis testing, the sequence L_n = p₁(X_1, ..., X_n) / p₀(X_1, ..., X_n) is a martingale under the null hypothesis p₀. This connection to statistics makes martingales central tools for sequential analysis.

The power of the martingale framework lies in its limit theorems and stopping theorems. The **optional stopping theorem** (informally) says that if you stop a fair game at a bounded stopping time, your expected fortune at stopping equals your initial fortune — you cannot beat a fair game by clever timing. The **martingale convergence theorem** says that a martingale bounded below converges almost surely. These results unify many classical limit theorems: the strong law of large numbers, convergence of likelihood ratios, and the behavior of branching processes all follow from martingale arguments. Recognizing that a process is a martingale is often the key that unlocks a proof.
