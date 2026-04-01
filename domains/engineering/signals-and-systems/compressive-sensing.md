---
id: compressive-sensing
title: Compressive Sensing and Sparse Recovery
domain: engineering
course: signals-and-systems
prerequisites:
- id: sparse-signal-recovery
  type: hard
- id: fourier-transform-definition-properties
  type: hard
tags:
- compressive-sensing
- sparse-recovery
- basis-pursuit
- random-sampling
- restricted-isometry-property
stage: expert
status: validated
---

# Compressive Sensing and Sparse Recovery

## Core Idea
Compressive sensing (CS) reconstructs sparse signals from far fewer measurements than traditional Nyquist sampling requires. Instead of sampling at the signal's Nyquist rate and compressing, CS acquires only M random projections of the signal (where M ≪ N, the signal length), then solves a convex optimization to recover the original signal. Recovery is guaranteed if the signal is sparse (few nonzero coefficients) in some basis and the measurement matrix satisfies the Restricted Isometry Property (RIP): random matrices (Gaussian, binary, or structured) satisfy RIP with high probability. Algorithms include Basis Pursuit (convex), Greedy methods (OMP, CoSaMP), and approximate message passing (AMP).

## How It's Best Learned
Generate a sparse signal (few nonzero coefficients in a Fourier or wavelet basis). Acquire M random linear measurements (dot products with random vectors), where M is much smaller than the signal length. Solve the basis pursuit problem (minimize ℓ₁ norm of coefficients subject to measurement constraints) using a convex solver (CVX, CVXPY). Observe perfect or near-perfect reconstruction. Vary M and sparsity to find the transition where recovery fails, confirming the phase diagram: recovery succeeds if M/N > C·K·log(N/K) where K is sparsity.

## Common Misconceptions
- Compressive sensing violates the Nyquist theorem; it does not — CS acquires information at a different rate (projection rate) than Nyquist sampling, and reconstructs by exploiting sparsity, which is additional structure the Nyquist theorem does not assume.
- Any random measurement matrix guarantees recovery; structured matrices (Fourier subsampled, circulant) work but are suboptimal compared to unstructured (Gaussian) matrices, which satisfy RIP more reliably.
- Basis pursuit (convex ℓ₁ minimization) always recovers the sparse signal; it recovers the *sparsest* solution consistent with measurements, which is the true signal if RIP holds and noise is small.

## Questions

```yaml
- question: "In compressive sensing, you measure a K-sparse signal using M random measurements where M = 2K. Can you always recover the signal exactly?"
  type: multiple-choice
  options:
    - "Yes, M = 2K is sufficient because 2K measurements can determine 2K unknowns (the support of the K-sparse signal and the K nonzero values)"
    - "Not necessarily — recovery requires M > C·K·log(N/K) for some constant C > 1, and M = 2K may not satisfy this if N is large relative to K"
    - "No, because random measurements discard information and violate the uncertainty principle"
    - "Yes, but only if the signal is Gaussian; for deterministic signals, more measurements are needed"
  answer: 1
  explanation: "Recovery requires the measurement matrix to satisfy RIP, which for random matrices holds with high probability only if M > C·K·log(N/K). The logarithmic factor log(N/K) is crucial: for a long signal (large N) with few nonzero coefficients (small K), many measurements are still needed to distinguish the sparse signal from all possible random combinations of the same sparsity. M = 2K is appealing intuitively but insufficient unless N is small or K is large. The log factor reflects the information-theoretic cost of not knowing which K positions are nonzero."
  
- question: "The Restricted Isometry Property (RIP) with isometry constant δ_K requires that (1−δ_K)||x||² ≤ ||Φx||² ≤ (1+δ_K)||x||² for all K-sparse vectors x. Why is this property sufficient for basis pursuit recovery?"
  type: multiple-choice
  options:
    - "RIP ensures the measurement matrix preserves distances, so sparse signals cannot collide under measurement"
    - "RIP guarantees that the ℓ₁-norm minimization (basis pursuit) will favor the original sparse solution over any other signal consistent with the measurements, because the true sparse signal is the unique minimum"
    - "RIP is necessary but not sufficient; additional conditions on noise are required"
    - "RIP applies only to Gaussian random matrices, not structured matrices"
  answer: 1
  explanation: "RIP says the measurement matrix acts like a quasi-isometry on sparse vectors: it preserves their geometry. If x is K-sparse and Φx is measured, then any other K-sparse signal x' with Φx' = Φx must have ||Φ(x−x')||² = 0. But RIP says ||Φ(x−x')||² ≥ (1−δ_K)||x−x'||², implying ||x−x'|| = 0, so x = x'. This means the true sparse signal is the unique K-sparse vector consistent with the measurements. Among all vectors consistent with the measurements, basis pursuit's ℓ₁ minimization will find the sparsest, which must be the true signal. RIP with small δ_K ≈ 0.3 ensures stable recovery with noise."
  
- question: "Compressive sensing theory assumes the signal is sparse. If the signal is not sparse in any known basis, can compressive sensing still recover it?"
  type: true-false
  answer: false
  explanation: "If a signal is not sparse in any basis (truly random or chaotic), then observing any subset of its samples contains little information about the rest, and recovery is impossible — the information-theoretic limits apply. Compressive sensing gains its power from sparsity. However, many real signals (audio, images, video) are sparse or nearly sparse in learned bases (wavelets, dictionary atoms, neural network encodings), and CS applies there. For non-sparse signals, traditional Nyquist sampling at the signal bandwidth is necessary."
  
- question: "In a compressive sensing application, you use a structured measurement matrix (e.g., Fourier subsampling: measure only M randomly chosen Fourier coefficients) instead of a Gaussian random matrix. Is performance as good?"
  type: true-false
  answer: false
  explanation: "Structured matrices are computationally efficient and fast to apply (no need to compute M arbitrary random dot products), but they do not satisfy RIP as reliably as unstructured Gaussian matrices. Fourier subsampling works well for signals sparse in time (few nonzero samples), but if the signal is sparse in frequency (few nonzero Fourier coefficients), then subsampling Fourier coefficients can alias and cause recovery to fail. Modern research uses structured matrices with theoretical guarantees (circulant matrices, binary matrices with specific properties), but as a rule, unstructured random matrices offer the best guaranteed performance for arbitrary sparse signals."
  
- question: "Explain the phase diagram of compressive sensing: why does recovery succeed when M/N > C·K·log(N/K) but fail when M/N is below this threshold? What does the log(N/K) factor mean intuitively?"
  type: short-answer
  answer: "The measurement rate M/N must exceed a critical threshold that depends on sparsity K and signal length N. Below the threshold, the subspace of solutions consistent with the measurements is large (many K-sparse signals fit the same measurements), and basis pursuit cannot distinguish the true signal. Above the threshold, RIP is satisfied and the true signal is the unique sparsest solution. The log(N/K) factor comes from information theory: to identify which K positions (out of N) are nonzero requires log(N choose K) ≈ K·log(N/K) bits of information. Since each measurement provides ≈ 1 bit of information (a random inner product), you need M ≈ K·log(N/K) measurements to encode the support. The constant C ≈ 1.0–1.5 depends on the RIP quality; typical statements use C ≈ 3–5 to be conservative."
  explanation: "This phase transition is sharp: below the threshold, recovery almost surely fails; above it, almost surely succeeds. It is one of the most beautiful results in signal processing, because it gives a principled way to choose M. In practice, you solve basis pursuit anyway and check whether recovery is accurate (compare to known signal or use cross-validation), but the phase diagram provides a rough guideline."
```

## Explainer

The Nyquist sampling theorem says you must sample a signal at twice its bandwidth to recover it. If a signal occupies a bandwidth of 100 MHz, you need 200 million samples per second. But many real signals are sparse: an audio recording might have 1000 frequency components spread across a spectrum of 1 million points; an image might have 90% of its pixels below noise threshold after wavelet transform. **Compressive sensing** exploits this sparsity to dramatically reduce the number of measurements needed.

The core idea: instead of sampling the signal and then compressing (discarding most values), **measure and compress simultaneously**. Take M random linear projections (random dot products) of the signal, where M is much smaller than N (the signal length): y = Φx, where Φ is M × N with M ≪ N. Since we have fewer equations than unknowns, the system is underdetermined. But if x is sparse (most coefficients zero in some basis), we can solve for x by finding the sparsest solution consistent with y — the unique solution is the sparse vector.

**The sparsity model** is crucial. The signal x may not be sparse in the time domain, but it is sparse in some basis Ψ: x = Ψs where s is sparse (K nonzero coefficients). Measuring y = Φx = ΦΨs reveals s (up to a change of variables). You then recover s by solving: minimize ||s||₀ (count of nonzero entries) subject to ΦΨs = y. This is combinatorial (NP-hard), but a convex relaxation works: minimize ||s||₁ (sum of absolute values) subject to ΦΨs = y. This **Basis Pursuit** problem is a linear program, solvable in polynomial time. Remarkably, under conditions on Φ and s's sparsity, the ℓ₁ solution is identical to the ℓ₀ solution — you can solve a hard problem by convex optimization.

**The Restricted Isometry Property (RIP)** is the condition that makes this work. A matrix Φ satisfies RIP of order K with constant δ_K if all K-sparse vectors are approximately preserved: (1−δ_K)||s||² ≤ ||Φs||² ≤ (1+δ_K)||s||² for all K-sparse s. Intuitively, Φ acts like an approximate isometry (distance-preserving) on sparse vectors. Random matrices (Gaussian entries, binary ±1) satisfy RIP with high probability when M > C·K·log(N/K). This is why randomness is beneficial: a worst-case adversarial matrix would map multiple distinct K-sparse signals to the same measurement, making recovery impossible, but random matrices almost never do this.

**Practical algorithms** beyond basis pursuit include **greedy methods** like Orthogonal Matching Pursuit (OMP): iteratively identify the nonzero support one coordinate at a time by finding which dictionary atom best explains the measurement residual. OMP is faster than basis pursuit (no NLP solver needed) but slightly suboptimal — it doesn't account for measurement noise as elegantly. **Approximate Message Passing (AMP)** is a newer iterative algorithm inspired by statistical physics, giving near-optimal reconstruction with lower computational cost.

**Applications** span MRI (acquire fewer k-space samples, reconstruct with sparsity in wavelet domain), radar (reconstruct target echoes from compressed pulse returns), astronomy (reconstruct images from telescope data), and machine learning (recover sparse feature vectors). The catch: you must be in a regime where M ≤ N but M is close to the information-theoretic limit K·log(N/K), which requires K ≪ N (signals genuinely sparse). For nearly-random signals or signals sparse only in learned, data-dependent bases, CS gains diminish. Modern extensions combine CS with deep learning: train a neural network to map compressed measurements directly to signal reconstructions, achieving better performance than model-based approaches for complex, learned sparsity structures.
