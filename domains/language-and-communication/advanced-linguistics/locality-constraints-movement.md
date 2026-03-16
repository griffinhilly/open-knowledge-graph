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

## Explainer

Locality constraints answer a deceptively simple question: how far can a syntactic element move from where it originates? From your work with X-bar theory, you know that sentences are built from hierarchically nested phrases — NPs, VPs, CPs — each with a head, specifier, and complement. Movement in syntax takes an element from one position in this tree and displaces it to another. Locality constraints are the rules that determine which movements are licit and which are not.

The clearest illustration comes from **wh-movement**. Consider the English question "What did Mary say that John bought?" The wh-word "what" is the object of "bought" at the bottom of the sentence but has moved to the front. Now compare: "What did you wonder who bought?" This is ungrammatical — a **wh-island violation**. "What" cannot move out of an embedded question clause ("who bought ___") across another wh-element. This contrast is not an accident of English idiom; it reflects a deep structural constraint. The embedded question clause forms a boundary that blocks extraction, and similar restrictions appear in virtually every human language that has been studied.

The key theoretical concept is **Successive Cyclicity**: movement does not happen in a single jump from deep in the structure to the final landing site. Instead, a moving element passes through intermediate positions, typically the specifier of each CP (Complementizer Phrase) along the way. In the Minimalist Program's terms, movement is driven by **feature checking** — an element moves to satisfy uninterpretable features in the grammar, and it must check these features at each phase boundary it crosses. The "phase" (typically vP and CP) defines the locality domain: an element must move to the edge of a phase before that phase is "spelled out" and becomes inaccessible to further operations. If an element fails to reach the phase edge in time, it is trapped.

This architecture explains island constraints without listing them as arbitrary rules. A wh-island blocks movement because the specifier of the embedded CP is already occupied by another wh-element — there is no intermediate landing site available at the phase edge. Similarly, a complex noun phrase island ("the man that Mary said left") blocks extraction because the relative clause does not provide an accessible specifier position through which the moving element can pass. What looks like a list of blocking environments all follow from the single requirement that movement proceed through successive phase edges with available specifier positions.

The distinction between **A-movement** (movement to argument positions, like subject raising: "John seems to be happy") and **A'-movement** (movement to non-argument positions, like wh-movement and topicalization) is crucial because they obey different locality properties. A-movement is constrained by a strict locality requirement that prevents it from crossing clause boundaries; A'-movement allows long-distance dependencies but is blocked by the island environments described above. These differences are captured in the Minimalist framework through the features that trigger movement: A-movement checks nominative case and phi-features; A'-movement checks edge features or wh-features. Different features interact differently with phase structure, producing the distinct locality profiles of the two movement types.
