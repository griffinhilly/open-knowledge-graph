---
id: angular-momentum-quantum
title: Quantum Angular Momentum
domain: physics
course: quantum-mechanics
prerequisites:
- id: commutation-relations
  type: hard
- id: conservation-of-angular-momentum
  type: soft
- id: eigenvalues-eigenvectors
  type: hard
- id: angular-momentum-of-rigid-body
  type: soft
builds-toward:
- orbital-angular-momentum-quantum
- spin-angular-momentum
tags:
- angular-momentum
- rotation
- symmetry
stage: advanced
status: validated
---
# Quantum Angular Momentum

## Core Idea
Quantum angular momentum operators L̂ₓ, L̂ᵧ, L̂ᵧ satisfy canonical commutation relations [L̂ᵢ, L̂ⱼ] = iℏεᵢⱼₖL̂ₖ. The total angular momentum squared L̂² commutes with each component, so L̂² and one component (typically L̂ᵧ) can be simultaneously diagonalized. Eigenvalues of L̂ᵧ are mℏ where m = -l, -l+1, …, l-1, l and l is the angular momentum quantum number.

## Questions

```yaml
- question: "A student argues: 'The z-component of angular momentum is mℏ, so the total angular momentum magnitude must also be mℏ (just taking m = l for the maximum case).' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — the total magnitude is indeed lℏ when m = l"
    - "The eigenvalue of L̂² is ℏ²l(l+1), not ℏ²l², so the total magnitude is ℏ√(l(l+1)), which is always greater than lℏ"
    - "The z-component and total magnitude cannot be simultaneously definite, so the premise is invalid"
    - "Angular momentum in quantum mechanics has no definite total magnitude — only the z-component has eigenvalues"
  answer: 1
  explanation: "The eigenvalue equation is L̂²|l,m⟩ = ℏ²l(l+1)|l,m⟩, so the total magnitude is ℏ√(l(l+1)), not lℏ. For l = 1: magnitude = ℏ√2 ≈ 1.41ℏ, but the maximum z-component is only 1·ℏ. The discrepancy ℏ²l(l+1) vs. ℏ²l² is not a technicality — it reflects the fact that you cannot align the angular momentum vector exactly with the z-axis. The x and y components have zero expectation value but nonzero uncertainty, contributing to the total. Option C is wrong because L̂² and L̂_z commute, so they can be simultaneously definite. Option D is wrong because L̂² does have eigenvalues."

- question: "Why is it impossible to simultaneously know the x and y components of angular momentum for a quantum system with l > 0?"
  type: multiple-choice
  options:
    - "Because angular momentum is conserved and so its components cannot change — but measuring one fixes it forever"
    - "Because [L̂ₓ, L̂ᵧ] = iℏL̂_z ≠ 0, so measuring one component necessarily disturbs the other"
    - "Because quantum mechanics allows knowing at most two quantum numbers simultaneously"
    - "Because L̂ₓ and L̂ᵧ are not Hermitian and therefore have no real eigenvalues"
  answer: 1
  explanation: "The Heisenberg uncertainty principle applies whenever two operators do not commute: [L̂ₓ, L̂ᵧ] = iℏL̂_z. For a state with l > 0, L̂_z has nonzero eigenvalues, so the right-hand side is not zero, and the commutator is non-trivial. This means measuring L̂ₓ collapses the state in a way that introduces uncertainty in L̂ᵧ, and vice versa. Options A and C are confused. Option D is wrong — L̂ₓ and L̂ᵧ are both Hermitian, which is required for physical observables."

- question: "The quantization of the angular momentum quantum number l — that it must be a non-negative integer or half-integer — is imposed as a physical postulate rather than derived from the algebra of the operators."
  type: true-false
  answer: false
  explanation: "The quantization of l emerges from the algebra itself, via the ladder operators L̂₊ and L̂₋. These raise and lower the m quantum number by 1. Since m is bounded above and below (the z-component cannot exceed the total magnitude), the ladder must terminate: L̂₊|l,l⟩ = 0 and L̂₋|l,−l⟩ = 0. Working through the algebra of these termination conditions forces l to be a non-negative integer or half-integer and restricts m to the 2l+1 values from −l to +l. No additional postulate is needed."

- question: "The eigenvalue of L̂² for the state |l, m⟩ is ℏ²l², which reduces to ℏ² for l = 1."
  type: true-false
  answer: false
  explanation: "The correct eigenvalue is ℏ²l(l+1), not ℏ²l². For l = 1 this gives ℏ²·1·2 = 2ℏ², not ℏ². The l(l+1) form is a direct output of the ladder operator algebra and reflects the fact that you cannot simultaneously know all three components — the total magnitude is always larger than any single component's maximum value. The difference between l² and l(l+1) is not cosmetic: it implies the angular momentum vector can never be perfectly aligned with any axis."

- question: "Why can you simultaneously measure L̂² and L̂_z but not L̂_z and L̂ₓ? Explain using commutation relations."
  type: short-answer
  answer: "Two observables can be simultaneously measured (have simultaneous eigenstates) if and only if they commute. L̂² and L̂_z commute: [L̂², L̂_z] = 0. This can be verified using the commutation relations [L̂ᵢ, L̂ⱼ] = iℏεᵢⱼₖL̂ₖ and the fact that L̂² = L̂ₓ² + L̂ᵧ² + L̂_z² is rotationally invariant. In contrast, [L̂_z, L̂ₓ] = iℏL̂ᵧ ≠ 0, so measuring L̂_z and L̂ₓ simultaneously is forbidden by the uncertainty principle. The physical picture is that L̂² measures the total length of the angular momentum vector (which is rotation-invariant), while L̂_z measures its projection onto one axis — these are compatible. But knowing two different components would completely specify the vector's direction, which would violate the uncertainty principle for the remaining component."
  explanation: "The strategy of identifying which operators commute is the general method for finding complete sets of commuting observables (CSCOs) in quantum mechanics. {L̂², L̂_z} forms a CSCO for angular momentum; their shared eigenstates |l, m⟩ are the basis for atomic orbital labels and for the hydrogen atom energy levels."
```

## Explainer

In classical mechanics you already know, angular momentum is a continuous vector L = r × p that can point in any direction and take any magnitude. Quantum mechanics replaces this with operators, and the commutation relations you studied tell you something profound: you cannot simultaneously know all three components of angular momentum. Specifically, [L̂ₓ, L̂ᵧ] = iℏL̂_z means measuring L̂ₓ disturbs L̂ᵧ. This is a direct consequence of the algebra, not an experimental accident.

The way out is to find what you *can* measure simultaneously. The total angular momentum squared L̂² = L̂ₓ² + L̂ᵧ² + L̂_z² commutes with each component: [L̂², L̂_z] = 0. This means you can simultaneously have definite values for the *magnitude* of angular momentum and *one* component (conventionally chosen as L̂_z). The shared eigenstates |l, m⟩ are labeled by two quantum numbers: **l** (the angular momentum quantum number, a non-negative integer or half-integer) and **m** (the magnetic quantum number, ranging from −l to +l in integer steps). The eigenvalue equations are L̂²|l,m⟩ = ℏ²l(l+1)|l,m⟩ and L̂_z|l,m⟩ = mℏ|l,m⟩.

The quantization of l to integer steps is not imposed by hand — it falls out of the algebra. The key argument uses **ladder operators** L̂₊ = L̂ₓ + iL̂ᵧ and L̂₋ = L̂ₓ − iL̂ᵧ, which raise and lower the m quantum number by 1. Since m must be bounded (you cannot have a component larger than the total magnitude), the ladder must terminate. The requirement that the ladder terminates at both ends — L̂₊|l,l⟩ = 0 and L̂₋|l,−l⟩ = 0 — forces l to be a non-negative integer or half-integer and restricts m to the 2l + 1 values from −l to +l.

The physical picture that helps: think of the angular momentum vector as having a fixed magnitude ℏ√(l(l+1)) and a definite projection mℏ onto the z-axis, but its orientation in the x-y plane is completely uncertain. The vector "precesses" around the z-axis in a way you cannot track — which is exactly what the uncertainty principle between L̂ₓ and L̂ᵧ enforces. This structure is the foundation for everything that follows: orbital angular momentum gives the l = 0, 1, 2, … states of the hydrogen atom, while spin angular momentum extends the framework to half-integer l, leading to the electron spin states you will study next.
