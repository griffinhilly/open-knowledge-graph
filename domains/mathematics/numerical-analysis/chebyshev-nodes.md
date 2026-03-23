---
id: chebyshev-nodes
title: Chebyshev Nodes and Optimal Interpolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: runges-phenomenon
  type: hard
builds-toward:
- cubic-spline-interpolation
tags:
- chebyshev
- optimal-nodes
- interpolation
stage: formal-systems
status: validated
---

# Chebyshev Nodes and Optimal Interpolation

## Core Idea
Chebyshev nodes, the roots of the Chebyshev polynomial T_n(x) = cos(n·arccos(x)), minimize max|∏(x - x_i)| and are clustered near the interval endpoints [-1,1]. Using Chebyshev nodes for interpolation prevents Runge oscillations and ensures convergence for smooth functions. This choice is optimal among all node sets in the minimax sense.

## Questions

```yaml
- question: "You interpolate f(x) = 1/(1 + 25x²) on [-1,1] using a degree-10 polynomial. With equally-spaced nodes, the interpolant oscillates wildly near the endpoints. After switching to Chebyshev nodes, the oscillation disappears. What feature of Chebyshev nodes explains this?"
  type: multiple-choice
  options:
    - "Chebyshev nodes avoid the interval endpoints entirely, where error is largest"
    - "Chebyshev nodes cluster near the endpoints, reducing |ω(x)| precisely where it would otherwise blow up"
    - "Chebyshev nodes are more evenly spaced than equally-spaced nodes, distributing error uniformly"
    - "Chebyshev nodes use a higher-degree polynomial near the endpoints to compensate for curvature"
  answer: 1
  explanation: "The interpolation error bound involves |ω(x)| = |(x−x_0)(x−x_1)···(x−x_n)|. With equally-spaced nodes, this product becomes very large near x = ±1, causing Runge oscillation. Chebyshev nodes are deliberately *denser* near the endpoints — they cluster where the error would otherwise explode. This is counterintuitive: the fix is not more uniform spacing but strategic non-uniform spacing that places nodes close to the danger zones. The nodes are not 'more uniform' — they are non-uniform in exactly the right way."

- question: "What is the mathematical reason Chebyshev nodes are optimal for polynomial interpolation on [-1, 1]?"
  type: multiple-choice
  options:
    - "They minimize the degree of the interpolating polynomial needed for a given accuracy"
    - "They are the roots of T_{n+1}(x), which is the monic degree-(n+1) polynomial with smallest possible maximum on [-1,1]"
    - "They minimize the average error ∫|f(x) − p(x)|dx rather than the maximum error"
    - "They are equidistant in the Chebyshev metric, corresponding to the L² norm on [-1,1]"
  answer: 1
  explanation: "The node error product ω(x) is monic of degree n+1 (leading coefficient 1, since each root contributes one factor). The Chebyshev polynomial T_{n+1}(x)/2^n is the unique monic polynomial of degree n+1 with the smallest possible maximum on [-1,1] — the minimax property. Choosing the roots of T_{n+1} as the interpolation nodes makes ω(x) equal to this minimax polynomial, achieving the tightest possible error bound. No other choice of n+1 nodes can do better in the minimax sense."

- question: "Chebyshev nodes are optimal because they distribute interpolation nodes uniformly across the interval, ensuring equal spacing between adjacent nodes."
  type: true-false
  answer: false
  explanation: "The opposite is true. Chebyshev nodes are *non-uniformly* spaced: denser near the endpoints and sparser near the center. This deliberate non-uniformity is what makes them optimal. Uniform spacing is the source of Runge's phenomenon, not the solution to it. Chebyshev nodes are geometrically the projections of equally-spaced points on the upper semicircle onto the x-axis — a construction that naturally produces endpoint clustering."

- question: "For smooth functions, using Chebyshev nodes guarantees that the interpolating polynomial converges to the function as the number of nodes increases, whereas equally-spaced nodes cannot provide this guarantee."
  type: true-false
  answer: true
  explanation: "Convergence with equally-spaced nodes is not guaranteed even for smooth functions — Runge's example (1/(1+25x²)) is smooth but the equally-spaced interpolant diverges near the endpoints. Chebyshev nodes make max|ω(x)| = 1/2^n (where n+1 is the node count), which decreases fast enough to overcome the growth of higher derivatives for smooth functions, guaranteeing convergence. This is a major practical advantage: you can add more Chebyshev nodes and be confident the approximation improves."

- question: "Why is minimizing max|ω(x)| = max|(x−x_0)(x−x_1)···(x−x_n)| the key problem in choosing interpolation nodes, and what makes this quantity controllable?"
  type: short-answer
  answer: "The interpolation error satisfies |f(x) − p(x)| ≤ (max|f^(n+1)|/(n+1)!) · |ω(x)|. The first factor depends only on the function being interpolated and cannot be controlled by node placement. The second factor — max|ω(x)| — depends entirely on where the nodes are placed. Minimizing max|ω(x)| is therefore the only part of the error bound we can optimize. Since ω(x) must be monic of degree n+1 (its roots are exactly the nodes), choosing the roots of the minimax monic polynomial T_{n+1}(x)/2^n achieves the smallest possible value of max|ω(x)|."
  explanation: "This is why Chebyshev node optimality is not a heuristic improvement but a mathematically provable best strategy. The Chebyshev polynomial T_{n+1}(x)/2^n achieves maximum value 1/2^n on [-1,1], the smallest possible for any monic degree-(n+1) polynomial. Since ω(x) must be monic, choosing its roots to be the Chebyshev nodes makes ω(x) equal to this minimax polynomial. The result is the tightest possible interpolation error bound across the entire interval."
```

## Explainer

Runge's phenomenon revealed that equally-spaced interpolation nodes cause polynomial interpolants to wildly oscillate near the endpoints of the interval, even for smooth functions like 1/(1 + 25x²). The source of the problem is the **node error product** ω(x) = (x - x_0)(x - x_1)···(x - x_n): the interpolation error at any point x is bounded by a term involving |ω(x)|, and with equally-spaced nodes, this product becomes very large near x = ±1. To fix the problem, you need to choose nodes that make max|ω(x)| as small as possible.

The answer comes from an unexpected direction: trigonometry. The **Chebyshev nodes** on [-1, 1] are x_k = cos((2k+1)π / (2n+2)) for k = 0, 1, ..., n. These are the projections onto the x-axis of equally-spaced points on the upper semicircle. Near the center x = 0, the points are spread apart; near the endpoints x = ±1, they cluster together. This crowding near the endpoints is precisely what counteracts the natural tendency of the error to blow up there.

The optimality of Chebyshev nodes is not accidental — it follows from a deep minimax property. The **Chebyshev polynomial** T_n(x) = cos(n arccos(x)) is the unique monic polynomial of degree n whose maximum absolute value on [-1, 1] is minimized. Its maximum value is 1/2^{n-1}, and no other monic polynomial of degree n can stay flatter on [-1, 1]. Since the node error product ω(x) is exactly a monic degree-(n+1) polynomial, choosing the roots of T_{n+1}(x) as your nodes makes ω(x) = T_{n+1}(x)/2^n, which achieves the minimum possible maximum.

In practice, transforming any interval [a, b] to [-1, 1] via x = (a + b)/2 + (b - a)/2 · t lets you always use Chebyshev nodes. For smooth functions, using Chebyshev nodes not only prevents the Runge explosion but guarantees that the interpolating polynomial converges to the function as n → ∞ — a guarantee that equally-spaced interpolation cannot provide. This makes Chebyshev nodes the default choice whenever you are doing polynomial interpolation and care about accuracy across the whole interval.
