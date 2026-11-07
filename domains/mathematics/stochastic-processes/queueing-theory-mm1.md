---
id: queueing-theory-mm1
title: 'Queueing Theory: The M/M/1 Queue and Little''s Law'
domain: mathematics
course: stochastic-processes
prerequisites:
  - id: continuous-time-markov-chains
    type: hard
  - id: poisson-processes
    type: hard
  - id: exponential-distribution
    type: hard
  - id: geometric-distribution
    type: soft
builds-toward:
  - reflected-brownian-motion
tags: [stochastic-processes, queueing-theory, birth-death-process, littles-law, stationary-distribution, operations-research]
stage: expert
status: validated
---

# Queueing Theory: The M/M/1 Queue and Little's Law

## Core Idea
Queueing theory models systems where customers arrive, wait and are served. In the M/M/1 queue, arrivals form a Poisson process with rate λ, service times are independent exponential random variables with rate μ, and there is a single server. The number in the system is then a birth-death continuous-time Markov chain. When the traffic intensity ρ = λ/μ is less than 1, the queue has stationary distribution πₙ = (1 - ρ)ρⁿ, with mean number in system L = ρ/(1 - ρ) and mean time in system W = 1/(μ - λ). Little's law, L = λW, links averages in very general queueing systems.

## How It's Best Learned
Draw the state diagram 0, 1, 2, ... with arrows at rate λ to the right and rate μ to the left, and solve the balance equations across each cut between neighboring states. Tabulate L for ρ = 0.5, 0.8, 0.9 and 0.95 to see the sharp growth as ρ approaches 1. Then justify Little's law with the picture of total waiting time as an area under the number-in-system curve, and apply it to compute waiting times from queue lengths.

## Common Misconceptions
- A server that is busy 90% of the time has a little spare capacity, so queues stay short. (In an M/M/1 queue with ρ = 0.9, the mean number in system is 0.9/0.1 = 9, and it grows without bound as ρ → 1.)
- A queue is stable as long as λ ≤ μ. (With λ = μ the M/M/1 queue has no stationary distribution; stability requires λ < μ.)
- Little's law holds only for M/M/1 queues. (L = λW holds for a broad class of stable systems, whatever the arrival and service distributions or the queue discipline.)

## Questions

```yaml
- question: "Customers arrive at a single-server M/M/1 queue at rate λ = 8 per hour, and the service rate is μ = 10 per hour. What is the mean time a customer spends in the system?"
  type: multiple-choice
  options: ["6 minutes", "24 minutes", "30 minutes", "48 minutes"]
  answer: 2
  explanation: "W = 1/(μ - λ) = 1/(10 - 8) = 1/2 hour = 30 minutes. The value 24 minutes is the mean waiting time before service begins, Wq = ρ/(μ - λ) = 0.8/2 hour, and 6 minutes is the mean service time 1/μ."

- question: "In the same queue (λ = 8, μ = 10), what fraction of time is the server idle, and what is the mean number in the system?"
  type: short-answer
  answer: "Idle fraction π₀ = 1 - ρ = 0.2; mean number L = ρ/(1 - ρ) = 0.8/0.2 = 4."
  explanation: "With ρ = λ/μ = 0.8, the stationary distribution is πₙ = 0.2 · 0.8ⁿ. As a check with Little's law, L = λW = 8 × (1/2) = 4."

- question: "An M/M/1 queue with arrival rate equal to service rate (λ = μ) settles into a steady state with a finite mean queue length."
  type: true-false
  answer: false
  explanation: "When ρ = 1 the balance equations force all πₙ to be equal, which cannot sum to 1, so no stationary distribution exists. The queue length behaves like a null-recurrent random walk and does not settle down."

- question: "A coffee shop has on average 12 customers inside, and customers arrive at 1 per minute. Assuming a stable system, how long does a customer stay on average?"
  type: short-answer
  answer: "12 minutes"
  explanation: "Little's law gives W = L/λ = 12/1 = 12 minutes. The law needs only long-run averages, so it applies without knowing the arrival or service distributions."
```

## Explainer

Queues appear in call centers, computer networks, hospitals and checkout lines. The simplest model that captures their main effects is the M/M/1 queue. In Kendall's notation, the first M means Markovian (Poisson) arrivals, the second M means Markovian (exponential) service times, and 1 is the number of servers.

Let N(t) be the number of customers present, including the one in service. Because exponential times are memoryless, N(t) is a continuous-time Markov chain. From state n it moves up to n + 1 at rate λ (an arrival) and, if n ≥ 1, down to n - 1 at rate μ (a departure). This is a birth-death process.

For a stationary distribution π, the flow across the cut between states n and n + 1 must balance: λπₙ = μπₙ₊₁. Writing ρ = λ/μ, this gives πₙ = ρⁿπ₀. The probabilities must sum to 1, which is possible only if ρ < 1, and then π₀ = 1 - ρ. So

πₙ = (1 - ρ)ρⁿ, n = 0, 1, 2, ...,

a geometric distribution. The server is idle a fraction 1 - ρ of the time, which is why ρ is called the utilization.

The mean number in the system is L = ρ/(1 - ρ). This formula explains a lot of everyday frustration. At ρ = 0.5, L = 1. At ρ = 0.8, L = 4. At ρ = 0.9, L = 9, and at ρ = 0.95, L = 19. Raising utilization from 90% to 95% roughly doubles the queue. On average the server keeps up, so this congestion comes from random fluctuations in arrivals and service.

Little's law connects queue lengths to waiting times. If customers arrive at long-run rate λ and each spends an average time W in the system, then the long-run average number present is L = λW. The idea is to add up total customer-time in two ways: as the area under N(t), or as the sum of individual stays. The law holds for a wide class of stable systems. For the M/M/1 queue it gives W = L/λ = 1/(μ - λ). With λ = 8 and μ = 10 per hour, W = 30 minutes, of which 6 minutes on average is service and 24 minutes is waiting in line.

The same method extends to multiple servers (M/M/c), finite waiting rooms and networks of queues. In heavy traffic, when ρ is close to 1, a suitably rescaled queue-length process is approximated by reflected Brownian motion.
