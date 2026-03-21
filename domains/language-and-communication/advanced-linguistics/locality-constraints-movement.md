---
id: locality-constraints-movement
title: Locality Constraints and Movement
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: x-bar-theory
  type: hard
- id: minimalist-program-core-concepts
  type: hard
builds-toward:
- feature-agreement-checking
tags:
- movement
- constraints
- syntax
stage: advanced
status: draft
---

# Locality Constraints and Movement

## Core Idea
Locality constraints restrict how far syntactic elements can move. The principle of Successive Cyclicity requires that A'-movement (like wh-movement) proceed through intermediate phrase markers rather than jumping directly to the final landing site. These constraints reduce the computational complexity of the grammar and account for universal restrictions on which movements are possible.

## How It's Best Learned
Work through examples of why certain wh-questions involve intermediate movement steps. Contrast licit long-distance dependencies with impossible ones, and analyze why intermediate landing sites must be available.

## Common Misconceptions
- Locality constraints are not language-specific stipulations; they follow from deeper principles like phase structure.
- Not all movements are subject to the same constraints; A-movement (NP-movement) and A'-movement (wh-movement) have different locality properties.

## Questions

```yaml
- question: "The sentence 'What did you wonder who bought?' is ungrammatical, while 'What did Mary say that John bought?' is fine. The best explanation for the contrast is:"
  type: multiple-choice
  options:
    - "English prohibits extraction of objects; only subjects can undergo wh-movement"
    - "The embedded question 'who bought ___' occupies the specifier of CP, leaving no intermediate landing site for 'what' to pass through on its way to the front"
    - "Wh-movement is generally prohibited across finite clause boundaries in English"
    - "The second sentence contains too many wh-elements for the grammar to process"
  answer: 1
  explanation: "This is a wh-island violation. Successive-cyclic movement requires an available specifier position at the edge of each CP phase the moving element must cross. In the grammatical sentence, no wh-element blocks the specifier of the embedded CP, so 'what' can pass through it on its way to the matrix. In the ungrammatical sentence, 'who' already occupies the embedded CP specifier, blocking 'what's' intermediate landing site — trapping it inside the island. The constraint follows from phase structure, not from an arbitrary rule about clause types."

- question: "In the Minimalist Program, syntactic movement is best described as:"
  type: multiple-choice
  options:
    - "A single direct dislocation from the base-generated position to the final surface position"
    - "A purely phonological reordering that occurs after syntactic structure is complete"
    - "A series of steps through intermediate phase-edge positions, checking uninterpretable features at each boundary"
    - "A language-specific operation whose properties vary freely across languages"
  answer: 2
  explanation: "Successive cyclicity is the core claim: movement does not 'jump' in one step to its final landing site. Instead, a moving element must pass through the specifier of each CP (and sometimes vP) phase boundary it crosses, checking features at each stop. This architecture has empirical consequences — leaving behind 'footprints' detectable in some languages — and explains island constraints without listing them as stipulations: if an intermediate position is unavailable, the movement is blocked."

- question: "Locality constraints on movement are language-specific rules that English has but many other languages lack."
  type: true-false
  answer: false
  explanation: "Locality constraints follow from general principles of phase structure in the Minimalist Program, not from language-particular stipulations. Similar island effects appear across typologically diverse languages. What varies cross-linguistically is which elements trigger movement and which features drive it — but the requirement that movement proceed through accessible phase edges is universal. This is part of the appeal of the Minimalist framework: it reduces an apparent catalogue of arbitrary constraints to consequences of a more general architecture."

- question: "A-movement (such as subject raising in 'John seems to be happy') and A'-movement (such as wh-movement) obey different locality constraints, with A-movement generally more strictly bounded to its local clause."
  type: true-false
  answer: true
  explanation: "A-movement moves an element to an argument position (like the subject position of a higher clause) and is constrained by strict locality — it cannot cross finite clause boundaries because nominative case and phi-feature checking must happen locally. A'-movement can create long-distance dependencies spanning many clauses, as in complex wh-questions, but is blocked by island environments (wh-islands, complex NP islands, etc.) rather than strict locality. The different locality profiles reflect the different features that drive each movement type and how those features interact with phase structure."

- question: "Why does the Minimalist Program require movement to proceed through successive phase edges rather than allowing a moving element to jump directly from its base position to its final landing site?"
  type: short-answer
  answer: "Phases are domains that are 'spelled out' and become inaccessible to further syntactic operations once the phase is complete. If an element doesn't escape to the phase edge before spell-out, it is frozen inside the phase and cannot be accessed by operations in higher structure. Successive cyclicity follows from this architecture: the only way a lower element can eventually reach a high landing site is to move to the edge of each intervening phase before that phase closes. Direct long-distance displacement would require the higher operation to 'see into' an already-closed phase, which the Phase Impenetrability Condition prohibits."
  explanation: "This design also has the advantage of reducing computational complexity: each operation is local (within a phase), and complex long-distance dependencies arise from the composition of local steps, rather than requiring an unbounded operation that must scan arbitrarily deep into the tree."
```

## Explainer

Locality constraints answer a deceptively simple question: how far can a syntactic element move from where it originates? From your work with X-bar theory, you know that sentences are built from hierarchically nested phrases — NPs, VPs, CPs — each with a head, specifier, and complement. Movement in syntax takes an element from one position in this tree and displaces it to another. Locality constraints are the rules that determine which movements are licit and which are not.

The clearest illustration comes from **wh-movement**. Consider the English question "What did Mary say that John bought?" The wh-word "what" is the object of "bought" at the bottom of the sentence but has moved to the front. Now compare: "What did you wonder who bought?" This is ungrammatical — a **wh-island violation**. "What" cannot move out of an embedded question clause ("who bought ___") across another wh-element. This contrast is not an accident of English idiom; it reflects a deep structural constraint. The embedded question clause forms a boundary that blocks extraction, and similar restrictions appear in virtually every human language that has been studied.

The key theoretical concept is **Successive Cyclicity**: movement does not happen in a single jump from deep in the structure to the final landing site. Instead, a moving element passes through intermediate positions, typically the specifier of each CP (Complementizer Phrase) along the way. In the Minimalist Program's terms, movement is driven by **feature checking** — an element moves to satisfy uninterpretable features in the grammar, and it must check these features at each phase boundary it crosses. The "phase" (typically vP and CP) defines the locality domain: an element must move to the edge of a phase before that phase is "spelled out" and becomes inaccessible to further operations. If an element fails to reach the phase edge in time, it is trapped.

This architecture explains island constraints without listing them as arbitrary rules. A wh-island blocks movement because the specifier of the embedded CP is already occupied by another wh-element — there is no intermediate landing site available at the phase edge. Similarly, a complex noun phrase island ("the man that Mary said left") blocks extraction because the relative clause does not provide an accessible specifier position through which the moving element can pass. What looks like a list of blocking environments all follow from the single requirement that movement proceed through successive phase edges with available specifier positions.

The distinction between **A-movement** (movement to argument positions, like subject raising: "John seems to be happy") and **A'-movement** (movement to non-argument positions, like wh-movement and topicalization) is crucial because they obey different locality properties. A-movement is constrained by a strict locality requirement that prevents it from crossing clause boundaries; A'-movement allows long-distance dependencies but is blocked by the island environments described above. These differences are captured in the Minimalist framework through the features that trigger movement: A-movement checks nominative case and phi-features; A'-movement checks edge features or wh-features. Different features interact differently with phase structure, producing the distinct locality profiles of the two movement types.
