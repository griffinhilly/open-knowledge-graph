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
stage: advanced
status: validated
---

# Long-Distance Extraction

## Core Idea
Long-distance extraction involves movement across multiple clause boundaries (e.g., 'Who did you say that Mary met?'). Such dependencies are constrained by islands (complex NP island, wh-island, adjunct island) and subjacency effects, though constraints vary crosslinguistically.

## Questions

```yaml
- question: "Which of the following sentences is grammatical, and why does it contrast with the others?"
  type: multiple-choice
  options:
    - "'Who do you wonder whether Mary met?' — extraction from an embedded interrogative is allowed in English"
    - "'Who did you believe the claim that Mary met?' — extraction from a complex NP is permitted through complement clauses"
    - "'Who did she say that Mary met?' — long-distance extraction through a complement clause is grammatical"
    - "'Who did she leave after meeting?' — extraction from an adjunct is allowed when the adjunct is temporal"
  answer: 2
  explanation: "English allows long-distance extraction only through complement clauses — embedded clauses that are direct arguments of verbs like 'say,' 'think,' 'believe.' Option C is grammatical because 'that Mary met' is a complement clause of 'say.' Options A, B, and D involve island environments: 'wonder whether' creates a wh-island (the embedded clause is itself interrogative), 'the claim that' creates a complex NP island, and 'after meeting' is an adjunct island. All three block extraction, producing ungrammaticality under standard subjacency theory."

- question: "Consider the contrast: 'Who do you think left?' (grammatical) vs. 'Who do you think that left?' (degraded in English). Which principle most directly explains the degraded status of the second sentence?"
  type: multiple-choice
  options:
    - "Subjacency: moving 'who' crosses two bounding nodes in the second sentence but only one in the first"
    - "The that-trace effect: a subject trace adjacent to an overt complementizer 'that' violates the Empty Category Principle"
    - "Wh-islands: 'that' creates an interrogative island blocking subject extraction"
    - "Complement clauses block subject extraction regardless of whether 'that' is present"
  answer: 1
  explanation: "The that-trace effect is the classic name for this phenomenon. When 'who' is extracted from the subject position of an embedded clause, leaving a trace immediately following 'that' (an overt complementizer), the result is degraded in English. This is attributed to the Empty Category Principle (ECP): the trace left by extraction of a subject must be properly governed, and an overt 'that' blocks the required government relationship. In 'Who do you think __ left?' the complementizer is absent, allowing proper government of the trace; in 'Who do you think that __ left?' the overt 'that' intervenes, creating the degradation."

- question: "In English, a wh-element can be extracted from an arbitrarily deeply embedded complement clause — spanning any number of clause boundaries — without becoming ungrammatical."
  type: true-false
  answer: true
  explanation: "This is the defining property of long-distance (unbounded) extraction through complement clauses. 'Who did she claim that he believed that Mary had seen?' spans three clause boundaries and remains grammatical because each movement step stops at the intermediate Spec,CP of each complement clause (successive-cyclic movement), crossing only one bounding node per step. The dependency is 'unbounded' in the sense that there is no fixed maximum depth, as long as each intermediate step respects subjacency."

- question: "Island constraints on long-distance extraction are universal: most human languages block extraction from complex NP islands, wh-islands, and adjunct islands in the same way."
  type: true-false
  answer: false
  explanation: "Crosslinguistic variation shows that island constraints are not uniformly universal. Many Scandinavian languages allow extraction from wh-islands that English disallows. Malagasy and other Austronesian languages impose much stronger restrictions on extraction. Some languages permit extraction from adjunct islands under certain conditions. This variation drives ongoing theoretical debate: do all languages share the same underlying constraints with surface differences driven by feature specifications ('strong' vs. 'weak' features), or are the constraints themselves parameterized? The crosslinguistic data suggests neither pure universality nor free variation."

- question: "Why does 'Who did you say that Mary met?' succeed as long-distance extraction while 'Who did you read the claim that Mary met?' fails? What structural difference accounts for the contrast?"
  type: short-answer
  answer: "In 'Who did you say that Mary met?', the gap is inside a complement clause — 'that Mary met' is a direct argument (complement) of 'say,' a transparent extraction domain. In 'Who did you read the claim that Mary met?', the gap is inside a noun complement clause embedded within the complex NP 'the claim that Mary met.' Complex NPs are islands: no element may be extracted from a relative clause or noun complement clause, because the NP constitutes a bounding node that cannot be crossed. The difference is not distance but the structural type of the embedded clause: complement clauses are transparent; complex NPs are barriers."
  explanation: "The complex NP island is one of the most robust extraction constraints across languages. The theoretical explanation varies by framework: in subjacency theory, crossing the NP boundary violates the constraint against crossing more than one bounding node per movement step. In more recent theories, the nominal structure's feature properties block movement through it. Practically, the test is whether the embedded clause is an argument of a verb (extractable) or embedded inside a nominal phrase (island). 'The claim that...' is the latter — the complement clause belongs to the noun 'claim,' not to the matrix verb 'read.'"
```

## Explainer

From your work on wh-movement and island constraints, you know two foundational facts: wh-elements move from their base position to a higher specifier position (Spec,CP), leaving a trace or gap behind; and certain syntactic environments — **islands** — block this movement, producing ungrammaticality. Long-distance extraction extends this picture by asking what happens when the movement isn't just one clause up, but two, three, or more clause boundaries away.

Consider the contrast: "Who did Mary meet?" involves movement within a single clause — "meet who" becomes "who did Mary meet?" entirely within one CP. Now consider "Who did you say that Mary met?" Here the gap for "who" is inside an embedded clause ("Mary met __"), but the wh-word has surfaced at the front of the matrix clause. The dependency crosses a clause boundary. This is **long-distance extraction** (also called **unbounded dependency** or **long-distance wh-movement**). Remarkably, English allows this: the gap can be arbitrarily far from the filler under the right structural conditions. "Who did she claim that he believed that Mary had seen?" is grammatical despite spanning three clause boundaries.

What constrains this long reach is the island typology you already know, now applied recursively. A **complex NP island** blocks extraction: "Who did you read the claim that Mary met?" is ungrammatical — the gap is inside a relative clause or noun complement, an island from which nothing can escape. A **wh-island** blocks it too: "Who do you wonder whether Mary met?" is degraded because the embedded clause is itself interrogative, creating a barrier. An **adjunct island** blocks extraction from inside an adjunct: "Who did she leave after meeting?" is bad in most analyses. The key pattern is that clause-boundary crossing is fine through complement clauses (the embedded clauses of verbs like "say," "think," "believe") but not through island structures.

**Subjacency**, the constraint you studied in island theory, predicts this distribution. Movement may cross at most one bounding node per step; crossing two simultaneously produces a subjacency violation. In long-distance extraction through multiple complement clauses, successive-cyclic movement — stopping at the intermediate Spec,CP of each embedded clause before moving to the next — allows the dependency to build up step by step without violating subjacency at any single move. Evidence for these intermediate positions comes from phonological phenomena in some languages (particles or morphology that surface at each intermediate landing site) and from "that-trace" effects: "Who do you think __ left?" is grammatical, but "Who do you think that __ left?" is degraded in English because the extracted subject would leave a trace adjacent to "that," violating the Empty Category Principle.

Crosslinguistic variation adds an important dimension. Some languages (like Malagasy or certain Austronesian languages) are much more restrictive about extraction; others (like many Scandinavian languages) allow extraction from wh-islands that English disallows. This variation has driven two generations of theoretical debate: do all languages share the same underlying movement constraints with surface variation driven by feature specifications, or are the constraints themselves parameterized? Long-distance extraction is thus not just a curiosity about complex sentences — it is a central testing ground for theories of syntax, locality, and crosslinguistic universals.
