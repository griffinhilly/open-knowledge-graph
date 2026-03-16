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

## Explainer

You already know how to describe a position in 2D space using coordinates: the vector (3, 4) means "3 units in the x̂ direction, 4 units in the ŷ direction." The basis {x̂, ŷ} is the pair of reference directions you are measuring against. A signal is not a position in 2D space — it is a function defined over time — but the mathematical structure is identical. A signal can be expressed as a "sum of reference shapes," where each reference shape is a **basis function** and each weight is a coefficient measuring how much of that shape is present. The Fourier series is the most famous example: it expresses any periodic signal as a weighted sum of sinusoids of different frequencies. The frequencies are the "directions," the Fourier coefficients are the "coordinates."

**Orthogonality** is the key property that makes this decomposition clean and efficient. Two basis functions φ_m(t) and φ_n(t) are orthogonal if their **inner product** ⟨φ_m, φ_n⟩ = ∫ φ_m(t) φ_n*(t) dt = 0. The inner product is the signal analog of the dot product for vectors — it measures "overlap" or "mutual content" between two functions. Zero inner product means the two functions measure completely independent aspects of the signal; knowing how much of φ_m is in x tells you nothing about how much of φ_n is in x. This independence is what allows coefficients to be computed one at a time: to find the coefficient c_n (how much of φ_n is in x), you simply compute ⟨x, φ_n⟩/‖φ_n‖². No system of equations, no cross-terms — each coefficient is isolated by orthogonality.

Contrast this with a non-orthogonal basis. If two basis functions overlap (nonzero inner product), then changing one coefficient affects how well the other fits the signal — the coefficients are coupled. Extracting them requires solving a linear system, and small errors or noise get spread across all coefficients. Orthogonal bases eliminate this coupling entirely, making decomposition stable, efficient, and numerically well-behaved. This is why signal processing, communications, and data compression so consistently use orthogonal structures: Fourier transforms, discrete cosine transforms, orthogonal wavelets, and orthogonal frequency-division multiplexing (OFDM) in wireless communications.

Familiar decompositions are all instances of this framework. The **Fourier series** uses {1, cos(nω₀t), sin(nω₀t)} — orthogonal over one period. The **DFT** uses complex exponentials {e^(j2πkn/N)} — orthogonal over N samples. **Haar wavelets** use step-function-like patterns that are orthogonal across different scales and translations. Each basis is optimized for different signal structures: sinusoids capture stationary, periodic signals cleanly; wavelets capture sharp edges and transients efficiently; principal component analysis finds the data-specific orthogonal basis that concentrates the most energy in the fewest components. A complete orthogonal basis spans the entire signal space — any signal can be exactly represented — whereas an incomplete basis can only approximate signals not in its span.

The practical payoff is signal compression and processing. If you decompose a signal into N coefficients using an orthogonal basis, and most of the signal energy concentrates in a few large coefficients while the rest are near zero, you can discard the small ones with minimal reconstruction error. JPEG image compression uses the discrete cosine transform (a relative of the Fourier transform) precisely because natural images tend to have energy concentrated at low spatial frequencies — most DCT coefficients are small and can be quantized coarsely or discarded. Signal filtering becomes coefficient editing: zero out the coefficients corresponding to unwanted frequency bands, then reconstruct. The choice of basis function determines what "frequency bands" mean and what can be selectively retained or discarded. Mastering orthogonal decomposition is mastering the language in which all of signal processing is written.
