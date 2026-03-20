---
id: semantic-networks-conceptual-organization
title: Semantic Networks and Conceptual Organization
domain: psychology
course: cognitive-psychology
prerequisites:
- id: schema-theory
  type: hard
builds-toward:
- prototype-exemplar-category-learning
- semantic-priming-spreading-activation
tags:
- semantics
- concepts
- networks
- organization
stage: advanced
status: draft
---

# Semantic Networks and Conceptual Organization

## Core Idea
Semantic knowledge is organized as associative networks where concepts (nodes) are connected by relations of meaning and association. Spreading activation models propose that retrieving a concept activates related concepts. Network properties explain semantic priming effects and how knowledge is accessed in long-term memory.

## Explainer

Your prerequisite of schema theory gave you a framework for thinking about structured knowledge: schemas are organized mental representations that package related concepts together and provide default expectations about how the world works. Semantic network models take that intuition and formalize it into a concrete representational architecture. Rather than asking what knowledge feels like from the inside (schemas), network models ask what structure the knowledge must have to explain how quickly and selectively it is accessed.

The basic architecture treats **concepts as nodes** in a graph and **semantic relations as edges** connecting them. Edges can carry different types of relations — IS-A hierarchical links (a robin IS-A bird, a bird IS-A animal), property links (birds HAVE wings, canaries HAVE yellow color), and associative links (bread — butter, doctor — nurse). The classic model from Collins and Quillian (1969) organized knowledge strictly hierarchically: properties shared by a category are stored once at the category level, not redundantly at each member. To verify "a canary has skin," you must traverse the chain: canary → bird → animal (has skin). This predicts that higher-level inferences should take longer — and they do, as the cognitive time cost of traversal is measurable in reaction time.

The key dynamic property of these networks is **spreading activation**: retrieving a concept activates it as a node, and activation spreads outward along edges to neighboring nodes, partially activating them. The activation spreads automatically and in parallel, explaining **semantic priming** — the finding that processing a prime word ("bread") speeds recognition of an associatively related target ("butter"). The mechanism is simple: activating "bread" pre-activates "butter" along their associative link, so when "butter" appears, less activation is needed to reach recognition threshold. This was verified by Meyer and Schvaneveldt's classic lexical decision experiments: "doctor" facilitates "nurse" more than it facilitates "bread," and the degree of facilitation tracks semantic distance in the network.

But simple hierarchical models don't capture everything. The **typicality effect** — the finding that "a robin is a bird" is verified faster than "a penguin is a bird" — requires moving beyond strict IS-A links. **Prototype models** and **connectionist networks** extend the basic architecture to include graded membership and feature-weighted similarity. In these models, a concept is represented as a pattern of feature activation, and category membership is a matter of degree — robins share many features with the prototype bird, penguins share fewer, so the robin connection activates more strongly. Contemporary semantic network research has moved toward large-scale empirical networks derived from free association norms (like the Small World of Words project), which reveal that semantic memory has **small-world network properties**: high clustering (related concepts form tight neighborhoods) combined with short average path length between any two concepts (facilitated by a small number of highly connected "hub" nodes). These structural properties explain how semantic memory can be simultaneously organized and rapidly traversable — the architecture of knowledge supports the speed of thought.
