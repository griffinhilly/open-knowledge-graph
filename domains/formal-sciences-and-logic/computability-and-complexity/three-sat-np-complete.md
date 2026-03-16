---
id: three-sat-np-complete
title: 3-SAT and NP-Completeness via CNF
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: sat-boolean-satisfiability
  type: hard
- id: cook-levin-theorem-formal
  type: hard
- id: np-completeness-formal
  type: hard
builds-toward:
- vertex-cover-problem
- clique-problem-np-complete
tags:
- sat
- cnf
- np-complete
stage: advanced
status: draft
---

# 3-SAT and NP-Completeness via CNF

## Core Idea
3-SAT restricts SAT to formulas in CNF where each clause has exactly three literals. Despite this restriction, 3-SAT remains NP-complete, making it a canonical problem for showing other problems are NP-hard via reduction. The Cook-Levin theorem proves that every NP problem reduces to 3-SAT in polynomial time.

## Explainer

You already know that SAT — the problem of deciding whether a propositional formula has a satisfying assignment — is NP-complete by the Cook-Levin theorem. **3-SAT** restricts SAT to a specific syntactic form: the formula must be in **conjunctive normal form (CNF)**, and every clause must contain exactly three literals. A concrete example is (x₁ ∨ ¬x₂ ∨ x₃) ∧ (¬x₁ ∨ x₂ ∨ x₄) ∧ (x₂ ∨ ¬x₃ ∨ ¬x₄). You need to find an assignment to the variables that makes at least one literal true in every clause simultaneously.

At first glance, restricting each clause to exactly three literals seems like it should make the problem easier — fewer choices per clause. But it doesn't. To prove 3-SAT is NP-complete you need two things: membership in NP (obvious — given an assignment, check each clause in linear time) and a reduction from the general SAT problem. The key step is converting an arbitrary CNF formula into one where every clause has exactly three literals, without changing satisfiability. Clauses with more than three literals can be split using fresh auxiliary variables: a clause (a ∨ b ∨ c ∨ d) becomes (a ∨ b ∨ y) ∧ (¬y ∨ c ∨ d), where y is new. Clauses with fewer than three literals can be padded: (a ∨ b) becomes (a ∨ b ∨ b). This conversion is polynomial, and the resulting formula is satisfiable if and only if the original was.

What makes 3-SAT valuable is not the problem itself but its role as a **reduction source**. Many NP-hardness proofs use 3-SAT rather than general SAT because its regular structure — exactly three literals, clean variable/clause interface — maps more directly onto the combinatorial structures of other problems. The clause structure provides a natural "gadget": each clause is a small constraint that must be satisfied, and the interaction between clauses through shared variables creates the global difficulty. When you reduce 3-SAT to a graph problem, you typically build one gadget per clause and connect gadgets by shared variable nodes.

The fact that 3-SAT is hard despite its extreme syntactic restriction is a deeper insight than it first appears. It says that the difficulty of SAT is not a matter of messy, arbitrary formula structure — it survives even after imposing a very clean, regular form. This robustness is one reason the NP-completeness of 3-SAT is so useful: the regular structure makes reductions *from* 3-SAT easier to design and verify, while the hardness result means any problem that 3-SAT reduces to is at least as hard. The chain from Cook-Levin → SAT → 3-SAT → thousands of other NP-complete problems is the historical spine of computational complexity theory.
