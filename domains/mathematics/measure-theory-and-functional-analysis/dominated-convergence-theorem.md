---
id: dominated-convergence-theorem
title: Dominated Convergence Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-general-definition
  type: hard
- id: fatou-lemma
  type: hard
- id: null-sets-almost-everywhere
  type: hard
builds-toward:
- lp-space-completeness-riesz-fischer
tags:
- convergence-theorems
stage: expert
status: validated
---

# Dominated Convergence Theorem

## Core Idea
If fₙ → f pointwise a.e. and |fₙ| ≤ g with ∫g < ∞, then ∫fₙ → ∫f. This is the most powerful convergence theorem, requiring only pointwise a.e. convergence and an integrable dominating function.

## How It's Best Learned
Apply to sequences shrinking to zero outside growing intervals, or bounded sequences on finite-measure sets.

## Common Misconceptions
The dominating function must be integrable; |fₙ| ≤ g pointwise is insufficient if ∫g = ∞. Without a dominating function, DCT does not apply.

## Questions

```yaml
- question: "Consider the sequence fₙ = 1_{[n, n+1]} (the indicator function of the interval [n, n+1] on ℝ). This sequence converges pointwise to 0 everywhere, yet ∫fₙ dμ = 1 for all n. Why does the Dominated Convergence Theorem fail to apply here?"
  type: multiple-choice
  options:
    - "The sequence does not converge pointwise — it only converges in measure"
    - "There is no integrable dominating function on ℝ for this sequence; the natural candidate g = 1 has infinite Lebesgue integral"
    - "The functions fₙ are not measurable because they change domain with each n"
    - "DCT requires uniform convergence, and this sequence only converges pointwise"
  answer: 1
  explanation: "The DCT requires both pointwise a.e. convergence and an integrable dominating function g with |fₙ| ≤ g a.e. Both conditions are load-bearing. For this sequence, pointwise convergence holds (each fₙ(x) = 0 eventually for any fixed x, since x ∉ [n, n+1] for large n). But the natural dominating function would be g = 1, and ∫ℝ 1 dμ = ∞ — g is not integrable on ℝ. There is no integrable dominator: the mass escapes to infinity rather than being controlled. This is precisely the intuition DCT formalizes — an integrable dominator prevents the sequence's integral from drifting away even while individual values go to zero."

- question: "You want to justify differentiating under the integral sign: d/dt ∫₀¹ f(x,t) dx = ∫₀¹ ∂f/∂t(x,t) dx. Which condition, when satisfied, allows you to apply DCT to justify this exchange?"
  type: multiple-choice
  options:
    - "f(x,t) is continuous in t for each fixed x ∈ [0,1]"
    - "The partial derivative ∂f/∂t exists everywhere and is bounded on [0,1] × [a,b]"
    - "There exists an integrable function g(x) on [0,1] such that |∂f/∂t(x,t)| ≤ g(x) for all t in the relevant range"
    - "f(x,t) is a uniformly convergent sequence of simple functions in t"
  answer: 2
  explanation: "Differentiating under the integral sign is justified by applying DCT to the difference quotients (f(x, t+h) - f(x, t))/h as h → 0. For DCT to apply, these difference quotients must be dominated by an integrable function. By the mean value theorem, |(f(x, t+h) - f(x,t))/h| ≤ sup |∂f/∂t(x,τ)|. If there is an integrable g(x) with |∂f/∂t(x,t)| ≤ g(x) for all relevant t, then DCT applies and the limit (the derivative) can pass through the integral. Mere continuity (option A) or pointwise boundedness without integrability (option B) is insufficient — the dominator must be integrable."

- question: "If fₙ is a sequence of measurable functions on a set E of finite measure, and |fₙ(x)| ≤ M for all x and all n (a bounded sequence), then g(x) = M · 1_E(x) is an integrable dominating function, making the DCT applicable whenever fₙ converges pointwise a.e."
  type: true-false
  answer: true
  explanation: "On a finite-measure set with a uniformly bounded sequence, finding an integrable dominator is automatic: g = M · 1_E satisfies |fₙ| ≤ g pointwise and ∫g dμ = M · μ(E) < ∞ because μ(E) is finite. This is why DCT is 'almost automatic' for bounded sequences on finite-measure domains — the two hardest parts (finding g and verifying its integrability) reduce to a trivial observation. The real analytical challenge arises on infinite-measure domains or for unbounded sequences, where finding a creative integrable dominator is the non-trivial work."

- question: "Pointwise convergence almost everywhere of a sequence of integrable functions is sufficient to justify exchanging the limit with the Lebesgue integral: lim ∫fₙ = ∫ lim fₙ."
  type: true-false
  answer: false
  explanation: "Pointwise convergence alone is not sufficient — this is exactly what the sequence fₙ = n · 1_{(0, 1/n)} demonstrates. Each fₙ integrates to 1 (the integral of n over an interval of length 1/n is 1), yet fₙ(x) → 0 pointwise almost everywhere (for any fixed x > 0, fₙ(x) = 0 eventually). The limit of integrals is 1 but the integral of the limit is 0. The DCT requires the additional condition of an integrable dominating function to prevent this kind of 'mass concentration' — where functions spike near a point with growing height and shrinking support, carrying finite area while converging to zero pointwise."

- question: "What role does the dominating function g play in the DCT, and why must g be integrable (∫g < ∞) rather than merely finite pointwise (g(x) < ∞ for a.e. x)?"
  type: short-answer
  answer: "The dominating function g acts as a uniform leash on the entire sequence: |fₙ(x)| ≤ g(x) for all n means no function in the sequence can put more mass anywhere than g does. Integrability (∫g < ∞) is what prevents mass from escaping to infinity in the limit — it ensures that the total 'budget' of mass the sequence can deploy is finite. If g is merely finite pointwise but has infinite integral, the sequence can redistribute mass without limit even while converging pointwise. The example fₙ = 1_{[n,n+1]} shows this: each function is bounded by 1 everywhere (pointwise finite), but the mass keeps moving to infinity, so ∫fₙ = 1 while ∫(lim fₙ) = 0. The integrability of g is the condition that prevents this escape."
  explanation: "The intuition is that ∫g < ∞ constrains not just the height of the functions but the total weight they can carry. Fatou's lemma (a weaker result requiring no dominator) gives only lim inf ∫fₙ ≥ ∫(lim inf fₙ) — an inequality, not equality. The dominator is what converts the inequality into equality, by blocking the mass from escaping to sets where the limit function is small."
```

## Explainer

From your study of the Lebesgue integral, you know that Lebesgue integration is more powerful than Riemann integration partly because it handles limits better. The central question in analysis is: when can you swap a limit with an integral? That is, when does ∫ lim fₙ = lim ∫ fₙ? Without restrictions, this swap can fail catastrophically. Consider the sequence fₙ = n · 1_{(0, 1/n)}: each function integrates to 1, yet fₙ → 0 pointwise almost everywhere. The limit of integrals is 1, but the integral of the limit is 0. The **Dominated Convergence Theorem (DCT)** gives precise conditions under which the swap is safe.

The theorem states: if a sequence fₙ converges **pointwise almost everywhere** to a function f, and if there exists an integrable function g — called a **dominating function** — such that |fₙ(x)| ≤ g(x) for almost every x and every n, then f is integrable and ∫fₙ → ∫f. The role of g is to act as a uniform leash on the entire sequence. No matter how wildly fₙ might oscillate or concentrate at individual points, as long as the whole sequence stays uniformly below g — and g itself has finite integral — the integral can't "escape to infinity" in the limit. The Lebesgue measure's ability to control mass on sets of small measure is what makes this work.

To understand why the integrability of g is non-negotiable: if g has infinite integral, the sequence could redistribute mass without limit even while converging pointwise. The example fₙ = 1_{[n, n+1]} converges pointwise to 0, so ∫f = 0, but ∫fₙ = 1 for all n. The natural dominating candidate g = 1 fails here only because ∫ℝ 1 = ∞; there is no integrable dominating function on ℝ for this sequence. The lesson is that both conditions — pointwise convergence and a genuine (finite-integral) dominator — are load-bearing.

In practice, the DCT is the workhorse of Lebesgue integration. When you need to differentiate under an integral sign, compute Fourier transforms, or pass a parameter through an integral, you typically exhibit a dominating function and invoke DCT to justify the exchange. For functions on a **finite-measure set** with a **bounded** sequence, the dominating function is just the bound times the characteristic function of the set — a convenient package that makes DCT almost automatic. The harder applications require finding a creative dominator, which is where the analytical depth of the theorem lives.
