---
id: discourse-representation-theory
title: Discourse Representation Theory
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: discourse-analysis
  type: hard
- id: formal-pragmatics-context
  type: soft
builds-toward:
- context-update-semantics
tags:
- pragmatics
- discourse
- formal
stage: advanced
status: draft
---

# Discourse Representation Theory

## Core Idea
Discourse Representation Theory models discourse by building structured Discourse Representation Structures. Each sentence adds referents and conditions; pronouns resolve to established referents. This handles anaphora and presupposition accommodation in extended discourse: 'A woman entered. She was happy' succeeds, but 'A woman entered. She had three children' accommodates missing information.

## Explainer

Your study of discourse analysis and formal pragmatics gave you two things: an understanding that meaning extends beyond the sentence, and some tools for thinking about how context shapes interpretation. **Discourse Representation Theory** (DRT), developed by Hans Kamp in the 1980s, provides the formal architecture that makes those intuitions precise. Its central insight is deceptively simple: to understand a discourse, you don't just interpret each sentence in isolation — you build a running mental model, and each new sentence updates that model.

The formal object DRT introduces is the **Discourse Representation Structure** (DRS), which you can think of as a box containing two things: a list of **discourse referents** (roughly, the individuals the discourse has introduced) and a list of **conditions** (propositions that are true of those referents in the model). When you hear "A farmer owns a donkey," the DRS box gets two new referents — call them *x* (the farmer) and *y* (the donkey) — plus the conditions *farmer(x)*, *donkey(y)*, and *owns(x,y)*. Nothing about this is exotic yet. The payoff comes with anaphora. When the next sentence is "He beats it," the pronouns *he* and *it* need to find antecedents. DRT says they can access the discourse referents already in scope: *he* can pick up *x* (the farmer), *it* can pick up *y* (the donkey). The conditions *beats(x,y)* get added to the same box. The discourse is now a single structured representation rather than two independent sentences.

This matters because it solves the **donkey anaphora** problem — a famous puzzle in formal semantics. "Every farmer who owns a donkey beats it" seems simple, but the pronoun *it* cannot be a simple variable bound by "a donkey" in the scope of "every farmer," because the scoping doesn't work out. DRT handles it elegantly: the indefinite "a donkey" inside the restrictor of "every farmer" introduces a referent that is accessible to the pronoun in the matrix clause, because both are inside the same conditional DRS structure. The box architecture tracks accessibility in a way that standard predicate logic does not.

**Presupposition accommodation** is the other major application. When someone says "A woman entered. She had three children," the second sentence presupposes the existence of three children — information not previously established. Rather than crashing, the discourse interpreter **accommodates** the presupposition by adding the three children as new referents to the DRS, inferring that they must exist because the sentence requires them to. DRT provides a principled account of when accommodation is possible (the presupposition is plausible and consistent with the model) and when it fails. This connects directly to the formal pragmatics you studied: accommodation is the mechanism by which context is dynamically enriched as discourse unfolds. The DRS is not a static representation of a situation; it is the record of an ongoing interpretive process in which each sentence both draws on and updates the shared context that speaker and hearer are building together.
