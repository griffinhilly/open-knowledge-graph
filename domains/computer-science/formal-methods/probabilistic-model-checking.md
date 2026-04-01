---
id: probabilistic-model-checking
title: Probabilistic Model Checking
domain: computer-science
course: formal-methods
prerequisites:
- id: model-checking-intro
  type: hard
- id: temporal-logic-ltl-ctl
  type: hard
- id: sat-solving-cdcl
  type: soft
builds-toward: []
tags:
- probabilistic-model-checking
- markov-chains
- markov-decision-processes
- probabilistic-temporal-logic
- rewards
- quantitative-verification
stage: expert
status: validated
---

# Probabilistic Model Checking

## Core Idea

Probabilistic model checking verifies systems with **stochastic behavior** — nondeterministic choices and probabilistic events. Rather than asking "does this system have a property," it asks "what is the probability that this system has a property?" For example: "what is the probability the system reaches a goal state?" or "what is the expected time to recover from a failure?" Models include **Markov chains** (fully probabilistic: all transitions have fixed probabilities), **Markov decision processes** (MDP: mix of nondeterminism and probability, capturing systems controlled by both a scheduler and random events), and **Markov automata** (continuous-time systems with probabilistic and nondeterministic transitions). Properties are expressed in **probabilistic temporal logic** (PCTL, CSL) that quantifies probabilities: P(φ ≥ 0.95) means "the probability of φ is at least 95%." Probabilistic model checking computes the probability of properties or the expected values of reward measures, enabling quantitative verification of safety and liveness in systems with randomness.

## Questions

```yaml
- question: "A Markov chain models a system where every transition has a fixed probability. An MDP (Markov decision process) additionally has nondeterministic choices. Why is the MDP model more expressive?"
  type: short-answer
  answer: "A Markov chain has a single probability distribution over the next state from any state. An MDP allows nondeterminism: from a state, there may be multiple possible actions, each with its own probability distribution. This models systems controlled by both a scheduler (making nondeterministic choices about which action to take) and randomness (once an action is chosen, its outcome is probabilistic). For example, a communication protocol might nondeterministically choose to retry (scheduler choice) and then probabilistically succeed or fail (randomness). MDP model checking computes the worst-case (minimum) and best-case (maximum) probabilities over all possible scheduler choices, answering 'what is the worst that could happen?' and 'what is the best that could happen?'"
  explanation: "The nondeterminism in MDPs captures the interplay between controllable and uncontrollable behaviors. A scheduler is an adversary or controller: in game-theoretic verification, you ask 'can the scheduler ensure property P?', answering in the affirmative if a scheduler exists that guarantees P. In synthesis, you find the scheduler that achieves the best probability. This is more expressive than pure probabilistic systems but computationally harder: model checking MDPs is NP-hard, while Markov chains can be checked in polynomial time."

- question: "In probabilistic temporal logic, the formula P(φ ≥ 0.95) means 'the probability of φ is at least 95%.' For a Markov chain, this is evaluated as: compute the probability of φ, check if it is ≥ 0.95. For an MDP, what does this formula mean?"
  type: short-answer
  answer: "For an MDP, P(φ ≥ 0.95) means: 'there exists a scheduler such that the probability of φ is at least 95%.' Equivalently, the maximum probability (best-case under optimal scheduling) of φ is ≥ 0.95. Dually, P(φ ≤ 0.05) means the minimum probability (worst-case, over all schedulers) is ≤ 0.05. MDP model checking computes both the maximum and minimum probabilities of a property over all possible schedulers, giving bounds on what could happen. This is essential for systems where some choices are adversarial (worst-case analysis) or cooperative (best-case analysis)."
  explanation: "The existential/universal quantification over schedulers is the key difference. In a Markov chain, there is one probability; in an MDP, there is a range (minimum to maximum) depending on the scheduler. Verification problems include: 'can you guarantee at least 95% success?', answered by checking if the maximum probability is ≥ 0.95, and 'is there a scheduler that might lead to failure?', answered by checking if the minimum probability of success is < 100%."

- question: "Rewards in probabilistic model checking allow reasoning about expected values beyond just probabilities. A system might have a property: 'the expected time to recover from failure is at most 10 seconds.' How would you verify this?"
  type: multiple-choice
  options:
    - "Assign a time cost to each transition and use model checking to compute the expected cost (sum of costs on all paths, weighted by path probability). Check if this expected value is ≤ 10"
    - "Simulate the system 1000 times and average the recovery times"
    - "Formally verify the system cannot fail"
    - "Measure the system on a test run"
  answer: 0
  explanation: "Reward model checking extends probabilistic model checking by assigning numeric values (rewards or costs) to states and transitions. Transitions might have time costs; states might have resource usage costs. The model checker computes the expected total reward on paths satisfying a property (e.g., paths from 'failure' to 'recovered'). The expectation is weighted by path probability: if a path has 30% probability and costs 8 seconds, it contributes 0.3 × 8 to the expectation. Model checking sums over all paths, computing the exact expected cost. This is much more precise than simulation (which requires many runs) and gives absolute guarantees (within the model's accuracy)."

- question: "Probabilistic model checking requires solving systems of equations. For a Markov chain computing the probability of reaching a goal state, the equations are linear (probability of reaching goal from state s = sum over next states of (transition probability * probability from next state)). Why does this enable efficient checking?"
  type: short-answer
  answer: "Linear systems of equations can be solved in polynomial time using Gaussian elimination or iterative methods like value iteration. For a Markov chain with n states, solving the system takes O(n^3) time, making probabilistic model checking scalable. In contrast, model checking nonprobabilistic systems typically involves NP-hard problems (SAT solving). The linearity of probabilistic systems is a computational advantage: even though you're computing probabilities over exponentially many paths, the recursive structure allows polynomial-time solution."
  explanation: "This is a counterintuitive advantage of probabilistic systems: adding randomness makes the verification problem easier (polynomial) rather than harder. The reason is that linear equations are tractable, whereas Boolean satisfiability (underlying standard model checking) is NP-hard. Modern probabilistic model checkers like PRISM exploit this: they build an automaton representing all paths, then set up and solve a system of linear equations, computing exact probabilities in polynomial time. For MDPs, the problem is harder (NP-hard, requiring game-theoretic reasoning) but still much more tractable than standard model checking of complex systems."
```

## Explainer

Most formal verification assumes systems are **deterministic**: the same input always produces the same output. But real systems have **stochastic behavior** — randomness from the environment, probabilistic scheduling, or deliberate randomization in algorithms. A communication protocol may retry with some probability on failure; a distributed system may randomly choose a backup server; a hybrid system may have probabilistic transitions between modes. **Probabilistic model checking** extends traditional model checking to verify systems with randomness by computing the probability of properties rather than just checking yes/no.

**Models and Properties**

The most common model is a **Markov chain**: a transition system where each edge is labeled with a probability. From state s, the system transitions to state s' with probability p(s, s'). Properties are expressed in **probabilistic temporal logic** — extensions of LTL/CTL that quantify probabilities:

- P(φ) — "the probability of φ"
- P(φ ≥ 0.95) — "φ holds with probability at least 95%"
- E[reward] — "the expected value of a reward accumulator"

A simple property: P(◇goal) — "the probability of eventually reaching a goal state." Model checking computes this probability: the sum of probabilities of all paths leading to the goal, weighted by path probability.

**Markov Decision Processes (MDPs)**

Many systems are not purely probabilistic but combine **nondeterminism** and **probability**. A scheduling algorithm might nondeterministically choose which process to run, then probabilistically succeed. A network protocol might choose to retry or give up, and each choice has a probability of success. **MDPs** model this: states have multiple possible transitions (nondeterministic choices), each with its own probability distribution.

For MDPs, properties are interpreted with quantifiers over schedulers (entities making nondeterministic choices). P(φ ≥ 0.95) means: "does there exist a scheduler such that φ holds with probability at least 95%?" The model checker computes the maximum and minimum probabilities over all possible schedulers, answering: "what's the best we can do?" and "what's the worst that could happen?" This is essential for adversarial analysis (assuming the worst scheduler, like an attacker) or synthesis (finding a scheduler that achieves goals).

**Computing Probabilities: The Equations**

To compute the probability of reaching a goal from state s in a Markov chain:

```
P(reach goal from s) = 1 if s is goal
                      = sum over s' of p(s,s') * P(reach goal from s')
                      = 0 if no path from s reaches goal
```

This recurrence defines a system of linear equations: one equation per state. Solving this system in polynomial time (via Gaussian elimination or value iteration) gives exact probabilities. The linearity is a computational advantage: even though there are exponentially many paths, the recursive structure allows efficient solution.

For MDPs, the equations are:

```
P_max(reach goal from s) = max over actions of (sum over s' of p(action,s,s') * P_max(reach goal from s'))
```

This is a nonlinear equation system (max is nonlinear), making MDP solving harder (NP-hard in the worst case), but still polynomial for many practical systems.

**Rewards and Quantitative Properties**

Beyond probabilities, you can assign **rewards** (or costs) to transitions and states. Rewards might represent time, energy, money, or any quantitative measure. A transition might cost 0.5 seconds; a state might consume 10 milliwatts. The model checker computes expected total reward: the weighted sum of rewards on all paths, where weights are path probabilities.

For example: "the expected time to deliver a message is at most 100ms." You assign time costs to transitions, set up reward equations analogous to probability equations, and solve to compute expected time. This provides quantitative verification: not just "the system is reliable" but "the system is 99.9% reliable and recovers in an average of 5 seconds."

**Practical Applications**

- **Probabilistic protocols**: Randomized consensus algorithms, distributed systems with probabilistic recovery.
- **Hybrid systems**: Systems with both continuous (stochastic differential equations) and discrete (event-based) components.
- **Security protocols**: Cryptographic protocols with randomness; verifying that deviations are caught with high probability.
- **Wireless networks**: Probabilistic models of packet loss, interference; verifying throughput guarantees.
- **Reliability and safety**: Systems with component failures modeled probabilistically (MTTF — mean time to failure).

**Tools**

- **PRISM**: The most widely used probabilistic model checker, supporting Markov chains, MDPs, and Markov automata. Excellent for systems with thousands to tens of thousands of states.
- **Storm**: A newer model checker focusing on scalability and quantitative verification.
- **aPMC**: Approximate probabilistic model checking for very large systems.

**Limitations**

Probabilistic model checking faces challenges scaling to extremely large systems (millions of states require abstraction or approximation). The accuracy of results depends on model quality: if the probabilistic model doesn't match reality, verified properties may not hold. Current research focuses on: (1) abstraction techniques to reduce state space while preserving properties, (2) verification of systems with unknown probabilities (robust verification), (3) verifying economic/game-theoretic properties of systems with both probability and strategic agents.

The key insight is that randomness, properly handled, can make verification more tractable. Probabilistic model checking demonstrates that you can rigorously reason about systems with stochastic behavior, computing exact quantitative properties and providing formal assurance for probabilistic systems.
