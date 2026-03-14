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
