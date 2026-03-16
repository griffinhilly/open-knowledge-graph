---
id: subsequences
title: Subsequences
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- bolzano-weierstrass-theorem
- limit-superior-and-inferior
tags:
- subsequences
- convergence
- selections
stage: advanced
status: draft
---

# Subsequences

## Core Idea
A subsequence of (aₙ) is a sequence (aₙₖ) where n₁ < n₂ < n₃ < ... A key fact: if (aₙ) converges to L, then every subsequence converges to L. Conversely, existence of convergent subsequences is a weaker property that allows us to extract convergence from non-convergent sequences.

## How It's Best Learned
Given (-1)ⁿ, identify its convergent subsequences: a₂ₖ → 1 and a₂ₖ₊₁ → -1. Extract a convergent subsequence from sin(n): though sin(n) oscillates chaotically, Bolzano-Weierstrass guarantees a convergent sub-sequence exists.

## Common Misconceptions
- Thinking a subsequence must be 'regular' (e.g., every other term); any selection with increasing indices counts.
- Assuming if a sequence diverges, no subsequence converges.
- Confusing the order: convergence ⟹ all subsequences converge, but not vice versa.

## Explainer

From your work on **ε-N convergence**, you know what it means for a sequence (aₙ) to converge to a limit L: for every ε > 0, all sufficiently far-out terms stay within ε of L. A **subsequence** is obtained by selecting an infinite subset of the original sequence's terms, preserving their original order. Formally, you choose a strictly increasing sequence of indices n₁ < n₂ < n₃ < ... and form the new sequence (aₙ₁, aₙ₂, aₙ₃, ...). The key word is *strictly increasing indices* — you can skip terms, but you cannot reorder them or repeat them.

The first major fact is that convergence is inherited by all subsequences: if aₙ → L, then every subsequence also converges to L. The ε-N proof is almost immediate — if all terms from index N onward are within ε of L, then in particular the subsequence terms with nₖ ≥ N are within ε of L, and since nₖ → ∞, eventually every nₖ ≥ N. The converse direction is more powerful and surprising: if you can find *two* subsequences that converge to *different* limits, the original sequence cannot converge. This is why (−1)ⁿ diverges — the even-indexed terms converge to 1 and the odd-indexed terms converge to −1, which is a contradiction with any single limit L.

The deeper use of subsequences is extracting convergence from sequences that do not themselves converge. A bounded sequence in ℝ need not converge — consider (sin n), which oscillates chaotically and never settles — but it cannot escape to infinity either. The **Bolzano-Weierstrass theorem**, which you will encounter next, guarantees that every bounded sequence in ℝ has at least one convergent subsequence. This means bounded sequences always contain "convergent pieces" even if the whole sequence misbehaves. Subsequences are the tool for identifying those pieces.

Think of it as a filtering operation. The original sequence might contain too much noise to see a limit. A subsequence is a principled act of selective attention — you choose the terms that exhibit the behavior you are studying and ignore the rest. The richness of a sequence's behavior can be read off from its convergent subsequences: their limit points are exactly the **limit superior** and **limit inferior**, which tell you the highest and lowest values the sequence accumulates near. Subsequences thus give you a vocabulary for describing not just whether a sequence converges, but *how* it fails to converge — and that vocabulary is essential throughout real analysis and topology.
