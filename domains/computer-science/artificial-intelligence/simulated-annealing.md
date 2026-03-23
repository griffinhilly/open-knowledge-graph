---
id: simulated-annealing
title: Simulated Annealing
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: local-search-optimization
  type: hard
- id: stochastic-gradient-descent
  type: soft
tags:
- optimization
- metaheuristic
- probability
- annealing
stage: advanced
status: validated
---

# Simulated Annealing

## Core Idea
Simulated annealing probabilistically accepts worse solutions early in search (high temperature) to escape local optima, then gradually accepts only improvements (low temperature) to converge. The cooling schedule determines the algorithm's behavior: fast cooling risks getting stuck in local optima, while slow cooling wastes iterations. The algorithm is theoretically guaranteed to find the global optimum with a sufficiently slow cooling schedule.

## How It's Best Learned
Implement simulated annealing with different cooling schedules (linear, exponential, adaptive) and visualize how each affects solution quality over iterations.

## Common Misconceptions
Simulated annealing always finds the global optimum (it requires infinitely slow cooling). Temperature should always decrease (adaptive schedules may increase temperature if improvement stalls).

## Questions

```yaml
- question: "When simulated annealing evaluates a neighboring solution that is worse than the current one, what does it do?"
  type: multiple-choice
  options:
    - "It always rejects worse solutions to ensure the objective function never decreases"
    - "It accepts the worse solution with probability exp(−ΔE/T), which is close to 1 at high temperature and near 0 at low temperature"
    - "It restarts from a random position in the search space to escape the local region"
    - "It pauses and waits for temperature to decrease before deciding whether to accept"
  answer: 1
  explanation: "This probabilistic acceptance of worse solutions is the defining mechanism of simulated annealing and the key difference from hill climbing. At high temperature, exp(−ΔE/T) ≈ 1, so almost any move is accepted — the algorithm wanders freely. As temperature decreases, the probability drops, and worse moves are accepted less often. This schedule of gradually restricting exploration is what allows the algorithm to first escape local optima (high T) and then converge to a good solution (low T)."

- question: "A practitioner runs simulated annealing with a very aggressive cooling schedule, halving the temperature every 10 iterations. What is the most likely outcome compared to using a slow cooling schedule?"
  type: multiple-choice
  options:
    - "The algorithm explores more of the search space and reliably finds a better final solution"
    - "The algorithm effectively behaves like hill climbing and is likely to get stuck in a local optimum"
    - "The algorithm converges to the global optimum faster because it wastes less time on bad solutions"
    - "The theoretical guarantee still ensures convergence to the global optimum in fewer total steps"
  answer: 1
  explanation: "Fast cooling means the temperature drops quickly to near zero, so the acceptance probability for worse solutions falls to near zero almost immediately. The algorithm then only accepts improvements — exactly like hill climbing — and gets stuck at whatever local optimum is nearby. The whole point of simulated annealing is to avoid this by cooling slowly enough that the algorithm has time to explore beyond local optima. The theoretical guarantee of finding the global optimum requires a specific logarithmically slow cooling schedule, which fast cooling violates entirely."

- question: "Simulated annealing is theoretically guaranteed to find the global optimum if the cooling schedule is slow enough."
  type: true-false
  answer: true
  explanation: "This is a proven theoretical result: if the temperature decreases no faster than T(t) ≥ C/log(t), where C is a constant related to the energy barriers in the problem, then simulated annealing converges to the global optimum with probability 1. The catch is that this logarithmic cooling schedule is extraordinarily slow — impractically slow for real problems. In practice, faster cooling schedules (geometric decay) are used, sacrificing the theoretical guarantee for a good-enough solution in reasonable computation time."

- question: "In practice, simulated annealing is widely used because any reasonable cooling schedule is guaranteed to find the global optimum in polynomial time."
  type: true-false
  answer: false
  explanation: "The theoretical guarantee of convergence to the global optimum requires a logarithmically slow cooling schedule — one so slow it is computationally impractical. No faster cooling schedule carries this guarantee. In practice, geometric cooling schedules (T_new = α·T_old with α close to 1) are used because they work well empirically, but they only guarantee a good solution, not the global optimum. Simulated annealing is a heuristic that trades guaranteed optimality for practical efficiency."

- question: "Explain how simulated annealing differs from simple hill climbing, and why accepting worse solutions early in the search actually improves the quality of the final solution."
  type: short-answer
  answer: "Hill climbing always moves to a better neighbor and never accepts worse solutions, so it converges to the nearest local optimum and gets stuck there — unable to explore the broader search space. Simulated annealing adds probabilistic acceptance of worse solutions, controlled by a temperature parameter. Early in the search (high temperature), the algorithm accepts almost any move, allowing it to explore widely across the search space and escape the basin of attraction around any single local optimum. As temperature decreases, acceptance becomes increasingly selective, and the algorithm settles into the best region it has found. The insight is that getting stuck in a local optimum is a failure of short-sighted greedy search; by temporarily allowing moves that look bad locally, the algorithm gains the ability to discover globally better solutions that would be inaccessible to hill climbing."
  explanation: "The physics analogy is instructive: a molten metal cooled rapidly (quenching) freezes into a disordered crystal with many local energy minima (defects). Cooled slowly (annealing), atoms have time to explore configurations and settle into the lowest-energy crystalline state. The algorithm mimics this process, using the Boltzmann probability distribution from statistical mechanics to control exploration vs exploitation."
```

## Explainer

From local search optimization, you know the fundamental problem: hill climbing finds a local optimum but gets stuck there, unable to reach a potentially better solution elsewhere in the search space. Imagine you are hiking in fog and can only feel the slope beneath your feet. Hill climbing always walks uphill, so you reach the nearest peak — but it might be a small hill when a mountain is just across the valley. Simulated annealing solves this by occasionally allowing downhill steps, especially early in the search, giving the algorithm a chance to escape local optima and explore the broader landscape.

The key mechanism is the **acceptance probability**. When simulated annealing considers a neighboring solution, it always accepts improvements (moves to a better solution). But when the neighbor is *worse*, it accepts the move with probability exp(−ΔE / T), where ΔE is how much worse the neighbor is and T is the current **temperature**. This formula comes from statistical mechanics — it models how atoms in a heated metal occasionally jump to higher-energy configurations. At high temperature, exp(−ΔE / T) is close to 1, so almost any move is accepted, and the algorithm wanders freely through the search space. As temperature decreases, the probability of accepting worse moves drops, and the algorithm increasingly behaves like pure hill climbing, settling into a good solution.

The **cooling schedule** controls how temperature decreases over time and is the most important design choice. A common schedule is geometric cooling: T_new = α · T_old, where α is typically between 0.9 and 0.999. Fast cooling (low α, or few iterations) behaves almost like hill climbing — you barely explore before settling. Slow cooling (high α, or many iterations) gives the algorithm time to escape traps but takes longer to converge. The theoretical guarantee is striking: with an infinitely slow cooling schedule (specifically, T(t) ≥ C / log(t)), simulated annealing converges to the global optimum with probability 1. In practice, you never cool this slowly, so you trade guaranteed optimality for a good-enough solution in reasonable time.

Simulated annealing shines on combinatorial optimization problems where the search space is too large for exhaustive search and too rugged for gradient-based methods. Classic applications include the traveling salesman problem, circuit layout, and scheduling. The algorithm requires only three things: a way to represent solutions, a way to generate neighboring solutions, and a way to evaluate solution quality. It needs no gradient, no differentiability, and no assumptions about the structure of the search space. The tradeoff is that tuning the cooling schedule, initial temperature, and neighborhood structure requires experimentation — there is no single recipe that works for all problems.
