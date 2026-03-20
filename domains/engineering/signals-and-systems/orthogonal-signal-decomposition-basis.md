---
id: orthogonal-signal-decomposition-basis
title: Orthogonal Signal Decomposition and Basis Functions
domain: engineering
course: signals-and-systems
prerequisites: []
builds-toward:
- fourier-series-representation
- fourier-transform-definition-properties
tags:
- signals
- orthogonal
- decomposition
- basis
stage: abstract-reasoning
status: draft
---

# Orthogonal Signal Decomposition and Basis Functions

## Core Idea
Signals can be decomposed as linear combinations of orthogonal basis functions such as sines, cosines, or wavelets. Orthogonality means basis functions are mutually independent with zero inner product. This decomposition enables efficient signal representation, compression, and analysis in the basis function domain.

## How It's Best Learned
Work through decomposing a simple square wave into Fourier series, computing coefficients via inner products. Verify reconstruction using partial sums and observe Gibbs phenomenon.

## Common Misconceptions
- Thinking the same basis works optimally for all signals.
- Assuming non-orthogonal functions cannot form a basis.
- Confusing orthogonal bases with complete bases.

## Questions

```yaml
- question: "A signal needs to be decomposed using an orthogonal basis and you want to find c₃ — how much of basis function φ₃ is present. Which procedure correctly exploits orthogonality?"
  type: multiple-choice
  options:
    - "Compute the inner product of the signal with all other basis functions, then subtract their contributions to isolate c₃"
    - "Solve a system of N equations simultaneously, because changing one coefficient always affects the fit of the others"
    - "Compute ⟨x, φ₃⟩/‖φ₃‖² — orthogonality ensures this inner product isolates c₃ without reference to any other coefficient"
    - "Take the Fourier transform of the signal and read off c₃ from the spectrum at the corresponding frequency"
  answer: 2
  explanation: "Orthogonality means each basis function is independent of all others — zero inner product means no overlap. This independence is precisely what allows c₃ to be computed as a single inner product without involving any other coefficient. Option B describes what you'd need with a non-orthogonal basis, where coupling forces you to solve a system. Option A is a more laborious version of the wrong approach."

- question: "Why does using a non-orthogonal basis create problems for signal decomposition?"
  type: multiple-choice
  options:
    - "Non-orthogonal bases cannot span the full signal space, so exact reconstruction is impossible"
    - "Basis functions with nonzero inner products overlap, so their coefficients are coupled — extracting them requires solving a linear system, and noise spreads across all coefficients"
    - "Non-orthogonal decompositions always produce complex-valued coefficients even for real signals"
    - "Non-orthogonal bases require more basis functions to represent the same signal"
  answer: 1
  explanation: "Non-orthogonality means the basis functions have nonzero mutual overlap. Because they share 'content,' knowing how much of one is in the signal doesn't tell you how much of another is — the coefficients are coupled. Extracting them requires solving a linear system, and noise or errors in any coefficient propagate to all others. This is why orthogonal structures (Fourier, DCT, wavelets) dominate practical signal processing."

- question: "In an orthogonal basis, knowing how much of one basis function is present in a signal tells you nothing about how much of any other basis function is present."
  type: true-false
  answer: true
  explanation: "This is the direct consequence of zero inner product. Orthogonality means basis functions measure completely independent aspects of the signal. The coefficient c₃ captures only what φ₃ contributes; c₄ captures only what φ₄ contributes. There is no cross-contamination — which is exactly what allows each coefficient to be computed as a single isolated inner product."

- question: "Any basis that spans the full signal space (a complete basis) is also orthogonal."
  type: true-false
  answer: false
  explanation: "Completeness and orthogonality are independent properties. A basis is complete if it can represent any signal in the space; it is orthogonal if its basis functions have zero pairwise inner products. Non-orthogonal complete bases exist and can represent any signal — they just require solving coupled systems to extract coefficients. Orthogonality is an additional property that makes coefficient extraction efficient and noise-stable."

- question: "Explain why orthogonality is so valuable for signal decomposition. What goes wrong if you use a non-orthogonal basis instead?"
  type: short-answer
  answer: "Orthogonality means the basis functions have zero inner product — they measure independent aspects of the signal. This independence lets each coefficient be computed as a single inner product without coupling to any other coefficient. With a non-orthogonal basis, the functions overlap, so their coefficients are coupled: you must solve a system of equations to extract them, and errors or noise in one coefficient contaminate all others. Orthogonal bases eliminate this coupling, making decomposition stable, efficient, and amenable to independent coefficient editing — the foundation of filtering, compression, and spectral analysis."
  explanation: "The vector analogy is useful: orthogonal basis vectors in 2D let you project onto x̂ and ŷ independently. Non-orthogonal basis vectors mean projecting onto one axis shifts what you see on the other. The same logic applies to signals, just with inner products replacing dot products."
```

## Explainer

You already know how to describe a position in 2D space using coordinates: the vector (3, 4) means "3 units in the x̂ direction, 4 units in the ŷ direction." The basis {x̂, ŷ} is the pair of reference directions you are measuring against. A signal is not a position in 2D space — it is a function defined over time — but the mathematical structure is identical. A signal can be expressed as a "sum of reference shapes," where each reference shape is a **basis function** and each weight is a coefficient measuring how much of that shape is present. The Fourier series is the most famous example: it expresses any periodic signal as a weighted sum of sinusoids of different frequencies. The frequencies are the "directions," the Fourier coefficients are the "coordinates."

**Orthogonality** is the key property that makes this decomposition clean and efficient. Two basis functions φ_m(t) and φ_n(t) are orthogonal if their **inner product** ⟨φ_m, φ_n⟩ = ∫ φ_m(t) φ_n*(t) dt = 0. The inner product is the signal analog of the dot product for vectors — it measures "overlap" or "mutual content" between two functions. Zero inner product means the two functions measure completely independent aspects of the signal; knowing how much of φ_m is in x tells you nothing about how much of φ_n is in x. This independence is what allows coefficients to be computed one at a time: to find the coefficient c_n (how much of φ_n is in x), you simply compute ⟨x, φ_n⟩/‖φ_n‖². No system of equations, no cross-terms — each coefficient is isolated by orthogonality.

Contrast this with a non-orthogonal basis. If two basis functions overlap (nonzero inner product), then changing one coefficient affects how well the other fits the signal — the coefficients are coupled. Extracting them requires solving a linear system, and small errors or noise get spread across all coefficients. Orthogonal bases eliminate this coupling entirely, making decomposition stable, efficient, and numerically well-behaved. This is why signal processing, communications, and data compression so consistently use orthogonal structures: Fourier transforms, discrete cosine transforms, orthogonal wavelets, and orthogonal frequency-division multiplexing (OFDM) in wireless communications.

Familiar decompositions are all instances of this framework. The **Fourier series** uses {1, cos(nω₀t), sin(nω₀t)} — orthogonal over one period. The **DFT** uses complex exponentials {e^(j2πkn/N)} — orthogonal over N samples. **Haar wavelets** use step-function-like patterns that are orthogonal across different scales and translations. Each basis is optimized for different signal structures: sinusoids capture stationary, periodic signals cleanly; wavelets capture sharp edges and transients efficiently; principal component analysis finds the data-specific orthogonal basis that concentrates the most energy in the fewest components. A complete orthogonal basis spans the entire signal space — any signal can be exactly represented — whereas an incomplete basis can only approximate signals not in its span.

The practical payoff is signal compression and processing. If you decompose a signal into N coefficients using an orthogonal basis, and most of the signal energy concentrates in a few large coefficients while the rest are near zero, you can discard the small ones with minimal reconstruction error. JPEG image compression uses the discrete cosine transform (a relative of the Fourier transform) precisely because natural images tend to have energy concentrated at low spatial frequencies — most DCT coefficients are small and can be quantized coarsely or discarded. Signal filtering becomes coefficient editing: zero out the coefficients corresponding to unwanted frequency bands, then reconstruct. The choice of basis function determines what "frequency bands" mean and what can be selectively retained or discarded. Mastering orthogonal decomposition is mastering the language in which all of signal processing is written.
