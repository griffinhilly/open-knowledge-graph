---
id: interpolation-error-analysis
title: Interpolation Error Analysis
domain: mathematics
course: numerical-analysis
prerequisites:
- id: newton-divided-differences
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- runges-phenomenon
- chebyshev-nodes
tags:
- error-analysis
- interpolation
- bounds
stage: advanced
status: validated
---

# Interpolation Error Analysis

## Core Idea
If P(x) interpolates f at n+1 points, the error E(x) = f(x) - P(x) satisfies |E(x)| ≤ (max |f^{(n+1)}|)/(n+1)! |∏(x - x_i)|. This bound reveals that error depends on the (n+1)-th derivative of f and the magnitude of the node product. For smooth functions with well-chosen nodes, interpolation error can be very small; poor node placement causes large errors.

## Questions

```yaml
- question: "You are interpolating f(x) = 1/(1 + 25x²) on [−1, 1] using a degree-20 polynomial with 21 equally spaced nodes. You add 10 more equally spaced nodes to get a degree-30 polynomial. What most likely happens to the interpolation error near the endpoints?"
  type: multiple-choice
  options:
    - "The error decreases uniformly because more nodes always improve accuracy"
    - "The error near the endpoints increases dramatically due to the large values of |ω(x)| there for equally spaced nodes"
    - "The error stays roughly the same because both polynomials have the same function f"
    - "The error decreases near the endpoints but increases near the center"
  answer: 1
  explanation: "This is Runge's phenomenon. For equally spaced nodes, |ω(x)| is very small near the interval center but grows enormously near the endpoints. As you add more equally spaced nodes, this endpoint amplification gets worse, and the interpolating polynomial oscillates wildly there. The interpolation actually deteriorates near x = ±1 even as you add nodes. This is why node placement — not just node count — determines interpolation quality."

- question: "In the interpolation error bound |E(x)| ≤ M/(n+1)! · |ω(x)|, which factor can a numerical analyst directly control by design choices?"
  type: multiple-choice
  options:
    - "M = max|f^{(n+1)}|, by choosing a smoother function f"
    - "|ω(x)| = |∏(x − xᵢ)|, by choosing where to place the interpolation nodes"
    - "Both M and |ω(x)| equally, since both depend on the polynomial degree"
    - "Neither factor — both are determined entirely by the function f"
  answer: 1
  explanation: "M = max|f^{(n+1)}| depends only on the function being interpolated — you cannot change it. But |ω(x)| depends entirely on where you place the interpolation nodes, which is a design choice. This is why error analysis is a design tool: Chebyshev nodes are chosen precisely to minimize max|ω(x)| over the interval, giving the smallest possible worst-case error from the controllable factor."

- question: "Replacing equally spaced nodes with Chebyshev nodes on [−1, 1] reduces the maximum value of |ω(x)| exponentially in n."
  type: true-false
  answer: true
  explanation: "For n+1 Chebyshev nodes, max|ω(x)| over [−1, 1] equals 1/2ⁿ — exponentially small in n. For equally spaced nodes, the maximum of |ω(x)| grows rapidly. Chebyshev nodes cluster near the endpoints, where |ω| would otherwise be large, effectively spreading the node polynomial's values more evenly across the interval."

- question: "Adding more interpolation nodes always reduces the interpolation error for any function."
  type: true-false
  answer: false
  explanation: "Runge's phenomenon shows this is false. For equally spaced nodes and certain functions (like Runge's function f(x) = 1/(1+25x²)), the interpolation error near the endpoints grows without bound as you add more nodes. The error depends on both M/(n+1)! (which decreases) and max|ω(x)| (which increases rapidly for equally spaced nodes). The product can diverge, making interpolation worse."

- question: "The interpolation error bound |E(x)| ≤ M/(n+1)! · |ω(x)| separates into two factors. What distinct insight does each factor provide, and why does that separation matter practically?"
  type: short-answer
  answer: "The factor M/(n+1)! measures the function's intrinsic complexity — how much its (n+1)-th derivative fluctuates — which is a property of f that the analyst cannot change. The factor |ω(x)| = |∏(x − xᵢ)| measures how the chosen node placement spreads the interpolation across the interval, which the analyst can control. The separation matters because it identifies what is within the analyst's power: by choosing Chebyshev nodes instead of equally spaced nodes, you minimize max|ω(x)|, dramatically reducing the worst-case error regardless of f's behavior."
  explanation: "This two-factor structure turns error analysis from a passive measurement into an active design tool. You cannot improve the bound by making f smoother, but you can choose nodes that keep |ω(x)| small everywhere — and the error bound tells you exactly how much improvement to expect."
```

## Explainer

From Taylor series, you know that approximating a function by a polynomial accumulates error controlled by higher derivatives. Specifically, the Taylor remainder after n terms involves f^(n+1) evaluated at some point between x and the expansion center. Interpolation error analysis tells a closely parallel story, but now the polynomial matches f at multiple points rather than matching all derivatives at one point. The structure of the error bound reflects this difference in a precise and instructive way.

When P(x) is the unique degree-n polynomial interpolating f at nodes x₀, x₁, …, xₙ, the error at a point x is exactly E(x) = f^(n+1)(ξ) / (n+1)! · ω(x), where ω(x) = (x − x₀)(x − x₁)···(x − xₙ) is the **node polynomial** and ξ is some point in the interval spanned by x and the nodes. The proof mirrors the Taylor remainder proof: define a helper function that vanishes at all n+2 points (the n+1 nodes plus x itself), then apply Rolle's theorem n+1 times to locate a point ξ where the (n+1)-th derivative of the helper equals zero. The final expression falls out cleanly.

The bound |E(x)| ≤ M/(n+1)! · |ω(x)| separates into two factors that tell distinct stories. The term M = max|f^(n+1)| measures how "curved" f is — how much its (n+1)-th derivative fluctuates. You cannot control this; it is a property of f itself. The term |ω(x)| = |∏(x − xᵢ)| measures how far the evaluation point x is from the interpolation nodes, and this you **can** control by choosing nodes wisely. At the nodes themselves, ω = 0 and the error vanishes exactly (as it must, since P interpolates f there). Between nodes and beyond them, |ω| can vary enormously depending on node placement.

The most striking consequence concerns **equally spaced nodes**. Your intuition might suggest that spacing nodes evenly across [a, b] is natural and good — after all, you're covering the interval uniformly. But |ω(x)| for equally spaced nodes is very small near the center of the interval and very large near the endpoints. For functions like f(x) = 1/(1 + 25x²) on [−1, 1] (Runge's function), this edge amplification is so severe that the interpolating polynomial with equally spaced nodes oscillates wildly near ±1 as n increases — the interpolation actually gets worse, not better, as you add more nodes. This is **Runge's phenomenon**.

The fix is **Chebyshev nodes**: xₖ = cos((2k+1)π/(2n+2)) for k = 0, …, n. These nodes cluster near the endpoints and spread out the node polynomial more evenly. The maximum of |ω(x)| over [−1, 1] for Chebyshev nodes is 1/2ⁿ — exponentially smaller than for equally spaced nodes. The lesson is that error analysis is not just about measuring error after the fact; it is a design tool that tells you where to put your nodes before you even begin the computation. Understanding the error formula is what separates a numerical analyst from someone who just applies a formula and hopes for the best.
