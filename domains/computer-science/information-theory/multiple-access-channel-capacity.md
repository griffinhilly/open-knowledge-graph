---
id: multiple-access-channel-capacity
title: Multiple Access Channel Capacity
domain: computer-science
course: information-theory
prerequisites:
- id: multiple-access-channel
  type: hard
- id: channel-capacity
  type: hard
- id: mutual-information
  type: hard
builds-toward: []
tags:
- MAC capacity region
- sum rate
- polymatroid
- successive interference cancellation
- achievability
- converse
stage: expert
status: validated
---

# Multiple Access Channel Capacity

## Core Idea
The capacity region of a discrete memoryless multiple access channel (MAC) with K users is the set of rate tuples (R_1, ..., R_K) simultaneously achievable with error probability approaching zero. For general MACs, the region is characterized by the union of inner and outer bounds. The achievable region (inner bound) is defined by the rate constraints: sum_{i in S} R_i <= I(X_S; Y | X_{S^c}) for every non-empty subset S of users, where X_S is the input vector for users in S and X_{S^c} is the complement. The region is a polymatroid — a convex set with special combinatorial structure. The converse (outer bound) matches the inner bound for discrete memoryless MACs, fully characterizing capacity. For Gaussian MACs, the sum-capacity is log2(1 + (sum_i P_i)/N) and is achieved by the orthogonal multiple access of users alone or by non-orthogonal access combined with successive interference cancellation (SIC).

## Questions

```yaml
- question: "For a K-user MAC, the capacity region has 2^K - 1 constraints (one for each non-empty subset). For K=3, how many rate constraints define the region (not counting the trivial R_i >= 0)?"
  type: multiple-choice
  options:
    - "Three constraints: R_1+R_2+R_3, one for each sum"
    - "Seven constraints: R_1, R_2, R_3 (individual), R_1+R_2, R_1+R_3, R_2+R_3 (pairwise), and R_1+R_2+R_3 (sum)"
    - "Four constraints: individual rates and sum rate only"
    - "Ten constraints from all possible combinations"
  answer: 1
  explanation: "For K users, the MAC capacity region is a polymatroid with 2^K - 1 constraints. For K=3, this gives 7 constraints: three individual (R_1 <= I(X_1;Y|X_2,X_3), etc.), three pairwise sums (R_i+R_j <= I(X_i,X_j;Y|X_k), etc.), and one three-way sum (R_1+R_2+R_3 <= I(X_1,X_2,X_3;Y)). The constraint for subset S is sum_{i in S} R_i <= I(X_S; Y | X_{S^c}), which is the rate of users in S given perfect knowledge at the receiver of users outside S (as if they were decoded and subtracted). This polymatroidal structure generalizes beyond MACs to network information theory."

- question: "The sum-capacity of a Gaussian K-user MAC is log2(1 + (sum_i P_i) / N). This rate is achievable by TDMA (time division), so TDMA is optimal for Gaussian MACs."
  type: true-false
  answer: false
  explanation: "TDMA (each user gets 1/K of the time) achieves sum rate (1/K) * K * (1/2) log2(1 + K*P/N) = (1/2) log2(1 + K*P/N) for equal power P. With successive interference cancellation (SIC), the sum rate is (1/2) log2(1 + (K*P)/N), which is strictly larger than TDMA when K > 1. The SIC-achieving coding scheme allows all K users to transmit simultaneously (non-orthogonal access), and the receiver separates them via SIC instead of dividing time. The power factor grows from K*P (TDMA) to (sum of all powers) without time division, making SIC more efficient."

- question: "In successive interference cancellation (SIC), the decoding order matters for the individual rates R_i but not the sum-rate boundary. Explain why the sum rate is the same regardless of SIC order."
  type: short-answer
  answer: "The sum-rate constraint is R_1 + R_2 + ... + R_K <= I(X_1, X_2, ..., X_K; Y), which depends only on the joint information between all inputs and the output, independent of how the receiver processes them. Decoding order affects individual rates (which user decodes first, which second, etc.), yielding different rate tuples, but these tuples all lie on the same hyperplane in rate space. Different decoding orders correspond to different corner points of the capacity region's dominant face. Time-sharing (randomizing the decoding order) traces the full dominant face. Any point on the dominant face is achievable; points deeper in the region (below the dominant face) use probabilistic time-sharing between SIC orders."
  explanation: "This is a consequence of the polymatroidal structure: all rate points with the same sum lie on the same hyperplane, and the union of achievable rate points forms a convex polytope. The dominant face is the sum-rate boundary where all constraints are tight. Individual rates vary, but the aggregate (sum) is fixed once we commit to the sum-rate constraint."

- question: "In a Gaussian 2-user MAC with users having power constraints P_1 = 10, P_2 = 1, and noise power N = 1. User 1 decodes first (treating user 2 as noise). What is user 1's rate R_1 (in bits)?"
  type: multiple-choice
  options:
    - "R_1 = 0.5 * log2(1 + 10/(1+1)) = 0.5*log2(6) ≈ 1.29 bits"
    - "R_1 = 0.5 * log2(1 + 10/1) = 0.5*log2(11) ≈ 1.79 bits"
    - "R_1 = 0.5 * log2(1 + 1/1) = 0.5 bits"
    - "R_1 = 0.5 * log2((10+1)/(1)) = 0.5*log2(11) ≈ 1.79 bits"
  answer: 0
  explanation: "If user 1 decodes first, they must treat user 2's power P_2 = 1 as additional noise. The signal-to-interference-and-noise ratio is SNR = P_1/(P_2+N) = 10/(1+1) = 5, so R_1 = (1/2)*log2(1+5) = (1/2)*log2(6) ≈ 1.29 bits. If user 2 decoded first instead, user 2 would get R_2 = (1/2)*log2(1+1/1) = 0.5 bits, then user 1 would get R_1 = (1/2)*log2(1+10/1) ≈ 1.79 bits after SIC removes user 2. Different orders yield different rate tuples on the capacity region boundary."
```

## Explainer

The multiple access channel is the canonical multi-user uplink: multiple transmitters sending independent information to a single receiver over a shared noisy channel. The fundamental question is: what is the set of rate tuples (R_1, ..., R_K) that all users can simultaneously achieve with arbitrarily low error probability?

For a **discrete memoryless MAC** with transition probability p(y|x_1, ..., x_K), the capacity region is the set of rate tuples satisfying:
- For each non-empty subset S of users: sum_{i in S} R_i <= I(X_S; Y | X_{S^c})

where X_S denotes the inputs of users in subset S, and X_{S^c} denotes inputs of the other users. This characterization is both achievable (inner bound, by random coding) and optimal (converse, by information-theoretic counting arguments), so it is the exact capacity region.

The achievability uses a clever coding scheme: random coding over all possible (x_1^n, x_2^n, ..., x_K^n) codeword sequences, with joint typicality decoding. The receiver decodes users sequentially (successive interference cancellation): decode user 1 treating all others as noise, subtract user 1's signal from the received signal, then decode user 2, and so on. The rate constraint for user i when decoded with users in set S decoded before i is precisely I(X_i; Y | X_S), hence the polymatroidal structure.

For the **Gaussian MAC**, where Y = X_1 + X_2 + ... + X_K + Z with Z ~ N(0, N), the capacity region is characterized by:
- sum_{i in S} R_i <= (1/2) log2(1 + (sum_{i in S} P_i) / (N + sum_{i in S^c} P_i))

for all subsets S. The sum-rate (all users transmit) is (1/2) log2(1 + (sum_i P_i) / N). This is significantly larger than orthogonal multiple access (TDMA, FDMA) which achieves sum-rate (1/K) sum_i (1/2) log2(1 + P_i / N), because non-orthogonal schemes allow concurrent transmission with interference resolved at the receiver.

The capacity region is a **polymatroid**: a convex polytope with special combinatorial properties. It is invariant under certain transformations and has the monotonicity property that if (R_1, ..., R_K) is in the region, then so is any (R_1', ..., R_K') with R_i' <= R_i for all i. The dominant face (where all constraints are tight) traces the Pareto frontier of rates. Different SIC decoding orders yield different corner points on this frontier; time-sharing (randomizing the order) achieves any point on the dominant face.

The MAC capacity region was the first multi-user capacity problem fully solved and remains the gold standard in network information theory. Its complete characterization motivates the field: other multi-user scenarios (broadcast, interference, relay channels) are either incompletely solved or remain open, revealing gaps in our understanding of multi-user communication. Modern wireless systems (5G NOMA, CDMA) are designed based on these information-theoretic principles to approach MAC capacity limits.
