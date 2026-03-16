---
id: order-property-instability
title: 'Order Property and Independence Property: Marks of Instability'
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: stability-and-instability-dividing-line
  type: hard
tags:
- order-property
- independence-property
- OP
- IP
- instability
stage: abstract-reasoning
status: draft
---

# Order Property and Independence Property: Marks of Instability

## Core Idea
A theory has the order property if there exists a formula φ(x,y) and sequences realizing all orders on finite sets (φ defines a dense linear order in the variables), and the independence property if φ defines all binary relations on sequences. Theories with OP or IP are unstable. These properties capture different flavors of instability: OP measures 'ordering complexity' while IP measures 'independence complexity'.

## Explainer

From your study of stability theory, you know that **stable theories** are classifiable — their models have a well-behaved structure theory, and types don't multiply uncontrollably. Instability comes in degrees, and the **order property (OP)** and **independence property (IP)** are the two most important structural markers of instability. Each captures a different way a formula can encode combinatorial complexity.

A formula φ(x, y) has the **order property** if there exist elements a₀, a₁, a₂,... and b₀, b₁, b₂,... such that φ(aᵢ, bⱼ) holds if and only if i < j. In other words, φ "defines a linear order" over the index sets: you can read off the order relation i < j directly from which pairs satisfy φ. The archetypal example is the formula x < y in the theory of dense linear orders (DLO): it obviously defines a linear ordering. Whenever a formula has OP, the theory is unstable, because the order encodes infinitely many distinct types — each position in the order is a distinct "cut" that can be isolated as a type over parameters.

A formula φ(x, y) has the **independence property** if for every finite set of elements b₁,...,bₙ and every subset S ⊆ {1,...,n}, there exists an element a such that φ(a, bᵢ) holds if and only if i ∈ S. This means φ can express *arbitrary* set membership patterns — it encodes all 2ⁿ subsets of any n-element set. The independence property is strictly stronger than OP: **IP implies OP** (and hence instability), but not vice versa. The theory of the random graph (the Rado graph) has IP: the edge relation defines all binary relations on any finite set of vertices. The theory DLO has OP but not IP — it encodes linear order but not arbitrary subsets — and belongs to the class of **NIP theories** (theories without the independence property).

The significance for model theory is structural: knowing whether a theory has OP and/or IP immediately tells you where it sits in Shelah's classification hierarchy. **Stable theories** have neither OP nor IP. **NIP theories** have OP but not IP; this class includes valued fields, ordered groups, and o-minimal structures, and admits its own rich theory (generically stable types, dp-rank, etc.). Theories with IP are the most combinatorially complex and resist Shelah-style classification. When you encounter a new theory, testing for OP and IP is often the first step in understanding how much structure its models possess and which classification tools apply.
