---
id: randomized-complexity-classes
title: Randomized Algorithms and Probabilistic Complexity Classes
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: probabilistic-computation
  type: hard
- id: bpp-randomized-complexity
  type: hard
builds-toward:
- approximation-hardness-results
tags:
- randomized-algorithms
- BPP
- RP
- ZPP
stage: advanced
status: validated
---

# Randomized Algorithms and Probabilistic Complexity Classes

## Core Idea
Randomized Turing machines accept strings with bounded probability. RP (random polynomial time) languages can be verified with one-sided error; BPP (bounded-error probabilistic polynomial time) allows two-sided error. Surprisingly, BPP ⊆ PSPACE and likely BPP = P, suggesting randomness does not provide a fundamental advantage for polynomial-time computation, though random algorithms are practically powerful.

## Questions

```yaml
- question: "A randomized algorithm for graph isomorphism always correctly rejects non-isomorphic graphs, but may incorrectly reject isomorphic graphs with probability 1/4. This algorithm belongs to:"
  type: multiple-choice
  options:
    - "BPP, because the error probability is bounded below 1/2"
    - "RP, because it rejects all non-isomorphic graphs with probability 1"
    - "co-RP, because it never produces a false YES — it only possibly produces a false NO on YES instances"
    - "ZPP, because the expected running time is polynomial"
  answer: 2
  explanation: "co-RP has no false positives (no false YES answers) but allows false negatives (false NO answers). This algorithm always correctly rejects NO instances (non-isomorphic graphs) — so it never says 'isomorphic' when the graphs are not. But on YES instances (isomorphic graphs), it may incorrectly reject with probability 1/4. This is exactly the co-RP error profile: possible false NO, never false YES. RP is the mirror image: never false NO, possible false YES. BPP would allow both types of error."

- question: "If BPP = P were proven, the most direct implication would be:"
  type: multiple-choice
  options:
    - "Randomized algorithms provide no speedup of any kind — they solve exactly the same problems in exactly the same time as deterministic algorithms"
    - "Every problem solvable by a bounded-error randomized algorithm in polynomial time can also be solved by a deterministic algorithm in polynomial time"
    - "The P vs NP question would be resolved, since BPP ⊆ NP implies P = NP"
    - "Pseudorandom number generators cannot exist, since deterministic machines cannot simulate true randomness"
  answer: 1
  explanation: "BPP = P would mean that for every language in BPP, a deterministic polynomial-time algorithm exists. It would not eliminate the practical advantages of randomized algorithms (simplicity, smaller constants, ease of design), only the asymptotic class separation. It does not resolve P vs NP — BPP ⊆ PSPACE but BPP's relationship to NP is unclear. The result is believed to hold because pseudorandom generators can derandomize BPP algorithms, making explicit randomness computationally unnecessary."

- question: "BPP's error threshold of 2/3 is fundamental: changing it to 0.51 would strictly enlarge the class, admitting problems not in BPP with the 2/3 threshold."
  type: true-false
  answer: false
  explanation: "BPP is robust to the exact error threshold via error amplification. Running a BPP algorithm k times independently and taking the majority vote reduces the error to at most 2^(−Ω(k)) while only multiplying running time by k (a polynomial factor). Any constant error probability strictly below 1/2 defines the same class BPP, regardless of whether the threshold is 0.51, 2/3, or 0.99. The only requirement is that the correct answer is more likely than not — any such threshold is equivalent under amplification."

- question: "RP is contained in NP because a randomizing polynomial-time machine that accepts YES instances with probability ≥ 1/2 can be viewed as a nondeterministic machine where each nondeterministic choice corresponds to a coin flip."
  type: true-false
  answer: true
  explanation: "An NTM accepts if *any* computation path accepts. An RP machine accepts a YES instance on at least half its coin-flip sequences. If we treat each coin-flip sequence as a nondeterministic branch, then on YES instances at least one branch accepts — so the NTM accepts. On NO instances, the RP machine always rejects on every branch, so the NTM also rejects. This argument shows RP ⊆ NP. The inclusion is strict unless RP = NP, which would imply a dramatic collapse of the complexity hierarchy."

- question: "Explain the error amplification technique for BPP, and why it implies that the exact value of the error bound (as long as it's a constant below 1/2) does not affect what problems are in BPP."
  type: short-answer
  answer: "Error amplification works by running the BPP algorithm k independent times on the same input and taking the majority vote. If the algorithm has error probability ε < 1/2 on each run, then by the Chernoff bound the probability that the majority vote is wrong decreases exponentially in k — specifically to at most exp(−2k(1/2 − ε)²). Choosing k = O(n) gives error at most 2^(−Ω(n)) at only a polynomial cost. Since any constant ε < 1/2 can be amplified to negligible error in polynomial time, the class BPP is the same whether defined with error 1/3, 0.49, or 0.001 — all these thresholds define identical sets of languages."
  explanation: "The amplification argument also explains why BPP is considered a 'robust' class: unlike RP (which has asymmetric error) or ZPP (which must always be correct), BPP's two-sided error can always be driven to negligible levels by repetition. This robustness is why BPP, not RP, is the main model for practical randomized algorithms."
```

## Explainer

You already know that a **probabilistic Turing machine** is like an NTM but each nondeterministic branch is taken with equal probability, so the machine's computation is a random variable over its random coin flips. The key question is: how do you define "accepts" when there is a distribution over outcomes? Different answers produce different complexity classes, distinguished by the type and amount of error they tolerate.

**ZPP** (zero-error probabilistic polynomial time) is the most demanding: the machine always gives the correct answer, but is allowed to output "don't know" on some fraction of inputs, provided the expected running time is polynomial. In practice, ZPP = RP ∩ co-RP. **RP** (randomized polynomial time) allows one-sided error: if the answer is YES, the machine accepts with probability ≥ 1/2; if the answer is NO, the machine always rejects. You can never get a false NO, only a false YES. co-RP is the mirror image: no false YES, possible false NO. The asymmetry in RP makes it useful for primality testing: a composite is always detected, but a prime might occasionally be misclassified (though in practice this probability is made negligible).

**BPP** (bounded-error probabilistic polynomial time) is the most permissive of the main classes: the machine accepts correctly with probability ≥ 2/3 on both YES and NO inputs. The choice of 2/3 is arbitrary — by **error amplification** (running the machine k times independently and taking the majority vote), you can reduce the error probability to 2^{−k} at the cost of only a polynomial factor in k. This makes BPP robust: the exact threshold doesn't matter as long as it's bounded away from 1/2. BPP is widely believed to equal P, because pseudorandom number generators can apparently simulate randomness computationally — if one-way functions exist, then P = BPP.

The relationship between these classes and the deterministic hierarchy is: P ⊆ ZPP ⊆ RP ⊆ BPP ⊆ PSPACE, and RP ⊆ NP. Whether RP = NP or BPP = P are major open questions. Intuitively, BPP ⊆ PSPACE because you can deterministically enumerate all possible random strings and take the majority answer, which is in PSPACE. The practical lesson is that randomness is a powerful *engineering* tool — randomized algorithms are often simpler and faster than their deterministic counterparts — but theoretically, it likely provides no asymptotic computational advantage.
