---
id: stochastic-integration-semimartingales
title: Stochastic Integration for Semimartingales
domain: mathematics
course: stochastic-processes
prerequisites:
- id: ito-integral
  type: hard
- id: itos-formula
  type: hard
- id: martingale-representation-theorem
  type: hard
- id: levy-processes
  type: soft
- id: lp-spaces
  type: soft
tags:
- semimartingale
- stochastic-integration
- bdg-inequality
- quadratic-variation
- general-ito-formula
stage: expert
status: validated
---

# Stochastic Integration for Semimartingales

## Core Idea
A semimartingale is a càdlàg adapted process X that decomposes as X = M + A, where M is a local martingale and A is an adapted process of finite variation. This is the most general class of "good integrators" — by the Bichteler-Dellacherie theorem, semimartingales are exactly the processes for which a reasonable stochastic integral ∫H dX can be defined. The Itô integral extends from Brownian motion to this full generality: the stochastic integral ∫₀ᵗ H(s) dX(s) is well-defined for predictable H, and the Burkholder-Davis-Gundy (BDG) inequality E[sup_{s≤t} |∫₀ˢ H dM|^p] ≤ C_p E[[∫H dM, ∫H dM]_t^{p/2}] controls the integral's moments through the quadratic variation.

## Questions

```yaml
- question: "Which of the following is the correct definition of a semimartingale?"
  type: multiple-choice
  options:
    - "A process with continuous paths and finite expectation"
    - "A process that can be decomposed as X = M + A where M is a local martingale and A is a predictable process of finite variation"
    - "Any process adapted to a filtration satisfying the usual conditions"
    - "A process with independent and stationary increments"
  answer: 1
  explanation: "A semimartingale decomposes as a local martingale plus a predictable finite-variation process. This decomposition (the canonical decomposition for special semimartingales) separates the 'noise' (local martingale M) from the 'signal' (finite variation A). The class includes Brownian motion (M = W, A = 0), Poisson processes (M = N - λt, A = λt), Lévy processes, solutions to SDEs, and much more. The Bichteler-Dellacherie theorem proves that this class is exactly the set of processes for which stochastic integration is possible — no extension beyond semimartingales can produce a reasonable integral."

- question: "The Burkholder-Davis-Gundy inequality states that for a continuous local martingale M, the maximal process sup_{s≤t}|M(s)| and the square root of the quadratic variation [M,M]_t^{1/2} have equivalent L^p norms for 1 ≤ p < ∞."
  type: true-false
  answer: true
  explanation: "The BDG inequality provides universal constants c_p and C_p such that c_p E[[M,M]_t^{p/2}] ≤ E[sup_{s≤t}|M(s)|^p] ≤ C_p E[[M,M]_t^{p/2}] for all continuous local martingales M. This two-sided bound says that the 'size' of a martingale (measured by its maximum) is controlled by its quadratic variation and vice versa. For p = 2, the upper bound generalizes the Itô isometry E[M(t)²] = E[[M,M]_t] to a maximal inequality. The BDG inequality is the principal tool for proving L^p estimates on stochastic integrals — it reduces moment bounds on path suprema to bounds on quadratic variation, which is often computable."

- question: "Explain why fractional Brownian motion with Hurst parameter H ≠ 1/2 is NOT a semimartingale, and what this implies about stochastic integration."
  type: short-answer
  answer: "Fractional Brownian motion (fBM) with H ≠ 1/2 has dependent increments — positively correlated for H > 1/2, negatively correlated for H < 1/2. A semimartingale must be decomposable as a local martingale plus a finite variation process. For H > 1/2, fBM paths are too smooth (Hölder continuous with exponent > 1/2) to be a martingale, and the 'drift' needed to compensate would have infinite variation. For H < 1/2, the paths are too rough. The Bichteler-Dellacherie theorem then implies that the standard stochastic integral ∫H dB^H is undefined — alternative integration theories (rough paths, Wick-Itô-Skorokhod) are needed."
  explanation: "This is a fundamental limitation result. The Bichteler-Dellacherie theorem says semimartingales are the LARGEST class of good integrators. Since fBM is not a semimartingale for H ≠ 1/2, one cannot define a pathwise stochastic integral using the standard theory. The rough paths theory of Lyons (1998) provides an alternative that extends stochastic calculus to processes with Hölder regularity > 1/3, covering fBM with H > 1/3. For H ≤ 1/3, even rough path theory requires additional structure."

- question: "For a general semimartingale X = M + A (with M a local martingale and A finite variation), the quadratic variation [X,X]_t equals:"
  type: multiple-choice
  options:
    - "[M,M]_t, since the finite variation part contributes nothing to quadratic variation"
    - "[M,M]_t + 2[M,A]_t + [A,A]_t, the full bilinear expansion"
    - "[M,M]_t + [A,A]_t, since [M,A]_t = 0 by orthogonality"
    - "∫₀ᵗ |dX(s)|², the pathwise squared total variation"
  answer: 1
  explanation: "The quadratic variation is bilinear: [X,X] = [M+A, M+A] = [M,M] + 2[M,A] + [A,A]. All three terms can be non-zero in general. However, if A is continuous and of finite variation, then [A,A]_t = 0 (continuous finite-variation processes have zero quadratic variation) and [M,A]_t = 0 (the cross-variation of a local martingale with a continuous finite-variation process vanishes). In this special case, [X,X]_t = [M,M]_t. But if A has jumps, [A,A]_t = Σ_{s≤t}(ΔA_s)² ≠ 0, and the full expansion applies."

- question: "The Itô formula for a general semimartingale X and a C² function f states: f(X_t) = f(X_0) + ∫₀ᵗ f'(X_{s-}) dX_s + ½∫₀ᵗ f''(X_{s-}) d[X,X]_s^c + Σ_{0<s≤t}[f(X_s) - f(X_{s-}) - f'(X_{s-})ΔX_s]. What does the sum over jumps accomplish?"
  type: short-answer
  answer: "The jump sum corrects for the fact that the continuous Itô formula (with only the ½f''d[X]^c term) is inaccurate at jump times. At a jump of size ΔX_s, the actual change in f is f(X_s) - f(X_{s-}), but the stochastic integral term contributes f'(X_{s-})ΔX_s (a linear approximation). The difference f(X_s) - f(X_{s-}) - f'(X_{s-})ΔX_s is the nonlinear correction — the 'second-order' effect of the jump that f' misses. For continuous semimartingales (no jumps), this sum vanishes and the formula reduces to the classical Itô formula. For pure jump processes, the continuous quadratic variation [X]^c vanishes and the sum captures all the nonlinearity."
  explanation: "The general Itô formula has three correction terms beyond the 'naive' chain rule ∫f'dX: the continuous quadratic variation term ½∫f''d[X]^c (the usual Itô correction), and the jump correction sum. Together they account for all second-order effects — continuous fluctuations via [X]^c and discontinuous jumps via the sum. This formula unifies Itô calculus for diffusions and the change-of-variable formula for jump processes into a single framework."
```

## Explainer

The **semimartingale** is the central object of modern stochastic calculus. A càdlàg adapted process X is a semimartingale if it admits a decomposition X = X_0 + M + A, where M is a local martingale (the "noise") and A is a predictable process of locally finite variation (the "drift"). This class is remarkably broad: it includes Brownian motion, Poisson processes, Lévy processes, diffusions, solutions to SDEs driven by any combination of continuous and jump noise, and much more. The **Bichteler-Dellacherie theorem** (1979) establishes that semimartingales are not merely a convenient class but the *largest* class of processes for which a reasonable stochastic integral can be defined — any attempt to extend integration beyond semimartingales violates either linearity or a minimal continuity requirement.

The construction of the stochastic integral ∫₀ᵗ H_s dX_s for a semimartingale X proceeds in two pieces corresponding to the decomposition X = M + A. The integral against A is a pathwise Lebesgue-Stieltjes integral (since A has finite variation), well-defined for any adapted H with ∫|H_s||dA_s| < ∞. The integral against M extends the Itô integral: first define it for simple predictable processes, then extend by an L² isometry (using the quadratic variation [M,M] as the "squared norm" of M), and finally localize to handle local martingales. The **Itô isometry** E[(∫₀ᵗ H dM)²] = E[∫₀ᵗ H² d[M,M]_s] generalizes from Brownian motion to any L²-martingale M, with the quadratic variation [M,M] playing the role that t plays for W.

The **Burkholder-Davis-Gundy (BDG) inequality** is the main analytic tool for controlling stochastic integrals. For a local martingale M and any p ≥ 1, it states c_p E[[M,M]_T^{p/2}] ≤ E[sup_{t ≤ T} |M_t|^p] ≤ C_p E[[M,M]_T^{p/2}], where c_p, C_p are universal constants depending only on p. This two-sided equivalence means that the "size" of a martingale (its maximal process) and the "size" of its randomness (the quadratic variation) are always comparable. For p = 2, the upper bound is the Doob maximal inequality upgraded with the quadratic variation. The BDG inequality is indispensable for proving existence and uniqueness of SDE solutions, for establishing convergence of numerical schemes, and for any argument that requires moment bounds on stochastic integrals.

The **Itô formula for semimartingales** unifies and extends the classical Itô formula to processes with jumps. For X a semimartingale and f ∈ C², it reads: f(X_t) = f(X_0) + ∫₀ᵗ f'(X_{s-}) dX_s + ½∫₀ᵗ f''(X_{s-}) d[X,X]_s^c + Σ_{0 < s ≤ t}[f(X_s) - f(X_{s-}) - f'(X_{s-})ΔX_s]. The three correction terms beyond the naive chain rule capture: (1) the stochastic integral (first-order), (2) the continuous quadratic variation correction (the familiar ½f''dt term for diffusions), and (3) a jump correction that accounts for the nonlinearity of f applied to finite-sized jumps. When X is continuous, the jump sum vanishes and the formula reduces to the standard Itô formula. When X is a pure jump process, the [X]^c term vanishes and the formula becomes a telescoping sum of discrete changes. This unified formula is the computational engine for pricing derivatives under jump-diffusion models, for deriving the generators of Markov processes, and for establishing the connections between SDEs and PDEs (Feynman-Kac type results) in the general semimartingale setting.
