---
id: romberg-integration
title: Romberg Integration
domain: mathematics
course: numerical-analysis
prerequisites:
- id: richardson-extrapolation
  type: hard
- id: composite-quadrature
  type: hard
tags:
- romberg
- integration
- extrapolation
stage: advanced
status: draft
---

# Romberg Integration

## Core Idea
Romberg integration systematically applies composite trapezoidal rules with successive halvings of step size, then uses Richardson extrapolation to accelerate convergence. The method builds a triangular array where each new entry combines results from halved step size with previous entries to cancel error terms. Romberg achieves high accuracy efficiently and provides adaptive error estimation.

## Questions

```yaml
- question: "A numerical analyst has computed composite trapezoidal estimates T(h), T(h/2), T(h/4), and T(h/8). When they form column 1 of the Romberg table by combining T(h) and T(h/2), what has been accomplished?"
  type: multiple-choice
  options:
    - "The estimate is now equivalent to using the trapezoidal rule with step size h/4"
    - "The O(h²) error term has been cancelled, leaving an estimate with O(h⁴) error"
    - "The result is simply the average of T(h) and T(h/2), providing a better mean"
    - "All error terms have been eliminated, giving the exact integral"
  answer: 1
  explanation: "Richardson extrapolation combines two estimates with known error structure to cancel the leading error term. The trapezoidal rule has error proportional to h², so combining T(h) and T(h/2) eliminates the O(h²) term, leaving an estimate with O(h⁴) error. This is not simply averaging — it is the weighted combination (4·T(h/2) − T(h))/3, which equals Simpson's rule. Further columns of the Romberg table cancel successively higher-order terms."

- question: "Why does Romberg integration require relatively few new function evaluations when adding a new row to the table by halving the step size?"
  type: multiple-choice
  options:
    - "It uses a Monte Carlo sampling scheme that does not require a fine grid"
    - "The new, finer grid contains all the points of the previous grid as a subset"
    - "It only evaluates the integrand at the endpoints, regardless of step size"
    - "Romberg avoids evaluating the integrand entirely, relying on symbolic integration"
  answer: 1
  explanation: "When you halve the step size from h to h/2, the new grid at h/2 includes all the points that were already in the grid at h, plus new midpoints between them. Only the new midpoints require fresh function evaluations. This means each new row of the Romberg table costs only about half as many new evaluations as the total evaluations in that row, making the method remarkably efficient for smooth functions."

- question: "The entries in column 1 of the Romberg table are equivalent to Simpson's rule approximations."
  type: true-false
  answer: true
  explanation: "Column 0 of the Romberg table holds composite trapezoidal approximations. Column 1 applies Richardson extrapolation to cancel the O(h²) error, producing estimates equivalent to Simpson's rule (which achieves O(h⁴) accuracy). Column 2 cancels the O(h⁴) error, equivalent to Boole's rule. Each successive column corresponds to a higher-order quadrature rule, with extrapolation systematically eliminating the next error term."

- question: "Romberg integration converges faster than the composite trapezoidal rule primarily because it uses more function evaluations per step."
  type: true-false
  answer: false
  explanation: "Romberg integration's speedup comes from Richardson extrapolation eliminating error terms algebraically, not from using more function evaluations. It achieves high accuracy by reusing existing evaluations and combining them cleverly, rather than simply taking more or smaller steps. A key structural fact enabling this is that the trapezoidal rule's error consists only of even powers of h, which allows successive Richardson steps to cancel each term precisely."

- question: "Explain why the composite trapezoidal rule's error consisting exclusively of even powers of h is crucial to Romberg integration's effectiveness."
  type: short-answer
  answer: "The Euler–Maclaurin formula shows that the trapezoidal error is T(h) = I + c₁h² + c₂h⁴ + ..., with no odd-power terms. Halving h to get T(h/2) scales each term by powers of 1/4. This predictable structure means you can algebraically combine T(h) and T(h/2) to cancel the c₁h² term exactly, leaving an error of order h⁴. If the error had odd-power terms, the cancellation would not be clean and the extrapolation would not eliminate the leading term so precisely."
  explanation: "The absence of odd-power terms follows from the trapezoidal rule's symmetry — errors from symmetric intervals cancel at even powers. Without this regularity, Romberg's systematic table construction would not work: you could not predict which combination of T(h) and T(h/2) eliminates the leading error, because the error structure would be less rigid."
```

## Explainer

From your study of composite quadrature, you know the composite trapezoidal rule approximates ∫f(x)dx with error proportional to h² — halving the step size h reduces the error by a factor of four, requiring twice as many function evaluations. That convergence rate is fine but not spectacular. From Richardson extrapolation, you know a more powerful idea: if you have two estimates of a quantity with a known error structure, you can algebraically combine them to cancel the leading error term and get a much more accurate estimate without extra function evaluations. Romberg integration is what happens when you apply Richardson extrapolation repeatedly and systematically to the trapezoidal rule.

Start with the trapezoidal approximation T(h) at step size h. The **Euler–Maclaurin formula** tells us the error has the exact form: T(h) = I + c₁h² + c₂h⁴ + c₃h⁶ + ..., where I is the true integral and the cₖ are constants (depending on the function but not on h). This is the key structural fact: the error consists of even powers of h only. Halve h to get T(h/2) = I + c₁(h/2)² + c₂(h/2)⁴ + ... = I + c₁h²/4 + c₂h⁴/16 + ... Multiply the first equation by 1 and the second by 4, then subtract: the c₁h² term cancels, leaving a new estimate with error O(h⁴). This is Richardson extrapolation eliminating the leading error term.

The **Romberg table** applies this process repeatedly. Column 0 holds trapezoidal approximations T(h), T(h/2), T(h/4), ... (each row halves the step, doubling the function evaluations but cleverly reusing old ones since every other point of the finer grid already exists). Column 1 holds the Richardson combinations that cancel O(h²) error — these are Simpson's rule values. Column 2 cancels O(h⁴) error — these are Boole's rule values. Each successive column eliminates another error term, so the diagonal of the triangular table converges much faster than the first column alone. For smooth functions, the method achieves very high accuracy with relatively few function evaluations.

The table also provides a natural **error estimate**: compare the bottom-right entries in adjacent columns. If they agree to many decimal places, you have likely converged. If not, add another row (halve h again) and extend the table. This adaptive character makes Romberg practical: you keep refining until the error estimate is satisfactory, spending function evaluations only where needed. For smooth integrands, Romberg is often the method of choice — it combines the simplicity of the trapezoidal rule (easy to implement, robust, reuses evaluations) with the accuracy of high-order methods, all without requiring any special structure from the integrand beyond smoothness.
