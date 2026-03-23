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
status: validated
---

# Relationships Between Modes of Convergence

## Core Idea
The convergence modes form a hierarchy: almost sure convergence implies convergence in probability, which implies convergence in distribution. L^p convergence implies convergence in L^q for p > q by Hölder's inequality. Convergence in probability and almost sure convergence are generally incomparable. Understanding these relationships helps select the appropriate convergence mode for applications.

## How It's Best Learned
Draw the hierarchy diagram showing implications. Work examples showing non-implications (e.g., convergence in distribution does not imply convergence in probability). Construct explicit counterexamples.

## Common Misconceptions
- Thinking all modes of convergence are equivalent. - Believing convergence in distribution implies convergence in probability. - Forgetting that almost sure and in-probability convergence are not directly comparable.

## Questions

```yaml
- question: "A sequence of random variables satisfies Xₙ → X in distribution. Under which additional condition does this imply convergence in probability?"
  type: multiple-choice
  options:
    - "When the Xₙ are mutually independent"
    - "When E[|Xₙ|] is uniformly bounded"
    - "When X is a constant (the limit distribution is degenerate)"
    - "Convergence in distribution always implies convergence in probability"
  answer: 2
  explanation: "Convergence in distribution generally does NOT imply convergence in probability. Canonical counterexample: let Xₙ = X for all n and Y be an independent copy of X ~ N(0,1). Then Xₙ → Y in distribution but P(|Xₙ − Y| > ε) = P(|X − Y| > ε) > 0 for all n — no convergence in probability. The exception is when the limit is a constant c: P(|Xₙ − c| > ε) = Fₙ(c−ε) + (1−Fₙ(c+ε)) → 0 + 0 = 0 by convergence of CDFs at continuity points."

- question: "You know that E[|Xₙ − X|²] → 0 (convergence in L²). Which conclusions are guaranteed?"
  type: multiple-choice
  options:
    - "Xₙ → X almost surely"
    - "Xₙ → X in probability and in L¹"
    - "Xₙ → X almost surely and in distribution"
    - "Only convergence in distribution is guaranteed"
  answer: 1
  explanation: "L² convergence implies: (1) convergence in probability, via Markov's inequality P(|Xₙ−X| > ε) ≤ E[|Xₙ−X|²]/ε² → 0; and (2) L¹ convergence, since Lᵖ ⟹ Lq for p > q by Hölder's inequality. But L² convergence does NOT imply almost sure convergence — the typewriter sequence converges to 0 in all Lᵖ but fails to converge a.s. at any point."

- question: "Almost sure convergence implies convergence in probability, but convergence in probability does not imply almost sure convergence."
  type: true-false
  answer: true
  explanation: "The implication a.s. ⟹ in probability is standard: if Xₙ → X on a probability-1 set of paths, then P(|Xₙ−X| > ε) → 0. The reverse fails: the 'typewriter sequence' on [0,1] — indicators of sliding intervals whose lengths shrink to zero — converges to 0 in probability but not a.s., since every ω is hit by infinitely many indicators and thus Xₙ(ω) oscillates between 0 and 1 for every ω."

- question: "If Xₙ → X almost surely, then Xₙ → X in L¹."
  type: true-false
  answer: false
  explanation: "Almost sure convergence and L¹ convergence are incomparable — neither implies the other in general. Counterexample for a.s. ⟹ L¹ failing: Xₙ = n·𝟏_{[0,1/n]} on [0,1]. Then Xₙ(ω) → 0 for all ω > 0 (a.s. convergence), but E[|Xₙ|] = n·(1/n) = 1 for all n — no L¹ convergence. The bridge from a.s. to L¹ requires the additional condition of uniform integrability (Vitali's theorem)."

- question: "Explain why convergence in distribution is strictly weaker than convergence in probability, and what conceptual difference accounts for this."
  type: short-answer
  answer: "Convergence in distribution (Xₙ →_d X) only requires that CDFs converge: Fₙ(t) → F(t) at continuity points of F. This is a statement about probability laws — not about how Xₙ and X are related as functions on a common probability space. Xₙ and X don't even need to be defined on the same space. Convergence in probability (Xₙ →_P X) requires both to live on the same space with P(|Xₙ−X| > ε) → 0. Two sequences can converge to the same distributional limit while the random variables themselves remain far apart in probability — as illustrated by independent copies of the same distribution."
  explanation: "The practical consequence: the CLT gives convergence in distribution. Strengthening to almost sure convergence (as in the strong LLN) requires different techniques, and the distinction matters when you need pathwise arguments rather than distributional ones."
```

## Explainer

You have studied four distinct ways a sequence of random variables Xₙ can converge to a limit X: almost surely (a.s.), in probability, in distribution, and in Lᵖ. Each definition makes a different type of claim about how Xₙ approaches X. Understanding these modes in isolation is necessary but not sufficient — the real analytical power comes from knowing which modes imply which others, and from developing the habit of asking "which type of convergence do I actually need for this theorem?"

The main hierarchy runs: **a.s. ⟹ in probability ⟹ in distribution**. Almost sure convergence says P(lim_{n→∞} Xₙ = X) = 1 — the convergence happens on a probability-1 set of sample paths. This is a strong pathwise statement, and it implies convergence in probability: if Xₙ → X on almost every path, then for any ε > 0, the probability that |Xₙ − X| > ε must vanish. Convergence in probability is weaker because it only asks that Xₙ is within ε of X *most* of the time, without requiring the exceptional excursions to disappear forever. Convergence in distribution is weaker still: it only requires that the CDFs Fₙ(t) → F(t) at continuity points of F — the limit X need not even live on the same probability space as the Xₙ.

None of these implications reverses. The canonical counterexample for "in probability ⟹ a.s." is the **typewriter sequence**: on [0,1] with Lebesgue measure, define Xₙ as the indicator of a sliding interval that covers every point infinitely often. Xₙ → 0 in probability (the interval's length shrinks to 0), but Xₙ(ω) fails to converge for any ω (every point is visited by infinitely many intervals). For "in distribution ⟹ in probability," let Xₙ = X for all n where X ~ N(0,1), and let Y be an independent N(0,1) copy. Then Xₙ → Y in distribution (both are N(0,1)) but P(|Xₙ − Y| > ε) = P(|X − Y| > ε) > 0 for all n — no convergence in probability.

The Lᵖ modes connect via two key facts: **Lᵖ ⟹ in probability** (by Markov's inequality: P(|Xₙ − X| > ε) ≤ E[|Xₙ − X|ᵖ]/εᵖ → 0), and **Lᵖ ⟹ Lq for p > q** (by Hölder's inequality). But Lᵖ convergence and a.s. convergence are independent of each other — neither implies the other in general. The complete diagram has a.s. and Lᵖ both pointing to in probability, which points to in distribution, with no arrows pointing backward. When a theorem requires one mode and you have another, checking this diagram immediately tells you whether your hypothesis is sufficient — or whether you need an additional condition like uniform integrability to bridge the gap.
