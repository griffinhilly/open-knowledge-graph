---
id: cook-levin-theorem
title: The Cook-Levin Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: boolean-logic-programming
  type: soft
tags:
- Cook-Levin
- SAT
- NP-complete
- CNF-SAT
- circuit-complexity
stage: advanced
status: validated
---

# The Cook-Levin Theorem

## Core Idea
The Cook-Levin theorem (Cook 1971, Levin 1973) proves that Boolean satisfiability (SAT) — and 3-SAT — is NP-complete, establishing the first NP-complete problem. The proof encodes any polynomial-time nondeterministic TM computation as a Boolean formula in CNF: variables represent the tableau of TM configurations, and clauses enforce valid transitions. If SAT could be solved in polynomial time, so could every NP problem. Once SAT was known NP-complete, hundreds of other problems were shown NP-complete by polynomial reduction from SAT or 3-SAT.

## How It's Best Learned
Study the tableau construction at a high level: understand that rows represent TM configurations, columns represent time steps, and clauses enforce consistency. Then read Karp's 1972 paper listing 21 NP-complete problems to see the reduction cascade that followed Cook's result.

## Common Misconceptions
- Confusing the Cook-Levin theorem with a proof that SAT is hard to solve — it proves SAT is NP-complete (in NP and NP-hard), not that it has no polynomial algorithm.
- Thinking the Cook-Levin proof directly applies to 3-SAT — a separate (easy) reduction from SAT to 3-SAT is needed.

## Explainer

You already know what NP-completeness means: a problem is NP-complete if it is in NP (a solution can be verified in polynomial time) and every problem in NP can be reduced to it in polynomial time. But knowing the definition raises an obvious question: how do you prove the *first* NP-complete problem? You cannot reduce from a known NP-complete problem because none has been established yet. The **Cook-Levin theorem** breaks this circularity by proving directly, from the definition of NP itself, that **Boolean satisfiability (SAT)** is NP-complete.

The proof strategy is to show that any NP computation can be encoded as a SAT instance. Here is the intuition. An NP problem, by definition, has a nondeterministic Turing machine that decides it in polynomial time. That machine's computation can be laid out as a **tableau** — a two-dimensional grid where rows represent successive configurations (tape contents, head position, state) and columns represent time steps. The entire computation fits in a p(n) × p(n) grid for some polynomial p. Cook and Levin's insight was to create Boolean variables for every cell in this tableau and then write clauses in **conjunctive normal form (CNF)** that enforce three things: the initial configuration is correct, each row follows from the previous one by a valid transition rule, and the machine reaches an accepting state. The resulting formula is satisfiable if and only if the Turing machine accepts — meaning a SAT solver could answer any NP question.

The theorem's importance is not that SAT is hard (though practitioners know it often is). It is that SAT is **universal for NP**: it can express any polynomial-time verification problem. Once Cook and Levin established SAT as NP-complete, Richard Karp showed in 1972 that 21 other well-known problems — including Clique, Vertex Cover, Hamiltonian Path, and Integer Programming — are also NP-complete by polynomial-time reductions from SAT or 3-SAT. Each new reduction was far simpler than Cook-Levin because it only needed to reduce from one already-known NP-complete problem. This cascade of reductions is why Cook-Levin is the keystone of NP-completeness theory: it did the heavy lifting once, and everything else followed.

One subtlety worth noting: the theorem as originally proved applies to SAT in general, not specifically to **3-SAT** (where every clause has exactly three literals). The reduction from SAT to 3-SAT is a separate, relatively straightforward step that introduces auxiliary variables to break long clauses into groups of three. The reason 3-SAT matters is practical — it is the most common starting point for further NP-completeness reductions because its restricted structure makes reductions cleaner to construct.
