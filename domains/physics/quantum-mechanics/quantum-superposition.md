---
id: quantum-superposition
title: Quantum Superposition
domain: physics
course: quantum-mechanics
prerequisites:
- id: state-vectors-and-wavefunctions
  type: hard
- id: vector-spaces
  type: hard
builds-toward:
- entanglement-quantum
- quantum-measurement-problem
tags:
- superposition
- quantum-state
- wave-nature
stage: advanced
status: validated
---

# Quantum Superposition

## Core Idea
A quantum system can exist in a superposition of multiple states simultaneously, written as |ψ⟩ = Σ cₙ|φₙ⟩ where |cₙ|² are probabilities. Unlike classical systems where the system definitely is in one state, a superposed quantum state genuinely exhibits properties of all constituent states until measured. Superposition is fundamental to quantum mechanics and has no classical analogue.

## Questions

```yaml
- question: "In the double-slit experiment, a single electron passes through the apparatus and lands on a detector screen. If quantum superposition were merely classical ignorance — the electron secretly going through one slit or the other, we just don't know which — what pattern would we expect on the screen over many trials?"
  type: multiple-choice
  options:
    - "Two bright bands directly behind each slit, with darkness elsewhere"
    - "A single broad band in the center from electrons scattering off the barrier"
    - "A wave-like interference pattern with alternating bright and dark fringes"
    - "A uniform spread across the entire screen"
  answer: 0
  explanation: "If electrons were secretly going through one definite slit (we just don't know which), the screen would show two bright bands — one behind each slit — just as it would for classical particles like bullets. The classical ignorance interpretation predicts no interference. But experiments show interference fringes, which only arise when both amplitudes are simultaneously present and add before squaring. This is the key evidence that superposition is not ignorance: a genuine superposition of two paths produces cross-terms (interference) that a statistical mixture of two paths cannot."

- question: "A quantum system is in the state |ψ⟩ = (1/√2)|↑⟩ + (1/√2)|↓⟩. What does the normalization condition tell you about this state?"
  type: multiple-choice
  options:
    - "The system is 50% likely to be spin-up and 50% spin-down at all times, regardless of measurement"
    - "The squared magnitudes |cₙ|² sum to 1, ensuring probabilities are well-defined upon measurement"
    - "The system oscillates between spin-up and spin-down with equal frequency"
    - "The two amplitudes cancel out, leaving the particle in neither spin state"
  answer: 1
  explanation: "The normalization condition Σ|cₙ|² = 1 ensures that the probabilities of all possible measurement outcomes sum to one — a basic requirement for any probability distribution. The coefficients cₙ are complex probability amplitudes, and their squared magnitudes give measurement probabilities. This state would yield spin-up with probability 1/2 and spin-down with probability 1/2. It does NOT mean the system oscillates or that the two terms cancel — before measurement, both terms are simultaneously present in the superposition."

- question: "A quantum particle in a superposition of two paths can produce an interference pattern that a classical mixture of the same two paths cannot."
  type: true-false
  answer: true
  explanation: "This is the defining experimental signature of genuine quantum superposition. In a classical mixture, you take each path separately and add the resulting probability distributions — no interference terms appear. In a quantum superposition, the amplitudes from each path add first, and then you square to get probabilities. The cross-terms that arise from squaring (|c₁|²|c₂|²cos(phase)) produce constructive and destructive interference that is impossible in any classical probability model. This is why interference patterns prove that superposition is a physical reality, not mere ignorance."

- question: "When a quantum system is in superposition, it means the system secretly has one definite property but we lack the information to determine which one."
  type: true-false
  answer: false
  explanation: "This is the 'hidden variable' or classical ignorance interpretation, and it is ruled out by experiment. A quantum superposition is not a statement about our knowledge — it is a complete description of the system's physical state. The evidence against hidden variables is the existence of interference: if the system had a definite hidden state, the probability distributions from different paths would add classically, with no interference fringes. The observation of interference requires that both amplitudes are physically real and simultaneously present. The Bell inequality experiments further confirm that no local hidden variable theory can reproduce quantum predictions."

- question: "Why does the observation of interference in the double-slit experiment rule out the interpretation that superposition is just classical ignorance about which state the system is in? Reference the mathematical structure of superposition in your answer."
  type: short-answer
  answer: "In classical ignorance, you assign probabilities to each state and add the resulting distributions: P(total) = P(path 1) + P(path 2). No cross-terms appear. In quantum mechanics, amplitudes add: ψ = c₁ψ₁ + c₂ψ₂, so the probability |ψ|² = |c₁ψ₁ + c₂ψ₂|² = |c₁|²|ψ₁|² + |c₂|²|ψ₂|² + 2Re(c₁*c₂ψ₁*ψ₂). The interference term 2Re(c₁*c₂ψ₁*ψ₂) is nonzero and produces the fringe pattern — it cannot exist if the system were secretly in one path."
  explanation: "This distinction is the heart of quantum mechanics. Classical probability theory adds probability distributions; quantum mechanics adds amplitudes. The square of a sum differs from the sum of squares by cross-terms, and those cross-terms are the interference fringes we observe. Any hidden-variable theory that assigns the particle a definite path would predict no interference, contradicting experiment. The superposition must be taken seriously as a physical description, not a statement of ignorance."
```

## Explainer

You already know that quantum states live in a vector space, and that a state |ψ⟩ can be expanded in any complete basis {|φₙ⟩} as |ψ⟩ = Σ cₙ|φₙ⟩. **Superposition** is what this expansion means physically: the system is not "secretly" in one of the basis states while we remain ignorant — it genuinely occupies all states simultaneously, weighted by the coefficients cₙ. This is the sharpest departure from classical physics, and it demands a careful re-examination of what "state" means.

A classical coin lying flat is definitely heads or definitely tails — we might not know which, but one of those descriptions is true. A quantum coin in superposition is different: before measurement it is neither heads nor tails, and the description |ψ⟩ = c₀|heads⟩ + c₁|tails⟩ is complete — there is nothing more to say. The evidence for this is **interference**. If the system were merely in a classical mixture (heads with probability |c₀|², tails with probability |c₁|²), probabilities for overlapping paths would simply add. But quantum amplitudes add before squaring, producing interference fringes that only appear when both terms are simultaneously "present." The double-slit experiment is the iconic demonstration: each particle goes through both slits simultaneously, and the wave-like interference pattern cannot be explained unless the particle was in a superposition of both paths.

The coefficients cₙ are **probability amplitudes** — complex numbers whose squared magnitudes |cₙ|² give the probability of finding the system in state |φₙ⟩ upon measurement. The normalization condition Σ|cₙ|² = 1 ensures probabilities sum to one. Before measurement, the superposition is the complete description. Upon measurement, the state **collapses** to a single eigenstate: the system is now definitely in some |φₖ⟩ with probability |cₖ|², and all other amplitudes vanish. This collapse is instantaneous and irreversible, and it is the source of the quantum measurement problem you will study next.

A crucial subtlety: superposition is basis-dependent. A state that is a superposition in the energy eigenbasis may be an eigenstate in the position basis, and vice versa. The Schrödinger equation governs how superpositions evolve in time — deterministically, linearly, and coherently, preserving the full superposition — until measurement disrupts it. This tension between deterministic evolution and probabilistic collapse is at the heart of quantum foundations. But the computational power of superposition is already clear: a quantum system of n two-level particles lives in a 2ⁿ-dimensional Hilbert space, and superposition allows it to occupy all 2ⁿ directions simultaneously — the basis of quantum computing.
