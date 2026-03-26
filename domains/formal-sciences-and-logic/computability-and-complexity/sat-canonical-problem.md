---
id: sat-canonical-problem
title: 'Satisfiability Problem: The Canonical NP-Complete Problem'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-theorem
  type: hard
- id: sat-boolean-satisfiability-computability-and-complexity
  type: soft
builds-toward:
- three-sat-reductions
tags:
- satisfiability
- boolean-satisfiability
- sat-solvers
- completeness
stage: formal-systems
status: validated
---
# Satisfiability Problem: The Canonical NP-Complete Problem

## Core Idea
The Boolean satisfiability problem (SAT) asks whether a Boolean formula has an assignment making it true. SAT is the prototypical NP-complete problem and appears across logic, AI, hardware verification, and combinatorics. The complexity of SAT directly connects to fundamental questions about problem-solving and the limits of efficient computation.

## How It's Best Learned
Experiment with SAT solvers (e.g., MiniSat) on small instances. Convert a graph coloring instance to SAT to see the encoding.

## Questions

```yaml
- question: "To prove that a new decision problem Q is NP-hard, which of the following proof strategies is correct?"
  type: multiple-choice
  options:
    - "Show that Q can be reduced to SAT in polynomial time"
    - "Show that SAT (or another known NP-hard problem) can be reduced to Q in polynomial time"
    - "Show that Q is in NP by exhibiting a polynomial-time verification algorithm"
    - "Show that Q requires superpolynomial time on all inputs by constructing a worst-case lower bound"
  answer: 1
  explanation: "NP-hardness is established by reduction FROM a known hard problem TO the new problem. If SAT reduces to Q (meaning every SAT instance can be transformed to a Q instance in polynomial time), then solving Q efficiently would imply solving SAT efficiently — so Q is at least as hard as SAT. Since SAT is NP-hard (all NP problems reduce to it), and all NP problems reduce to SAT, they all indirectly reduce to Q through SAT. Option A gets the direction backwards: if Q reduces to SAT, that just means Q is in NP (or at most as hard as SAT), not NP-hard. Option C proves membership in NP but not hardness. Showing NP-hardness always requires demonstrating that a known hard problem reduces to the target."

- question: "A SAT solver is given a formula with 500,000 variables representing a hardware verification problem, and solves it in 45 seconds. A colleague says this disproves NP-completeness of SAT. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — solving large instances quickly does prove SAT is not NP-complete"
    - "NP-completeness is about worst-case time complexity; efficient solutions to specific classes of practical instances are consistent with SAT being NP-complete"
    - "The solver must have made an error — NP-complete problems cannot be solved with 500,000 variables"
    - "Hardware verification formulas are a special case not covered by the NP-completeness proof"
  answer: 1
  explanation: "NP-completeness is a worst-case statement about a class of instances, not a guarantee that all instances are hard. Modern CDCL SAT solvers are extraordinarily effective on structured industrial instances (hardware verification, planning, cryptanalysis) because they use conflict-driven clause learning to detect and prune large portions of the search space. Practical instances often have structure (regularity, locality, sparse constraint graphs) that solvers exploit. The existence of hard instances — formulas near the satisfiability threshold, or adversarially constructed inputs — is what makes SAT NP-complete. Efficient average-case performance on structured inputs is entirely consistent with NP-completeness."

- question: "SAT is in NP because a satisfying assignment, if one exists, can be verified in polynomial time by evaluating the formula on that assignment."
  type: true-false
  answer: true
  explanation: "True. This is exactly what NP membership means: a problem is in NP if there exists a polynomial-time verification algorithm for positive instances. For SAT, the 'certificate' is a truth assignment to all variables. Given a formula φ and an assignment σ, you can verify that σ satisfies φ by evaluating each clause under σ in O(|φ|) time — simply check that at least one literal in each clause is true. This evaluation is linear in the formula size. Note that membership in NP says nothing about how hard it is to FIND the satisfying assignment — only that you can CHECK it quickly once found. The difficulty of finding the certificate is what makes NP problems potentially hard."

- question: "Because SAT is NP-complete, any SAT solver that solves real-world instances quickly is expected to be using a fundamentally different computational model than what the NP-completeness proof assumes."
  type: true-false
  answer: false
  explanation: "False. Modern SAT solvers (based on CDCL — conflict-driven clause learning) operate on standard computational models. NP-completeness doesn't mean every instance is hard — it means no known polynomial-time algorithm exists for the worst case. Practical instances from hardware verification, planning, and other domains have structure that CDCL solvers exploit efficiently: they learn clauses from conflicts that prune the search space, making many large structured instances tractable. The theoretical worst-case hardness of SAT and the practical efficiency of CDCL solvers on real-world instances are entirely compatible."

- question: "What is the significance of SAT being both in NP and NP-hard? How does the Cook-Levin theorem establish that every NP problem reduces to SAT?"
  type: short-answer
  answer: "Being in NP means SAT's solutions can be verified quickly. Being NP-hard means every problem in NP can be reduced to SAT in polynomial time — SAT is at least as hard as any problem in NP. Together, these make SAT NP-complete: it is simultaneously solvable by nondeterministic polynomial algorithms and as hard as anything in the class. The Cook-Levin theorem establishes the NP-hard direction by encoding the computation of an arbitrary nondeterministic Turing machine as a Boolean formula. The variables represent the machine's full configuration (tape content, head position, state) at each of polynomially many time steps. Clauses encode three things: the initial configuration, the valid transition rules (each step follows from the previous by a legal machine transition), and the accepting condition. The formula is satisfiable if and only if the NTM accepts. Since any NP problem has such an NTM, any NP problem can be reduced to SAT this way in polynomial time."
  explanation: "The significance is that SAT is a universal language for NP: any NP problem can be expressed as a Boolean satisfiability question. This is why proving SAT NP-hard was revolutionary — it turned the abstract question 'is problem X in P?' into the concrete question 'is there a polynomial-time SAT algorithm?' And it explains why SAT solvers are so broadly useful: since any NP problem reduces to SAT, a powerful SAT solver can attack any NP problem by encoding it as a formula."
```

## Explainer

You know NP-completeness: a problem is NP-complete if it is in NP *and* every NP problem reduces to it in polynomial time. SAT — the Boolean satisfiability problem — is the canonical example, historically the first proved NP-complete (Cook, 1971; Levin, 1973), and the starting point for the vast web of NP-completeness reductions that followed.

**SAT** asks: given a Boolean formula φ over variables x₁, ..., xₙ with connectives ∧, ∨, ¬, does any truth-value assignment to the variables make φ evaluate to true? For example, (x₁ ∨ ¬x₂) ∧ (¬x₁ ∨ x₂) is satisfiable (set x₁ = x₂ = T), while (x₁) ∧ (¬x₁) is not. The certificate for membership in SAT is just the satisfying assignment — easy to verify in linear time by evaluating the formula. So SAT is in NP.

That SAT is NP-*hard* — that every NP problem reduces to SAT — is the deep claim, proved by the Cook-Levin theorem. The proof encodes any nondeterministic Turing machine computation as a Boolean formula: variables represent the machine's configuration (tape content, head position, state) at each of polynomially many time steps, and the formula asserts that the transitions are valid and the computation accepts. This encoding is polynomial in the input size. Because every NP problem has such an NTM computation, every NP problem has a polynomial-time reduction to SAT. SAT is thus a universal language for NP: it can express any NP problem.

In practice, modern **SAT solvers** (MiniSat, CryptoMiniSat, Z3) are remarkably powerful despite the theoretical hardness. They use the DPLL algorithm enhanced with **conflict-driven clause learning (CDCL)** — when a partial assignment leads to a contradiction, the solver learns a new clause that prunes future search. Industrial instances with millions of variables in hardware verification, automated planning, cryptanalysis, and program synthesis are routinely solved. Understanding SAT in both its theoretical (NP-completeness, reductions from other problems) and practical (solver algorithms, phase transitions near the satisfiability threshold) aspects gives you the central problem around which complexity theory and automated reasoning both revolve.
