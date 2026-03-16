---
id: axiom-of-infinity
title: Axiom of Infinity
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
builds-toward:
- von-neumann-ordinals
- infinite-cardinal-numbers
tags:
- ZFC
- infinity
- natural numbers
- inductive set
stage: formal-systems
status: validated
---

# Axiom of Infinity

## Core Idea
The axiom of infinity asserts the existence of an inductive set: a set I such that ∅ ∈ I and whenever x ∈ I, also x ∪ {x} ∈ I. This guarantees that the natural numbers — identified in the von Neumann encoding with ∅, {∅}, {∅,{∅}}, ... — form a set. Without this axiom, ZF could be modeled entirely by hereditarily finite sets, making infinite mathematics impossible. The axiom of infinity is therefore the gateway to all of transfinite set theory, enabling ordinals, cardinals, and the full hierarchy of infinities.

## How It's Best Learned
Verify explicitly that {∅, {∅}, {∅,{∅}}, ...} is inductive. Observe that the von Neumann natural number n is the set {0, 1, ..., n-1}, so 3 = {0, 1, 2} = {∅, {∅}, {∅,{∅}}}. Reflect on what mathematics would look like without this axiom — only finite sets would exist.

## Common Misconceptions
- The axiom does not directly assert ℕ is a set — it asserts an inductive set exists. The set ω of natural numbers is then defined as the smallest inductive set (carved out by separation).
- 'Inductive' here is a precise set-theoretic property, not the same as 'infinite' in the everyday sense.

## Explainer

From your study of the ZFC axioms, you know that most of them deal with *constructing new sets from existing ones*: pairing combines two sets, union collects their members, power set collects all subsets, separation carves out subsets satisfying a property, replacement applies a function to an existing set. None of these axioms, applied to a starting universe of only finite sets, can ever produce an infinite set. The **axiom of infinity** is the one axiom that reaches beyond the finite by directly asserting the existence of a set that cannot be built by finite construction.

The axiom says: there exists a set I such that ∅ ∈ I and whenever x ∈ I, also x ∪ {x} ∈ I. Such a set is called **inductive**. Starting from ∅, the closure condition generates: ∅ ∪ {∅} = {∅}, then {∅} ∪ {{∅}} = {∅, {∅}}, and so on without end. These generated elements are exactly the **von Neumann natural numbers**: 0 = ∅, 1 = {∅}, 2 = {∅, {∅}}, 3 = {∅, {∅}, {∅,{∅}}}, where each natural number n is the set of all its predecessors {0, 1, ..., n−1}. The axiom of infinity guarantees this entire infinite sequence can be collected into a single set.

The axiom does not directly define ω — it asserts some inductive set I exists. The set ω of natural numbers is then carved out by the **separation axiom**: ω = {x ∈ I : x belongs to every inductive subset of I}. This intersection-of-all-inductive-subsets maneuver extracts the *smallest* inductive set, which is ω. This two-step process is necessary because without first having some inductive set in hand, separation has nothing to apply to. The axiom provides the raw material; separation shapes it precisely.

Without the axiom of infinity, ZF could be modeled entirely by the **hereditarily finite sets** V_ω — every set in this universe is finite, and infinite mathematics is impossible within it. The axiom of infinity is therefore the dividing line between finitary and infinitary set theory. Once ω exists as a set, the power set axiom produces P(ω) (an uncountable set), replacement iterates the ordinal construction into the transfinite, and the full hierarchy of infinite cardinals and ordinals opens up. Every subsequent piece of infinitary mathematics — transfinite induction, cardinal arithmetic, the continuum — ultimately rests on this single axiom's guarantee that one infinite set exists.
