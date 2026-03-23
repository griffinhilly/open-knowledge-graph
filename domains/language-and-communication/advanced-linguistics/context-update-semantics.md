---
id: context-update-semantics
title: Context-Update Semantics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: discourse-representation-theory
  type: hard
- id: formal-pragmatics-context
  type: hard
tags:
- pragmatics
- semantics
- context
stage: expert
status: draft
---

# Context-Update Semantics

## Core Idea
Context-update semantics views utterance meaning as how utterances change conversational context. Rather than assigning truth values relative to fixed context, it asks: what is the update effect of this utterance? This framework elegantly handles assertions, questions, and imperatives as different context-update types, explaining why presupposition is fundamentally about context change rather than truth-conditional semantics.

## Questions

```yaml
- question: "In classical truth-conditional semantics, 'The King of France is bald' is false because there is no King of France. In context-update semantics, what is the better description of the problem with this sentence?"
  type: multiple-choice
  options:
    - "The sentence is true in some possible worlds and false in others, so its truth value is indeterminate"
    - "The presupposition that there is a King of France must already be in the common ground for the update to succeed; absent that, the update operation fails before truth-value can be evaluated"
    - "The sentence is false because 'bald' is vague and cannot be evaluated without a contextual standard"
    - "Context-update semantics handles this identically to truth-conditional semantics — both classify it as simply false"
  answer: 1
  explanation: "Context-update semantics reframes presupposition failure as an update operation failure rather than a truth-value problem. The sentence carries the presupposition that there is a King of France. In the framework, a presupposition is a precondition on successful update: this sentence can only update the common ground if its presupposition is already in the common ground. If it isn't, the update operation fails — not because the proposition is false, but because it cannot even be processed. This elegantly explains why presuppositions survive embedding under negation: 'The King of France is NOT bald' still presupposes his existence, because both the affirmative and negative assertions require the same precondition to succeed."

- question: "A speaker asks 'Is it raining?' How does context-update semantics analyze this question compared to the assertion 'It is raining'?"
  type: multiple-choice
  options:
    - "Both utterances propose the same propositional update to the common ground, but questions additionally require confirmation before the update takes effect"
    - "Questions reduce the common ground by removing propositions, while assertions add propositions to it"
    - "Questions transform the common ground into an open issue to be resolved; assertions propose adding a proposition to the common ground"
    - "Questions and assertions are semantically equivalent — both express the same proposition, differing only in grammatical mood"
  answer: 2
  explanation: "Context-update semantics distinguishes speech act types by how they change different dimensions of context. An assertion proposes adding a proposition to the common ground — an additive update. A question doesn't add a proposition; it transforms the common ground into an issue — an open set of possibilities the conversation must now resolve. The common ground shifts from settled knowledge to open inquiry. This framework unifies assertion and question under the single principle of context-change without reducing one to the other, and extends naturally to imperatives, which update the set of obligations on the addressee."

- question: "In context-update semantics, all utterances update the same dimension of context — the propositional content of the common ground."
  type: true-false
  answer: false
  explanation: "This is false — the framework is explicitly multidimensional. Assertions update the propositional content of the common ground. Questions transform it into an issue (an open inquiry the discourse must resolve). Imperatives update a different dimension entirely: the set of obligations or commitments incumbent on the addressee. This multidimensional view is what allows context-update semantics to unify speech act theory with formal semantics through a single organizing principle: every utterance is a context-change instruction, but different utterance types target different dimensions of context and transform them in different ways."

- question: "On the context-update view, presupposition is fundamentally about context change rather than about truth conditions."
  type: true-false
  answer: true
  explanation: "This is the key insight that motivates the framework. Classical truth-conditional semantics struggles with presupposition because it cannot easily explain why 'The King of France is bald' and its negation share the same presupposition despite having opposite truth conditions. In context-update semantics, presupposition is a precondition on the update operation itself: the utterance can only update the common ground if the presupposed information is already there. This explains why presuppositions project through negation, questions, and conditionals — in all these cases, the update is conditioned on the presupposition being satisfied, regardless of how the sentence is embedded."

- question: "What is the 'common ground,' and how does treating assertion as a 'proposal to update' rather than a 'statement of fact' change how we analyze meaning?"
  type: short-answer
  answer: "The common ground is the information mutually accepted by all participants in a conversation — the shared whiteboard of settled propositions that forms the basis for further discourse. Treating assertion as a proposal to update (rather than a display of information) captures the interpersonal, dynamic nature of communication: when I assert something, I am making a bid to change the shared conversational record, which the other participant can accept or reject. This reframing shifts the analysis from 'what proposition does this sentence express?' to 'what does this sentence do to the conversation?' — a fundamentally different question. It explains why the same proposition can function differently depending on what is already in the common ground, why assertions can fail without being false, and why rejection of an assertion leaves the common ground unchanged."
  explanation: "The proposal-to-update model dissolves the puzzle of why communication feels like a cooperative act rather than information transfer. Because assertion is a proposal, it requires the other party's uptake to succeed as a communicative act — the common ground only updates when both parties accept the proposed addition. This makes meaning fundamentally intersubjective rather than a property of sentences alone, and it directly motivates the formalization of the common ground as the central object in the semantics of discourse."
```

## Explainer

From your work in discourse representation theory you know that meaning extends beyond individual sentences — how we interpret an utterance depends on what has been established in the discourse so far. Context-update semantics sharpens this insight into a formal framework. Instead of asking "what proposition does this sentence express?" — the standard truth-conditional move — it asks "what does this sentence *do* to the state of the conversation?" Meaning becomes an operation on context, not an assignment of content to a fixed context.

The key technical notion is the **common ground** — the information mutually accepted by all participants in a conversation. Think of it as a shared whiteboard. When I assert "It's raining," I am not merely expressing a proposition; I am proposing to add that proposition to the whiteboard. If you accept the assertion, the common ground updates. If you reject it, the whiteboard stays the same. This move — treating assertion as a *proposal to update* rather than a *statement of fact* — solves a problem that classical truth-conditional semantics struggles with: it explains why assertion is a speech act, not just a display of information.

**Presupposition** is where context-update semantics becomes particularly powerful. Your prerequisite work in formal pragmatics introduced presupposition as information the speaker takes for granted. In the context-update framework, a presupposition is a *precondition on successful update*: an assertion can only update the common ground if its presuppositions are already part of the common ground. "The King of France is bald" presupposes there is a King of France; if that information isn't on the whiteboard, the update operation fails — not because the proposition is false, but because it cannot even be processed. This explains **presupposition projection** (why presuppositions survive embedding under negation and questions) without any special stipulation.

Questions and imperatives fit naturally into the framework as distinct update types. A question does not add a proposition; it transforms the common ground into an *issue* — an open set of possibilities that the discourse is now tasked with resolving. An imperative updates a different dimension of context: the set of obligations on the addressee. This **multidimensional** view of context — tracking facts, issues, and commitments simultaneously — unifies speech act theory with formal semantics, explaining diverse utterance types through a single principle: every utterance is a context-change instruction, differing in *which* dimension of context it targets and *how* it transforms it.
