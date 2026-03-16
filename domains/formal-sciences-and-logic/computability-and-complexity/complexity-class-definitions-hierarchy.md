---
id: complexity-class-definitions-hierarchy
title: Complexity Classes and the Complexity Hierarchy
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: space-complexity-classes-formal
  type: hard
- id: algorithm-analysis-big-o
  type: soft
- id: algorithm-complexity
  type: hard
builds-toward:
- p-versus-np
- polynomial-hierarchy
tags:
- complexity-classes
- hierarchy-theorem
- p-np-pspace
stage: advanced
status: draft
---

# Complexity Classes and the Complexity Hierarchy

## Core Idea
Complexity classes like P, NP, PSPACE, and EXPTIME group problems by the computational resources (time or space) required to solve them. The Hierarchy Theorem shows that these classes are strictly nested (e.g., P ⊆ NP ⊆ PSPACE ⊆ EXPTIME), with some containments proven and others (like P vs. NP) remaining famously open.

## How It's Best Learned
Study the hierarchy theorem proofs to understand how resource bounds create proper inclusions. Visualize complexity classes as concentric circles to internalize nestings.

## Common Misconceptions
- Confusing 'properly contained' with 'strictly separated by a provable gap.' Hierarchy theorems use resource separation, not problem difficulty.
- Assuming all inclusions are proven. P ⊆ NP is known; P = NP is open.

## Explainer

You already know how to measure time and space complexity: a problem's time complexity is roughly how many steps the best algorithm takes as input grows, expressed in big-O notation, and you've studied formal resource bounds like DTIME(f(n)) and DSPACE(f(n)). **Complexity classes** are simply the collections of all decision problems solvable within some bound. **P** is the class of problems solvable in polynomial time — O(n^k) for some fixed k. **NP** is the class solvable in polynomial time on a nondeterministic Turing machine, equivalently, the class of problems whose solutions can be *verified* in polynomial time. Sorting is in P; given a proposed Hamiltonian cycle, you can check it in polynomial time, so the Hamiltonian cycle problem is in NP.

The hierarchy of classes P ⊆ NP ⊆ PSPACE ⊆ EXPTIME is an inclusion chain organized by resource. **PSPACE** groups problems solvable using polynomial *space* (but possibly exponential time), while **EXPTIME** groups those solvable in at most exponential time. The key insight is that using more resources can only help: a problem solvable in polynomial time is certainly solvable in polynomial space, because space can be reused across steps. This gives you the chain of inclusions for free — every problem in the smaller class is automatically a member of every larger class.

The **Time Hierarchy Theorem** and **Space Hierarchy Theorem** prove that the inclusions are *proper* when you jump by a sufficient factor. The Time Hierarchy Theorem says DTIME(n) ⊊ DTIME(n²) — there are problems solvable in quadratic time that cannot be solved in linear time. The proof is a diagonal argument in the tradition of Cantor and Turing: construct a machine that reads the description of other machines and deliberately differs from each in finite time, guaranteeing it computes a function none of them can. This gives you the guaranteed proper nesting: P ⊊ EXPTIME and PSPACE ⊊ EXPSPACE are both proven. The hierarchy theorems do *not*, however, resolve P vs. NP — diagonalization cannot separate classes that differ only by a polynomial factor without additional structure.

The famous open question — whether **P = NP** — asks if polynomial verifiability implies polynomial solvability. The question is hard precisely because every technique that would separate them (diagonalization, circuit lower bounds, natural proofs) has hit known barriers. What we *do* know is that if P ≠ NP, the class NP splits further: there are problems in NP that are neither in P nor NP-complete, a fact established by Ladner's theorem. The complexity hierarchy is thus not just a tower of inclusions but a landscape of problems clustered by difficulty, with P and EXPTIME as the two proven landmarks and NP as the central mystery between them.
