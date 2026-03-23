---
id: relevance-theory-pragmatics
title: Relevance Theory and Pragmatic Inference
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: formal-pragmatics-context
  type: hard
- id: conversational-implicature
  type: hard
tags:
- pragmatics
- relevance-theory
- inference
stage: expert
status: draft
---

# Relevance Theory and Pragmatic Inference

## Core Idea
Relevance theory proposes that utterance interpretation is driven by search for optimal relevance: listeners assume speakers provide information maximizing cognitive benefit relative to processing effort. This framework explains inferential implicatures and how context guides interpretation.

## How It's Best Learned
Apply Relevance Theory to resolve ambiguities and infer implicatures in real discourse; compare relevance-theoretic explanations with Gricean maxims for cases of divergence.

## Common Misconceptions
Relevance is not subjective preference; it is a technical property of relative cognitive effect to processing cost, formally defined by Relevance Theory.

## Questions

```yaml
- question: "A listener interprets 'Can you pass the salt?' as a request for action rather than a question about the listener's physical capability. Relevance Theory explains this interpretation by:"
  type: multiple-choice
  options:
    - "The listener detects a violation of Grice's maxim of Quantity and generates a repair implicature"
    - "The listener has stored a lexical convention mapping this sentence form directly to requests"
    - "The literal ability-question interpretation requires more processing effort for fewer cognitive effects; the request interpretation delivers higher relevance and is selected first"
    - "The context contains an explicit signal (e.g., a dinner table) that marks the sentence as a request"
  answer: 2
  explanation: "Relevance Theory's interpretation procedure starts with the most accessible interpretation and stops when optimal relevance is achieved. The ability-question reading requires extra processing (assessing whether the person can physically reach the salt, formulating a capacity response) while delivering minimal cognitive effects in context. The request reading connects immediately to the shared mealtime situation, produces actionable cognitive effects, and requires less effort — so it achieves higher relevance and is selected. This is not a deliberate maxim-checking procedure but an automatic cognitive process."

- question: "Which of the following represents a genuine theoretical advantage of Relevance Theory over Grice's Cooperative Principle and its four maxims?"
  type: multiple-choice
  options:
    - "Relevance Theory abandons the idea that communication is inferential, replacing it with a conventional signal model"
    - "Relevance Theory provides more maxims, giving analysts a richer toolkit for explaining implicature"
    - "Relevance Theory replaces four potentially conflicting maxims with a single formally specified principle, eliminating the need for ad hoc adjudication between maxims"
    - "Relevance Theory limits itself to spoken language, where inference is more tractable than in writing"
  answer: 2
  explanation: "Grice's maxims can conflict — being fully informative (Quantity) may conflict with being brief (Manner) — requiring the analyst to adjudicate without a principled basis. Relevance Theory collapses this complexity into one principle: every utterance is interpreted as achieving the greatest cognitive effects relative to processing effort. Additionally, Grice's maxim of Relation ('be relevant') does the most explanatory work but is left formally unspecified; Relevance Theory makes this precise through the concepts of cognitive effects and processing costs."

- question: "In Relevance Theory, 'relevance' is a subjective property — it refers to what the listener personally finds interesting or important at any given moment."
  type: true-false
  answer: false
  explanation: "This is the central misconception the Common Misconceptions section flags. In Relevance Theory, relevance is a technical, formally defined property: the ratio of cognitive effects (changes to a listener's mental representation — new conclusions, strengthened or weakened assumptions) to processing effort (mental cost of parsing, accessing context, computing an interpretation). A stimulus is more relevant if it yields greater effects for less effort. This is not subjective preference — it is a property of how the cognitive system processes information relative to the mental representations already available."

- question: "Relevance Theory predicts that the same utterance can receive different optimal interpretations in different contexts."
  type: true-false
  answer: true
  explanation: "Because context determines what cognitive effects are available from an utterance, the same sentence can achieve optimal relevance through different interpretations depending on the mental representations the listener brings to it. If the listener's background assumptions differ, a different interpretation may yield greater effects for less effort. This under-determination is predicted by the theory — it does not require that every utterance have a single correct interpretation, only that each be understood as aiming for optimal relevance given the contextual resources available."

- question: "Why does Relevance Theory describe pragmatic interpretation as an automatic, cognitively efficient process rather than as deliberate checking of conversational rules?"
  type: short-answer
  answer: "Because the Principle of Optimal Relevance is not a rule speakers consciously follow or listeners consciously check — it describes how the cognitive system operates automatically. The interpretation procedure (start from the most accessible interpretation, stop when optimal relevance is achieved) runs without deliberate maxim-checking because it is a property of the human cognitive architecture's orientation toward relevance. This makes pragmatics continuous with general cognition rather than a domain-specific rule-following system, and it explains why interpretation happens rapidly and without conscious effort in ordinary conversation."
  explanation: "This contrasts with Gricean accounts, where listeners must detect maxim violations, identify which maxim is flouted, and generate implicatures as repairs — a relatively deliberate, multi-step inference. Relevance Theory's unified procedure is cognitively more parsimonious and better matches the speed and automaticity of real-time language comprehension, which occurs faster than conscious rule-checking could plausibly explain."
```

## Explainer

You already know Grice's theory of conversational implicature: speakers generate meaning beyond what is literally said, and listeners recover this meaning by assuming the speaker is following the Cooperative Principle and its maxims (quantity, quality, relation, manner). Relevance Theory, developed by Dan Sperber and Deirdre Wilson in the 1980s, keeps Grice's core insight — that communication is inferential — but replaces his four maxims with a single, more fundamental principle. The claim is that human cognition is oriented toward **relevance**: we preferentially process information that yields the greatest cognitive benefit for the least mental effort. Communication works because speakers know this about listeners, and listeners know that speakers know it.

The technical definition is precise. **Cognitive effects** are changes to a listener's mental representation of the world: a stimulus has cognitive effects if it combines with existing knowledge to yield new conclusions, or if it strengthens or weakens existing assumptions. **Processing effort** is the mental work required to parse an utterance, access context, and compute an interpretation. **Relevance** is the ratio of cognitive effects to processing effort — greater effects for less effort means higher relevance. The **Principle of Optimal Relevance** states that every utterance is interpreted as achieving the greatest relevance the speaker could reasonably achieve, given the speaker's abilities and preferences. This is not a rule speakers consciously follow; it is a description of how the cognitive system operates automatically.

Consider why this improves on Grice. Grice's maxim of Relation ("be relevant") notoriously does the most explanatory work but receives the least formal specification — what counts as "relevant" is left to intuition. Relevance Theory makes this precise. Moreover, Grice's maxims can conflict, requiring ad hoc adjudication; Relevance Theory has only one principle. More importantly, Relevance Theory handles a wider range of phenomena than classical implicature. It explains **lexical pragmatics** — why "Can you pass the salt?" is interpreted as a request and not a question about ability — and **loose use** — why "France is hexagonal" is true enough to assert despite France not being perfectly hexagonal. In both cases, the interpretation selected is the one that delivers the highest relevance: alternative interpretations either require more processing effort (the literal ability-question interpretation) or yield fewer cognitive effects (a pedantically precise interpretation of France's borders).

The key analytical move Relevance Theory provides is the **relevance-guided interpretation procedure**: starting from the most accessible interpretation and stopping when relevance is achieved. This makes pragmatic interpretation not a matter of deliberate maxim-checking but an automatic, cognitively efficient process. It also predicts **under-determination**: a single utterance can be optimal-relevance-interpreted differently in different contexts, because context changes what cognitive effects are available. Your knowledge of formal pragmatics gives you the background to see why this matters — Relevance Theory does not replace truth-conditional semantics but adds an inferential layer above it, explaining how the minimal linguistic meaning of an utterance becomes a full pragmatic interpretation in context. Where Gricean accounts require listeners to detect maxim violations and generate implicatures as repairs, Relevance Theory describes a smoother, unified process in which every step in interpretation is guided by the search for optimal relevance.
