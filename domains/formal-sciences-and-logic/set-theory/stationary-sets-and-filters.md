---
id: stationary-sets-and-filters
title: Stationary Sets and Club Filters
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: ordinal-numbers-and-order
  type: hard
- id: infinite-cardinal-numbers
  type: soft
builds-toward:
- consistency-strength-large-cardinals
- measurable-cardinals-ultra-filters
tags:
- stationary-sets
- clubs
- filters
- unbounded
stage: formal-systems
status: draft
---

# Stationary Sets and Club Filters

## Core Idea
A set S of ordinals is stationary if it intersects every club set (closed and unbounded subset). Club filters are dual to stationary sets and form important filter structures on cardinals. Stationary sets capture a notion of 'generic' behavior in the ordinal hierarchy. Many consistency-strength results depend on the saturation of club filters and stationary partitions.

## How It's Best Learned
Prove that the set of all limit ordinals below κ is stationary in κ. Show that any two stationary sets intersect (club filter is an ultrafilter-like structure). Explore Fodor's lemma: stationary sets admit regressive functions with constant fiber. Apply to large-cardinal properties.

## Common Misconceptions
- Confusing 'stationary' with 'unbounded'; a set can be stationary without being unbounded.
- Overlooking that stationarity is κ-dependent: a set stationary in κ may not be stationary in λ > κ.

## Explainer

From your work with ordinal numbers, you know that limit ordinals are those with no immediate predecessor—ordinals like ω, ω·2, ω², which are approached from below as limits of increasing sequences. A **club set** (short for *closed and unbounded*) in a cardinal κ is a set C ⊆ κ that is closed under such limit operations (if a sequence of elements from C has a supremum below κ, that supremum is also in C) and unbounded (for every β < κ, some element of C exceeds β). Think of a club as a "thick" or "dense" subset of κ: it reaches all the way to κ and contains all its own accumulation points. The prototypical example is the set of all limit ordinals below κ—it is clearly unbounded, and the limit of any sequence of limit ordinals is itself a limit ordinal.

A **stationary set** is defined by its relationship to clubs: a set S ⊆ κ is stationary if it intersects every club. That is, no matter what club C you choose, S ∩ C ≠ ∅. Equivalently, S cannot be "avoided" by any club. This makes stationarity a robustness property: the set is spread throughout κ in a way that no club can dodge it. Non-stationary sets, by contrast, are subsets of the complement of some club—they fit inside a "thin" gap. A key fact is that the intersection of finitely many clubs is again a club, and the intersection of any two stationary sets is not necessarily stationary—but it is not empty (this follows from the club filter structure).

The **club filter** on κ consists of all sets that contain a club, and it forms a proper filter: it is closed under supersets and finite intersections. This filter is not generally an ultrafilter, but it behaves like one in many consistency-strength arguments. The complement of a stationary set is not in the club filter, but its complement is not necessarily stationary either—the two classes can interleave. The most powerful tool for working with stationary sets is **Fodor's Lemma** (the pressing-down lemma): if f: S → κ is a *regressive* function (meaning f(α) < α for all α ∈ S), then f is constant on a stationary subset of S. This is a pigeonhole principle for the ordinal hierarchy—any attempt to "press down" a stationary set must land on a single value for a stationary portion of it.

The significance of stationary sets emerges most fully when you study large cardinals. A cardinal κ is **measurable** if the club filter on κ extends to a κ-complete ultrafilter—essentially, if stationary sets can be "decided" in a coherent way. The question of whether the club filter on ω₁ is *saturated* (every two stationary sets have stationary intersection) is independent of ZFC and connects directly to the existence of large cardinals. Stationary partitions—decomposing κ into many disjoint stationary sets—are central to combinatorial arguments about tree properties and reflection principles, forming the bridge between the combinatorics of infinite cardinals and the consistency strength hierarchy you will explore with measurable cardinals and ultrafliters.
