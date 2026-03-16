---
id: long-distance-extraction
title: Long-Distance Extraction
domain: language-and-communication
course: linguistics
prerequisites:
- id: wh-movement-operator-quantification
  type: hard
- id: island-constraints-subjacency
  type: hard
- id: locality-constraints-movement
  type: soft
tags:
- syntax
- movement
- constraints
- locality
stage: formal-systems
status: draft
---

# Long-Distance Extraction

## Core Idea
Long-distance extraction involves movement across multiple clause boundaries (e.g., 'Who did you say that Mary met?'). Such dependencies are constrained by islands (complex NP island, wh-island, adjunct island) and subjacency effects, though constraints vary crosslinguistically.

## Explainer

From your work on wh-movement and island constraints, you know two foundational facts: wh-elements move from their base position to a higher specifier position (Spec,CP), leaving a trace or gap behind; and certain syntactic environments — **islands** — block this movement, producing ungrammaticality. Long-distance extraction extends this picture by asking what happens when the movement isn't just one clause up, but two, three, or more clause boundaries away.

Consider the contrast: "Who did Mary meet?" involves movement within a single clause — "meet who" becomes "who did Mary meet?" entirely within one CP. Now consider "Who did you say that Mary met?" Here the gap for "who" is inside an embedded clause ("Mary met __"), but the wh-word has surfaced at the front of the matrix clause. The dependency crosses a clause boundary. This is **long-distance extraction** (also called **unbounded dependency** or **long-distance wh-movement**). Remarkably, English allows this: the gap can be arbitrarily far from the filler under the right structural conditions. "Who did she claim that he believed that Mary had seen?" is grammatical despite spanning three clause boundaries.

What constrains this long reach is the island typology you already know, now applied recursively. A **complex NP island** blocks extraction: "Who did you read the claim that Mary met?" is ungrammatical — the gap is inside a relative clause or noun complement, an island from which nothing can escape. A **wh-island** blocks it too: "Who do you wonder whether Mary met?" is degraded because the embedded clause is itself interrogative, creating a barrier. An **adjunct island** blocks extraction from inside an adjunct: "Who did she leave after meeting?" is bad in most analyses. The key pattern is that clause-boundary crossing is fine through complement clauses (the embedded clauses of verbs like "say," "think," "believe") but not through island structures.

**Subjacency**, the constraint you studied in island theory, predicts this distribution. Movement may cross at most one bounding node per step; crossing two simultaneously produces a subjacency violation. In long-distance extraction through multiple complement clauses, successive-cyclic movement — stopping at the intermediate Spec,CP of each embedded clause before moving to the next — allows the dependency to build up step by step without violating subjacency at any single move. Evidence for these intermediate positions comes from phonological phenomena in some languages (particles or morphology that surface at each intermediate landing site) and from "that-trace" effects: "Who do you think __ left?" is grammatical, but "Who do you think that __ left?" is degraded in English because the extracted subject would leave a trace adjacent to "that," violating the Empty Category Principle.

Crosslinguistic variation adds an important dimension. Some languages (like Malagasy or certain Austronesian languages) are much more restrictive about extraction; others (like many Scandinavian languages) allow extraction from wh-islands that English disallows. This variation has driven two generations of theoretical debate: do all languages share the same underlying movement constraints with surface variation driven by feature specifications, or are the constraints themselves parameterized? Long-distance extraction is thus not just a curiosity about complex sentences — it is a central testing ground for theories of syntax, locality, and crosslinguistic universals.
