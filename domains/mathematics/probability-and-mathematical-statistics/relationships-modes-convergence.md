---
id: relationships-modes-convergence
title: Relationships Between Modes of Convergence
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: convergence-in-probability
  type: hard
- id: almost-sure-convergence
  type: hard
- id: convergence-in-distribution
  type: hard
- id: convergence-in-lp
  type: hard
builds-toward:
- central-limit-theorem-rigorous
tags:
- convergence
- relationships
- analysis
stage: advanced
status: draft
---

# Relationships Between Modes of Convergence

## Core Idea
The convergence modes form a hierarchy: almost sure convergence implies convergence in probability, which implies convergence in distribution. L^p convergence implies convergence in L^q for p > q by Hölder's inequality. Convergence in probability and almost sure convergence are generally incomparable. Understanding these relationships helps select the appropriate convergence mode for applications.

## How It's Best Learned
Draw the hierarchy diagram showing implications. Work examples showing non-implications (e.g., convergence in distribution does not imply convergence in probability). Construct explicit counterexamples.

## Common Misconceptions
- Thinking all modes of convergence are equivalent. - Believing convergence in distribution implies convergence in probability. - Forgetting that almost sure and in-probability convergence are not directly comparable.

## Explainer

You have studied four distinct ways a sequence of random variables Xₙ can converge to a limit X: almost surely (a.s.), in probability, in distribution, and in Lᵖ. Each definition makes a different type of claim about how Xₙ approaches X. Understanding these modes in isolation is necessary but not sufficient — the real analytical power comes from knowing which modes imply which others, and from developing the habit of asking "which type of convergence do I actually need for this theorem?"

The main hierarchy runs: **a.s. ⟹ in probability ⟹ in distribution**. Almost sure convergence says P(lim_{n→∞} Xₙ = X) = 1 — the convergence happens on a probability-1 set of sample paths. This is a strong pathwise statement, and it implies convergence in probability: if Xₙ → X on almost every path, then for any ε > 0, the probability that |Xₙ − X| > ε must vanish. Convergence in probability is weaker because it only asks that Xₙ is within ε of X *most* of the time, without requiring the exceptional excursions to disappear forever. Convergence in distribution is weaker still: it only requires that the CDFs Fₙ(t) → F(t) at continuity points of F — the limit X need not even live on the same probability space as the Xₙ.

None of these implications reverses. The canonical counterexample for "in probability ⟹ a.s." is the **typewriter sequence**: on [0,1] with Lebesgue measure, define Xₙ as the indicator of a sliding interval that covers every point infinitely often. Xₙ → 0 in probability (the interval's length shrinks to 0), but Xₙ(ω) fails to converge for any ω (every point is visited by infinitely many intervals). For "in distribution ⟹ in probability," let Xₙ = X for all n where X ~ N(0,1), and let Y be an independent N(0,1) copy. Then Xₙ → Y in distribution (both are N(0,1)) but P(|Xₙ − Y| > ε) = P(|X − Y| > ε) > 0 for all n — no convergence in probability.

The Lᵖ modes connect via two key facts: **Lᵖ ⟹ in probability** (by Markov's inequality: P(|Xₙ − X| > ε) ≤ E[|Xₙ − X|ᵖ]/εᵖ → 0), and **Lᵖ ⟹ Lq for p > q** (by Hölder's inequality). But Lᵖ convergence and a.s. convergence are independent of each other — neither implies the other in general. The complete diagram has a.s. and Lᵖ both pointing to in probability, which points to in distribution, with no arrows pointing backward. When a theorem requires one mode and you have another, checking this diagram immediately tells you whether your hypothesis is sufficient — or whether you need an additional condition like uniform integrability to bridge the gap.
