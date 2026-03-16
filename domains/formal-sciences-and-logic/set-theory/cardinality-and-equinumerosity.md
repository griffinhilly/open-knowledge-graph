---
id: cardinality-and-equinumerosity
title: Cardinality and Equinumerosity
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: injections-surjections-bijections-classification
  type: hard
- id: bijection-counting-principle
  type: soft
builds-toward:
- finite-sets-and-natural-numbers
- countably-infinite-sets
tags:
- cardinality
- equinumerosity
- size
- bijection
stage: formal-systems
status: draft
---

# Cardinality and Equinumerosity

## Core Idea
Two sets have the same cardinality if there exists a bijection between them. This extends the notion of set size beyond finite collections to all sets, allowing meaningful comparison of infinite sets. For any two sets A and B, exactly one of |A| < |B|, |A| = |B|, or |A| > |B| holds by the Cantor-Schröder-Bernstein theorem.

## How It's Best Learned
Construct explicit bijections: f(n) = 2n shows ℕ and the even natural numbers have equal cardinality. Use Cantor-Schröder-Bernstein: if injections f: A → B and g: B → A exist, then |A| = |B|. Verify with standard pairs: ℕ ≅ ℤ ≅ ℚ.

## Common Misconceptions
- Thinking ℕ and 2ℕ have different cardinalities because 2ℕ ⊂ ℕ (they are equinumerous). - Assuming cardinality is always a number; cardinality is an equivalence class of sets. - Confusing 'same cardinality' with 'same elements'—cardinality measures size, not identity.

## Explainer

You already understand injections, surjections, and bijections — functions with precise structural properties. Cardinality repurposes bijections as the measuring instrument for size. The definition is precise: two sets A and B are **equinumerous** (have the same **cardinality**, written |A| = |B|) if and only if there exists a bijection f: A → B. For finite sets this agrees with your intuitive notion of size: {a, b, c} and {1, 2, 3} have the same cardinality because f(a)=1, f(b)=2, f(c)=3 is a bijection. The powerful move is that this definition applies to infinite sets too, where your intuition about size breaks down.

The counterintuitive results follow immediately. Let **ℕ** = {0, 1, 2, 3, ...} and let **2ℕ** = {0, 2, 4, 6, ...} be the even natural numbers. Since 2ℕ ⊂ ℕ, it seems smaller. But the function f(n) = 2n is a bijection from ℕ to 2ℕ: every natural number maps to a unique even, and every even comes from some natural number. So |ℕ| = |2ℕ|. Similarly, f(n) = n+1 maps ℕ bijectively onto {1, 2, 3, ...}, and the function f(n) = (−1)^n · ⌊(n+1)/2⌋ maps ℕ bijectively onto ℤ. The key lesson: for infinite sets, "proper subset" does not imply "smaller cardinality." In fact, the ability to biject with a proper subset is a *definition* of being infinite (Dedekind infinite).

The **Cantor-Schröder-Bernstein theorem** is the main technical tool for proving equinumerosity without constructing an explicit bijection. It says: if there is an injection f: A → B and an injection g: B → A, then there is a bijection h: A → B and hence |A| = |B|. This is powerful because injections are often easier to construct than bijections. To show |ℝ| = |(0,1)|, you inject (0,1) into ℝ via the identity, and inject ℝ into (0,1) via the arctan function (scaled and shifted). Both injections exist, so the sets are equinumerous even though (0,1) is a bounded interval and ℝ is the whole line.

Cardinality defines a **partial order** on sets: |A| ≤ |B| if there is an injection A → B. The Cantor-Schröder-Bernstein theorem shows this is actually a total order on cardinalities: for any two sets, either |A| ≤ |B| or |B| ≤ |A| (assuming the axiom of choice). And the ordering is non-trivial for infinite sets: Cantor's diagonal argument shows |ℕ| < |ℝ| — the real numbers are *strictly* larger than the naturals, meaning no bijection between them exists. This means there are different **sizes of infinity**, and cardinality is the precise language for comparing them. You'll explore this hierarchy further when you study countable and uncountable sets.

