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
stage: expert
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

## Questions

```yaml
- question: "In the sentence 'The cats walk,' which syntactic element acts as the probe in the Agree operation, and which acts as the goal?"
  type: multiple-choice
  options:
    - "The verb 'walk' is the probe; 'the cats' is the goal — the verb searches upward for phi-features to copy"
    - "T (the Tense head, which hosts agreement morphology) is the probe; the DP 'the cats' is the goal — T searches its c-command domain for interpretable phi-features"
    - "The subject 'the cats' is the probe; T is the goal — the subject's interpretable features attract the functional head"
    - "Both T and the verb serve as probes simultaneously — agreement is a symmetric relation"
  answer: 1
  explanation: "In minimalist syntax, T (Tense) carries uninterpretable phi-features (person, number) that must be valued and deleted. It is the probe and searches its c-command domain for a goal with matching interpretable phi-features. The subject DP 'the cats' has interpretable number (plural) and person (third) features — it is the goal. The Agree operation values T's uninterpretable features from the goal and deletes them. The morphological agreement on the verb ('walk' not 'walks' for plural) is the surface reflex of this operation. Agree is asymmetric and directional — probes search, goals are found."

- question: "A language has no overt verbal agreement morphology — verbs never change form based on subject number or person. According to the minimalist Agree framework, what does this most likely imply?"
  type: multiple-choice
  options:
    - "The language has no syntactic agreement at all and features are never checked"
    - "The language may still have Agree operations, but the phi-features on T may be absent or the uninterpretable features may be deleted without any morphological spell-out"
    - "Subjects in this language must always be adjacent to the verb, since Agree requires strict adjacency"
    - "This language cannot be analyzed within the minimalist program"
  answer: 1
  explanation: "Morphological realization is distinct from the syntactic Agree operation. A language without agreement morphology may still perform Agree internally — features are valued and deleted without any overt phonological consequence, or those features simply are not part of that language's functional vocabulary. Chinese, for example, lacks agreement morphology but remains analyzable within minimalism. Overt agreement morphology is one possible surface reflex of Agree, not its definition. Option C is wrong: Agree is bounded by c-command and locality conditions, not adjacency."

- question: "In the minimalist framework, uninterpretable features must be valued and deleted before transfer to the semantic interface because they contribute nothing to meaning."
  type: true-false
  answer: true
  explanation: "This is the core motivation for Agree. Interpretable features (like number on a noun) contribute to semantic interpretation — they encode whether one or many entities are being discussed. Uninterpretable features (like number on a verb) are purely morphological: a verb being 'singular' has no semantic content. If uninterpretable features reach the semantic interface, the derivation crashes because the interface cannot interpret them. This 'full interpretation' requirement is why feature valuation and deletion are syntactically obligatory — agreement is not stylistic but driven by survival to the interfaces."

- question: "Syntactic movement in the minimalist program is triggered by the need to satisfy phrase structure rules, independently of feature-checking requirements."
  type: true-false
  answer: false
  explanation: "In the minimalist program, movement is feature-driven: an element moves only because a feature must be checked that cannot be valued in situ due to locality constraints. When a probe cannot reach its goal within its c-command domain, the goal must move to a position where Agree can apply. There are no movement rules for their own sake — every displacement has a feature-theoretic motivation. This is what unifies wh-movement, subject raising, object shift, and other transformations under a single mechanism (Agree + feature requirements), replacing the earlier stipulated movement rules of GB theory."

- question: "Explain the distinction between interpretable and uninterpretable features, and why this distinction explains why agreement is obligatory rather than optional in languages that have it."
  type: short-answer
  answer: "Interpretable features contribute to meaning at the semantic interface (e.g., plural on a noun encodes multiplicity). Uninterpretable features have no semantic content (e.g., plural on a verb does not characterize the event) and cannot survive to the semantic interface without crashing the derivation. Because the Agree operation that values and deletes uninterpretable features must complete successfully, agreement is obligatory in any language whose functional heads carry such features."
  explanation: "This reframes agreement from a descriptive morphological pattern to a computationally necessary operation. Languages that 'have agreement' have uninterpretable phi-features on functional heads like T; those features must be valued by Agree or the derivation fails at the semantic interface. Languages without agreement morphology either lack those uninterpretable features or have them with no phonological spell-out. The minimalist insight is that the morphological surface pattern (verb changes form) is secondary — the primary phenomenon is the feature-checking requirement, and morphology is just how some languages make it visible."
```

## Explainer

From your study of Merge and the Minimalist Program, you know that syntactic derivations build structure by combining elements according to strict principles, and that the interfaces with phonology and semantics drive what must be computed. Feature agreement sits at the heart of this architecture: it is the mechanism by which elements at a distance "communicate" in the grammar, ensuring that morphological markers on one element reflect properties of another. The classic example is subject-verb agreement in English — the verb *walks* rather than *walk* reflects that its subject is third-person singular. But how does the verb "know" what its subject is, given that they are in different structural positions? In minimalist syntax, the answer is the **Agree** operation.

The crucial insight of minimalist feature checking is the distinction between **interpretable** and **uninterpretable** features. An interpretable feature is one that contributes to meaning at the semantic interface — number on a noun is interpretable because it encodes whether we are talking about one entity or many. An uninterpretable feature contributes nothing to meaning and must be deleted before the derivation reaches the semantic interface — number on a verb is uninterpretable, because a verb being "singular" doesn't mean anything semantically; it is purely a morphological marker. Uninterpretable features are the engine of Agree: they must be valued and deleted, or the derivation **crashes** (fails to produce a grammatical output). This is why agreement is not optional in languages that have it — it is driven by the formal requirement that uninterpretable features cannot survive to the interfaces.

The **Agree** operation works asymmetrically. A **probe** — an element with uninterpretable features — searches its c-command domain for a **goal** — an element with matching interpretable features. When probe finds goal, two things happen: the probe's uninterpretable feature is valued (it takes the value of the goal's interpretable feature) and then deleted before semantic transfer. This is why English subject-verb agreement works: T (the Tense head, which hosts agreement morphology) is the probe; the subject DP is the goal. T searches downward, finds the subject, copies its number and person features, and the morphological agreement is derived. The search is bounded by **locality** — probes cannot reach across certain structural barriers, which predicts precisely the agreement restrictions that linguists observe cross-linguistically.

Why does this matter beyond morphology? Feature checking is the mechanism that drives **movement** in the minimalist framework. When a feature cannot be valued in situ because the goal is not in the probe's c-command domain, the goal must move to a position where Agree can apply. This connects feature checking to the broader architecture of the grammar: syntactic movement is not arbitrary displacement but **feature-driven necessity**. Wh-movement, object agreement in languages where objects trigger verb morphology, and long-distance dependencies all involve probes searching for goals and triggering movement when locality conditions require it. The elegance of the Agree system is that it reduces a wide range of disparate phenomena — morphological agreement, syntactic movement, scope interpretation — to a single operation governed by feature valuation and deletion.
