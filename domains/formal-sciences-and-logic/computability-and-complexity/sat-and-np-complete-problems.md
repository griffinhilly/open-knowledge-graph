---
id: sat-and-np-complete-problems
title: Boolean Satisfiability and Standard NP-Complete Problems
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: cook-levin-theorem-formal
  type: hard
- id: nondeterministic-polynomial-time-computability-and-complexity
  type: hard
- id: polynomial-time-computation-fundamentals
  type: soft
builds-toward:
- np-completeness-reduction-proof-techniques
tags:
- SAT
- NP-completeness
- hard-problems
stage: formal-systems
status: validated
---

# Boolean Satisfiability and Standard NP-Complete Problems

## Core Idea
SAT (Boolean satisfiability) is NP-complete by the Cook-Levin theorem: any NP problem reduces to SAT in polynomial time. Other canonical NP-complete problems—3-SAT, independent set, vertex cover, Hamiltonian path—form a landscape of computationally hard problems. Solving SAT efficiently would imply P = NP and break modern cryptography.

## Questions

```yaml
- question: "A researcher wants to prove that a new graph problem X is NP-complete. They show that X reduces to 3-SAT in polynomial time. Is this proof complete?"
  type: multiple-choice
  options:
    - "Yes — showing X reduces to 3-SAT proves X is at least as hard as 3-SAT, establishing NP-hardness"
    - "No — the reduction goes the wrong direction. To prove X is NP-hard, you must show 3-SAT reduces to X, not X to 3-SAT"
    - "Yes — any polynomial-time reduction between two NP problems establishes that they are both NP-complete"
    - "No — the researcher must also reduce X to the independent set problem, since reductions from 3-SAT alone are insufficient"
  answer: 1
  explanation: "This is the most common error in NP-completeness arguments. If X reduces to 3-SAT, then X is no harder than 3-SAT — a polynomial-time algorithm for 3-SAT would solve X. But this only shows X ∈ NP (or easier); it says nothing about X being hard. To prove X is NP-hard, you must show that 3-SAT (or another NP-complete problem) reduces to X — meaning X is at least as hard as 3-SAT. Hardness transfers in the direction of the reduction: A reduces to B means B is at least as hard as A."

- question: "Suppose someone proves that CLIQUE (the problem of finding a complete subgraph of size k) can be solved in polynomial time. What is the immediate implication?"
  type: multiple-choice
  options:
    - "SAT can be solved in polynomial time, because CLIQUE reduces to SAT via graph complement"
    - "Every problem in NP can be solved in polynomial time, because CLIQUE is NP-complete and a polynomial algorithm for any NP-complete problem implies P = NP"
    - "Only graph problems in NP can be solved in polynomial time; number-theoretic problems like factoring remain hard"
    - "CLIQUE can be solved in polynomial time, but other NP-complete problems remain hard until independent proofs are given"
  answer: 1
  explanation: "CLIQUE is NP-complete. By definition of NP-completeness, every problem in NP reduces to CLIQUE in polynomial time. If CLIQUE has a polynomial-time algorithm, then every NP problem can be solved in polynomial time by first reducing to CLIQUE, then solving it. This would establish P = NP, meaning the entire class NP collapses to P. This includes factoring-based cryptography, RSA, and all other NP problems — a catastrophic consequence for cryptography."

- question: "To prove a new problem X is NP-complete, it is sufficient to show that X is in NP and that some known NP-complete problem reduces to X in polynomial time."
  type: true-false
  answer: true
  explanation: "This is the standard two-step method for NP-completeness proofs. Step 1: show X ∈ NP by exhibiting a polynomial-time verifier — a procedure that, given a candidate solution, checks its correctness in polynomial time. Step 2: show a known NP-complete problem (commonly 3-SAT) reduces to X in polynomial time, establishing that X is NP-hard. Together, X ∈ NP and X being NP-hard make X NP-complete. You need both: NP-hardness alone doesn't place X in NP (it could be harder than NP), and membership in NP alone doesn't establish hardness."

- question: "If a new problem X reduces to 3-SAT in polynomial time, then X is expected to be NP-complete."
  type: true-false
  answer: false
  explanation: "This is the direction error again, now stated as a true-false. X reducing to 3-SAT means X is no harder than 3-SAT — any polynomial solution for 3-SAT would also solve X. This shows X ∈ NP (assuming X is a decision problem), but it says nothing about whether X is NP-hard. Many problems in P reduce to 3-SAT (since every problem in P trivially reduces to any problem), yet P problems are definitely not NP-complete (assuming P ≠ NP). NP-completeness requires showing that 3-SAT (or another NP-complete problem) reduces TO X."

- question: "Explain why the direction of a polynomial-time reduction matters when establishing NP-completeness, using an example."
  type: short-answer
  answer: "Reductions transfer hardness in one direction: if A reduces to B, then B is at least as hard as A. To prove problem X is NP-hard, you must show a known hard problem reduces TO X — meaning X can 'simulate' any NP-complete problem, so it must be at least as hard. For example, to prove INDEPENDENT SET is NP-complete, you reduce 3-SAT to INDEPENDENT SET (building a graph gadget from the 3-SAT formula). If INDEPENDENT SET could be solved in polynomial time, that solution would solve 3-SAT — proving the hardness transfer. Reducing INDEPENDENT SET to 3-SAT would only show INDEPENDENT SET is in NP, not that it is hard."
  explanation: "The intuition: 'A reduces to B' means 'solving B is enough to solve A.' So if A is known to be hard and A reduces to B, then B must also be hard — if B were easy, A would be easy too. The reduction must go from the known hard problem to the problem you want to prove hard. Getting the direction reversed is the single most common mistake in complexity theory proofs."
```

## Explainer

From the Cook-Levin theorem you already know that SAT is NP-complete: any nondeterministic polynomial-time computation can be encoded as a Boolean formula, so SAT captures the hardest problems in NP. But the Cook-Levin proof produces complicated formulas — exponentially large circuits of gates. In practice, nearly everything in complexity theory reduces not directly from SAT but from a simplified variant: **3-SAT**, where every clause has *exactly three literals*. The reduction from SAT to 3-SAT is a key exercise: replace a clause with k > 3 literals by introducing fresh auxiliary variables and a chain of 3-literal clauses that is satisfiable iff the original was. 3-SAT is easier to reduce *from* than SAT because its structure is rigid and uniform, making it the primary workhorse for NP-completeness proofs.

The landscape of NP-complete problems is built by a web of polynomial-time reductions. **Independent set** asks: does a graph contain k vertices with no edge between any pair? **Vertex cover** asks: do k vertices touch every edge? These two are complementary — S is an independent set iff the complement V \ S is a vertex cover — so they reduce to each other trivially. **Clique** — does the graph contain a complete subgraph on k vertices? — reduces to independent set by complementing the graph. **Hamiltonian path** and **Hamiltonian cycle** ask whether a graph has a path or cycle visiting every vertex exactly once, and these reduce from 3-SAT by gadget constructions that force the Hamiltonian path to "choose" truth assignments. **Subset sum** — can a subset of integers sum to a target T? — is NP-complete too, showing that number-theoretic problems are not inherently easier than graph problems.

The unifying principle behind all these reductions is that **hardness transfers**: if problem A reduces to problem B, then B is at least as hard as A. Once you know 3-SAT is NP-complete, proving that a new problem X is NP-complete requires only (1) showing X is in NP (exhibit a polynomial-time verifier) and (2) showing 3-SAT (or any NP-complete problem) reduces to X in polynomial time. You pick whichever NP-complete problem is most convenient to reduce from. The skill in NP-completeness proofs is designing reduction gadgets that faithfully translate the source problem's structure into the target problem's language.

The practical consequence is stark. If any NP-complete problem were solvable in polynomial time, every NP problem would be — including factoring large integers and breaking RSA. Modern cryptography, blockchain systems, and secure communication rely on the assumed hardness of NP problems (or problems believed to be at least as hard). Solving SAT efficiently would unravel cryptographic security across the internet. This is why NP-completeness is not an abstract curiosity but a load-bearing pillar of both theoretical computer science and practical security.
