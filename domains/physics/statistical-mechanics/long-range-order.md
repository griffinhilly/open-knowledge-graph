---
id: long-range-order
title: Long-Range Order
domain: physics
course: statistical-mechanics
prerequisites:
- id: two-point-correlation-functions
  type: hard
- id: phase-transitions
  type: soft
builds-toward:
- symmetry-breaking-phase-transitions
- goldstone-theorem
tags:
- order
- correlations
- phase-transitions
stage: expert
status: draft
---

# Long-Range Order

## Core Idea
Long-range order characterizes correlations that persist at arbitrarily large distances, quantified by non-zero lim_{|r|→∞} ⟨σ(r)σ(0)⟩. Ordered phases (crystals, ferromagnets, superconductors) exhibit long-range order; disordered phases do not. Its appearance/disappearance marks a phase transition.

## Questions

```yaml
- question: "A system's two-point correlation function ⟨σ(r)σ(0)⟩ behaves as exp(−|r|/ξ) for large |r|, with ξ finite. What does this indicate about the system's phase?"
  type: multiple-choice
  options:
    - "The system is in an ordered phase with long-range order characterized by correlation length ξ"
    - "The system is in a disordered phase — correlations decay to zero beyond a few correlation lengths, with no long-range coherence"
    - "The system is exactly at its critical point, where correlations decay as a power law"
    - "The system has partial long-range order, with ξ setting the range of ordering"
  answer: 1
  explanation: "Exponential decay to zero means distant points are statistically independent — the system has no global coherence. This is the disordered phase (e.g., a paramagnet above its Curie temperature). Long-range order requires ⟨σ(r)σ(0)⟩ to approach a non-zero constant as |r| → ∞. Option C (the critical point) is also wrong: at criticality, ξ diverges and correlations decay as a power law, not exponentially. A finite ξ means you are in a disordered phase, not at criticality."

- question: "In a ferromagnet below the Curie temperature with order parameter m = ⟨σ⟩ ≠ 0, why does the two-point function ⟨σ(r)σ(0)⟩ approach m² rather than zero at large |r|?"
  type: multiple-choice
  options:
    - "Because at large distances, σ(r) and σ(0) become statistically independent conditional on the global order, so ⟨σ(r)σ(0)⟩ → ⟨σ(r)⟩⟨σ(0)⟩ = m·m = m²"
    - "Because ordered phases have no fluctuations, so every spin exactly equals m"
    - "Because m² is the theoretical maximum of the correlation function"
    - "Because the correlation function must equal 1 at all distances in the ordered phase"
  answer: 0
  explanation: "When |r| is large enough that the two spins are statistically independent, their joint expectation factorizes: ⟨σ(r)σ(0)⟩ → ⟨σ(r)⟩⟨σ(0)⟩ = m². This is non-zero precisely because the system has broken symmetry: m ≠ 0 means each spin has a non-zero mean even when uncorrelated with any other specific spin. In the disordered phase, m = 0, and the same factorization gives zero — which is why the correlation function decays to zero there."

- question: "Exactly at the critical point of a second-order phase transition, the two-point correlation function decays exponentially with a very large but finite correlation length."
  type: true-false
  answer: false
  explanation: "Exactly at the critical point, the correlation length ξ *diverges* to infinity. The two-point function then cannot decay exponentially (exponential decay requires a finite ξ); instead it follows a power law: ⟨σ(r)σ(0)⟩ ~ |r|^(−(d−2+η)), where η is a critical exponent. This scale-invariant power-law behavior is the signature of criticality and underlies universality — the same exponents appear in seemingly different physical systems. 'Very large ξ' describes near-critical behavior approaching the transition, not the critical point itself."

- question: "Crystals, ferromagnets, and superconductors all exhibit long-range order, but the physical quantity that becomes long-range correlated differs between them."
  type: true-false
  answer: true
  explanation: "All three share the same mathematical signature — a two-point function that approaches a non-zero constant at large separation — but the quantity being correlated differs. In ferromagnets it is the spin ⟨σ(r)σ(0)⟩; in crystals it is the density ⟨ρ(r)ρ(0)⟩ oscillating at lattice periodicity; in superconductors and superfluids it is the off-diagonal element of the one-particle density matrix ⟨ψ†(r)ψ(0)⟩ (off-diagonal long-range order, ODLRO). The mathematical criterion for long-range order is universal; the physical interpretation varies."

- question: "Why is a non-zero order parameter m = ⟨σ⟩ equivalent to long-range order in the two-point correlation function?"
  type: short-answer
  answer: "When two spins are very far apart, they become statistically independent. Their correlation then factorizes: ⟨σ(r)σ(0)⟩ → ⟨σ⟩² = m². If the system has broken symmetry and m ≠ 0, this limit is non-zero — which is the definition of long-range order. If m = 0 (no broken symmetry), the factorized limit is zero, and the correlation decays to zero, meaning no long-range order."
  explanation: "The connection reveals why spontaneous symmetry breaking and long-range order are two sides of the same phenomenon. A non-zero order parameter means every spin independently carries a preferred direction. Statistical independence at large distance doesn't destroy the correlation because each spin is individually biased toward m, so their product averages to m² rather than zero. This equivalence between m ≠ 0 and non-zero limiting correlation is what makes the order parameter a complete diagnostic of the ordered phase."
```

## Explainer

You learned about **two-point correlation functions** ⟨σ(r)σ(0)⟩ as a way to quantify how fluctuations at one point in a system relate to fluctuations at another. In a completely disordered phase — a high-temperature paramagnet, or a liquid well above its critical temperature — correlations decay exponentially: ⟨σ(r)σ(0)⟩ ~ exp(−|r|/ξ), where ξ is the **correlation length**. Beyond a few correlation lengths, distant points are statistically independent. **Long-range order** is precisely the opposite behavior: the two-point function approaches a non-zero constant as |r| → ∞, meaning distant regions of the system remain statistically coupled no matter how far apart they are. The system has global coherence built into its equilibrium state.

The physical picture behind long-range order is **spontaneous symmetry breaking**. In a ferromagnet below the Curie temperature, every spin preferentially aligns along a global direction even though the Hamiltonian treats up and down symmetrically. Once the symmetry is broken, a spin at position r "knows" about the preferred direction regardless of its distance from the origin — hence non-zero ⟨σ(r)σ(0)⟩ at large |r|. The **order parameter** m = ⟨σ⟩ is non-zero in the ordered phase: the system has selected one particular state from among the symmetry-equivalent options. The correlation function at large distance approaches m², because when |r| is very large the two spins are statistically independent conditional on the global order: ⟨σ(r)σ(0)⟩ → ⟨σ(r)⟩⟨σ(0)⟩ = m².

Different physical systems exhibit distinct types of long-range order. Crystals have **translational long-range order**: the density-density correlation function ⟨ρ(r)ρ(0)⟩ oscillates at the lattice periodicity and maintains that oscillation out to arbitrarily large distances. Liquids lack this — density correlations decay within a few molecular diameters. Superconductors and superfluids carry **off-diagonal long-range order** (ODLRO): the off-diagonal elements of the one-particle density matrix ⟨ψ†(r)ψ(0)⟩ remain non-zero at large separation, reflecting the macroscopic phase coherence of the condensate. All these examples share the same mathematical signature: a two-point function that does not decay to zero.

The appearance or disappearance of long-range order defines a phase transition. Approaching the critical point from below, the order parameter m → 0 continuously (for a second-order transition), and correlations become long-ranged but not infinite. Exactly at the critical point, the correlation length ξ diverges and the two-point function decays as a power law: ⟨σ(r)σ(0)⟩ ~ |r|^(−(d−2+η)), where η is a critical exponent. This scale-invariant behavior at the critical point — and the fact that the same exponents appear in seemingly different systems — is what makes the renormalization group approach so powerful. The correlation function is therefore not just a diagnostic of order: it is the microscopic quantity that encodes the full structure of each phase, the phase boundaries between them, and the universal behavior at criticality.
