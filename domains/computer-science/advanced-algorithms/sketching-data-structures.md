---
id: sketching-data-structures
title: Sketching Data Structures
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: streaming-algorithms
  type: hard
- id: randomized-algorithms
  type: hard
- id: universal-and-perfect-hashing
  type: soft
tags:
- sketching
- data-structures
- approximation
- linear-algebra-over-finite-fields
stage: expert
status: validated
---

# Sketching Data Structures

## Core Idea
Sketching compresses high-dimensional data into a small-space summary (a "sketch") that supports approximate queries. The sketch operates via random linear projections: map the data vector x to a much lower-dimensional sketch s = A * x (mod prime or in a vector space), where A is a random matrix chosen from a structured family. The count-min sketch uses independent hash functions for item frequency estimation; the Johnson-Lindenstrauss lemma shows that random projections preserve pairwise distances with high probability, enabling approximate nearest-neighbor search in subquadratic space. Min-hashing estimates Jaccard similarity between sets by tracking the minimum hash value. Sketch linearity (the sketch of a sum equals the sum of sketches) enables distributed computation and streaming. These structures trade off sketch size, space, update time, and query error in precise ways, offering guarantees on approximation quality and probability of failure.

## Questions

```yaml
- question: "The count-min sketch maintains a d-by-w matrix of counters. When an item x arrives with frequency update, each counter in row i is incremented at position h_i(x). Why is sketch merging (element-wise addition of two sketches) exact, and how does this enable distributed processing?"
  type: multiple-choice
  options:
    - "Merging is approximate; it introduces additional errors from the two sketches"
    - "The count-min sketch is a linear function of the frequency vector — sketch(f1 + f2) = sketch(f1) + sketch(f2) exactly because each counter independently sums the frequencies of items hashing to its position"
    - "Merging is exact only if the two sketches use the same random hash functions, but this is impractical for distributed systems"
    - "Merging requires re-hashing all items, which defeats the purpose of sketching"
  answer: 1
  explanation: "Each counter at position (i, j) tracks the sum of frequencies f_x for all items x such that h_i(x) = j. This is a linear operation on the frequency vector. When two sketches are merged (added element-wise), counter (i, j) in the merged sketch equals the sum of the two original counters, which equals the frequency sum from both input streams combined. Distributed count-min works by: partition the stream across compute nodes, each computes a sketch, send sketches to a central coordinator (O(d * w) bits each), sum them element-wise, and query the merged sketch. The result is identical to sketching the concatenated stream, making distribution seamless."

- question: "The Johnson-Lindenstrauss lemma states that random projections preserve all pairwise distances in a set of n points to within a (1 ± epsilon) multiplicative factor, using only O(log(n) / epsilon^2) dimensions. This enables approximate nearest-neighbor search in high-dimensional data."
  type: true-false
  answer: true
  explanation: "Given n points in d-dimensional space (d can be huge, like 10^6 for image features), choose a random d-by-k matrix where k = O(log(n) / epsilon^2). Project each point: p' = A * p. With high probability, ||p'_i - p'_j|| ≈ (1 ± epsilon) * ||p_i - p_j|| for all pairs (i,j). Since distances are preserved, nearest neighbors in the original space remain near-neighbors in the projection, enabling fast approximate nearest-neighbor via brute force in O(k * n^2) = O(log(n) / epsilon^2 * n^2) time instead of brute force in original space. For massive-scale problems, this dimension reduction is critical."

- question: "Min-hashing estimates the Jaccard similarity between two sets A and B. The method: choose k hash functions, for each set compute the minimum hash value across all elements, then estimate Jaccard similarity as the fraction of hash functions on which the two sets agree. Why does this work?"
  type: short-answer
  answer: "For a random hash function h, min(h(A)) = min(h(B)) if and only if the minimum hash value comes from the union A ∪ B and belongs to both A and B (since if only one set contains the minimum, they cannot agree). The probability that min(h(A)) = min(h(B)) equals the probability that the element yielding the minimum hash is in both sets, which is |A ∩ B| / |A ∪ B| = Jaccard(A, B). Each of k hash functions provides an independent estimate; the fraction that agree (estimate) converges to true Jaccard similarity. With k = O(1 / epsilon^2) functions, the estimate is (1 ± epsilon)-multiplicative with high probability."
  explanation: "Min-hashing is elegant: a single number (minimum hash value) per set encodes membership probability information. Multiple repetitions reduce variance. This is foundational for large-scale similarity search and set operations in databases."

- question: "Sketches are mergeable (can be added/combined) because they are linear functions of the input. This property enables one-shot distributed algorithms and streaming updates that would be impossible with non-linear summaries."
  type: true-false
  answer: true
  explanation: "A sketch is linear if sketch(f) = A * f (matrix-vector multiplication) for some fixed matrix A. Then sketch(f1 + f2) = A * (f1 + f2) = A * f1 + A * f2 = sketch(f1) + sketch(f2). Non-linear summaries like median or percentile are not mergeable: you cannot compute the median of a combined dataset by merging medians of subsets. Linearity is why count-min and min-hashing are so practical for distributed systems: compute sketches independently at nodes, transmit O(space) bits, merge, answer queries. This would be infeasible with non-linear statistics."
```

## Explainer

Sketches are a fundamental tool for handling massive data: when the data is too large to store or process in real time, summarize it into a small sketch that supports approximate queries. The sketch is a lossy compression of the data, carefully designed so that despite the information loss, the approximation guarantees are strong and well-understood.

The count-min sketch is the workhorse. It maintains a d-by-w matrix where w = O(1 / epsilon) (space to achieve relative error epsilon) and d = O(log(1 / delta)) (rows to achieve failure probability delta). For each arriving item with frequency, increment w positions (one per row). To query item frequency, return the minimum counter across rows. Why minimum? Because collisions only cause overcounting: each counter tracks not just the item's frequency but also frequencies of other items hashing to the same bucket. The minimum over independent hash functions is the tightest overestimate, and the union bound over d rows bounds the overestimation. Total space: O((1 / epsilon) * log(1 / delta)) counters, completely independent of the stream size n.

The Johnson-Lindenstrauss lemma lifts sketching from frequency estimation to geometry. In high-dimensional space (like neural network embeddings, which live in thousands of dimensions), random projections to just O(log(n) / epsilon^2) dimensions preserve all pairwise distances up to (1 ± epsilon) factors with high probability. This is counterintuitive: you can lose 99.9% of the dimensions and still preserve geometry. The proof uses concentration of measure: the projection of any vector has norm concentrated tightly around its expected value, and distances are sums of squared projections, which concentrate by Chebyshev's inequality.

Min-hashing is elegant for set similarity. Hash each element of a set, track the minimum hash value. Two sets' minimum hashes agree with probability equal to the Jaccard similarity (intersection over union). Repeat with k independent hash functions and average: estimate converges to true Jaccard. With k = O(1 / epsilon^2) functions, estimate is (1 ± epsilon)-approximation with high probability. Each set requires only k integers (64 bits each), making similarity search on massive collections feasible. This is the core of large-scale clustering and deduplication systems.

The unifying property is linearity: sketches are linear functions of the data (matrix-vector products, hash-based counts). This enables merging — the sketch of combined data equals the sum of sketches. Distributed processing becomes seamless: compute sketches at each node, transmit O(space) bits to a coordinator, sum sketches, answer global queries. This is impossible for non-linear statistics (median, percentile), which cannot be recovered from local summaries. Sketch design is an active field: how to trade space, time per update, and approximation error? New sketches (t-digest, HyperLogLog variants) optimize for specific error metrics or distributions, but all preserve the core structure: random projections + linearity + provable approximation bounds.
