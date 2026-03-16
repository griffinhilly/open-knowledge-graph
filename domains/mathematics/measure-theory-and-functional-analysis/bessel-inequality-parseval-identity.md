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
stage: abstract-reasoning
status: draft
---

# Bessel's Inequality and Parseval's Identity

## Core Idea
Bessel's inequality states Σᵢ |⟨x, eᵢ⟩|² ≤ ‖x‖² for any orthonormal system {eᵢ}. Parseval's identity is the equality case: when {eᵢ} is a complete orthonormal basis, Σᵢ |⟨x, eᵢ⟩|² = ‖x‖². This connects L² functions to their Fourier coefficients.

## Explainer

From orthonormal bases in Hilbert spaces, you know that given an orthonormal system {e₁, e₂, e₃, …} and a vector x, you can form the **Fourier coefficients** cᵢ = ⟨x, eᵢ⟩. These are the coordinates of x with respect to the basis vectors — or partial coordinates, if the system is not yet known to be complete. The partial sums Sₙ = Σᵢ₌₁ⁿ cᵢeᵢ represent the best approximation to x within the finite-dimensional span of {e₁, …, eₙ}. Bessel's inequality emerges immediately from examining how well this approximation does.

The key computation is to expand ‖x − Sₙ‖². Using orthonormality, this equals ‖x‖² − Σᵢ₌₁ⁿ |cᵢ|². Since a squared norm is always non-negative, ‖x‖² − Σᵢ₌₁ⁿ |cᵢ|² ≥ 0, which rearranges to **Bessel's inequality**: Σᵢ₌₁ⁿ |cᵢ|² ≤ ‖x‖². Because this holds for every n, the infinite series Σᵢ |⟨x, eᵢ⟩|² converges and is bounded above by ‖x‖². Intuitively: the total "energy" in all the Fourier coefficients cannot exceed the total "energy" in x itself. Some energy may be "lost" if the orthonormal system is incomplete — meaning there are directions in the Hilbert space not captured by any eᵢ.

**Parseval's identity** is the equality version: Σᵢ |⟨x, eᵢ⟩|² = ‖x‖². This holds exactly when the orthonormal system is a complete orthonormal basis — when there are no missing directions. Equality means the partial sums Sₙ → x in norm: the Fourier series converges to x in the Hilbert space sense. Parseval's identity is equivalent to completeness of the orthonormal system, and it is the Hilbert space analogue of the Pythagorean theorem: the squared norm of a vector equals the sum of the squares of all its coordinate magnitudes.

For L²([0, 2π]) with the trigonometric basis {1/√(2π), cos(nx)/√π, sin(nx)/√π}, Parseval's identity says that for any square-integrable function f, the sum of the squares of all its Fourier coefficients equals (1/2π)∫|f|². This is why Fourier analysis works: you can represent a function by its coefficients and recover its norm exactly. In quantum mechanics, the same identity underpins the interpretation of probability amplitudes — the sum of squared coefficients in any orthonormal expansion of a state vector must equal 1.

The gap between Bessel's inequality and Parseval's identity is precisely the missing "energy" in directions not spanned by the orthonormal system. Testing whether a given orthonormal set is actually a basis amounts to checking whether this gap is zero for all x — equivalently, whether the only vector orthogonal to every eᵢ is the zero vector. When Parseval's identity holds, the Hilbert space is "fully described" by the basis, and the coefficients ⟨x, eᵢ⟩ carry complete information about x.
