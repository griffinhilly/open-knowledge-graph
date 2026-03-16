---
id: polya-enumeration-theorem
title: Pólya Enumeration Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: group-actions
  type: hard
tags:
- combinatorics
- enumeration
stage: advanced
status: draft
---

# Pólya Enumeration Theorem

## Core Idea
Pólya's Enumeration Theorem counts equivalence classes of structures under group actions via the cycle index polynomial of the group. If G acts on positions and we color with c colors, the number of distinct colorings is (1/|G|) Σ c^(cyc(g)) over g in G, where cyc(g) is the number of cycles. This solves counting problems involving symmetries.

## How It's Best Learned
Apply the theorem to necklaces and bracelets using the cyclic group, verifying results by hand enumeration for small cases.

## Common Misconceptions
The formula counts distinct colorings under the group action, not all colorings; it 'quotients out' the symmetry.

## Explainer

Pólya's Enumeration Theorem solves a deceptively tricky class of counting problems: how many structurally distinct colorings of a set of positions exist when two colorings are considered the same if one can be obtained from the other by a symmetry of the structure? Without the theorem, you might list all colorings and manually eliminate duplicates — but this becomes impossible for large cases. The theorem provides an algebraic shortcut grounded in the group theory you studied in group actions.

The foundation is **Burnside's lemma**: the number of distinct objects under a group action equals the average number of objects fixed by each group element — (1/|G|) Σ |Fix(g)|. If you have the rotation group of a square acting on colorings of its 4 corners, you sum up, for each rotation, how many colorings are unchanged by that rotation, then divide by 4. Burnside already handles many problems. Pólya extends this by encoding the **cycle structure** of each group element into a polynomial, called the **cycle index** Z(G).

The cycle index is computed by expressing each group element g as a product of disjoint cycles acting on the positions. A rotation by 90° of a 4-bead necklace is a single 4-cycle (all four beads rotate together). A rotation by 180° decomposes into two 2-cycles. The identity consists of four 1-cycles. For each group element g with cycle type (c₁, c₂, ...) — meaning c₁ cycles of length 1, c₂ cycles of length 2, and so on — you form a monomial a₁^(c₁) × a₂^(c₂) × ... The **cycle index** Z(G; a₁, a₂, ...) averages these monomials over all group elements.

To count colorings with k colors, substitute aᵢ = k for every variable in the cycle index. The result is the number of distinct colorings. This substitution works because each cycle of length ℓ must be a single uniform color (otherwise the coloring changes under the permutation), giving k independent choices per cycle. Summing and averaging over all group elements precisely implements Burnside's count, but the cycle index packages it into a reusable polynomial that can be evaluated for any number of colors.

The theorem also generalizes to **weighted enumeration**, where colors have associated weights (monomials in new variables). Substituting aᵢ = w₁ⁱ + w₂ⁱ + ... (sum of weight variables raised to the ith power) into the cycle index produces a generating function where the coefficient of each monomial counts how many distinct colorings use each color the specified number of times. This is far more powerful than a raw count — it tells you, for example, exactly how many 6-bead necklaces with 3 red and 3 blue beads exist, distinguishing by composition. For necklaces, bracelets, and any combinatorial object with a natural symmetry group, the Pólya theorem is the standard tool.
