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

## Questions

```yaml
- question: "A quantum particle is described by a state vector |ψ⟩. A physicist writes ψ(x) = ⟨x|ψ⟩. What is ψ(x)?"
  type: multiple-choice
  options:
    - "A complete description of the particle that fully replaces the state vector |ψ⟩"
    - "The probability of finding the particle at position x"
    - "The position-space representation of |ψ⟩ — one basis decomposition of the same abstract state"
    - "A different quantum state from |ψ⟩, defined only when position is measured"
  answer: 2
  explanation: "ψ(x) = ⟨x|ψ⟩ is the projection of the abstract state vector |ψ⟩ onto the position basis vector |x⟩ — it is the position-space representation of the state. The state vector |ψ⟩ is the fundamental object; ψ(x) is what you get when you decompose it in the position basis, just as a 3D vector can be expressed as its Cartesian components. The same state has a momentum-space representation ψ̃(p) = ⟨p|ψ⟩, related by a Fourier transform. Neither representation is more fundamental than the other; both encode the same information about |ψ⟩."

- question: "A physicist knows the position-space wavefunction ψ(x) of a particle. To find the probability density for measuring a specific momentum value p, they need a separate, independent measurement. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — position and momentum wavefunctions contain different physical information and require independent preparation"
    - "No — ψ̃(p) is the Fourier transform of ψ(x), and both encode the full state |ψ⟩"
    - "Yes — once you have ψ(x), momentum information is destroyed by the Heisenberg uncertainty principle"
    - "No — but only because momentum can be inferred from the slope of ψ(x)"
  answer: 1
  explanation: "ψ(x) and ψ̃(p) are two representations of the same state vector |ψ⟩ in two different bases. The relation ψ̃(p) = ⟨p|ψ⟩ can be computed directly from ψ(x) via the Fourier transform — changing from the position basis to the momentum basis in Hilbert space is literally what a Fourier transform does. No additional measurement or preparation is needed. The state vector |ψ⟩ simultaneously encodes probability amplitudes for position, momentum, energy, and every other observable. Only measurement collapses the state; knowing ψ(x) gives you all of this before any measurement."

- question: "The position-space wavefunction ψ(x) and the momentum-space wavefunction ψ̃(p) contain the same physical information about a quantum system — neither is more fundamental."
  type: true-false
  answer: true
  explanation: "Both are representations of the same abstract state vector |ψ⟩ in different bases. The Fourier transform that relates ψ(x) to ψ̃(p) is exactly the change-of-basis operation in Hilbert space. The position basis {|x⟩} and momentum basis {|p⟩} are equally valid complete orthonormal sets; decomposing |ψ⟩ in either one gives a function that encodes all physical predictions for that observable. There is no preferred representation — choosing position or momentum space is a practical convenience, not a statement about which is more real."

- question: "The Born rule states that |ψ(x)|² gives the probability of finding the particle exactly at position x."
  type: true-false
  answer: false
  explanation: "This is a subtle but important error: |ψ(x)|² is the probability *density*, not the probability. For a continuous variable like position, the probability of finding the particle in any single point is zero; you can only meaningfully ask for the probability in a finite interval. The correct statement is that the probability of finding the particle between x and x + dx is |ψ(x)|² dx. This is why the normalization condition is ∫|ψ(x)|² dx = 1 (integrating the density over all space gives 1), not |ψ(x)|² = 1."

- question: "Why does switching between the position-space wavefunction ψ(x) and the momentum-space wavefunction ψ̃(p) correspond to a change of basis in Hilbert space, and what does this reveal about the role of the Fourier transform in quantum mechanics?"
  type: short-answer
  answer: "ψ(x) = ⟨x|ψ⟩ is the component of |ψ⟩ along the basis vector |x⟩ in Hilbert space. ψ̃(p) = ⟨p|ψ⟩ is the component along |p⟩. Changing from the position basis to the momentum basis is mathematically equivalent to taking the Fourier transform of ψ(x). This reveals that the Fourier transform is not merely a mathematical technique in quantum mechanics — it is the natural operation of changing basis between two physically fundamental representations. The deep connection between position and momentum in quantum mechanics is thus a consequence of the Hilbert space structure, not an independent physical postulate."
  explanation: "This connection explains many features of quantum mechanics that would otherwise seem arbitrary. The uncertainty principle (Δx·Δp ≥ ℏ/2) is a theorem about Fourier transform pairs — a function that is tightly localized in position must be broadly spread in momentum, and vice versa. This is a property of the mathematics of Fourier transforms, not a mysterious physical fact layered on top. Understanding that ψ̃(p) is the Fourier transform of ψ(x) because they are basis representations of the same state vector |ψ⟩ makes the uncertainty principle structurally inevitable."
```

## Explainer

From your work with Hilbert spaces and Dirac notation, you know that a Hilbert space is a complete vector space equipped with an inner product. A quantum state is a vector |ψ⟩ in such a space — that is the fundamental postulate. Everything else follows from how this vector evolves and how measurements relate to it. The power of this abstraction is that it works for any quantum system: a spin-1/2 particle lives in a two-dimensional Hilbert space, a harmonic oscillator lives in an infinite-dimensional one, and the formalism is identical in both cases.

The **wavefunction** ψ(x) is what you get when you represent the abstract state vector in the position basis. Just as a 3D vector **v** can be written as its Cartesian components (vx, vy, vz), the state |ψ⟩ can be decomposed into "components" along the position basis vectors |x⟩ — and that continuum of components is the function ψ(x) = ⟨x|ψ⟩. The inner product ⟨x|ψ⟩ projects |ψ⟩ onto the direction |x⟩ in Hilbert space, extracting the amplitude for finding the particle at position x. Because position is continuous, the "components" form a function rather than a finite or countably infinite list.

The Born rule connects this to measurement: |ψ(x)|² is the **probability density** of finding the particle at position x. This is the bridge between the abstract vector formalism and experimental outcomes. But ψ(x) is just one representation — the momentum-space wavefunction ψ̃(p) = ⟨p|ψ⟩ is another representation of the same state |ψ⟩, related to ψ(x) by a Fourier transform. Switching between position and momentum space is literally changing basis in Hilbert space, which explains why ψ(x) and ψ̃(p) are Fourier transform pairs.

The conceptual shift from the Schrödinger equation you've seen to this framework is that the wavefunction ψ(x,t) is demoted from fundamental to derived: it is the position-space projection of the state vector |ψ(t)⟩, which evolves by iℏ d|ψ⟩/dt = Ĥ|ψ⟩. Any observable is a Hermitian operator Ô, and measuring it returns an eigenvalue with probability |⟨n|ψ⟩|² where |n⟩ is the corresponding eigenvector. The state vector encodes all this probabilistic information about every possible measurement simultaneously — not just position, but momentum, energy, angular momentum, and any other observable you care to ask about.
