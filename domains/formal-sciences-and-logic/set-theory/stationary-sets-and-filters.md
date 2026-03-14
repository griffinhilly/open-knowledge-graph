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
