---
id: pairing-axiom
title: Axiom of Pairing
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
builds-toward:
- union-axiom
tags:
- pairing
- axiom
- ordered pairs
- Kuratowski
- ZFC
stage: formal-systems
status: draft
---

# Axiom of Pairing

## Core Idea
The axiom of pairing asserts that for any two objects a and b, there exists a set {a, b} containing exactly those two elements. From pairing alone one can form singletons ({a} = {a, a}) and, together with extensionality, construct the Kuratowski ordered pair: (a, b) = {{a}, {a, b}}. This encoding reduces ordered pairs — and therefore relations, functions, and Cartesian products — to pure sets. Without pairing, the ZFC universe could not bootstrap from individual sets to structured collections.

## How It's Best Learned
Start by applying the axiom explicitly: given sets x and y, invoke pairing to obtain {x, y}. Then build the Kuratowski pair and prove the characteristic property: (a, b) = (c, d) if and only if a = c and b = d. This exercise reveals how a seemingly trivial axiom enables the encoding of order within an unordered framework.

## Common Misconceptions
- The axiom does not produce sets of arbitrary size — it only guarantees two-element (or one-element) sets. Larger finite sets require iterated pairing combined with union.
- Ordered pairs are not primitive in ZFC; they are defined objects. The Kuratowski encoding is the standard choice but is not the only possible one.
