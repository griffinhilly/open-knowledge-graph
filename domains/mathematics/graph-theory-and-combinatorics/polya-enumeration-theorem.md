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
stage: formal-systems
status: validated
---

# Pólya Enumeration Theorem

## Core Idea
Pólya's Enumeration Theorem counts equivalence classes of structures under group actions via the cycle index polynomial of the group. If G acts on positions and we color with c colors, the number of distinct colorings is (1/|G|) Σ c^(cyc(g)) over g in G, where cyc(g) is the number of cycles. This solves counting problems involving symmetries.

## How It's Best Learned
Apply the theorem to necklaces and bracelets using the cyclic group, verifying results by hand enumeration for small cases.

## Common Misconceptions
The formula counts distinct colorings under the group action, not all colorings; it 'quotients out' the symmetry.

## Questions

```yaml
- question: "A 4-bead necklace is acted on by the cyclic rotation group C₄. The 90° rotation is a single 4-cycle (all four beads permuted together). How many 3-color bead arrangements are fixed by this rotation?"
  type: multiple-choice
  options:
    - "81 — all 3⁴ arrangements are considered fixed"
    - "12 — the rotation fixes one bead position, allowing 3 choices for each of the 4 beads"
    - "3 — only arrangements where all four beads are the same color are unchanged by the rotation"
    - "27 — arrangements where any three beads share a color"
  answer: 2
  explanation: "A coloring is fixed by a permutation only if every bead in each cycle has the same color — otherwise rotating the necklace changes the arrangement. A single 4-cycle means all four bead positions are linked: rotating by 90° sends bead 1 to position 2, bead 2 to position 3, and so on. For the coloring to look identical after this rotation, all four beads must be the same color. With 3 available colors, there are exactly 3 such colorings. This is also what the cycle index substitution predicts: a single 4-cycle contributes a₄, and substituting a₄ = 3 gives 3 fixed colorings."

- question: "Why does substituting aᵢ = k for every variable in the cycle index of a group give the number of *distinct* colorings with k colors, rather than the total number of colorings?"
  type: multiple-choice
  options:
    - "The cycle index divides by |G| to average out symmetries, implementing Burnside's count of equivalence classes"
    - "The substitution aᵢ = k discards colorings that use fewer than k colors, leaving only fully-colored arrangements"
    - "The cycle index only counts colorings where each cycle receives a different color"
    - "The substitution removes duplicate colorings by mapping them to the identity group element"
  answer: 0
  explanation: "The cycle index Z(G) is constructed precisely to implement Burnside's lemma: the number of distinct objects under a group action equals (1/|G|) Σ |Fix(g)|. For each group element g, the number of fixed colorings equals k^(number of cycles in g) — because each cycle must receive a uniform color, giving k independent choices per cycle. The cycle index encodes this as a polynomial, and substituting aᵢ = k evaluates k^(cycles) for every element and averages over the group. The result is the count of equivalence classes — distinct colorings where symmetrically equivalent ones are identified — not the brute total of k^n."

- question: "The Pólya Enumeration Theorem counts all possible colorings of a structure with k colors and then divides by the group order to correct for symmetry."
  type: true-false
  answer: false
  explanation: "This is the common misconception. Dividing the total number of colorings (k^n) by |G| would be correct only if every coloring had exactly |G| distinct images under the group — that is, no coloring was fixed by any non-identity element. But many colorings are fixed by symmetries (e.g., a uniformly colored necklace is fixed by every rotation), so they appear in fewer than |G| equivalence partners. Burnside's lemma (and Pólya's theorem) instead averages the *number of fixed colorings per group element*, which correctly handles these symmetric cases. The two approaches give different results whenever any non-identity group element fixes at least one coloring."

- question: "Two colorings of a necklace are considered identical under Pólya's theorem if and only if one can be obtained from the other by applying some element of the symmetry group."
  type: true-false
  answer: true
  explanation: "This is exactly the definition of the equivalence relation that Pólya's theorem counts equivalence classes of. Two colorings c₁ and c₂ are equivalent under the group G if there exists some g ∈ G such that g·c₁ = c₂. Pólya's theorem counts the number of orbits under this action — each orbit is a set of colorings that are all related by some group element, representing a single 'structurally distinct' coloring. This is why the theorem is said to 'quotient out' the symmetry: it treats two arrangements as the same if a symmetry operation connects them."

- question: "Explain why every cycle in a permutation must receive a single uniform color when counting colorings fixed by that permutation, and why this leads to the formula k^(number of cycles) for fixed colorings."
  type: short-answer
  answer: "A coloring is fixed by a permutation g if applying g to the bead positions leaves the coloring unchanged — every bead ends up at a position with the same color it started with. Within a single cycle of length ℓ, position 1 maps to position 2, position 2 to position 3, ..., position ℓ back to position 1. For the coloring to be unchanged, each position must have the same color as the position it maps to: color(1) = color(2) = ... = color(ℓ). The entire cycle must be one uniform color. Since each cycle can independently be any of the k colors, and the cycles are disjoint, the total number of fixed colorings is k multiplied by itself once per cycle — k^(number of cycles in g)."
  explanation: "This is the mechanical heart of the theorem and why understanding it matters more than memorizing the formula. The cycle structure of a permutation completely determines how many colorings it fixes. A permutation with many short cycles fixes many colorings (each short cycle can be colored independently); a permutation with one long cycle fixes very few (the whole cycle must be uniform). The cycle index averages these counts over the group, and the resulting polynomial captures all symmetry information needed to count distinct colorings for any number of colors."
```

## Explainer

Pólya's Enumeration Theorem solves a deceptively tricky class of counting problems: how many structurally distinct colorings of a set of positions exist when two colorings are considered the same if one can be obtained from the other by a symmetry of the structure? Without the theorem, you might list all colorings and manually eliminate duplicates — but this becomes impossible for large cases. The theorem provides an algebraic shortcut grounded in the group theory you studied in group actions.

The foundation is **Burnside's lemma**: the number of distinct objects under a group action equals the average number of objects fixed by each group element — (1/|G|) Σ |Fix(g)|. If you have the rotation group of a square acting on colorings of its 4 corners, you sum up, for each rotation, how many colorings are unchanged by that rotation, then divide by 4. Burnside already handles many problems. Pólya extends this by encoding the **cycle structure** of each group element into a polynomial, called the **cycle index** Z(G).

The cycle index is computed by expressing each group element g as a product of disjoint cycles acting on the positions. A rotation by 90° of a 4-bead necklace is a single 4-cycle (all four beads rotate together). A rotation by 180° decomposes into two 2-cycles. The identity consists of four 1-cycles. For each group element g with cycle type (c₁, c₂, ...) — meaning c₁ cycles of length 1, c₂ cycles of length 2, and so on — you form a monomial a₁^(c₁) × a₂^(c₂) × ... The **cycle index** Z(G; a₁, a₂, ...) averages these monomials over all group elements.

To count colorings with k colors, substitute aᵢ = k for every variable in the cycle index. The result is the number of distinct colorings. This substitution works because each cycle of length ℓ must be a single uniform color (otherwise the coloring changes under the permutation), giving k independent choices per cycle. Summing and averaging over all group elements precisely implements Burnside's count, but the cycle index packages it into a reusable polynomial that can be evaluated for any number of colors.

The theorem also generalizes to **weighted enumeration**, where colors have associated weights (monomials in new variables). Substituting aᵢ = w₁ⁱ + w₂ⁱ + ... (sum of weight variables raised to the ith power) into the cycle index produces a generating function where the coefficient of each monomial counts how many distinct colorings use each color the specified number of times. This is far more powerful than a raw count — it tells you, for example, exactly how many 6-bead necklaces with 3 red and 3 blue beads exist, distinguishing by composition. For necklaces, bracelets, and any combinatorial object with a natural symmetry group, the Pólya theorem is the standard tool.
