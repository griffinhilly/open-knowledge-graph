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
status: validated
---

# Stationary Sets and Club Filters

## Core Idea
A set S of ordinals is stationary if it intersects every club set (closed and unbounded subset). Club filters are dual to stationary sets and form important filter structures on cardinals. Stationary sets capture a notion of 'generic' behavior in the ordinal hierarchy. Many consistency-strength results depend on the saturation of club filters and stationary partitions.

## How It's Best Learned
Prove that the set of all limit ordinals below κ is stationary in κ. Show that any two stationary sets intersect (club filter is an ultrafilter-like structure). Explore Fodor's lemma: stationary sets admit regressive functions with constant fiber. Apply to large-cardinal properties.

## Common Misconceptions
- Confusing 'stationary' with 'unbounded'; a set can be stationary without being unbounded.
- Overlooking that stationarity is κ-dependent: a set stationary in κ may not be stationary in λ > κ.

## Questions

```yaml
- question: "A set S ⊆ ω₁ contains only successor ordinals and is unbounded in ω₁. Is S stationary in ω₁?"
  type: multiple-choice
  options:
    - "Yes — any unbounded subset of ω₁ is automatically stationary"
    - "No — the set of all limit ordinals below ω₁ is a club, and S (containing only successors) has empty intersection with it"
    - "Yes — S is dense enough to intersect every club because it is unbounded in ω₁"
    - "It depends on whether S has cardinality ω₁"
  answer: 1
  explanation: "The set of all limit ordinals below ω₁ is a club: it is clearly unbounded (limit ordinals occur cofinally) and closed (the limit of a sequence of limit ordinals is itself a limit ordinal). Since S contains only successor ordinals, S ∩ {limit ordinals} = ∅, so S fails to intersect this club. Therefore S is not stationary, despite being unbounded. This shows the key distinction: unbounded means you can find elements arbitrarily high; stationary means you must hit every club, which is a much stronger requirement."

- question: "A function f: S → ω₁ is defined on a stationary set S ⊆ ω₁, with f(α) < α for every α ∈ S. Fodor's lemma concludes:"
  type: multiple-choice
  options:
    - "f is eventually constant on all of S — there exists γ such that f(α) = γ for all sufficiently large α ∈ S"
    - "f is constant on a stationary subset of S — there exists γ < ω₁ such that {α ∈ S : f(α) = γ} is stationary"
    - "f is bounded — there exists β < ω₁ such that f(α) < β for all α ∈ S"
    - "The range of f contains a club subset of ω₁"
  answer: 1
  explanation: "Fodor's lemma (the pressing-down lemma) says: any regressive function on a stationary set is constant on a stationary subset. The full set S need not be sent to a single value — only a stationary portion of it. Option (a) would require constancy on a tail, which is stronger than what the lemma gives. Option (c), boundedness, follows from a simpler argument and does not require stationarity. The power of Fodor's lemma is that it forces a stationary concentration at a single value, which is what makes it useful in combinatorial arguments."

- question: "A set that is stationary in κ remains stationary in any larger regular cardinal λ > κ."
  type: true-false
  answer: false
  explanation: "Stationarity is κ-dependent. A set S ⊆ κ is stationary 'in κ' relative to the clubs of κ. The clubs of λ are subsets of λ, and a club in λ restricted to κ need not be a club in κ, and vice versa. A set can intersect every club in κ while missing some club in λ entirely. This is why one must always specify the ambient cardinal when speaking of stationarity: 'S is stationary in κ' is a well-defined statement, but stationarity does not automatically transfer upward."

- question: "If S is a stationary subset of κ and C is any club in κ, then S ∩ C is non-empty."
  type: true-false
  answer: true
  explanation: "This is the definition of stationarity: S ⊆ κ is stationary if and only if S ∩ C ≠ ∅ for every club C in κ. Equivalently, S cannot be 'avoided' by any club — it is spread throughout κ in a way that no closed unbounded set can dodge it. Non-stationary sets, by contrast, are contained in the complement of some club, meaning some club entirely avoids them."

- question: "State Fodor's lemma (the pressing-down lemma) and explain why it is named a 'pressing-down' lemma."
  type: short-answer
  answer: "Fodor's lemma: if κ is a regular uncountable cardinal, S ⊆ κ is stationary, and f: S → κ is a regressive function (f(α) < α for all α ∈ S with α > 0), then there exists a value γ < κ such that f⁻¹(γ) = {α ∈ S : f(α) = γ} is stationary in κ. The name 'pressing-down' comes from the image of mapping each ordinal α in S to some strictly smaller value f(α) < α — pressing the set downward. The lemma says that this downward pressure must concentrate a stationary portion of S on a single value. It is a pigeonhole principle for the ordinal hierarchy: you cannot disperse a stationary set over many distinct small values without some value receiving stationary mass."
  explanation: "Fodor's lemma is one of the central tools in infinitary combinatorics. It is used to prove properties of stationary sets, to establish regularity of large cardinals, and in forcing arguments. The key application pattern: define a regressive function encoding some combinatorial property, invoke Fodor to get a stationary homogeneous fiber, and use that fiber to build the desired object."
```

## Explainer

From your work with ordinal numbers, you know that limit ordinals are those with no immediate predecessor—ordinals like ω, ω·2, ω², which are approached from below as limits of increasing sequences. A **club set** (short for *closed and unbounded*) in a cardinal κ is a set C ⊆ κ that is closed under such limit operations (if a sequence of elements from C has a supremum below κ, that supremum is also in C) and unbounded (for every β < κ, some element of C exceeds β). Think of a club as a "thick" or "dense" subset of κ: it reaches all the way to κ and contains all its own accumulation points. The prototypical example is the set of all limit ordinals below κ—it is clearly unbounded, and the limit of any sequence of limit ordinals is itself a limit ordinal.

A **stationary set** is defined by its relationship to clubs: a set S ⊆ κ is stationary if it intersects every club. That is, no matter what club C you choose, S ∩ C ≠ ∅. Equivalently, S cannot be "avoided" by any club. This makes stationarity a robustness property: the set is spread throughout κ in a way that no club can dodge it. Non-stationary sets, by contrast, are subsets of the complement of some club—they fit inside a "thin" gap. A key fact is that the intersection of finitely many clubs is again a club, and the intersection of any two stationary sets is not necessarily stationary—but it is not empty (this follows from the club filter structure).

The **club filter** on κ consists of all sets that contain a club, and it forms a proper filter: it is closed under supersets and finite intersections. This filter is not generally an ultrafilter, but it behaves like one in many consistency-strength arguments. The complement of a stationary set is not in the club filter, but its complement is not necessarily stationary either—the two classes can interleave. The most powerful tool for working with stationary sets is **Fodor's Lemma** (the pressing-down lemma): if f: S → κ is a *regressive* function (meaning f(α) < α for all α ∈ S), then f is constant on a stationary subset of S. This is a pigeonhole principle for the ordinal hierarchy—any attempt to "press down" a stationary set must land on a single value for a stationary portion of it.

The significance of stationary sets emerges most fully when you study large cardinals. A cardinal κ is **measurable** if the club filter on κ extends to a κ-complete ultrafilter—essentially, if stationary sets can be "decided" in a coherent way. The question of whether the club filter on ω₁ is *saturated* (every two stationary sets have stationary intersection) is independent of ZFC and connects directly to the existence of large cardinals. Stationary partitions—decomposing κ into many disjoint stationary sets—are central to combinatorial arguments about tree properties and reflection principles, forming the bridge between the combinatorics of infinite cardinals and the consistency strength hierarchy you will explore with measurable cardinals and ultrafliters.
