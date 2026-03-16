---
id: strong-law-of-large-numbers
title: Strong Law of Large Numbers
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: weak-law-of-large-numbers
  type: soft
- id: almost-sure-convergence
  type: hard
- id: borel-cantelli-lemmas
  type: hard
builds-toward:
- central-limit-theorem-rigorous
tags:
- law-of-large-numbers
- limit-theorems
- probability
stage: advanced
status: draft
---

# Strong Law of Large Numbers

## Core Idea
If {Xₙ} are i.i.d. with finite mean μ, then Sₙ/n converges almost surely to μ: P(lim_{n→∞} Sₙ/n = μ) = 1. This is stronger than the weak law. The proof uses the Borel-Cantelli lemmas (for bounded random variables) or truncation arguments. The SLLN provides certainty (up to sets of probability zero) rather than just high probability.

## Explainer

You know from the Weak Law of Large Numbers that for any ε > 0, P(|Sₙ/n − μ| > ε) → 0 as n → ∞. This says that for any fixed threshold, the probability of being far from the mean goes to zero. But it leaves open a disconcerting possibility: the sample average could wander far from μ infinitely often, as long as those excursions become increasingly rare. The **Strong Law of Large Numbers** closes this gap: with probability 1, the sample average *actually converges* to μ — meaning you could observe the entire infinite sequence X₁, X₂, X₃, … and the running average would settle down permanently to μ, not just occasionally get close.

The difference between weak and strong convergence is precisely the difference you studied between convergence in probability and **almost sure convergence**. Almost sure convergence requires P({ω : Sₙ(ω)/n → μ}) = 1 — the set of sample paths on which the average fails to converge has probability zero. This is a statement about the whole trajectory, not just about snapshots at individual n. It is possible for Sₙ/n to converge in probability to μ without converging almost surely — but the SLLN guarantees both simultaneously.

The **Borel-Cantelli lemmas** are the key tools in the proof for bounded random variables. First Borel-Cantelli says: if Σ P(Aₙ) < ∞, then P(infinitely many Aₙ occur) = 0. Applying this to the events Aₙ = {|Sₙ/n − μ| > ε}: the goal is to show the sum of their probabilities converges, which implies the average can exceed ε for only finitely many n (with probability 1). For bounded variables, Chebyshev-like tail bounds give P(Aₙ) ≤ C/n², whose sum converges. For unbounded i.i.d. variables with finite mean, a **truncation argument** handles the heavy tails separately — approximate the Xᵢ by truncated versions, prove the SLLN for those, then show the truncation error is negligible almost surely.

The practical meaning is profound. If you run a casino game with house edge μ > 0 indefinitely, the SLLN says your profit per game *will* converge to μ — not just with high probability, but with certainty in the measure-theoretic sense. Actuaries rely on this when pricing insurance over large portfolios. Physicists rely on it when equating time averages with ensemble averages in ergodic systems. The SLLN is what transforms μ from a theoretical expectation into an empirically observable frequency — the mathematical foundation for the entire enterprise of statistical estimation from data.
