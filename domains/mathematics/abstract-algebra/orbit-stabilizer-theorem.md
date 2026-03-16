---
id: orbit-stabilizer-theorem
title: Orbit-Stabilizer Theorem
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-actions
  type: hard
builds-toward:
- class-equation
- sylow-theorems
tags:
- orbit
- stabilizer
- orbit-stabilizer
- counting
stage: advanced
status: draft
---

# Orbit-Stabilizer Theorem

## Core Idea
For a group action of G on a finite set X and any x ∈ X, the orbit Orb(x) and stabilizer Stab(x) satisfy |Orb(x)| · |Stab(x)| = |G|. This relates local structure to global structure.

## Explainer

From your study of group actions, you know that a group G can act on a set X by assigning to each g ∈ G a permutation of X in a way that respects the group structure. The **orbit** of a point x is the set of all positions x can be moved to: Orb(x) = {g·x : g ∈ G}. The **stabilizer** of x is the set of all group elements that fix x: Stab(x) = {g ∈ G : g·x = x}. The stabilizer is actually a subgroup of G — worth verifying: if g and h both fix x, then gh fixes x, and g⁻¹ fixes x too.

The orbit-stabilizer theorem says these two structures multiply to give the full group size: |Orb(x)| · |Stab(x)| = |G|. The intuition comes from a counting argument that mirrors Lagrange's theorem (which you may know from cosets). Different group elements g produce the same image g·x precisely when they differ by an element of Stab(x) — that is, g and h send x to the same place if and only if h⁻¹g ∈ Stab(x), meaning g and h are in the same left coset of Stab(x). So there is a bijection between the orbit of x and the set of left cosets of Stab(x) in G. By Lagrange's theorem applied to Stab(x) ≤ G, the number of such cosets is |G|/|Stab(x)|, giving |Orb(x)| = |G|/|Stab(x)|.

Consider a concrete example: let G = S₃ act on itself by conjugation, and pick x = (12). The orbit is the set of all elements conjugate to (12) — the entire conjugacy class, which contains all three transpositions: {(12), (13), (23)}. The stabilizer is the set of permutations that fix (12) under conjugation, i.e., commute with (12): this is {e, (12)}, which has order 2. Check: 3 · 2 = 6 = |S₃|. The theorem confirms the arithmetic before you do any detailed computation.

The theorem's power is most visible in **combinatorial counting problems**. To count the number of distinct colorings of an object under symmetry (like how many ways to color the faces of a cube with k colors up to rotation), you apply the orbit-stabilizer theorem across all orbits. The stabilizer at each configuration tells you how much symmetry "wastes" group elements keeping that configuration fixed. This is the engine behind Burnside's lemma, and later behind the Sylow theorems, where the orbit-stabilizer setup forces divisibility conditions on subgroup counts. In short: wherever a group acts on a set, the orbit-stabilizer theorem is the tool that translates between the local symmetry at a point and the global size of the group.
