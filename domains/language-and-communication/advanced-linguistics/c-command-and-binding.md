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
stage: expert
status: draft
---

# C-command and Binding Theory

## Core Idea
C-command is a fundamental asymmetric structural relation: node A c-commands node B if every node dominating A also dominates B, but A does not dominate B. Binding theory uses c-command to characterize pronoun distribution (pronouns must be free in their local domain), reflexive distribution (reflexives must be bound locally), and R-expression constraints (R-expressions must be free).

## Questions

```yaml
- question: "In the sentence 'John believes that Mary likes him,' can 'him' refer to John? Why or why not?"
  type: multiple-choice
  options:
    - "No — 'him' is a pronoun and must be free everywhere in the sentence, so it cannot refer to any NP in the sentence"
    - "Yes — 'him' is a pronoun (Principle B), which must be free only in its local domain (the embedded clause); John is outside that domain, so co-reference is permitted"
    - "No — John c-commands 'him' throughout the entire sentence, blocking any co-reference"
    - "Yes — pragmatic plausibility allows 'him' to refer to John regardless of structural constraints"
  answer: 1
  explanation: "Principle B states that a pronoun must be *free* in its local domain — the minimal clause containing it and a potential c-commanding antecedent. Here the pronoun 'him' is in the embedded clause 'Mary likes him.' John sits in the matrix clause, outside this local domain. Since John does not c-command 'him' within the embedded clause, co-reference is grammatically available. Contrast this with *John hurt him* — there, John is in the same clause and c-commands 'him,' blocking co-reference."

- question: "In 'The manager expects John to promote himself,' why can 'himself' not refer to 'the manager'?"
  type: multiple-choice
  options:
    - "Because 'himself' is not licensed by any semantic content in the sentence"
    - "Because Principle A requires 'himself' to be bound locally — its local domain is the embedded infinitival clause where 'John' is the c-commanding NP, not 'the manager'"
    - "Because 'the manager' is too far removed from 'himself' for any c-command relationship to apply"
    - "Because reflexives can only take sentence-initial NPs as antecedents"
  answer: 1
  explanation: "Principle A requires an anaphor (reflexive) to be *bound* — have a c-commanding antecedent — within its local domain. The local domain for 'himself' is the infinitival clause 'John to promote himself.' Within that domain, 'John' c-commands 'himself,' satisfying Principle A. The manager is outside this local domain and therefore cannot bind 'himself.' This shows that binding is determined by tree geometry (local c-command), not linear proximity or semantic plausibility."

- question: "An R-expression like 'the senator' cannot co-refer with any noun phrase that c-commands it, regardless of where in the sentence that noun phrase appears."
  type: true-false
  answer: true
  explanation: "Principle C states that R-expressions (full referring noun phrases) must be *free everywhere* — no c-commanding noun phrase anywhere in the sentence can be co-referential with them. This is why sentences like 'He₁ said that the senator₁ was corrupt' are ungrammatical with co-reference: 'he' c-commands 'the senator' from a higher position. The constraint applies without locality restrictions, unlike the local-domain requirements of Principles A and B."

- question: "C-command is a symmetric relation: if node A c-commands node B, then B necessarily c-commands A as well."
  type: true-false
  answer: false
  explanation: "C-command is explicitly *asymmetric*. A c-commands B if the first branching node dominating A also dominates B, and A does not dominate B. A subject NP c-commands the VP and everything within it, but the VP does not necessarily c-command the subject. This asymmetry is what gives c-command its explanatory power for reference: it captures the directionality of binding — antecedents are structurally higher than the pronouns or reflexives they bind."

- question: "Why is c-command a *structural* account of pronoun distribution, rather than a linear (left-to-right) one, and why does this distinction matter for linguistic theory?"
  type: short-answer
  answer: "C-command is defined entirely on the hierarchical tree structure — it depends on dominance relations, not on which word comes first in the string. This matters because linear order alone fails to predict reference patterns. In languages with different word orders, or in sentences with extraposition and movement, the same structural c-command relations hold and predict the same reference constraints, even when the surface order differs. A purely linear account would incorrectly predict that pronouns preceding their antecedents are always ungrammatical, but 'Near John₁, he₁ saw the snake' is acceptable. The structural account captures the generalization across all word orders and constructions."
  explanation: "The argument that reference constraints are structural rather than linear is one of the core arguments for syntactic theory over purely sequential models of language. C-command generalizes across languages with radically different surface orders, suggesting that the relevant level of description is hierarchical phrase structure, not the observable string. Binding theory is thus an argument not just about pronouns but about the psychological reality of syntactic trees."
```

## Explainer

From your study of X-bar theory, you have a precise way to represent sentence structure: every phrase projects from a head through specifier and complement positions, building up a hierarchical tree. From your study of pronoun reference, you know that pronouns can and cannot refer to nearby nouns in ways that seem patterned but are hard to state without the right formal tools. **C-command** is that tool — a structural relation defined entirely on the tree geometry that unlocks the systematic distribution of pronouns, reflexives, and full noun phrases across languages.

The definition is technical but becomes intuitive once you work through examples. Node A **c-commands** node B if the first branching node that dominates A also dominates B, and A does not dominate B. Think of it spatially: A c-commands everything in its "sibling" subtree — everything that shares A's immediate parent node. If A is high in the tree (say, a subject NP), it c-commands a great deal. If A is deeply embedded in a complement clause, it commands very little. Crucially, this is an *asymmetric* relation: if A c-commands B, it does not follow that B c-commands A. This asymmetry is what makes the relation useful for capturing the directionality of reference constraints.

**Binding theory** uses c-command to state three elegant principles about how different types of noun phrases behave. **Principle A**: an **anaphor** (a reflexive like *himself* or a reciprocal like *each other*) must be bound — must have a c-commanding antecedent — within its local domain (roughly, the minimal clause containing it). This is why *John hurt himself* is grammatical (John c-commands himself in the same clause) but *John thinks that Mary hurt himself* is not (John does not c-command himself locally). **Principle B**: a **pronoun** must be free in its local domain — it *cannot* be bound by a local c-commanding antecedent. This explains why *John hurt him* cannot mean that John hurt himself: *him* is a pronoun and must refer outside the local clause. **Principle C**: an **R-expression** (a full referring noun phrase like *John* or *the senator*) must be free everywhere — it cannot be bound by any c-commanding noun phrase anywhere in the sentence.

These three principles, stated in terms of c-command and local domains, explain an enormous range of facts about reference across languages — not as a list of exceptions but as the output of a small set of structural constraints. The deeper claim is that reference patterns are not semantic or pragmatic but structural: what matters is not meaning or context but tree geometry. A learner who has mastered X-bar representation now has access to one of formal linguistics' most powerful tools: the ability to predict which referential interpretations are grammatically available from the structure of the tree alone.
