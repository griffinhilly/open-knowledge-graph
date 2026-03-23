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
status: validated
---

# Complexity Class NP: Nondeterministic Polynomial Time

## Core Idea
NP contains languages decided by nondeterministic TMs in polynomial time. Equivalently, NP is languages where yes-instances admit polynomial-size certificates verifiable in polynomial time. Many practical hard problems (SAT, clique, TSP decision version) are NP. The P vs NP question asks: is guessing-and-checking as fast as deterministic solving? Most believe P ≠ NP, but it remains open.

## Questions

```yaml
- question: "A student claims: 'The Traveling Salesman Problem is in NP, which means it definitely cannot be solved in polynomial time.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing is wrong — being in NP means a problem is outside P by definition"
    - "The reasoning confuses NP with 'non-polynomial.' NP means solutions can be verified in polynomial time; whether NP problems can also be solved in polynomial time is exactly the open P vs NP question"
    - "The Traveling Salesman Problem is not actually in NP"
    - "NP problems can always be solved in polynomial time — the student has the definition of P wrong"
  answer: 1
  explanation: "NP stands for 'nondeterministic polynomial time,' not 'not polynomial.' NP contains problems whose proposed solutions can be verified in polynomial time. Since P ⊆ NP, every problem in P is also in NP. Whether there are NP problems that cannot be solved in polynomial time — whether P ≠ NP — is the most famous open problem in computer science. Saying 'in NP therefore not in P' assumes the answer to that question, which remains unresolved."

- question: "For the CLIQUE problem (does graph G contain a complete subgraph of k vertices?), what serves as a polynomial-size certificate for a 'yes' instance?"
  type: multiple-choice
  options:
    - "A complete enumeration of all subsets of vertices, confirming that at least one of size k is a clique"
    - "A specific list of k vertices that can be checked in polynomial time to confirm every pair is connected by an edge"
    - "The full adjacency matrix of G, which encodes all edge information"
    - "A proof that no efficient algorithm can determine k-clique membership"
  answer: 1
  explanation: "A certificate for a 'yes' instance must be checkable in polynomial time. For CLIQUE, the certificate is a specific set of k vertex identifiers. Verification is straightforward: for each pair among the k vertices, check whether an edge exists — that's O(k²) checks, which is polynomial. Finding the clique may require examining exponentially many subsets, but verifying a claimed clique is easy. This asymmetry between finding and checking is the essence of NP."

- question: "Every problem in P is also in NP."
  type: true-false
  answer: true
  explanation: "If you can solve a problem in polynomial time, you can certainly verify a proposed solution in polynomial time — just solve the problem yourself and compare. Therefore P ⊆ NP. The open question is whether this containment is strict (P ≠ NP, meaning some NP problems have no polynomial-time deterministic solution) or whether all NP problems are also efficiently solvable (P = NP). Either way, P being a subset of NP is uncontroversial."

- question: "NP is the class of problems that cannot be solved in polynomial time."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about NP. NP does not mean 'not polynomial.' NP stands for 'nondeterministic polynomial time' and contains problems whose solutions can be verified in polynomial time. Whether NP problems can also be solved in polynomial time is the P vs NP question — still unsolved after decades. Many NP problems may well be in P; we simply don't know how to prove or disprove it. The 'NP = hard problems' interpretation is an intuition, not the definition."

- question: "Why would a proof that P = NP be catastrophic for modern cryptography?"
  type: short-answer
  answer: "Cryptographic security relies on the assumption that certain problems — like factoring large integers (underlying RSA) or computing discrete logarithms — are easy to verify but computationally infeasible to solve. If P = NP, every problem whose solutions can be verified in polynomial time can also be found in polynomial time. That would mean breaking encryption keys is as fast as verifying them, instantly collapsing the security guarantees of virtually all public-key cryptography and digital signatures."
  explanation: "The hardness of problems like integer factorization is assumed but not proven. If P = NP, that assumption fails: efficient algorithms would exist for all NP problems, including the ones cryptographic protocols depend on. Secure communication, online transactions, and authenticated software — all of which rely on one-way functions that are easy to apply but hard to invert — would be fundamentally broken. The entire infrastructure of secure digital communication rests on the conjecture P ≠ NP."
```

## Explainer

You already know that **P** contains problems solvable in polynomial time by a deterministic Turing machine. **NP** — nondeterministic polynomial time — captures a broader and more subtle idea: problems where proposed solutions can be *verified* efficiently, even if finding them from scratch might be hard. The formal definition says a language is in NP if a **nondeterministic** Turing machine can decide it in polynomial time. A nondeterministic TM can "guess" at each step, exploring many computational paths simultaneously. If *any* path leads to acceptance within polynomial steps, the machine accepts.

But the more intuitive and practically useful characterization is the **verifier definition**. A language L is in NP if there exists a polynomial-time deterministic TM (called a verifier) and a constant *c* such that for every string *x* in L, there exists a **certificate** (also called a witness) of length at most |*x*|^*c* that the verifier can check to confirm *x* ∈ L. Think of it like a jigsaw puzzle: finding the solution may take an enormous amount of trial and error, but if someone hands you the completed puzzle, you can quickly verify it's correct by checking that all pieces fit. The completed puzzle is the certificate.

Consider the problem CLIQUE: given a graph G and a number k, does G contain a complete subgraph of k vertices? This is in NP because if someone claims the answer is "yes" and hands you k specific vertices as the certificate, you can verify in polynomial time that every pair of those vertices is connected by an edge. You don't need to search through all possible subsets — you just check the proposed solution. Similarly, for SAT (Boolean satisfiability), a certificate is a specific truth assignment to all variables; verifying that it satisfies every clause takes linear time in the formula length.

Every problem in P is automatically in NP — if you can *solve* a problem in polynomial time, you can certainly *verify* a solution in polynomial time (just solve it yourself and compare). So P ⊆ NP. The monumental open question is whether this containment is strict: does P = NP? If P = NP, then every problem whose solutions can be efficiently verified can also be efficiently solved — a staggering collapse that would break most of modern cryptography and solve countless optimization problems overnight. Most computer scientists believe P ≠ NP, meaning there exist problems where checking is fundamentally easier than finding. But despite decades of effort, no one has proven this. The P vs NP question is one of the seven Millennium Prize Problems, with a million-dollar bounty for its resolution.
