---
id: probabilistic-turing-machines
title: Probabilistic Turing Machines
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: nondeterministic-finite-automata
  type: soft
builds-toward:
- bpp-complexity-class
- rp-corp-complexity
tags:
- randomization
- probabilistic-computation
stage: advanced
status: draft
---

# Probabilistic Turing Machines

## Core Idea
A probabilistic Turing machine (PTM) is a nondeterministic TM where each branch is taken with specified probability. Unlike NTM (existential: accept if any branch succeeds), PTM explores branches stochastically. A PTM decides a language L with error probability ε if for x ∈ L it accepts with probability ≥ 1-ε and for x ∉ L it rejects with probability ≥ 1-ε. PTMs formalize randomized algorithms and enable analysis of error probability via amplification.

## Explainer

You already know that a standard Turing machine follows a single deterministic path of computation, and that a nondeterministic TM can branch into many paths simultaneously (accepting if any branch accepts). A **probabilistic Turing machine** sits between these two models: at each step where multiple transitions are possible, the machine flips a coin to decide which branch to follow. Instead of exploring all branches or just one, it randomly walks through one computational path — and that randomness turns out to be surprisingly powerful.

The key difference from nondeterminism is how acceptance works. A nondeterministic TM asks an existential question: "does *some* branch accept?" A probabilistic TM asks a statistical question: "does a *large fraction* of branches accept?" Formally, a PTM decides a language with bounded error if it gives the correct answer with probability at least 2/3 (or any constant greater than 1/2). The specific threshold doesn't matter much, because of a technique called **probability amplification**: if you run the machine many times independently and take a majority vote, the error probability drops exponentially. Run it 100 times, and the chance of a wrong majority answer becomes astronomically small.

This model formalizes real randomized algorithms you may encounter in practice. The Miller-Rabin primality test, for example, can determine whether a number is prime with high probability in polynomial time — something that was not known to be achievable deterministically until much later (and the deterministic algorithm is slower in practice). Randomized quicksort, random sampling algorithms, and many graph algorithms exploit the same idea: a little randomness can make hard problems tractable or make algorithms faster on average.

PTMs give rise to important complexity classes like **BPP** (bounded-error probabilistic polynomial time), which captures problems solvable efficiently with randomness and two-sided error, and **RP** (randomized polynomial time), where errors occur only on one side. Whether BPP equals P — whether randomness actually helps — remains an open question, though most complexity theorists conjecture that it does not, meaning every efficient randomized algorithm has an efficient deterministic counterpart we just haven't found yet.
