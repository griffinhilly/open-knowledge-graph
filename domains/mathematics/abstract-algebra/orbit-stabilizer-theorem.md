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
status: validated
---

# Orbit-Stabilizer Theorem

## Core Idea
For a group action of G on a finite set X and any x ∈ X, the orbit Orb(x) and stabilizer Stab(x) satisfy |Orb(x)| · |Stab(x)| = |G|. This relates local structure to global structure.

## Questions

```yaml
- question: "A group G of order 24 acts on a finite set. If the stabilizer of a point x has order 6, what is the size of the orbit of x?"
  type: multiple-choice
  options:
    - "4"
    - "6"
    - "18"
    - "24"
  answer: 0
  explanation: "By the orbit-stabilizer theorem, |Orb(x)| · |Stab(x)| = |G|, so |Orb(x)| = 24 / 6 = 4. The common mistake is to subtract rather than divide: |G| − |Stab(x)| = 18 is incorrect. The theorem is a multiplicative relationship, not additive, because the orbit corresponds to the cosets of the stabilizer in G."

- question: "The group S₃ acts on itself by conjugation. The orbit of (123) has size 2 (the two 3-cycles). What is the order of its stabilizer?"
  type: multiple-choice
  options:
    - "1"
    - "2"
    - "3"
    - "6"
  answer: 2
  explanation: "|Stab((123))| = |G| / |Orb((123))| = 6 / 2 = 3. The stabilizer consists of all elements that commute with (123) under conjugation — these are the identity and the two 3-cycles themselves, forming a cyclic subgroup of order 3. This illustrates how the theorem lets you compute the stabilizer's size from orbit size alone, without listing stabilizer elements."

- question: "The stabilizer of any point x under a group action is always a subgroup of G."
  type: true-false
  answer: true
  explanation: "Stab(x) = {g ∈ G : g·x = x} is closed under the group operation (if g and h fix x, then (gh)·x = g·(h·x) = g·x = x), contains the identity, and is closed under inverses (if g·x = x, then x = g⁻¹·(g·x) = g⁻¹·x). These three properties make it a subgroup. This fact is what allows Lagrange's theorem to be applied in the proof of the orbit-stabilizer theorem."

- question: "If two points x and y in a set have the same stabilizer subgroup, they must lie in the same orbit."
  type: true-false
  answer: false
  explanation: "Having equal stabilizers does not imply being in the same orbit. Consider Z₂ = {e, r} acting on a three-element set {a, b, c} where r fixes both a and b but swaps nothing (trivial action on a and b) — both a and b have Stab = G, yet they are each their own orbit. The orbit-stabilizer theorem links the *size* of the orbit to the *size* of the stabilizer, but two points with equal-sized stabilizers can still be in different orbits."

- question: "Why do two group elements g and h produce the same orbit image (g·x = h·x) if and only if they belong to the same left coset of Stab(x) in G?"
  type: short-answer
  answer: "g·x = h·x iff h⁻¹g·x = x iff h⁻¹g ∈ Stab(x) iff g and h are in the same left coset of Stab(x). So each coset of Stab(x) corresponds to exactly one element of the orbit."
  explanation: "This coset correspondence is the heart of the proof: distinct cosets map to distinct orbit elements, and every orbit element is hit by exactly one coset. The number of left cosets of Stab(x) in G equals |G|/|Stab(x)| by Lagrange's theorem, so |Orb(x)| = |G|/|Stab(x)|. This is why the theorem feels like an extension of Lagrange's theorem from subgroups to group actions."
```

## Explainer

From your study of group actions, you know that a group G can act on a set X by assigning to each g ∈ G a permutation of X in a way that respects the group structure. The **orbit** of a point x is the set of all positions x can be moved to: Orb(x) = {g·x : g ∈ G}. The **stabilizer** of x is the set of all group elements that fix x: Stab(x) = {g ∈ G : g·x = x}. The stabilizer is actually a subgroup of G — worth verifying: if g and h both fix x, then gh fixes x, and g⁻¹ fixes x too.

The orbit-stabilizer theorem says these two structures multiply to give the full group size: |Orb(x)| · |Stab(x)| = |G|. The intuition comes from a counting argument that mirrors Lagrange's theorem (which you may know from cosets). Different group elements g produce the same image g·x precisely when they differ by an element of Stab(x) — that is, g and h send x to the same place if and only if h⁻¹g ∈ Stab(x), meaning g and h are in the same left coset of Stab(x). So there is a bijection between the orbit of x and the set of left cosets of Stab(x) in G. By Lagrange's theorem applied to Stab(x) ≤ G, the number of such cosets is |G|/|Stab(x)|, giving |Orb(x)| = |G|/|Stab(x)|.

Consider a concrete example: let G = S₃ act on itself by conjugation, and pick x = (12). The orbit is the set of all elements conjugate to (12) — the entire conjugacy class, which contains all three transpositions: {(12), (13), (23)}. The stabilizer is the set of permutations that fix (12) under conjugation, i.e., commute with (12): this is {e, (12)}, which has order 2. Check: 3 · 2 = 6 = |S₃|. The theorem confirms the arithmetic before you do any detailed computation.

The theorem's power is most visible in **combinatorial counting problems**. To count the number of distinct colorings of an object under symmetry (like how many ways to color the faces of a cube with k colors up to rotation), you apply the orbit-stabilizer theorem across all orbits. The stabilizer at each configuration tells you how much symmetry "wastes" group elements keeping that configuration fixed. This is the engine behind Burnside's lemma, and later behind the Sylow theorems, where the orbit-stabilizer setup forces divisibility conditions on subgroup counts. In short: wherever a group acts on a set, the orbit-stabilizer theorem is the tool that translates between the local symmetry at a point and the global size of the group.
