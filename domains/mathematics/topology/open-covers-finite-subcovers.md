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
builds-toward:
- sequential-compactness-metric-spaces
tags:
- open-covers
- compactness
stage: advanced
status: draft
---

# Open Covers and Finite Subcovers

## Core Idea
An open cover of K is a collection {Uᵢ} of open sets with K ⊆ ⋃ Uᵢ. A space is compact if every open cover has a finite subcover. Open covers encode 'global' properties: compact spaces cannot be covered by infinitely many 'small' open sets. Compactness is preserved by continuous images and closed subsets of compact spaces.

## Explainer

You already know what **open sets** are — sets where every point has a neighborhood entirely contained within the set. An **open cover** of a set K is simply a collection of open sets whose union contains K: think of it as a collection of "patches" that together cover all of K, where each patch is allowed to overlap with others. There is no restriction on how many patches you use or how large they are; an open cover can be infinite, even uncountably so.

**Compactness** is the property that no matter how profligate your initial covering, you can always thin it down to finitely many patches. Formally: K is compact if every open cover of K has a finite subcover — a finite sub-collection that still covers K. This sounds technical, but the intuition is powerful: compact spaces have "no room to escape to infinity or to the boundary." The canonical example to hold in mind is the contrast between (0, 1) and [0, 1] in ℝ. Cover (0, 1) by the intervals (1/n, 1) for n = 2, 3, 4, … Each interval is open, and their union is (0, 1). But no finite sub-collection covers (0, 1) — every finite sub-collection misses points near 0. So (0, 1) is not compact. Cover [0, 1] by the same collection and add (−0.1, 0.1): now the point 0 is covered, and 1 is always covered. By the Heine–Borel theorem, [0, 1] is compact — any open cover reduces to a finite one.

The abstract definition may seem harder to use than Heine–Borel (closed and bounded in ℝⁿ implies compact), but it is essential for working in general topological spaces where no metric exists. The key theorem you should internalize: **continuous images of compact spaces are compact**. If f: K → Y is continuous and K is compact, then f(K) is compact. One spectacular consequence is the extreme value theorem: a continuous function on a compact space attains its maximum and minimum, because the image is compact (and compact subsets of ℝ are closed and bounded, hence contain their supremum and infimum). **Closed subsets of compact spaces are compact** for the same reason: restrict any open cover of the closed subset to an open cover of the whole compact space, extract a finite subcover, and restrict back. These two preservation theorems are the main tools for applying compactness in practice.
