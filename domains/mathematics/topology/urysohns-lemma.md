---
id: urysohns-lemma
title: Urysohn's Lemma
domain: mathematics
course: topology
prerequisites:
- id: normal-spaces
  type: hard
- id: continuous-functions-topology
  type: hard
builds-toward:
- tietze-extension-theorem
- metrization-theorems
tags:
- urysohn
- lemma
stage: advanced
status: validated
---

# Urysohn's Lemma

## Core Idea
In a normal space, if F and G are disjoint closed sets, there exists a continuous function f: X → [0,1] with f(F) = {0} and f(G) = {1}.

## Questions

```yaml
- question: "What is the key construction used in the proof of Urysohn's Lemma to build the separating function f: X → [0,1]?"
  type: multiple-choice
  options:
    - "For each rational r ∈ [0,1], define U(r) = {x : d(x, F) < r} using the metric structure of the space"
    - "Use the axiom of choice to select a point between F and G in each open set, then define f by interpolation"
    - "For each dyadic rational r ∈ [0,1], construct a nested family of open sets U(r) using normality at each step, then define f(x) = inf{r : x ∈ U(r)}"
    - "Define f(x) = 0 on F and f(x) = 1 on G, then extend continuously using the Tietze Extension Theorem"
  answer: 2
  explanation: "The proof doesn't use a metric (the space need not be metrizable) and doesn't assume the Tietze Extension Theorem (which Urysohn's Lemma implies, not the other way around). The key construction is a dyadic family: for each k/2ⁿ ∈ [0,1], use normality to insert an open set U(k/2ⁿ) between previously constructed sets, building a nested family indexed by a dense set. The function f(x) = inf{r : x ∈ U(r)} is then continuous because the nested structure provides enough 'checkpoints' to force continuity everywhere."

- question: "Urysohn's Lemma concludes that in a normal space, disjoint closed sets can be separated by a continuous function. Why is this stronger than the definition of normality itself?"
  type: multiple-choice
  options:
    - "It is not stronger — normal spaces are defined precisely by the existence of such separating functions"
    - "It is stronger because normality only guarantees disjoint open neighborhoods around the closed sets, while Urysohn's Lemma constructs a globally continuous function that interpolates between them throughout the entire space"
    - "It is stronger because Urysohn's Lemma applies to all topological spaces, while normality is a special axiom"
    - "It is stronger because continuous functions are harder to construct than open sets in metric spaces"
  answer: 1
  explanation: "Normality is defined as: for any two disjoint closed sets, there exist disjoint open sets containing them. This is a purely set-theoretic separation condition — it gives you two open sets that don't overlap. Urysohn's Lemma goes further: it builds a continuous function that equals 0 on one closed set and 1 on the other, varying continuously throughout the entire space. Building a globally continuous function with prescribed values requires coordinating the topology across the whole space, not just finding two disjoint open sets. The lemma reveals that normality is strong enough to support this function-theoretic construction."

- question: "Urysohn's Lemma applies to most Hausdorff spaces, since normal spaces are simply Hausdorff spaces with an additional separation property."
  type: true-false
  answer: false
  explanation: "Not all Hausdorff spaces are normal. Hausdorff (T₂) requires that any two distinct points can be separated by disjoint open sets. Normal spaces additionally require that any two disjoint closed sets can be separated by disjoint open sets — a strictly stronger condition. There exist Hausdorff spaces that are not normal (the Sorgenfrey plane is a classic example), and Urysohn's Lemma does not apply to them. Normal spaces form a proper subclass of Hausdorff spaces."

- question: "In the proof of Urysohn's Lemma, the dyadic rationals are used because they are dense in [0,1], and this density is what guarantees the function f(x) = inf{r : x ∈ U(r)} is continuous."
  type: true-false
  answer: true
  explanation: "Continuity of f requires that preimages of open sets are open. The nested family U(r) provides open sets indexed by dyadic rationals, which are dense in [0,1]. For any point x and any open interval (a,b) containing f(x), the density of dyadic rationals ensures there exist dyadic rationals r₁ < f(x) < r₂ with (r₁, r₂) ⊂ (a,b), and the sets U(r) then provide the open neighborhood of x whose image lands in (a,b). Without density, there would be gaps in the family where continuity could break down."

- question: "Urysohn's Lemma can be paraphrased as: 'In a normal space, closed sets can be separated by a continuous function.' Why is this stronger than the mere fact that normal spaces have disjoint separating open sets?"
  type: short-answer
  answer: "Separating open sets give two disjoint open neighborhoods — one around each closed set — but say nothing about what happens in between. A continuous separating function must coordinate the topology of the entire space: it must assign values in [0,1] to every point such that the assignment varies continuously everywhere, equaling 0 on one closed set and 1 on the other. Continuity is a global condition (preimages of all open sets must be open), not just a local one. The fact that normality — a condition about separating two closed sets with two open sets — is sufficient to build such a globally continuous function is the non-obvious content of the lemma."
  explanation: "This is why Urysohn's Lemma is described as showing that normality is the 'right' condition for doing analysis in a topological setting: it is exactly strong enough to support function-theoretic arguments. Spaces that are not normal cannot always support such functions, which limits what analysis can be done on them. The lemma also unlocks major consequences: the Tietze Extension Theorem and Urysohn's Metrization Theorem both follow from it."
```

## Explainer

You already know that a **normal space** is one where any two disjoint closed sets can be separated by disjoint open neighborhoods — a strong form of the Hausdorff property. You also know what continuous functions between topological spaces look like. **Urysohn's Lemma** bridges these two ideas in a non-obvious direction: normality is not only a separation property about open sets, it is actually a *function-construction* property. Given two disjoint closed sets F and G in a normal space, you can find a continuous function that maps all of F to 0 and all of G to 1, varying continuously in between.

Why is this surprising? Continuity is a topological condition: preimages of open sets must be open. Building a continuous function from scratch that takes prescribed values on two "far apart" closed sets requires precise coordination of the topology across the entire space. The key to the proof is an inductive construction using **dyadic rationals** — the numbers of the form k/2ⁿ for integers k and n. For each dyadic rational r ∈ [0,1], you construct an open set U(r) satisfying F ⊆ U(r) and U(r) ⊆ U(s) for r < s, with G disjoint from U(1). The normality hypothesis is used at each step to insert a separating open set between the closures. Once all U(r) are built, define f(x) = inf{r : x ∈ U(r)}. The nested structure of the U(r)'s guarantees continuity.

The construction is an elegant iteration: start with U(0) and U(1) separating F from G (using normality once), then insert U(1/2) between them (using normality again), then U(1/4) and U(3/4), and so on. The dyadic rationals are dense in [0,1], so the resulting function f is determined at enough "checkpoints" that it must be continuous everywhere. This is a rare instance where a density argument is used not to find limits, but to construct a function.

Urysohn's Lemma is a cornerstone result with major consequences. It implies the **Tietze Extension Theorem** (continuous functions defined on closed subsets of normal spaces extend to the whole space) and is the key step in proving **Urysohn's Metrization Theorem** (second-countable normal spaces are metrizable). The lemma also reveals that normality is the *right* condition for doing analysis in a topological setting: normal spaces support enough continuous functions to separate points and closed sets, which is the minimum needed for function-theoretic arguments to work.
