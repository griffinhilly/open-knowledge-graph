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
status: draft
---

# The Cook-Levin Theorem

## Core Idea
The Cook-Levin theorem (Cook 1971, Levin 1973) proves that Boolean satisfiability (SAT) — and 3-SAT — is NP-complete, establishing the first NP-complete problem. The proof encodes any polynomial-time nondeterministic TM computation as a Boolean formula in CNF: variables represent the tableau of TM configurations, and clauses enforce valid transitions. If SAT could be solved in polynomial time, so could every NP problem. Once SAT was known NP-complete, hundreds of other problems were shown NP-complete by polynomial reduction from SAT or 3-SAT.

## How It's Best Learned
Study the tableau construction at a high level: understand that rows represent TM configurations, columns represent time steps, and clauses enforce consistency. Then read Karp's 1972 paper listing 21 NP-complete problems to see the reduction cascade that followed Cook's result.

## Common Misconceptions
- Confusing the Cook-Levin theorem with a proof that SAT is hard to solve — it proves SAT is NP-complete (in NP and NP-hard), not that it has no polynomial algorithm.
- Thinking the Cook-Levin proof directly applies to 3-SAT — a separate (easy) reduction from SAT to 3-SAT is needed.
