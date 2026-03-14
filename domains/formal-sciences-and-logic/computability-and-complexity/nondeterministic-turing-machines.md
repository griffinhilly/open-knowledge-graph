---
id: nondeterministic-turing-machines
title: Nondeterministic Turing Machines
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: time-complexity-classes-formal
  type: soft
builds-toward:
- np-and-polynomial-time
- space-complexity-classes-formal
tags:
- computation
- nondeterminism
- automata
- complexity
stage: advanced
status: validated
---

# Nondeterministic Turing Machines

## Core Idea
A nondeterministic Turing machine (NTM) has a transition relation rather than a function, allowing multiple possible moves at each step. An NTM accepts an input if *some* branch of its computation tree accepts. Any NTM can be simulated by a deterministic TM, but at an exponential cost in time — the deterministic machine must explore the entire computation tree. This exponential simulation gap is the heart of the P vs. NP question: can nondeterminism for polynomial-time computation always be eliminated without super-polynomial cost?

## How It's Best Learned
Visualize NTM computation as a tree of computation paths, with acceptance defined by the existence of an accepting leaf. Then prove the simulation theorem: a DTM simulates an NTM running in time t(n) in time 2^O(t(n)) by BFS over the computation tree.

## Common Misconceptions
- Nondeterminism is not probabilistic computation; an NTM accepts if *any* branch accepts, whereas a probabilistic TM accepts based on the fraction of accepting branches.
- NTMs are not more computationally powerful than DTMs in terms of *what* they compute (same Turing-computable functions), only potentially in *how efficiently* they compute.
