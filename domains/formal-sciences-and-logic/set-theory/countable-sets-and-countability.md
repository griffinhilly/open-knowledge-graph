---
id: countable-sets-and-countability
title: Countable Sets and Enumeration
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: bijections-establish-equinumerosity
  type: hard
- id: naive-set-theory
  type: hard
builds-toward:
- infinite-cardinal-numbers
- aleph-numbers
tags:
- countability
- enumeration
- cardinality
- infinity
stage: formal-systems
status: draft
---

# Countable Sets and Enumeration

## Core Idea
A set is countably infinite if it is equinumerous with the natural numbers ℕ. Countable sets can be listed in a sequence, though the listing may not terminate. Countable unions of countable sets remain countable, and many 'familiar' infinite sets (ℤ, ℚ, ℕ×ℕ) are countable.

## How It's Best Learned
Use explicit bijections: pair ℤ with ℕ via n ↔ ⌊n/2⌋·(-1)^(n mod 2). Show ℚ is countable via Cantor's diagonal enumeration. Prove closure under countable unions.

## Common Misconceptions
- Confusing countable with finite; countably infinite is still infinite.
- Thinking all infinite sets are countable (leads to surprise at uncountability).

## Explainer

You already know what a bijection is: a function that is both injective (no two inputs share an output) and surjective (every output is hit). The theory of countability is almost entirely built on applying bijections carefully to infinite sets. A set A is **countably infinite** if there exists a bijection f : ℕ → A — in other words, if you can list every element of A as a₀, a₁, a₂, ... without repetition or omission. The listing may never terminate (it's an infinite list), but every element must eventually appear at some finite position.

The surprising power of this definition is that many sets you might expect to be "larger" than ℕ turn out to be countable. The integers ℤ are countable: list them as 0, 1, −1, 2, −2, 3, −3, .... This works because you can weave the positive and negative integers into a single sequence. The rationals ℚ require more ingenuity: **Cantor's diagonal enumeration** arranges all fractions p/q in an infinite grid (row p, column q), then traces a diagonal zigzag path through the grid to list them all. Any duplicate fractions (2/4 = 1/2) are skipped, but every rational is hit at some finite step — so ℚ is countable. Even ℕ × ℕ (ordered pairs of naturals) is countable by the same diagonal argument: the pair (m, n) appears at position (m+n)(m+n+1)/2 + n in the listing.

A key closure property: **countable unions of countable sets are countable**. If A₁, A₂, A₃, ... are each countably infinite, their union ⋃ₙ Aₙ is also countable. The proof: list element (i, j) of the union (the j-th element of Aᵢ) by running the diagonal enumeration on the grid of listings. This closure underlies many later arguments — for example, the set of all finite strings over a finite alphabet is countable (each length-n strings form a finite set, and there are countably many lengths), which is why the set of all computer programs is countable.

But not every infinite set is countable. Cantor's **diagonal argument** shows the reals are uncountable: assume for contradiction that all reals in [0,1] are listed as r₀, r₁, r₂, .... Construct a new real x by making x's n-th decimal digit differ from rₙ's n-th digit. Then x differs from every rₙ at the n-th position, so x is not in the list — but x is in [0,1], contradicting that the list was complete. This argument shows that the power set of ℕ (equivalently, the reals) has strictly greater cardinality than ℕ itself, and therefore countability is not the only kind of infinity. The existence of uncountable sets is what makes cardinality theory genuinely interesting: there is a strict hierarchy of infinities, and countability is just the first rung.
