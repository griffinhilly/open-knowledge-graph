---
id: equivalence-relations-and-partitions
title: Equivalence Relations and Partitions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: relations-properties-and-types
  type: hard
tags:
- equivalence relation
- partition
- equivalence class
stage: formal-systems
status: draft
---

# Equivalence Relations and Partitions

## Core Idea
An equivalence relation is reflexive, symmetric, and transitive. It partitions a set into equivalence classes—disjoint subsets where elements are related if and only if they are in the same class. Equivalence relations formalize the intuitive notion of 'grouping by type' and are foundational in abstract mathematics.

## How It's Best Learned
Verify that familiar relations (equality, modular congruence) are equivalence relations. Compute equivalence classes explicitly for small examples.

## Common Misconceptions
- Thinking any relation with these three properties automatically induces a valid partition.
- Confusing equivalence relation with equality.
- Forgetting that equivalence classes must be non-empty and disjoint.

## Explainer

You already know about relations on sets and their properties — reflexivity, symmetry, transitivity, and others. An **equivalence relation** is a relation that satisfies all three of these simultaneously, and the payoff for that combination is remarkable: it perfectly organizes the set into non-overlapping groups. The three axioms are not arbitrary; they exactly capture the idea of "sameness" or "belonging to the same category."

Here is why each axiom is load-bearing. **Reflexivity** (every element is related to itself) ensures that no element falls outside all groups — everyone belongs to at least their own group. **Symmetry** (if a ~ b then b ~ a) ensures the grouping relation is mutual — membership is not directional. **Transitivity** (if a ~ b and b ~ c then a ~ c) is the key closure property: if a and c are both "equivalent to b," they must be equivalent to each other, meaning they land in the same group. Remove any one of these and the grouping structure breaks down.

Given an equivalence relation ~ on a set S, the **equivalence class** of an element a is [a] = {x ∈ S : x ~ a} — all elements equivalent to a. The central theorem is that the equivalence classes form a **partition** of S: they are pairwise disjoint, non-empty, and their union is all of S. The proof hinges on transitivity: if [a] and [b] share any element c, then a ~ c and b ~ c, so by symmetry and transitivity a ~ b, which means [a] = [b]. Two equivalence classes are either identical or completely disjoint — there is no partial overlap.

Examples help make this concrete. On the integers, define a ~ b if a ≡ b (mod 3). This is an equivalence relation: reflexive (n ≡ n mod 3), symmetric, and transitive. The equivalence classes are exactly {…, −3, 0, 3, 6, …}, {…, −2, 1, 4, 7, …}, and {…, −1, 2, 5, 8, …} — the three residue classes mod 3. Modular arithmetic is entirely built on this partition. In geometry, "same length" partitions line segments into classes; "congruent" partitions triangles. Equivalence relations are the formal backbone of every mathematical construction that treats different-looking objects as "the same thing."
