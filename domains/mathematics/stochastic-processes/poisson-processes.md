---
id: poisson-processes
title: Poisson Processes
domain: mathematics
course: stochastic-processes
prerequisites:
- id: exponential-distribution
  type: hard
- id: conditional-probability
  type: hard
- id: poisson-distribution
  type: hard
tags:
- poisson-process
- counting-process
- exponential-distribution
- jump-process
stage: expert
status: validated
---

# Poisson Processes

## Core Idea
A Poisson process N(t) with rate λ counts events occurring randomly in time: it has independent and stationary increments, with N(t) - N(s) ~ Poisson(λ(t-s)) for t > s. Equivalently, inter-arrival times are i.i.d. Exponential(λ). It is the continuous-time counting process with the "memoryless" property — the process restarts probabilistically after each event. The Poisson process is the fundamental model for random arrivals and the jump-process counterpart of Brownian motion.

## Questions

```yaml
- question: "Events occur according to a Poisson process with rate λ = 3 per hour. Given that exactly 1 event occurred in [0,2], the conditional distribution of the event's time is:"
  type: multiple-choice
  options:
    - "Exponential with rate 3"
    - "Uniform on [0,2]"
    - "Normal with mean 1 and variance 1/3"
    - "The event occurs at time 1 with probability 1 (deterministic)"
  answer: 1
  explanation: "This is a fundamental property of the Poisson process: given N(t) = n events in [0,t], the event times are distributed as the order statistics of n independent Uniform([0,t]) random variables. With n = 1, the single event time is Uniform on [0,2]. This follows from the homogeneity of the Poisson process — events are equally likely to occur at any moment within the interval. The result generalizes: given N(t) = n, the n arrival times have the same joint distribution as n i.i.d. Uniform([0,t]) random variables, sorted."

- question: "The sum of two independent Poisson processes with rates λ₁ and λ₂ is again a Poisson process, with rate λ₁ + λ₂."
  type: true-false
  answer: true
  explanation: "If N₁ and N₂ are independent Poisson processes with rates λ₁ and λ₂, then N(t) = N₁(t) + N₂(t) has independent stationary increments (inherited from the independence of N₁ and N₂), and N(t) - N(s) = (N₁(t)-N₁(s)) + (N₂(t)-N₂(s)) is the sum of two independent Poisson random variables, which is Poisson(λ₁(t-s) + λ₂(t-s)) = Poisson((λ₁+λ₂)(t-s)). This superposition property makes Poisson processes the natural model for merged independent event streams."

- question: "Explain why the exponential distribution of inter-arrival times is equivalent to the memoryless property of the Poisson process."
  type: short-answer
  answer: "The memoryless property states P(T > t+s | T > t) = P(T > s) — knowing that no event has occurred for t time units doesn't change the distribution of the remaining waiting time. The exponential distribution is the unique continuous distribution with this property: P(T > t+s | T > t) = e^{-λ(t+s)}/e^{-λt} = e^{-λs} = P(T > s). This means the process 'restarts' after each moment — the future is independent of the past given that no event has occurred. The memoryless property characterizes the Poisson process among all counting processes with stationary increments."
  explanation: "The memoryless property is both the defining intuition and the characterizing theorem for exponential inter-arrivals. The geometric distribution plays the same role in discrete time: it is the unique memoryless discrete distribution, and the Poisson process is the continuous-time limit of Bernoulli trials with geometric inter-arrivals."

- question: "A compound Poisson process X(t) = Σᵢ₌₁^{N(t)} Yᵢ, where N is Poisson(λt) and Yᵢ are i.i.d., has E[X(t)] = λt·E[Y₁] and Var(X(t)) = λt·E[Y₁²]."
  type: true-false
  answer: true
  explanation: "By the law of total expectation: E[X(t)] = E[N(t)]·E[Y₁] = λt·E[Y₁]. By the law of total variance: Var(X(t)) = E[N(t)]·Var(Y₁) + Var(N(t))·(E[Y₁])² = λt·Var(Y₁) + λt·(E[Y₁])² = λt·E[Y₁²]. The compound Poisson process generalizes the Poisson process by allowing each event to carry a random magnitude Yᵢ — it models aggregate insurance claims, total demand in a queue, or cumulative jump sizes in a financial model."
```

## Explainer

The **Poisson process** is the simplest and most important continuous-time counting process. It counts events (arrivals, failures, transactions) that occur randomly in time at a constant average rate λ. The three equivalent characterizations are: (1) N(t) has independent, stationary Poisson-distributed increments with N(t)-N(s) ~ Poisson(λ(t-s)); (2) inter-arrival times T₁, T₂, ... are i.i.d. Exponential(λ); (3) for infinitesimally small dt, P(one event in [t, t+dt]) = λdt + o(dt) and P(two or more events) = o(dt). Each characterization captures a different aspect — the distribution of counts, the distribution of waiting times, and the infinitesimal event rate.

The **memoryless property** of the exponential distribution is the Poisson process's signature. Given that no event has occurred for s time units, the distribution of the remaining waiting time is the same Exponential(λ) — the process "doesn't remember" how long it has been waiting. This is the unique continuous distribution with this property (the geometric distribution is the discrete analogue). The memoryless property implies that the Poisson process is Markov: the future depends only on the current count, not on the history of arrival times.

Key structural properties include **superposition** (merging independent Poisson processes produces another Poisson process with summed rates), **thinning** (independently keeping each event with probability p produces a Poisson process with rate λp), and the **order-statistic property** (given N(t) = n, the n arrival times are distributed as the order statistics of n i.i.d. Uniform([0,t]) variables). The **compound Poisson process** X(t) = Σᵢ₌₁^{N(t)} Yᵢ attaches an i.i.d. random magnitude Yᵢ to each event, modeling aggregate claims in insurance, total demand, or cumulative price jumps.

The Poisson process is the jump-process counterpart of Brownian motion. Where Brownian motion has continuous paths and is the building block for continuous stochastic calculus, the Poisson process has piecewise-constant paths with unit jumps and is the building block for jump-process calculus. The **compensated Poisson process** Ñ(t) = N(t) - λt is a martingale — the counting process minus its expected rate. This martingale plays the same role for jump processes that Brownian motion plays for continuous processes, and it is the starting point for the stochastic calculus of jump processes and Levy processes.
