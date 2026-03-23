---
id: boolean-satisfiability-and-reductions
title: Boolean Satisfiability, Cook-Levin, and Reductions
domain: computer-science
course: theory-of-computation
prerequisites:
- id: cook-levin-theorem
  type: hard
- id: np-completeness-and-hardness
  type: soft
builds-toward:
- space-complexity-definitions
tags:
- sat
- 3sat
- cook-levin
- cnf
- reduction
- canonical
stage: advanced
status: validated
---

# Boolean Satisfiability, Cook-Levin, and Reductions

## Core Idea
SAT (Boolean satisfiability) asks if a CNF formula has a satisfying assignment. Cook-Levin theorem proves SAT is NP-complete by showing every NP language reduces to SAT—establishing SAT as canonical. 3-SAT (3 literals per clause) is NP-complete. Reductions from SAT prove other problems NP-complete: map satisfying assignments to solutions of the target problem.

## Questions

```yaml
- question: "A researcher wants to prove that CLIQUE is NP-complete. She has already shown CLIQUE is in NP. Which correctly describes the next step?"
  type: multiple-choice
  options:
    - "Reduce CLIQUE to 3-SAT in polynomial time"
    - "Reduce 3-SAT to CLIQUE in polynomial time"
    - "Show CLIQUE reduces to SAT, then SAT reduces back to CLIQUE"
    - "Show that any algorithm for CLIQUE can directly solve SAT"
  answer: 1
  explanation: "To show NP-hardness, you reduce a *known* NP-complete problem (3-SAT) TO the *target* problem (CLIQUE). This proves CLIQUE is at least as hard as 3-SAT: a polynomial-time algorithm for CLIQUE would immediately yield one for 3-SAT. Option A gets the direction backwards — reducing CLIQUE to 3-SAT only shows CLIQUE is no harder than 3-SAT (i.e., CLIQUE ∈ NP), which you already knew. The direction of reduction is the most common confusion in NP-completeness proofs."

- question: "The Cook-Levin theorem proves SAT is NP-complete. What does the NP-hardness part of this mean precisely?"
  type: multiple-choice
  options:
    - "SAT cannot be solved in polynomial time"
    - "SAT is the hardest problem solvable in polynomial space"
    - "Every language in NP can be reduced to SAT in polynomial time"
    - "SAT can solve every NP problem without any reduction"
  answer: 2
  explanation: "NP-hardness means every language in NP polynomial-time reduces TO SAT — if you could solve SAT efficiently, you could solve any NP problem by first transforming it into SAT. Cook-Levin establishes this by showing the accepting computations of any nondeterministic polynomial-time TM can be encoded as a satisfiable CNF formula. Crucially, the theorem does not *prove* SAT is intractable (that would require proving P ≠ NP) — it only shows SAT is at least as hard as every other NP problem."

- question: "If problem A reduces to problem B in polynomial time, and B is in P, then A must also be in P."
  type: true-false
  answer: true
  explanation: "This is the core property that makes polynomial-time reductions useful. If A ≤_p B, you solve any instance of A by: (1) running the polynomial-time reduction to produce a B instance, then (2) running the polynomial-time algorithm for B. The composition of two polynomial-time procedures is polynomial-time, so A ∈ P. This is why NP-completeness is so consequential: if any NP-complete problem is in P, then P = NP, because every NP language reduces to that problem."

- question: "To prove SUBSET-SUM is NP-complete, it suffices to reduce SUBSET-SUM to 3-SAT in polynomial time."
  type: true-false
  answer: false
  explanation: "This gets the reduction direction backwards — the most common error in NP-completeness arguments. Reducing SUBSET-SUM *to* 3-SAT shows SUBSET-SUM is no harder than 3-SAT (i.e., SUBSET-SUM ∈ NP). To prove NP-hardness, you must reduce *from* 3-SAT *to* SUBSET-SUM: given a 3-SAT formula, construct a SUBSET-SUM instance that is solvable if and only if the formula is satisfiable. That shows any polynomial algorithm for SUBSET-SUM would also solve 3-SAT."

- question: "Why does the Cook-Levin proof encode a Turing machine's computation as a CNF formula, and what do the variables in that formula represent?"
  type: short-answer
  answer: "To show every NP language L reduces to SAT, the proof takes the nondeterministic polynomial-time TM M for L and constructs a CNF formula that is satisfiable iff M accepts the input. Variables represent the configuration at each time step: the machine's state, head position, and tape cell contents. Clauses enforce that each step follows M's transition function, the initial configuration matches the input, and some accepting state is reached. A satisfying assignment corresponds exactly to an accepting computation history."
  explanation: "The insight is that 'does an accepting computation exist?' is a combinatorial question about a table of configurations, and CNF clauses naturally express local consistency constraints between adjacent table cells. The formula size is polynomial because M runs in polynomial time, making the computation table polynomial-sized. This translation is the conceptual bridge between abstract nondeterministic computation and concrete logical satisfiability."
```

## Explainer

The **Boolean satisfiability problem** (SAT) asks a seemingly straightforward question: given a Boolean formula — a logical expression built from variables, AND, OR, and NOT — is there some assignment of true/false values to the variables that makes the entire formula evaluate to true? The formula is typically presented in **conjunctive normal form** (CNF): a conjunction (AND) of clauses, where each clause is a disjunction (OR) of literals (variables or their negations). For example, (x₁ ∨ ¬x₂) ∧ (x₂ ∨ x₃) ∧ (¬x₁ ∨ ¬x₃) is a CNF formula with three clauses. You need to find values for x₁, x₂, x₃ that satisfy all three clauses simultaneously — or determine that no such assignment exists.

SAT is clearly in NP: if someone hands you a proposed assignment, you can plug in the values and check each clause in linear time. But the **Cook-Levin theorem** proves something far deeper — SAT is **NP-complete**, meaning it is at least as hard as every other problem in NP. The proof works by showing that for *any* language L in NP, with its nondeterministic polynomial-time TM M, you can construct a CNF formula that is satisfiable if and only if M accepts the input. The formula encodes the entire computation: variables represent the state, head position, and tape contents at each time step, and clauses enforce that each step follows M's transition function. A satisfying assignment literally *is* an accepting computation history. This construction is the bridge that connects abstract nondeterministic computation to concrete logical formulas.

**3-SAT** restricts each clause to exactly three literals, and it remains NP-complete. The reduction from general SAT to 3-SAT introduces auxiliary variables to break long clauses into chains of three-literal clauses while preserving satisfiability. The importance of 3-SAT is practical: it's a cleaner, more structured starting point for reductions to other problems. To prove a new problem X is NP-complete, you show that 3-SAT (or any known NP-complete problem) **reduces** to X in polynomial time — meaning you can transform any 3-SAT instance into an instance of X such that the 3-SAT formula is satisfiable if and only if the X instance has a solution.

This reduction technique is the workhorse of complexity theory. Hundreds of problems have been proven NP-complete through chains of reductions, all tracing back to SAT via Cook-Levin. Each reduction is a polynomial-time translation that maps satisfying assignments to solutions of the target problem and vice versa. For example, reducing 3-SAT to CLIQUE involves constructing a graph where each clause becomes a group of vertices (one per literal), with edges connecting compatible literals from different clauses; a k-clique in this graph corresponds to a satisfying assignment. The art of NP-completeness proofs lies in designing these gadgets — structural components in the target problem that faithfully simulate the logical constraints of SAT. Once you establish that a problem is NP-complete, you know that a polynomial-time algorithm for it would imply P = NP, effectively ruling out efficient exact solutions under the widely believed conjecture that P ≠ NP.
