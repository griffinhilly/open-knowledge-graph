---
id: complexity-class-np-definition
title: 'Complexity Class NP: Nondeterministic Polynomial Time'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: complexity-class-p-definition
  type: hard
- id: multi-tape-turing-machines
  type: soft
- id: asymptotic-notation-big-o-omega-theta
  type: soft
builds-toward:
- np-completeness-and-hardness
tags:
- np-class
- nondeterminism
- verification
- certificate
- hard
stage: advanced
status: draft
---

# Complexity Class NP: Nondeterministic Polynomial Time

## Core Idea
NP contains languages decided by nondeterministic TMs in polynomial time. Equivalently, NP is languages where yes-instances admit polynomial-size certificates verifiable in polynomial time. Many practical hard problems (SAT, clique, TSP decision version) are NP. The P vs NP question asks: is guessing-and-checking as fast as deterministic solving? Most believe P ≠ NP, but it remains open.

## Explainer

You already know that **P** contains problems solvable in polynomial time by a deterministic Turing machine. **NP** — nondeterministic polynomial time — captures a broader and more subtle idea: problems where proposed solutions can be *verified* efficiently, even if finding them from scratch might be hard. The formal definition says a language is in NP if a **nondeterministic** Turing machine can decide it in polynomial time. A nondeterministic TM can "guess" at each step, exploring many computational paths simultaneously. If *any* path leads to acceptance within polynomial steps, the machine accepts.

But the more intuitive and practically useful characterization is the **verifier definition**. A language L is in NP if there exists a polynomial-time deterministic TM (called a verifier) and a constant *c* such that for every string *x* in L, there exists a **certificate** (also called a witness) of length at most |*x*|^*c* that the verifier can check to confirm *x* ∈ L. Think of it like a jigsaw puzzle: finding the solution may take an enormous amount of trial and error, but if someone hands you the completed puzzle, you can quickly verify it's correct by checking that all pieces fit. The completed puzzle is the certificate.

Consider the problem CLIQUE: given a graph G and a number k, does G contain a complete subgraph of k vertices? This is in NP because if someone claims the answer is "yes" and hands you k specific vertices as the certificate, you can verify in polynomial time that every pair of those vertices is connected by an edge. You don't need to search through all possible subsets — you just check the proposed solution. Similarly, for SAT (Boolean satisfiability), a certificate is a specific truth assignment to all variables; verifying that it satisfies every clause takes linear time in the formula length.

Every problem in P is automatically in NP — if you can *solve* a problem in polynomial time, you can certainly *verify* a solution in polynomial time (just solve it yourself and compare). So P ⊆ NP. The monumental open question is whether this containment is strict: does P = NP? If P = NP, then every problem whose solutions can be efficiently verified can also be efficiently solved — a staggering collapse that would break most of modern cryptography and solve countless optimization problems overnight. Most computer scientists believe P ≠ NP, meaning there exist problems where checking is fundamentally easier than finding. But despite decades of effort, no one has proven this. The P vs NP question is one of the seven Millennium Prize Problems, with a million-dollar bounty for its resolution.
