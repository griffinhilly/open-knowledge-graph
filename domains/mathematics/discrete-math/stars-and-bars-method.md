---
id: stars-and-bars-method
title: 'Stars and Bars: Combinatorial Method for Distributions'
domain: mathematics
course: discrete-math
prerequisites:
- id: combinations-and-selections
  type: hard
builds-toward:
- generating-functions-discrete
tags:
- combinatorics
- counting
stage: formal-systems
status: draft
---

# Stars and Bars: Combinatorial Method for Distributions

## Core Idea
The stars and bars method counts ways to distribute n identical items into k distinct bins using the formula C(n+k-1, k-1). This is equivalent to counting non-negative integer solutions to x₁ + x₂ + ⋯ + xₖ = n. The method visualizes items as stars and bin separations as bars.

## Explainer

Suppose you want to distribute 5 identical cookies among 3 children. The children are distinct (they have names and feelings), but the cookies are not (one cookie is as good as another). Your prerequisite work on combinations counted ways to choose from a set where the items were distinct. The stars and bars method handles the new wrinkle: identical items going into labeled containers.

The key move is a **bijection** — a one-to-one correspondence between distributions and a new kind of arrangement. Represent each cookie as a star (★) and each boundary between children's shares as a bar (|). To separate 3 children's portions you need exactly 2 bars. So a distribution of 5 cookies into 3 children corresponds to an arrangement of 5 stars and 2 bars in a row. For example, ★★|★★★| means child 1 gets 2, child 2 gets 3, child 3 gets 0. The arrangement ★|★★★|★ means child 1 gets 1, child 2 gets 3, child 3 gets 1. Every possible distribution maps to exactly one such arrangement, and vice versa.

Now counting the arrangements is just a combinations problem — the one you already know. You have 5 + 2 = 7 positions total and you choose which 2 of them are bars (equivalently, which 5 are stars). That's C(7, 2) = 21. In general, distributing n identical items into k bins requires k−1 bars, giving n + k − 1 total positions, and you choose k−1 of them for bars: **C(n+k−1, k−1)**. This is the formula, and it comes directly from the bijection, not from any special formula-memorization.

The equation interpretation makes this even more flexible. "Distribute n identical items into k bins" is the same as finding all non-negative integer solutions to x₁ + x₂ + ⋯ + xₖ = n, where xᵢ is the number of items in bin i. If you need solutions where each bin gets at least 1 item, substitute yᵢ = xᵢ − 1 to reduce to a problem with n−k items and no minimum constraint. This substitution trick extends stars and bars to a wide range of counting problems involving constraints on minimum values.
