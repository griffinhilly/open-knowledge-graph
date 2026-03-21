---
id: joint-distributions-marginals-rigorous
title: Joint Distributions and Marginals (Rigorous)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: distribution-functions-densities-rigorous
  type: hard
- id: iterated-integrals
  type: hard
builds-toward:
- conditional-expectation
- independence-sigma-algebras
- multivariate-normal-distribution
tags:
- multivariate
- joint-distributions
- measure-theory
stage: advanced
status: draft
---

# Joint Distributions and Marginals (Rigorous)

## Core Idea
For random vector X = (X₁, ..., Xₙ), the joint CDF is F(x₁,...,xₙ) = P(X₁ ≤ x₁,...,Xₙ ≤ xₙ). Marginal distributions describe individual Xᵢ. A joint pdf f satisfies P((X₁,...,Xₙ) ∈ A) = ∫ₐ f(x₁,...,xₙ) dx₁...dxₙ. The Radon-Nikodym theorem guarantees densities when distributions are absolutely continuous.

## Questions

```yaml
- question: "Random variables X and Y each have marginal distributions that are Uniform[0,1]. Which of the following conclusions necessarily follows?"
  type: multiple-choice
  options:
    - "The joint pdf must be f(x,y) = 1 on the unit square — they must be independent"
    - "The joint CDF is fully determined by the two marginals"
    - "The joint distribution could be any of infinitely many possibilities — independent, positively correlated, negatively correlated, and more — all consistent with these marginals"
    - "X and Y must have zero covariance because they share the same marginal"
  answer: 2
  explanation: "Marginal distributions describe each variable in isolation; they do not determine how the variables relate to each other. Two random variables can share identical marginals while being independent, perfectly positively correlated, perfectly negatively correlated, or anything in between. The joint distribution encodes the dependence structure, which the marginals alone cannot recover. This is the central insight of the topic: the joint contains strictly more information than the marginals together."

- question: "To rigorously verify that two continuous random variables X and Y are independent, you must show:"
  type: multiple-choice
  options:
    - "Their means and variances are equal"
    - "The joint pdf factors as f(x,y) = f_X(x) · f_Y(y) for (almost) all (x,y)"
    - "Their marginal pdfs each integrate to 1"
    - "Their covariance equals zero"
  answer: 1
  explanation: "Independence is precisely the condition that the joint pdf factors into the product of the marginals. This factorization must hold across all (x,y), not just at selected points. Note that zero covariance (option D) is *necessary* for independence but not sufficient — two dependent variables can have zero covariance (e.g., if Y = X²). The factorization of the joint pdf is the rigorous definition and the primary verification tool."

- question: "If two random variables have identical marginal distributions, they must have the same joint distribution."
  type: true-false
  answer: false
  explanation: "This is the most important misconception this topic addresses. Shared marginals do not determine the joint distribution. A standard counterexample: X and Y both Uniform[0,1] as marginals, but (X,Y) could be jointly uniform on the unit square (independent) or supported only on the diagonal y = x (perfectly correlated) — the marginals are the same in both cases, but the joint distributions are completely different."

- question: "The marginal pdf of X₁ from a continuous joint distribution can be obtained by integrating the joint pdf f(x₁, x₂) over all values of x₂."
  type: true-false
  answer: true
  explanation: "This is the defining operation for marginals: f₁(x₁) = ∫₋∞^∞ f(x₁, x₂) dx₂. The integration 'sums over' all possible values of the second variable, collapsing the two-dimensional distribution onto one axis. Fubini's theorem, applicable under the absolute continuity assumptions that justify the existence of the joint density via Radon-Nikodym, guarantees this integration is well-defined and can be performed in either order."

- question: "Why does knowing both marginal distributions of a random vector (X, Y) not give you the complete probabilistic story of (X, Y)?"
  type: short-answer
  answer: "The marginals describe each variable in isolation — X's distribution ignoring Y, and Y's distribution ignoring X. They contain no information about how the two variables relate to each other. The joint distribution encodes whether large X values tend to coincide with large Y values, whether the variables are independent, and so on. Two distributions can have identical marginals while being completely independent or tightly correlated; only the joint distribution distinguishes them."
  explanation: "The point generalizes: in statistics, knowing the marginal distributions of two (or more) variables is often insufficient for prediction, simulation, or inference about joint events. The joint distribution — and specifically the dependence structure it encodes — is what matters for questions like 'what is the probability that both X > a and Y > b?' Marginals only answer questions about each variable separately."
```

## Explainer

From your prerequisite on **distribution functions and densities**, you know that a real-valued random variable X is characterized by its CDF F(x) = P(X ≤ x), and that when F is absolutely continuous, its derivative yields the **probability density function** (pdf) f with P(X ∈ A) = ∫ₐ f(x) dx. The rigorous treatment of joint distributions extends every part of this framework to random vectors — pairs, triples, and n-tuples of random variables observed simultaneously.

For a random vector (X₁, X₂), the **joint CDF** is F(x₁, x₂) = P(X₁ ≤ x₁ and X₂ ≤ x₂). This is a function of two variables encoding all probabilistic information about how X₁ and X₂ behave together. When the joint CDF is absolutely continuous (with respect to two-dimensional Lebesgue measure), the **Radon-Nikodym theorem** — the measure-theoretic version of the fundamental theorem of calculus — guarantees the existence of a **joint pdf** f(x₁, x₂) satisfying F(x₁, x₂) = ∫₋∞^x₁ ∫₋∞^x₂ f(u, v) dv du. Probabilities of any measurable set A are then computed using your prerequisite skill of **iterated integrals**: P((X₁, X₂) ∈ A) = ∬_A f(x₁, x₂) dx₁ dx₂. The Radon-Nikodym condition matters precisely because it rules out distributions with point masses, which cannot be represented by a density in the usual sense.

**Marginal distributions** recover the behavior of individual variables from the joint. For continuous random variables, the marginal pdf of X₁ is obtained by integrating out X₂: f₁(x₁) = ∫₋∞^∞ f(x₁, x₂) dx₂. The intuition is that you are "summing over" all possible values of the second variable, collapsing the two-dimensional distribution onto one axis. The order of integration in iterated integrals (Fubini's theorem) justifies swapping the roles of x₁ and x₂ freely when f is non-negative or integrable, which is guaranteed under the standing absolute continuity assumption. This is why rigorous control over when densities exist — via Radon-Nikodym — matters: it ensures Fubini applies.

The distinction between the joint distribution and the marginals is fundamental to everything that follows. Two random variables can have the same marginal distributions but completely different joint distributions — one might be independent, the other tightly correlated. The joint pdf carries more information than the two marginals separately. **Independence** is the special case where the joint pdf factors: f(x₁, x₂) = f₁(x₁) · f₂(x₂). Verifying this factorization (or its failure) using iterated integrals is the primary technical tool. The rigorous language of sigma-algebras, which this topic builds toward, allows independence to be extended beyond pairs of random variables to whole families — but the density-level intuition you develop here, integrating over one coordinate at a time, is exactly what carries over.
