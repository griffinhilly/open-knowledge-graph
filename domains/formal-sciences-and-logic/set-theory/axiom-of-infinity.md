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
