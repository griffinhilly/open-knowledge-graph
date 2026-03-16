---
id: semantic-networks
title: Semantic Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: first-order-logic-ai
  type: hard
- id: graph-theory-fundamentals
  type: soft
builds-toward:
- knowledge-graphs
tags:
- knowledge-representation
- conceptual-networks
- inference
stage: advanced
status: draft
---

# Semantic Networks

## Core Idea
Semantic networks represent knowledge as labeled directed graphs where nodes are concepts and edges represent relationships such as "is-a", "part-of", or "has-property". They enable inheritance (properties of a parent class apply to children) and path-based reasoning, though they are less expressive than first-order logic and can lead to ambiguity in reasoning.

## Explainer

From your study of first-order logic, you know how to represent knowledge using predicates, quantifiers, and logical connectives — statements like ∀x(Bird(x) → CanFly(x)). This is precise and powerful, but it can be unwieldy for representing the kind of everyday knowledge that humans navigate effortlessly: "a robin is a bird," "birds have wings," "wings enable flight." **Semantic networks** represent this same knowledge as a labeled directed graph, where each concept is a node and each relationship is a labeled edge. The statement "a robin is a bird" becomes a node for Robin, a node for Bird, and a directed edge labeled "is-a" connecting them.

The most important feature of semantic networks is **inheritance through the is-a hierarchy**. If Bird has a "has-property" edge to Wings, and Robin has an "is-a" edge to Bird, then Robin automatically inherits the property Wings without needing to state it explicitly. This mirrors how humans organize knowledge taxonomically — you do not need to separately learn that every individual robin has wings, a beak, and feathers. You learn these facts about birds once, and every subclass inherits them. The graph structure from graph theory that you already understand makes this traversal natural: to find what properties a robin has, simply follow "is-a" edges upward and collect "has-property" edges along the way.

Semantic networks excel at representing **default reasoning** with exceptions. The general network might encode that birds can fly, but a specific "is-a" link from Penguin to Bird can override this with an explicit "cannot-fly" property. The convention is that more specific (closer) properties take precedence over inherited ones. This works intuitively for simple hierarchies but becomes problematic with **multiple inheritance** — if an object inherits from two parent classes that assign conflicting values to the same property, the network provides no principled way to resolve the conflict. This ambiguity is one reason semantic networks are considered less expressive than first-order logic, which can represent the same knowledge with explicit quantifiers and exception clauses.

Despite these limitations, semantic networks were foundational to AI knowledge representation and remain influential today. Their direct descendants include modern **knowledge graphs** like those powering search engines and recommendation systems, where billions of entity-relationship-entity triples (essentially semantic network edges) encode facts about the world. The intuitive visual structure makes semantic networks an excellent tool for organizing domain knowledge, even when the formal reasoning tasks require translation into a more rigorous representation.
