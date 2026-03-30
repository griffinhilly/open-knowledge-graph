---
id: fourier-analysis-sobolev-embedding
title: Fourier Analysis for PDEs and Sobolev Embedding
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: fourier-transform-methods-pdes
  type: hard
- id: sobolev-spaces-pdes
  type: hard
tags: [pde, fourier-analysis, sobolev-embedding, pseudodifferential, regularity]
stage: expert
status: validated
---
# Fourier Analysis for PDEs and Sobolev Embedding

## Core Idea
The Fourier transform provides a frequency-space characterization of Sobolev spaces: u ∈ H^s(ℝⁿ) if and only if (1+|ξ|²)^{s/2}û(ξ) ∈ L²(ℝⁿ). This characterization defines fractional Sobolev spaces H^s for any real s, extends the Sobolev embedding theorems to this general setting, and connects PDE regularity to the decay of Fourier coefficients. The theory of pseudodifferential operators and Fourier multipliers grows from this foundation, providing a systematic calculus for studying variable-coefficient and nonlinear PDEs through their behavior in frequency space.

## Questions
```yaml
- question: "The Sobolev space H^s(ℝⁿ) is characterized via the Fourier transform as:"
  type: multiple-choice
  options:
    - "u ∈ H^s iff ∫(1+|ξ|²)^s |û(ξ)|² dξ < ∞"
    - "u ∈ H^s iff |û(ξ)| ≤ C|ξ|^{-s}"
    - "u ∈ H^s iff û has compact support"
    - "u ∈ H^s iff û ∈ L^s"
  answer: 0
  explanation: "The H^s norm is ||u||²_{H^s} = ∫(1+|ξ|²)^s|û(ξ)|²dξ. The weight (1+|ξ|²)^s penalizes high frequencies when s > 0 (requiring smoothness) and allows high frequencies when s < 0 (permitting distributions). This is equivalent to the weak derivative definition when s is a non-negative integer."
- question: "Fractional Sobolev spaces H^s for non-integer s are naturally defined using the Fourier transform."
  type: true-false
  answer: true
  explanation: "While integer-order Sobolev spaces can be defined using weak derivatives, the Fourier characterization immediately extends to any real s, including negative values. H^{-s} is the dual of H^s₀, and H^{1/2} appears naturally as the trace space for H¹."
- question: "What does the Sobolev embedding theorem say in terms of Fourier decay?"
  type: short-answer
  answer: "If s > n/2, then the Fourier integral ∫(1+|ξ|²)^{-s}dξ converges, so H^s(ℝⁿ) embeds into continuous functions"
  explanation: "When s > n/2, functions in H^s have Fourier transforms in L¹ (by Cauchy-Schwarz: ∫|û|dξ ≤ ||u||_{H^s}(∫(1+|ξ|²)^{-s}dξ)^{1/2} < ∞), so u = ∫ûe^{iξ·x}dξ is continuous and bounded. This is the critical condition for pointwise regularity."
- question: "A Fourier multiplier operator T_m defined by (T_m u)^∧(ξ) = m(ξ)û(ξ) is bounded on L² for any bounded m."
  type: true-false
  answer: true
  explanation: "By Parseval's theorem, ||T_m u||_{L²} = ||m û||_{L²} ≤ ||m||_{L^∞}||û||_{L²} = ||m||_{L^∞}||u||_{L²}. L² boundedness of Fourier multipliers is automatic. Boundedness on L^p for p ≠ 2 is much deeper and is the subject of the Hormander-Mikhlin multiplier theorem."
```

## Explainer
The Fourier transform is the natural lens through which to view Sobolev spaces and regularity for PDEs. A function is smooth if and only if its Fourier transform decays rapidly at high frequencies, and a function is in H^s if its Fourier transform decays fast enough that the weighted L² integral ∫(1+|ξ|²)^s|û|²dξ converges. This frequency-space perspective makes the Sobolev embedding theorems geometrically transparent: embedding into continuous functions requires the Fourier transform to be in L¹, which happens when the H^s norm controls enough frequency decay, specifically when s > n/2.

Fractional Sobolev spaces are indispensable in PDE theory. The trace of an H¹ function on a hypersurface belongs to H^{1/2}—a fractional space that cannot be defined using classical derivatives. Interpolation between integer-order spaces, regularity results for non-integer gains, and the precise characterization of boundary regularity all require the fractional framework. The Fourier definition makes these spaces effortless to work with: H^s is simply the space where the "frequency weight" (1+|ξ|²)^{s/2} times û is square-integrable.

Pseudodifferential operators generalize both differential operators and Fourier multipliers. A differential operator P = Σ a_α(x)D^α has symbol p(x,ξ) = Σ a_α(x)ξ^α, and the pseudodifferential operator P(x,D)u = ∫p(x,ξ)û(ξ)e^{iξ·x}dξ extends this to symbols p(x,ξ) that need not be polynomial in ξ. The calculus of pseudodifferential operators—composition, adjoint, and parametrix construction—provides a systematic machinery for studying elliptic regularity, wave propagation, and spectral theory. The symbol encodes the microlocal behavior: where in phase space (position × frequency) the operator acts.

The Littlewood-Paley decomposition is another Fourier-analytic tool central to modern PDE theory. It decomposes a function into frequency bands: u = Σ_j Δ_j u, where each Δ_j u has Fourier transform supported in an annulus |ξ| ~ 2^j. This decomposition characterizes Sobolev and Besov spaces through sequence-space conditions on the pieces, and it is the main technical tool for proving nonlinear estimates, establishing well-posedness for dispersive equations, and understanding the cascade of energy across scales in fluid dynamics.
