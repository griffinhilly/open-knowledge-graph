---
id: syntax-semantics-interface
title: Syntax-Semantics Interface and Compositionality
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: compositional-semantics
  type: hard
- id: minimalist-program-core-concepts
  type: hard
tags:
- syntax
- semantics
- interface
stage: advanced
status: draft
---

# Syntax-Semantics Interface and Compositionality

## Core Idea
The syntax-semantics interface determines how syntactic structures map to semantic representations, ideally with semantic composition mirroring syntactic composition. Challenges arise with non-compositional idioms, scope ambiguities, and phenomena where syntactic and semantic constituents diverge.

## How It's Best Learned
Analyze cases where syntactic structure and semantic composition align perfectly versus cases of non-compositionality (idioms, anaphora); consider mapping rules between syntax and logical form.

## Common Misconceptions
Syntax and semantics are not isomorphic; some semantic phenomena (scope, binding) are determined post-syntactically via logical form derivations.

## Explainer

From compositional semantics you know the **principle of compositionality**: the meaning of a complex expression is a function of the meanings of its parts and their syntactic arrangement. From the Minimalist Program you know that syntactic derivations build phrase markers via Merge and that the output feeds two interface levels — PF (phonological form, the sound side) and LF (**Logical Form**, the meaning side). The syntax-semantics interface is the study of how those two modules connect: what syntactic structure is visible to semantic interpretation, and where the mapping breaks down.

The ideal case is what you might call **transparent compositionality**: syntactic constituency directly mirrors semantic constituency, and semantic rules operate in parallel with syntactic ones. A sentence like *The dog bit the cat* works cleanly: the VP *bit the cat* combines the transitive verb with its object to form a predicate, and the subject combines with that predicate via functional application. The syntactic tree and the semantic derivation tree are isomorphic. When you extend this to quantifiers using **generalized quantifiers** (determiners as relations between sets), it still works cleanly in simple sentences.

The trouble begins with **scope ambiguities**. The sentence *Every student read a book* is ambiguous: either there is one book that every student read (∃ > ∀ reading), or each student read some book or other (∀ > ∃ reading). In the surface syntax, *every student* c-commands *a book*, which predicts only the ∀ > ∃ reading. The Minimalist account posits that quantifiers can undergo **covert movement** (movement at LF that has no phonological reflex) to different scope positions, generating the ambiguity. This is the key move: LF is a syntactic level where interpretive operations — scope, binding, anaphora resolution — are "visible" to semantic rules, even though no overt word order changes occur.

**Binding theory** provides another probe into the interface. Anaphors (*himself*, *themselves*) must be bound within their local domain; pronouns (*him*, *them*) must be free within that domain; R-expressions (*John*, *the professor*) must be free everywhere. These constraints are stated over syntactic configurations — c-command relations — but have semantic consequences (reference determination). When binding patterns seem to deviate (as in some long-distance reflexives in languages like Chinese or Japanese), it raises the question of whether binding is a purely syntactic phenomenon or whether some binding is resolved semantically post-syntactically. **Idioms** provide the limit case of non-compositionality: *kick the bucket* (die) has no compositional semantic derivation from its parts — the meaning is stored as a unit. That such non-compositional expressions exist is not a problem for the architecture, but it marks the boundary of where compositional rules apply. Mapping that boundary — between what syntax feeds directly to semantics and what requires additional interpretive mechanisms — is the central ongoing project of interface research.
