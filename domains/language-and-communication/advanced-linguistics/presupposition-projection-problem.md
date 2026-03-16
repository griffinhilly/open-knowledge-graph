---
id: presupposition-projection-problem
title: Presupposition and the Projection Problem
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
- id: discourse-representation-theory
  type: hard
tags:
- semantics
- pragmatics
- presupposition
stage: advanced
status: draft
---

# Presupposition and the Projection Problem

## Core Idea
Presuppositions are entailments that survive negation and embedding ('The king of France is bald' presupposes a king exists whether affirmed or denied), yet project selectively—they disappear in some embeddings but not others, creating the projection problem.

## How It's Best Learned
Systematically test presuppositions from definite descriptions, factive verbs, and aspect under negation and embedding; compare frameworks (satisfaction, accommodation, context-change) that predict different projection patterns.

## Common Misconceptions
Presuppositions differ from entailments; they are asymmetric under negation and not asserted content, yet their interpretation depends on context and listener beliefs.

## Explainer

You've already worked through Montague semantics — the compositional, model-theoretic approach that builds sentence truth conditions from lexical entries and syntactic rules. And you've studied **Discourse Representation Theory** (DRT), which extends formal semantics to handle anaphora and discourse-level phenomena by building representations that update incrementally as a discourse unfolds. The projection problem in presupposition is where these tools meet one of the semantics-pragmatics interface's hardest puzzles.

A **presupposition** is a background assumption that a sentence takes for granted and that must hold for the sentence to be felicitous — not merely true or false. "The king of France is bald" presupposes that there is a king of France; if there is none, the sentence is not simply false (as classical logic would have it) — it is defective, or as philosophers say, it suffers a **truth-value gap**. The classic diagnostic is negation: "The king of France is not bald" also presupposes a king of France. Most entailments don't survive negation this way: "John went to Paris" entails John went somewhere, but "John didn't go to Paris" does not. Presuppositions project through negation; regular entailments do not.

The **projection problem** is explaining when presuppositions survive embedding and when they are canceled or weakened. Presuppositions triggered by simple declaratives project reliably. But a conditional like "If the king of France exists, then the king of France is bald" seems to suspend the existential presupposition. A factive verb like "knows" — "John doesn't know that Mary left" — lets the complement presupposition (Mary left) project through negation. A sentence embedded under "maybe" projects the presupposition but with reduced force. Different embedding environments behave differently, and no single rule ("presuppositions always project" or "operators always block them") captures the pattern.

The major frameworks diverge on how to solve this. The **satisfaction theory** (Heim, Karttunen) treats presuppositions as requirements on the discourse context: a sentence's presupposition must be entailed by the context at the point of utterance. In DRT terms, the presupposition introduces a discourse referent that must be linked to an already-available antecedent — or be **accommodated** into the common ground, the listener's silent acceptance of the presupposed content as background. Accommodation explains why presuppositions don't always require prior establishment: a speaker can introduce "My sister called yesterday" without first establishing that they have a sister, and hearers silently update their model. The challenge for any theory is predicting the asymmetric filtering behavior of complex sentences. Working through the projection problem deepens both Montague compositionality and DRT discourse modeling, while revealing that even a fully formal semantics requires a theory of how context shapes meaning.
