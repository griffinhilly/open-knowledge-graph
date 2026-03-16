---
id: constituent-trees-and-notation
title: Constituent Trees and Formal Notation
domain: language-and-communication
course: linguistics
prerequisites:
- id: symbolic-representation-linguistics
  type: hard
- id: constituency-and-phrases
  type: soft
builds-toward:
- derivation-vs-generation
- x-bar-theory
tags:
- syntax
- representation
- tree-structures
stage: formal-systems
status: draft
---

# Constituent Trees and Formal Notation

## Core Idea
Constituent structure is formally represented as labeled trees where nodes represent phrases and edges represent dominance relations. Notational systems (brackets, indented lists, line diagrams) make trees explicit and computationally processable.

## Explainer

You already know from symbolic representation that linguistic structures can be expressed formally rather than just intuitively, and from constituency and phrases that a sentence is not a flat string of words — it is a **hierarchical structure** in which words group into phrases, and phrases group into larger phrases. Constituent trees are the primary formal tool for making that hierarchy explicit. A tree diagram takes the implicit groupings that a fluent speaker feels and renders them visible, precise, and manipulable.

In a constituent tree, each **node** represents a unit — either a terminal (an individual word) or a non-terminal (a phrase). Non-terminal nodes are **labeled** with their syntactic category: NP for noun phrase, VP for verb phrase, PP for prepositional phrase, S for sentence. The **edges** connecting nodes represent the **dominance relation**: a higher node immediately dominates the nodes directly below it. Domination means containment — the VP node dominates the verb and every element inside the verb phrase. This is structural containment made visible and formal.

Consider "The old man saw the cat." The tree has an S node at the top, which branches into two daughters: an NP ("The old man") and a VP ("saw the cat"). The NP branches further into a determiner, an adjective, and a noun; the VP branches into a verb and another NP. **Bracket notation** encodes the identical structure linearly: [S [NP The old man] [VP saw [NP the cat]]]. Trees are visually clearer for human reading; brackets are easier to type and process computationally. Both representations carry exactly the same structural information — learning to move fluently between them is a core skill.

The power of formal notation becomes clear when you encounter **structural ambiguity**. "I saw the man with the telescope" can have two distinct structures: either "with the telescope" attaches inside the VP (you used the telescope to see him) or inside the NP (he had the telescope). Two different trees, one string of words. The ambiguity that native speakers feel intuitively maps precisely onto two distinct structural descriptions, and drawing both trees makes the source of the ambiguity transparent in a way that prose explanation cannot. Formal notation thus enables systematic reasoning about structure — and provides the foundation for computational parsing and for formal syntactic theories like X-bar theory.
