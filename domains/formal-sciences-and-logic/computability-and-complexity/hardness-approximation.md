---
id: hardness-approximation
title: Hardness of Approximation Introduction
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: approximation-algorithms
  type: hard
- id: three-sat-reductions
  type: hard
- id: approximation-hardness-results
  type: soft
tags:
- approximation-hardness
- inapproximability
- reductions
- lower-bounds
stage: advanced
status: validated
---
# Hardness of Approximation Introduction

## Core Idea
Even when a problem is NP-hard, we sometimes compute approximate solutions rather than exact ones. Hardness of approximation results show that some NP-hard problems are also hard to approximate: there exist constants c > 1 such that achieving a c-approximation is NP-hard. These results reveal fundamental limits to what approximation algorithms can achieve.

## How It's Best Learned
Study the PCP (Probabilistically Checkable Proofs) theorem at an intuitive level. Work through one inapproximability result, like the maximal independent set hardness.

## Questions

```yaml
- question: "A research paper proves that achieving a 1.5-approximation for Problem X is NP-hard. What does this mean in practice?"
  type: multiple-choice
  options:
    - "No algorithm can solve Problem X at all, even approximately"
    - "Any polynomial-time algorithm for Problem X must return solutions within a factor of 1.5 of optimal"
    - "No polynomial-time algorithm can guarantee a solution within a factor of 1.5 of optimal — unless P = NP"
    - "Problem X is harder than NP-hard, placing it in a strictly higher complexity class"
  answer: 2
  explanation: "An inapproximability result of ratio ρ means that a ρ-approximation algorithm would imply P = NP — so no such algorithm exists under the standard assumption. It does NOT mean no algorithm can solve the problem at all (exact exponential-time solutions exist), and it doesn't say anything about what approximations can be achieved in superpolynomial time. Problem X remains NP-hard; inapproximability is a statement about what polynomial-time algorithms can guarantee, not a reclassification into a higher class."

- question: "What distinguishes a gap-preserving reduction (used in inapproximability proofs) from an ordinary polynomial-time NP-hardness reduction?"
  type: multiple-choice
  options:
    - "Gap-preserving reductions must run in linear time; ordinary reductions only need polynomial time"
    - "Gap-preserving reductions preserve a gap in objective value between YES and NO instances, showing that even approximate discrimination is hard; ordinary reductions only need to preserve feasibility"
    - "Gap-preserving reductions work on maximization problems; ordinary reductions work on decision problems"
    - "Gap-preserving reductions require the PCP theorem as a subroutine in the reduction itself"
  answer: 1
  explanation: "An ordinary NP-hardness reduction from 3-SAT to Problem X maps satisfiable instances to YES instances and unsatisfiable ones to NO instances, showing exact solution is hard. A gap-preserving reduction additionally ensures that YES instances have objective value ≥ α (high) and NO instances have objective value ≤ β (low), with α/β > ρ. This gap means that any ρ-approximation algorithm would solve the 3-SAT instance — so approximation within ratio ρ is also NP-hard. The reduction must carefully track how transformation affects objective values, not just feasibility."

- question: "The PCP theorem implies that for some constant ε > 0, no polynomial-time algorithm can achieve a (1 − ε)-approximation for MAX-3SAT unless P = NP."
  type: true-false
  answer: true
  explanation: "This is one of the foundational consequences of the PCP theorem. The theorem provides a characterization of NP where proofs can be checked by reading only a constant number of bits — this yields a gap in the MAX-3SAT instance (satisfiable vs. at most (1−ε)-satisfiable) that is NP-hard to close. Any polynomial-time approximation beyond this constant ratio would allow efficient discrimination of satisfiable from nearly-unsatisfiable instances, collapsing NP into P. This base inapproximability for MAX-3SAT propagates via gap-preserving reductions to other problems."

- question: "Since most NP-hard problem is hard to solve exactly, no NP-hard optimization problem can be efficiently approximated to within any fixed constant ratio."
  type: true-false
  answer: false
  explanation: "This is the core misconception that hardness of approximation addresses. Many NP-hard optimization problems admit excellent approximation algorithms: Vertex Cover has a 2-approximation, various scheduling problems admit polynomial-time approximation schemes (PTAS) achieving (1+ε)-approximation for any ε > 0. NP-hardness of exact solution says nothing directly about approximability. Hardness of approximation is a *separate, additional* result showing that for specific problems, even approximation to within certain ratios is NP-hard. Some NP-hard problems are easy to approximate; others (like MAX-CLIQUE) are essentially impossible."

- question: "Why does proving that a problem is NP-hard not automatically tell you how hard it is to approximate, and what additional machinery is needed?"
  type: short-answer
  answer: "An NP-hardness proof shows that no polynomial-time algorithm can find the exact optimal solution unless P = NP — but it says nothing about finding a near-optimal solution. To show approximation hardness, you need a gap-preserving reduction that maps YES instances to instances with high objective value and NO instances to instances with low objective value, such that any approximation algorithm achieving ratio ρ would distinguish them and solve the NP-hard source problem. The PCP theorem is the key tool that creates this gap 'for free' for MAX-3SAT — it reformulates satisfiability so that valid proofs are accepted and invalid ones are rejected with constant probability using only constant-many bit checks, which directly translates into a multiplicative gap in the MAX-3SAT objective."
  explanation: "The conceptual shift is from 'can you find an exact solution?' to 'can you distinguish between a solution near the optimum and one far from it?' A problem can be NP-hard to solve exactly but still easy to approximate (e.g., some scheduling problems). The PCP theorem is surprising precisely because it shows this isn't always the case — for some problems, even approximation within a constant factor is as hard as exact solution."
```

## Explainer

From your study of approximation algorithms, you know the standard framework: since many optimization problems are NP-hard to solve exactly, we settle for algorithms that return solutions within a provable factor of optimal. A **ρ-approximation algorithm** guarantees an answer no worse than ρ times the optimal value. For some problems this works beautifully — the greedy algorithm gives a 2-approximation for vertex cover, and more sophisticated methods give (1 + ε)-approximations for many scheduling and packing problems. The natural question is: how far does this go? Can every NP-hard optimization problem be approximated to within any fixed ratio?

The answer is no, and **hardness of approximation** results make this precise. These results show that for certain NP-hard problems, even achieving a ρ-approximation is NP-hard — meaning no polynomial-time algorithm can guarantee that ratio unless P = NP. The key tool is the **PCP theorem** (Probabilistically Checkable Proofs), which provides a reformulation of NP: every NP language has a proof system where a verifier can check a proof by reading only a *constant* number of bits, with the guarantee that valid proofs are always accepted and invalid proofs are rejected with probability at least 1/2. This may seem unrelated to approximation, but the connection is powerful.

The PCP theorem implies inapproximability via **gap amplification**: if you could approximate MAX-3SAT to within a ratio better than some constant c < 1, you could distinguish satisfiable instances from highly unsatisfiable ones — which the PCP theorem shows is NP-hard. Concretely, there is a constant ε > 0 such that no polynomial-time algorithm achieves a (1 − ε)-approximation for MAX-3SAT unless P = NP. From this "base" inapproximability, reductions from your prerequisite work propagate hardness to other problems. The MAX-CLIQUE problem is especially striking: it cannot be approximated within a factor of n^(1−ε) for any ε > 0 unless P = NP — so the approximability gap is polynomial, not just a small constant.

The conceptual shift from NP-hardness reductions to inapproximability reductions is worth emphasizing. An ordinary reduction from 3-SAT to a problem X shows that exact optimization is hard. A *gap-preserving* reduction preserves a gap in the objective value between YES and NO instances — it shows that even finding a solution in the gap is hard. Constructing such reductions requires careful attention to how the transformation affects objective values, not just feasibility. This is why inapproximability proofs tend to be more intricate than their exact-hardness counterparts, and why the PCP theorem — which creates the initial gap "for free" — is such a powerful foundation for the whole theory.
