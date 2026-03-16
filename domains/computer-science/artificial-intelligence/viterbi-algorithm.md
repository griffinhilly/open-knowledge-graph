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
status: draft
---

# Viterbi Algorithm

## Core Idea
Viterbi finds the most likely hidden state sequence in an HMM given observations using dynamic programming. It maintains the maximum probability path to each state at each time step, eliminating suboptimal paths with O(T × N²) complexity.

## Explainer

You know from Hidden Markov Models that a system has hidden states generating observable outputs — for example, weather conditions (hidden) producing observable activity choices, or part-of-speech tags (hidden) generating observed words. Given a sequence of observations, a natural question is: what is the most likely sequence of hidden states that produced them? A brute-force approach would enumerate every possible state sequence, compute its probability, and pick the best one — but with N possible states and T time steps, that means N^T candidates, which is exponentially intractable. The **Viterbi algorithm** solves this problem in O(T × N²) time using dynamic programming.

The key insight, which you will recognize from your study of dynamic programming, is **optimal substructure**: the most likely path of length T ending in state sⱼ must consist of the most likely path of length T−1 ending in some state sᵢ, followed by a transition from sᵢ to sⱼ. You do not need to consider all possible length-(T−1) paths — only the best one reaching each state. At each time step t, the algorithm maintains a table δₜ(j) representing the probability of the most likely path that ends in state j at time t and produces the observations seen so far. The recursion is: δₜ(j) = maxᵢ [δₜ₋₁(i) × transition(i→j) × emission(j→oₜ)]. You also store backpointers recording which predecessor state i achieved the maximum, so you can reconstruct the full path at the end.

The algorithm proceeds left to right through the observation sequence. **Initialization** sets δ₁(j) = π(j) × emission(j→o₁) for each state j, where π(j) is the initial state probability. **Recursion** fills in each subsequent column of the table using the formula above, taking O(N²) per time step (for each of N states, you maximize over N predecessors). **Termination** finds the state with the highest δ_T value, and **backtracking** follows the stored pointers backward from that state to recover the most likely complete path.

The Viterbi algorithm appears throughout computer science and engineering: in speech recognition (decoding the most likely phoneme sequence), natural language processing (part-of-speech tagging), bioinformatics (gene finding), and digital communications (decoding convolutional codes). Its efficiency comes from the same principle that powers all dynamic programming — recognizing that exponentially many candidate solutions share overlapping subproblems, and that you only need to keep the best partial solution reaching each intermediate state. Once you see Viterbi as "shortest path through a trellis graph," the connection to dynamic programming becomes concrete: the trellis has N nodes per time step, and you are finding the highest-probability path from any start node to any end node.
