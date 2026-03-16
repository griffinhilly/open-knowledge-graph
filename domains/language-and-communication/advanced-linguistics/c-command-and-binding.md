---
id: c-command-and-binding
title: C-command and Binding Theory
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: x-bar-theory
  type: hard
- id: pronoun-reference-clarity
  type: hard
tags:
- syntax
- binding
- anaphora
stage: advanced
status: draft
---

# C-command and Binding Theory

## Core Idea
C-command is a fundamental asymmetric structural relation: node A c-commands node B if every node dominating A also dominates B, but A does not dominate B. Binding theory uses c-command to characterize pronoun distribution (pronouns must be free in their local domain), reflexive distribution (reflexives must be bound locally), and R-expression constraints (R-expressions must be free).

## Explainer

From your study of X-bar theory, you have a precise way to represent sentence structure: every phrase projects from a head through specifier and complement positions, building up a hierarchical tree. From your study of pronoun reference, you know that pronouns can and cannot refer to nearby nouns in ways that seem patterned but are hard to state without the right formal tools. **C-command** is that tool — a structural relation defined entirely on the tree geometry that unlocks the systematic distribution of pronouns, reflexives, and full noun phrases across languages.

The definition is technical but becomes intuitive once you work through examples. Node A **c-commands** node B if the first branching node that dominates A also dominates B, and A does not dominate B. Think of it spatially: A c-commands everything in its "sibling" subtree — everything that shares A's immediate parent node. If A is high in the tree (say, a subject NP), it c-commands a great deal. If A is deeply embedded in a complement clause, it commands very little. Crucially, this is an *asymmetric* relation: if A c-commands B, it does not follow that B c-commands A. This asymmetry is what makes the relation useful for capturing the directionality of reference constraints.

**Binding theory** uses c-command to state three elegant principles about how different types of noun phrases behave. **Principle A**: an **anaphor** (a reflexive like *himself* or a reciprocal like *each other*) must be bound — must have a c-commanding antecedent — within its local domain (roughly, the minimal clause containing it). This is why *John hurt himself* is grammatical (John c-commands himself in the same clause) but *John thinks that Mary hurt himself* is not (John does not c-command himself locally). **Principle B**: a **pronoun** must be free in its local domain — it *cannot* be bound by a local c-commanding antecedent. This explains why *John hurt him* cannot mean that John hurt himself: *him* is a pronoun and must refer outside the local clause. **Principle C**: an **R-expression** (a full referring noun phrase like *John* or *the senator*) must be free everywhere — it cannot be bound by any c-commanding noun phrase anywhere in the sentence.

These three principles, stated in terms of c-command and local domains, explain an enormous range of facts about reference across languages — not as a list of exceptions but as the output of a small set of structural constraints. The deeper claim is that reference patterns are not semantic or pragmatic but structural: what matters is not meaning or context but tree geometry. A learner who has mastered X-bar representation now has access to one of formal linguistics' most powerful tools: the ability to predict which referential interpretations are grammatically available from the structure of the tree alone.
