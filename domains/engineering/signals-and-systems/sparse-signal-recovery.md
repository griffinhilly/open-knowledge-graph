---
id: sparse-signal-recovery
title: Sparse Signal Recovery and Basis Pursuit
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
tags:
- sparse-recovery
- basis-pursuit
- l1-minimization
- matching-pursuit
- dictionary-learning
stage: expert
status: validated
---

# Sparse Signal Recovery and Basis Pursuit

## Core Idea
Sparse signal recovery solves the inverse problem: given noisy measurements y = Ax + noise where x is unknown but sparse in some basis, find the sparsest x that explains y. The ℓ₀ problem (minimize count of nonzero coefficients) is combinatorial, but the convex relaxation (minimize ℓ₁ norm) provably recovers the true sparse signal under coherence and identifiability conditions. Basis Pursuit, Iterative Thresholding, and Matching Pursuit algorithms solve this efficiently. Applications include signal denoising, feature selection, source localization, and blind source separation where the number of sources is much smaller than the number of sensors.

## How It's Best Learned
Create a synthetic sparse signal (few nonzero coefficients in a dictionary of atoms), corrupt with noise, and solve the ℓ₁ minimization problem: minimize ||x||₁ subject to ||Ax − y||₂ ≤ noise_level (or minimize ||Ax − y||₂² + λ||x||₁ for a Lagrangian form). Use a convex solver and recover the original sparse coefficients. Vary the noise level, dictionary coherence, and sparsity to observe when ℓ₁ recovery succeeds or fails. Compare with ℓ₀ minimization (via exhaustive search or greedy methods) to confirm that ℓ₁ is a good convex proxy.

## Common Misconceptions
- Sparse recovery is only relevant for signals that are literally sparse (few nonzero samples); signals that are sparse in a transformed domain (Fourier, wavelets, learned dictionaries) also benefit.
- The ℓ₁ norm is chosen arbitrarily; it is the tightest convex lower bound of the ℓ₀ norm and has natural interpretations in robust statistics and information theory.
- Basis pursuit always recovers the true sparse solution; recovery is guaranteed only under conditions on the dictionary (coherence, restricted isometry) and noise level — adversarial or incoherent dictionaries can fail.

## Questions

```yaml
- question: "A signal x is sparse (K nonzero coefficients out of N) and observed as y = Ax + noise. To recover x via basis pursuit, you solve minimize ||x||₁ subject to ||Ax − y||₂ ≤ ε. Why is minimizing ||x||₁ (sum of absolute values) better than minimizing ||x||₀ (counting nonzeros) directly?"
  type: multiple-choice
  options:
    - "ℓ₀ minimization is nonconvex and NP-hard; ℓ₁ is convex and solvable in polynomial time. Under coherence conditions, they give the same answer"
    - "ℓ₁ is always better than ℓ₀; ℓ₀ is never a good sparsity measure"
    - "ℓ₁ requires fewer measurements than ℓ₀, violating the Nyquist theorem"
    - "ℓ₀ and ℓ₁ are equivalent; the choice is purely computational"
  answer: 0
  explanation: "ℓ₀ counts nonzeros directly (the true sparsity) but is a nonconvex function: the combinatorial search over all possible K-sparse supports is NP-hard. ℓ₁ (sum of absolute values) is convex: you minimize it via linear programming, polynomial-time solvable. Remarkably, for many realistic dictionaries and noise levels, the ℓ₁ solution equals the ℓ₀ solution — the convex relaxation is exact. This is not always guaranteed, but coherence and restricted isometry conditions ensure it in many cases. The success of basis pursuit hinges on this: we solve an intractable ℓ₀ problem via a tractable ℓ₁ proxy."
  
- question: "Iterative Hard Thresholding (IHT) recovers a sparse signal by repeating: update x ← shrink(x + A^T(y − Ax), K), where shrink(·, K) keeps the K largest magnitude coefficients and zeros the rest. Why does this work, and why is it faster than basis pursuit?"
  type: multiple-choice
  options:
    - "IHT directly enforces the cardinality constraint ||x||₀ = K, guaranteeing sparsity; it is faster because each iteration is simple thresholding, not solving a linear program"
    - "IHT is a gradient descent variant that projects onto the sparse set at each step, trading guaranteed convergence for computational speed"
    - "IHT only works for noise-free signals; in the presence of noise, basis pursuit is required"
    - "IHT and basis pursuit are mathematically equivalent; the difference is purely implementation"
  answer: 1
  explanation: "IHT is a projected gradient descent algorithm: you take a gradient step x ← x + A^T(y − Ax) (moving toward the data fit), then project back to the set of K-sparse vectors (keeping only the K largest magnitudes). This alternation between gradient steps and hard projection is faster than solving a linear program, especially for large-scale problems. However, IHT is not convex (the hard projection is nonconvex) — it only guarantees convergence to a local minimum if the RIP constant is small. Basis pursuit has global optimality guarantees (it's a convex problem), but solves a larger LP. Modern sparse recovery often uses IHT or similar greedy methods for speed, then validates against a convex solution."
  
- question: "Coherence of a dictionary A is the maximum absolute inner product between any two distinct atoms: μ(A) = max_{i≠j} |⟨a_i, a_j⟩|. High coherence (μ ≈ 1) makes sparse recovery harder; low coherence (μ ≈ 0) makes it easier. Why?"
  type: true-false
  answer: true
  explanation: "Low coherence means the dictionary atoms are nearly orthogonal — each atom has a unique 'signature' in measurement space. If two atoms are nearly collinear (high coherence), measurements cannot distinguish which one is present in the true sparse signal; two different sparse solutions (one using atom i, the other using atom j) produce nearly identical measurements. Basis pursuit or matching pursuit cannot disambiguate and may recover the wrong atom. Low coherence ensures that atoms are distinguishable, allowing recovery algorithms to identify which atoms are active. This is why incoherent dictionaries (random dictionaries, orthogonal dictionaries) are preferred."
  
- question: "In a noisy setting, basis pursuit (minimize ||x||₁ subject to ||Ax − y||₂ ≤ ε) can sometimes recover a non-sparse solution that fits the data. What prevents this, and when does basis pursuit fail?"
  type: true-false
  answer: true
  explanation: "Basis pursuit prefers sparse solutions: minimizing ||x||₁ penalizes spreading energy across many atoms. Even with noise, a sparse solution with small ℓ₁ norm will be preferred over a dense solution with the same data fit. However, if the true signal is genuinely non-sparse, or if the dictionary is highly coherent, basis pursuit may fail to recover it. Failure modes: (1) the noise level ε is too large (more uncertainty than signal content); (2) the dictionary is incoherent or the signal structure is not well-represented; (3) the true signal is not sparse. In such cases, other priors (structured sparsity, group sparsity, low-rank structure) may be needed."
  
- question: "Explain the relationship between the coherence μ(A) and the minimum sparsity level K_min such that basis pursuit recovers K-sparse signals. Why does reducing coherence allow recovery of sparser signals?"
  type: short-answer
  answer: "The theoretical guarantee is: if K < 1/(2μ(A)), basis pursuit recovers any K-sparse signal from noiseless measurements. Low coherence μ ≈ 0 allows K to be close to 1 (very sparse signals are recoverable), while high coherence μ ≈ 1 requires K < 1/2 (only half-sparse signals are recoverable, which is weak). The intuition: coherence measures dictionary redundancy. If atoms are similar (high μ), the algorithm cannot distinguish which atoms are active, limiting recovery to cases where sparsity is very low (only a few atoms possible). If atoms are dissimilar (low μ), even moderately sparse signals are identifiable. Modern dictionaries are designed with low coherence: random projections (random Gaussian entries), Fourier + wavelets (complementary time-frequency structures), or learned dictionaries optimized for coherence."
  explanation: "This quantifies the trade-off: larger, more redundant dictionaries (higher coherence) have better signal representation capability (can express many signals) but worse identifiability (hard to determine which atoms were used). Sparser recovery (smaller K) requires more orthogonal dictionaries. In practice, you either accept slightly higher coherence (dictionaries represent signals better but need higher sparsity for guaranteed recovery), or use learned dictionaries optimized jointly for representation and coherence."
```

## Explainer

From your study of linear algebra and Fourier analysis, you know how to represent signals in different bases and transform between domains. **Sparse recovery** takes this further: given observations of a signal in one domain, find the sparsest representation in another domain.

The problem is concrete: you have measurements y (from a sensor or compressive sampling), a dictionary of atoms A (a matrix where each column is a possible signal component), and you want to find the sparsest x (fewest nonzero coefficients) such that Ax ≈ y. This is the **sparse coding problem**. If there is no noise, you solve exactly: Ax = y. If y is noisy or the system is underdetermined, you regularize with a sparsity term.

**The ℓ₀ vs ℓ₁ tradeoff** is the core of sparse recovery. Minimizing ||x||₀ (the count of nonzeros, "cardinality") is the true sparsity measure, but it is a combinatorial optimization problem: there are C(N,K) possible sparse supports (positions of nonzeros), and finding the best one requires checking all or using branch-and-bound, which is NP-hard. **Basis Pursuit** replaces ℓ₀ with its convex surrogate ℓ₁: minimize ||x||₁ subject to Ax = y (or Ax ≈ y with noise). This is a linear program, solvable by interior-point methods in polynomial time. The miracle of compressive sensing and sparse recovery is that under conditions on A (incoherence, restricted isometry), the ℓ₁ solution equals the ℓ₀ solution — you solve a hard problem via convex optimization.

**Conditions for recovery** are encoded in two properties: **Mutual Coherence** μ(A) (how much dictionary atoms overlap) and **Restricted Isometry Property** (how well A preserves sparse signals). Low coherence μ means atoms are nearly orthogonal and thus distinguishable in measurement space. If μ is small, you can recover any K-sparse signal where K < 1/(2μ). Structured dictionaries (Fourier, wavelets, random Gaussian) have low coherence by design.

**Algorithms** for sparse recovery range from convex (basis pursuit, cvx solvers) to greedy (Matching Pursuit, Orthogonal Matching Pursuit). **Orthogonal Matching Pursuit (OMP)** is intuitive: iteratively find the atom with the highest correlation to the current residual, add it to the support, update the residual, and repeat until the residual is small. OMP is faster than basis pursuit (no LP solver) but slightly suboptimal — it is greedy and does not account for measurement noise as carefully. **Iterative Thresholding** alternates between a gradient descent step (x ← x + A^T(y − Ax)) and a hard or soft thresholding operation (keep K largest or shrink by λ). Hard thresholding (keeping K largest) is computationally simple and converges if the RIP constant is small.

**Applications** are broad: **signal denoising** (represent as sparse in wavelets, shrink small coefficients), **feature selection** (in regression, add ℓ₁ penalty to select few features), **source localization** (many microphones, few active sources), **radar** (map K targets from M measurements), **matrix completion** (fill missing entries by assuming low-rank, which is sparse in singular value domain). Many machine learning problems are implicitly sparse recovery: regularized regression (LASSO, elastic net) is basis pursuit in the feature space.

The **limits** of sparse recovery are when the dictionary is wrong (the true signal is not sparse in any known basis), when coherence is high (atoms overlap, indistinguishable in measurements), or when noise is large. Modern extensions address these: **dictionary learning** (learn the atoms from data rather than use fixed dictionaries), **structured sparsity** (groups of atoms must be active together, e.g., image blocks), **low-rank models** (exploit rank structure, not just sparsity), and **deep learning** (learn end-to-end mappings from measurements to signals, implicitly learning both dictionary and recovery algorithm).
