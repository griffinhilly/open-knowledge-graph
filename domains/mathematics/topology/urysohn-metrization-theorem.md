---
id: urysohn-metrization-theorem
title: Urysohn Metrization Theorem
domain: mathematics
course: topology
prerequisites:
- id: normality-t4-axiom
  type: hard
- id: second-countable-spaces
  type: soft
tags:
- metrization
- urysohn
stage: advanced
status: validated
---

# Urysohn Metrization Theorem

## Core Idea
A second-countable normal space is metrizable (its topology comes from a metric). This characterizes when abstract topological spaces are actually metric spaces. The theorem shows such spaces embed into ℓ²(ℕ), a Hilbert space with a natural metric. Provides a powerful criterion for recognizing metric spaces.

## Questions

```yaml
- question: "A topological space X is normal but not second-countable. What does the Urysohn Metrization Theorem tell you about X?"
  type: multiple-choice
  options:
    - "X is metrizable, since normality alone is sufficient"
    - "X is not metrizable, since normality alone is insufficient"
    - "The theorem is silent — it gives no conclusion about X's metrizability"
    - "X is metrizable only if it is also Hausdorff"
  answer: 2
  explanation: "The Urysohn Metrization Theorem states that second-countable AND normal implies metrizable. It is a sufficient condition requiring both hypotheses. If one hypothesis is missing, the theorem simply does not apply — it says nothing about whether X is or is not metrizable. A normal space without second-countability may or may not be metrizable; the theorem is silent. (The long line is a classic example of a normal, non-second-countable, non-metrizable space.)"

- question: "What does it mean to say that a topological space X is metrizable?"
  type: multiple-choice
  options:
    - "X has a distance function, but it may generate a coarser topology than the one given"
    - "X can be given a metric that generates a topology that agrees with the given topology"
    - "X embeds into some metric space, possibly losing some open sets in the process"
    - "Every continuous function on X extends to a metric space"
  answer: 1
  explanation: "Metrization is precise: a metric must exist on X such that the topology it generates is exactly the given topology — not merely related to it, but identical. A coarser or finer metric topology would not count. The key point is that an abstract topological space defined by open sets turns out to be secretly described by a distance function. Options A and C describe weaker conditions (the topology might not be recovered); option D is unrelated."

- question: "In the proof of the Urysohn Metrization Theorem, normality is used to construct Urysohn functions. This means normality guarantees that for any two disjoint closed sets, there exists a continuous function separating them."
  type: true-false
  answer: true
  explanation: "This is precisely the content of Urysohn's lemma: a space is normal if and only if for any two disjoint closed sets C and D, there is a continuous f : X → [0,1] with f = 0 on C and f = 1 on D. Normality is the exact topological condition that makes such separator functions exist, and the metrization proof assembles a countable family of these functions to build the embedding into ℓ²(ℕ)."

- question: "Every second-countable space is metrizable, regardless of whether it is normal."
  type: true-false
  answer: false
  explanation: "Second-countability alone is not sufficient for metrizability. The Urysohn Metrization Theorem requires both second-countability and normality. A second-countable space that fails normality need not be metrizable — the two conditions work together, with second-countability providing a countable base for building the function family, and normality providing the Urysohn functions themselves. Dropping either condition breaks the argument."

- question: "Explain why the Urysohn Metrization Theorem uses an embedding into ℓ²(ℕ), and what role second-countability plays in making this embedding possible."
  type: short-answer
  answer: "Second-countability guarantees a countable base {U₁, U₂, …}, which yields a countable collection of pairs (Uᵢ, Uⱼ) with cl(Uᵢ) ⊆ Uⱼ. Normality then produces a Urysohn function for each such pair. Because the collection of functions is countable, the map x ↦ (f₁(x), f₂(x), …) lands in ℓ²(ℕ), a separable Hilbert space with a natural metric. Pulling back the ℓ² metric gives the desired metric on X. Without second-countability, the function family might be uncountable, making the ℓ²(ℕ) embedding unavailable."
  explanation: "The embedding strategy — mapping X into a known metric space and pulling back the metric — requires that the coordinate functions form a countable sequence. Second-countability is exactly the condition that makes this countability available. This is why the theorem fails without it: you cannot assemble an uncountable family of functions into coordinates of ℓ²(ℕ). The two hypotheses are not redundant; they play complementary roles in the proof."
```

## Explainer

Start with the problem. A topological space is defined abstractly by its open sets, with no requirement that distances between points exist. Metric spaces are special: they carry a distance function d(x, y) satisfying the triangle inequality, and their topology is generated by open balls. The question is: when does an abstractly defined topological space secretly have an underlying metric? **Metrization** means finding a metric on the space that generates exactly the given topology — not just any metric, but one that recovers all the open sets you started with.

You know two prerequisites. **Normality** (the T4 axiom) says that disjoint closed sets can be separated by disjoint open sets. This is a strong separation condition: any two "incompatible" closed pieces of the space can be pushed apart. **Second-countability** says the topology has a countable base — a countable collection of open sets from which every open set is built by unions. Euclidean spaces are second-countable (rational-radius balls centered at rational points form a countable base). The **Urysohn Metrization Theorem** says these two conditions together guarantee metrization.

The proof works in two steps, each using the two hypotheses in turn. First, normality gives you **Urysohn functions**: for any two disjoint closed sets C and D, there exists a continuous function f : X → [0,1] with f = 0 on C and f = 1 on D. Normality is exactly the condition that makes such separator functions exist. Second, second-countability gives you a countable base {U₁, U₂, U₃, …}, and for each pair (Uᵢ, Uj) with cl(Uᵢ) ⊆ Uj, normality produces a Urysohn function fᵢⱼ. Collecting all such functions gives a countable family. This family defines an embedding X → ℓ²(ℕ) by x ↦ (fᵢⱼ(x)), and the metric pulled back from ℓ² is the desired metric on X.

The theorem draws a sharp boundary between abstract topology and metric topology. All metric spaces are normal and, if second-countable, satisfy the theorem's hypotheses. So second-countable normal spaces are exactly those topological spaces that "look like" metric spaces, even when presented abstractly. Spaces that are normal but not second-countable (like the long line) may fail to be metrizable. Spaces that are second-countable but not normal (unusual but possible) also fail. The theorem is an "if and only if" in the second-countable case: for second-countable Hausdorff spaces, normality is equivalent to metrizability. This makes it one of the most satisfying classification results in topology — a clean algebraic-separation condition translating into a geometric distance structure.
