---
id: eulers-method-convergence
title: 'Euler''s Method: Error Analysis'
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eulers-method
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- runge-kutta-methods
tags:
- euler-method
- ode
- error-analysis
stage: formal-systems
status: draft
---

# Euler's Method: Error Analysis

## Core Idea
Euler's method y_{n+1} = y_n + hf(t_n, y_n) has local truncation error O(h²) at each step and global error O(h) over a fixed time interval. The method converges as h → 0 under standard Lipschitz conditions, but slowly—halving h halves the error. Understanding error behavior guides practical choices of step size and informs when faster methods are needed.

## Questions

```yaml
- question: "Euler's method makes a local truncation error of O(h²) per step. Over a fixed interval [0, T] with T/h total steps, what global error results, and why?"
  type: multiple-choice
  options:
    - "O(h²) — local errors cancel out across many steps, so the global error matches the local error"
    - "O(h) — multiplying O(h²) local errors by T/h steps gives O(h), and careful analysis confirms errors don't grow faster than this under the Lipschitz condition"
    - "O(1) — global error does not shrink as h decreases because floating-point errors dominate at scale"
    - "O(h³) — the method is secretly higher-order than the local truncation error suggests"
  answer: 1
  explanation: "The global error is O(h). Multiplying local error O(h²) by number of steps T/h gives O(h) — but this multiplication is not trivially justified, because each step starts from a slightly wrong position, propagating earlier errors forward. A careful analysis using the Lipschitz condition shows that error propagation is bounded (errors grow at most exponentially, not faster), so the total global error remains first-order: O(h). Halving h halves the error. This is what it means for Euler's method to be a first-order method."

- question: "A student uses Euler's method with h = 0.1 and gets a global error of 0.05 at the endpoint. She switches to h = 0.025 (one-quarter the step size). What global error should she expect?"
  type: multiple-choice
  options:
    - "Approximately 0.05 — smaller h doesn't help because the error is dominated by floating-point precision"
    - "Approximately 0.0125 — the global error is O(h), so quartering h quarters the error"
    - "Approximately 0.003125 — the global error is O(h²), so quartering h gives a 16× improvement"
    - "Approximately 0.025 — the global error is O(h^(1/2)), so quartering h halves the error"
  answer: 1
  explanation: "Euler's method has global error O(h), meaning error ≈ Ch for some constant C. With h = 0.1 giving error 0.05, we get C ≈ 0.5. With h = 0.025, error ≈ 0.5 × 0.025 = 0.0125 — a 4× improvement from a 4× reduction in h. This contrasts sharply with fourth-order Runge-Kutta, where a 4× reduction in h gives a 4⁴ = 256× improvement. The first-order convergence of Euler's method makes it expensive when high accuracy is needed."

- question: "The local truncation error of Euler's method is O(h²) per step, which is one order higher than the global error O(h), because Taylor series truncation after the h-term discards an h² term, while accumulation over T/h steps removes one power of h from the exponent."
  type: true-false
  answer: true
  explanation: "True. The Taylor expansion y(t_{n+1}) = y(t_n) + h·y'(t_n) + (h²/2)·y''(t_n) + ··· shows that Euler's update (keeping only the h term) makes an error of O(h²) in each individual step. Over [0,T], there are T/h steps, so the accumulated global error is O(h²) × (T/h) = O(h). The Lipschitz condition ensures errors don't grow faster than linear in the number of steps, confirming this first-order global behavior."

- question: "The Lipschitz condition on f(t, y) is needed for Euler's method to converge, because without it, nearby solution curves could diverge so rapidly that step-to-step errors amplify without bound as h → 0."
  type: true-false
  answer: true
  explanation: "True. The Lipschitz condition |f(t, y₁) − f(t, y₂)| ≤ L|y₁ − y₂| ensures that nearby solution trajectories cannot diverge faster than exponentially. In the convergence proof, L controls how much a step-n error grows by step n+1. Without this bound, errors could cascade — a small early error could grow super-exponentially, and no finite step size would produce a useful approximation. The Lipschitz constant L also gives practical guidance: large L (stiff problems) requires very small h to control error growth, making explicit Euler expensive."

- question: "Why does halving the step size h in Euler's method only halve the global error, rather than producing a much larger improvement?"
  type: short-answer
  answer: "Euler's method is first-order: its global error is O(h), meaning error ≈ Ch for some constant. Halving h halves Ch — a factor of 2 improvement. This is a consequence of the local truncation error being O(h²): the error per step shrinks quadratically with h, but the number of steps grows as 1/h, so the two effects partially cancel, leaving first-order global convergence. Compare this to fourth-order Runge-Kutta, where halving h gives a 2⁴ = 16× improvement, because its local error is O(h⁵) and global error is O(h⁴)."
  explanation: "The order of a method directly determines how efficiently accuracy improves with smaller h. A first-order method like Euler requires 10× more steps (10× more computation) to get 10× better accuracy. A fourth-order method needs only 10^(1/4) ≈ 1.78× more steps for the same improvement. For smooth problems requiring high accuracy, this difference makes first-order methods impractical and higher-order methods essential. Understanding error orders is the foundation for choosing numerical methods wisely."
```

## Explainer

Euler's method steps forward in time by replacing the exact solution curve with a straight-line tangent approximation: at each point (t_n, y_n), it travels along the tangent for a distance h. Your prerequisite, Taylor series, lets you quantify precisely how much is lost in each such step. Expand the exact solution y(t_{n+1}) around t_n: y(t_{n+1}) = y(t_n) + h·y'(t_n) + (h²/2)·y''(t_n) + ···. Since y'(t_n) = f(t_n, y(t_n)), the Euler update y_{n+1} = y_n + h·f keeps the first two terms and discards everything from h² onward. The **local truncation error** — the error made in one step, assuming the previous value is exact — is therefore proportional to h², typically written O(h²).

But errors accumulate over time. Over a fixed interval [0, T], the number of steps is T/h. Each step introduces an O(h²) error, and these errors can compound: each new step is taken from a slightly wrong position, creating an error in the next step. A careful analysis shows the errors do not simply add — the **global error** at the endpoint is O(h), not O(h²). Intuitively: the sum of (T/h) terms each of size O(h²) is O(h), and this first-order accumulation dominates. Halving h halves the global error — a first-order method. By contrast, a fourth-order method like Runge-Kutta has global error O(h^4), so halving h gives a 16× improvement. Euler's method is the baseline that all better methods are measured against.

The convergence proof — that global error → 0 as h → 0 — requires one technical condition: the **Lipschitz condition** on f. This says |f(t, y₁) - f(t, y₂)| ≤ L|y₁ - y₂| for all t and all y₁, y₂, where L is a fixed constant. The Lipschitz condition bounds how fast nearby solution curves can diverge. When L is large (a stiff problem), errors amplify rapidly and small h is required to achieve any accuracy. When L is small, errors stay controlled and moderate h suffices. Understanding this gives you a practical tool: if a problem requires very small h to stabilize, suspect stiffness and consider an implicit method rather than brute-forcing Euler with tiny steps.
