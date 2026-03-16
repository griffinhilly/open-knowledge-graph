---
id: np-completeness-and-hardness
title: NP-Completeness and NP-Hardness
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: complexity-class-np-definition
  type: soft
builds-toward:
- boolean-satisfiability-and-reductions
tags:
- np-complete
- np-hard
- reduction
- hardest-problems
- equivalence
stage: advanced
status: draft
---

# NP-Completeness and NP-Hardness

## Core Idea
A language is NP-complete if it's in NP and every NP language polynomial-time reduces to it. NP-hard means hard but not necessarily in NP (e.g., TQBF). If any NP-complete problem is in P, then P = NP. NP-complete problems (SAT, 3-SAT, clique, vertex cover) are equivalent in difficulty—if one is tractable, all are.

## Explainer

You already know that NP is the class of problems whose solutions can be verified in polynomial time. NP-completeness sharpens this by identifying the **hardest problems within NP** — the ones that every other NP problem can be transformed into. Think of NP-complete problems as universal translators: if you could solve any single one of them efficiently, you could solve all of NP efficiently, because every NP problem has a polynomial-time reduction to every NP-complete problem.

The formal definition has two parts. A problem L is **NP-complete** if (1) L is in NP, meaning solutions can be verified quickly, and (2) every problem in NP polynomial-time reduces to L, meaning L is at least as hard as anything in NP. The second condition is called **NP-hardness**. Crucially, NP-hardness is a standalone concept: a problem can be NP-hard without being in NP at all. For example, the halting problem is NP-hard (you can reduce any NP problem to it) but it is not in NP because it is undecidable — you cannot even verify a proposed answer in finite time. NP-completeness is the intersection: NP-hard and also in NP.

The reason this matters is the chain reaction. Because NP-complete problems are all interreducible — SAT reduces to 3-SAT, 3-SAT reduces to CLIQUE, CLIQUE reduces to VERTEX COVER, and so on — they form an equivalence class of difficulty. A polynomial-time algorithm for any one of them would immediately give polynomial-time algorithms for all of them, and therefore for every problem in NP. This would prove P = NP. Conversely, proving that any single NP-complete problem has no polynomial-time solution would prove P ≠ NP. This is why the P vs NP question can be focused on any one NP-complete problem rather than requiring a proof about all of NP simultaneously.

In practice, when you encounter a new problem and suspect it is intractable, the standard approach is to show it is NP-hard by reducing a known NP-complete problem to it. This is a proof of difficulty: you are showing that your new problem is at least as hard as a problem the entire field has failed to solve efficiently. If the new problem is also in NP, it is NP-complete, joining the equivalence class. If it is not in NP — perhaps because its solutions cannot even be verified quickly — it is NP-hard but sits outside NP, potentially in a harder class like PSPACE or even among undecidable problems.
