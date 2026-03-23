---
id: matrix-exponential
title: Matrix Exponential and Differential Equations
domain: mathematics
course: linear-algebra
prerequisites:
- id: diagonalization-similar-matrices
  type: hard
builds-toward:
- applications-linear-algebra-modeling
tags:
- matrix-exponential
- odes
- systems
stage: formal-systems
status: validated
---

# Matrix Exponential and Differential Equations

## Core Idea
The matrix exponential eᴬ = Σ Aⁿ/n! solves the matrix ODE dX/dt = AX with initial condition X(0) = I, giving X(t) = eᴬᵗ. If A is diagonalizable, eᴬ = PeᴰPP⁻¹ where e^D is diagonal. Solutions to dx/dt = Ax are x(t) = eᴬᵗx₀. Jordan normal form provides formulas for eᴬᵗ in the non-diagonalizable case.

## Questions

```yaml
- question: "A system x' = Ax has eigenvalues −2 and 3. Starting from any nonzero initial condition, what happens to solutions as t → ∞?"
  type: multiple-choice
  options:
    - "All solutions decay to zero, since one eigenvalue is negative"
    - "All solutions grow without bound (for generic initial conditions), since the positive eigenvalue component dominates"
    - "Solutions oscillate between growing and decaying phases"
    - "Only initial conditions aligned with the first eigenvector will cause growth"
  answer: 1
  explanation: "The solution is x(t) = e^{At}x₀ = c₁e^{−2t}v₁ + c₂e^{3t}v₂, where v₁, v₂ are eigenvectors. As t → ∞, the e^{−2t} term vanishes but the e^{3t} term grows without bound. For any initial condition with a nonzero component along v₂ (i.e., generic x₀), solutions grow. The negative eigenvalue does not save the system — it only controls one mode. The positive eigenvalue governs long-term behavior. A student who says 'one eigenvalue is negative so it might decay' is missing that growth always wins over decay as t → ∞."

- question: "Why does the diagonalization A = PDP⁻¹ make computing e^{At} tractable?"
  type: multiple-choice
  options:
    - "It reduces A to upper triangular form, where matrix exponentials always simplify"
    - "Because Aⁿ = PDⁿP⁻¹, the power series for e^{At} collapses to scalar exponentials e^{λᵢt} on the diagonal of e^{Dt}"
    - "Diagonalization ensures all eigenvalues are real, eliminating oscillatory behavior"
    - "It converts the matrix ODE into a system of decoupled polynomial equations"
  answer: 1
  explanation: "The key algebraic fact is Aⁿ = PDⁿP⁻¹, which follows by induction since (PDP⁻¹)ⁿ = PDⁿP⁻¹. Substituting into the series e^{At} = Σ (At)ⁿ/n!, you get P(Σ(Dt)ⁿ/n!)P⁻¹ = Pe^{Dt}P⁻¹. Since D is diagonal, e^{Dt} is simply diagonal with entries e^{λᵢt} — reducing the entire computation to scalar exponentials applied to eigenvalues. Diagonalization decouples the system into independent one-dimensional ODEs along eigenvector directions."

- question: "If a 2×2 matrix A has purely imaginary eigenvalues ±iω, then e^{At} produces oscillating solutions without growth or decay."
  type: true-false
  answer: true
  explanation: "Eigenvalues with zero real part give e^{(±iω)t} = cos(ωt) ± i·sin(ωt). The magnitude |e^{λt}| = e^{Re(λ)t} = e^0 = 1 for all t, so solutions neither grow nor shrink. The system oscillates forever at frequency ω. This is the undamped harmonic oscillator — purely imaginary eigenvalues are the hallmark of sustained periodic motion."

- question: "The matrix exponential satisfies e^{A+B} = e^A · e^B for any square matrices A and B."
  type: true-false
  answer: false
  explanation: "This identity holds for scalars but fails for matrices unless A and B commute (AB = BA). The proof for scalars uses the binomial theorem, which requires commutativity. For noncommuting matrices, cross terms in the series expansion do not cancel properly. A simple counterexample: A = [[0,1],[0,0]], B = [[0,0],[1,0]] gives AB ≠ BA and e^{A+B} ≠ e^A e^B. The correct generalization is the Baker–Campbell–Hausdorff formula."

- question: "A linear system x' = Ax has all eigenvalues with strictly negative real parts. What can you conclude about solutions for any initial condition, and why does this follow from the matrix exponential?"
  type: short-answer
  answer: "All solutions x(t) = e^{At}x₀ decay to zero as t → ∞. This follows because each mode in the solution is proportional to e^{λᵢt}, and |e^{λᵢt}| = e^{Re(λᵢ)t} → 0 as t → ∞ when Re(λᵢ) < 0. The matrix exponential decomposes the solution into independent modes — one per eigenvalue — and each mode decays exponentially. The system is asymptotically stable: regardless of where you start, the trajectory converges to the origin."
  explanation: "The matrix exponential makes long-term behavior a purely spectral question: look at the eigenvalues of A. Negative real parts → decay; positive real parts → growth; zero real parts → sustained oscillation or polynomial growth (if Jordan blocks exist). Engineers designing stable control systems, physicists modeling dissipative oscillators, and mathematicians analyzing dynamical systems all use this eigenvalue criterion as their first diagnostic."
```

## Explainer

The scalar exponential e^(at) solves the ODE dx/dt = ax — it is the function that is its own derivative, up to the factor a. The **matrix exponential** eᴬᵗ is the natural generalization: a matrix-valued function that solves the system dx/dt = Ax with any initial condition x(0) = x₀. Just as e^(at) is defined by its power series e^(at) = Σ (at)ⁿ/n!, the matrix exponential is defined by eᴬ = Σ Aⁿ/n!. This series converges for every square matrix A, making the definition rigorous — though computing it directly from the series would require infinitely many matrix multiplications.

This is where your prerequisite, diagonalization, becomes essential. If A = PDP⁻¹ where D is diagonal, then Aⁿ = PDⁿP⁻¹ for every n, and the power series telescopes: eᴬ = P(Σ Dⁿ/n!)P⁻¹ = PeᴰP⁻¹. Since D is diagonal, eᴰ is simply the diagonal matrix with e^(λᵢ) on each diagonal entry — reducing the whole computation to scalar exponentials applied to eigenvalues. Diagonalization decouples the system into independent one-dimensional ODEs, one for each eigenvector direction, and the matrix exponential reassembles the solutions.

The payoff is that any system of linear ODEs, dx/dt = Ax, has the general solution x(t) = eᴬᵗx₀. The long-term behavior — whether solutions grow, decay, or oscillate — depends entirely on the eigenvalues of A. Eigenvalues with negative real part produce decay; positive real part produces growth; purely imaginary eigenvalues produce oscillation. The matrix exponential transforms the qualitative question "what does this system do over time?" into a purely algebraic question about the **spectrum** of A.

When A is not diagonalizable, Jordan normal form provides the fallback. A Jordan block for eigenvalue λ gives e^(Jt) = e^(λt) times an upper-triangular matrix whose off-diagonal entries involve polynomial factors: te^(λt), t²e^(λt)/2, and so on. These **resonant terms** are characteristic of degenerate systems and explain phenomena like resonance in coupled oscillators, where the response grows without bound even at bounded input. The matrix exponential thus unifies the classification of linear ODE behavior — stability, oscillation, and resonance — under a single computational framework.
