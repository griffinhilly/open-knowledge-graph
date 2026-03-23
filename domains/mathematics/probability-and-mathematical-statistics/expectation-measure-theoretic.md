---
id: expectation-measure-theoretic
title: Expectation (Measure-Theoretic)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: distribution-functions-densities-rigorous
  type: hard
- id: expected-value
  type: soft
builds-toward:
- variance-higher-moments-rigorous
- conditional-expectation
- convergence-in-lp
tags:
- expectation
- integration
- measure-theory
stage: advanced
status: validated
---

# Expectation (Measure-Theoretic)

## Core Idea
The expectation E[X] = ∫_Ω X dP is defined as a Lebesgue integral with respect to the probability measure P, generalizing the Riemann integral definition. For X to have finite expectation, ∫_Ω |X| dP < ∞. The monotone convergence theorem and dominated convergence theorem characterize when expectations of limits equal limits of expectations.

## How It's Best Learned
Compare Riemann and Lebesgue expectations. Work examples where exchanging limits and integrals is justified (or not). Apply monotone and dominated convergence theorems.

## Common Misconceptions
- Thinking Riemann and Lebesgue integrals always coincide; they differ on sets of measure zero. - Assuming E[lim Xₙ] = lim E[Xₙ] without verifying conditions. - Forgetting that X must be integrable; finite mean is not automatic.

## Explainer

In your earlier study of expected value, you learned two formulas: E[X] = Σ xᵢ P(X = xᵢ) for discrete random variables and E[X] = ∫ x f(x) dx for continuous ones with a density. These work well in their respective settings, but they are fundamentally different formulas — and they leave out important cases. The **Cantor distribution** has no point masses and no density function; neither formula applies. Mixtures of discrete and continuous components require awkward case-splitting. The measure-theoretic definition E[X] = ∫_Ω X dP provides a single unified framework that handles all cases — discrete, continuous, singular, and mixed — under one integral sign.

The integral ∫_Ω X dP is a **Lebesgue integral** with respect to the probability measure P. It is constructed in stages: first for simple (step) functions, where the integral is a finite weighted sum; then for non-negative measurable functions, using the supremum over all simple functions below; and finally for general integrable functions by writing X = X⁺ − X⁻ (positive and negative parts) and defining ∫ X dP = ∫ X⁺ dP − ∫ X⁻ dP, provided at least one of these is finite. When both ∫ X⁺ dP and ∫ X⁻ dP are infinite, the expectation is undefined — you cannot subtract ∞ from ∞. This is why **integrability** (E[|X|] < ∞) must be verified: it guarantees both parts are finite and the expectation is a well-defined real number.

The two great convergence theorems govern when you can interchange limits and expectations. The **Monotone Convergence Theorem** (MCT) says: if 0 ≤ X₁ ≤ X₂ ≤ ⋯ and Xₙ → X pointwise, then E[Xₙ] → E[X], even if E[X] = ∞. The hypotheses are minimal — non-negativity and monotonicity. The **Dominated Convergence Theorem** (DCT) says: if Xₙ → X almost surely and |Xₙ| ≤ g for all n where E[g] < ∞, then E[Xₙ] → E[X] and moreover E[|Xₙ − X|] → 0. The dominating function g provides a uniform bound that prevents the tails of the Xₙ from carrying runaway mass. Without such a bound, the interchange can fail spectacularly — Xₙ = n · 𝟏_{(0,1/n)} converges to 0 pointwise, yet E[Xₙ] = 1 for all n.

These tools are not abstract luxuries — they are the engine behind nearly every computation in rigorous probability. The MCT is used to prove Fatou's lemma, which in turn underpins the proof of the DCT. The DCT justifies differentiation under the integral sign in moment-generating functions, the interchange of summation and integration in discrete/continuous mixtures, and the passage to limits in characteristic function arguments. Whenever you see "and by dominated convergence" in a proof, the author is invoking this theorem to justify swapping a limit and an expectation — a step that requires a domination hypothesis and is not valid in general.

## Questions

```yaml
- question: "Let Xₙ = n · 𝟏{0 < U < 1/n} where U ~ Uniform(0,1). Then Xₙ → 0 almost surely, yet E[Xₙ] = 1 for all n. Which theorem fails to apply here, and why?"
  type: multiple-choice
  options:
    - "The Monotone Convergence Theorem — it fails because the sequence is not monotone increasing"
    - "The Dominated Convergence Theorem — it fails because there is no integrable function g with |Xₙ| ≤ g for all n"
    - "The Law of Large Numbers — it fails because the Xₙ are not identically distributed"
    - "Both MCT and DCT — they fail because Xₙ does not converge in L¹"
  answer: 1
  explanation: "The DCT would allow E[lim Xₙ] = lim E[Xₙ] if there existed an integrable dominating function g with |Xₙ(ω)| ≤ g(ω) for all n and almost all ω. But Xₙ = n on (0, 1/n), and the supremum sup_n Xₙ = ∞ on (0,1) — any candidate g would need to be infinite on this set, which is not integrable. Without a dominating function, the DCT does not apply, and the exchange of limit and expectation fails. This is the canonical example showing why the dominated convergence condition is not merely technical — it is necessary."

- question: "What is the key advantage of defining expectation as E[X] = ∫_Ω X dP (a Lebesgue integral on the probability space) over the elementary definitions E[X] = Σ xᵢP(X = xᵢ) or E[X] = ∫ x f(x) dx?"
  type: multiple-choice
  options:
    - "The measure-theoretic definition is easier to compute numerically for most practical distributions"
    - "It provides a single unified framework that handles discrete, continuous, and mixed distributions — and distributions with no density — under one definition"
    - "It automatically guarantees that every random variable has a finite expectation"
    - "It eliminates the need to check measurability conditions for the random variable"
  answer: 1
  explanation: "The elementary formulas only work in their respective special cases: the sum requires a discrete distribution, the integral requires an absolutely continuous one with a density. The Lebesgue integral E[X] = ∫_Ω X dP works for any random variable on any probability space — discrete, continuous, singular (like the Cantor distribution), or mixed. This generality is not just aesthetically satisfying; it is necessary for the general theory of conditional expectation, convergence theorems, and stochastic processes, none of which can be built cleanly on the elementary definitions alone."

- question: "If Xₙ ≥ 0 for all n and Xₙ increases pointwise to X (possibly with X = ∞ on some set), the Monotone Convergence Theorem guarantees that E[Xₙ] → E[X], even when E[X] = ∞."
  type: true-false
  answer: true
  explanation: "The MCT holds without requiring finiteness of the limit: if 0 ≤ X₁ ≤ X₂ ≤ ⋯ and Xₙ → X pointwise, then ∫ Xₙ dP → ∫ X dP, where both sides may equal +∞. This is a strength of the Lebesgue integral — it handles the infinite case cleanly. The conclusion 'E[Xₙ] → ∞' is meaningful and correct when E[X] = ∞. In contrast, DCT requires a finite dominating integrable function, so DCT cannot handle this infinite limit case."

- question: "Every random variable defined on a probability space has a well-defined finite expectation, since probabilities are bounded between 0 and 1."
  type: true-false
  answer: false
  explanation: "Boundedness of P (a probability measure) does not imply that integrals of X are finite. A random variable can take arbitrarily large values with just enough probability that ∫ |X| dP = ∞. The Cauchy distribution is the canonical example: its density is f(x) = 1/(π(1+x²)), symmetric about zero, but ∫ |x| f(x) dx diverges. For the Cauchy distribution, E[X] is undefined — neither finite nor infinite in a well-defined sense. Integrability (E[|X|] < ∞) must always be verified, not assumed."

- question: "Why must we verify that E[|X|] < ∞ (absolute integrability) rather than just checking that ∫_Ω X dP converges, before concluding that E[X] is well-defined?"
  type: short-answer
  answer: "The Lebesgue integral ∫ X dP is defined as ∫ X⁺ dP − ∫ X⁻ dP, where X⁺ and X⁻ are the positive and negative parts of X. If both integrals are finite, E[X] is well-defined. But if both ∫ X⁺ dP = ∞ and ∫ X⁻ dP = ∞, then E[X] = ∞ − ∞ is undefined — not a number. Checking E[|X|] = ∫ X⁺ dP + ∫ X⁻ dP < ∞ ensures both parts are finite, so their difference is a well-defined real number."
  explanation: "This is analogous to the distinction between absolutely convergent and conditionally convergent series: a conditionally convergent series can be rearranged to converge to any value or diverge, while an absolutely convergent series has a unique well-defined sum. The Lebesgue integral is by design an 'absolute' integral — it does not extend naturally to conditionally convergent situations. Requiring E[|X|] < ∞ is what puts X in L¹(P), the natural function space for expectation, and is the prerequisite for most convergence theorems (DCT, uniform integrability, etc.)."
```
