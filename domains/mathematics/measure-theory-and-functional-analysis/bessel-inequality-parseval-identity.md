---
id: bessel-inequality-parseval-identity
title: Bessel's Inequality and Parseval's Identity
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: orthonormal-bases-in-hilbert
  type: hard
tags:
- hilbert-spaces
- parseval
stage: advanced
status: draft
---

# Bessel's Inequality and Parseval's Identity

## Core Idea
Bessel's inequality states Σᵢ |⟨x, eᵢ⟩|² ≤ ‖x‖² for any orthonormal system {eᵢ}. Parseval's identity is the equality case: when {eᵢ} is a complete orthonormal basis, Σᵢ |⟨x, eᵢ⟩|² = ‖x‖². This connects L² functions to their Fourier coefficients.

## Questions

```yaml
- question: "For a Hilbert space vector x and an orthonormal system {eᵢ}, you compute Σ|⟨x, eᵢ⟩|² and find it is strictly less than ‖x‖². What can you conclude?"
  type: multiple-choice
  options:
    - "The partial series has not converged yet; summing more terms will close the gap"
    - "The orthonormal system does not form a complete basis for the Hilbert space"
    - "The vector x was not correctly normalized before computing the coefficients"
    - "The Fourier series for x diverges in this orthonormal system"
  answer: 1
  explanation: "A strict inequality Σ|⟨x, eᵢ⟩|² < ‖x‖² means the system is incomplete — x has a nonzero component in directions orthogonal to every eᵢ. The gap is not about truncation: even the full infinite sum fails to reach ‖x‖². Parseval's identity (equality) is equivalent to completeness of the orthonormal system."

- question: "What is the fundamental reason Bessel's inequality (Σᵢ|⟨x, eᵢ⟩|² ≤ ‖x‖²) holds for any orthonormal system?"
  type: multiple-choice
  options:
    - "Orthogonality forces the Fourier coefficients to sum to zero, bounding their squares"
    - "The Cauchy-Schwarz inequality bounds each individual coefficient by ‖x‖, so their sum is bounded"
    - "The squared norm ‖x − Sₙ‖² is always non-negative, which forces the sum of squared coefficients to be at most ‖x‖²"
    - "Convergence of the Fourier series in norm implies the coefficients must be square-summable"
  answer: 2
  explanation: "Expanding ‖x − Sₙ‖² using orthonormality yields ‖x‖² − Σᵢ₌₁ⁿ|cᵢ|². Since any squared norm is ≥ 0, this gives Σᵢ₌₁ⁿ|cᵢ|² ≤ ‖x‖². The inequality is a direct consequence of non-negativity of norms — not of individual coefficient bounds."

- question: "Parseval's identity Σᵢ|⟨x, eᵢ⟩|² = ‖x‖² holding for all x in a Hilbert space is equivalent to the orthonormal system {eᵢ} being a complete orthonormal basis."
  type: true-false
  answer: true
  explanation: "Parseval's identity (equality) holds if and only if the Fourier series converges to x itself, which happens if and only if there is no nonzero vector orthogonal to all eᵢ — the definition of completeness. The identity is literally the Pythagorean theorem extended to infinite dimensions, valid only when all directions are accounted for."

- question: "If an orthonormal system {eᵢ} satisfies Bessel's inequality but not Parseval's identity for some vector x, the 'missing energy' can be recovered by simply summing more terms in the same Fourier series."
  type: true-false
  answer: false
  explanation: "The missing energy corresponds to the component of x lying in the orthogonal complement of the closed subspace spanned by all the eᵢ. No additional terms drawn from the same system can capture it — those directions simply do not exist in the span. Recovering the energy requires either adding new basis vectors that span the missing directions or recognizing the system is incomplete."

- question: "An orthonormal system {eᵢ} spans a proper closed subspace V of a Hilbert space H. Explain why the Fourier series Σᵢ⟨x, eᵢ⟩eᵢ converges for any x ∈ H, yet fails to converge to x when x ∉ V."
  type: short-answer
  answer: "The series converges because Bessel's inequality guarantees Σ|⟨x, eᵢ⟩|² ≤ ‖x‖² < ∞, and in a Hilbert space, square-summability of coefficients implies convergence of the series in norm. However, the sum converges to PV(x), the orthogonal projection of x onto V — not to x itself. The difference x − PV(x) is orthogonal to every eᵢ and represents the component of x in the orthogonal complement of V. Only when V = H (the system is complete) does PV(x) = x and Parseval's identity hold."
  explanation: "The key distinction is between convergence of the series (guaranteed by Bessel) and convergence to x (guaranteed only by completeness). The Fourier series always recovers the projection; Parseval's identity is the statement that this projection is the identity map — that V = H."
```

## Explainer

From orthonormal bases in Hilbert spaces, you know that given an orthonormal system {e₁, e₂, e₃, …} and a vector x, you can form the **Fourier coefficients** cᵢ = ⟨x, eᵢ⟩. These are the coordinates of x with respect to the basis vectors — or partial coordinates, if the system is not yet known to be complete. The partial sums Sₙ = Σᵢ₌₁ⁿ cᵢeᵢ represent the best approximation to x within the finite-dimensional span of {e₁, …, eₙ}. Bessel's inequality emerges immediately from examining how well this approximation does.

The key computation is to expand ‖x − Sₙ‖². Using orthonormality, this equals ‖x‖² − Σᵢ₌₁ⁿ |cᵢ|². Since a squared norm is always non-negative, ‖x‖² − Σᵢ₌₁ⁿ |cᵢ|² ≥ 0, which rearranges to **Bessel's inequality**: Σᵢ₌₁ⁿ |cᵢ|² ≤ ‖x‖². Because this holds for every n, the infinite series Σᵢ |⟨x, eᵢ⟩|² converges and is bounded above by ‖x‖². Intuitively: the total "energy" in all the Fourier coefficients cannot exceed the total "energy" in x itself. Some energy may be "lost" if the orthonormal system is incomplete — meaning there are directions in the Hilbert space not captured by any eᵢ.

**Parseval's identity** is the equality version: Σᵢ |⟨x, eᵢ⟩|² = ‖x‖². This holds exactly when the orthonormal system is a complete orthonormal basis — when there are no missing directions. Equality means the partial sums Sₙ → x in norm: the Fourier series converges to x in the Hilbert space sense. Parseval's identity is equivalent to completeness of the orthonormal system, and it is the Hilbert space analogue of the Pythagorean theorem: the squared norm of a vector equals the sum of the squares of all its coordinate magnitudes.

For L²([0, 2π]) with the trigonometric basis {1/√(2π), cos(nx)/√π, sin(nx)/√π}, Parseval's identity says that for any square-integrable function f, the sum of the squares of all its Fourier coefficients equals (1/2π)∫|f|². This is why Fourier analysis works: you can represent a function by its coefficients and recover its norm exactly. In quantum mechanics, the same identity underpins the interpretation of probability amplitudes — the sum of squared coefficients in any orthonormal expansion of a state vector must equal 1.

The gap between Bessel's inequality and Parseval's identity is precisely the missing "energy" in directions not spanned by the orthonormal system. Testing whether a given orthonormal set is actually a basis amounts to checking whether this gap is zero for all x — equivalently, whether the only vector orthogonal to every eᵢ is the zero vector. When Parseval's identity holds, the Hilbert space is "fully described" by the basis, and the coefficients ⟨x, eᵢ⟩ carry complete information about x.
