---
id: nondeterministic-polynomial-time-computability-and-complexity
title: Nondeterministic Polynomial Time and NP
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-and-polynomial-time
  type: hard
- id: nondeterministic-turing-machines
  type: hard
builds-toward:
- sat-and-np-complete-problems
- np-complete-problems-standard
tags:
- NP
- nondeterminism
- complexity-classes
stage: advanced
status: draft
---

# Nondeterministic Polynomial Time and NP

## Core Idea
NP is the class of languages recognized by nondeterministic Turing machines in polynomial time, or equivalently, languages with polynomial-time verifiers: for membership x ∈ L, a short certificate exists that can be verified in polynomial time. This characterization makes NP capture optimization and constraint-satisfaction problems; P ⊆ NP, and whether they are equal is the P vs NP problem.

## Explainer

You already know about deterministic polynomial time (P) and nondeterministic Turing machines. The class NP arises naturally when you combine them: it is the set of languages recognized by a **nondeterministic Turing machine (NTM)** running in polynomial time. A nondeterministic machine at each step can branch into multiple computation paths simultaneously, and it *accepts* an input if any single branch accepts. When we say NP allows polynomial time, we mean every accepting branch has polynomial length — the machine may spawn exponentially many branches, but each individual branch is short.

The second characterization — the **verifier definition** — is often more intuitive and reveals why NP is natural. A language L is in NP if there exists a polynomial-time algorithm V (the **verifier**) and a polynomial p such that: x ∈ L if and only if there exists a **certificate** (witness) c with |c| ≤ p(|x|) where V(x, c) = 1. The certificate is short evidence that x belongs to L. For graph 3-colorability, the certificate is a valid coloring; for the Hamiltonian cycle problem, it is the cycle itself; for satisfiability, it is a satisfying assignment. The verifier checks the certificate in polynomial time — quickly, once it has the answer in hand. The two definitions are provably equivalent: the nondeterministic machine "guesses" the certificate on one branch and then verifies it deterministically.

Why does this capture so many natural problems? Because optimization and constraint-satisfaction problems nearly always have the structure "Does there exist a solution satisfying these constraints?" — and when a solution exists, it is a short certificate. Scheduling, integer programming, graph problems, protein folding, circuit layout: all fit this template. The certificate makes the "yes" side easy to witness, even if finding the certificate seems hard.

P ⊆ NP because a deterministic polynomial-time algorithm is a degenerate nondeterministic one with no branching. Whether P = NP — whether every problem whose solution is easy to *verify* is also easy to *find* — is the central open question in theoretical computer science. Most researchers believe P ≠ NP, but no proof exists. A resolution would reshape cryptography (whose security assumes certain problems are easy to verify but hard to solve), artificial intelligence, and mathematics itself. NP is the formal container for this question.
