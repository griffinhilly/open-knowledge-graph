---
id: property-testing
title: Property Testing
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: sublinear-algorithms
  type: hard
- id: randomized-algorithms
  type: hard
- id: probability-rules-for-events
  type: soft
tags:
- property-testing
- sublinear-algorithms
- graph-properties
- epsilon-far
stage: expert
status: validated
---

# Property Testing

## Core Idea
Property testing asks whether an input has a specific property or is "far" from having it, using a number of queries sublinear in the input size. An input is epsilon-far from a property if more than an epsilon fraction of the input must change to satisfy the property. A property tester must accept inputs with the property (with probability >= 2/3) and reject inputs that are epsilon-far (with probability >= 2/3). Blum, Luby, and Rubinfeld initiated the field with a tester for linearity of Boolean functions using O(1/epsilon) queries. Goldreich, Goldwasser, and Ron showed that many graph properties (bipartiteness, k-colorability, having a large clique) are testable in the dense graph model with query complexity depending only on epsilon, independent of graph size. The field reveals a fundamental classification of properties by their query complexity.

## Questions

```yaml
- question: "The BLR (Blum-Luby-Rubinfeld) linearity test checks whether f: {0,1}^n -> {0,1} is a linear function by sampling random x, y and verifying f(x) + f(y) = f(x+y) (mod 2). If f is epsilon-far from every linear function, the test rejects with probability at least epsilon. Why does this work with O(1/epsilon) repetitions?"
  type: multiple-choice
  options:
    - "Each test independently has probability epsilon of detecting a nonlinearity, so O(1/epsilon) tests give constant detection probability by the coupon collector argument"
    - "If f is epsilon-far from linear, then for a random x,y the probability that f(x) + f(y) != f(x+y) is at least epsilon — each random test has at least epsilon probability of catching a violation, and O(1/epsilon) independent tests boost this to constant probability"
    - "The test exhaustively checks all pairs within a random subset of size 1/epsilon"
    - "The linearity test requires O(n/epsilon) queries, not O(1/epsilon)"
  answer: 1
  explanation: "The key theorem states: if f is epsilon-far from every linear function, then Pr[f(x) + f(y) != f(x+y)] >= epsilon for uniformly random x, y. This is not obvious — it requires Fourier analysis over GF(2)^n. Given this, each independent test catches a violation with probability >= epsilon. After O(1/epsilon) tests, the probability of catching at least one violation is 1 - (1-epsilon)^(1/epsilon) >= 1 - 1/e ≈ 0.63, which exceeds 2/3 with a slightly larger constant. The test uses O(1/epsilon) queries total (3 per test), independent of n."

- question: "In the dense graph model (adjacency matrix queries), every graph property expressible in first-order logic is testable with query complexity depending only on epsilon."
  type: true-false
  answer: true
  explanation: "This is a consequence of Szemerédi's regularity lemma and the work of Alon and Shapira. The regularity lemma decomposes any dense graph into a bounded number of 'pseudo-random' parts (the number depends only on epsilon). First-order properties can be evaluated on the regularity partition, which has bounded size. The tester samples O(1/epsilon^c) vertices (for some constant c depending on the property) and checks the property on the induced subgraph. The query complexity is enormous (due to the tower-function bounds in the regularity lemma) but independent of n. This is an existence result — the testers are often impractical but theoretically fundamental."

- question: "Explain the difference between one-sided and two-sided error in property testing, and give an example where one-sided error requires more queries than two-sided error."
  type: short-answer
  answer: "A one-sided tester always accepts inputs with the property (zero false negatives); a two-sided tester may reject valid inputs with probability up to 1/3 (both types may accept epsilon-far inputs with probability up to 1/3). For triangle-freeness in the dense graph model, two-sided testing requires O(1/epsilon^c) queries (via regularity-based sampling), while one-sided testing — which must find an actual triangle witness when rejecting — requires Theta(n^(1-delta)) queries for some delta depending on epsilon. The gap arises because one-sided testers must produce a certificate of violation (an explicit triangle), while two-sided testers can reject based on statistical evidence without finding an explicit witness."
  explanation: "The one-sided vs two-sided gap is dramatic for some properties. In the sparse graph model, bipartiteness is testable one-sided with O(sqrt(n) / epsilon^O(1)) queries but requires Omega(sqrt(n)) even for two-sided testing, so the gap is smaller. Understanding which properties have efficient one-sided testers is a major open direction."

- question: "Property testing in the bounded-degree graph model (where each vertex has degree at most d and queries are adjacency list queries) can always be done with query complexity independent of the graph size n."
  type: true-false
  answer: false
  explanation: "In the bounded-degree graph model, many important properties require query complexity that depends on n. For example, testing whether a bounded-degree graph is connected requires Omega(sqrt(n)) queries, and testing bipartiteness requires Omega(sqrt(n)) queries. This contrasts with the dense graph model where many properties have query complexity independent of n. The difference arises from information density: in a dense graph, each sampled vertex reveals O(n) adjacency bits, while in a bounded-degree graph each query reveals only O(d) bits. The graph model fundamentally affects testability."
```

## Explainer

Property testing sits at the intersection of sublinear algorithms and computational complexity. The question is precise: given query access to an input, can you distinguish "has property P" from "is epsilon-far from P" using few queries? The formal definition requires the tester to accept inputs with P with probability at least 2/3 and reject inputs epsilon-far from P with probability at least 2/3. Inputs that are close-but-not-satisfying may be handled either way — the definition only constrains the two extremes.

The BLR linearity test is the historical starting point. Given a function f: {0,1}^n -> {0,1}, the test picks random x, y and checks f(x) XOR f(y) = f(x XOR y). If f is linear, this always passes. If f is epsilon-far from linear, it fails with probability at least epsilon per test. The proof uses Fourier analysis: a function's distance from linearity equals the fraction of its Fourier weight outside the linear characters, and this fraction lower-bounds the test's rejection probability. Three queries per test, O(1/epsilon) tests, independent of n — this is sublinear in the most dramatic sense.

Graph property testing brings geometric and combinatorial structure into play. In the dense graph model (n^2 possible edges, adjacency matrix access), many properties are testable with query complexity independent of n. The regularity lemma is the key tool: it guarantees that any dense graph can be approximated by a partition of bounded size (depending only on epsilon), and properties that depend on the graph's global structure can be evaluated on this partition. In the bounded-degree (sparse) model, the picture is different: queries reveal less information per step, and many properties require sqrt(n) or more queries. Bipartiteness testing illustrates both models: O(poly(1/epsilon)) queries in the dense model, but Theta(sqrt(n)/epsilon^O(1)) in the bounded-degree model.

The classification of properties by query complexity is the central theoretical project. Which properties are testable with O(1/epsilon) queries? Which require poly(n) queries? The answers depend on the query model, the error type (one-sided vs two-sided), and the property's combinatorial structure. Recent breakthroughs have shown that in the dense graph model, the testable properties are essentially characterized by Szemerédi's regularity lemma, while in the sparse model, the picture is more complex and connects to local algorithms, distributed computing, and the theory of graph limits.
