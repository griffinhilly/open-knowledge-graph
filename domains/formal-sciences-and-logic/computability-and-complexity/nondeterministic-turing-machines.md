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

## Explainer

You already know that a **deterministic Turing machine (DTM)** processes its input one step at a time, with each configuration uniquely determining the next move. A **nondeterministic Turing machine (NTM)** relaxes this: at each step, the machine may have several valid transitions available. The right mental model is not a single thread of computation but a **computation tree** — the root is the initial configuration, and each node branches into all possible next steps. The NTM accepts an input if *at least one* leaf in this tree is an accepting state. Rejection requires every branch to reject or loop.

This definition captures a natural abstraction for search problems. Consider checking whether a Boolean formula is satisfiable (the SAT problem): an NTM can nondeterministically "guess" a truth assignment in one step and then verify it in polynomial time. The NTM doesn't enumerate all assignments one by one — it explores all branches simultaneously in the abstract model. This is precisely why **NP** (nondeterministic polynomial time) is defined as the class of problems decidable by NTMs in polynomial time: each problem in NP has a polynomial-time "guess-and-verify" structure that corresponds naturally to an NTM computation.

A critical distinction: an NTM is not a **probabilistic Turing machine**. A probabilistic TM accepts based on the fraction of branches that accept — it models randomized algorithms. An NTM accepts if *any* branch accepts — it is a logical OR over all branches, finding the "best case" outcome. Nondeterminism is a theoretical tool for characterizing problem complexity, not a description of actual random computation. The complexity class BPP (bounded-error probabilistic polynomial time) captures probabilistic computation; NP captures nondeterministic computation. These are different classes.

Any NTM can be simulated by a DTM by **breadth-first search** over the computation tree: the deterministic machine systematically explores all branches level by level. If the NTM runs in time t(n), its computation tree has depth t(n) and at most some constant branching factor b, yielding at most b^{t(n)} nodes total. The DTM must visit all of them, so the simulation costs 2^{O(t(n))} time — an exponential blowup. Whether this blowup is unavoidable is the P vs. NP question: can every NP problem (solvable by an NTM in polynomial time) also be solved by a DTM in polynomial time? No one knows. The NTM is, in essence, the formal model whose expressive power the entire P vs. NP question is about.
