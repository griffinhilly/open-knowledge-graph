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
status: validated
---

# Strong Law of Large Numbers

## Core Idea
If {Xₙ} are i.i.d. with finite mean μ, then Sₙ/n converges almost surely to μ: P(lim_{n→∞} Sₙ/n = μ) = 1. This is stronger than the weak law. The proof uses the Borel-Cantelli lemmas (for bounded random variables) or truncation arguments. The SLLN provides certainty (up to sets of probability zero) rather than just high probability.

## Questions

```yaml
- question: "A casino game has a house edge of μ = $0.05 per play. The Weak Law of Large Numbers guarantees that for large n, the average profit per game is close to $0.05 with high probability. What does the Strong Law add that the Weak Law does not?"
  type: multiple-choice
  options:
    - "The Strong Law guarantees the total profit grows without bound"
    - "The Strong Law guarantees that with probability 1, the running average of profit per game converges permanently to $0.05, not just that it is close at each fixed large n"
    - "The Strong Law guarantees convergence for dependent random variables, while the Weak Law requires independence"
    - "The Strong Law gives a faster rate of convergence than the Weak Law"
  answer: 1
  explanation: "The Weak Law says P(|Sₙ/n − μ| > ε) → 0 for any fixed ε — a statement about snapshots at individual n. It does not rule out the average escaping ε infinitely often, as long as those excursions become progressively rarer. The Strong Law closes this gap: P(limₙ Sₙ/n = μ) = 1. This is almost sure convergence — the set of sample paths that fail to converge to μ has probability zero. The trajectory itself settles down permanently."

- question: "A textbook states: 'Since P(|Sₙ/n − μ| > ε) → 0 for all ε, the sample average must eventually stay within ε of μ for all sufficiently large n.' Is this a valid conclusion from the Weak Law alone?"
  type: multiple-choice
  options:
    - "Yes — this follows immediately from the definition of convergence in probability"
    - "No — convergence in probability only controls probabilities at each fixed n; it does not prevent the average from returning outside ε infinitely often as n grows"
    - "Yes, but only when the random variables are bounded"
    - "No — this would require the Central Limit Theorem, not just the Weak Law"
  answer: 1
  explanation: "This is the key misconception separating the Weak and Strong Laws. Convergence in probability says: for any fixed ε, the probability of exceeding it at step n goes to zero. But it allows the running average to wander outside ε on a sparse-but-infinite set of times — the 'occasionally bad' behavior can persist forever while still having vanishingly small probability at each individual n. Almost sure convergence (the Strong Law) rules this out by asserting that with probability 1, there exists N such that for all n ≥ N, |Sₙ/n − μ| < ε."

- question: "Almost sure convergence implies convergence in probability."
  type: true-false
  answer: true
  explanation: "Almost sure convergence is strictly stronger. If Sₙ/n → μ almost surely, then for any ε > 0, the set of ω where Sₙ(ω)/n fails to be close to μ for large n has probability zero — and in particular, the probability of the event {|Sₙ/n − μ| > ε} must go to zero. The reverse is not true: there exist sequences that converge in probability but not almost surely (the 'sliding bump' example in probability textbooks)."

- question: "The classical Strong Law of Large Numbers requires that the random variables have finite second moment (finite variance)."
  type: true-false
  answer: false
  explanation: "The SLLN holds under the weaker condition that the Xᵢ are i.i.d. with finite first moment E[|X₁|] < ∞. Finite variance is sufficient for the Weak Law via Chebyshev's inequality, but it is not necessary for the Strong Law. The proof for unbounded variables uses a truncation argument — approximate Xᵢ by truncated versions with bounded support, prove the SLLN for those, then show the error from truncating is negligible almost surely."

- question: "Explain why the Weak Law of Large Numbers does not guarantee that the sample average 'eventually stays close' to μ, and what the Strong Law adds to give this guarantee."
  type: short-answer
  answer: "The Weak Law says P(|Sₙ/n − μ| > ε) → 0 for each fixed ε — a pointwise statement about individual time steps. This is compatible with the average oscillating away from μ infinitely often, as long as those excursions become increasingly rare. The Strong Law asserts P(lim_{n→∞} Sₙ/n = μ) = 1 — a statement about the whole trajectory. Almost sure convergence means: except for a set of sample paths of measure zero, the running average eventually settles within ε of μ and stays there. The Borel-Cantelli approach makes this precise: by showing the sum of probabilities P(|Sₙ/n − μ| > ε) converges, one concludes (via first Borel-Cantelli) that the bad events occur only finitely many times almost surely."
```

## Explainer

You know from the Weak Law of Large Numbers that for any ε > 0, P(|Sₙ/n − μ| > ε) → 0 as n → ∞. This says that for any fixed threshold, the probability of being far from the mean goes to zero. But it leaves open a disconcerting possibility: the sample average could wander far from μ infinitely often, as long as those excursions become increasingly rare. The **Strong Law of Large Numbers** closes this gap: with probability 1, the sample average *actually converges* to μ — meaning you could observe the entire infinite sequence X₁, X₂, X₃, … and the running average would settle down permanently to μ, not just occasionally get close.

The difference between weak and strong convergence is precisely the difference you studied between convergence in probability and **almost sure convergence**. Almost sure convergence requires P({ω : Sₙ(ω)/n → μ}) = 1 — the set of sample paths on which the average fails to converge has probability zero. This is a statement about the whole trajectory, not just about snapshots at individual n. It is possible for Sₙ/n to converge in probability to μ without converging almost surely — but the SLLN guarantees both simultaneously.

The **Borel-Cantelli lemmas** are the key tools in the proof for bounded random variables. First Borel-Cantelli says: if Σ P(Aₙ) < ∞, then P(infinitely many Aₙ occur) = 0. Applying this to the events Aₙ = {|Sₙ/n − μ| > ε}: the goal is to show the sum of their probabilities converges, which implies the average can exceed ε for only finitely many n (with probability 1). For bounded variables, Chebyshev-like tail bounds give P(Aₙ) ≤ C/n², whose sum converges. For unbounded i.i.d. variables with finite mean, a **truncation argument** handles the heavy tails separately — approximate the Xᵢ by truncated versions, prove the SLLN for those, then show the truncation error is negligible almost surely.

The practical meaning is profound. If you run a casino game with house edge μ > 0 indefinitely, the SLLN says your profit per game *will* converge to μ — not just with high probability, but with certainty in the measure-theoretic sense. Actuaries rely on this when pricing insurance over large portfolios. Physicists rely on it when equating time averages with ensemble averages in ergodic systems. The SLLN is what transforms μ from a theoretical expectation into an empirically observable frequency — the mathematical foundation for the entire enterprise of statistical estimation from data.
