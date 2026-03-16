---
id: set-equality-and-extensionality
title: Set Equality and Extensionality
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: set-membership-and-notation
  type: hard
- id: extensionality-axiom
  type: soft
builds-toward:
- subset-proper-subset-relations
tags:
- equality
- extensionality
- foundation
stage: formal-systems
status: draft
---

# Set Equality and Extensionality

## Core Idea
Two sets are equal if and only if they contain exactly the same elements—the principle of extensionality. This means {1,2,3} = {3,2,1} and {x | x² = 4, x ∈ ℤ} = {-2,2}. Sets are completely determined by their membership, independent of how they are described.

## Explainer

You already know what set membership means: the statement x ∈ A says that x belongs to A. The **principle of extensionality** takes that single relationship and makes it the whole story. Two sets are equal — not just equivalent or interchangeable, but literally the same object — if and only if they have exactly the same members. Nothing else counts: not the name of the set, not the order elements were listed, not the description used to define it. The set *is* its extension.

This collapses many apparently different descriptions to the same set. Consider {1, 2, 3} and {3, 1, 2}. These look distinct in notation, but membership is the only test: is 1 in both? Yes. Is 2 in both? Yes. Is 3 in both? Yes. Is anything in either set that's not in the other? No. By extensionality, they are identical. Similarly, {x ∈ ℤ : x² = 4} and {-2, 2} are the same set — not because we *decided* to equate them, but because they have identical membership rosters. The **intension** (how we described it) is irrelevant; the **extension** (what's actually in it) is everything.

This principle also gives set equality a rigorous logical form. To prove A = B, you prove two biconditionals: for every x, x ∈ A if and only if x ∈ B. In practice this usually breaks into two directions — show A ⊆ B, then show B ⊆ A — a proof structure you will use constantly once you reach subset relations. Extensionality is what makes that strategy valid: if every member of A is in B and every member of B is in A, there is nothing left to distinguish them.

One subtle but important implication: the **empty set** is unique. There is only one set with no elements, because any two empty sets have the same (vacuous) membership roster. Extensionality makes ∅ a definite object, not a vague concept. This is one of the foundational reasons set theory, once axiomatized, can be precise enough to serve as a foundation for mathematics: equality between sets is fully determined by membership facts, and nothing else.

## How It's Best Learned
Work through examples where the same set is specified multiple ways — a list, a rule, a complement — and practice verifying equality by checking membership in both directions. The discipline of writing "show A ⊆ B and B ⊆ A" builds the habit extensionality requires.
