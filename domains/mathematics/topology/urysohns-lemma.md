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
stage: formal-systems
status: draft
---

# Urysohn's Lemma

## Core Idea
In a normal space, if F and G are disjoint closed sets, there exists a continuous function f: X → [0,1] with f(F) = {0} and f(G) = {1}.

## Explainer

You already know that a **normal space** is one where any two disjoint closed sets can be separated by disjoint open neighborhoods — a strong form of the Hausdorff property. You also know what continuous functions between topological spaces look like. **Urysohn's Lemma** bridges these two ideas in a non-obvious direction: normality is not only a separation property about open sets, it is actually a *function-construction* property. Given two disjoint closed sets F and G in a normal space, you can find a continuous function that maps all of F to 0 and all of G to 1, varying continuously in between.

Why is this surprising? Continuity is a topological condition: preimages of open sets must be open. Building a continuous function from scratch that takes prescribed values on two "far apart" closed sets requires precise coordination of the topology across the entire space. The key to the proof is an inductive construction using **dyadic rationals** — the numbers of the form k/2ⁿ for integers k and n. For each dyadic rational r ∈ [0,1], you construct an open set U(r) satisfying F ⊆ U(r) and U(r) ⊆ U(s) for r < s, with G disjoint from U(1). The normality hypothesis is used at each step to insert a separating open set between the closures. Once all U(r) are built, define f(x) = inf{r : x ∈ U(r)}. The nested structure of the U(r)'s guarantees continuity.

The construction is an elegant iteration: start with U(0) and U(1) separating F from G (using normality once), then insert U(1/2) between them (using normality again), then U(1/4) and U(3/4), and so on. The dyadic rationals are dense in [0,1], so the resulting function f is determined at enough "checkpoints" that it must be continuous everywhere. This is a rare instance where a density argument is used not to find limits, but to construct a function.

Urysohn's Lemma is a cornerstone result with major consequences. It implies the **Tietze Extension Theorem** (continuous functions defined on closed subsets of normal spaces extend to the whole space) and is the key step in proving **Urysohn's Metrization Theorem** (second-countable normal spaces are metrizable). The lemma also reveals that normality is the *right* condition for doing analysis in a topological setting: normal spaces support enough continuous functions to separate points and closed sets, which is the minimum needed for function-theoretic arguments to work.
