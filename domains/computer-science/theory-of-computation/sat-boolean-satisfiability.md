---
id: sat-boolean-satisfiability
title: 'SAT: Boolean Satisfiability Problem'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: complexity-class-np-definition
  type: hard
- id: boolean-satisfiability-and-reductions
  type: hard
tags:
- np-complete
- satisfiability
- canonical-problem
stage: advanced
status: draft
---

# SAT: Boolean Satisfiability Problem

## Core Idea
The SAT problem asks: given a Boolean formula in conjunctive normal form (CNF), does an assignment exist making the formula true? SAT is the canonical NP-complete problem (Cook-Levin theorem); all other NP-completeness proofs reduce to SAT. Despite its NP-completeness, modern SAT solvers (using DPLL, clause learning, and heuristics) solve many practical instances efficiently, making SAT critical for formal verification, constraint satisfaction, and cryptanalysis.

## How It's Best Learned
Study the Cook-Levin proof of SAT's NP-completeness. Understand CNF representation and conversion. Use SAT solvers on small instances to observe practical tractability despite theoretical hardness.

## Common Misconceptions
Confusing NP-completeness (no known polynomial algorithm) with unsolvability. Thinking practical SAT solvability contradicts NP-completeness (fast heuristics ≠ polynomial guarantee). Assuming all satisfiable formulas are equally hard.

## Explainer

You already know that NP is the class of decision problems where a "yes" answer can be verified in polynomial time given a certificate. The **Boolean Satisfiability Problem (SAT)** asks a deceptively simple question: given a Boolean formula — a logical expression built from variables, AND, OR, and NOT — does there exist an assignment of true/false values to the variables that makes the entire formula evaluate to true? The formula is typically presented in **conjunctive normal form (CNF)**: a conjunction (AND) of clauses, where each clause is a disjunction (OR) of literals (a variable or its negation). For example, (x₁ ∨ ¬x₂) ∧ (x₂ ∨ x₃) ∧ (¬x₁ ∨ ¬x₃) is a 3-CNF formula with three clauses.

SAT occupies a unique position in complexity theory because of the **Cook-Levin theorem**: SAT is NP-complete. This means two things. First, SAT is in NP — given a candidate assignment, you can check in polynomial time whether it satisfies every clause. Second, every problem in NP can be reduced to SAT in polynomial time. The proof works by encoding the entire computation of a nondeterministic Turing machine as a Boolean formula: variables represent the machine's state, head position, and tape contents at each time step, and clauses enforce that the computation follows legal transitions. If the machine accepts, the formula is satisfiable; if not, it is not. This universality makes SAT the "master problem" of NP — if you could solve SAT in polynomial time, you could solve every problem in NP in polynomial time, which would prove P = NP.

What makes SAT fascinating in practice is the gap between worst-case theory and real-world performance. Modern **SAT solvers** based on the DPLL algorithm (Davis-Putnam-Logemann-Loveland) with enhancements like **conflict-driven clause learning (CDCL)**, watched literals, and restart strategies routinely solve instances with millions of variables that arise in hardware verification, software testing, and planning. The key insight is that practical instances have structure — they are not random worst-case formulas. Clause learning lets the solver extract general lessons from dead ends ("if these three variables are set this way, a contradiction is inevitable"), effectively pruning enormous portions of the search space. This does not contradict NP-completeness: worst-case instances remain exponentially hard, but the instances that matter in practice tend to have exploitable structure.

SAT also serves as the foundation for proving other problems NP-complete. Once you have established SAT as NP-complete via the Cook-Levin theorem, you can prove that a new problem Q is NP-complete by reducing SAT to Q in polynomial time (and showing Q is in NP). This is far easier than reducing every NP problem to Q directly. The chain of reductions typically starts at SAT, moves to 3-SAT (every clause has exactly three literals), then branches out to CLIQUE, VERTEX COVER, HAMILTONIAN PATH, and hundreds of other problems. SAT is thus both a theoretical anchor point and a practical computational engine at the heart of modern computer science.
