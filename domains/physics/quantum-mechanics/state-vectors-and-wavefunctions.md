---
id: state-vectors-and-wavefunctions
title: State Vectors and Wavefunctions
domain: physics
course: quantum-mechanics
prerequisites:
- id: hilbert-spaces-and-dirac-notation
  type: hard
- id: schrodinger-equation-intro
  type: soft
builds-toward:
- quantum-superposition
- quantum-postulates
tags:
- quantum-state
- wavefunction
- foundations
stage: advanced
status: draft
---

# State Vectors and Wavefunctions

## Core Idea
A quantum state is represented by a vector in Hilbert space, written as |ψ⟩ in Dirac notation or ψ(x) in position representation. The wavefunction ψ(x) is the position-space representation of the state vector, and |ψ(x)|² gives the probability density of finding the particle at position x. All information about a quantum system is encoded in its state vector.

## Explainer

From your work with Hilbert spaces and Dirac notation, you know that a Hilbert space is a complete vector space equipped with an inner product. A quantum state is a vector |ψ⟩ in such a space — that is the fundamental postulate. Everything else follows from how this vector evolves and how measurements relate to it. The power of this abstraction is that it works for any quantum system: a spin-1/2 particle lives in a two-dimensional Hilbert space, a harmonic oscillator lives in an infinite-dimensional one, and the formalism is identical in both cases.

The **wavefunction** ψ(x) is what you get when you represent the abstract state vector in the position basis. Just as a 3D vector **v** can be written as its Cartesian components (vx, vy, vz), the state |ψ⟩ can be decomposed into "components" along the position basis vectors |x⟩ — and that continuum of components is the function ψ(x) = ⟨x|ψ⟩. The inner product ⟨x|ψ⟩ projects |ψ⟩ onto the direction |x⟩ in Hilbert space, extracting the amplitude for finding the particle at position x. Because position is continuous, the "components" form a function rather than a finite or countably infinite list.

The Born rule connects this to measurement: |ψ(x)|² is the **probability density** of finding the particle at position x. This is the bridge between the abstract vector formalism and experimental outcomes. But ψ(x) is just one representation — the momentum-space wavefunction ψ̃(p) = ⟨p|ψ⟩ is another representation of the same state |ψ⟩, related to ψ(x) by a Fourier transform. Switching between position and momentum space is literally changing basis in Hilbert space, which explains why ψ(x) and ψ̃(p) are Fourier transform pairs.

The conceptual shift from the Schrödinger equation you've seen to this framework is that the wavefunction ψ(x,t) is demoted from fundamental to derived: it is the position-space projection of the state vector |ψ(t)⟩, which evolves by iℏ d|ψ⟩/dt = Ĥ|ψ⟩. Any observable is a Hermitian operator Ô, and measuring it returns an eigenvalue with probability |⟨n|ψ⟩|² where |n⟩ is the corresponding eigenvector. The state vector encodes all this probabilistic information about every possible measurement simultaneously — not just position, but momentum, energy, angular momentum, and any other observable you care to ask about.
