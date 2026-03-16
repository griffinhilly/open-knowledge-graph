---
id: np-completeness
title: NP-Completeness and Cook-Levin Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: nondeterministic-polynomial-time
  type: hard
tags:
- np-completeness
- cook-levin
- hardness
stage: abstract-reasoning
status: draft
---

# NP-Completeness and Cook-Levin Theorem

## Core Idea
A language is NP-complete if it is in NP and every language in NP reduces to it in polynomial time. The Cook-Levin theorem proves that boolean satisfiability (SAT) is NP-complete. NP-complete problems are presumed intractable; a polynomial-time algorithm for any NP-complete problem would imply P = NP.

## Questions

```yaml
- question: "Which of the following best describes what it means for a problem to be NP-complete?"
  type: multiple-choice
  options: ["It has no solution", "It is in NP and every problem in NP reduces to it in polynomial time", "It cannot be solved by any deterministic algorithm", "It can only be solved in exponential time"]
  answer: 1
  explanation: "NP-completeness requires two things: (1) the problem is in NP — a proposed solution can be verified in polynomial time — and (2) every problem in NP reduces to it in polynomial time, making it at least as hard as any NP problem. It does not mean unsolvable; it means no polynomial-time deterministic algorithm is known."

- question: "Because no polynomial-time algorithm has ever been found for any NP-complete problem, it has been proven that P ≠ NP."
  type: true-false
  answer: false
  explanation: "The absence of a known polynomial-time algorithm does not constitute a mathematical proof that none exists. P ≠ NP is one of the most famous open problems in mathematics — the Clay Millennium Prize Problem. We strongly believe NP-complete problems are intractable, but 'conjectured' and 'proven' are fundamentally different things in theoretical computer science."

- question: "Why does finding a polynomial-time algorithm for any single NP-complete problem imply that P = NP?"
  type: short-answer
  answer: "Every problem in NP reduces to every NP-complete problem in polynomial time. So if you can solve one NP-complete problem in polynomial time, you can solve any NP problem in polynomial time by first applying the polynomial reduction and then running the polynomial algorithm. That means NP ⊆ P, and since P ⊆ NP already, P = NP."
  explanation: "The reduction structure is the key: NP-completeness means every NP problem is 'no harder than' the NP-complete problem, up to polynomial overhead. A poly-time solution to the NP-complete problem, composed with poly-time reductions from all other NP problems, yields poly-time algorithms for all of NP. The entire class collapses."
```

## Explainer

From your study of nondeterministic polynomial time (NP), you know that NP is the class of decision problems whose solutions can be *verified* in polynomial time — even if finding a solution might seem hard. NP-completeness identifies a special core within NP: the problems that are, in a formal sense, maximally difficult for the entire class.

A problem is NP-complete if it satisfies two conditions. First, it must be in NP — a witness (a proposed solution) can be checked efficiently. Second, every problem in NP must be polynomial-time reducible to it. This second condition is what makes NP-complete problems remarkable: they are universal difficulty benchmarks. If you could solve one NP-complete problem in polynomial time, the reduction structure would give you polynomial-time algorithms for *every* problem in NP — and we would have P = NP.

The Cook-Levin theorem established the first NP-complete problem: boolean satisfiability (SAT). The proof works by showing that any nondeterministic polynomial-time computation can be encoded as a SAT instance — the variables represent the bits of the machine's computation and the clauses enforce the machine's transition rules. This was a profound result: it showed that SAT captures all of NP inside it. Once SAT was known to be NP-complete, proving other problems NP-complete became easier — you just need to show they are in NP and that SAT (or some already-known NP-complete problem) reduces to them in polynomial time.

It is important to resist two common misreadings. First, NP-complete does not mean "impossible" or "unsolvable" — it means no polynomial-time algorithm is currently known. For small instances, many NP-complete problems are solved routinely by exact or approximation algorithms. Second, and more subtly, the conjecture that P ≠ NP is still *unproven*. We believe it strongly — intuitively, verifying a solution feels easier than finding one — but a mathematical proof has eluded computer scientists for over fifty years. The P vs. NP question remains open.

For practical purposes, proving that your problem is NP-complete is actually useful: it tells you to stop searching for an efficient exact algorithm and instead look to approximation algorithms, heuristics, or special-case structure. It shifts the question from "why can't I solve this efficiently?" to "what is the best we can do given this hardness?"

