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
status: draft
---

# Boolean Satisfiability, Cook-Levin, and Reductions

## Core Idea
SAT (Boolean satisfiability) asks if a CNF formula has a satisfying assignment. Cook-Levin theorem proves SAT is NP-complete by showing every NP language reduces to SAT—establishing SAT as canonical. 3-SAT (3 literals per clause) is NP-complete. Reductions from SAT prove other problems NP-complete: map satisfying assignments to solutions of the target problem.

## Explainer

The **Boolean satisfiability problem** (SAT) asks a seemingly straightforward question: given a Boolean formula — a logical expression built from variables, AND, OR, and NOT — is there some assignment of true/false values to the variables that makes the entire formula evaluate to true? The formula is typically presented in **conjunctive normal form** (CNF): a conjunction (AND) of clauses, where each clause is a disjunction (OR) of literals (variables or their negations). For example, (x₁ ∨ ¬x₂) ∧ (x₂ ∨ x₃) ∧ (¬x₁ ∨ ¬x₃) is a CNF formula with three clauses. You need to find values for x₁, x₂, x₃ that satisfy all three clauses simultaneously — or determine that no such assignment exists.

SAT is clearly in NP: if someone hands you a proposed assignment, you can plug in the values and check each clause in linear time. But the **Cook-Levin theorem** proves something far deeper — SAT is **NP-complete**, meaning it is at least as hard as every other problem in NP. The proof works by showing that for *any* language L in NP, with its nondeterministic polynomial-time TM M, you can construct a CNF formula that is satisfiable if and only if M accepts the input. The formula encodes the entire computation: variables represent the state, head position, and tape contents at each time step, and clauses enforce that each step follows M's transition function. A satisfying assignment literally *is* an accepting computation history. This construction is the bridge that connects abstract nondeterministic computation to concrete logical formulas.

**3-SAT** restricts each clause to exactly three literals, and it remains NP-complete. The reduction from general SAT to 3-SAT introduces auxiliary variables to break long clauses into chains of three-literal clauses while preserving satisfiability. The importance of 3-SAT is practical: it's a cleaner, more structured starting point for reductions to other problems. To prove a new problem X is NP-complete, you show that 3-SAT (or any known NP-complete problem) **reduces** to X in polynomial time — meaning you can transform any 3-SAT instance into an instance of X such that the 3-SAT formula is satisfiable if and only if the X instance has a solution.

This reduction technique is the workhorse of complexity theory. Hundreds of problems have been proven NP-complete through chains of reductions, all tracing back to SAT via Cook-Levin. Each reduction is a polynomial-time translation that maps satisfying assignments to solutions of the target problem and vice versa. For example, reducing 3-SAT to CLIQUE involves constructing a graph where each clause becomes a group of vertices (one per literal), with edges connecting compatible literals from different clauses; a k-clique in this graph corresponds to a satisfying assignment. The art of NP-completeness proofs lies in designing these gadgets — structural components in the target problem that faithfully simulate the logical constraints of SAT. Once you establish that a problem is NP-complete, you know that a polynomial-time algorithm for it would imply P = NP, effectively ruling out efficient exact solutions under the widely believed conjecture that P ≠ NP.
