---
id: open-covers-finite-subcovers
title: Open Covers and Finite Subcovers
domain: mathematics
course: topology
prerequisites:
- id: open-sets-definition-examples
  type: hard
- id: compact-sets
  type: soft
- id: heine-borel-compact-sets
  type: soft
builds-toward:
- sequential-compactness-metric-spaces
tags:
- open-covers
- compactness
stage: advanced
status: validated
---
# Open Covers and Finite Subcovers

## Core Idea
An open cover of K is a collection {Uᵢ} of open sets with K ⊆ ⋃ Uᵢ. A space is compact if every open cover has a finite subcover. Open covers encode 'global' properties: compact spaces cannot be covered by infinitely many 'small' open sets. Compactness is preserved by continuous images and closed subsets of compact spaces.

## Questions

```yaml
- question: "Is the open interval (0,1) compact as a subset of ℝ with the standard topology?"
  type: multiple-choice
  options:
    - "Yes, because it is bounded and any open cover can be reduced to finitely many sets"
    - "No, because the cover {(1/n, 1) : n = 2, 3, 4, ...} has no finite subcover"
    - "No, because (0,1) is not closed, and only closed sets can be compact"
    - "Yes, because every continuous function on (0,1) attains its maximum and minimum"
  answer: 1
  explanation: "The collection {(1/n, 1)} for n ≥ 2 covers (0,1) — every x ∈ (0,1) lies in (1/n, 1) for all large enough n. But no finite sub-collection covers (0,1): any finite collection omits (1/N, 1) for some large N, leaving points near 0 uncovered. So (0,1) fails the compactness definition. Option C conflates closed and compact — closedness is relevant only when the set sits inside a compact ambient space. Option D is false: f(x) = 1/x is continuous on (0,1) but attains no maximum."

- question: "A continuous function f: K → ℝ attains its maximum value on K for every continuous f. What does this tell us about K?"
  type: multiple-choice
  options:
    - "K must be closed, since the maximum must be achieved at a boundary point"
    - "K must be compact, since continuous images of compact sets are compact, and compact subsets of ℝ are closed and bounded"
    - "K must be connected, since attaining a maximum requires no gaps in the domain"
    - "K must be both compact and path-connected, so that the intermediate value theorem also applies"
  answer: 1
  explanation: "The extreme value theorem states that continuous functions on compact spaces attain their maximum and minimum. The key theorem here: continuous images of compact spaces are compact. If f(K) is compact in ℝ, it is closed and bounded, hence contains its supremum — so f attains its maximum. Conversely, if K is not compact, one can find a continuous function that doesn't attain its maximum (as (0,1) shows). Connectedness (options C, D) is needed for the intermediate value theorem, not the extreme value theorem."

- question: "If K is compact and C ⊆ K is closed, then C is compact."
  type: true-false
  answer: true
  explanation: "Given any open cover {Uᵢ} of C, add the open set K\\C (open because C is closed in K) to obtain an open cover of K. Since K is compact, this extended cover has a finite subcover. Remove K\\C from that finite subcover to get a finite sub-collection of the original {Uᵢ} that covers C. So C is compact. This is one of the two main preservation theorems: compact sets pass compactness to their closed subsets."

- question: "Compactness is a metric-space concept, so the same set can be compact under one metric and non-compact under another on the same underlying set."
  type: true-false
  answer: false
  explanation: "Compactness is a topological property defined purely in terms of open sets, making no reference to any metric. The open-cover definition applies in any topological space. It is true that different metrics on the same set can induce different topologies — and a change in topology can change compactness — but the concept itself is topological, not metric. This is precisely why the abstract open-cover definition matters: it works in spaces where no metric exists."

- question: "Explain in your own words why (0,1) fails to be compact while [0,1] is compact. What does this contrast reveal about what compactness captures?"
  type: short-answer
  answer: "(0,1) fails compactness because points can 'escape toward the boundary': the cover {(1/n,1)} has no finite subcover because any finite collection misses points arbitrarily close to 0. [0,1] is compact because its boundary points 0 and 1 are in the set, blocking that escape route; by Heine-Borel, any open cover of [0,1] reduces to a finite one. Compactness captures the absence of any way to 'escape' — to infinity or to a missing boundary point."
  explanation: "Non-compactness corresponds to a kind of leak: you can build covers where finitely many sets are always insufficient because points crowd toward some inaccessible limit. Compactness blocks all such leaks. This is why compactness is so powerful in analysis — it converts infinite coverings into finite ones, enabling extremal arguments (maximum and minimum) that fail on non-compact spaces like (0,1) or all of ℝ."
```

## Explainer

You already know what **open sets** are — sets where every point has a neighborhood entirely contained within the set. An **open cover** of a set K is simply a collection of open sets whose union contains K: think of it as a collection of "patches" that together cover all of K, where each patch is allowed to overlap with others. There is no restriction on how many patches you use or how large they are; an open cover can be infinite, even uncountably so.

**Compactness** is the property that no matter how profligate your initial covering, you can always thin it down to finitely many patches. Formally: K is compact if every open cover of K has a finite subcover — a finite sub-collection that still covers K. This sounds technical, but the intuition is powerful: compact spaces have "no room to escape to infinity or to the boundary." The canonical example to hold in mind is the contrast between (0, 1) and [0, 1] in ℝ. Cover (0, 1) by the intervals (1/n, 1) for n = 2, 3, 4, … Each interval is open, and their union is (0, 1). But no finite sub-collection covers (0, 1) — every finite sub-collection misses points near 0. So (0, 1) is not compact. Cover [0, 1] by the same collection and add (−0.1, 0.1): now the point 0 is covered, and 1 is always covered. By the Heine–Borel theorem, [0, 1] is compact — any open cover reduces to a finite one.

The abstract definition may seem harder to use than Heine–Borel (closed and bounded in ℝⁿ implies compact), but it is essential for working in general topological spaces where no metric exists. The key theorem you should internalize: **continuous images of compact spaces are compact**. If f: K → Y is continuous and K is compact, then f(K) is compact. One spectacular consequence is the extreme value theorem: a continuous function on a compact space attains its maximum and minimum, because the image is compact (and compact subsets of ℝ are closed and bounded, hence contain their supremum and infimum). **Closed subsets of compact spaces are compact** for the same reason: restrict any open cover of the closed subset to an open cover of the whole compact space, extract a finite subcover, and restrict back. These two preservation theorems are the main tools for applying compactness in practice.
