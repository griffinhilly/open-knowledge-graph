---
id: viterbi-algorithm
title: Viterbi Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: hidden-markov-models
  type: hard
- id: dynamic-programming-intro
  type: hard
tags:
- sequence-models
- dynamic-programming
- decoding
stage: advanced
status: validated
---

# Viterbi Algorithm

## Core Idea
Viterbi finds the most likely hidden state sequence in an HMM given observations using dynamic programming. It maintains the maximum probability path to each state at each time step, eliminating suboptimal paths with O(T × N²) complexity.

## Questions

```yaml
- question: "With N=10 states and T=100 time steps, brute-force enumeration of all state sequences requires examining 10^100 candidates. Why does Viterbi reduce this to O(T × N²)?"
  type: multiple-choice
  options:
    - "Viterbi prunes low-probability transitions early, skipping most candidates without evaluating them"
    - "Most state transitions have zero probability in real HMMs, so the effective search space is much smaller"
    - "The most likely path ending in any state at time t depends only on the best path reaching each predecessor at t−1; keeping one optimal partial path per state eliminates the need to track all paths"
    - "HMMs have at most N² possible transitions, which directly caps the number of paths to evaluate"
  answer: 2
  explanation: "Viterbi exploits optimal substructure: the best complete path to state j at time t must pass through the best path to some predecessor state i at t−1. You do not need to remember every possible partial path to each state — only the single best one. At each of T time steps, you update N state scores, each requiring a max over N predecessors: T × N × N = O(T × N²). The exponential blowup is eliminated because suboptimal partial paths are discarded immediately."

- question: "After running Viterbi on an observation sequence, what is the purpose of the backpointer table stored during the algorithm?"
  type: multiple-choice
  options:
    - "To record the emission probabilities at each time step, so results can be verified against the original HMM"
    - "To store probabilities for every possible state sequence, enabling comparison with alternative paths"
    - "To record, at each time step and state, which predecessor state achieved the maximum probability — enabling reconstruction of the optimal path by tracing backward from the final state"
    - "To allow the algorithm to restart if the most likely final state has probability zero"
  answer: 2
  explanation: "The Viterbi table δₜ(j) stores the probability of the best path ending in state j at time t, but does not itself tell you what that path was. The backpointer ψₜ(j) records which predecessor state i produced the maximum when computing δₜ(j). After the algorithm terminates, you find the most likely final state, then follow backpointers backward through time to reconstruct the complete optimal sequence. Without backpointers, you would know the probability of the best path but not which path it was."

- question: "The Viterbi algorithm finds the single most likely state sequence given the observations — it does not compute the probability of a particular observation sequence."
  type: true-false
  answer: true
  explanation: "Viterbi solves the 'decoding problem': finding the most likely hidden state sequence, argmax P(states | observations). Computing P(observations) — the total probability of the observation sequence summed over all state sequences — is a different problem solved by the Forward algorithm. Viterbi maximizes over paths rather than summing them, so it finds the best single path but not the marginal probability of the observations."

- question: "Viterbi is guaranteed to find the globally optimal state sequence because it carefully evaluates all N^T possible paths before selecting the best one."
  type: true-false
  answer: false
  explanation: "Viterbi finds the global optimum without evaluating all N^T paths. It achieves this by exploiting optimal substructure: once a suboptimal partial path is identified at any time step, it can be discarded permanently, because no extension of a suboptimal partial path can produce the globally optimal complete path. The algorithm guarantees optimality through dynamic programming logic, not exhaustive search — which is precisely what makes it tractable."

- question: "Explain why the Viterbi algorithm can be viewed as finding the highest-probability path through a trellis graph, and what the nodes and edges of that graph represent."
  type: short-answer
  answer: "The trellis is a directed acyclic graph with T columns (one per time step) and N rows (one per state), giving N×T nodes total. Each node represents being in state j at time t. Edges connect each node at time t to all nodes at time t+1, weighted by the transition probability times the emission probability for the next observation. Finding the most likely state sequence is equivalent to finding the highest-weight path from any node in column 1 to any node in column T — a shortest-path problem on this graph."
  explanation: "Viewing Viterbi as a shortest-path problem makes the dynamic programming structure concrete and connects it to graph algorithms. The trellis perspective also clarifies why backpointers are needed: just as Dijkstra's algorithm stores predecessor nodes to reconstruct the shortest path, Viterbi stores predecessor states to reconstruct the most likely sequence. The O(T × N²) complexity corresponds to the number of edges in the trellis."
```

## Explainer

You know from Hidden Markov Models that a system has hidden states generating observable outputs — for example, weather conditions (hidden) producing observable activity choices, or part-of-speech tags (hidden) generating observed words. Given a sequence of observations, a natural question is: what is the most likely sequence of hidden states that produced them? A brute-force approach would enumerate every possible state sequence, compute its probability, and pick the best one — but with N possible states and T time steps, that means N^T candidates, which is exponentially intractable. The **Viterbi algorithm** solves this problem in O(T × N²) time using dynamic programming.

The key insight, which you will recognize from your study of dynamic programming, is **optimal substructure**: the most likely path of length T ending in state sⱼ must consist of the most likely path of length T−1 ending in some state sᵢ, followed by a transition from sᵢ to sⱼ. You do not need to consider all possible length-(T−1) paths — only the best one reaching each state. At each time step t, the algorithm maintains a table δₜ(j) representing the probability of the most likely path that ends in state j at time t and produces the observations seen so far. The recursion is: δₜ(j) = maxᵢ [δₜ₋₁(i) × transition(i→j) × emission(j→oₜ)]. You also store backpointers recording which predecessor state i achieved the maximum, so you can reconstruct the full path at the end.

The algorithm proceeds left to right through the observation sequence. **Initialization** sets δ₁(j) = π(j) × emission(j→o₁) for each state j, where π(j) is the initial state probability. **Recursion** fills in each subsequent column of the table using the formula above, taking O(N²) per time step (for each of N states, you maximize over N predecessors). **Termination** finds the state with the highest δ_T value, and **backtracking** follows the stored pointers backward from that state to recover the most likely complete path.

The Viterbi algorithm appears throughout computer science and engineering: in speech recognition (decoding the most likely phoneme sequence), natural language processing (part-of-speech tagging), bioinformatics (gene finding), and digital communications (decoding convolutional codes). Its efficiency comes from the same principle that powers all dynamic programming — recognizing that exponentially many candidate solutions share overlapping subproblems, and that you only need to keep the best partial solution reaching each intermediate state. Once you see Viterbi as "shortest path through a trellis graph," the connection to dynamic programming becomes concrete: the trellis has N nodes per time step, and you are finding the highest-probability path from any start node to any end node.
