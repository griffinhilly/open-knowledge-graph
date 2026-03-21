---
id: weierstrass-m-test
title: Weierstrass M-Test
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence-functions
  type: hard
- id: series-convergence-rigorous
  type: hard
builds-toward:
- uniform-convergence-power-series
tags:
- weierstrass-m-test
- uniform-convergence
- series
stage: advanced
status: draft
---

# Weierstrass M-Test

## Core Idea
If |fₙ(x)| ≤ Mₙ for all x in a set S and all n, and if ∑Mₙ converges, then ∑fₙ(x) converges uniformly on S. This is the workhorse for proving uniform convergence of series without explicit calculation. It applies to power series, Fourier series, and integral representations.

## Questions

```yaml
- question: "The series ∑_{n=1}^∞ sin(nx)/n² is being analyzed for uniform convergence on all of ℝ. Which of the following correctly applies the Weierstrass M-test?"
  type: multiple-choice
  options:
    - "Since |sin(nx)/n²| ≤ 1/n² for all x ∈ ℝ and ∑1/n² = π²/6 converges, the M-test gives uniform convergence on ℝ"
    - "Since sin(nx)/n² → 0 pointwise for each x, uniform convergence follows automatically"
    - "The series converges uniformly because the partial sums are uniformly bounded"
    - "The M-test cannot be applied because sin(nx) oscillates and has no fixed bound"
  answer: 0
  explanation: "The M-test requires finding constants Mₙ ≥ |fₙ(x)| for all x simultaneously. Here Mₙ = 1/n² works because |sin(nx)| ≤ 1 for all x, so |sin(nx)/n²| ≤ 1/n² regardless of x. Since ∑1/n² converges, the M-test applies. Option B is wrong because pointwise convergence (each x independently) does not imply uniform convergence — uniform convergence requires the same N to work for all x at once. Option D misunderstands the test: sin(nx) is bounded, and that bound is all we need."

- question: "A student concludes: 'The series ∑fₙ(x) fails the Weierstrass M-test on [0,1] because no constants Mₙ with ∑Mₙ convergent can bound all |fₙ(x)|. Therefore the series does not converge uniformly on [0,1].' This reasoning is:"
  type: multiple-choice
  options:
    - "Correct: the M-test is both necessary and sufficient for uniform convergence"
    - "Incorrect: the M-test is sufficient but not necessary — failing it does not rule out uniform convergence by other methods"
    - "Correct only when the functions fₙ are continuous on [0,1]"
    - "Incorrect because the M-test always applies to series on closed bounded intervals"
  answer: 1
  explanation: "The Weierstrass M-test is a sufficient condition, not a necessary one. A series can converge uniformly on a set even when no valid sequence of dominating constants Mₙ exists with ∑Mₙ < ∞. The alternating series ∑(-1)ⁿ/n converges uniformly on certain sets despite failing the M-test. When the M-test fails, other tools — Dirichlet's test, Abel's test — may still establish uniform convergence. Failing the M-test only means this particular tool cannot help; it is not a proof of non-uniform convergence."

- question: "The Weierstrass M-test establishes uniform convergence by finding x-independent constants Mₙ ≥ |fₙ(x)| for all x, and the critical feature is that these constants are independent of x — making the same bound hold everywhere simultaneously."
  type: true-false
  answer: true
  explanation: "The x-independence of the constants Mₙ is exactly what converts the argument from pointwise to uniform. When ∑Mₙ < ∞, the tail ∑_{n>N} Mₙ can be made smaller than any ε by choosing N large enough — and because Mₙ ≥ |fₙ(x)| for *every* x, the same N makes the tail of the function series smaller than ε everywhere simultaneously. This is the definition of uniform convergence: a single N that works across all x, rather than an N that may depend on the specific x chosen."

- question: "If a series of functions ∑fₙ(x) converges pointwise on a set S, the Weierstrass M-test can be applied to conclude it also converges uniformly."
  type: true-false
  answer: false
  explanation: "Pointwise convergence and uniform convergence are genuinely different, and the M-test is not a bridge between them. Pointwise convergence means: for each fixed x, the partial sums eventually stay within ε of the limit — but the required N may depend on x. Uniform convergence requires a single N that works for all x. The M-test establishes uniform convergence directly (without going through pointwise convergence); it cannot be applied to series merely because they converge pointwise. The classic counterexample ∑_{n} fₙ(x) = x^n on [0,1] converges pointwise but not uniformly."

- question: "Why is pointwise convergence insufficient for swapping limits with integration or differentiation, and how does the Weierstrass M-test restore these properties?"
  type: short-answer
  answer: "Pointwise convergence allows the rate of convergence to vary arbitrarily across x — some points may require many more terms than others. When you integrate or differentiate, this x-dependent variation can accumulate or interact in ways that break the limit-integral interchange. Uniform convergence, by contrast, means the worst-case error over all x goes to zero, so the limit function is approached at a uniform rate. Under uniform convergence, ∫∑fₙ = ∑∫fₙ and (under additional conditions) d/dx ∑fₙ = ∑ d/dx fₙ. The M-test establishes uniform convergence by bounding each |fₙ(x)| by an x-independent Mₙ with ∑Mₙ < ∞, ensuring the tail of the series is uniformly small."
  explanation: "The practical payoff of the M-test is precisely these interchange theorems. Once you know ∑fₙ converges uniformly on S, you can integrate term by term, differentiate term by term (under mild additional conditions), and conclude the limit function is continuous if all fₙ are continuous. These conclusions fail for merely pointwise convergent series, where the limit function can be discontinuous even when all fₙ are continuous. The M-test is the most commonly invoked tool to access these powerful consequences."
```

## Explainer

From your study of uniform convergence, you know that a series of functions ∑fₙ(x) converges uniformly if the partial sums can be made uniformly close to the limit — meaning the worst-case error over all x in S can be driven to zero by taking enough terms. The trouble with checking this directly is that you need to control a supremum over an infinite set. The **Weierstrass M-test** sidesteps this by replacing the x-dependent functions with x-independent constants: if you can bound each |fₙ(x)| above by a number Mₙ that does not depend on x, and if the series ∑Mₙ of constants converges, then you have uniform convergence for free.

The proof uses comparison with the tail of ∑Mₙ. For any ε > 0, the convergence of ∑Mₙ guarantees that the tail ∑_{n=N+1}^∞ Mₙ < ε for large enough N. But then the tail of the function series satisfies |∑_{n=N+1}^∞ fₙ(x)| ≤ ∑_{n=N+1}^∞ |fₙ(x)| ≤ ∑_{n=N+1}^∞ Mₙ < ε for *every* x in S simultaneously. That uniform bound is exactly what uniform convergence requires — the same N works everywhere, not just pointwise. This is why the test is so useful: you delegate the convergence question to a numerical series, where you already have many tools.

A standard application is the power series ∑xⁿ/n². On the closed interval [−1, 1], you have |xⁿ/n²| ≤ 1/n², and ∑1/n² = π²/6 converges. So the M-test immediately gives uniform convergence on [−1, 1]. You did not have to track how the partial sums behave as x varies — the constants did all the work. Once uniform convergence is established, you can swap limits with integration or pass differentiation through the sum, conclusions that would not be valid from mere pointwise convergence alone.

The test is sufficient but not necessary: a series can converge uniformly even when no suitable sequence of constants Mₙ exists with ∑Mₙ convergent. When the M-test fails, uniform convergence may still hold by more delicate arguments (Dirichlet's test, Abel's test). But in practice — especially for power series inside the radius of convergence, and for Fourier series with summable coefficient sequences — the M-test is almost always the first tool to reach for. Its elegance lies in translating a functional analysis problem (uniform convergence of functions) into a classical analysis problem (convergence of a numerical series) where comparison, ratio, and integral tests all apply.


