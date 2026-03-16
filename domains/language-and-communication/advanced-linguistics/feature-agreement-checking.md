---
id: feature-agreement-checking
title: Feature Agreement and Checking
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: merge-operation-and-structure-building
  type: hard
- id: minimalist-program-core-concepts
  type: hard
builds-toward:
- null-elements-pro-drop
tags:
- agreement
- features
- minimalism
stage: advanced
status: draft
---

# Feature Agreement and Checking

## Core Idea
In minimalist syntax, agreement is not a symmetrical relation but an asymmetrical checking relation: a probe with uninterpretable features searches for a goal with matching interpretable features. The Agree operation values the probe's features and deletes them before transfer to the interfaces. This replaces earlier transformational accounts of agreement with a feature-checking mechanism that integrates syntax with semantic and phonological interpretation.

## How It's Best Learned
Trace agreement relations in subject-verb agreement and object agreement, identifying which element is the probe and which is the goal. Examine how feature-checking drives syntax when interpretable features require matching.

## Common Misconceptions
- Agreement is not merely a morphological marking; it is a syntactic operation driven by interpretability on the semantic and phonological interfaces.
- Not all matching relations are instances of Agree; some may be allomorphy or post-syntactic processes.

## Explainer

From your study of Merge and the Minimalist Program, you know that syntactic derivations build structure by combining elements according to strict principles, and that the interfaces with phonology and semantics drive what must be computed. Feature agreement sits at the heart of this architecture: it is the mechanism by which elements at a distance "communicate" in the grammar, ensuring that morphological markers on one element reflect properties of another. The classic example is subject-verb agreement in English — the verb *walks* rather than *walk* reflects that its subject is third-person singular. But how does the verb "know" what its subject is, given that they are in different structural positions? In minimalist syntax, the answer is the **Agree** operation.

The crucial insight of minimalist feature checking is the distinction between **interpretable** and **uninterpretable** features. An interpretable feature is one that contributes to meaning at the semantic interface — number on a noun is interpretable because it encodes whether we are talking about one entity or many. An uninterpretable feature contributes nothing to meaning and must be deleted before the derivation reaches the semantic interface — number on a verb is uninterpretable, because a verb being "singular" doesn't mean anything semantically; it is purely a morphological marker. Uninterpretable features are the engine of Agree: they must be valued and deleted, or the derivation **crashes** (fails to produce a grammatical output). This is why agreement is not optional in languages that have it — it is driven by the formal requirement that uninterpretable features cannot survive to the interfaces.

The **Agree** operation works asymmetrically. A **probe** — an element with uninterpretable features — searches its c-command domain for a **goal** — an element with matching interpretable features. When probe finds goal, two things happen: the probe's uninterpretable feature is valued (it takes the value of the goal's interpretable feature) and then deleted before semantic transfer. This is why English subject-verb agreement works: T (the Tense head, which hosts agreement morphology) is the probe; the subject DP is the goal. T searches downward, finds the subject, copies its number and person features, and the morphological agreement is derived. The search is bounded by **locality** — probes cannot reach across certain structural barriers, which predicts precisely the agreement restrictions that linguists observe cross-linguistically.

Why does this matter beyond morphology? Feature checking is the mechanism that drives **movement** in the minimalist framework. When a feature cannot be valued in situ because the goal is not in the probe's c-command domain, the goal must move to a position where Agree can apply. This connects feature checking to the broader architecture of the grammar: syntactic movement is not arbitrary displacement but **feature-driven necessity**. Wh-movement, object agreement in languages where objects trigger verb morphology, and long-distance dependencies all involve probes searching for goals and triggering movement when locality conditions require it. The elegance of the Agree system is that it reduces a wide range of disparate phenomena — morphological agreement, syntactic movement, scope interpretation — to a single operation governed by feature valuation and deletion.
