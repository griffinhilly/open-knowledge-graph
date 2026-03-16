---
id: sat-boolean-satisfiability-computability-and-complexity
title: Boolean Satisfiability (SAT)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: satisfiability-and-unsatisfiability
  type: hard
- id: np-and-polynomial-time
  type: hard
- id: boolean-algebra
  type: hard
- id: boolean-functions-and-circuits
  type: soft
builds-toward:
- three-sat-np-complete
tags:
- satisfiability
- np
- decision-problems
stage: advanced
status: draft
---

# Boolean Satisfiability (SAT)

## Core Idea
The Boolean satisfiability problem asks whether a propositional formula can be made true by assigning truth values to its variables. SAT is the canonical NP problem: every problem in NP can be reduced to SAT. Despite its centrality, no polynomial-time algorithm is known, and SAT is widely believed to require exponential time in the worst case.

## How It's Best Learned
Experiment with small propositional formulas: try to find assignments making them true. Understand why verifying a satisfying assignment is easy (linear time) but finding one seems hard.

## Common Misconceptions
- SAT is tractable because individual assignments can be checked quickly (confuses verification with solving).
- SAT-solvers are polynomial-time algorithms (in fact, SAT-solvers employ heuristics that work well in practice but guarantee no worst-case bound).

## Explainer

You know from your prerequisites that **NP** is the class of decision problems whose solutions can be *verified* in polynomial time — given a candidate answer, a polynomial-time algorithm can confirm or refute it. You also know Boolean algebra: propositional variables taking values true/false, connected by AND (∧), OR (∨), and NOT (¬). The **Boolean satisfiability problem (SAT)** asks: given a propositional formula, is there an assignment of true/false to its variables that makes the whole formula evaluate to true? For example, (x₁ ∨ ¬x₂) ∧ (x₂ ∨ x₃) is satisfied by x₁ = true, x₂ = false, x₃ = anything. SAT is in NP because if you're given a satisfying assignment, you can verify it in linear time by just evaluating the formula.

The deeper result — the **Cook-Levin theorem** — is that SAT is **NP-complete**: not just in NP, but as hard as any problem in NP. This means every problem in NP can be reduced to SAT in polynomial time. The argument is constructive: for any NP problem with a polynomial-time verifier, you encode the verifier's computation as a Boolean formula whose satisfying assignments correspond exactly to the accepting computations on inputs that are yes-instances. The encoding captures the entire tableau of the verifier step by step. If you could solve SAT in polynomial time, you could solve every NP problem in polynomial time — so P = NP. SAT is thus the "first" NP-complete problem and the canonical benchmark for computational hardness.

The **asymmetry between verification and search** is at the heart of why SAT is hard. Checking that an assignment satisfies a formula takes O(n) time — you just evaluate each clause. But *finding* a satisfying assignment requires exploring a space of 2^n possible assignments in the worst case, and no algorithm is known that avoids this exponential blowup in general. This gap between easy verification and apparently hard search is the defining feature of NP-complete problems. The open P vs. NP question is precisely asking whether this gap is real or whether clever polynomial-time search algorithms exist for SAT (and therefore all of NP).

Modern **SAT-solvers** (like DPLL and CDCL-based tools) exploit structure in real-world instances — unit propagation, conflict-driven clause learning, smart branching heuristics — to solve instances with millions of variables in practice. These solvers are foundational tools in hardware verification, planning, and constraint satisfaction. But they are not polynomial-time algorithms; they have no worst-case guarantee that avoids exponential time. The practical tractability of most real-world SAT instances is a separate empirical fact from the theoretical worst-case hardness — a crucial distinction that separates algorithm engineering from complexity theory.
