---
id: introduction-lebesgue-integral
title: Introduction to the Lebesgue Integral
domain: mathematics
course: real-analysis
prerequisites:
- id: introduction-lebesgue-measure
  type: hard
- id: fundamental-theorem-calculus-rigorous
  type: soft
tags:
- lebesgue-integral
- measure-theory
- integration
stage: advanced
status: draft
---

# Introduction to the Lebesgue Integral

## Core Idea
The Lebesgue integral extends integration to a larger class of functions using measure theory. For a non-negative measurable function f, ∫ f dμ is defined by partitioning the range (not the domain) and summing contributions weighted by measure. The Lebesgue integral has superior convergence theorems (Dominated Convergence, Monotone Convergence) compared to the Riemann integral.

## Questions

```yaml
- question: "What does the Lebesgue integral of the Dirichlet function (1 on rationals, 0 on irrationals) over [0,1] equal?"
  type: multiple-choice
  options:
    - "1, because there are infinitely many rationals in [0,1]"
    - "1/2, because rationals and irrationals are each dense in [0,1]"
    - "0, because the rationals have Lebesgue measure zero"
    - "Undefined — the Dirichlet function is not Lebesgue measurable"
  answer: 2
  explanation: "The Dirichlet function equals 0 almost everywhere (the set of rationals has measure zero; irrationals fill the interval in measure). The Lebesgue integral handles this cleanly: the contribution from the value '1' is 1 × μ({rationals}) = 1 × 0 = 0. The Riemann integral fails here because every subinterval contains both rationals and irrationals, so upper and lower Riemann sums never agree. This is a paradigm case of why measure-theoretic integration is strictly more powerful."

- question: "The Dominated Convergence Theorem says you can always interchange limits and Lebesgue integrals: lim ∫ fₙ = ∫ lim fₙ."
  type: true-false
  answer: false
  explanation: "The DCT requires a crucial hypothesis: there must exist an integrable dominating function g such that |fₙ(x)| ≤ g(x) for all n and almost all x. Without this 'ceiling,' interchange of limits and integrals can fail — even pointwise converging sequences can have integrals that don't converge to the integral of the limit (e.g., functions that shift mass toward infinity). The dominating function prevents the fₙ from escaping to infinity, which is what justifies the interchange."

- question: "The fundamental difference between Riemann and Lebesgue integration is that Lebesgue integration uses finer partitions of the domain."
  type: true-false
  answer: false
  explanation: "This is the key misconception. The Riemann integral partitions the *domain* into intervals, regardless of how fine. The Lebesgue integral partitions the *range* — it asks 'for which x-values does f(x) lie in [a,b]?' and measures the preimage. This reversal is not a refinement of Riemann's approach; it is a conceptually different strategy. It is what allows the integral to handle irregular functions like the Dirichlet function and to interact cleanly with measure-theoretic structure."

- question: "A sequence of non-negative measurable functions fₙ increases pointwise to f. According to the Monotone Convergence Theorem, what can you conclude?"
  type: multiple-choice
  options:
    - "∫ fₙ dμ → ∫ f dμ, provided fₙ converges uniformly"
    - "∫ fₙ dμ → ∫ f dμ, with no additional conditions needed beyond monotone pointwise convergence"
    - "∫ fₙ dμ → ∫ f dμ, but only if each fₙ is bounded"
    - "∫ fₙ dμ → ∫ f dμ, provided f is Riemann integrable"
  answer: 1
  explanation: "The Monotone Convergence Theorem requires only that the fₙ are non-negative measurable functions increasing pointwise to f — no uniformity, no boundedness, no Riemann integrability. This is far weaker than what Riemann theory requires (uniform convergence). Uniform convergence is sufficient but far too strong; the MCT shows you need far less. This is the theorem's power: it licenses interchange of limit and integral under the minimal conditions that make the conclusion well-posed."

- question: "Why does partitioning the range rather than the domain allow the Lebesgue integral to handle functions that the Riemann integral cannot?"
  type: short-answer
  answer: "By partitioning the range, you group x-values by their f-output rather than by their position on the x-axis. The measure of each preimage set replaces interval width. This means irregular functions — ones that spike wildly on complicated sets — are handled as long as their preimage sets are measurable. The Dirichlet function's preimage of {1} is the rationals (measure zero), so it contributes nothing to the integral. The Riemann approach fails because every small x-interval contains both 0s and 1s, so no Riemann sum can resolve the function's behavior."
  explanation: "The range-partition strategy decouples the integral from the geometric regularity of the function's graph. Riemann integration implicitly assumes the function is 'nice enough' that its graph can be approximated by rectangles. Lebesgue integration doesn't need this: it only needs the preimage sets to be measurable, a much weaker condition. This is why the Lebesgue integral extends to a vastly larger class of functions and becomes the foundation for modern probability, functional analysis, and Fourier theory."
```

## Explainer

Recall how the Riemann integral works: partition the *domain* into small intervals, pick a sample point in each, multiply height by width, and sum. This works beautifully for continuous functions, but fails for anything too irregular. The classic example is the Dirichlet function — 1 on rationals, 0 on irrationals. The Riemann integral cannot handle it because every interval contains both rationals and irrationals, so the upper and lower sums never agree. From your study of Lebesgue measure, you know that the rationals have measure zero. The Lebesgue perspective says: the Dirichlet function should integrate to 0, because it equals 0 "almost everywhere." The entire machinery of Lebesgue integration is built to make this intuition rigorous.

The key reversal is **partitioning the range instead of the domain**. Rather than asking "what is f(x) on this small interval of x-values?", ask "for which set of x-values does f(x) lie in this small interval [a, b] of output values?" The measure of that preimage set plays the role that interval width plays in Riemann integration. For a **simple function** — one that takes only finitely many values — this is straightforward: ∫ φ dμ = Σ cᵢ · μ(Eᵢ), where Eᵢ is the set where φ = cᵢ. The Lebesgue integral of a general non-negative measurable function is then defined as the supremum over all simple functions bounded below by f. This construction inherits all the pleasant properties of measure: it handles countably many exceptional points without issue, it works on abstract measure spaces, and it interacts cleanly with the σ-algebra structure.

The real payoff is the convergence theorems. The Riemann framework gives you results like "if fₙ → f uniformly, then ∫ fₙ → ∫ f" — uniform convergence is a very strong condition. Lebesgue gives you far more powerful theorems. The **Monotone Convergence Theorem** says: if fₙ is a sequence of non-negative measurable functions increasing pointwise to f, then ∫ fₙ dμ → ∫ f dμ. No uniformity required. The **Dominated Convergence Theorem** is the most frequently used tool in analysis: if fₙ → f pointwise (or almost everywhere) and |fₙ(x)| ≤ g(x) for some integrable function g, then ∫ fₙ dμ → ∫ f dμ. The dominating function g serves as a "ceiling" that prevents the fₙ from escaping to infinity in any direction, justifying the interchange. These theorems are what make modern probability theory, functional analysis, and Fourier analysis work — they let you pass limits through integrals in situations where Riemann integration would be silent or wrong.
