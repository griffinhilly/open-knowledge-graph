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
stage: expert
status: draft
---

# Presupposition and the Projection Problem

## Core Idea
Presuppositions are entailments that survive negation and embedding ('The king of France is bald' presupposes a king exists whether affirmed or denied), yet project selectively—they disappear in some embeddings but not others, creating the projection problem.

## How It's Best Learned
Systematically test presuppositions from definite descriptions, factive verbs, and aspect under negation and embedding; compare frameworks (satisfaction, accommodation, context-change) that predict different projection patterns.

## Common Misconceptions
Presuppositions differ from entailments; they are asymmetric under negation and not asserted content, yet their interpretation depends on context and listener beliefs.

## Questions

```yaml
- question: "Consider: (A) 'John stopped smoking.' and (B) 'John didn't stop smoking.' What does this pair reveal about the assumption that John previously smoked?"
  type: multiple-choice
  options:
    - "Both sentences entail that John previously smoked — this is a regular entailment that projects from both the positive and negative"
    - "Both sentences presuppose that John previously smoked — the assumption survives negation, which is the defining diagnostic of presupposition"
    - "Sentence A entails John smoked before; sentence B cancels this, confirming it is an entailment rather than a presupposition"
    - "The assumption is pragmatically implicated by both sentences but is technically neither an entailment nor a presupposition"
  answer: 1
  explanation: "The negation test is the core diagnostic for presupposition. Regular entailments do not survive negation: 'John went to Paris' entails he went somewhere, but 'John didn't go to Paris' does not. Presuppositions do survive: both 'John stopped smoking' and 'John didn't stop smoking' carry the background assumption that John previously smoked. If that assumption fails — he never smoked — both sentences are defective, not simply false. This survival under negation distinguishes presuppositions from ordinary entailments."

- question: "Consider: 'If John has a sister, then John's sister is a doctor.' Does this sentence presuppose that John has a sister?"
  type: multiple-choice
  options:
    - "Yes — 'John's sister' triggers a definite description presupposition that always projects regardless of context"
    - "No — the conditional context filters the presupposition; the sentence merely raises the sister's existence as a hypothetical, suspending the existential claim"
    - "No — presuppositions only arise from factive verbs, not from definite descriptions"
    - "Yes — the presupposition is present but weakened, not blocked"
  answer: 1
  explanation: "This is a classic case of the projection problem. Definite descriptions like 'John's sister' normally trigger an existential presupposition. But when the description appears in the consequent of a conditional whose antecedent establishes exactly that existential condition, the presupposition is filtered — the sentence does not globally commit to John having a sister. This shows that presuppositions do not always project: the embedding environment determines behavior, and no simple rule ('presuppositions always project') captures all cases."

- question: "Unlike regular entailments, presuppositions survive negation — negating a sentence typically leaves its presuppositions intact."
  type: true-false
  answer: true
  explanation: "This is the defining property of presuppositions and the primary diagnostic used to identify them. 'The king of France is bald' and 'The king of France is not bald' both presuppose that France has a king. If France has no king, both sentences are infelicitous — they suffer a truth-value gap. Regular entailments disappear under negation: 'She managed to finish the exam' entails it was difficult, but 'She didn't manage to finish the exam' does not."

- question: "Presuppositions always project out of any embedding environment — conditional, modal, or interrogative — because they are background assumptions rather than asserted content."
  type: true-false
  answer: false
  explanation: "This is the misconception the projection problem directly addresses. Presuppositions project in some environments but are filtered or suspended in others. A conditional like 'If there is a king of France, then the king of France is bald' filters the existential presupposition. A modal like 'Maybe John knows that Mary left' lets the complement presupposition (Mary left) project, but with reduced force. Factive verbs typically project through negation. The point is that different operators treat presuppositions differently — which is precisely what makes the projection problem hard."

- question: "What is the projection problem in presupposition theory, and why does it resist a simple rule?"
  type: short-answer
  answer: "The projection problem is the challenge of predicting when a presupposition projects out of an embedding environment and when it is canceled or suspended. Simple declaratives reliably project their presuppositions. But presuppositions embedded under negation still project, while the same presuppositions embedded under conditionals may be filtered, under 'maybe' project with reduced force, and so on. No single rule — 'presuppositions always project' or 'operators always block them' — captures the asymmetric pattern. Different operators (negation, modals, conditionals, questions) behave differently, and even the same operator can behave differently depending on where in the sentence the presupposition trigger occurs."
  explanation: "Frameworks like satisfaction theory (Heim/Karttunen) try to handle this by requiring presuppositions to be entailed by the local context at each point of evaluation — which allows conditionals to filter when the antecedent provides the needed background. Accommodation handles cases where presuppositions introduce content not already in the common ground. The difficulty is that no framework fully predicts all patterns without residual complexity."
```

## Explainer

You've already worked through Montague semantics — the compositional, model-theoretic approach that builds sentence truth conditions from lexical entries and syntactic rules. And you've studied **Discourse Representation Theory** (DRT), which extends formal semantics to handle anaphora and discourse-level phenomena by building representations that update incrementally as a discourse unfolds. The projection problem in presupposition is where these tools meet one of the semantics-pragmatics interface's hardest puzzles.

A **presupposition** is a background assumption that a sentence takes for granted and that must hold for the sentence to be felicitous — not merely true or false. "The king of France is bald" presupposes that there is a king of France; if there is none, the sentence is not simply false (as classical logic would have it) — it is defective, or as philosophers say, it suffers a **truth-value gap**. The classic diagnostic is negation: "The king of France is not bald" also presupposes a king of France. Most entailments don't survive negation this way: "John went to Paris" entails John went somewhere, but "John didn't go to Paris" does not. Presuppositions project through negation; regular entailments do not.

The **projection problem** is explaining when presuppositions survive embedding and when they are canceled or weakened. Presuppositions triggered by simple declaratives project reliably. But a conditional like "If the king of France exists, then the king of France is bald" seems to suspend the existential presupposition. A factive verb like "knows" — "John doesn't know that Mary left" — lets the complement presupposition (Mary left) project through negation. A sentence embedded under "maybe" projects the presupposition but with reduced force. Different embedding environments behave differently, and no single rule ("presuppositions always project" or "operators always block them") captures the pattern.

The major frameworks diverge on how to solve this. The **satisfaction theory** (Heim, Karttunen) treats presuppositions as requirements on the discourse context: a sentence's presupposition must be entailed by the context at the point of utterance. In DRT terms, the presupposition introduces a discourse referent that must be linked to an already-available antecedent — or be **accommodated** into the common ground, the listener's silent acceptance of the presupposed content as background. Accommodation explains why presuppositions don't always require prior establishment: a speaker can introduce "My sister called yesterday" without first establishing that they have a sister, and hearers silently update their model. The challenge for any theory is predicting the asymmetric filtering behavior of complex sentences. Working through the projection problem deepens both Montague compositionality and DRT discourse modeling, while revealing that even a fully formal semantics requires a theory of how context shapes meaning.
