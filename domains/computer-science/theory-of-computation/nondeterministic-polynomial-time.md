---
id: nondeterministic-polynomial-time
title: NP Class and Nondeterministic Polynomial Time
domain: computer-science
course: theory-of-computation
prerequisites:
- id: time-complexity-p-class
  type: hard
builds-toward:
- np-completeness
tags:
- np-class
- nondeterminism
- verification
stage: abstract-reasoning
status: draft
---

# NP Class and Nondeterministic Polynomial Time

## Core Idea
The complexity class NP consists of languages decidable by a nondeterministic Turing machine in polynomial time. Equivalently, NP consists of languages where membership can be verified in polynomial time given a certificate. P ⊆ NP, and the question P = NP is the most important open problem in computer science.

## Explainer

You already know what it means for a problem to be in P: a deterministic Turing machine can solve it in polynomial time. NP extends this idea by changing what "solve" means. Instead of requiring a machine to *find* an answer efficiently, NP only requires that a machine can *check* a proposed answer efficiently. The class **NP** (nondeterministic polynomial time) contains every decision problem where, if the answer is "yes," there exists a short proof — called a **certificate** or **witness** — that a deterministic Turing machine can verify in polynomial time.

Consider a concrete example: the Hamiltonian path problem asks whether a graph contains a path that visits every vertex exactly once. Finding such a path appears to require exploring exponentially many possibilities. But if someone hands you a specific sequence of vertices and claims it is a Hamiltonian path, you can verify this easily — just check that every vertex appears exactly once and each consecutive pair is connected by an edge. That verification runs in polynomial time, so Hamiltonian path is in NP. Every problem in P is automatically in NP as well, because if you can *solve* a problem in polynomial time, you can certainly *verify* a solution in polynomial time (just solve it yourself and compare).

The formal definition uses **nondeterministic Turing machines** — machines that can branch into multiple computational paths simultaneously and accept if *any* branch accepts. A nondeterministic TM running in polynomial time can "guess" the right certificate on one of its branches and then verify it. This nondeterministic guessing is not physically realistic, which is why the verifier definition is more intuitive: NP is the set of problems where "yes" answers have efficiently checkable proofs.

The central open question in computer science — **P versus NP** — asks whether every problem whose solutions can be *verified* quickly can also be *solved* quickly. If P = NP, then the apparent difficulty of problems like Hamiltonian path, Boolean satisfiability, and integer factorization would be an illusion — efficient algorithms would exist even if we haven't found them yet. Most computer scientists believe P ≠ NP, meaning that verification is fundamentally easier than discovery, but no one has been able to prove this. The resolution of this question would reshape cryptography, optimization, artificial intelligence, and mathematics itself.
