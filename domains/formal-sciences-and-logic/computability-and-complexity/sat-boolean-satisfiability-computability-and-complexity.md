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
stage: formal-systems
status: validated
---

# Boolean Satisfiability (SAT)

## Core Idea
The Boolean satisfiability problem asks whether a propositional formula can be made true by assigning truth values to its variables. SAT is the canonical NP problem: every problem in NP can be reduced to SAT. Despite its centrality, no polynomial-time algorithm is known, and SAT is widely believed to require exponential time in the worst case.

## How It's Best Learned
Experiment with small propositional formulas: try to find assignments making them true. Understand why verifying a satisfying assignment is easy (linear time) but finding one seems hard.

## Common Misconceptions
- SAT is tractable because individual assignments can be checked quickly (confuses verification with solving).
- SAT-solvers are polynomial-time algorithms (in fact, SAT-solvers employ heuristics that work well in practice but guarantee no worst-case bound).

## Questions

```yaml
- question: "A software engineer's SAT solver successfully handles one million real-world industrial SAT instances per day with 100% success. She argues this demonstrates P = NP. What is the critical flaw in this reasoning?"
  type: multiple-choice
  options:
    - "SAT is not NP-complete, so solving it efficiently does not imply P = NP"
    - "Practical performance on real-world instances does not establish polynomial worst-case complexity — structured instances that yield to heuristics are not the adversarial inputs that determine complexity"
    - "Her solver uses randomization, which places it outside the deterministic polynomial class P"
    - "NP-completeness requires solving all instances simultaneously, not one at a time"
  answer: 1
  explanation: "Complexity classes are defined by worst-case behavior. A SAT solver can be extraordinarily fast on structured, real-world instances — exploiting unit propagation, conflict-driven clause learning, and clever branching — while still requiring exponential time on carefully constructed adversarial inputs. Proving P = NP requires an algorithm that solves every SAT instance in polynomial time bounded by a polynomial in the input size, without exception. The practical tractability of real-world SAT is an empirical observation about the structure of instances that appear in practice, not a complexity-theoretic result."

- question: "The Cook-Levin theorem establishes that SAT is NP-complete. The most important consequence of this result is:"
  type: multiple-choice
  options:
    - "SAT requires exponential time on all inputs, confirming P ≠ NP"
    - "Every problem in NP can be transformed into a SAT instance in polynomial time, so a polynomial-time SAT algorithm would solve all of NP in polynomial time"
    - "SAT is harder than all other NP-hard problems, making it uniquely difficult"
    - "SAT-solvers are always as efficient as any other algorithm for NP problems"
  answer: 1
  explanation: "NP-completeness combines two facts: (1) SAT ∈ NP (a satisfying assignment can be verified in linear time), and (2) every problem in NP is polynomial-time reducible to SAT. Together, these mean that if SAT could be solved in polynomial time, every NP problem could be solved in polynomial time (P = NP). Cook-Levin does NOT prove SAT requires exponential time — it establishes SAT as the universal representative of NP hardness. The P vs. NP question remains open precisely because no polynomial SAT algorithm has been found, but none has been ruled out."

- question: "Because each assignment to n Boolean variables can be checked in linear time, SAT can be solved in polynomial time."
  type: true-false
  answer: false
  explanation: "This confuses verification with solving — the core distinction in NP theory. Verifying a *given* assignment takes O(n) time: evaluate each clause under the proposed truth values. But *finding* a satisfying assignment (or proving none exists) requires searching among 2^n possible assignments in the worst case. The ability to quickly verify a candidate solution is exactly what places SAT in NP. It says nothing about how quickly the solution can be found. This gap between easy verification and apparently hard search is the defining feature of NP-complete problems and the heart of the P vs. NP question."

- question: "If a polynomial-time algorithm for SAT were discovered, it would prove that P = NP."
  type: true-false
  answer: true
  explanation: "By Cook-Levin, every problem in NP can be reduced to SAT in polynomial time. If SAT ∈ P, then by composition of reductions, every NP problem could be solved in polynomial time: solve the SAT reduction in poly time, giving a poly-time algorithm for the original NP problem. Since P ⊆ NP always holds, this would give P = NP. A polynomial-time SAT algorithm would simultaneously unlock polynomial-time solutions to planning, scheduling, graph coloring, protein structure prediction, integer factoring, and every other NP problem."

- question: "Why does the fact that SAT can be verified in linear time not imply that SAT can be solved in polynomial time?"
  type: short-answer
  answer: "Verification is easy because we are given the answer — just evaluate the formula under the proposed assignment, checking each clause in linear time. Solving requires finding a satisfying assignment without being given one, which means searching a space of 2^n possible truth assignments. No algorithm is known that avoids worst-case exponential exploration of this space. The ability to verify quickly defines membership in NP; solving quickly would require SAT ∈ P. Whether P = NP — i.e., whether every problem with efficient verification also has efficient search — is the central open question in computer science."
  explanation: "The asymmetry between verification and search is the defining structural feature of NP-complete problems. For any specific satisfying assignment, checking it is trivial. The difficulty is that we don't know which of the 2^n assignments satisfies the formula, and eliminating candidates requires exponential work in the worst case. SAT-solvers use heuristics that short-circuit this search for structured instances, but they offer no polynomial worst-case guarantee — consistent with SAT remaining an open problem for worst-case polynomial solvability."
```

## Explainer

You know from your prerequisites that **NP** is the class of decision problems whose solutions can be *verified* in polynomial time — given a candidate answer, a polynomial-time algorithm can confirm or refute it. You also know Boolean algebra: propositional variables taking values true/false, connected by AND (∧), OR (∨), and NOT (¬). The **Boolean satisfiability problem (SAT)** asks: given a propositional formula, is there an assignment of true/false to its variables that makes the whole formula evaluate to true? For example, (x₁ ∨ ¬x₂) ∧ (x₂ ∨ x₃) is satisfied by x₁ = true, x₂ = false, x₃ = anything. SAT is in NP because if you're given a satisfying assignment, you can verify it in linear time by just evaluating the formula.

The deeper result — the **Cook-Levin theorem** — is that SAT is **NP-complete**: not just in NP, but as hard as any problem in NP. This means every problem in NP can be reduced to SAT in polynomial time. The argument is constructive: for any NP problem with a polynomial-time verifier, you encode the verifier's computation as a Boolean formula whose satisfying assignments correspond exactly to the accepting computations on inputs that are yes-instances. The encoding captures the entire tableau of the verifier step by step. If you could solve SAT in polynomial time, you could solve every NP problem in polynomial time — so P = NP. SAT is thus the "first" NP-complete problem and the canonical benchmark for computational hardness.

The **asymmetry between verification and search** is at the heart of why SAT is hard. Checking that an assignment satisfies a formula takes O(n) time — you just evaluate each clause. But *finding* a satisfying assignment requires exploring a space of 2^n possible assignments in the worst case, and no algorithm is known that avoids this exponential blowup in general. This gap between easy verification and apparently hard search is the defining feature of NP-complete problems. The open P vs. NP question is precisely asking whether this gap is real or whether clever polynomial-time search algorithms exist for SAT (and therefore all of NP).

Modern **SAT-solvers** (like DPLL and CDCL-based tools) exploit structure in real-world instances — unit propagation, conflict-driven clause learning, smart branching heuristics — to solve instances with millions of variables in practice. These solvers are foundational tools in hardware verification, planning, and constraint satisfaction. But they are not polynomial-time algorithms; they have no worst-case guarantee that avoids exponential time. The practical tractability of most real-world SAT instances is a separate empirical fact from the theoretical worst-case hardness — a crucial distinction that separates algorithm engineering from complexity theory.
